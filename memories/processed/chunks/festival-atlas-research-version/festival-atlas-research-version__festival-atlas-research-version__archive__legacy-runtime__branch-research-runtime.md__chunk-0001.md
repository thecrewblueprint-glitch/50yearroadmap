---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__archive__legacy-runtime__branch-research-runtime.md__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/archive/legacy-runtime/branch-research-runtime.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 546,
  "source_sha256": "494b61c10203e37fdeb2ed4340e2c6d1d394b90af76205649059e78299374bc0",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Legacy `data/packages/branch-research-runtime.js`

This runtime was used during the transitional single-page-to-multi-page phase to override opportunity popups and load branch research packages.

It is retired because the active multi-page core now performs this work directly:

```text
assets/atlas-core-v2.js
```

Reason archived:

- Duplicated branch package loading.
- Duplicated popup rendering.
- Older popup behavior included source links inside popups.
- The active code now keeps popups clean and moves source links to `sources.html`.
