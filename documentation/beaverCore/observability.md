---
sidebar_position: 6
title: Observability
---

# Observability

BeaverCore exposes two optional hooks for integrating with logs, metrics, and traces: `observer` for lifecycle events, and `throttle` for client-side rate limiting. Both are plain callables and default to `None` — the fast path pays a single `is not None` check when either is unused.

## `observer` — lifecycle events

The `observer` callable receives a dict for every meaningful moment in the request lifecycle. The dict always contains an `event` key and standard fields (`method`, `url`, `attempt`), plus any fields specific to that event type.

```python
def observer(event: dict) -> None:
    print(event)

client = Client("https://api.example.com", observer=observer)
```

### Event types

| event | fired when | extra fields |
|---|---|---|
| `request` | just before each attempt leaves the client | — |
| `response` | immediately after each response is received | `status` |
| `retry` | the client has decided to retry | `reason` (e.g. `"5xx:503"`, `"rate_limit:429"`, `"network:Timeout"`) |
| `auth_refresh` | after `refresh` returned `True` and before the retry fires | — |

An event dict looks like this:

```python
{
    "event": "retry",
    "method": "GET",
    "url": "https://api.example.com/thing",
    "attempt": 1,
    "reason": "5xx:503",
}
```

### Wiring into logging

```python
import logging

log = logging.getLogger("beavercore")

def observer(event: dict) -> None:
    if event["event"] == "retry":
        log.warning(
            "retrying %s %s (attempt %d) — %s",
            event["method"], event["url"], event["attempt"] + 1, event["reason"],
        )
```

### Wiring into Prometheus

```python
from prometheus_client import Counter, Histogram

requests_total = Counter(
    "http_client_requests_total",
    "HTTP requests attempted",
    ["method", "status"],
)
retries_total = Counter(
    "http_client_retries_total",
    "HTTP request retries",
    ["method", "reason"],
)

def observer(event: dict) -> None:
    if event["event"] == "response":
        requests_total.labels(method=event["method"], status=event["status"]).inc()
    elif event["event"] == "retry":
        retries_total.labels(method=event["method"], reason=event["reason"]).inc()
```

### Wiring into OpenTelemetry

```python
from opentelemetry import trace

tracer = trace.get_tracer("beavercore")
spans: dict[tuple[str, str], trace.Span] = {}

def observer(event: dict) -> None:
    key = (event["method"], event["url"])
    kind = event["event"]
    if kind == "request":
        spans[key] = tracer.start_span(f"{event['method']} {event['url']}")
    elif kind == "response":
        span = spans.pop(key, None)
        if span is not None:
            span.set_attribute("http.status_code", event["status"])
            span.end()
```

## `throttle` — client-side rate limiting

The `throttle` callable is invoked before every attempt. If it blocks, the request is delayed. The contract is intentionally minimal — anything with the shape `() -> None` works, which means any rate-limiting primitive you already have in the project can be dropped in directly.

```python
import threading

semaphore = threading.BoundedSemaphore(10)   # cap concurrent in-flight requests

def throttle() -> None:
    semaphore.acquire()

client = Client("https://api.example.com", throttle=throttle)
```

A simple fixed-rate token bucket:

```python
import time
import threading

class TokenBucket:
    def __init__(self, rate_per_second: float):
        self._interval = 1.0 / rate_per_second
        self._last = 0.0
        self._lock = threading.Lock()

    def __call__(self) -> None:
        with self._lock:
            wait = (self._last + self._interval) - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()

client = Client("https://api.example.com", throttle=TokenBucket(5))   # 5 req/s
```

BeaverCore ships no built-in rate limiter. Different upstreams have different quota shapes — per-second, per-minute, per-user, token-bucket, sliding-window — and most projects already have a suitable primitive (Redis-backed limiter, in-memory semaphore, third-party library). The `throttle` callable lets you compose whichever one fits.

## Combining the two

The observer and throttle work independently; use both at once with no coordination:

```python
client = Client(
    "https://api.example.com",
    auth=my_auth,
    throttle=my_rate_limiter,
    observer=my_metrics_recorder,
)
```

Each hook is called in a predictable order: `throttle` → `auth` → `observer("request")` → the actual HTTP call → `observer("response")` → retry decision → `observer("retry")` (if applicable).
