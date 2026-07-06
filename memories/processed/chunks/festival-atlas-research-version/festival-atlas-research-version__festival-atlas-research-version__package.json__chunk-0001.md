---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__package.json__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/package.json",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 542,
  "source_sha256": "7c7b7df9bbccf53a1bb3c71c28e5ab2091abd850a252b560be81a0277f8e7c7e",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

{
  "name": "festival-atlas-research-version",
  "version": "0.1.0",
  "private": true,
  "description": "Research expansion branch for Festival Atlas / Production Atlas.",
  "scripts": {
    "validate:data": "node tools/validate-data.js",
    "validate:branch-research": "node tools/validate-branch-research-packages.js",
    "validate:static-app": "node tools/validate-static-app.js",
    "validate:all": "npm run validate:data && npm run validate:branch-research && npm run validate:static-app"
  },
  "engines": {
    "node": ">=18"
  }
}
