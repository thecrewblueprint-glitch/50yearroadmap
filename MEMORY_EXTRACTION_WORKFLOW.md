# Memory Extraction Workflow

## How to Feed 879 Memory Chunks into the Roadmap

### Three-Step Process

```
MEMORY CHUNKS (879 total)
  │
  ├─→ Step 1: READ & DIGEST
  │     What: Manually review chunks (or auto-extract patterns)
  │     Where: memories/processed/chunks/{archive}/*.md
  │     Output: Create digest file
  │
  ├─→ Step 2: CREATE DIGEST FILE
  │     What: Extract key claims in structured format
  │     Where: data/raw-reports/{date}-{source}-digest.md
  │     Format: Markdown with:
  │       - Active Projects & Decisions
  │       - Blockers Identified
  │       - Evidence links back to memory source
  │       - Status (active/completed/deferred)
  │       - Pillar mapping
  │
  └─→ Step 3: RUN WATCHER
        What: Extract claims, propose roadmap updates
        Command: python scripts/roadmap-watcher.py
        Output: watcher-proposals.json (new proposals)
        
          ↓ (YOU REVIEW & DECIDE)
        
        data/roadmap/projects.json (populate from proposals)
        data/roadmap/tasks.json (break projects into tasks)
        
          ↓
        
        Validate: python scripts/validate-roadmap.py
        Build: python scripts/build-roadmap.py
        Commit & Push
        
          ↓
        
        Dashboard updates on GitHub Pages
```

---

## Example: Claude Batch (222 chunks)

### Step 1: Read the Chunks

```bash
# See what's in Claude batch
ls memories/processed/chunks/Claude-Batch-2026-07-05/ | wc -l
# Output: 222 chunks

# Pick key files to read (don't read all 222 — sample strategically)
cat memories/processed/chunks/Claude-Batch-2026-07-05/*GitHub*.md
cat memories/processed/chunks/Claude-Batch-2026-07-05/*Business*.md
cat memories/processed/chunks/Claude-Batch-2026-07-05/*Invoice*.md
cat memories/processed/chunks/Claude-Batch-2026-07-05/*Dashboard*.md
```

**Time estimate:** 30-60 min to skim key conversations

### Step 2: Create Digest File

Save findings to: `data/raw-reports/2026-07-06-claude-batch-digest.md`

Example format:

```markdown
# Claude Batch Digest — 2026-07-06

## Active Projects & Decisions

### Website Portfolio
**Status:** Planning phase  
**Project:** Deadhang Labor LLC website redesign  
**Decision:** Phased approach (learn → profile → portfolio → architecture → build)  
**Pillar:** pillar-1  
**Evidence:** Business website planning conversation

### Crew Blueprint MVP
**Status:** Critical blocker  
**Decision:** Must reach MVP before Deadhang cross-linking  
**Pillar:** pillar-2  
**Evidence:** User explicit priority statement

## Blockers

1. Crew Blueprint MVP — blocks Deadhang website integration
   Evidence: "have to make crew blueprint 100% as MVP first"

## Code Review & Security

**Status:** Completed  
**Description:** Security best practices documented  
**Pillar:** pillar-4  
**Evidence:** Code review conversation
```

**Time estimate:** 10-15 min to write digest

### Step 3: Run Watcher

```bash
cd /home/user/50yearroadmap

# Watcher reads ALL available memory sources including:
# - Processed memory chunks (from archives)
# - Raw report digests (from data/raw-reports/)
python scripts/roadmap-watcher.py
```

**Output:** `data/roadmap/watcher-proposals.json`

Example:

```json
{
  "frontier": {
    "pillar_id": "pillar-2",
    "pillar_title": "The Crew Blueprint",
    "priority": "high",
    "active_work": 2,
    "blockers": 1,
    "reasoning": "Crew Blueprint MVP blocks Deadhang; critical path item"
  },
  "proposals": {
    "projects": [
      {
        "id": "project-crew-blueprint-mvp",
        "title": "Crew Blueprint MVP completion",
        "purpose": "Build minimum viable training platform",
        "status": "active",
        "priority": "critical",
        "pillar_id": "pillar-2",
        "evidence": "User priority: MVP first before cross-linking"
      },
      {
        "id": "project-deadhang-website",
        "title": "Deadhang Labor LLC website + portfolio",
        "purpose": "Professional portfolio with personality-driven about section",
        "status": "blocked",
        "priority": "high",
        "pillar_id": "pillar-1",
        "blocked_by": ["project-crew-blueprint-mvp"],
        "evidence": "Website planning phase, blocked on Blueprint MVP"
      }
    ],
    "blockers": [
      {
        "title": "Portfolio image curation needed",
        "status": "blocked",
        "pillar_id": "pillar-1",
        "action": "REQUIRES DECISION: Review photos and select best work"
      }
    ]
  }
}
```

**Time estimate:** 2-5 min (watcher runs automatically)

### Step 4: You Validate & Update Roadmap

```bash
# Review proposals
cat data/roadmap/watcher-proposals.json

# Copy approved projects to roadmap
# (edit data/roadmap/projects.json, add from proposals)

# Run validator (catches sensitive data)
python scripts/validate-roadmap.py

# Build dashboard
python scripts/build-roadmap.py

# Commit
git add data/roadmap docs/roadmap.json
git commit -m "Update roadmap with Claude batch digest findings"
git push origin main
```

**Time estimate:** 20-30 min (review + editing + validation)

---

## How to Do This for All 879 Chunks

### Option A: Sampling (Fast, Good Coverage)

Pick **5-7 archives** by importance:

1. **Claude batch** (222 chunks) — code decisions, business planning ← START HERE
2. **Festival atlas** (452 chunks) — research, vendor patterns, opportunities
3. **Perplexity batch** (81 chunks) — market research, planning
4. **Kimi handoffs** (38 chunks) — project state snapshots
5. **ChatGPT production atlas** (64 chunks) — tool decisions, app status
6. **Contentrepo** (2 chunks) — small, can skim
7. **Gemini social enterprise** (2 chunks) — small, can skim

**For each:**
- Skim 10-20 key files (not all)
- Create 1 digest file (5-10 min each)
- Run watcher (automatic)
- Update roadmap (20 min)

**Total time:** 4-5 hours to digest all 7 archives

### Option B: Guided Extraction (Best Quality)

Have me review specific archives with you:

```bash
# Step 1: I analyze the archive
# Step 2: I show you key findings
# Step 3: You review + approve
# Step 4: Create digest together
# Step 5: Feed to watcher
```

**Time:** 30-60 min per archive

---

## Recommended First Week

**Monday:** Claude batch digest (START HERE — you did Step 1 already!)
**Tuesday:** Festival atlas sampling (focus on vendor + lodging patterns)
**Wednesday:** Perplexity research digest (market analysis, business insights)
**Thursday:** Kimi handoffs review (project state snapshots)
**Friday:** Run full watcher, update roadmap, validate & publish

**One hour per day = complete extraction by Friday**

---

## Keys to Success

1. **Don't try to read all 879 chunks** — sample strategically
2. **Create digests, don't raw-dump chunks** — structure = extractable
3. **Link every claim to evidence** — watcher needs proof
4. **Keep digests public-safe** — no names, contacts, financial data
5. **Run watcher after each digest** — incremental, not batch
6. **Validate before committing** — safety gate catches leaks

---

## What Gets Extracted

✅ **Active projects** — work with evidence  
✅ **Completed work** — with dates/details  
✅ **Blockers** — decisions needed  
✅ **Deferred ideas** — not deleted, just moved later  
✅ **Vendor/market patterns** — from research  
✅ **Technical decisions** — from code reviews  
✅ **Business insights** — from planning conversations  

❌ **NOT extracted:**
- Personal data (names, addresses, phone)
- Financial details (pay, taxes, accounts)
- Private conversations
- Unverified speculation

---

## Commands You'll Use (Repeatedly)

```bash
# 1. Create digest (you write, 10 min)
cat > data/raw-reports/YYYY-MM-DD-{source}-digest.md << 'EOF'
# Your digest content here
EOF

# 2. Run watcher (automatic, 1 min)
python scripts/roadmap-watcher.py

# 3. Review proposals (you read, 10 min)
cat data/roadmap/watcher-proposals.json

# 4. Update roadmap (you edit, 15 min)
nano data/roadmap/projects.json
nano data/roadmap/tasks.json

# 5. Validate (automatic, 1 min)
python scripts/validate-roadmap.py

# 6. Build & publish (automatic, 1 min)
python scripts/build-roadmap.py

# 7. Commit
git add data/roadmap docs/roadmap.json
git commit -m "Update from {source} digest"
git push origin main
```

---

## This Week

You've already done Step 1 (read Claude chunks).

**Next:**
- Step 2: Save the digest file you created ✅ (done)
- Step 3: Feed to watcher (next)
- Step 4: Review proposals (then)
- Step 5: Update roadmap + publish (finally)

Ready to see the watcher extract from your digest?

