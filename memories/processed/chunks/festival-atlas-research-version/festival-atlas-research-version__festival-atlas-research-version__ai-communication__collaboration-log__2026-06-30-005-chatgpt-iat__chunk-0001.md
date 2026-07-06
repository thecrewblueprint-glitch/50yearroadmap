---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-30-005-chatgpt-iat__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-30-005-chatgpt-iatse-stats-placement.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1933,
  "source_sha256": "b25b0dbd6cd0430093e80f79e2f66f0621d5c0e5b319929bdf27429fefcb9164",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Status: complete
Created: 2026-06-30
Review after: 2026-07-14
Assistant: ChatGPT
Branch: research-version
Commit: 165f543908c41b8f86aeb63b6980a77c37dc78c2
Access mode: GitHub connector only

# IATSE Stats Placement Update

## Files changed

- iatse.html
- ai-communication/collaboration-log/2026-06-30-005-chatgpt-iatse-stats-placement.md

## Files deleted

None.

## What changed

- Moved the IATSE coverage stats block below the top pagination controls for the local directory.
- Added a small `moveStatsBelowTopPager()` routine inside the current IATSE pagination script.
- The local directory order should now read:
  - Local and craft organizations heading,
  - pagination controls,
  - coverage stats,
  - local cards,
  - bottom pagination controls.

## Documents examined for drift

- ai-communication/DOCUMENT_DRIFT_CONTROL_PROTOCOL.md
- iatse.html
- recent IATSE pagination audit notes

## Documents updated

- This collaboration log.

## Documents intentionally not updated and why

- README.md and ROADMAP.md were not updated because this was a small page-layout adjustment inside the existing IATSE page feature.
- Validation scripts were not updated because no new required file or validation contract was introduced.

## Validation status

Validation not run from this environment.

Human live visual review is acting as the immediate review gate. Automated validation remains a later audit step.

## Human-review status

Pending Aaron visual check after `iatse.html` deploys.

## Known risks

- The IATSE pagination is still inline in `iatse.html`, which was already identified as an architectural cleanup item. The requested placement adjustment was made within the current implementation.
- Browser cache or Pages deployment lag may delay the visible update.

## Next action

Aaron should refresh the IATSE page and confirm the coverage stats now appear below the top pagination controls for the IATSE locals list.
