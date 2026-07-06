---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-07-03-001-chatgpt-upd__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-07-03-001-chatgpt-updated-repo-instructions.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 2956,
  "source_sha256": "54ba3cbd6a85ceaa8c5d80cf41f6d6b2a55510e6cff93ff6839ce782d129d081",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Status: complete
Created: 2026-07-03
Review after: 2026-07-17
Assistant: ChatGPT
Branch: research-version
Commit: c29b32802c7de8310a3c46c1c329517331f924a7
Access mode: GitHub connector only

# Updated Repo Instructions

## Files changed

- ai-communication/2026-07-03-updated-repo-instructions.md
- ai-communication/collaboration-log/2026-07-03-001-chatgpt-updated-repo-instructions.md

## Files deleted

None.

## What changed

- Added a new active update-instructions document for future AI assistants.
- Captured current repo operating state:
  - repository and branch rules,
  - static app boundary,
  - public-safety rules,
  - source-link policy,
  - page/runtime ownership,
  - current page list,
  - practical current header nav,
  - filter/search behavior,
  - IATSE search expectations after the `local 26` issue,
  - Employers popup expectations,
  - branch research manifest rules,
  - 2027 rollover state,
  - validation commands,
  - collaboration-log requirements,
  - generated logo asset note,
  - next priorities and caution items.

## Documents examined for drift

- ai-communication/PROJECT_CHAT_GROUP_INSTRUCTIONS.md
- ai-communication/AI_COLLABORATION_PROTOCOL.md
- ai-communication/DOCUMENT_DRIFT_CONTROL_PROTOCOL.md
- ai-communication/PRODUCT_ROADMAP.md
- README.md
- ROADMAP.md
- package.json
- data/packages/branch-research-manifest.js
- assets/atlas-core-v2.js
- tools/validate-static-app.js
- tools/validate-branch-research-packages.js
- tools/validate-data.js

## Documents updated

- ai-communication/2026-07-03-updated-repo-instructions.md
- This collaboration log.

## Documents intentionally not updated and why

- README.md was not updated because this change adds a new assistant-facing instruction set rather than changing public app behavior.
- ROADMAP.md was not updated because no roadmap scope or milestone changed.
- Existing protocol files were not edited because this new document supplements rather than replaces them.
- Validation scripts were not updated because no validation contract changed.

## Validation status

Validation not run from this environment.

Human live visual review is acting as the immediate review gate.

Automated validation remains a later audit step.

## Human-review status

Pending Aaron review of the new update-instructions file.

## Known risks

- The new instruction set captures current state but does not automatically resolve older doc disagreement about whether Schedule belongs in header nav. It records README/current files as the practical state.
- The generated Production Atlas logo is noted as a sandbox asset but has not been committed into the repo.
- IATSE search was recently changed and still needs live visual confirmation.

## Next action

Aaron or the next assistant should use `ai-communication/2026-07-03-updated-repo-instructions.md` as a current compact handoff before starting new repo work, then verify against actual current files on `research-version`.
