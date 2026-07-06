---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__schemas__festival.schema.json__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/schemas/festival.schema.json",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 2314,
  "source_sha256": "22c5635fb5b0838c1430be39021670fc2d3702c6b3213962adf2e3d87d166c0d",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/thecrewblueprint-glitch/festival-atlas/schemas/festival.schema.json",
  "title": "Festival Atlas Festival Profile",
  "type": "object",
  "required": [
    "id",
    "name",
    "city",
    "state",
    "country",
    "research_status",
    "sources"
  ],
  "additionalProperties": false,
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9-]+$"
    },
    "name": {
      "type": "string"
    },
    "aliases": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "city": {
      "type": "string"
    },
    "state": {
      "type": "string"
    },
    "country": {
      "type": "string",
      "default": "US"
    },
    "region": {
      "type": "string"
    },
    "month": {
      "type": [
        "integer",
        "null"
      ],
      "minimum": 1,
      "maximum": 12
    },
    "date_window": {
      "type": "string"
    },
    "venue": {
      "type": "string"
    },
    "producer": {
      "type": "string"
    },
    "parent_company": {
      "type": "string"
    },
    "genre": {
      "type": "string"
    },
    "scale": {
      "type": "string"
    },
    "estimated_attendance": {
      "type": [
        "integer",
        "null"
      ]
    },
    "work_window": {
      "type": "string"
    },
    "departments": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "likely_hiring_channels": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "known_or_likely_vendors": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "union_jurisdiction_notes": {
      "type": "string"
    },
    "worker_entry_notes": {
      "type": "string"
    },
    "research_status": {
      "type": "string",
      "enum": [
        "confirmed",
        "needs-verification",
        "lead-only",
        "historical",
        "user-supplied",
        "conflicting-sources"
      ]
    },
    "last_verified_date": {
      "type": [
        "string",
        "null"
      ],
      "format": "date"
    },
    "sources": {
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
