# Memory Extraction Workflow

## How to Feed Memory Chunks into the Roadmap

### Three-Step Process

```text
MEMORY CHUNKS
  │
  ├─→ Step 1: READ & DIGEST
  │     What: Manually review chunks or auto-extract patterns
  │     Where: memories/processed/chunks/{archive}/*.md
  │     Output: Create digest file
  │
  ├─→ Step 2: CREATE DIGEST FILE
  │     What: Extract key claims in structured format
  │     Where: data/raw-reports/{date}-{source}-digest.md
  │     Format: Markdown with:
  │       - Active Projects & Decisions
  │       - Blockers Identified
  │       - Code Review & Other Work
  │       - Evidence links back to memory source
  │       - Status: active/completed/deferred/blocked
  │       - Pillar mapping: pillar-1 through pillar-8
  │
  └─→ Step 3: RUN WATCHER + VALIDATE OUTPUT
        What: Extract claims, propose roadmap updates
        Command: python scripts/roadmap-watcher.py
        Output: data/roadmap/watcher-proposals.json

          ↓

        Validate watcher output:
        python scripts/validate-watcher-output.py

          ↓ (YOU REVIEW & DECIDE)

        data/roadmap/projects.json
        data/roadmap/tasks.json

          ↓

        Validate roadmap: python scripts/validate-roadmap.py
        Build dashboard: python scripts/build-roadmap.py
        Commit & push
```

---

## Digest Format Contract

The watcher expects digest files in `data/raw-reports/*-digest.md`.

Use this structure:

```markdown
# Source Digest — YYYY-MM-DD

## Active Projects & Decisions

### Project or Decision Title
**Status:** active  
**Project:** Short project name  
**Decision:** What changed, what was decided, or what must be preserved.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `path/to/source.md` lines 10-20.

## Blockers Identified

1. **Blocker title** — Why this blocks progress or needs a decision.  
   **Status:** blocked  
   **Pillar:** pillar-3 (Production Atlas)  
   Evidence: `path/to/source.md` lines 21-30.

## Code Review & Other Work

### Completed or Reviewed Item
**Status:** completed  
**Description:** What was reviewed, fixed, shipped, or validated.  
**Pillar:** pillar-3 (Production Atlas)  
**Evidence:** `path/to/source.md` lines 31-40.
```

### Required Fields

For each `###` item under **Active Projects & Decisions**:

- `**Status:**` must be one of: `active`, `completed`, `blocked`, `deferred`, `moved_later`.
- `**Pillar:**` must include a valid `pillar-*` value.
- `**Evidence:**` should point back to the source file or digest evidence.

For each numbered blocker under **Blockers Identified**:

- Use bold blocker title: `1. **Title** — explanation`.
- Include `**Status:** blocked`.
- Include `**Pillar:** pillar-*`.
- Include evidence.

The watcher now reads multi-line blocker entries and preserves their pillar mapping. Do not omit the pillar field unless the blocker truly belongs in Personal Operations.

---

## Pillar Map

| Pillar | Name | Current watcher status |
|---|---|---|
| `pillar-1` | Deadhang Labor LLC | active |
| `pillar-2` | The Crew Blueprint | active |
| `pillar-3` | Production Atlas | active |
| `pillar-4` | Contractor Tools | active |
| `pillar-5` | Land Acquisition | future |
| `pillar-6` | Homestead Network | future, but digest claims may still be tracked |
| `pillar-7` | Personal Operations | active |
| `pillar-8` | Skills & Certifications | active |

Production Atlas is active because the July 2026 digests show active repository, research, and app-architecture work.

---

## Watcher + Validation Commands

```bash
# 1. Run watcher
python scripts/roadmap-watcher.py

# 2. Validate watcher output
python scripts/validate-watcher-output.py

# 3. Review proposals
cat data/roadmap/watcher-proposals.json

# 4. Update approved roadmap files
nano data/roadmap/projects.json
nano data/roadmap/tasks.json

# 5. Validate final roadmap
python scripts/validate-roadmap.py

# 6. Build dashboard
python scripts/build-roadmap.py

# 7. Commit
git add data/raw-reports data/roadmap docs scripts MEMORY_EXTRACTION_WORKFLOW.md
git commit -m "Update roadmap from memory digests"
git push
```

---

## Watcher Output Validation

Run this after every digest/proposal change:

```bash
python scripts/validate-watcher-output.py
```

It checks for the exact failure modes found during the July 2026 extraction pass:

- digest files exist but `proposals.projects` is empty
- blockers are all incorrectly mapped to `pillar-7`
- Production Atlas active projects are missing
- frontier is malformed or has no active work
- proposal buckets are missing or malformed
- completed/deferred buckets are unexpectedly empty

If validation fails, fix the watcher or proposal output before moving anything into the final roadmap files.

---

## Current July 2026 Extraction Status

Processed digest coverage exists for:

1. Claude batch
2. Festival Atlas archive
3. Perplexity batch
4. Kimi handoffs
5. ChatGPT Atlas archive
6. Gemini social-enterprise export
7. Contentrepo-main
8. ChatGPT context export
9. Production Atlas workstream sub-archive

The corrected watcher frontier is currently **Production Atlas** because that is where the highest volume of active, blocked, and recently modified work exists.

---

## What Gets Extracted

✅ **Active projects** — work with evidence  
✅ **Completed work** — with source-backed status  
✅ **Blockers** — decisions needed  
✅ **Deferred ideas** — preserved as moved-later  
✅ **Vendor/market patterns** — from research  
✅ **Technical decisions** — from code reviews  
✅ **Business insights** — from planning conversations  
✅ **Roadmap navigation constraints** — primary path, “you are now here,” move-later handling

❌ **Not extracted into public roadmap output:**

- personal addresses or phone numbers
- private email/account details
- financial account details
- hotel/travel booking details
- private jobsite logistics
- unverified private third-party names/contact details
- medical or mental-health details
- unverified claims presented as fact

---

## Keys to Success

1. Create digests, not raw dumps.
2. Put `Status`, `Pillar`, and `Evidence` on every meaningful claim.
3. Preserve blockers under their true pillar.
4. Keep Production Atlas active while repo/research work is current.
5. Run watcher validation after every watcher/proposal change.
6. Keep private or sensitive context out of public roadmap output.
7. Move side quests later instead of deleting them.
