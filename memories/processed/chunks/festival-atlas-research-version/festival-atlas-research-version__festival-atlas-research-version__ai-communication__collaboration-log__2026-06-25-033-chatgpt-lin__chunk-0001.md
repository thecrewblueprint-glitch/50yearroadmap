---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-25-033-chatgpt-lin__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-25-033-chatgpt-link-regression-fix.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1950,
  "source_sha256": "2c33465604b7f4941edd97cf25ffcf05bd380249f8e9e8b1d2e190cc66dfc292",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Link Regression Fix

Status: incomplete
Created: 2026-06-25
Review after: 2026-07-09
Assistant: ChatGPT
Branch: research-version
Commit: 4bfc7dd12e02f71db9fda7636dc3ab9bad384fcf and 721b4e8758306e2ca527e29323deb526b47ad6b7

## Files changed

```text
assets/home-guide-page.js
assets/approx-date-labels.js
```

## What happened

Aaron reported that links were broken after the screenshot-targeted UI polish pass.

Likely cause: recent helper-script changes rewrote DOM content after the core app renderer created links and onclick handlers. Broad `innerHTML` rewrites and persistent MutationObserver polishing can break clickable cards, inline handlers, anchors, and modal behavior.

## What changed

### `assets/home-guide-page.js`

Removed the department-picker overlay polish layer that:

```text
- injected extra stylesheet rules
- rewrote the “Your branch” heading
- inserted helper text
- edited pathway count labels
- appended extra action labels
- kept a broad MutationObserver running against the home app area
```

Returned it to the safer home-guide footer behavior only.

### `assets/approx-date-labels.js`

Removed broad public DOM rewrite behavior that:

```text
- scanned many node types
- rewrote innerHTML for labels
- removed rendered blocks after the app generated links
- observed the entire document for ongoing rewrites
```

Kept only:

```text
- taxonomy package load trigger
- route research update load trigger
- narrow approximate-date label helper
- openOpportunity wrapper for refresh timing
```

## Validation status

Validation not run; connector session cannot run local repo validation.

Required next command:

```bash
npm run validate:all
```

## Next action

Refresh and confirm links/cards/buttons work again before making any new UI edits. Future visual changes should be made directly in `assets/atlas-core-v2.js` and `assets/atlas.css`, not through broad DOM-rewrite overlay scripts.
