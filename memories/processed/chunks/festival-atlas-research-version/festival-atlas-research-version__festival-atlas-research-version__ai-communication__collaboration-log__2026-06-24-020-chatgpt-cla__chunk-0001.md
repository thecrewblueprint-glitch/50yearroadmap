---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-24-020-chatgpt-cla__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-24-020-chatgpt-claude-notebooklm-research-handoff.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1448,
  "source_sha256": "ea632c091b2f77dceccc2b62b32c4a007eb1a419c52b93e768ee296c8331eb0d",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Claude NotebookLM Research Handoff

Status: complete
Created: 2026-06-24
Review after: 2026-07-08
Assistant: ChatGPT
Branch: research-version
Commit: 12dd0d930dd7a50011dd3a06568ceeae0335bbf7

## Files changed

```text
ai-communication/2026-06-24-chatgpt-to-claude-notebooklm-research-handoff.md
ai-communication/collaboration-log/2026-06-24-020-chatgpt-claude-notebooklm-research-handoff.md
```

## What changed

Created a major handoff for Claude covering the current NotebookLM/source-research workstream.

The handoff summarizes:

```text
active repo/branch instructions
public-safety rules
NotebookLM capture files 001-014
clean URL queue file 010
Goldenvoice / AEG source leads
Danny Wimmer Presents source leads
C3 / Bonnaroo source leads
why current captures are not app-ready
recommended source-extraction workflow
next safe actions for Claude
```

## Validation status

Validation not run; documentation/handoff-only change.

## Known risks

No app/runtime/data files changed.

Claude should not update `data/packages/opportunities-2026.js`, `research-queue-route-updates.js`, or `sources.html` until URL-backed extraction and public-safety review are complete.

## Next action

Claude should begin with:

```text
research/notebooklm-public-research/010-combined-source-url-dump-clean.md
```

Then build reviewed URL-backed extraction packets before any public app data update.

## README impact

Not affected.
