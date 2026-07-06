---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__schemas__company.schema.json__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/schemas/company.schema.json",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1783,
  "source_sha256": "58d7e4b8de26e2549ccf10779c3753571f56cbc59360cded5ac96e050139df77",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/thecrewblueprint-glitch/festival-atlas/schemas/company.schema.json",
  "title": "Festival Atlas Company Profile",
  "type": "object",
  "required": [
    "id",
    "name",
    "company_type",
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
    "company_type": {
      "type": "string"
    },
    "service_categories": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "headquarters": {
      "type": "string"
    },
    "markets_served": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "website": {
      "type": "string"
    },
    "careers_url": {
      "type": "string"
    },
    "contact_url": {
      "type": "string"
    },
    "known_festival_connections": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "worker_entry_notes": {
      "type": "string"
    },
    "classification_notes": {
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
