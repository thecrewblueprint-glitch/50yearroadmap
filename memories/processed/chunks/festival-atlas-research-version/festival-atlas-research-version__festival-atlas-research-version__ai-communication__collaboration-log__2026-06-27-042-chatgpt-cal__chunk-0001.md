---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-27-042-chatgpt-cal__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-27-042-chatgpt-calendar-overlaid-date-bars.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1836,
  "source_sha256": "f1ea5639cb961f2e8ae81ca21efadf61f0a807d4b5c49ab937f0682086666e4f",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Calendar Overlaid Date Bars

Status: incomplete
Created: 2026-06-27
Review after: 2026-07-11
Assistant: ChatGPT
Branch: research-version
Commit: 609eb223f7f7cae6aaf0a42b4d97de4ff997b704 and b7508a6c5f5cc028bfc18485277981daf4fa260b

## Files changed

```text
assets/calendar-interactive.js
calendar.html
```

## What changed

Aaron said the two separate calendar bars looked messy and asked to overlay them.

The calendar now renders each festival as a single combined row:

```text
Outer muted/dashed bar = approximate work window
Inner bright solid segment = actual festival show days
```

## Why

The previous version stacked the approximate work window and festival show dates as two separate bars. That was accurate but visually noisy. The new version preserves the distinction while reducing clutter.

## Behavior

```text
Month view: one row per festival per week, with show days overlaid inside the work-window bar.
Week view: one row per festival, with show days overlaid inside the work-window bar.
Legend updated to explain the overlaid bar design.
Status strip updated to explain outer/inner meaning.
Day detail modal still separates show days from approximate work-window-only days.
```

## Cache/version update

`calendar.html` now loads:

```html
<script src="assets/calendar-interactive.js?v=cal4"></script>
```

## Public safety / accuracy

Approximate work windows remain labeled as estimates and the date disclaimer remains visible. The app does not claim exact load-in, strike, or crew-call dates.

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Validate, wait for Pages deploy, hard refresh the calendar page, and visually inspect month/week views for less clutter.
