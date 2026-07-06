---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__ai-communication__collaboration-log__2026-06-23-009-chatgpt-hum__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/ai-communication/collaboration-log/2026-06-23-009-chatgpt-human-input-intake-direction.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1526,
  "source_sha256": "ddff0ca8b3d4eb93026b067f958d26f30f3c38c16ab73edcf6c0eac2fcff8029",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Collaboration Log Entry — Human Input Intake Direction

Status: complete
Created: 2026-06-23
Review after: 2026-07-07
Assistant: ChatGPT
Branch: research-version
Commit: f6a665293f7c7b571e30890bc8f651e6b45d386b

## Files changed

```text
ai-communication/2026-06-23-human-input-intake-direction.md
ai-communication/collaboration-log/2026-06-23-009-chatgpt-human-input-intake-direction.md
```

## What changed

Documented Aaron's new direction: Production Atlas needs a human-input intake and review workflow because the most valuable labor-route, lodging, travel, and vendor-hiring information is usually not publicly posted.

The direction establishes this workflow:

```text
private intake -> private review -> public-safe distilled summary -> repo data update -> validation
```

It explicitly says raw human submissions should not be written directly into the public app or public repository.

## Validation status

Validation not run; documentation-only direction note.

## Known risks

No app/runtime/data files changed.

## Next action

Design the private intake form and review table schema.

Recommended starting point:

```text
Google Forms -> private Google Sheet
```

or:

```text
Airtable form -> private Airtable base
```

Do not connect intake directly to the public app until sanitization/review is proven.

## README impact

Potential future README update if the human-input intake system becomes part of the active app workflow or public data model. Not required for this documentation-only direction note.
