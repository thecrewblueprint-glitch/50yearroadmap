# ChatGPT Atlas Memory Digest — 2026-07-06

Extracted from the ChatGPT Production Atlas repo-audit archive. Strategic sample reviewed: Production Atlas project instructions, repo audit and patch notes, documentation-alignment pass, 2027 rollover/source retrieval pass, app-usable research prompt, and graph-structure discussion.

---

## Active Projects & Decisions

### Production Atlas Repo Operating Rules
**Status:** active  
**Project:** Production Atlas repo operation  
**Decision:** Treat `thecrewblueprint-glitch/festival-atlas` on `research-version` as the active working state. `main` is not the active source unless explicitly requested. The app remains a static GitHub Pages research dashboard; default scope excludes backend, login, database, payment, private contact storage, and scraping automation. Repo docs and collaboration protocols are source of truth.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0001.md` lines 18-45 and 53-62.

### Validator Drift Fix
**Status:** completed  
**Project:** Static app validation coverage  
**Decision:** The repo had a validator drift issue: README listed 12 active pages, including `map.html` and `schedule.html`, but the static validator checked only 10. The validator was patched on `research-version` so `map.html` and `schedule.html` are included.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0001.md` lines 99-120 and 127-154; `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0002.md` lines 35-79.

### Missing Claude Handoff Documentation Gap
**Status:** active  
**Project:** Collaboration handoff continuity  
**Decision:** Expected Claude stage/source-cleanup handoffs were not found on `research-version` or the known Claude PR branch. Treat this as a repo-visible documentation gap. Continue from actual current files, not from assumed uncommitted handoffs.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0001.md` lines 89-97 and 123-131; `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0002.md` lines 35-49 and 76-95.

### Source URL Cleanup Phase
**Status:** active  
**Project:** Production Atlas source verification cleanup  
**Decision:** Claude had been gathering source URLs when usage limits interrupted the work. The next work should resume source URL gathering in small batches, not jump into broad cleanup. Records should be handled 5–10 at a time, with official/public URLs only, and backlog files should track missing official 2026/2027 sources, date verification, venue verification, and weak source issues.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0001.md` lines 122-154; `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0002.md` lines 175-242.

### Documentation Alignment Pass
**Status:** completed  
**Project:** Production Atlas repo documentation alignment  
**Decision:** A documentation-alignment pass updated README, roadmap, chat instructions, collaboration protocol, public white pages, legal/policy pages, research support docs, and collaboration logs so they match the current functioning static app. Docs now reflect active nav, Schedule direct-URL status, Analytics queue scope, active opportunity counts, master registry count, coordinate coverage, public-cycle guard, and static-app boundaries.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Update_Festival__2026-07-05_17-55-12.json__chunk-0001.md` lines 23-31 and 58-77.

### Automatic Validation Workflow Assumption
**Status:** active  
**Project:** Validation workflow  
**Decision:** The user clarified that an automatic workflow sets up/runs validation, so future repo agents should treat validation as handled by workflow rather than repeatedly blocking on inability to run local validation in connector-only sessions.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Update_Festival__2026-07-05_17-55-12.json__chunk-0001.md` lines 68-77.

### Map Department Filter Fix
**Status:** completed  
**Project:** Map page filter parity  
**Decision:** A safe repo fix added the missing Department filter to `map.html`, matching support already present in `assets/map-page-static.js`. This fixed a page/UI mismatch without touching the large core renderer.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Festival_Atlas_Issue__2026-07-05_17-54-36.json__chunk-0001.md` lines 70-84 and 92-115.

### Public Cycle / 2027 Rollover Data Pathway
**Status:** active  
**Project:** Opportunity rollover and active planning scope  
**Decision:** Festivals whose 2026 windows were in the past should not remain active as 2026 planning targets. Verified 2027 records were added through a rollover package for early-year events such as Coachella, Ultra Miami, EDC Las Vegas, Welcome to Rockville, Beyond Wonderland SoCal, BottleRock Napa, plus missed records like CRSSD and Sick New World. Records without verified 2027 dates should be hidden from active planning until verified.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06.json__chunk-0001.md` lines 38-61 and 72-113.

### Employer Source Retrieval Pathway
**Status:** active  
**Project:** Sources page employer/careers routes  
**Decision:** The Sources page had a retrieval gap: it showed opportunity and branch sources but not public employer, careers, contact, or route links central to the app. A new employer-route sources section was added to `sources.html`, pulling public employer route data and respecting filters where relevant.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06.json__chunk-0001.md` lines 72-113 and 156-179.

### Repo Knowledge Graph Proposal
**Status:** deferred  
**Project:** AI retrieval and repo-context compression  
**Decision:** Adding a lightweight static repo graph would reduce context-window bloat, improve file targeting, and reduce patch-layer mistakes. The first step should be a repo-visible graph spec/document, not a heavy database. Candidate graph tracks files, roles, owners, loaded-by, depends-on, validates-with, documents-behavior-of, public-safety constraints, and do-not-edit-casually files.  
**Pillar:** pillar-4 (Contractor Tools)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Festival_Atlas_Issue__2026-07-05_17-54-36.json__chunk-0001.md` lines 117-138 and 177-206.

### App-Usable Labor Market Research Prompt
**Status:** active  
**Project:** Production Atlas research prompt framework  
**Decision:** The app needs research prompts designed for app-usable data, not generic articles. Required research dimensions include labor market maps, opportunity types, labor routes, department demand, job market keywords, confidence scoring, app fields, seasonal planning, public-safe source strategy, next actions, and dashboard language.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Research_Prompt_for_C_2026-07-05_17-57-12.json__chunk-0003.md` lines 18-35.

---

## Blockers Identified

1. **Source URL cleanup remains incomplete** — Claude’s source URL pass was interrupted. The app needs small-batch official source verification before broader cleanup or expansion.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0001.md` lines 122-154 and `...__chunk-0002.md` lines 175-242.

2. **Claude handoff files are missing from expected branches** — The missing handoffs make prior work harder to audit; current agents must rely on actual files and collaboration logs that exist.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Project_Instructions__2026-07-05_17-57-23.json__chunk-0001.md` lines 89-97 and `...__chunk-0002.md` lines 35-49.

3. **Public-cycle helper / owner-file boundary remains a risk** — Prior audit found a helper-script approach that may violate owner-file rules. Long-term fix should canonicalize cycle behavior in owner files/data rather than stacking workaround scripts.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Festival_Atlas_Issue__2026-07-05_17-54-36.json__chunk-0001.md` lines 70-84 and 92-115.

4. **Repo context retrieval is inefficient without a graph/map** — Assistants repeatedly load broad docs and may miss owner relationships. A static repo graph is deferred but would reduce context bloat and patch mistakes.  
   **Status:** blocked  
   **Pillar:** pillar-4 (Contractor Tools)  
   Evidence: `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Festival_Atlas_Issue__2026-07-05_17-54-36.json__chunk-0001.md` lines 117-138 and 177-206.

---

## Code Review & Other Work

### Repo Audit and Patch Passes
**Status:** completed  
**Description:** ChatGPT performed several connector-only repo audit/patch passes, including documentation alignment, map department filter fix, validator drift fix, and 2027 rollover/source retrieval pathway work.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Update_Festival__2026-07-05_17-55-12.json__chunk-0001.md` lines 58-77; `memories/processed/chunks/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41/ChatGPT_Production_Atlas_-_Repo_Audit_Instructio_2026-07-05_18-01-41__ChatGPT_Production_Atlas_-_Repo_Downloadable_Fil_2026-07-05_17-56-06.json__chunk-0001.md` lines 58-113.

---

## Sample Coverage

Reviewed 8 chunk files / ranges from the ChatGPT Atlas archive, including:

- Project Instructions chunks 0001-0003
- Festival Atlas Issue chunk 0001
- Repo Update Festival chunk 0001
- Research Prompt for Contracts chunk 0003
- Repo Downloadable File chunk 0001
- related collaboration-log search results

**Public-safe:** Yes — digest excludes private contact data, pay rates, lodging details, private field notes, credentials, and raw source dumps.
