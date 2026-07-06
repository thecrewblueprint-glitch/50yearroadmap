---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-29-001-chatgpt-opp__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-29-001-chatgpt-opportunity-date-sort.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1528,
  "source_sha256": "41eb074ab76ff02fffa15d729dddbe3c0273af23d9ba48a22d3197cf4ba04a88",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Status: complete
Created: 2026-06-29
Review after: 2026-07-13
Assistant: ChatGPT
Branch: research-version
Commit: 6e33efae83f69d7c8fbe50bf17e43ee42c410dfd

# Opportunity Date Sort Fix

## Files changed

- `assets/opportunities-promoter-filter.js`

## Validation status

Validation not run in this connector session. Required follow-up command:

```bash
npm run validate:all
```

## What changed

- Added Opportunities-page date-ordering behavior that sorts rendered opportunity cards by parsed `startDate`.
- Unknown or missing start dates sort last.
- Ties sort alphabetically by opportunity name.
- Added a MutationObserver so the chronological order is re-applied after the core renderer updates the Opportunities grid.
- Preserved existing Opportunities filters: state, department, producer/promoter, and month.

## Known risks

- This is a page-specific patch in `assets/opportunities-promoter-filter.js`, not a core rewrite of `sortOpportunities()` in `assets/atlas-core-v2.js`.
- A later cleanup should move the date-first sort into core runtime sorting so Schedule and other shared browse lists follow the same rule without page-specific DOM reordering.

## Next action

- Run `npm run validate:all` locally or in GitHub Actions.
- Spot-check `opportunities.html` on mobile and confirm 2026 festival records render before 2027 rollover records when no date/month filter is active.

## README impact

No README update made. This was a narrow runtime behavior fix for the existing Opportunities page filter/sort behavior.
