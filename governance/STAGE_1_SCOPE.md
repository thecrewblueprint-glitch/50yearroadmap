# Stage 1 Scope — Deadhang Labor LLC Canonical Documentation

**Status:** scaffolded + first-pass drafted (`companies/deadhang-labor/`, all 12
docs). Remaining: fill the "To confirm" items with owner input, and finish the
in-progress docs (safety, contractor framework) as that work lands.
**Goal:** everything about Deadhang Labor LLC is reconstructable from repository
documentation alone.

## Definition of done

A person or AI who has never seen the business can read one folder and
understand — and rebuild — Deadhang Labor LLC: what it is, how it's legally
structured, what it sells, how it operates end to end, its systems and assets,
its contracts, its brand, its revenue streams, and its growth plan. No outside
context required, except deliberately-private material (see guardrails).

## Where it lives (proposed)

A new top-level folder, one per company as the repo becomes a multi-company
command center:

```
companies/
  deadhang-labor/
    README.md              # index + one-paragraph "what this is"
    00_overview.md
    01_legal_structure.md
    02_services.md
    03_operations.md
    04_financial_systems.md
    05_contracts_legal.md
    06_safety.md
    07_digital_assets.md
    08_brand.md
    09_revenue_streams.md
    10_growth_model.md
    11_compliance_and_risk.md
```

(Stage 2 = `companies/crew-blueprint/`, Stage 3 = `companies/production-atlas/`,
same pattern.)

## The canonical document set

| Doc | Covers | Primary source today | Status |
| --- | --- | --- | --- |
| 00_overview | One-page: mission, what Deadhang does, who it serves, current stage | roadmap Deadhang branch, DECISION_LOG | ✅ ready to draft |
| 01_legal_structure | AZ single-member LLC, Schedule C, cash basis, owner-operated; EIN/bank exist (no numbers); formation basics | DECISION_LOG, roadmap | ⚠️ ready; a few formation facts may need owner confirm |
| 02_services | Service catalog: production labor, rigging, staging, lighting, A/V support, load-in/out, set changes, supervised rigging | July digests, resume work | ✅ ready to draft |
| 03_operations | End-to-end workflow: inquiry → agreement → gig → hours → invoice → payment → records | roadmap dh-2 (gig tracking), invoice system | ⚠️ ready; workflow to confirm/standardize |
| 04_financial_systems | Invoicing (1099 generator), payment/finance tracking, recordkeeping, accounting method; **link** to tax knowledge base | roadmap, July digest; tax KB in `invoicing` repo | ⚠️ references another repo — index, don't duplicate |
| 05_contracts_legal | Client MSA, W-9 workflow, client agreements, independent-contractor framework (in progress) | roadmap dh-6/dh-10 | ⚠️ contractor framework still in progress |
| 06_safety | Safety documentation/standards for live-event labor (in progress) | roadmap dh-11 | ⚠️ in progress — document as it's built |
| 07_digital_assets | Website (deadhanglaborllc.com, live+SSL), business email, portfolio, tools (invoice generator, affirmation calendar) | July digests | ✅ ready to draft |
| 08_brand | Navy & gold identity, logo/name-tag concept, voice, portfolio caption standards | July digests; assets in `Contentrepo`/portfolio | ⚠️ asset files live elsewhere — reference |
| 09_revenue_streams | Contract labor (staffing cos + direct), print-on-demand merch (under Deadhang), affirmation calendar | roadmap dh-12, July digests | ✅ ready to draft |
| 10_growth_model | Solo → team deployment → labor-staffing-agency path | roadmap, DECISION_LOG (OD-8) | ✅ ready to draft |
| 11_compliance_and_risk | Insurance (deferred), licenses/permits, compliance posture | DECISION_LOG, KNOWN_RISKS | ✅ ready to draft |

## Guardrails (public-safe — repo is public)

Keep OUT of these docs (belongs in private storage or another private repo):
- Income figures, per-client pay, rates; bank/EIN numbers; personal PII;
  third-party individuals' contact details; reservation/receipt numbers.
- Where sensitive detail is essential, **reference** it ("tax records maintained
  in the private `invoicing` repo") rather than reproducing it.

## Source material available

- `roadmap.json` — Deadhang branch (current state, work items, blockers).
- `governance/DECISION_LOG.md` + `CURRENT_STATE.md` — structure/tax/insurance decisions.
- `data/raw-reports/` — the July digests (sanitized) with rich operational detail.
- Other repos (referenced, not copied): `invoicing` (tax KB), `Contentrepo`
  (brand/portfolio assets), `Shirts` (print-on-demand automation).

## Build sequence (after sign-off)

1. Scaffold `companies/deadhang-labor/` with `README.md` + the 12 stubs.
2. Draft the ✅ "ready" docs first (00, 02, 07, 09, 10, 11) — highest signal, least blocked.
3. Draft the ⚠️ docs, confirming the handful of open facts with the owner.
4. Cross-link from the roadmap Deadhang branch to this folder.
5. Mark Stage 1 complete when the definition-of-done is met; update CHANGELOG + DECISION_LOG.

## What I need from the owner to proceed

1. **Approve the folder + structure** (`companies/deadhang-labor/`, the 12 docs) — or adjust.
2. A few facts for the ⚠️ items (only what you're comfortable putting in a public repo):
   - Formation basics for `01` (year established is fine; keep EIN/registered-agent private).
   - Confirm the standard gig workflow for `03` (how a job goes from inquiry to paid).
3. Confirm which specialized material should be **referenced** vs. lives elsewhere
   (tax KB in `invoicing`, brand assets in `Contentrepo`).
