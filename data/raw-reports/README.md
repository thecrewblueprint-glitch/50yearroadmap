# Raw Reports / Curated Digests

This folder holds watcher-ready operational digest files.

Raw memory dumps and imported archives belong in `/memories`. They are source evidence and should remain part of the long-term digest pipeline, but they should not be rendered raw in the public roadmap dashboard.

## Pipeline

```text
/memories raw archives
  ↓
scripts/process-memories.py
  ↓
/memories/processed chunks + indexes
  ↓
curated digest files in /data/raw-reports
  ↓
scripts/roadmap-watcher.py
  ↓
/data/roadmap/watcher-proposals.json
  ↓
approved roadmap state + docs/roadmap.json
```

## Digest Rule

A digest should extract:

- active projects and decisions
- blockers
- completed work
- moved-later items
- conflicts
- evidence references
- pillar mapping
- public-safe summaries

Do not flatten high-meaning roadmap material too early. If the material is primarily about values, identity, emotional meaning, Homes for Hands direction, or long-range roadmap purpose, store it first in `/data/roadmap-deep-context/` and only extract public-safe operational claims into this folder.
