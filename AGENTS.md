# AGENTS.md — Operating Rules for AI Collaborators

This repository is a shared workspace. Multiple AI agents (and the owner)
work in it at different times. These rules keep that collaboration coherent
so work never gets stranded, duplicated, or silently overwritten again.

Read this file in full before making any change.

---

## 0. The Golden Rule: commit to `main`, never branch

**All work happens on `main`. Do not create branches. Do not open pull
requests. Commit and push directly to `main`.**

Why this rule exists: earlier a full watcher pipeline and a batch of digests
were built on a side branch (`claude/repository-review-yvxvn5`) and never
merged. Meanwhile the dashboard was rebuilt on `main`. The two diverged, the
data model changed underneath the stranded work, and it became unusable.
Single-trunk development prevents exactly that.

- If you find useful commits on another branch that are not in `main`, **do
  not merge them silently.** Summarize what they contain and raise it with
  the owner for a decision. (See `CHANGELOG.md` for the running record.)
- Pull/refresh `main` before you start so you build on the latest state.
- Keep commits small and frequent with clear messages.

---

## 1. Every change ends with two things

1. **Validate the data.** If you touched `roadmap.json`, confirm it still
   parses and that all cross-references resolve (see §4).
2. **Log the change.** Add a dated entry to `CHANGELOG.md` describing what
   changed and why. This is the shared memory between agents — an agent that
   picks up later reads the CHANGELOG to understand what happened.

A change is not "done" until both are true and the work is pushed to `main`.

---

## 2. The live product = the repo root

The dashboard is served by GitHub Pages **from the repository root** (not
`/docs`). These are the live files — treat them as production:

- `index.html` — Timeline view (default) + Dashboard view
- `branch.html` — per-branch hub (`?branch=<id>&view=overview|work|blockers|details`)
- `present.html` — "The Vision" (read-only page for outsiders)
- `app.js` — dashboard logic
- `styles.css` — shared theme
- `roadmap.json` — **the single source of truth for all views**

`roadmap.json` is currently hand-authored. There is no automated builder or
watcher feeding it (see §5). When you change the plan, you edit `roadmap.json`
directly and keep it valid.

---

## 3. The data model (current — the "branch / journey" model)

`roadmap.json` top-level keys:

- `north_star` — one-sentence destination statement.
- `end_goal` — `{ destination, what_it_is, how_to_reach_it[] }`.
- `phases` — `[{ number, name, status: active|future, goal, branch_ids[] }]`.
- `branches` — the areas of work. Each branch:
  `{ id, name, role, status_percentage, ultimate_goal, current_state,
     critical_blocker, timeline:{ phase_1_ready, description },
     blockers[], work_items[], phase, lifecycle: active|future }`.
  Each work item: `{ id, task, why, priority: CRITICAL|HIGH|MEDIUM|LOW,
     status: not_started|in_progress|blocked|completed|moved_later }`.
  `moved_later` = deferred work: it stays visible (rendered with a dashed,
  muted style) but is understood to be off the active path.
- `journey` — the linear path. `{ you_are_here, start_label,
     milestones[{ id, order, title, area_branch_id, state:current|upcoming|done,
     summary, outcome, step_ids[], leads_to }] }`.
  `step_ids` reference `work_items` by id — branches stay the single source
  of truth; milestones just sequence existing work.
- `this_week_focus` — `{ priority_1, priority_2, priority_3, note }` where each
  priority is a comma-separated list of work-item ids.
- `thirty_sixty_ninety` — the near-term operating layer.
  `{ title, summary, windows[{ id, label, status, theme, goal,
     focus_step_ids[], outcomes[], guardrail }] }`. `focus_step_ids` reference
  `work_items` by id (same single-source-of-truth rule as milestones). Rendered
  in the Dashboard view by `app.js`; there is no separate renderer.
- `ecosystem_flow` — `{ flow[] }`, ordered strings describing the loop.

> Note: an older **pillar model** (`vision.json`, `pillars.json`, `projects`,
> `tasks`, `frontier`) predates this. It is retired, and its files
> (`vision.json`, `pillars.json`, `scripts/build-roadmap.py`, the `compiled.json`
> artifact) were **removed 2026-07-18**. Do not reintroduce it into the live
> `roadmap.json`.

---

## 4. Integrity rules for `roadmap.json`

Before committing a `roadmap.json` change, confirm:

- It is valid JSON.
- Every `journey.milestones[].step_ids` entry matches a real `work_items[].id`.
- Every `journey.milestones[].area_branch_id` matches a real `branches[].id`.
- Every `phases[].branch_ids` entry matches a real branch, and every branch
  appears in exactly one phase.
- `journey.you_are_here` matches a real milestone id.
- Every id in `this_week_focus` matches a real work-item id.
- Every `thirty_sixty_ninety.windows[].focus_step_ids` entry matches a real
  work-item id.
- No duplicate work-item ids.

Run the validator instead of checking by hand:

```bash
python3 scripts/validate-roadmap.py
```

It enforces every rule above plus enum/range checks and a public-safety scan
(no email/phone/SSN/card/address/HTML). Exit code 0 = pass, 1 = errors. Run it
before committing any `roadmap.json` change; a failing validation must be fixed,
not committed.

---

## 5. What is automated vs. manual

- ✅ **Memory processing** — `scripts/process-memories.py` (also a GitHub
  Action) turns raw archives in `/memories` into chunks + indexes under
  `/memories/processed`. This is safe to re-run; it rebuilds its output.
- ⏳ **Curation → roadmap** — done by hand. Read chunks, distill into
  `/data/raw-reports`, then update `roadmap.json`.
- 🟡 **Watcher (proposals only)** — `scripts/roadmap-watcher.py` reads the
  curated digests, maps candidate work items / blockers to the current
  branches, filters for public-safety, de-dupes against the existing roadmap,
  and writes **proposals** to `data/roadmap/watcher-proposals.json`. It does
  **not** edit `roadmap.json` — a human promotes approved proposals by hand.
  See `WATCHER_GUIDE.md`. (Running it is manual, not wired into CI.)
- 🟡 **Prioritizer (read-only view)** — `scripts/prioritize-proposals.py` ranks
  the open watcher candidates into `data/roadmap/proposal-backlog.md` ("work on
  first" order) using the 30/60/90 windows, blockers-first, and confidence. It
  **deletes nothing** and never edits the proposals or `roadmap.json`; it only
  produces the ranked report for the owner to decide from.

---

## 6. Evidence & safety (do not violate)

1. **Raw memory is immutable evidence.** Never overwrite or silently delete
   archives in `/memories` or curated digests in `/data/raw-reports`.
2. **Do not publish raw memory or private data** into the live dashboard.
   Dashboard/`present.html` output must be public-safe: no contact,
   financial, travel, or private personal details.
3. **Do not mark inferred items as confirmed** without owner validation.
4. **Do not collapse conflicting information** — preserve both and flag it.
5. **Consult deep context before changing direction.**
   `data/roadmap/deep-context-decision-sources.json` indexes the
   `data/roadmap-deep-context/` files that inform frontier, sequencing,
   priority, and boundary decisions. (Note: the indexed files currently live
   only on the `claude/repository-review-yvxvn5` branch — flag this gap rather
   than acting as if they are present.)
6. **The owner is the executive.** Agents structure and maintain; the owner
   decides direction. When a change affects direction (the Homestead,
   Crew Blueprint scope, phase sequencing, what "you are here" points to),
   confirm with the owner rather than deciding unilaterally.

---

## 7. Multi-agent coordination checklist

When you start:
1. Refresh `main`. Read `CHANGELOG.md` (most recent entries first) to see what
   the last agent did.
2. Read this file and the relevant source files.

When you work:
3. Make focused changes on `main`. If you touched `roadmap.json`, run
   `python3 scripts/validate-roadmap.py` and fix any errors before committing.
4. Verify the live pages still render (open them / do a headless check).

When you finish:
5. Add a `CHANGELOG.md` entry (date, what changed, why, any follow-ups).
6. Commit with a clear message and push to `main`.
7. If you discovered stranded work on another branch or an unresolved
   inconsistency, note it in the CHANGELOG under "Open threads" and raise it
   with the owner.

---

## 8. Governance

`/governance/` holds the durable operating-governance layer as the repo grows
into an operational command center:

- `governance/CURRENT_STATE.md` — plain-language snapshot of where things stand.
- `governance/DECISION_LOG.md` — durable strategic decisions + reasoning (e.g.
  Arizona single-member LLC / Schedule C / cash basis; no S-Corp yet; insurance
  deferred; print-on-demand under Deadhang). Consult before reversing direction.
- `governance/handoffs/` — dated AI/human handoff documents.
- `governance/README.md` — the folder's purpose and the Stage 0–5 evolution plan.

This file (`AGENTS.md`) is the collaboration standard; `CHANGELOG.md` is the
work/decision log; `CHATGPT_HANDOFF.md` is the standing AI-onboarding handoff.
Together with `/governance/` they are the governance system — don't duplicate
across them.
