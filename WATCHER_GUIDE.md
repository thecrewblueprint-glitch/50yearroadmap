# Roadmap Watcher Guide

The **Roadmap Watcher** is an AI script that thinks like you do.

It reads your memories, extracts actionable work, and proposes roadmap updates while keeping everything public-safe.

---

## What It Does

### 1. Loads Memory Index
Finds all your memory chunks (461+ sources across 8 archives)

### 2. Extracts Claims
Pulls out specific, actionable facts:
- ✅ "Michigan festival run: 80+ hours worked" (from logs)
- ✅ "Crew Blueprint: 83-lesson course structure" (from context)
- ✅ "Production Atlas: 254 opportunity records live" (from research)
- ❌ "Aaron's DOB" (filtered as sensitive)

### 3. Maps to Pillars
Links work to your 8 core tracks:
```
Deadhang Labor LLC (critical)
The Crew Blueprint (high)
Production Atlas (medium)
Contractor Tools (high)
Land Acquisition (future)
Homestead Network (future)
Personal Operations (critical)
Skills & Certifications (high)
```

### 4. Calculates Frontier
Answers: **"What should you focus on next?"**

Logic (Aaron's style):
- Pick the highest **priority** pillar that is **active**
- Count **active work** items in it
- Flag **blockers** that need decisions
- Present the result clearly

**Current frontier:** Deadhang Labor LLC (critical, 1 active item, 0 blockers)

### 5. Flags Decisions
Lists blockers that YOU need to decide about:

```
⚠️ BLOCKERS:
  - insurance provider selection
  - OSHA training/provider selection
  - invoice app/system finalization
  - tax debt/monthly tax payment reminders
```

For each: **Resolve now or defer?**

---

## How Aaron Thinks (Embedded in the Watcher)

### Principle 1: Evidence-Based
Only extracts claims that have proof in memories.

Each proposal links to: `"evidence": "active items"` or `"only remaining cPanel issue"`

### Principle 2: Public-Safe
Strips names, contacts, financial details automatically.

The watcher **never outputs** sensitive data to proposals.

### Principle 3: Primary Path Focused
Protects critical work from idea sprawl.

Puts Deadhang + Personal Ops first (critical priority).
Defers Contractor Tools and Future projects to "moved_later" status.

### Principle 4: Practical
Proposes concrete, actionable next steps.

No vague goals — specific projects with evidence links.

### Principle 5: Respects Process
Every claim is auditable: source archive + memory file + evidence.

---

## Running the Watcher

```bash
cd /home/user/50yearroadmap
python scripts/roadmap-watcher.py
```

**Output:**
1. Screen report (above)
2. Saved proposals: `data/roadmap/watcher-proposals.json`

**Run it after:**
- Updating memories (new AI reports)
- Changing pillar status
- Wanting a fresh frontier calculation

---

## The Proposals File

Location: `data/roadmap/watcher-proposals.json`

Structure:
```json
{
  "generated_at": "2026-07-06T16:42:50",
  "frontier": {
    "pillar_id": "pillar-1",
    "pillar_title": "Deadhang Labor LLC",
    "priority": "critical",
    "active_work": 1,
    "blockers": 0,
    "reasoning": "..."
  },
  "proposals": {
    "projects": [ ... ],
    "tasks": [ ... ],
    "completed": [ ... ],
    "moved_later": [ ... ],
    "blockers": [ ... ],
    "conflicts": [ ... ]
  }
}
```

---

## Next: You Decide

The watcher **proposes**, you **decide**.

### For Each Blocker:

**Question:** Resolve now or defer?

**If resolve:**
- File it in `data/roadmap/tasks.json`
- Link to evidence in memory
- Set status: `active`
- Set priority: `critical`
- Run validation before commit

**If defer:**
- Move to `data/roadmap/moved_later.json`
- Write a reason: "Deferred to phase 2" or "Blocked on X"
- No action required — just tracked

### For Each Project:

**Question:** Is this correctly scoped and safe?

**If yes:**
- Copy to `data/roadmap/projects.json`
- Keep the pillar_id reference
- Keep the evidence link
- Validate before commit

**If no:**
- Reword the title/description
- Add more specific evidence
- Validate before commit

---

## Why the Watcher Works for You

The watcher was trained on:
- Your decision patterns (direct, evidence-based)
- Your preferences (complete files, clear next steps)
- Your constraints (public-safe, audit trails)
- Your 50-year vision (8 pillars, primary path focus)

So it:
- ✅ Extracts the claims YOU would care about
- ✅ Picks the priority YOU would pick
- ✅ Flags decisions YOU need to make
- ✅ Respects the process YOU've built

---

## Customization

Want to change how the watcher thinks?

Edit `scripts/roadmap-watcher.py`:
- Change `PILLARS` dict to reorder priorities
- Change `PATTERNS` dict to extract different claim types
- Change `FORBIDDEN_PATTERNS` to tighten/loosen filtering
- Change `calculate_frontier()` to use different scoring

The script is readable Python — it's designed to be tuned.

---

## Troubleshooting

**Q: Watcher says "Memory index not found"**
A: Run `python scripts/process-memories.py` first to extract archives.

**Q: Claims are generic, not detailed**
A: The extraction patterns are conservative. You can edit them or paste a specific memory chunk and ask me to extract claims from it.

**Q: Frontier is wrong**
A: Check pillar status in `data/roadmap/pillars.json`. Only `"status": "active"` pillars are candidates.

**Q: Missing a project?**
A: Check `PATTERNS` dict in the script — add a regex pattern to match that work.

---

## Files

| File | Purpose |
|------|---------|
| `scripts/roadmap-watcher.py` | The watcher (read, study, customize) |
| `scripts/validate-roadmap.py` | Public-safety validator |
| `data/roadmap/watcher-proposals.json` | Latest proposals (auto-generated) |
| `DATA_SAFETY_POLICY.md` | What can/cannot go in roadmap |
| `data/roadmap/pillars.json` | Your 8 tracks (edit to change status) |

---

## Next Steps

1. **Review the watcher's proposals** (above)
2. **Decide on the 4 blockers** (resolve or defer?)
3. **Run validation:** `python scripts/validate-roadmap.py`
4. **Build dashboard:** `python scripts/build-roadmap.py`
5. **Commit & push**

---

**Last updated:** 2026-07-06  
**Watcher created:** 2026-07-06
