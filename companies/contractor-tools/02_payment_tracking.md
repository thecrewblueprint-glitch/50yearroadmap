# 02 — Payment Tracking

**Status:** Documented (built — roadmap `ct-4` completed).

## What it is

A **finance / payment-tracking system** that lets the contractor monitor and
manage payments — what has been invoiced, what is owed, and what has been paid.
Together with the invoice generator (doc 01), it closes the loop from invoicing to
payment.

## Role

- **Monitor payments** — track invoice status through to payment.
- **Manage finances** — support the business's recordkeeping and cash-basis
  accounting (see `companies/deadhang-labor/04_financial_systems.md`).
- **Feed recordkeeping** — payment records support tax and audit readiness.

## Relationship to Deadhang's financial systems

Deadhang Labor's financial systems doc (`04_financial_systems.md`) describes the
business-side use: invoicing, payment/finance tracking, and record retention on a
cash basis. Contractor Tools is the **tooling** behind that — the payment-tracking
capability Deadhang uses. The two are kept consistent: the business doc says
*what the business does*; this doc says *what the tool provides*.

## Public-safe boundary

This document describes the tracking **capability**, not any financial data.
Actual amounts, client names, and pay figures live in the business's private
records — never in this public repository.

## Status

Built and in place (roadmap `ct-4` completed). Remaining Contractor-Tools work is
concentrated in calendar reliability (doc 03) and backend-scope validation
(doc 04), not in payment tracking.
