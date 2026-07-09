# Kimi Handoffs Memory Digest — 2026-07-06

Extracted from 38 Kimi handoff chunks. Strategic sample reviewed: handoff bundle index, calendar affirmation scheduler context, invoice generator framework summary, Production Atlas research handoff review/V2, Production Atlas batch research plan context, GitHub connector capability context, and code-review framework loop.

---

## Active Projects & Decisions

### Production Atlas Research Handoff V2
**Status:** active  
**Project:** Production Atlas public-safe research protocol  
**Decision:** The research handoff needs stronger structure before continuing large research batches. V2 adds event status, load-in/show/strike timing, freshness tracking, a clearer `possible` rubric, evidence-level separation, split site-ops and power vendor categories, unknowns tracking, public-safe source definitions, and a human-verification protocol.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__03_production_atlas_research_handoff_review_and_v2.md__chunk-0001.md` lines 114-148, 151-182, and 188-210; `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__03_production_atlas_research_handoff_review_and_v2.md__chunk-0002.md` lines 33-58, 60-166, and 177-222; `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__03_production_atlas_research_handoff_review_and_v2.md__chunk-0003.md` lines 42-58, 61-99, and 103-123.

### Production Atlas Research Strategy Shift
**Status:** active  
**Project:** Public research execution strategy  
**Decision:** Broad public research across many festival records creates high unknown rates because crew logistics, worker support, labor routes, vendor stacks, and local-jurisdiction confirmations are rarely public. The better strategy is targeted and hybrid: prioritize public vendor case studies, active local labor web presence, producer career pages, industry publications, Tier 1 events, and remote/lodging-sensitive events; use assisted verification workflows for non-public logistics.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__04_production_atlas_batch1_research_and_research_plan_context.md__chunk-0004.md` lines 18-49, 67-104, and 107-148.

### Production Atlas Batch 1/2 Research State
**Status:** active  
**Project:** Production Atlas research packet backlog  
**Decision:** Batch 1 DWP research was compiled as complete with six events, producer-level summary, audio-vendor evidence, and documented public sources. Batch 2 Goldenvoice/AEG remained partial with limited public production information and many unknown fields. Use compiled research as queue/context for the new research plan, not as final app-ready data.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__04_production_atlas_batch1_research_and_research_plan_context.md__chunk-0004.md` lines 61-88 and 91-104.

### Calendar Affirmation Scheduler Reliability
**Status:** active  
**Project:** Affirmation calendar automation  
**Decision:** The calendar affirmation scheduler needs automatic session/authorization renewal inside the calendar service so scheduled event creation does not depend on manual refresh steps. Calendar operations should run through a service layer that verifies access before list/create/update/delete/batch actions.  
**Pillar:** pillar-4 (Contractor Tools)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__01_google_calendar_affirmations_auto_refresh_scheduler_context.md__chunk-0001.md` lines 33-40, 54-118, 122-170, and 172-222.

### Invoice Generator Scope Divergence
**Status:** deferred  
**Project:** Custom invoice generator with payments/banking  
**Decision:** Kimi produced a broad enterprise-grade invoice generator plan with multiple client apps, API gateway, several application services, payment and bank integrations, search/cache/storage services, 12-week build phases, and high cost estimates. This conflicts with the later narrowed Deadhang invoice decision and should be treated as an overbuilt/future reference, not the current MVP.  
**Pillar:** pillar-4 (Contractor Tools)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__02_custom_invoice_generator_framework_summary.md__chunk-0001.md` lines 30-50, 54-83, 87-101, and 105-117.

### GitHub Connector Limitation Context
**Status:** completed  
**Project:** Tool-capability clarification  
**Decision:** Kimi could not directly connect to or interact with GitHub repositories; it could only analyze pasted code, generate files, discuss workflows, and read public URLs. This explains why later repo work required a connector-capable agent.  
**Pillar:** pillar-4 (Contractor Tools)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__05_github_connector_capability_context.md__chunk-0001.md` lines 30-49.

### Code Review Framework / Missing Payload Guardrail
**Status:** completed  
**Project:** Code review workflow framework  
**Decision:** Preserve the 8-part review framework: Keep, Remove, Rewrite, Security issues, Performance issues, Architecture problems, Commit-ready change list, and AI-agent implementation prompt. Add an operating guardrail: do not hallucinate analysis when no code/payload is provided; stop recursive “paste the code” loops after identifying missing input.  
**Pillar:** pillar-4 (Contractor Tools)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__06_code_review_framework_loop_context.md__chunk-0001.md` lines 40-55, 145-188, and 198-210.

---

## Blockers Identified

1. **Production Atlas research cannot rely on public sources alone for crew logistics** — Public data is too thin for worker support, labor routes, full vendor stack, and local-jurisdiction confirmation; continuing broad research creates many unknown fields.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__04_production_atlas_batch1_research_and_research_plan_context.md__chunk-0004.md` lines 18-49 and 91-104.

2. **Production Atlas needs a human-verification assistance mechanism** — The user stated they would not gather human verification without assistance; the system needs a framework/tool for assisted verification before non-public logistics can be completed safely.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__04_production_atlas_batch1_research_and_research_plan_context.md__chunk-0004.md` lines 120-148 and 152-172.

3. **Invoice generator enterprise plan is overbuilt for current MVP** — The large payment/bank/multi-service plan is useful as long-term reference but mismatched to the current narrower invoice-generator direction.  
   **Status:** blocked  
   **Pillar:** pillar-4 (Contractor Tools)  
   Evidence: `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__02_custom_invoice_generator_framework_summary.md__chunk-0001.md` lines 42-50, 74-83, and 97-101.

4. **Calendar automation depends on reliable authorization renewal** — Calendar sync/event creation needs automatic renewal and persistence to avoid manual refresh steps and failed scheduled jobs.  
   **Status:** blocked  
   **Pillar:** pillar-4 (Contractor Tools)  
   Evidence: `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__01_google_calendar_affirmations_auto_refresh_scheduler_context.md__chunk-0001.md` lines 33-36 and 66-118.

5. **Code review workflows need actual payload enforcement** — Review agents must stop when no code/content is provided and avoid fabricating reviews from empty input.  
   **Status:** blocked  
   **Pillar:** pillar-4 (Contractor Tools)  
   Evidence: `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__06_code_review_framework_loop_context.md__chunk-0001.md` lines 145-188 and 198-210.

---

## Code Review & Other Work

### Research Handoff Template Review
**Status:** completed  
**Description:** Kimi identified 12 flaws in the Production Atlas research handoff and produced a stronger V2 template with evidence levels, timing fields, status values, vendor granularity, source-quality rules, and human verification protocol.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__03_production_atlas_research_handoff_review_and_v2.md__chunk-0001.md` lines 114-210 and `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__03_production_atlas_research_handoff_review_and_v2.md__chunk-0003.md` lines 103-123.

### Code Review Loop Test
**Status:** completed  
**Description:** The Kimi conversation validated a key operating rule: do not continue a workflow loop when the payload is missing, and do not hallucinate a code review from framework text alone.  
**Pillar:** pillar-4 (Contractor Tools)  
**Evidence:** `memories/processed/chunks/kimi-batch-2026-07-05/kimi-batch-2026-07-05__md_handoff_bundle__06_code_review_framework_loop_context.md__chunk-0001.md` lines 145-188 and 198-210.

---

## Sample Coverage

Reviewed 10 chunk files / ranges from the Kimi archive, including:

- 00_INDEX chunk 0001
- Google Calendar affirmations context
- custom invoice generator framework summary
- Production Atlas research handoff review/V2 chunks 0001-0003
- Production Atlas batch research plan context chunk 0004
- GitHub connector capability context
- code review framework loop context

**Public-safe:** Yes — digest excludes personal contact details, private credentials, pay rates, lodging addresses, private referrals, raw private source dumps, and sensitive field notes.
