# 02 — Dashboard

**Status:** Documented (built and live — roadmap `po-1` completed, `po-4`
completed).

## What it is

A **static GitHub Pages dashboard** served from the repository root, rendering
`roadmap.json` (doc 01) into several focused views. It has no backend — `app.js`
reads the JSON and builds the pages client-side.

- **Live URL:** https://thecrewblueprint-glitch.github.io/50yearroadmap/
- **Files:** `index.html`, `app.js`, `styles.css`, `ninety.css`, `branch.html`,
  `present.html`.

## The views

- **Timeline** — the linear "you are here → Homestead" progression (the `journey`
  milestones): how to get from now to the end goal, step by step.
- **Dashboard** — the branch view: each branch's goal, % complete, blockers, and
  work items.
- **30 / 60 / 90** — the near-term operating windows (`thirty_sixty_ninety`),
  rendered by `renderNinetyDayDashboard()`.
- **Branch hubs** (`branch.html`) — each timeline branch link opens its own lean
  hub page with a sitemap menu and focused sub-views, rather than cramming
  everything onto one page.
- **The Vision** (`present.html`) — a shareable page showing the structure and the
  detailed pathway from now to the Homestead, for communicating vision to others.

## Design decisions

- **Layered views (overview vs. detail)** — Timeline/Dashboard/30-60-90 give the
  overview; branch hubs and The Vision give focused detail without clustering
  everything into one dense page (roadmap `po-4`).
- **Professional palette** — a blue/teal professional color structure (not the
  earlier gold).
- **Pagination** — used to organize features/segments without overwhelming.
- **Header** — "Deadhang Labor" branding; the "50-year" framing was dropped.

## Serving detail (important)

GitHub Pages serves from the **repository root**, not `/docs`. Edits must go to
the root files. (A past bug was edits landing in a `/docs` copy that Pages didn't
serve; the duplicate was removed.)

## Relationship to the interactive spec

A future, fully-interactive dashboard (drag-and-drop status changes, direct
editing, backend persistence) is specified in `INTERACTIVE_DASHBOARD_SPEC.md`.
That is **not built** — the current dashboard is read-only over `roadmap.json`,
and edits happen by changing the JSON. The interactive direction ties to the
database-migration decision (doc 05, OD-5).
