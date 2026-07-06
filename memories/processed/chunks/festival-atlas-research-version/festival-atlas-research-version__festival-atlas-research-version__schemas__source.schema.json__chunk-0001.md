---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__schemas__source.schema.json__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/schemas/source.schema.json",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1484,
  "source_sha256": "e6040c9a426b87cdab0ec229fe4e3f843dfab7794c12e30db6f23fe033008d96",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/thecrewblueprint-glitch/festival-atlas/schemas/source.schema.json",
  "title": "Festival Atlas Source Record",
  "type": "object",
  "required": [
    "id",
    "title",
    "url",
    "source_type",
    "confidence",
    "date_accessed"
  ],
  "additionalProperties": false,
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9-]+$"
    },
    "title": {
      "type": "string"
    },
    "url": {
      "type": "string"
    },
    "publisher": {
      "type": "string"
    },
    "source_type": {
      "type": "string",
      "enum": [
        "official-site",
        "careers-page",
        "press-release",
        "vendor-site",
        "union-local",
        "job-board",
        "government",
        "industry-org",
        "news",
        "social",
        "user-note",
        "other"
      ]
    },
    "confidence": {
      "type": "string",
      "enum": [
        "primary-official",
        "secondary-credible",
        "job-board-listing",
        "social-or-forum",
        "user-supplied",
        "unknown"
      ]
    },
    "date_published": {
      "type": [
        "string",
        "null"
      ]
    },
    "date_accessed": {
      "type": "string",
      "format": "date"
    },
    "claims_supported": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "notes": {
      "type": "string"
    }
  }
}
