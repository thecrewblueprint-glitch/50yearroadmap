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

- **Watcher not active.** A watcher pipeline exists on branch
  `claude/repository-review-yvxvn5` but targets the retired pillar model and
  was never merged. Rebuilding it for the current branch/journey model is a
  planned project (pairs with the future database migration).
_(No open threads at the moment.)_
- **No automated `roadmap.json` validator yet.** Integrity is checked by hand
  against the rules in `AGENTS.md` §4. A validator for the current model is
  planned.

---

## Entries

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
