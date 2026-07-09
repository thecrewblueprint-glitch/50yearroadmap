# Festival Atlas Memory Digest — 2026-07-06

Extracted from 452 Festival Atlas / Production Atlas archive chunks. Strategic sample reviewed: roadmap, product roadmap, schema, employer-route methodology, long-term gig model, employer landscape research, source/data backlog, handoff, research prompts, and producer/vendor evidence captures.

---

## Active Projects & Decisions

### Production Atlas Public Research Dashboard
**Status:** active  
**Project:** Production Atlas static public-safe work research dashboard  
**Decision:** Keep Production Atlas as a static GitHub Pages research dashboard with no backend, login, private contact storage, payment system, scraping automation, or private pay/lodging field-note publication. Current worker-facing questions are where the work is, when it happens, who publicly produces/routes it, which public employer/vendor/labor-route leads are relevant, and what public source/planning page should be reviewed next.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ai-communication__PRODUCT_ROADMAP.md__chunk-0001.md` lines 26-40 and 42-60.

### Research-Version Deployment and Scope Control
**Status:** active  
**Project:** Production Atlas deployment/source-of-truth control  
**Decision:** Treat `research-version` as the working/live branch for the Festival Atlas app; do not patch `main` as a shortcut. If live output is stale, fix deployment, validation, or source drift instead.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ROADMAP.md__chunk-0001.md` lines 28-35; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__HANDOFF-2026-06-24.md__chunk-0001.md` lines 90-97.

### Public-Safe Opportunity Data Model
**Status:** active  
**Project:** Opportunity record schema and validator-backed data quality  
**Decision:** Use generalized opportunity records rather than festival-only records. Records must include public location/date/source fields, department presets, lodging/travel/per-diem fields, long-term value score, next research actions, and relationship arrays. Confirmed vendors require specific public evidence; candidate arrays remain unconfirmed leads.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__data__packages__OPPORTUNITY_RECORD_SCHEMA.md__chunk-0001.md` lines 18-33, 53-64, 67-98, 123-155, and 168-179.

### Lodging, Travel, and Long-Term Work Value Analysis
**Status:** active  
**Project:** Accommodation/travel/per-diem research layer  
**Decision:** Score opportunities by work-year usefulness, not event popularity. Lodging, extended work windows, travel reimbursement, per diem, repeat annual cycle, route clarity, and application route increase value. Accommodation/travel fields should remain unknown unless public evidence or reliable verified source review supports stronger labels.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__long-term-gig-scouting-model.md__chunk-0001.md` lines 26-44 and 212-260; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__RESEARCH_PROMPT_FILL_GAPS.md__chunk-0001.md` lines 25-31, 52-88, and 133-179.

### Vendor and Employer Route Intelligence
**Status:** active  
**Project:** Employer/vendor/labor-route mapping by department and market  
**Decision:** Do not treat the festival brand as the employer. Map the actual route ecosystem: promoter, venue/site owner, production management, labor companies, IATSE/local jurisdiction, staging, rigging, lighting, audio, video/LED, power, site operations, logistics, scenic, backline, stage management, and production office channels.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__employer-landscape-market-analysis.md__chunk-0001.md` lines 26-33 and 130-151; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__festival-employer-landscape-map.md__chunk-0001.md` lines 18-23, 24-145, and 146-183.

### Multi-Market Record Splitting
**Status:** active  
**Project:** Breakaway and Country Thunder per-market records  
**Decision:** Multi-market records need per-market handling before route, lodging, labor, vendor, and jurisdiction conclusions can be trusted. Broad placeholders should not be used as precise outreach justification until dates, venues, market-specific labor routes, vendor stacks, and IATSE/local jurisdiction are verified.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__notebooklm-public-research__006-multi-market-split-re__chunk-0001.md` lines 61-64, 102-130, and 141-183; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__data-quality-backlog.md__chunk-0002.md` lines 18-32 and 44-61.

### Source Verification and Data Quality Backlog
**Status:** active  
**Project:** Production Atlas source verification and cleanup queue  
**Decision:** All active records reached source-attached verification in the June 24 pass, but remaining work includes per-market records, fall CRSSD handling, producer verification, accommodation/travel fill for top-scoring records, and route-lead wording review so unverified leads are not presented as confirmed work relationships.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__data-quality-backlog.md__chunk-0001.md` lines 139-168 and 172-182; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__data-quality-backlog.md__chunk-0002.md` lines 36-40, 78-95, 102-122, and 126-133.

### Public Worker UI Scope
**Status:** active  
**Project:** Page-specific public filtering and navigation scope  
**Decision:** Do not revert the app to date/promoter-only filtering. Keep current page-specific controls: Opportunities supports text, state, department, producer/promoter, and date/month; Calendar supports date/month; Map supports state and date/month; Employers supports text, department, state, and employer type; Sources supports festival, department, and employer route. Keep Schedule off header navigation until mobile usability is rebuilt.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ROADMAP.md__chunk-0001.md` lines 60-93; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ai-communication__PRODUCT_ROADMAP.md__chunk-0001.md` lines 107-140.

### Future Unified Planning Workspace
**Status:** deferred  
**Project:** Schedule/map/travel planning layer  
**Decision:** Defer the full planning workspace until Schedule is mobile-usable. Longer-term direction is a selected-opportunity workspace showing map location, public show dates, approximate work window, add/remove schedule controls, and later travel distance/time comparisons after scope and source rules are approved.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ai-communication__PRODUCT_ROADMAP.md__chunk-0002.md` lines 29-42 and 60-73; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ROADMAP.md__chunk-0001.md` lines 152-160.

---

## Blockers Identified

1. **Production Atlas validation cannot be confirmed in connector-only environments** — `npm run validate:all` is required for app data changes, but validation must be run in a real workspace or GitHub Actions environment before claiming clean status.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ai-communication__PRODUCT_ROADMAP.md__chunk-0001.md` lines 155-167; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__HANDOFF-2026-06-24.md__chunk-0001.md` lines 161-172.

2. **Accommodation and travel intelligence remains largely unfilled** — active records still need accommodation, travel, and per-diem research, with top-scoring records prioritized. Unknown must stay unknown when public evidence is not available.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__HANDOFF-2026-06-24.md__chunk-0001.md` lines 215-217; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__RESEARCH_PROMPT_FILL_GAPS.md__chunk-0001.md` lines 52-88 and 133-179.

3. **Multi-market records require market-level split verification** — Breakaway and Country Thunder remain high-potential but speculative until per-market dates, venues, labor routes, vendor stacks, travel/lodging signals, and IATSE/local jurisdiction are verified.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__notebooklm-public-research__006-multi-market-split-re__chunk-0001.md` lines 141-183; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__data-quality-backlog.md__chunk-0002.md` lines 18-32 and 102-122.

4. **Producer/vendor evidence often lacks URL-level extraction** — several NotebookLM captures identify useful producer or vendor evidence categories, but they remain non-app-ready until citation URLs are exported, reviewed, and classified as current, historical, producer-pattern, vendor-pattern, or event-specific.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__notebooklm-public-research__009-goldenvoice-aeg-sourc__chunk-0001.md` lines 77-105 and 121-138; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__notebooklm-public-research__011-c3-bonnaroo-evidence-__chunk-0001.md` lines 78-130; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__notebooklm-public-research__013-dwp-producer-event-pa__chunk-0001.md` lines 67-124.

5. **Schedule remains off public header navigation** — Schedule exists by direct URL but should not return to primary navigation until mobile usability issues are resolved.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ROADMAP.md__chunk-0001.md` lines 50-57, 90-93, and 152-160; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__ai-communication__PRODUCT_ROADMAP.md__chunk-0002.md` lines 29-42 and 60-73.

---

## Code Review & Other Work

### Static App Validation Rules
**Status:** active  
**Description:** Production Atlas app changes must preserve validator rules, public-safe display, centralized source links, branch manifest ownership, and banned construct rules.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__HANDOFF-2026-06-24.md__chunk-0001.md` lines 176-199.

### Source and Coordinate Package Cleanup
**Status:** completed  
**Description:** June 24 work completed full source verification for all active records and moved map coordinates into a dedicated package loaded only by `map.html`.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__HANDOFF-2026-06-24.md__chunk-0001.md` lines 141-158 and `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__HANDOFF-2026-06-24.md__chunk-0001.md` lines 221-229.

### Route Lead Confidence Boundary
**Status:** active  
**Description:** Branch research records using unverified or possible confidence labels must be treated as research directions, not confirmed employers or current-year vendor assignments.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__branch-research-batch-006-staging.md__chunk-0001.md` lines 41-58 and 108-120; `memories/processed/chunks/festival-atlas-research-version/festival-atlas-research-version__festival-atlas-research-version__research__data-quality-backlog.md__chunk-0002.md` lines 118-122.

---

## Sample Coverage

Reviewed 20 chunk files / chunk ranges from the Festival Atlas archive, including:

- ROADMAP.md chunk 0001
- ai-communication/PRODUCT_ROADMAP.md chunks 0001-0002
- data/packages/OPPORTUNITY_RECORD_SCHEMA.md chunk 0001
- research/long-term-gig-scouting-model.md chunk 0001
- research/festival-employer-landscape-map.md chunk 0001
- employer-route-methodology.html chunk 0001
- research/RESEARCH_PROMPT_FILL_GAPS.md chunks 0001-0002
- research/employer-landscape-market-analysis.md chunks 0001-0002
- research/research-batch-002-major-national-anchor-targets.md chunk 0001
- research/branch-research-batch-006-staging.md chunk 0001
- research/notebooklm-public-research captures 005, 006, 009, 011, 013, 014
- research/data-quality-backlog.md chunks 0001-0002
- research/HANDOFF-2026-06-24.md chunk 0001

**Public-safe:** Yes — digest excludes personal contact details, pay rates, lodging addresses, private field notes, referrals, and NDA/client-sensitive content.
