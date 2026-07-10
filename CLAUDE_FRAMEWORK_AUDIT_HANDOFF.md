# Claude Handoff — Framework Audit and Recommended Next Steps

Claude, this file captures the latest framework audit and the recommended cleanup path.

We need to review this before making larger updates. The framework is mostly sound, but the audit identifies a likely next sequence of changes that should be followed carefully:

1. Promote the 30 / 60 / 90 layer into `roadmap.json` so the roadmap returns to one source of truth.
2. Update the validator so 30 / 60 / 90 `focus_step_ids` resolve to real work-item IDs.
3. Remove or reduce the temporary `ninety.js` sidecar once the data is formalized.
4. Add a formal `moved_later` / deferred-work model so skipped work stays visible without cluttering the active path.
5. Triage watcher proposals against the current milestone and 30 / 60 / 90 windows before promoting anything.

Do **not** treat this as automatic permission to rewrite the roadmap direction. Review the recommendations against `AGENTS.md`, `CHANGELOG.md`, and the current `roadmap.json`. If a change affects direction, sequencing, the Homestead, Crew Blueprint scope, or what "you are here" points to, confirm with the owner first.

---

## Framework audit — concept upward

I audited this as a **system**, not just as a website.

The framework is mostly sound. The main issue is that it is starting to split into **two sources of truth**: the official `roadmap.json` model and the temporary `ninety.js` 30/60/90 sidecar. That is acceptable for a prototype, but it should be corrected before the system grows.

---

# 1. Core concept

## Current concept

The strongest version of the framework is:

> **Build the Homestead by first building a self-sustaining Labor → Training → Jobs engine.**

That is coherent.

The repo already expresses this clearly:

- `north_star` points to the Homestead and the movement around it.
- Phase 1 builds the engine.
- Phase 2 acquires land and builds the Homestead.

## Audit judgment

**Strong. Keep it.**

The concept has a clean dependency chain:

```text
Deadhang Labor earns and proves the labor model
        ↓
Contractor Tools stabilize payments, scheduling, coordination
        ↓
Production Atlas finds and verifies work
        ↓
The Crew Blueprint trains and prepares people
        ↓
The loop becomes self-sustaining
        ↓
Land acquisition becomes responsible
        ↓
The Homestead becomes buildable
```

That flow matches the current ecosystem flow in `roadmap.json`: Deadhang secures contracts, Production Atlas surfaces work, Crew Blueprint trains workers, Contractor Tools manage coordination, and the system repeats/improves.

## Core risk

The concept is broad enough that it can sprawl unless every feature answers:

> “Does this help the Labor → Training → Jobs engine become real?”

If not, it should be moved later, archived, or kept out of the active dashboard.

---

# 2. Data model

## Current model

The official model is the **branch / journey model**:

- `branches` hold the work.
- `journey` sequences the work.
- `this_week_focus` tells you what to work on now.
- `phases` separate Phase 1 foundation from Phase 2 destination.
- `roadmap.json` is supposed to be the single source of truth.

## Audit judgment

**Structurally good. Needs one controlled extension.**

The existing model handles:

| Need | Current support |
|---|---|
| Long-term vision | `north_star`, `end_goal` |
| Major work areas | `branches` |
| Linear progression | `journey.milestones` |
| Immediate focus | `this_week_focus` |
| Dependency structure | `phases` |
| Public dashboard safety | validator + safety policy |

The missing layer is:

```text
Near-term execution horizon:
30 days → 60 days → 90 days
```

You now have that visually, but the data does not live in `roadmap.json` yet. The changelog explicitly says the 30/60/90 dashboard is currently supplied by `ninety.js` and should later be promoted into `roadmap.json`.

## Primary data-model issue

The official rule says `roadmap.json` is the single source of truth.

But the 30/60/90 layer currently lives in `ninety.js`.

That creates a temporary split:

```text
roadmap.json = official roadmap truth
ninety.js    = active 30/60/90 operating truth
```

That should be fixed soon.

## Correct fix

Add this to `roadmap.json` later:

```json
"thirty_sixty_ninety": {
  "title": "30 / 60 / 90 Day Operating Dashboard",
  "summary": "...",
  "windows": [
    {
      "id": "day-30",
      "label": "Next 30 days",
      "status": "current",
      "theme": "...",
      "goal": "...",
      "focus_step_ids": ["dh-1", "dh-2", "po-1"],
      "outcomes": [],
      "guardrail": "..."
    }
  ]
}
```

Then update the validator so every `focus_step_ids[]` entry must resolve to a real work item, the same way `journey.milestones[].step_ids` are validated now. The validator currently checks milestone step IDs and `this_week_focus` IDs, but not 30/60/90 IDs because that field is not formal yet.

---

# 3. Branch architecture

## Current branches

The seven-branch structure works:

### Phase 1 — Engine

- Deadhang Labor
- The Crew Blueprint
- Production Atlas
- Contractor Tools
- Personal Operations / Roadmap System

### Phase 2 — Destination

- Land Acquisition
- Homestead / Homes for Hands

The phase split is clean and correctly keeps the Homestead from becoming an immediate distraction.

## Audit judgment

**Good architecture. Do not add more top-level branches right now.**

The existing branches already cover the system.

If new ideas appear, they should usually become:

- work items inside a branch
- blockers inside a branch
- 30/60/90 items
- later/deferred items

They should **not** become new branches unless they represent a permanent operating pillar of the whole system.

## Potential weak spot

**Personal Operations / Roadmap System** is doing a lot:

- anti-sprawl controls
- dashboard execution
- near-term milestones
- documentation templates
- decision framework

That branch is necessary, but it can become a junk drawer. It needs stricter separation:

```text
Personal Operations = command center mechanics
Not = every random idea that does not fit elsewhere
```

---

# 4. Journey model

## Current journey

The journey is currently linear:

1. Solidify Deadhang’s foundation
2. Get paid reliably
3. Find the work
4. Teach the skills
5. Build teams and win bigger contracts
6. Close the loop
7. Acquire land
8. Build the Homestead

## Audit judgment

**This is the strongest part of the framework.**

It prevents the exact problem you described earlier: bouncing into a million projects while half-finished systems pile up.

## Improvement needed

The journey answers:

> “What order should I move in?”

The 30/60/90 dashboard answers:

> “What should I do in the next practical operating window?”

Those two should connect like this:

```text
Journey milestone = strategic sequence
30/60/90 window = near-term execution layer
This week focus = tactical work queue
Work item = actual unit of work
```

That is the core hierarchy the whole framework should enforce.

---

# 5. Dashboard flow

## Current flow

The live dashboard now has:

- Timeline view
- Dashboard view
- 30/60/90 dashboard section
- End Goal
- This Week Focus
- Branches
- Branch detail panel
- Ecosystem flow

The new 30/60/90 section is placed above the End Goal, which makes sense because it gives the user an operating layer before reviewing the broader destination.

## Audit judgment

**Good direction, but order should be reconsidered.**

For actual daily use, the best dashboard order is probably:

```text
1. You Are Here
2. 30 / 60 / 90
3. This Week Focus
4. Branches
5. End Goal
6. Ecosystem Flow
```

Right now, the End Goal still sits above This Week Focus. That is fine for vision, but not ideal for execution.

## Recommended dashboard hierarchy

### Timeline view

Purpose: orientation.

```text
Where am I in the long path?
What milestone am I on?
What comes next?
```

### Dashboard view

Purpose: work.

```text
What window am I in?
What do I do now?
What branch does this belong to?
What is blocked?
```

So the dashboard should become more operational and less presentation-oriented.

---

# 6. The 30/60/90 layer

## Current implementation

The 30/60/90 dashboard currently uses:

- `ninety.css` for styling
- `ninety.js` for data and rendering
- existing `roadmap.json` work-item IDs for focus items
- fallback behavior so it can later read `roadmap.json.thirty_sixty_ninety` if promoted.

## Audit judgment

**Good prototype. Not good as a permanent architecture.**

The content itself flows correctly:

### 30 days

Stabilize Deadhang foundation:

- business audit
- gig tracking
- dashboard execution surface

### 60 days

Lock money/workflow tools:

- contractor tools requirements
- invoice MVP
- payment tracking
- calendar reliability

### 90 days

Connect the loop:

- Production Atlas verification
- Crew Blueprint authority/safety boundary
- anti-sprawl controls

That logic is right.

## Main flaw

`ninety.js` uses timed re-renders to keep the section visible because `app.js` hides it when `roadmap.json.thirty_sixty_ninety` is absent. That is a patch, not a clean framework pattern.

The changelog already labels this as a follow-up.

## Correct next technical move

Promote the 30/60/90 data into `roadmap.json`, then remove the standalone data from `ninety.js`.

Target architecture:

```text
roadmap.json
  └── thirty_sixty_ninety
        └── windows[]
              └── focus_step_ids[]

app.js
  └── renderNinetyDayDashboard()

ninety.css
  └── styling only
```

Then `ninety.js` can be deleted or reduced to nothing.

---

# 7. Safety and evidence model

## Current safety model

The repo has a strong public-data policy:

- no contact info
- no financial details
- no credentials
- no owner personal identity
- no travel/hotel details
- no raw memory content
- no private client/jobsite specifics

The watcher is proposal-only and does not edit `roadmap.json`.

## Audit judgment

**Strong. Keep strict.**

This matters because the dashboard is public. The safety model is doing its job.

## Improvement needed

The safety policy is strong, but the framework also needs a **decision-safety rule**:

> Do not promote a proposal into the active roadmap unless it supports the current journey milestone, the current 30/60/90 window, or a confirmed owner direction.

That prevents the watcher backlog from turning into dashboard clutter.

---

# 8. Agent workflow

## Current workflow

AGENTS.md is clear:

- commit to `main`
- no branches
- changelog every change
- validate if `roadmap.json` changes
- raw memory is immutable
- owner decides direction

## Audit judgment

**Strong for multi-agent work.**

This is exactly what prevents Claude/GPT/Gemini from trampling each other.

## Issue

The rules say to verify live pages render, but via connector-only work we cannot reliably run the site or local validator. AGENTS.md says agents should verify live pages or do a headless check.

That means the framework needs either:

1. a GitHub Action that runs validation and maybe a basic static smoke test, or
2. a documented “connector-only limitation” note for agents working without runtime access.

---

# 9. Current critical issues

## Critical issue 1 — Split source of truth

`roadmap.json` is official. `ninety.js` now contains live execution data.

**Risk:** future agents may update one and not the other.

**Fix:** promote 30/60/90 into `roadmap.json`, update validator, remove sidecar data.

---

## Critical issue 2 — No formal “move later” model yet

You asked for “move to later.” The 30/60/90 guardrail mentions skipped work, but the data model does not formally support deferred/moved-later work yet.

**Risk:** skipped tasks either disappear or stay in the active flow and create noise.

**Fix:** add either:

```json
"status": "moved_later"
```

or:

```json
"deferred": true,
"deferred_reason": "...",
"revisit_after": "..."
```

Best option: add `status: "moved_later"` first because it is simple and visible.

---

## Critical issue 3 — Proposal backlog is not yet governed

The watcher output has a proposal backlog. The changelog says approved items still need manual promotion.

**Risk:** dumping too many proposals into `roadmap.json` will break the clarity of the framework.

**Fix:** create a promotion rule:

```text
Only promote proposals that fit:
1. current milestone,
2. current 30/60/90 window,
3. active blocker,
4. owner-confirmed direction.
```

Everything else goes later.

---

# 10. Recommended framework architecture

This is the clean version I would build toward:

```text
NORTH STAR
The Homestead + movement

PHASES
Phase 1: Labor → Training → Jobs engine
Phase 2: Land → Homestead

BRANCHES
Permanent work domains

JOURNEY
Linear strategic sequence

30 / 60 / 90
Near-term operating windows

THIS WEEK
Tactical focus

WORK ITEMS
Actual tasks

WATCHER PROPOSALS
Inbound suggestions only

MOVED LATER
Deferred work that stays visible but out of the active path
```

The rule should be:

> Every active task must belong to a branch, appear in either the journey, the 30/60/90 plan, or this-week focus, and support the current milestone.

---

# 11. Recommended next implementation steps

## Step 1 — Promote 30/60/90 into `roadmap.json`

Move the current plan from `ninety.js` into `roadmap.json`.

Then update:

- `scripts/validate-roadmap.py`
- `AGENTS.md`
- `DATA_SAFETY_POLICY.md`
- `CHANGELOG.md`

This restores single-source-of-truth discipline.

## Step 2 — Remove `ninety.js` sidecar logic

After promotion:

- keep `ninety.css`
- keep `renderNinetyDayDashboard()` in `app.js`
- remove `ninety.js`
- remove the extra script tag from `index.html`

## Step 3 — Add `moved_later`

Update validator enum:

```python
WORK_STATUS = {"not_started", "in_progress", "blocked", "completed", "moved_later"}
```

Then update CSS display:

```text
moved_later = muted / parked / not active
```

## Step 4 — Add a “Now / Later” control layer

Not necessarily interactive yet. Just visual grouping:

```text
Current
Next
Later
Blocked
Moved Later
```

## Step 5 — Triage watcher proposals using the framework

Do not promote broadly. Triage against the hierarchy:

```text
Does it support the 30-day window?
If no, does it support the 60-day window?
If no, does it support the 90-day window?
If no, move later.
```

---

# Bottom line

The framework is viable.

The best part is the **branch/journey model**. It gives the entire project a spine. The weakest part is that new layers are starting to appear outside `roadmap.json`.

The next high-value move is not adding more features. It is this:

> **Promote the 30/60/90 layer into `roadmap.json`, validate it, and make the dashboard read from one source of truth again.**
