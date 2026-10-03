---
sidebar_position: 3
title: Client
---

# Client

`Client` is the only class most users ever touch. It holds a `requests.Session`, applies the retry policy, calls user-supplied hooks, and raises typed exceptions. Extension is done by passing callables at construction — not by subclassing.

## Constructing a client

```python
from beavercore import Client, RetryPolicy

client = Client(
    base_url="https://api.example.com",
    auth=my_auth,
    refresh=my_refresh,
    retry=RetryPolicy(max_attempts=4),
    throttle=my_throttle,
    observer=my_observer,
    timeout=15.0,
    verify_ssl=True,
    session=None,
)
```

Only `base_url` is required. Every other argument has a sensible default and can be omitted.

## Constructor options

| arg | default | notes |
|---|---|---|
| `base_url` | required | Trailing slash optional. Paths passed to request methods are joined onto this. |
| `auth` | `None` | `(request_kwargs) -> None`. Mutate the dict to attach credentials. |
| `refresh` | `None` | `() -> bool`. Called once on the first 401; return `True` to retry. |
| `retry` | `RetryPolicy()` | See [Retries & Errors](./retries-and-errors). |
| `throttle` | `None` | `() -> None`. Called before every attempt — bring your own rate limiter. |
| `observer` | `None` | `(event_dict) -> None`. Receives lifecycle events. |
| `timeout` | `30` | Seconds. Applied to every request unless overridden per-call. |
| `verify_ssl` | `True` | Set `False` for self-signed internal endpoints. |
| `session` | `None` | Provide a preconfigured `requests.Session` for custom adapters. |

## HTTP methods

Each verb takes a path and the same keyword arguments as `requests.Session.request`:

```python
client.get("/items", params={"page": 1})
client.post("/items", json={"name": "widget"})
client.put("/items/42", json={"name": "renamed"})
client.patch("/items/42", json={"status": "archived"})
client.delete("/items/42")
```

Every method returns a `requests.Response`. The response is only returned when the status is 2xx — any other status either raises or triggers the retry loop.

## Context manager usage

The recommended pattern is a `with` block, which guarantees the underlying session is closed:

```python
with Client("https://api.example.com") as client:
    data = client.get("/thing").json()
# session is closed here
```

Manual lifecycle management is also supported:

```python
client = Client("https://api.example.com")
try:
    data = client.get("/thing").json()
finally:
    client.close()
```

## Supplying a custom session

For adapter-level customization — custom TLS, SOCKS proxies, retry handling at the transport layer — provide a preconfigured `requests.Session`:

```python
import requests
from requests.adapters import HTTPAdapter

session = requests.Session()
session.mount("https://", HTTPAdapter(pool_connections=20, pool_maxsize=100))

client = Client("https://api.example.com", session=session)
```

BeaverCore does not configure urllib3's retry layer — all retry behavior is handled above the session. The session is used purely as a transport.

## Overriding timeout per-call

The `timeout` passed at construction becomes the default. Any single request can override it:

```python
client.get("/slow-endpoint", timeout=120.0)
```

The same applies to `headers`, `params`, and any other keyword accepted by `requests`.
