---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__archive__legacy-runtime__atlas-core-legacy-note.md__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/archive/legacy-runtime/atlas-core-legacy-note.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 465,
  "source_sha256": "b2aa5f3b9d13f9699d9e98da51c595badafe222d88f355ee339f2ac079ce41dd",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Legacy `assets/atlas-core.js`

The original `assets/atlas-core.js` was created during the first multi-page split and still contained popup rendering that exposed source links directly inside popups.

It has been retired from the active architecture.

The active app core is now:

```text
assets/atlas-core-v2.js
```

The current `assets/atlas-core.js` path is retained only as a lightweight compatibility loader for older page shells that may still reference it.
