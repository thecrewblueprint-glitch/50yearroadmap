# Operations Command Center: Setup Checklist

**Goal:** Get real roadmap data live on the dashboard  
**Estimated time:** 1-2 hours  
**Prerequisites:** Complete `IMPLEMENTATION_SUMMARY.md` reading

---

## Phase 1: Make Blocker Decisions (15 min)

These 4 decisions gate everything else:

- [ ] **Insurance provider selection**
  - [ ] Resolve now (investigate + choose provider this week)
  - [ ] Defer to phase 2 (move to moved_later.json)

- [ ] **OSHA training/provider selection**
  - [ ] Resolve now (research + enroll this month)
  - [ ] Defer to phase 2

- [ ] **Invoice app/system finalization**
  - [ ] Resolve now (build Android app framework)
  - [ ] Defer to phase 2

- [ ] **Tax debt/monthly tax payment reminders**
  - [ ] Resolve now (reconcile taxes, set up payments)
  - [ ] Defer to phase 2

**After deciding:** Note decisions somewhere you'll reference them for roadmap.

---

## Phase 2: Create projects.json (20 min)

**Location:** `data/roadmap/projects.json`

Use this template and fill in from the watcher proposals:

```json
[
  {
    "id": "project-deadhang-ssl",
    "title": "Deadhang website SSL/security implementation",
    "purpose": "Secure cPanel-hosted portfolio website",
    "summary": "Only remaining Deadhang Labor LLC website infrastructure task",
    "status": "active",
    "priority": "high",
    "progression_track": "business_operations",
    "pillar_id": "pillar-1",
    "evidence": "Remaining cPanel issue documented in context"
  },
  {
    "id": "project-crew-content",
    "title": "Crew Blueprint course content creation",
    "purpose": "Build 83-lesson stagehand training course",
    "summary": "Content structure defined; lesson writing in progress",
    "status": "active",
    "priority": "high",
    "progression_track": "content_platform",
    "pillar_id": "pillar-2",
    "evidence": "Lesson structure, module manifest, and JSON workflow documented"
  },
  {
    "id": "project-atlas-research",
    "title": "Production Atlas vendor & logistics research",
    "purpose": "Expand festival opportunity data (vendors, crew routing, travel)",
    "summary": "6 research batches underway; deepen vendor stack and lodging data",
    "status": "active",
    "priority": "medium",
    "progression_track": "software_projects",
    "pillar_id": "pillar-3",
    "evidence": "254 opportunity records live; 6 research batches in progress"
  }
]
```

**What to include:**
- From watcher proposals, all items with `"status": "active"`
- Keep pillar_id, evidence, priority
- Write 1-2 sentence descriptions that are generic (no specific names)

**Save as:** `data/roadmap/projects.json`

---

## Phase 3: Create tasks.json (30 min)

**Location:** `data/roadmap/tasks.json`

Break each project into 2-4 concrete next actions:

```json
[
  {
    "id": "task-deadhang-ssl-1",
    "title": "Audit cPanel SSL certificate requirements",
    "summary": "Determine if certificate is installed, expired, or missing",
    "status": "active",
    "priority": "critical",
    "progression_track": "business_operations",
    "project_id": "project-deadhang-ssl"
  },
  {
    "id": "task-deadhang-ssl-2",
    "title": "Purchase or renew SSL certificate if needed",
    "summary": "Source cert through cPanel or Let's Encrypt",
    "status": "active",
    "priority": "high",
    "progression_track": "business_operations",
    "project_id": "project-deadhang-ssl"
  },
  {
    "id": "task-crew-content-1",
    "title": "Finalize module 1 lesson content",
    "summary": "Complete all 10 lessons in stagehand fundamentals module",
    "status": "active",
    "priority": "high",
    "progression_track": "content_platform",
    "project_id": "project-crew-content"
  }
]
```

**Format:**
- 1 task = 1-3 days of work
- `status` = "active", "completed", "blocked"
- `priority` = "critical", "high", "medium"
- link to `project_id`

**Save as:** `data/roadmap/tasks.json`

---

## Phase 4: Create moved_later.json (10 min)

**Location:** `data/roadmap/moved_later.json`

For any blockers you decided to **defer**, list them here:

```json
[
  {
    "id": "blocker-insurance",
    "title": "insurance provider selection",
    "reason": "Deferred to Q4; focus on revenue generation first",
    "moved_later_date": "2026-07-06"
  },
  {
    "id": "contractor-tools-1",
    "title": "Android invoice app development",
    "reason": "Framework ready; build deferred to phase 2",
    "moved_later_date": "2026-07-06"
  }
]
```

**Format:**
- `reason` = why you deferred (not deleted)
- `moved_later_date` = when you moved it

**Save as:** `data/roadmap/moved_later.json`

---

## Phase 5: Update pillars.json (5 min)

**Location:** `data/roadmap/pillars.json`

If any blockers changed a pillar's status, update it:

```json
[
  {
    "id": "pillar-7",
    "title": "Personal Operations",
    "purpose": "Taxes, insurance, legal, and financial stability.",
    "status": "active",  // ← change if blockers moved it
    "priority": "critical",
    "sequence_order": 7,
    "progression_track": "personal_admin"
  }
]
```

- `status`: "active" / "future" / "completed" / "blocked"
- Only change if decisions affected it

**Save as:** (already exists; edit in place)

---

## Phase 6: Run Validation (5 min)

```bash
cd /home/user/50yearroadmap
python scripts/validate-roadmap.py
```

**Expected output:**
```
✓ Checking for sensitive data... ✓
✓ Validating status values... ✓
✓ Validating progression tracks... ✓
✓ Validating pillar references... ✓

✅ Roadmap data is valid and safe for public commit.
```

**If it fails:**
```
ERROR: SENSITIVE DATA DETECTED in projects[0].title: person
  Value: "Aaron's invoice app"
```

**Fix:** Remove names, specific contacts, financial data. Re-run validation.

**Do NOT commit if validation fails.**

---

## Phase 7: Build Dashboard (5 min)

```bash
cd /home/user/50yearroadmap
python scripts/build-roadmap.py
```

**Expected output:**
```
✅ Roadmap compiled to docs/roadmap.json
```

This creates the file that powers the GitHub Pages dashboard.

---

## Phase 8: Commit & Push (5 min)

```bash
cd /home/user/50yearroadmap
git add data/roadmap/ docs/roadmap.json
git commit -m "Populate roadmap from watcher proposals and blocker decisions"
git push origin main
```

**Important:** Push to `main` branch (not a feature branch).

**What happens:**
1. GitHub Actions runs on push
2. Process-memories workflow triggers (if memory files changed)
3. Dashboard updates at: https://thecrewblueprint-glitch.github.io/50yearroadmap/
4. Your roadmap goes live

---

## Phase 9: Verify Dashboard (5 min)

Go to: https://thecrewblueprint-glitch.github.io/50yearroadmap/

**Look for:**
- [ ] "You Are Now Here" section populated
- [ ] Your 8 pillars listed
- [ ] Active projects showing
- [ ] Correct frontier pillar selected
- [ ] No personal/sensitive data visible

**If dashboard is blank:**
- GitHub Pages rebuild can take 30-60 seconds
- Check GitHub Actions: repo → Actions → see "Deploy" workflow

---

## Phase 10: (Optional) Update Raw Reports

If you add new daily reports:

```bash
# Put your AI reports here
echo "2026-07-06 daily report" > data/raw-reports/2026-07-06.txt

# Run watcher to extract new claims
python scripts/roadmap-watcher.py

# Review proposals in watcher-proposals.json
# Update roadmap files as needed
# Validate, build, commit
```

---

## Checklist Summary

- [ ] Phase 1: Made blocker decisions (4 items)
- [ ] Phase 2: Created projects.json
- [ ] Phase 3: Created tasks.json
- [ ] Phase 4: Created moved_later.json
- [ ] Phase 5: Updated pillars.json (if needed)
- [ ] Phase 6: Ran validation (passed ✅)
- [ ] Phase 7: Built dashboard
- [ ] Phase 8: Committed & pushed to main
- [ ] Phase 9: Verified dashboard is live
- [ ] Phase 10: (Optional) Tested raw report workflow

---

## Troubleshooting

**Q: Validation fails with "SENSITIVE DATA"**
A: Edit projects.json/tasks.json to remove the flagged text. Re-validate.

**Q: Dashboard still showing test data after 1 minute**
A: GitHub Pages takes 30-60 seconds. Check GitHub Actions for deployment status.

**Q: Watcher proposals look wrong**
A: Edit `scripts/roadmap-watcher.py` PATTERNS dict to add/fix extraction rules.

**Q: Dashboard URL 404s**
A: Repo is `thecrewblueprint-glitch/50yearroadmap`; URL should be:
https://thecrewblueprint-glitch.github.io/50yearroadmap/

---

## After Setup: Monthly Workflow

Once live, repeat monthly:

```bash
# 1. Add weekly/daily reports
echo "This week: worked 40 hours, completed X, blocked on Y" > data/raw-reports/weekly.txt

# 2. Run watcher
python scripts/roadmap-watcher.py

# 3. Review proposals
cat data/roadmap/watcher-proposals.json

# 4. Update roadmap
# - Move completed tasks to "completed" status
# - Add new active tasks
# - Update moved_later if resolving deferred items

# 5. Validate, build, commit
python scripts/validate-roadmap.py
python scripts/build-roadmap.py
git add data/roadmap docs/roadmap.json
git commit -m "Monthly roadmap update"
git push origin main
```

---

**You're ready. Start with Phase 1.**
