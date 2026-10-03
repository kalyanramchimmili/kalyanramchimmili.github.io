---
sidebar_position: 1
title: Introduction
---

# BeaverCore

BeaverCore is a lightweight HTTP client wrapper on top of `requests`. You bring the URL and the credentials — the client handles retries with backoff, 429 rate-limit compliance, one-shot session-token refresh on 401, typed exceptions, connection pooling, and an observability hook. Downstream clients become endpoint code and nothing else.

## Features

- Automatic retries with exponential backoff and jitter on 5xx and network failures
- `Retry-After`-aware handling of 429 responses
- One-shot session refresh on 401 via a user-supplied callable
- Typed exception hierarchy that carries status, response, and attempt count
- Pluggable auth, throttle, and observer callables — no subclassing required
- Context manager interface for connection pooling and cleanup

## Requirements

- Python 3.10 or newer

## Install

```bash
pip install beavercore
```

## Links

- **GitHub:** [kalyanramchimmili/beaverCore](https://github.com/kalyanramchimmili/beaverCore)
- **PyPI:** [pypi.org/project/beavercore](https://pypi.org/project/beavercore/)

Continue to [Getting Started](./getting-started) to build your first client.

## License

BeaverCore is released under the MIT License.

```
MIT License

Copyright (c) 2026 Kalyan Ram Chimmili

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OF THE SOFTWARE.
```
