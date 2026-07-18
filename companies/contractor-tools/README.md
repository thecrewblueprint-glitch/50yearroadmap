# Contractor Tools — Canonical Documentation

**What this is:** the permanent, rebuildable record of Contractor Tools — the
shared **infrastructure layer** that gives contractors integrated tooling for
**invoicing, payment tracking, scheduling, and (eventually) team coordination.**

If you have never seen Contractor Tools, you can read this one folder and
understand — and rebuild — it: what it is, the 1099 invoice generator and its
deterministic architecture, the payment tracking system, the calendar/scheduling
infrastructure, the build principles that keep it from overreaching, and where
it's headed.

## The big picture (as of 2026-07)

Two core pieces are **built and working**: a production-ready **1099 invoice
generator** and a **finance / payment-tracking system**. **Calendar
infrastructure** (ICS subscription feeds across Google/Apple/Outlook) is working,
with **reliable authorization renewal** as the main remaining reliability task.
The guiding discipline is **MVP-first, anti-overbuild** — validate real
requirements before building backend infrastructure.

Deadhang Labor is the **first consumer** of these tools (its invoice system and
records run on them); the tooling is written to generalize to contractors broadly.

## The documents

| Doc | Covers |
| --- | --- |
| [00_overview](00_overview.md) | What it is, the infra-layer role, who it serves |
| [01_invoice_generator](01_invoice_generator.md) | The 1099 invoice tool: features + deterministic architecture |
| [02_payment_tracking](02_payment_tracking.md) | The finance / payment-tracking system |
| [03_calendar_infrastructure](03_calendar_infrastructure.md) | ICS subscription feeds, multi-platform, authorization renewal |
| [04_architecture_principles](04_architecture_principles.md) | MVP-first, narrow/deterministic, no premature backend |
| [05_growth_model](05_growth_model.md) | Current state, remaining work, future team coordination |

## Guardrails (this repo is public)

These tools **process** sensitive data (invoice amounts, client names, pay). This
documentation describes the **tools**, never their contents — no amounts, client
names, pay rates, PII, or secrets. Built vs. future capabilities are clearly
distinguished throughout.
