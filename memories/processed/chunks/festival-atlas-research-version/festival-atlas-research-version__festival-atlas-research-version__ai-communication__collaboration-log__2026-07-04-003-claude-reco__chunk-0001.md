---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-07-04-003-claude-reco__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-07-04-003-claude-record-schema-template.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1683,
  "source_sha256": "8be737750be56f48f8064d66fb7076f6d64c2bc868fb1e2fcb679dcc85aceaa8",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Status: complete
Created: 2026-07-04
Review after: 2026-07-18
Assistant: Claude
Branch: research-version
Commit: pending-same-commit

# Festival record schema template + completeness gate

## Access mode

Full local shell (can run `npm run validate:all`).

## Context

Second half of the agent-guardrails work: make bulk festival entry
structurally correct so a high-volume agent produces complete records the
first time instead of the human catching gaps later.

## Files changed

- `data/packages/OPPORTUNITY_RECORD_SCHEMA.md` — added a "How to add a festival
  (copy-paste template)" section: the real `opp({...})` insertion format,
  department presets (full/edm/music/standard), a filled real example (Wonky
  Woods), the coords-file pin step, and the validator rules.
- `tools/validate-data.js` — added a completeness gate: any record with
  `visibleInActive2026View: true` must have non-empty `city`, `state`,
  `region`, and `departments`. Incomplete records must stay hidden until
  verified.
- `AGENTS.md` — points agents to the schema doc for adding/editing records.

## Verification

- `npm run validate:all` passes 3/3. All 105 currently-visible records already
  satisfy the completeness gate (0 missing city/state/region/departments), so
  the check is non-breaking today and catches future incomplete visible cards.
- Negative-tested: a visible record with empty city/state/region and no
  departments triggers four distinct failures.

## Validation status

`npm run validate:all` → passed 3/3.

## Next action

None required. The bulk-entry path is now: read schema doc → copy template →
fill known fields → validate. Incomplete records fail the gate unless hidden.
