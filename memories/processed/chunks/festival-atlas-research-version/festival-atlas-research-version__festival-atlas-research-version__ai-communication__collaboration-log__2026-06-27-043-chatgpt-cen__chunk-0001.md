---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-043-chatgpt-cen__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-043-chatgpt-center-calendar-festival-labels.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1507,
  "source_sha256": "0f7a89999b1adf11acad2b8c154fa304f2ae1d9c485d145260d8a2a574e65290",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Center Calendar Festival Labels

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: 24fea1f2fbaa30ed4f38860a4b2b70fb1df4ba7e and c85be0f5d9374da69a60c70a664a460db1e7234a

## Files changed

```text
assets/calendar-interactive.js
calendar.html
```

## What changed

Aaron requested that festival names be centered onto their festival day bars.

The calendar combined-bar renderer now places the festival name inside the bright inner festival-show segment instead of on the broader approximate work-window bar.

## Resulting visual model

```text
Outer muted/dashed bar = approximate work window
Inner bright solid segment = festival show days
Festival name = centered inside the bright show-day segment
```

The approximate bar still provides context around the event, but the label now visually belongs to the actual public festival date range.

## Cache/version update

`calendar.html` now loads:

```html
<script src="assets/calendar-interactive.js?v=cal5"></script>
```

## Public safety / accuracy

Approximate work windows remain explicitly labeled as estimates and the calendar disclaimer remains visible.

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for GitHub Pages deploy, then hard refresh the calendar page and inspect the label placement in month and week views.
