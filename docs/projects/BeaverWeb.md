---
title: BeaverWeb 🦫
description: A tiny Python web framework I wrote from a raw socket up — v0.1, decorators, path params, Jinja2, no WSGI.
tags: [Python, HTTP, Sockets, Jinja2, Web Framework, PyPI]
---

# BeaverWeb 🦫

A small Python web framework I built weekend by weekend, currently at v0.1. On PyPI as [`beaverweb`](https://pypi.org/project/beaverweb/), source in [the repo](https://github.com/kalyanramchimmili/beaverWeb).

## How it started

I was recently watching a [YouTube playlist on backend from first principles](https://www.youtube.com/watch?v=0Rwb4Xmlcwc&list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1), where the presenter talks about what frameworks hide. He only really covers what HTTP is, but I wanted to go deeper into what frameworks *actually* hide, so I decided to write one myself. Around the same time I watched *Hoppers* and picked up how beavers build dams piece by piece — a framework felt similar, building it up step by step. That's where the name came from: beaverWeb.

The frameworks I use at work — Flask, Django — parse the request for me, sort out the routing, and hand me a `request` object.

## How I built it

As an initial effort I started learning about sockets and HTTP — how to parse a request line, decode and encode headers, handle bodies. After that I looked at how Flask and Django solve the same things and took a bit from each.

From there the pieces came in one at a time:

- **Splitting request parsing.** `Request.parse_header(bytes)` returns a `Request`, then `attach_body(body)` fills in the body separately — so the two-phase read has a clean two-phase API.
- **Path parameters.** Routes moved from a dict keyed on path to a list of `(method, segments, handler)`. A segment wrapped in `{...}` is a wildcard captured into `req.path_params`. First-registered wins, so `/users/me` has to be registered before `/users/{id}` or `me` gets treated as an id.
- **405 with an Allow header.** If the path matches but the method doesn't, the response is 405 instead of 404, with an `Allow` header listing every method that *is* registered on that path.
- **Concurrency.** A `ThreadPoolExecutor` behind `app.run(max_workers=…)`, default 50. Every accepted connection gets submitted to the pool instead of blocking the accept loop.
- **Tiered exception handling.** `ConnectionError`/`TimeoutError` log at debug (client dropped, not our problem), `OSError` at warning, everything else at error. Stopped drowning real bugs in "client dropped" noise.
- **Templates.** Jinja2 rendering via `app.render_template("welcome.html", …)`, with a `FileSystemLoader` that checks the user's `templates/` folder first and falls back to a package-internal one.
- **Zero-config defaults.** `beaver/templates/{welcome,404,500}.html` and `beaver/static/beaverWeb.png` ship inside the wheel, so a fresh `pip install beaverweb` has a working welcome page and styled 404/500 without any setup. `App.__init__` also registers a `beaver_version` Jinja global so templates can render it with no handler kwargs.

## What's not there yet

No WSGI/ASGI compliance, no middleware chain, no type-hint validation, no chunked transfers. Middleware is what I want to add next, and type hints and chunked transfers are things I'd want in future versions. This could all change as I go.

## Documentation

Official docs live in this same portfolio site — source in [`/documentation/beaverWeb/`](https://github.com/kalyanramchimmili/kalyanramchimmilli/tree/main/documentation/beaverWeb) of this repo, rendered at [kalyanramchimmili.github.io/documentation/beaverWeb/introduction](https://kalyanramchimmili.github.io/documentation/beaverWeb/introduction).

## What I picked up

Learnt a lot about HTTP parsing and sockets, how Jinja templating works, HTTP methods and status codes, packaging for PyPI, and GitHub Actions with trusted publishing. And a lot more that I'll pick up as I keep adding to it.

- For more information on the project refer :- https://github.com/kalyanramchimmili/beaverWeb

`I wanted to publish this on PyPI because I have a plan to publish more projects under the beaver family name — this was my first project on that path.`
