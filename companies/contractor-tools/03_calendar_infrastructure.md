# 03 — Calendar Infrastructure

**Status:** Documented (feeds working; robust authorization renewal is the main
remaining task — roadmap `ct-3`).

## What it is

The **scheduling / calendar infrastructure** — reliable calendar feeds and the
service layer beneath them. Its first proving ground is a **365-Day Affirmation
Calendar**, a live calendar subscription feed (a Deadhang-branded product that
runs on this infrastructure).

## Working today

- **ICS subscription feeds** — a live subscription calendar.
- **Multi-platform subscription flows** — Google Calendar (with an Android
  workaround), Apple, and Outlook.
- **Edge-case handling** — leap year and day-366 handled in the calendar logic.

## The reliability problem (roadmap `ct-3`)

The scheduler needs **automatic session / authorization renewal inside the
calendar service**, so scheduled event creation does **not** depend on manual
refresh steps. The design direction:

- Calendar operations run through a **service layer** that **verifies access
  before** any `list` / `create` / `update` / `delete` / `batch` action.
- Authorization renewal is automatic, not a manual re-auth the user has to
  remember.

This is the main open reliability item for Contractor Tools — the feeds work, but
unattended scheduling depends on this renewal being robust.

## Design stance

Consistent with the tool philosophy (doc 04): calendar work stays on open
standards (ICS) and a thin, verifiable service layer rather than a heavy backend.
Reliability (authorization that renews itself) is prioritized over feature
breadth.

## Note on ownership

The **affirmation calendar** is treated here as a Deadhang product that runs on
this calendar infrastructure (it also appears in Deadhang's digital-assets and
revenue docs). This documentation covers the **infrastructure**; the product
framing lives with Deadhang. (Owner may later confirm which home is canonical —
see `governance/STAGE_4_SCOPE.md`.)
