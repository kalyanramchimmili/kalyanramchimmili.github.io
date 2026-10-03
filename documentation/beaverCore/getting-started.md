---
sidebar_position: 2
title: Getting Started
---

# Getting Started

## Install

```bash
pip install beavercore
```

This installs `requests` as a dependency. No other third-party packages are required.

## Your first client

```python
from beavercore import Client

with Client("https://api.github.com") as client:
    response = client.get("/users/octocat")
    print(response.json()["login"])
```

The `Client` is a context manager — it opens a connection pool on entry and closes it on exit.

## Attaching credentials

Pass an `auth` callable that mutates the request kwargs. It runs before every attempt, so a refreshed token takes effect immediately:

```python
TOKEN = "ghp_..."

def auth(request_kwargs: dict) -> None:
    request_kwargs.setdefault("headers", {})["Authorization"] = f"Bearer {TOKEN}"

with Client("https://api.github.com", auth=auth) as client:
    me = client.get("/user").json()
```

See [Authentication](./auth) for the refresh pattern that handles stale tokens.

## HTTP methods

Every standard HTTP verb is exposed as a method on the client:

```python
client.get("/items")
client.post("/items", json={"name": "widget"})
client.put("/items/1", json={"name": "renamed"})
client.patch("/items/1", json={"status": "archived"})
client.delete("/items/1")
```

Each method accepts the same keyword arguments as `requests.Session.request` — `params`, `json`, `data`, `headers`, `files`, `timeout`, etc. The return value is a `requests.Response`.

## What happens on failure

The client handles the common failure modes automatically:

- **5xx and network errors** are retried with exponential backoff.
- **429 Too Many Requests** is retried honoring the `Retry-After` header.
- **401 Unauthorized** triggers an optional refresh callable, then one retry.
- **4xx** (other than 401) raises immediately — these aren't fixed by retrying.

When retries are exhausted or an unrecoverable status is received, the client raises a typed exception that carries the response, status code, and attempt count:

```python
from beavercore import Client, TransientError

try:
    with Client("https://api.example.com") as client:
        client.get("/thing")
except TransientError as e:
    print(f"gave up after {e.attempts} attempts ({e.last_reason})")
```

See [Retries & Errors](./retries-and-errors) for the full behavior and the exception hierarchy.

## Next steps

- [Client](./client) — constructor options and the full request surface
- [Retries & Errors](./retries-and-errors) — `RetryPolicy`, retry rules, exception types
- [Authentication](./auth) — `auth` and `refresh` callables
- [Observability](./observability) — hooking into retries and emitting metrics
