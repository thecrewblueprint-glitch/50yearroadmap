---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__incomplete__README.md__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/incomplete/README.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1231,
  "source_sha256": "50c7a867314c5bb8a200674b5e1cfbd47ec3f253540a606696d0d11ee0a64345",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Incomplete Collaboration Logs

This folder stores collaboration-log entries that are not safe to delete during routine cleanup.

## What belongs here

Move old collaboration logs here when they are older than 14 days and marked:

```text
Status: incomplete
Status: blocked
```

This keeps unresolved work auditable without forcing every assistant to read a giant active ledger.

## Cleanup rule

Do not delete files from this folder during automatic or routine cleanup.

Aaron can manually delete files here when he decides the unresolved item no longer matters.

A later assistant can also create a new root collaboration-log entry that marks an incomplete file resolved or superseded.

## Required fields to preserve

Each moved file should still include:

```text
Status
Created
Review after
Assistant
Branch
Commit SHA or range
Files changed
Validation status
Known risks
Next action
README impact
```

## Recommended review cadence

Every two weeks:

1. Review root collaboration-log files older than 14 days.
2. Delete old `complete` or `superseded` files if they are no longer useful.
3. Move old `incomplete` or `blocked` files into this folder.
4. Review this folder manually for items Aaron wants to finish or discard.
