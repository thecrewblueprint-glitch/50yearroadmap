# 05 — Growth Model

**Status:** Documented.

## Current state

Two core tools are **built and in place** — the 1099 invoice generator (doc 01)
and the payment-tracking system (doc 02) — and the calendar infrastructure
(doc 03) works via ICS subscription feeds. The branch is disciplined about scope
(doc 04): it deliberately has *few* tools, each reliable, rather than a broad
fragile suite.

## Remaining work

- **Reliable calendar authorization renewal** (roadmap `ct-3`) — the main open
  reliability item: automatic session/authorization renewal in the calendar
  service so scheduled events don't depend on manual refresh.
- **Validate backend requirements against MVP scope** (roadmap `ct-1`) — decide
  what backend, if any, is actually needed before building it.

## Future direction

- **Team coordination / communication.** The ultimate goal includes team
  communication tools. This is **largely future** — it becomes relevant as
  Deadhang grows from solo work to deploying teams (see
  `companies/deadhang-labor/10_growth_model.md` and roadmap `dh-3`/`dh-4`). Scope
  it when team deployment is real, not before (per the anti-overbuild principle).
- **Generalize beyond Deadhang.** As the tools prove out on Deadhang, they can be
  offered to contractors more broadly — again, when the need is validated.

## The through-line

Contractor Tools grows **reliability-first and demand-pulled**: harden what
exists, validate before building, and let real need (especially Deadhang's team
growth) pull new capability into existence — never speculative infrastructure.

## Status snapshot

| Piece | State |
| --- | --- |
| 1099 invoice generator | Built (MVP-scoped) |
| Payment tracking | Built |
| Calendar feeds (ICS, multi-platform) | Working |
| Calendar authorization renewal | Remaining (`ct-3`) |
| Backend-scope validation | Remaining (`ct-1`) |
| Team coordination / communication | Future (pull with team deployment) |
