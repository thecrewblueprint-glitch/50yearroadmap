---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__data__README.md__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/data/README.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 1233,
  "source_sha256": "ebf3926c6ec8b67070db7b18d371644070507e246ec57b8c389a77b775ba14d0",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Research Data Directory

This branch is the market-research version of Festival Atlas. Use this directory for structured, expandable research data.

## Purpose

The current app still uses embedded data inside `index.html`. This branch prepares the project for data expansion by defining clean data targets, schemas, templates, and validation rules before the app is refactored to load external JSON.

## Directory plan

```text
data/
├── README.md
├── festivals.json
├── companies.json
├── sources.json
└── notes/
```

## Research rules

1. Every festival or company entry must include a `research_status` value.
2. Every claim that affects hiring, production vendor identity, union jurisdiction, or job pathway should have a source record.
3. Do not treat old vendor relationships as current unless recently verified.
4. Separate confirmed facts from leads, assumptions, and user-supplied notes.
5. Use consistent IDs so profiles can be cross-linked later.

## Recommended status values

```text
confirmed
needs-verification
lead-only
historical
user-supplied
conflicting-sources
```

## Recommended source confidence values

```text
primary-official
secondary-credible
job-board-listing
social-or-forum
user-supplied
unknown
```
