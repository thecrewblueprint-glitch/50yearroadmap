# 05 — Growth Model

**Status:** Documented.

## The strategic position

The command center is **mature and operational**: the dashboard is live, the data
model is stable, the AI pipeline is built, and governance is established. The
remaining work is **polish and scale**, not foundation.

## Remaining work

- **Anti-sprawl scope gates** (roadmap `po-2`, in progress). Controls already
  exist — the validator gate, the `moved_later` status, the prioritizer hiding
  already-covered items, and the 30/60/90 "don't turn the roadmap into a storage
  dump" guardrail. More gating is possible to keep the command center from
  becoming too dense.
- **Downloadable documentation templates** (roadmap `po-5`, not started).
  Reusable templates for investor pitches, market research, and project planning.
  Confirm the desired set with the owner when ready.

## Future direction

- **Database migration** (OPEN_DECISIONS OD-5). The owner plans to move the
  roadmap to a database eventually; JSON is the source of truth for now. Deferred
  until hand-editing JSON becomes the bottleneck.
- **Interactive dashboard** (`INTERACTIVE_DASHBOARD_SPEC.md`). A fully-interactive
  editing surface (drag-and-drop status, direct edits, backend persistence) is
  specified but not built. It rides on the database decision — build it when the
  static/JSON workflow is genuinely limiting, not before.

## The through-line

Like the rest of the ecosystem, this branch grows **demand-pulled**: harden and
document what exists, keep the source of truth clean and safe, and add heavier
machinery (database, interactive editing) only when the simple version becomes the
bottleneck. The command center should stay boring, auditable, and reliable.

## Self-assessment (2026-07)

| Area | Status |
| --- | --- |
| Data model (`roadmap.json`) | Solid — single source of truth, validated |
| Dashboard (live views) | Built (`po-1`, `po-4` complete) |
| 30/60/90 near-term milestones | Built (`po-3` complete) |
| AI pipeline (watcher/prioritizer/validator) | Built, human-in-the-loop |
| Governance + public-safety | Established (incl. CI validator) |
| Canonical documentation | Built — 5 of 5 companies |
| Anti-sprawl scope gates | In progress (`po-2`) |
| Documentation templates | Not started (`po-5`) |
| Database / interactive dashboard | Deferred (OD-5) |
