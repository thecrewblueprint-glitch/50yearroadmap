# Interactive Dashboard Feature Specification

**Status:** Planned (Future Enhancement)  
**Priority:** Medium  
**Added:** 2026-07-07  
**Source:** User feedback after initial dashboard review

---

## Overview

Current system: Read-only dashboard displaying roadmap data from JSON files. Updates require manual JSON editing or AI-mediated conversations.

**Proposed system:** Fully interactive drag-and-drop interface where users can directly manipulate roadmap items without AI involvement. Changes persist to backend automatically.

---

## Vision

Transform the dashboard from **static reporting** to **active management interface**:

- Click items to edit details
- Drag-and-drop to change status/priority
- Reorder projects visually
- Create/delete items directly
- Real-time persistence (no manual file editing)
- No AI conversations needed for routine updates

---

## User Interactions (Desired)

### 1. Item Selection & Expansion
- Click project card → expand to show details
- Show: title, description, pillar, status, priority, dependencies
- Inline edit fields

### 2. Drag-and-Drop Status Changes
- Drag "Blocked" item → drop on "Active" column
- Backend updates: `status: "blocked"` → `status: "active"`
- Visual feedback during drag
- Auto-commit to git or persist to database

### 3. Priority Reordering
- Drag items within a column to reorder
- Updates sequence/priority in data
- Reflects in frontier calculation (if applicable)

### 4. Create New Items
- "+" button to add new project/task
- Modal or inline form
- Auto-saves to data files

### 5. Batch Operations
- Multi-select items
- Move multiple → one status
- Delete, archive, or move-later

---

## Architecture Requirements

### Frontend
- Interactive component library (React, Vue, or vanilla + drag-drop lib)
- Drag-and-drop library: Dnd-kit, React Beautiful DnD, or Sortable.js
- Real-time UI feedback
- Responsive design

### Backend API
- `GET /api/roadmap` — Fetch current state
- `POST /api/roadmap/projects` — Create project
- `PATCH /api/roadmap/projects/:id` — Update status/priority
- `DELETE /api/roadmap/projects/:id` — Remove item
- `POST /api/roadmap/reorder` — Batch reorder
- `GET /api/roadmap/history` — (Optional) Change history

### Data Persistence
**Option A: Git-based (current)**
- API writes to JSON files
- Auto-commits changes to git
- Maintains audit trail via git history

**Option B: Database (future)**
- SQLite or lightweight DB
- Faster updates
- Better for concurrent access
- Export to JSON for GitHub Pages

### Real-time Sync
- WebSocket updates (if multi-user)
- Or polling + change detection

---

## Phases

### Phase 1: Basic Interactivity (Foundation)
- Drag-and-drop status changes
- Click to expand items
- Inline editing (title, description)
- Auto-save to JSON + git commit

### Phase 2: Advanced Interactions
- Create/delete items from UI
- Reorder by drag
- Batch operations
- Undo/redo

### Phase 3: Collaboration & History
- Change history view
- Collaborative editing (multi-user support)
- Comments/notes on items
- Audit trail

---

## Success Criteria

✅ User can move item from "Blocked" to "Active" via drag-drop  
✅ Change persists to roadmap.json automatically  
✅ Git commit is created with change record  
✅ No manual JSON editing required  
✅ No AI conversation needed for routine updates  
✅ Frontier recalculates if status changes priority logic  

---

## Current State (Baseline)

**What exists:**
- Read-only dashboard serving `docs/roadmap.json`
- 40 projects, 41 tasks across 8 pillars
- Frontier calculation (Production Atlas)
- GitHub Pages deployment
- Watcher-based extraction from memory chunks

**What's missing:**
- Interactive elements
- Direct data mutation
- UI-based create/edit/delete
- API endpoints
- Real-time persistence

---

## Next Steps

1. **Review & Refine** — User inspection of current system
2. **Architecture Decision** — Git-based vs. Database backend
3. **Tech Stack Selection** — Framework/library choices
4. **Prototype Phase 1** — Drag-drop for status changes
5. **Testing & Iteration** — User feedback loops

---

## Notes for Continuation

- Keep current read-only dashboard as fallback
- Ensure public-safety validation still applies (no PII in UI)
- GitHub Pages deployment should remain static (API could run elsewhere)
- Consider offline support if using client-side persistence
