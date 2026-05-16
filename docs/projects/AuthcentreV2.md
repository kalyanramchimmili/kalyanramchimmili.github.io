---
title: AuthCentre v2
description: A small JWT auth service in Django — access + refresh tokens, Google/GitHub OAuth, and a dev console to watch the auth flow happen.
tags: [Django, DRF, JWT, OAuth, Python]
---

# AuthCentre v2

A small JWT auth service I built in Django over a few weekends — access + refresh tokens, Google and GitHub OAuth, and a dev console that lets you watch the tokens tick. Code is in [the repo](https://github.com/kalyanramchimmili/AuthcentreV2).

## How it started

 In a tech meet at our org, one team was explaining how they rewrote their whole auth to oauth 2.0. That weekend at Starbucks with a Java Chip Frappuccino — I started actually watching youtube on: what a JWT is, how you sign one, how OAuth 2.0 plugs into Google and GitHub.

This isn't new tech, but it was new to me in this shape. At work I write APIs for network automation with basic auth against our AD servers, which is more than enough for an internal tool. I wanted to know how the *external* world does it. Hence AuthCentre v2 — v1 is the internal one at work, for anyone wondering.

## How I built it

Spun up an empty Django project, registered a fresh `auth_app`, pulled in PyJWT, and started wiring things up.

### JWTs

PyJWT's `encode` / `decode` are about as simple as it gets. HS256 was the default I picked — most common signing algo for this kind of thing. The other family (RS256, ES256) uses public/private key pairs and is what microservices reach for so each service only needs the *public* key to verify, no shared secret. The asymmetric model is neat to know about.

A JWT is three parts: a header (algo + type), a payload (`uid`, `email`, `role`, `iat`, `exp`), and a signature computed with the secret. Decoding gives back the payload plus built-in checks for expiry and tampering — which is the whole point of using a signed format instead of just stuffing data into a session cookie. Please feel free to skip if you find this basic.

Models for users, serializers, DRF views, URL wiring. The interesting bits were the token functions: a UUID for refresh, a real signed JWT for access.

### Access vs. refresh

Two tokens with different jobs:

- **Access** — short-lived (15 min), sent on every request, stateless to verify.
- **Refresh** — long-lived (24 h), sent rarely, stored hashed in the DB.

Every refresh call issues a fresh pair and rotates the row. If both tokens ever get stolen, the access expires in 15 min and the refresh is single-use after rotation, so the blast radius is bounded.

The refresh token rides as an `HttpOnly` cookie — invisible to JavaScript, so an XSS bug on the page can't extract it. Plus `SameSite=Strict` blocks cross-origin sends, which closes off the CSRF angle. The browser auto-sends it, server reads it 🫂.

Logout deletes the matching DB row. Session nuked. Expired refresh rows get cleaned up opportunistically on every refresh call — could be a cron, but at this scale, fine.

### OAuth: Google + GitHub

Registered apps on both consoles to get client IDs and secrets. The flow is the same shape for both providers, give or take a few quirks:

1. User clicks "Continue with Google" → backend redirects to Google's authorize URL with `client_id`, `redirect_uri`, and `state`.
2. User approves, provider redirects back with a `code`.
3. Backend POSTs `code + client_id + client_secret` to the token endpoint, gets back an access token. **The provider's** access token, not mine — used only to fetch the profile.
4. Backend hits the userinfo endpoint, gets name + email. If the email already exists in my `Users` table, link to that user. Otherwise create a new row.
5. Mint *my* JWT + refresh, set the cookie, redirect to the dashboard.

GitHub has two quirks worth flagging:

- The token endpoint returns form-urlencoded by default, so you have to send `Accept: application/json` to get JSON back.
- If a user's email is private, `/user` returns `email: null`. Fix: hit `/user/emails`, pick the entry where both `primary` and `verified` are true. No verified primary → auth fails. I don't want accounts created for unverified emails.

### State for CSRF

In step 1, the backend generates a UUID, stashes it in `request.session`, and ships it as the `state` query param. In the callback, I pop it back out and compare to whatever the provider echoed. Mismatch = reject.

Without state, an attacker could prep a callback URL with their own `code`, bait a victim into clicking it, and silently link the victim's browser session to the *attacker's* identity. State binds each callback to one specific browser session. Didn't know about this until my senior software agent flagged this as a issue 🙂, which is wild Tbh.

### The "trapped in OAuth" thing

The thing I always found annoying about apps like Spotify — log in once with Google and you're stuck with it. No way to add a password later and use email login.

Fixed it on AuthCentre with a "Set password" section on the dashboard:

- **OAuth user with no password yet** — just `new` + `confirm`. The hash gets written to the user row. Email login now works for them.
- **User with an existing password** — `current` + `new` + `confirm`. Current is verified, new is set. Standard change-password UX.

One endpoint, two branches based on whether `password_hash` is null. The serializer makes `old_password` optional; the view enforces it for users who already have one.

### Dev console

A small UI: copy the access token, watch the countdown to expiry tick down, refresh button to swap tokens, activity log of every call. Nothing fancy — just enough to *see* the auth flow happen instead of poking at it with curl.

For the actual code: [github.com/kalyanramchimmili/AuthcentreV2](https://github.com/kalyanramchimmili/AuthcentreV2).

-- Thanks for reading, have a great day!!