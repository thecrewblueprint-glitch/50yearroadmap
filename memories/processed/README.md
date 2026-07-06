# Processed AI Memory

Generated from files stored in `/memories`. Original ZIP and JSON files remain unchanged.

## Folders
- `chunks/`: AI-ready Markdown chunks split by archive and source file.
- `indexes/`: JSON/JSONL navigation indexes for agents.
- `_extracted_raw/`: safely extracted raw ZIP contents for audit/reference.

## Rules
- Generated files are rebuildable.
- Source archives are the immutable memory evidence.
- Chunk files include YAML-style JSON metadata headers.
- Text is split with overlap and no truncation.
