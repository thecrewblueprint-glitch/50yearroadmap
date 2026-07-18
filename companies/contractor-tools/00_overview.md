# 00 — Overview

**Status:** Documented.

## What it is

Contractor Tools is the **shared infrastructure layer** of the ecosystem — the
practical software a working contractor needs to run the business side of the
job:

- **Invoicing** — generate professional invoices (doc 01).
- **Payment tracking** — monitor and manage what's owed and paid (doc 02).
- **Scheduling / calendar** — reliable calendar feeds and scheduling
  infrastructure (doc 03).
- **Team coordination** — communication and coordination as teams grow (future,
  doc 05).

## Ultimate goal

Provide contractors with **integrated tools for invoicing, payment tracking,
calendar management, and team communication** — the operational back office, kept
lightweight and reliable.

## Who it serves

- **Deadhang Labor first.** Deadhang is the first real consumer: its invoice
  system, payment records, and scheduling run on these tools (see
  `companies/deadhang-labor/` docs 03–04). Deadhang is the proving ground.
- **Contractors broadly, over time.** The tooling is written to generalize beyond
  a single operator as the need is validated.

## Current stage

**Foundation working, disciplined about scope.** The invoice generator and
payment tracking are built; calendar infrastructure works with authorization-
renewal reliability as the main open item. The defining principle is
**MVP-first / anti-overbuild** — don't build backend infrastructure before the
real requirements are known (doc 04).

## Where it sits in the ecosystem

Contractor Tools is the **operational plumbing** beneath the other branches:
Deadhang runs the business on it, and as the labor engine grows (team
deployment), the coordination tools grow with it. It is infrastructure, not a
public-facing product in its own right.
