# Dashboard UI/UX Analysis & Improvement Recommendations

**Date:** 2026-07-07  
**Current State:** Read-only dashboard (Production Atlas frontier, 40 projects, 8 pillars)  
**User Context:** Operational roadmap management (no AI conversations for updates)

---

## Current Strengths ✅

1. **Clean, dark theme** — Minimal distraction, professional appearance
2. **Clear hierarchy** — Frontier → pillars → blockers → completed → deferred
3. **At-a-glance metrics** — Summary counts visible in header
4. **Color coding** — Yellow frontier badge, red blockers, muted completed items
5. **Responsive grid layout** — Adapts to screen size
6. **Escape HTML** — Safe from XSS attacks
7. **Smooth scroll to frontier** — Quick navigation via "You Are Now Here" button

---

## Critical Issues for Operational Use ⚠️

### 1. **No Search/Filter Capability**
**Problem:** With 40 projects and 32 blockers, finding a specific item requires scrolling.

**Impact:** Time-consuming to locate item by name, status, or pillar.

**Solution:**
- Add search bar (top of page)
- Filter by: Pillar, Status, Priority
- Real-time filtering as user types
- Show "X results found" counter

---

### 2. **Blocked Items Listed as Plain Text**
**Problem:** Blockers are shown as simple list items with no context.

**Current:**
```
- Crew Blueprint LMS remains paused
- Production Atlas needs human-verification
```

**Missing:**
- Which pillar does this blocker belong to?
- What is blocking it? (dependency info)
- Owner/responsible person?
- Severity/impact level?
- Resolution path?

**Solution:**
- Convert blockers to cards with metadata
- Show pillar relationship
- Add priority/severity indicator
- Include "action needed" vs "waiting on external"

---

### 3. **No Actionable Status Indicators**
**Problem:** Dashboard shows **what** is blocked, not **why** or **what to do**.

**Example:** "Crew Blueprint LMS remains paused"
- Why is it paused?
- Who can unstick it?
- What's the blocker type? (decision, resource, external, code)
- What's next step?

**Solution:**
- Categorize blockers: `NEEDS_DECISION`, `BLOCKED_ON`, `WAITING_EXTERNAL`, `RESOURCE_CONSTRAINT`
- Show assigned owner
- Display "next action" suggestion
- Add severity/priority indicator

---

### 4. **Pillars Show Only First 8 Projects**
**Problem:** If a pillar has 10+ projects, you see "+ 3 more" but can't expand.

**Current:**
```
Production Atlas
15 active projects
- Project 1
- Project 2
...
- Project 8
+ 7 more (CLICKABLE?)
```

**Solution:**
- Make pillar cards clickable/expandable
- Show all projects in expanded view
- Option: collapse to save space
- Preserve scroll position when toggling

---

### 5. **No Timeline or Dependency View**
**Problem:** No visibility into:
- Which projects are prerequisites for others
- Sequence dependencies (X must finish before Y)
- Critical path items
- Parallel vs. sequential work

**Solution:** (Future feature)
- Add dependency graph visualization
- Show blockers that gate multiple projects
- Timeline view (if you add dates)
- Critical path highlighting

---

### 6. **Metrics Are Summary Only**
**Problem:** Metric counts (40 projects, 32 blockers) don't show breakdown.

**Current:**
```
Projects: 40 | Tasks: 41 | Blockers: 32 | Completed: 6 | Moved Later: 3
```

**Missing:**
- How many blockers per pillar?
- How many projects are "critical" vs "medium" priority?
- Completion rate: 6 done / 46 total = 13%
- Blocker aging: how old are these blockers?

**Solution:**
- Make metric cards clickable → drill down to detail
- Add mini pie chart or progress bar
- Show top 3 blockers by age/severity
- Display blocker accumulation rate

---

### 7. **No Sort or Prioritization Within Sections**
**Problem:** Blockers/items appear in arbitrary order (JSON order).

**Current:** Not clear which blocker is most urgent

**Solution:**
- Sort blockers by: severity, age, impact (# of projects blocked)
- Sort projects within pillars by: priority, blocker count, estimated effort
- Allow user to customize sort order
- Remember sort preference (localStorage)

---

### 8. **Decision Context Section Unclear**
**Problem:** "Deep-Context Decision Policy" section is abstract.

**Current:**
```
Deep-Context Decision Policy
Roadmap deep-context files are decision context for the watcher. 
They must be consulted before changing frontier, sequencing, 
pillar priority, project boundaries, or public-safe summaries.
```

**Problem:** User seeing this doesn't know what action to take.

**Solution:**
- Rename to "How Decisions Affect Roadmap"
- Make it collapsible
- Show concrete examples: "e.g., changing Production Atlas priority requires review of decision-sources.json"
- Add link to decision context file

---

### 9. **No Quick Actions**
**Problem:** Dashboard is read-only; no way to mark blocker as "resolved" or move item.

**Current:** Requires manual JSON editing or AI conversation

**Solution:** (For interactive version Phase 1)
- "Mark as Resolved" button on blockers
- Quick-move to status dropdown
- "Assign to me" button
- "Snooze for 1 week" option

---

### 10. **No Historical Comparison**
**Problem:** No way to see if you're making progress over time.

**Missing:**
- Blocker count trend (was 28 last week, now 32 — getting worse?)
- Project velocity (completing X per week)
- Frontier stability (changed 3 times this month)

**Solution:** (Future analytics feature)
- Add timeline/history view
- Show metrics from previous snapshots
- Display trend arrows (↑ blockers, ↓ progress)
- Last updated timestamp

---

## Low-Priority UI Issues 🔹

1. **No loading indicator** — Page just appears (not a real problem with static JSON)
2. **No empty states** — What if a section has 0 items? (currently shows nothing)
3. **Keyboard navigation limited** — Tab through sections, but no hotkeys
4. **Mobile view untested** — Likely works, but may need adjustment

---

## Recommendations by Priority

### IMMEDIATE (High Impact)
1. **Add search/filter bar** — Enables finding items in large list
2. **Expand blocked items to cards** — Show pillar, owner, action needed
3. **Make pillar cards expandable** — See all projects without "X more"
4. **Sort items by severity/priority** — Most urgent items appear first

### SHORT-TERM (Medium Impact)
1. **Add drill-down to metrics** — Click "Blockers: 32" → see all with filters
2. **Categorize blocker types** — `NEEDS_DECISION` vs `BLOCKED_ON` vs `RESOURCE`
3. **Add owner/assignee field** — Who can fix this blocker?
4. **Show blocker age** — Created date or "open for X days"

### FUTURE (Lower Impact, Requires Backend)
1. **Drag-drop status changes** — Interactive phase 1
2. **Dependency graph** — Visualize project relationships
3. **Timeline view** — If you add date estimates
4. **Collaboration/comments** — Discuss blockers in dashboard
5. **Activity history** — Track changes over time

---

## Specific UX Flows to Improve

### Use Case 1: "What's blocking me right now?"
**Current flow:**
1. Open dashboard
2. Scroll to "Blockers" section
3. Read 32 items (find one relevant to me)
4. No context on what to do
5. Check JSON manually for more info

**Improved flow:**
1. Open dashboard
2. Click "Blockers" in header → jump to section
3. Search "blueprint" → filter to 3 relevant blockers
4. Click blocker → expand card → see pillar, owner, reason, next steps
5. "Mark as resolved" or assign to self

---

### Use Case 2: "How's pillar X doing?"
**Current flow:**
1. Scroll to Pillars section
2. Find card for pillar X
3. See first 8 projects + "X more" badge
4. Can't see the rest without manually checking JSON

**Improved flow:**
1. Search pillar name
2. Click pillar card → expand → see all projects
3. Filter by status (active, blocked, completed)
4. Sort by priority or blocker count
5. Quick actions: create new project, mark project complete

---

### Use Case 3: "What's our progress?"
**Current flow:**
1. Look at header metrics (40 projects, 6 completed = 15%)
2. No way to drill down by pillar or time period
3. No trend data (better or worse than last week?)

**Improved flow:**
1. Click metrics → dashboard analytics view
2. See breakdown: 40 projects → 15 active, 9 blocked, 12 future, 4 other
3. See trend: blocker count +4 this week (yellow warning)
4. See completion rate: 6/46 done (13%, on track?)
5. See velocity: 1.5 projects/week average

---

## Data Model Gaps

Current roadmap.json is missing:
- `project.owner` — Who's responsible?
- `project.blockedBy` — Which items gate this?
- `project.effort` — T-shirt size (S/M/L/XL) or days?
- `project.createdDate` / `completedDate` — Timeline data
- `blocker.severity` — CRITICAL, HIGH, MEDIUM, LOW
- `blocker.type` — NEEDS_DECISION, BLOCKED_ON, EXTERNAL, RESOURCE
- `blocker.owner` — Who can fix it?
- `blocker.resolution` — What needs to happen to clear it?

These should be added to support operational queries and interactive features.

---

## Summary

**Current dashboard:** Beautiful, clear frontier visualization, good pillar overview.

**For operational use:** Needs better filtering, more actionable blocker info, expandable sections, drill-down capabilities, and sorting.

**Recommendation:** Before building interactive version, implement these read-only improvements. They'll make the current system useful for daily management and will inform the database schema design for the interactive version.
