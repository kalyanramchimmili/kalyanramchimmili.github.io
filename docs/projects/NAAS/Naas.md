---
title: NAAS
description: A self-service network automation gateway built at work — DNS, firewall, load balancers, and switches behind one Django API.
tags: [Django, DRF, Python, Network Automation]
---

# NAAS

NAAS stands for **Network as a Service**, and the whole point of it is this: developers shouldn't have to raise a ticket and wait around just because their app needs a DNS record or a port opened. They hit an API, they get what they need, we are saved from doing mundane tasks.

It's a big one, so it lives in its own section. **Each module — DNS, firewall, load balancers, switches, public DNS — gets its own page underneath**. This page is the lay of the land.

This isn't a weekend project, it's the thing I actually get paid to do. So there's no public repo to link. But why am I discussing it here? It's a project I built from scratch (with some guidance ofc), first project to run in prod serving real workflows, people 🤝.

## What it looks like underneath

A Django + DRF service. Same stack as half the internal tooling around here — it first started out in Flask. When it started getting bigger, I had to adopt Django. Every time I ran Flask it would say "not suited for production systems" ofc, hence the shift to a better framework. Functionally it's an API gateway hiding bunch of different vendors and complexity on its backend. 


- An **internal DNS appliance** for A / CNAME / PTR / TXT records inside the network
- A **public DNS provider** for anything that has to be reachable from the internet
- A **load balancer** that also happens to be the advanced firewall in front of the infra — the main wall, basically
- A separate **firewall vendor** at the edge
- A **switch vendor** for the L2 / L3 fabric

Each of those is its own NAAS module and gets its own page in this section. But before any of them make sense, there are two things that show up *everywhere* and are worth pulling out first.

## What's common across modules

### Auth

NAAS uses the *original* AuthCentre — the v1 sitting in production here, which I mention in the [AuthCentre v2](../AuthcentreV2.md) post. (v2 is the weekend rewrite I did for fun. v1 is the one actually keeping the lights on.) It accepts basic auth, which validates against AD servers to fetch resource groups.

Multiple resource groups were created during the start of NAAS, each group with its own set of unique permissions aimed at different tasks. NAAS validates the user's groups against it to perform auth — it's stateful.

### Logs & notifications

Two destinations for every action:

- **Logs** to the central log aggregator. That's the system of record — if something exploded two weeks ago, that's where I'm headed.
- **Notifications** to a Teams channel as a live feed, and where it matters, to an email DL. Less for forensics, more so the team sees DNS records being created and deleted scroll past in real time.

More on the email side under the firewall module, which is the chattiest of the lot by a long way.

### Database

We started with SQLite, it was simple, but as the project kept getting bigger — and with the shift to Django, with its amazing ORM that hid all the SQL queries we had to write — we shifted to Postgres. Honestly, it's amazing. What makes it even better is the Django admin panel, which lets me view records via the UI and modify them — life couldn't get any easier than this 🫂.