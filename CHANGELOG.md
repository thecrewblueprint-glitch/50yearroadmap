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
