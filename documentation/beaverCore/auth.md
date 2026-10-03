---
sidebar_position: 5
title: Authentication
---

# Authentication

BeaverCore does not know what kind of credentials your API uses. Authentication is supplied through two callables that run at the right moment in the request lifecycle: `auth` attaches credentials to every outgoing request, and `refresh` recovers from a stale session.

## `auth` — attach credentials to every request

The `auth` callable receives the dict of keyword arguments about to be passed to `requests.Session.request`. Mutate it in place to add headers, query parameters, or anything else. It runs before every attempt, so a credential rotated between attempts takes effect immediately.

**Bearer token:**

```python
TOKEN = "ghp_..."

def auth(request_kwargs: dict) -> None:
    request_kwargs.setdefault("headers", {})["Authorization"] = f"Bearer {TOKEN}"

client = Client("https://api.github.com", auth=auth)
```

**Basic auth:**

```python
import base64

def auth(request_kwargs: dict) -> None:
    creds = base64.b64encode(b"user:pass").decode()
    request_kwargs.setdefault("headers", {})["Authorization"] = f"Basic {creds}"
```

**API key as a query parameter:**

```python
def auth(request_kwargs: dict) -> None:
    request_kwargs.setdefault("params", {})["api_key"] = API_KEY
```

The callable is responsible for merging into existing values — `setdefault("headers", {})` ensures the dict exists without clobbering a per-call `headers` override.

## `refresh` — recover from a stale session

When the client receives a 401 and a `refresh` callable is configured, it is called exactly once. Its return value controls what happens next:

- Return `True` → the client retries the original request once with the (presumably) refreshed credentials.
- Return `False` → the client raises `AuthError` immediately.

```python
def login() -> str:
    # exchange a long-lived credential for a short-lived session token
    return exchange_refresh_token()

def refresh() -> bool:
    global TOKEN
    TOKEN = login()
    return True

client = Client("https://api.example.com", auth=auth, refresh=refresh)
```

Because `auth` runs before every attempt and reads the current `TOKEN`, the retry picks up the new credential automatically.

## Why refresh runs only once

A misconfigured refresh function could otherwise turn a single failed request into an infinite loop of refresh calls. BeaverCore's one-shot policy guarantees:

- **Bounded blast radius.** If `refresh` itself is broken, the error surfaces immediately rather than after N retries.
- **Refresh is expensive.** Most upstreams charge for refresh calls — a rate-limit budget, a database write, an OAuth round-trip. The client makes exactly one such call per request.
- **Terminal failures are visible.** If the retry also 401s, `AuthError` is raised with `refresh_attempted=True` so the caller knows the refresh was tried and still failed.

## Full example — a GitHub client

```python
import os

from beavercore import Client, RetryPolicy


def github_client(token: str) -> Client:
    def auth(request_kwargs: dict) -> None:
        headers = request_kwargs.setdefault("headers", {})
        headers["Authorization"] = f"Bearer {token}"
        headers.setdefault("Accept", "application/vnd.github+json")
        headers.setdefault("X-GitHub-Api-Version", "2022-11-28")

    return Client(
        base_url="https://api.github.com",
        auth=auth,
        retry=RetryPolicy(max_attempts=4),
    )


with github_client(os.environ["GITHUB_TOKEN"]) as gh:
    me = gh.get("/user").json()
    print(f"logged in as {me['login']}")
```

The entire file is business logic. All retry handling, 429 compliance, and error classification is inherited from the client.
