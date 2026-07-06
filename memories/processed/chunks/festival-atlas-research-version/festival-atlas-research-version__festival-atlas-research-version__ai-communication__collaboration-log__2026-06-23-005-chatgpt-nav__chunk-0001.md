---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-23-005-chatgpt-nav__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-23-005-chatgpt-nav-consistency-plan.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1411,
  "source_sha256": "f67c6925e63d414de9eda69378967a7f9ae0cd01bae9a018c450c48911fa7256",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Nav Consistency and Next Plan

Status: complete
Created: 2026-06-23
Review after: 2026-07-07
Assistant: ChatGPT
Branch: research-version
Commit: 65a48b7796dbe67664d04b091093b4a0c0a9d516 through 4ac62e4d47e55e6e664a277153458d9b9245e2a9

## Files changed

```text
calendar.html
opportunities.html
branches.html
employers.html
iatse.html
matrix.html
analytics.html
sources.html
map.html
schedule.html
tools/validate-static-app.js
ai-communication/2026-06-23-next-actions-plan.md
ai-communication/collaboration-log/2026-06-23-005-chatgpt-nav-consistency-plan.md
```

## What changed

Implemented Step 1 from the next-actions plan: global navigation consistency.

Updated active secondary pages so Home and Guide are separate links instead of a combined `Home / Guide` label.

Updated `tools/validate-static-app.js` so active pages fail validation if they contain `Home / Guide` or lack separate Home and Guide links.

Added:

```text
ai-communication/2026-06-23-next-actions-plan.md
```

## Validation status

Passed, according to Aaron's 2026-06-23 project chat update.

## Known risks

No known validation blocker for this entry. Browser visual review can still be done as a normal follow-up.

## Next action

Proceed to Step 2 from the next-actions plan: Analytics command-center planning.

## README impact

Not affected. README already documents separate Home and Guide page roles.
