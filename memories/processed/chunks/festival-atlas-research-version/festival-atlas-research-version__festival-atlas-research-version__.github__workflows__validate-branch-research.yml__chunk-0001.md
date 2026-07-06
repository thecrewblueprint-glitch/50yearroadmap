---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__.github__workflows__validate-branch-research.yml__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/.github/workflows/validate-branch-research.yml",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 503,
  "source_sha256": "3bde623436edf780ef084bb51c4888dcfba62519c3f10c401ef73079f241c9f9",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

name: Validate Production Atlas

on:
  push:
    branches:
      - main
      - research-version
  pull_request:
    branches:
      - main
      - research-version

jobs:
  validate-production-atlas:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Validate branch research and static app
        run: npm run validate:all
