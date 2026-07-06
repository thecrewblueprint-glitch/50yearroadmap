---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-25-031-chatgpt-dar__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-25-031-chatgpt-dark-ui-modal-scroll-fix.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1618,
  "source_sha256": "65b5942e0b6e18c57f1c8422a345e87d50b966ed57d1853ad03ee9a305e68a92",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Dark UI and Modal Scroll Fix

Status: incomplete
Created: 2026-06-25
Review after: 2026-07-09
Assistant: ChatGPT
Branch: research-version
Commit: 6084f02e0cdeedb5bd6cbbe35a64cf74ed2ee19a

## Files changed

```text
assets/atlas.css
```

## What changed

Aaron reported two immediate UI regressions after the public UI/UX makeover pass:

```text
1. Popup/modal windows no longer scroll.
2. The new white page background is not desired.
```

This update restores a dark public UI theme and changes modal scrolling behavior.

## Modal scrolling fix

The modal overlay now handles vertical scroll:

```css
.modal {
  align-items: flex-start;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
```

The modal box no longer forces its own internal max-height/overflow lock:

```css
.modalbox {
  max-height: none;
  overflow: visible;
}
```

Mobile modal behavior was also adjusted so long popups can scroll from the page overlay rather than trapping content inside a fixed-height card.

## Dark UI restoration

The public theme was moved away from the white/light redesign and back to a dark production-style UI:

```text
dark page background
dark cards
dark tables
dark modals
dark map popups
dark schedule/Gantt surfaces
gold active accents
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Aaron will likely provide screenshots for targeted visual tuning. Use screenshots as the source of truth for the next UI pass rather than making broad visual assumptions.
