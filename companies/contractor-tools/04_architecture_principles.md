# 04 — Architecture Principles

**Status:** Documented (the guiding discipline for the whole branch).

These are the standing principles that keep Contractor Tools reliable and prevent
it from overreaching. They apply to every tool in this folder.

## 1. MVP-first / anti-overbuild

The recurring risk is **overbuilding infrastructure before the real requirements
are known.** The standing rule: **validate backend requirements against actual
MVP scope** before building (roadmap `ct-1`). Concretely, the invoice generator's
earlier "enterprise" plan was judged overbuilt and scoped down (`ct-2`). Build the
smallest thing that meets the real need; add scale only when validated.

## 2. Narrow and deterministic

Each tool does one thing well. Calculations are **deterministic and
code-controlled — never AI-controlled** (doc 01). Inputs are parsed and validated,
then reviewed by a human before anything consequential (like invoice totals) is
computed.

## 3. Static / offline-first, no premature backend

Prefer static, offline-capable workflows over servers, databases, and cloud
storage until there is a validated reason to add them. The invoice generator is a
single-file HTML tool with no database; the calendar rides on ICS. This keeps the
tools cheap, durable, and safe (no private storage to protect).

## 4. Stability over drift

Core architectures that work are **protected from drift** (doc 01's invoice
parser/PDF pipeline is explicitly flagged this way). New features are weighed
against the risk of destabilizing a known-good tool.

## 5. Reliability over breadth

Where something is already built (invoicing, payment tracking, calendar feeds),
the priority is making it **reliable** (e.g. self-renewing calendar
authorization, doc 03) before adding new surface area.

## Why these matter

Contractor Tools is infrastructure the business actually depends on. A flashy but
fragile tool is worse than a narrow, boring, reliable one. These principles are
the reason the branch can be "only" a few tools yet genuinely load-bearing.
