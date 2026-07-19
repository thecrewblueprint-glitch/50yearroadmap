# 03 — AI Pipeline

**Status:** Documented (built; runs on demand, human-in-the-loop).

The pipeline turns raw, messy evidence into **reviewable proposals** — never
direct edits. A human promotes what they approve. This is principle 1 in action:
"chaos goes in, auditable structure comes out."

## The flow

```text
RAW MEMORY ARCHIVES
  ↓  scripts/process-memories.py  (+ GitHub Action)  [automated]
/memories/processed chunks + indexes
  ↓  manual curation                                 [human]
curated digests in /data/raw-reports
  ↓  scripts/roadmap-watcher.py   (proposals only — never edits roadmap.json)
data/roadmap/watcher-proposals.json
  ↓  scripts/prioritize-proposals.py  (ranked "work on first" backlog)
data/roadmap/proposal-backlog.md
  ↓  owner records approvals in data/roadmap/promotions.json   [human-in-the-loop]
  ↓  scripts/promote-proposals.py  (applies + auto-IDs + validates, rollback on fail)
roadmap.json  (branch model)
  ↓  scripts/validate-roadmap.py  (gate: refs, enums, public-safety)
  ↓  commit to main → dashboard
```

There are **two update paths**, both ending at the promote step: **evidence-based**
(the watcher proposes from digests) and **real-world progress** the watcher can't
see (Drive, website, "I filed my taxes") — the latter is described directly in
`promotions.json`. See `WATCHER_GUIDE.md` for the full workflow.

## The scripts

- **`process-memories.py`** — chunks raw archives into `/memories/processed`
  (zip-slip-safe). Automated via `.github/workflows/process-memories.yml` on
  pushes of `memories/*.zip`.
- **`roadmap-watcher.py`** — reads curated digests, maps candidate work
  items/blockers to branches, applies public-safety filters, dedups, and writes
  **proposals only** to `watcher-proposals.json`. It **never edits**
  `roadmap.json`. (Guide: `WATCHER_GUIDE.md`.)
- **`prioritize-proposals.py`** — read-only ranking of proposals into
  `proposal-backlog.md` (by 30/60/90 window → current branch → blockers →
  confidence). **Deletes nothing** (principle 5).
- **`promote-proposals.py`** — the "apply" step. Reads `promotions.json` (your
  approved changes: status updates, new work items, new blockers), writes them
  into `roadmap.json` with auto-assigned IDs and enum checks, runs the validator,
  and **rolls back** if validation fails. Resets `promotions.json` on success so
  nothing is applied twice. This is the only script that writes `roadmap.json`,
  and only from changes you approved.
- **`validate-roadmap.py`** — the gate: checks references, status enums, ranges,
  duplicates, and public-safety (PII/street-address/HTML). Exit 0 pass / 1 fail.
  Wired into CI via `.github/workflows/validate-roadmap.yml`.

## Deep context (parallel route)

```text
/data/roadmap-deep-context
  ↓
/data/roadmap/deep-context-decision-sources.json   (index, used by the watcher)
  ↓
watcher decision context for priority, sequencing, and project boundaries
```

## Why human-in-the-loop

Promotion into `roadmap.json` is **deliberately manual.** The watcher only
proposes; a person decides what becomes real roadmap state. This prevents the
roadmap from filling with unreviewed, possibly-unsafe, or low-signal items — and
it keeps the owner in control of direction.

## Working convention (watcher output)

`watcher-proposals.json` and `proposal-backlog.md` are **regenerated** every run,
so a re-run produces a diff even when nothing meaningful changed. Convention:
keep them tracked (the backlog is valued and must not be silently dropped), but
**revert incidental regeneration** unless you are actually promoting/approving new
proposals. Do not commit churn for its own sake.
