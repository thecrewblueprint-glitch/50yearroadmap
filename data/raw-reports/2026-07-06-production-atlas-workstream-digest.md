# Production Atlas Workstream Memory Digest — 2026-07-06

Extracted from the 40-chunk ChatGPT Production Atlas / Freelance Stagehand workstream inside the ChatGPT Atlas archive. This digest focuses on durable project decisions, branch state, app architecture changes, data-model direction, and handoff status. It does not attempt to preserve every conversational step.

---

## Active Projects & Decisions

### Festival Atlas Renamed as Production Atlas
**Status:** active  
**Project:** Production Atlas app identity  
**Decision:** The visible app should be named **Production Atlas** even though the GitHub repository may remain `festival-atlas`. The project should be framed as a resource scouting database for long-term production work opportunities, not just a music festival list.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0008.md` lines 99-123.

### Two-Track Branch Strategy
**Status:** completed  
**Project:** Production Atlas repository branching  
**Decision:** Two branches were created from the same baseline: one for a market-research-specific version and one for production-ready app development. Research work should happen on `research-version`; production-readiness work belongs in a separate production branch.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0002.md` lines 26-55.

### Research-Version Branch Only for Current Adjustments
**Status:** active  
**Project:** Production Atlas branch discipline  
**Decision:** Recent adjustments were targeted to `thecrewblueprint-glitch/festival-atlas` on `research-version`. `main` and the production branch should not be edited for research-version changes unless explicitly requested.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0004.md` lines 198-213.

### Production Labor Branch Taxonomy
**Status:** active  
**Project:** Production Atlas data taxonomy  
**Decision:** The app should focus on staging labor and production-core job branches: staging/structures, rigging, lighting, audio, video/LED, power/electrical distribution, site ops/build crew, logistics/equipment movement, scenic/carpentry/fabrication, backline/stage tech support, stage management/deck operations, and production office/PA work.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0003.md` lines 61-81 and 83-92.

### Key Research Questions Per Opportunity
**Status:** active  
**Project:** Production Atlas research workflow  
**Decision:** Each opportunity should eventually answer who builds the stage, supplies rigging, lighting, audio, video/LED, site ops, power, which IATSE local applies, which nonunion labor companies staff it, and who coordinates production. These should not be guessed; they require source-backed or human-verified data.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0003.md` lines 83-117 and 156-180.

### Master Data Source Cleanup
**Status:** completed  
**Project:** Production Atlas data-source cleanup  
**Decision:** Older research/data files should remain in the repo as archive, but the visible Pages app should read from one clean active master data source instead of a messy compiled set. Later this evolved again into structured packages, but the decision to avoid deleting old research remains active.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0005.md` lines 21-45 and 54-80.

### U.S.-Only Employer Leads
**Status:** active  
**Project:** Production Atlas employer matrix  
**Decision:** The active app should show United States employer leads only. Multinational companies may remain only when represented as U.S. operations or U.S. hiring leads. Broad global employer categories should not be shown in the active matrix.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0005.md` lines 117-150.

### Employer Link Rule
**Status:** active  
**Project:** Employer matrix link behavior  
**Decision:** Employer matrix links should point to verified career/apply pages where available. If no clear career/apply page exists, link to the company homepage instead, while retaining an internal status distinction between career links and homepage fallbacks. The empty homepage fallback tag was later removed from the visible card UI.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0006.md` lines 92-149; `...__chunk-0007.md` lines 18-47 and `...__chunk-0009.md` lines 186-220.

### U.S. IATSE Local Directory
**Status:** active  
**Project:** IATSE local directory  
**Decision:** Add a United States IATSE local directory as a separate lookup aid, searchable by local number, state, city/jurisdiction, craft, and district. It is not a final jurisdiction ruling; final verification should use the official IATSE directory.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0007.md` lines 50-106.

### Opportunity Calendar Scope Expansion
**Status:** active  
**Project:** Production Atlas calendar model  
**Decision:** The calendar should track any long-term production opportunity in the live-event industry that may provide accommodations, not only music festivals. Opportunity categories should include festivals, tours, conventions/expos, arena/stadium builds, corporate events, venue residencies, seasonal productions, broadcast/live TV, esports, fairs, and grandstand circuits.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0007.md` lines 184-222; `...__chunk-0008.md` lines 18-27.

### Structured Data Packages
**Status:** active  
**Project:** Production Atlas data architecture  
**Decision:** The app should load clean structured package files rather than one compressed pipe-delimited master file. Packages include production branches, opportunities, employers, and initially a loader. A later code audit removed compatibility-loader dependence and made the app read directly from structured packages.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0008.md` lines 79-147; `...__chunk-0009.md` lines 127-183.

### Phase 2 Opportunity Schema
**Status:** completed  
**Project:** Production Atlas opportunity records  
**Decision:** Opportunity records should carry normalized fields such as opportunityType, startDate, endDate, venue, producer, status, mapped branches, lodging/accommodation potential, travel potential, per diem potential, long-term value score, and next research actions. A schema document was added to prevent drift back into compressed strings.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0008.md` lines 149-173; `...__chunk-0009.md` lines 18-29.

### Public / Field-Intel Separation
**Status:** active  
**Project:** Production Atlas data safety model  
**Decision:** Because much production labor information is not public, Production Atlas should separate public evidence from field intelligence. Public app data should show public-safe confidence labels, source types, research status, and human-verification queues. Sensitive/private field details should not be published.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0009.md` lines 31-77 and 79-124.

### Code Audit and Cleanup Direction
**Status:** active  
**Project:** Production Atlas codebase cleanup  
**Decision:** Patch/compatibility code should be removed where possible. The active app should read directly from structured packages, avoid old festival-master-data compatibility objects, preserve active/inactive filtering, and keep public-safe classification in the active code path.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0009.md` lines 127-183.

### Branch Research Batch Progress
**Status:** active  
**Project:** Production Atlas branch research packages  
**Decision:** Research packages were created in branch batches. The later handoff states progress through Logistics batch 005, with Scenic batch 001 data created but its paired report missing. Next sequence should audit/clean the repository, create the missing Scenic batch 001 report, then continue Scenic batch 002.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0020.md` lines 29-167; `...__chunk-0040.md` lines 18-22 and 96-135.

### AI Collaboration Handoff System
**Status:** active  
**Project:** Production Atlas AI collaboration workflow  
**Decision:** Add a main handoff package and collaboration log so ChatGPT and Claude can collaborate across chats. The workflow requires reading the collaboration log and handoff first, checking current branch state, appending dated notes, listing commits/files changed, and avoiding overwriting other AI notes unless correcting an error.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0020.md` lines 154-208; `...__chunk-0040.md` lines 40-118.

---

## Blockers Identified

1. **Scenic batch 001 paired report is missing** — Scenic batch 001 data exists, but its report was not created.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0040.md` lines 18-22 and 96-118.

2. **Repository needs comprehensive audit before more research batches** — The handoff explicitly says to run a comprehensive code audit and cleanup of `research-version` before continuing research.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0020.md` lines 154-167; `...__chunk-0040.md` lines 112-118 and 152-158.

3. **Public vendor staffing relationships remain mostly unverified** — The app must not present employer leads as confirmed festival-specific vendors without source-backed proof.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0004.md` lines 156-195; `...__chunk-0005.md` lines 54-115.

4. **2026 active status source URLs are incomplete** — Some active statuses came from a user-provided report without direct source URLs; those fields still need official/public source-link attachment.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0006.md` lines 153-189.

5. **Data structure still needs continued normalization and UI work** — Later phases should add better card displays for lodging, travel, per diem, opportunity type, value score, missing-data checklists, and verification filters.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0008.md` lines 18-27 and 149-173; `...__chunk-0009.md` lines 18-29.

---

## Code Review & Other Work

### Research-Version Code Cleanup
**Status:** completed  
**Description:** Compatibility loader was removed from active app path; the app began reading directly from structured packages. Active page logic was cleaned around opportunity arrays, active filtering, public-safe classification, cards, and modal profile behavior.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0009.md` lines 127-183.

### Multi-Page Branch Cleanup Later in Workstream
**Status:** completed  
**Description:** Later handoff references cleanup commits across index, branches, calendar, opportunities, employers, IATSE, matrix, analytics, sources, guide, validator strengthening, and collaboration log correction.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Freelance_Stagehand_W_2026-07-05_18-00-47.json__chunk-0040.md` lines 152-174.

---

## Sample Coverage

Reviewed representative chunks from the 40-chunk workstream: chunks 0001-0009, 0020, and 0040. These covered setup, branch strategy, data expansion, employer matrix, IATSE directory, opportunity-scope expansion, structured data packages, public/private intelligence separation, code cleanup, research batches, and the final handoff state.

**Public-safe:** Yes — digest excludes private contact details, sensitive operational details, and unverified employer/festival claims beyond their project-management status.
