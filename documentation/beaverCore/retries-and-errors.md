---
sidebar_position: 4
title: Retries & Errors
---

# Retries & Errors

BeaverCore retries only genuinely retryable failures, exposes a small typed exception hierarchy, and leaves the retry policy itself as an immutable `RetryPolicy` dataclass that can be shared across clients.

## What counts as retryable

| Outcome | Behavior |
|---|---|
| 2xx | Returned to the caller. |
| 401 (first time, refresh set) | Refresh callable runs; if it returns `True`, retry the request once. |
| 401 / 403 (otherwise) | Raise `AuthError` immediately. |
| 429 | Retry honoring `Retry-After`; raise `RateLimitError` if retries exhaust. |
| 500 / 502 / 503 / 504 | Retry with exponential backoff; raise `TransientError` if retries exhaust. |
| 4xx (other) | Raise `HttpError` immediately. These aren't fixed by retrying. |
| Network error / timeout | Retry with exponential backoff; raise `TransientError` if retries exhaust. |

4xx errors other than 401 are never retried — they signal a problem with the request itself, not a transient upstream condition.

## `RetryPolicy`

```python
from beavercore import RetryPolicy

policy = RetryPolicy(
    max_attempts=3,
    backoff_base=0.5,
    backoff_cap=30.0,
    jitter=0.5,
)
```

`RetryPolicy` is a frozen dataclass — construct once, pass to any number of clients. All fields have defaults; override only what you need.

| field | default | meaning |
|---|---|---|
| `max_attempts` | `3` | Total attempts including the first. `1` disables retries. |
| `backoff_base` | `0.5` | Seconds. Multiplier for `2 ** attempt`. |
| `backoff_cap` | `30.0` | Seconds. Upper bound on any single sleep. |
| `jitter` | `0.5` | `0` = deterministic. `1` = add up to a full `backoff_base` of random jitter. |

The sleep duration for a given attempt is:

```
delay = min(backoff_base * 2 ** attempt, backoff_cap)
     + random.uniform(0, jitter * backoff_base)
```

With defaults, that produces delays of roughly 0.5s, 1.0s, 2.0s, 4.0s… up to the 30-second cap.

## 429 handling

When a 429 is received, the client prefers the server's `Retry-After` header over its own backoff curve:

- If `Retry-After` is a numeric value (seconds), sleep for that duration — capped at `backoff_cap` to prevent runaway sleeps on misbehaving servers.
- If `Retry-After` is absent or unparseable, fall back to the exponential backoff formula.

When all attempts exhaust on 429, `RateLimitError` is raised with the last `Retry-After` value exposed as `.retry_after` so the caller can decide whether to wait and retry at the application level.

## Exception hierarchy

```
HttpError                base — carries .status, .response, .attempts
├── AuthError            401/403 (extra: .refresh_attempted)
├── RateLimitError       429 after retries exhausted (extra: .retry_after)
└── TransientError       5xx or network fault, retries exhausted (extra: .last_reason)
```

Every exception carries three fields from the base class:

- `.status` — the HTTP status code, or `None` for network failures.
- `.response` — the raw `requests.Response`, or `None` for network failures.
- `.attempts` — the total number of attempts made before raising.

`.status_code` is also provided as an alias for compatibility with code that expects the attribute name used by `requests`.

Each subclass adds one field specific to why it was raised:

- `AuthError.refresh_attempted` — `True` if the refresh callable ran and still failed.
- `RateLimitError.retry_after` — the parsed `Retry-After` value from the last response, in seconds, or `None`.
- `TransientError.last_reason` — a short tag such as `"5xx:503"` or `"network:Timeout"`.

Non-retryable statuses that don't fit `AuthError`, `RateLimitError`, or `TransientError` (for example 404, 418, 400) raise the base `HttpError`.

## Catching the right thing

Most callers only need to handle a few cases:

```python
from beavercore import AuthError, HttpError, RateLimitError, TransientError

try:
    response = client.get("/thing")
except AuthError:
    # token invalid or revoked — surface to the user
    raise
except RateLimitError as e:
    # upstream told us to back off further than our policy allows
    schedule_retry_after(e.retry_after)
except TransientError:
    # upstream is unhealthy — fall back or alert
    raise
except HttpError as e:
    # non-retryable 4xx (404, 400, 422, …)
    log.warning("request failed with %s", e.status)
    raise
```

`HttpError` is the common base, so a single `except HttpError` catches everything the client can raise.
