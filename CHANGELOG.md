# Changelog

The shared work log for this repository. Every agent (and the owner) records
what changed here so the next collaborator can pick up with full context.
See `AGENTS.md` for the rules. Newest entries first.

**How to add an entry:** at the top of the "Entries" section, add a dated
block. Say *what* changed, *why*, and note any *follow-ups* or *open threads*.
Keep it short but specific. One block per working session is fine.

---

## Open threads

Things known-incomplete or awaiting a decision. Clear them when resolved.

- **Watcher remains manual.** The current branch/journey watcher exists and writes
  proposals only to `data/roadmap/watcher-proposals.json`; it is not wired into
  CI and never edits `roadmap.json` automatically.
- **Proposal review backlog.** The latest watcher output contains candidate work
  items/blockers for human review. Approved items still need to be promoted by
  hand into `roadmap.json`.

---

## Entries

### 2026-07-18 — Stage 2 scoped: The Crew Blueprint canonical documentation
- Added `governance/STAGE_2_SCOPE.md` (mirrors Stage 1 structure): proposed
  `companies/crew-blueprint/` folder + 9-doc set, per-doc source/readiness table,
  public-safe guardrails (**no certification claims**; describe course
  architecture/catalog but do **not** reproduce full paid lessons), source-material
  map, build sequence, and the handful of owner-input gaps (authority/safety model,
  content pipeline steps).
- Awaiting owner sign-off before scaffolding/drafting — same gate as Stage 1.

### 2026-07-17 — Stage 1: Deadhang docs completed via owner interview
- One-item-at-a-time interview filled every "To confirm" fact:
  - `01` Legal — **formed 2026** (first year); AZ single-member LLC.
  - `03` Operations — work comes in via **direct relationships + staffing
    companies**; gig log lives in **Google Sheets/Drive + ChatGPT** (formalizing via `dh-2`).
  - `06` Safety — operating baseline: **OSHA / ANSI / ESTA / ETCP first + site
    requirements** (detailed procedures still build via `dh-11`).
  - `08` Brand — exact navy/gold from the **site CSS** (source of truth); noted
    per-project CSS schemas (Deadhang, Crew Blueprint, roadmap, Production Atlas).
  - `11` Compliance — **no TPT/business license now** (service labor); **merch
    t-shirt launch (`dh-12`) triggers likely AZ TPT registration** — evaluate before selling.
- Docs 00, 01, 02, 03, 04, 07, 08, 09, 10, 11 are Documented. Remaining: `05`
  (contractor framework) and `06` (detailed procedures) complete as `dh-10`/`dh-11`
  land; optional tagline. Stage 1 substantially complete.

### 2026-07-17 — Stage 1 first pass: Deadhang canonical documentation drafted
- Scaffolded `companies/deadhang-labor/` and drafted all 12 canonical docs
  (README + 00 overview → 11 compliance/risk): legal structure, services,
  operations, financial systems, contracts, safety, digital assets, brand,
  revenue streams, growth model, compliance/risk.
- Ready docs written fully from repo context; in-progress/gap items marked
  "To confirm (owner)" rather than blocking. Sensitive detail (income, account
  numbers, tax records, brand assets) is **referenced**, not reproduced.
- PII-scanned clean (no emails, dollar amounts, SSN, or full name).
- Remaining for Stage 1 completion: owner fills the "To confirm" facts;
  safety + contractor-framework docs finish as that work lands.

### 2026-07-17 — Stage 1 scope drafted (Deadhang canonical documentation)
- Added `governance/STAGE_1_SCOPE.md`: goal + definition-of-done, proposed
  `companies/deadhang-labor/` folder, a 12-document canonical set (with per-doc
  source + readiness), public-safe guardrails, source-material map, and a build
  sequence. Awaiting owner sign-off on structure + a few ⚠️ facts before drafting.
- No roadmap/data changes; scoping only.

### 2026-07-17 — Governance docs added + stale docs refreshed (Stage 0 cont.)
- Added the genuinely-new governance docs (the ones not already covered):
  `governance/OPEN_DECISIONS.md`, `KNOWN_RISKS.md`, `LESSONS_LEARNED.md`.
- Evaluated the docs that already fill the other proposed roles and refreshed the
  stale ones (Stage 0 = remove outdated info):
  - `README.md`: it wrongly listed the watcher, `/data/schema`, and
    `/data/roadmap-deep-context` as "not yet in the repo" (all exist now); updated
    the pipeline (watcher/prioritizer/validator are built), the data-model snapshot
    (added north_star/end_goal/phases/journey/thirty_sixty_ninety + full status
    enum), and added `/governance/`.
  - `CHATGPT_HANDOFF.md`: refreshed to 2026-07-17 — added `completed`/`moved_later`
    statuses, the `thirty_sixty_ninety` field, the prioritizer script, governance,
    Deadhang AZ-LLC facts, Homestead outreach, and the GPT-paused note.
- Did NOT add duplicate docs: SESSION_SUMMARY (=CHANGELOG), AI_HANDOFF
  (=CHATGPT_HANDOFF), NEXT_ACTIONS (=roadmap this_week/30-60-90/backlog),
  EXECUTIVE_SUMMARY (=README + governance CURRENT_STATE) — the existing files serve
  those roles.

### 2026-07-17 — Stage 0: roadmap synchronization + governance framework
- Acted on the ChatGPT Stage 0 handoff (GPT paused — GitHub connector issue;
  Claude solo on the repo for now). GPT's session was read-only; nothing had
  been committed.
- **Roadmap synchronized with reality** (`roadmap.json`): made Deadhang's
  Arizona single-member LLC / Schedule C / cash-basis identity explicit
  (corrected any drift toward Wisconsin); `dh-1` business-structure audit →
  in_progress (~90%); `dh-6` client MSA → completed; added `dh-9` insurance
  (`moved_later` — deferred, not forgotten), `dh-10` independent-contractor
  framework (in_progress), `dh-11` safety documentation (in_progress), `dh-12`
  print-on-demand merch line under Deadhang (in_progress, no new LLC); refreshed
  current_state/blockers; Deadhang 45% → 60%. Validator passes.
- **Governance framework established** in `/governance/`: `README.md` (purpose +
  Stage 0–5 plan), `CURRENT_STATE.md` (snapshot), `DECISION_LOG.md` (structure,
  tax, insurance, print-on-demand, single-source-of-truth decisions), and
  `handoffs/2026-07-17-chatgpt-stage0-handoff.md` (the source handoff, stored
  verbatim). `AGENTS.md` §8 now points to it.
- Noted that Stage 0's "collaboration standards" and "AI handoff system" were
  already largely built (`AGENTS.md`, `CHANGELOG.md`, `CHATGPT_HANDOFF.md`).
- **Open:** remaining proposed governance docs (EXECUTIVE_SUMMARY, NEXT_ACTIONS,
  OPEN_DECISIONS, KNOWN_RISKS, LESSONS_LEARNED, SESSION_SUMMARY) — several
  overlap with existing files; confirm with owner before adding. Stages 1–5 not
  started (Stage 0 first, by design).

### 2026-07-16 — Add nomadic-movement lead: Van Life Campgrounds
- Owner-supplied lead for the Homestead / nomadic-movement vision.
- Added `hs-4` to the Homestead branch: "Investigate Van Life Campgrounds
  (vanlifecampgrounds.com) as a nomadic-movement connection" (HIGH, not_started),
  mapped onto milestone m8. Website + purpose only — validator passes, no email
  in roadmap.json.
- Recorded the full contact (org, website, info@ business email, purpose) in a
  new `data/roadmap/connections.md` leads log (business contacts only; no private
  individuals). Ran a reputation check on the domain: verdict unknown, but
  registered 4+ years (established, not flagged malicious).

### 2026-07-16 — Add sanitized July MTD work report to the evidence layer
- Stored a **public-safe** digest of the owner's July 1–16 month-to-date report
  as `data/raw-reports/2026-07-16-july-mtd-work-report-digest.md`.
- Redacted (per DATA_SAFETY_POLICY, repo is public): income amounts + per-client
  pay breakdowns, bank/financial details, personal/third-party names and emails,
  reservation/receipt numbers and lodging specifics, and secret names. The full
  unredacted report stays private with the owner, not in this repo.
- Preserved work activity/decisions: 60 confirmed paid labor hours, tax
  knowledge base + 6 manuals, Upstage W-2→1099 transition, Festival/Production
  Atlas fixes, Crew Blueprint course-preview workflow, new print-on-demand
  clothing line + Printify automation spec.
- Verified the file contains no dollar amounts, emails, phones, or redacted names.

### 2026-07-16 — Add 30-day work summary to the evidence layer
- Stored the owner-supplied 30-day work summary (Jun 16 – Jul 16) as
  `data/raw-reports/2026-07-16-30-day-work-summary-digest.md`. Redacted one
  email address to keep it public-safe (DATA_SAFETY_POLICY); all other content
  preserved.
- Confirms/expands real progress across Deadhang (site live, 1099 invoice tool,
  affirmation calendar), Crew Blueprint (3 publication-ready course packets:
  RIG-201 96/100, Bridle Math, Predictive Hazard), Festival Atlas (Production
  Atlas — calendar sorting), and system org (Android file organizer).
- Not yet reflected into roadmap.json — flagged for owner-directed promotion
  (esp. Crew Blueprint course content, which shows more progress than the
  branch currently records). Watcher runs cleanly with the new digest present.

### 2026-07-09 — Record real Deadhang / Contractor Tools progress (owner update)
- Owner reported: website SSL/security fixed, portfolio clean and site running;
  an invoice + finance-tracking system is in place; last 3 years of finances
  sorted; tax filings being brought current.
- Reflected in roadmap.json:
  - `dh-7` (website hardening/SSL + portfolio) → **completed**
  - `dh-5` (business documents) → **in_progress** (finances sorted)
  - New `dh-8` "Resolve tax situation and bring filings current" → **in_progress**
    (HIGH), mapped onto milestone m1
  - Removed the resolved Deadhang blocker "Invoice tracking and payment systems
    incomplete"; refreshed Deadhang current_state; status 30% → 45%
  - Contractor Tools: `ct-2` (invoice MVP) and `ct-4` (payment tracking) →
    **completed**; refreshed current_state; status 15% → 35%
- Validator passes. Re-ran the prioritizer so the backlog reflects the changes.

### 2026-07-09 — Add proposal prioritizer (ranked "work-on-first" backlog)
- Added `scripts/prioritize-proposals.py`: a **read-only** ranker over the
  watcher proposals. It deletes nothing and never edits the proposals or
  `roadmap.json`; it writes `data/roadmap/proposal-backlog.md`.
- Ranking: by the owner's own 30/60/90 windows (earliest first), the current
  "you are here" branch leads its tier, blockers before work items, then
  confidence. Verified the proposals file is byte-identical before/after (md5).
- Also hides candidates already covered in the roadmap via a token-containment
  check (catches reworded promotions the watcher's title-only dedup missed) —
  e.g. the 3 Deadhang items promoted earlier no longer resurface. 117 raw
  candidates → 108 shown (9 already-covered hidden).
- Documented in AGENTS.md §5.

### 2026-07-09 — Promote 3 Deadhang foundation items from the watcher backlog
- Triaged the watcher proposals and promoted the 3 genuinely-new, public-safe
  Deadhang items that sharpen the current 30-day "stabilize the business
  foundation" window (the rest of GPT's suggested promotions already existed):
  - `dh-5` Assemble first-year business document system (plan, formation/EIN
    records, operating agreement)
  - `dh-6` Select and standardize a client MSA / service agreement
  - `dh-7` Finish website hardening (SSL/security) and portfolio cleanup
- Mapped all three onto milestone `m1` ("Solidify Deadhang's foundation") so they
  stay on the linear path (no orphan work). Left `this_week_focus` and the
  30/60/90 windows unchanged — sequencing those is the owner's call.
- Validator passes; items render on the timeline and in the Deadhang branch.
- Backlog note: many watcher candidates remain (mostly Production Atlas /
  Personal Operations); promote further items deliberately, not in bulk.

### 2026-07-09 — Formalize 30/60/90 into roadmap.json + add moved_later (owner-approved)
- Followed GPT's framework-audit handoff to fix the two-sources-of-truth issue.
- Moved GPT's 30/60/90 plan verbatim from the `ninety.js` sidecar into
  `roadmap.json` as a formal `thirty_sixty_ninety` field. `app.js` already read
  this field, so it now renders the 30/60/90 with no sidecar — deleted
  `ninety.js` and its `<script>` include (kept `ninety.css`). One source of
  truth, one renderer.
- Extended `scripts/validate-roadmap.py`: it now checks every
  `thirty_sixty_ninety.windows[].focus_step_ids` resolves to a real work item.
  Verified: live roadmap PASSes; a planted bad focus_step_id FAILs.
- Added the `moved_later` deferred-work status: valid in the validator, with
  dashed/muted styling in the work-item list and timeline dots so deferred work
  stays visible but off the active path. (Also added `completed` styling, which
  the validator already accepted.)
- Updated AGENTS.md §3/§4 to document the new field, the `moved_later` status,
  and the focus_step_ids integrity rule.

### 2026-07-09 — Claude framework audit handoff
- Added `CLAUDE_FRAMEWORK_AUDIT_HANDOFF.md` with a handoff note for Claude and
  the framework audit/recommended sequence to review before larger updates.
- The note directs the next agent to likely follow the audit path: promote the
  30 / 60 / 90 layer into `roadmap.json`, update validation, remove the sidecar
  data once formalized, add moved-later handling, and triage watcher proposals
  through the framework before promotion.
- No roadmap data or production page logic was changed, so no roadmap validation
  run was required.

### 2026-07-09 — 30 / 60 / 90 operating dashboard
- Added a dashboard section for a 30 / 60 / 90 execution layer above the End Goal
  section in `index.html`.
- Added `ninety.css` for the three-window dashboard cards and mobile layout.
- Added `ninety.js` as a standalone first-pass renderer. It reads current
  `roadmap.json` work items by ID, then displays 30-day, 60-day, and 90-day
  operating windows tied to existing branch work items.
- Updated `app.js` with a branch/journey-compatible renderer so the same section
  can later read from `roadmap.json.thirty_sixty_ninety` if the data model is
  formally promoted.
- `roadmap.json` was intentionally not changed in this pass; no roadmap
  validation run was required.

### 2026-07-09 — Documentation cleanup for current branch/journey system
- Cleaned the stale Open Threads section so it no longer claims the watcher or
  validator are missing after both were added.
- Updated the public data-safety policy to match the current repo-root dashboard
  and branch/journey model, removing retired pillar/docs/build-roadmap language.
- Updated the watcher detail cleanup so future proposal runs strip legacy
  pillar-model labels from candidate descriptions before writing proposals.
- `roadmap.json` was not changed, so no roadmap validation run was required.

### 2026-07-09 — Handoff doc for GPT
- Added `CHATGPT_HANDOFF.md`: a current-state orientation for a GPT collaborator
  (points to AGENTS.md/CHANGELOG, the branch/journey data model, the pipeline,
  the scripts, the commit-to-main rule, and safety/evidence rules). Replaces the
  stale pillar-model handoff that only exists on the legacy branch.

### 2026-07-09 — End-to-end flow audit + watcher accuracy fixes
- Audited the full pipeline (process-memories → watcher → validator → dashboard).
  Findings: memory processing is deterministic (8 archives → 518 sources → 880
  chunks, committed output accurate); validator passes on live and catches all
  planted violations; dashboard renders; watcher never writes `roadmap.json`.
- Watcher accuracy: confident mappings are correct (it rightly routes
  invoice→Contractor Tools and market-research→Production Atlas despite
  misleading titles). Found several clearly-mappable items being left unmapped
  because the keyword index ignored branch blockers.
- Fix: `branch_keyword_index` now also draws from each branch's `blockers` and
  `critical_blocker`. Result: unmapped 9 → 2 (the 2 left are genuinely
  ambiguous), already-tracked recognition 10 → 14, no new mis-maps.
- Polished the proposal `detail` field (stripped markdown bold / empty labels).
- Known/accepted: 1 of 124 mapped items is a borderline route (a "roadmap
  milestones" note whose sentence references Homes for Hands scored Homestead
  8 vs Personal-Ops 7). Left as-is — it's what human review catches, and
  title-weighting to fix it would regress the correctly-overridden titles.

### 2026-07-09 — roadmap.json validator
- Added `scripts/validate-roadmap.py` for the current model. Enforces the
  AGENTS.md §4 integrity rules (all step/branch/phase/focus refs resolve, no
  duplicate ids, every branch in exactly one phase, valid `you_are_here`) plus
  enum/range checks (priority, status, lifecycle, phase status, milestone state,
  status_percentage 0-100) and a public-safety scan (email/phone/SSN/card/real
  street address/HTML = error; owner personal name = warning).
- Exit code 0 = pass, 1 = errors, so it can gate commits/CI. Verified: the live
  roadmap PASSes with no warnings; a copy with 11 planted violations FAILs and
  each violation is reported.
- Wired into AGENTS.md §4 and the coordination checklist as the pre-commit step.

### 2026-07-09 — New watcher (branch/journey model)
- Built `scripts/roadmap-watcher.py` for the current model, using the retired
  pillar-model watcher only as reference (the old code was not merged).
- It loads current branches from `roadmap.json`, extracts work-item/blocker
  candidates from `data/raw-reports/*-digest.md`, maps them to branches,
  applies public-safe filtering (`data/schema/roadmap-public-safety.json`),
  de-dupes against the existing roadmap, and writes **proposals only** to
  `data/roadmap/watcher-proposals.json`. It never edits `roadmap.json`.
- First run: 133 claims → 114 new suggestions, 10 already-tracked, 9 unmapped,
  0 unsafe. Verified deterministic and that `roadmap.json` is untouched.
- Fixed a false-positive in the street-address safety check (the schema regex
  matched "way" inside words like "Pathway"); the watcher now uses a stricter,
  word-boundaried, case-sensitive address detector.
- Added `WATCHER_GUIDE.md`; updated `AGENTS.md` §5 (watcher now available as a
  proposal generator, run manually).

### 2026-07-09 — Port useful content from feature branch to main
- Brought over from `claude/repository-review-yvxvn5` (owner-approved):
  `data/roadmap-deep-context/` (2 files — resolves the dangling reference in
  `deep-context-decision-sources.json`), `data/raw-reports/` (10 curated
  digests), `DATA_SAFETY_POLICY.md`, and `data/schema/roadmap-public-safety.json`.
- Did **not** port the 7 root `.zip` archives — `main` already has them under
  `memories/` (correct location) and already processed. The feature-branch
  copies at repo root were misplaced duplicates.
- Did **not** port the old `docs/` dashboard copy (superseded) or the
  old-model watcher (being rebuilt instead).

### 2026-07-09 — Collaboration system + branch audit
- Rewrote `AGENTS.md` into a multi-agent operating guide: commit-to-`main` /
  no-branching rule, the current branch/journey data model, integrity rules,
  and a start/work/finish coordination checklist.
- Added this `CHANGELOG.md` as the shared work log.
- Audited all branches. Findings: `dev` has no unique commits;
  `claude/repository-review-yvxvn5` holds 40 unmerged commits (the old-model
  watcher, curated digests, deep-context files, governance/workflow docs, raw
  memory archives, and a now-superseded `docs/` dashboard copy). Nothing merged
  yet — logged under Open threads for an owner decision.

### 2026-07-09 — Dashboard rebuild & restructure (reconstructed from git)
This session predates the changelog; summarized from commit history.
- Rebuilt the dashboard around the **branch/journey model** and moved the live
  site to the **repo root** (Pages serves from root, not `/docs`); removed the
  duplicate `docs/` copy.
- Reframed into two lenses with a switcher: **Timeline** (linear path, now →
  Homestead) and **Dashboard** (branches grouped by phase, this-week focus,
  ecosystem flow). Added the **End Goal** section and restored the **Homestead**
  and **Land Acquisition** as Phase 2.
- Added **The Vision** page (`present.html`) — a read-only vision document —
  and a per-branch hub (`branch.html`) with a sitemap menu and focused
  sub-views (work / blockers / details).
- Removed the **Skills & Certifications** branch (teaching lives in The Crew
  Blueprint). Rebranded the header to **Deadhang Labor**; dropped 50-year
  framing.
- Hardened `app.js` (guards against missing fields, keyboard access,
  accessible pagination) and defused `scripts/build-roadmap.py` so it can no
  longer overwrite the live `roadmap.json`.
