# Stage 4 Scope — Contractor Tools Canonical Documentation

**Status:** BUILT (2026-07-18). Unlike Stages 2–3 there was no fresh owner
review; this stage was reconstructed from **existing repository evidence** — the
roadmap contractor-tools branch (`ct-1..ct-4`) and the July work digests
(`data/raw-reports/`), which contain detailed invoice-tool and calendar
architecture decisions. Future/unconfirmed pieces (team coordination) are marked
as such rather than asserted.
**Goal:** everything about Contractor Tools is reconstructable from repository
documentation alone.

## Definition of done

A person or AI who has never seen Contractor Tools can read one folder and
understand — and rebuild — it: what it is (the shared **infrastructure layer**
for invoicing, payment tracking, scheduling, and eventual team coordination),
the 1099 invoice generator and its deterministic architecture, the payment
tracking system, the calendar/scheduling infrastructure, the guiding
build principles (MVP-first, anti-overbuild), and its growth direction.

## Where it lives

```
companies/
  contractor-tools/
    README.md
    00_overview.md               # what it is; the shared infra layer; who it serves
    01_invoice_generator.md      # 1099 invoice tool: features + deterministic architecture
    02_payment_tracking.md       # finance/payment tracking system (ct-4, done)
    03_calendar_infrastructure.md# ICS subscription feeds, multi-platform, auth-renewal (ct-3)
    04_architecture_principles.md# MVP-first, narrow/deterministic, no premature backend (ct-1)
    05_growth_model.md           # current state, remaining work, future team coordination
```

## Guardrails (public-safe — repo is public)

- No invoice amounts, client names, pay rates, or PII — the tools **process**
  that data; this documentation describes the **tools**, not their contents.
- Tech stack details (PHP/OpenRouter parser, pdfmake, ICS) are fine; secrets/keys
  are not.
- Distinguish clearly between **built** (invoice generator, payment tracking,
  calendar feeds) and **future** (robust auth renewal, team coordination,
  validated backend).

## Source material

- `roadmap.json` contractor-tools branch (`ct-1..ct-4`, blockers).
- `data/raw-reports/` digests — invoice generator architecture (narrow,
  deterministic: text → PHP/OpenRouter parse → JSON → review → calc → fixed
  PDF), calendar affirmation scheduler / authorization-renewal service layer,
  1099 generator feature set (payment terms), ICS subscription flows.
- `companies/deadhang-labor/` — Deadhang is the first consumer of these tools
  (invoice system, W-9 workflow reference in docs 03–04).

## Build sequence

1. Scaffold `companies/contractor-tools/` + README + 6 docs. ✅
2. Draft from roadmap + digest evidence; flag future items. ✅
3. Light roadmap sync (add canonical-docs pointer; statuses already current). ✅
4. Update CHANGELOG + CURRENT_STATE. ✅

## Owner-input gaps (fill later, low urgency)

- Confirm the **team-coordination / communication** direction (largely future).
- Confirm whether the **affirmation calendar** should be documented as a Deadhang
  product running on this calendar infrastructure (current treatment) or owned
  here.
