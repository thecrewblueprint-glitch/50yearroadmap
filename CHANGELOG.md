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
- **No automated `roadmap.json` validator yet.** Integrity is checked by hand
  against the rules in `AGENTS.md` §4. A validator for the current model is a
  natural next step (the watcher already does the reference-resolution work).
- **No automated `roadmap.json` validator yet.** Integrity is checked by hand
  against the rules in `AGENTS.md` §4. A validator for the current model is
  planned.

---

## Entries

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
