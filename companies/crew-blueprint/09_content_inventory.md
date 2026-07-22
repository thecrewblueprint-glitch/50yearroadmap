# 09 — Content Inventory

**Status:** Documented (inventory of existing course content; reviewed 2026-07-21).
**The content itself lives in private storage (Google Drive), not this public
repo** — full lessons are the product. This is the public-safe **map**: what
exists, where, its state, and how ready it is to gamify.

> **Where it lives:** Google Drive, the owner's **personal Google account**, in a
> hub folder **"Course Data Packages,"** organized by discipline, plus separate
> WordPress site backups. (This is the only account visible to the connector; if
> content also lives on another account or the owner's computer, it isn't
> reflected here — confirm and consolidate.)

## The content hub — "Course Data Packages"

| Folder | What's in it | State |
| --- | --- | --- |
| **Course 1: Your First Work Call** | The ground/field-hand fundamentals course (Module 1 complete — see below); QA review reports | ✅ Module 1 complete; more modules to come |
| **Playable Prototypes** | The self-contained playable builds (see below) + an "About" record | ✅ 3 prototypes; newest = *Coil Line* (3D) |
| **Module Data Packages** | `module-01-lessons.json` (structured lessons) + `crew-blueprint-v0.3-data-module-01.zip` | ✅ structured, gamification-ready |
| **Rigging & Hardware** | `TCB-RIG-201_Rigging_Course_Final.pdf` | ✅ final — but **advanced/future** (not the entry point) |
| **Predictive Hazard Recognition** | `Predictive_Hazard_Recognition_Course.docx` | ✅ drafted |
| **Lighting Production Flow** | (discipline folder) | ⏳ started |
| **Video Systems** | (discipline folder) | ⏳ started |
| **Industry Standards & Research** | Stagehand pathways, career profiles, industry data | reference |
| **Curriculum Development Workflows** | Process/workflow docs | reference |
| **Course checklist**, **Course Groupings & Syllabus Review** (×3) | Planning/QA spreadsheets | ⚠️ multiple versions — consolidate |

Separate: **WordPress site backups** (`backup_*_The_crew_blueprint_*.zip/gz` — DB,
plugins, themes, uploads) in their own folder. Strategy docs
(`Deadhang_CrewBlueprint_Master_Strategy`, business plans) in another.

## Course 1, Module 1 — the ground-first core (complete)

Five entry-level, US-context lessons (titles only — full text stays private):

1. What a Stagehand Actually Does
2. The Difference Between Load-In, Show Call, and Load-Out
3. Common Work Environments (arena / theater / convention / outdoor)
4. Who Is on the Crew
5. What Makes a New Stagehand Valuable

This **is** the ground/field-hand fundamentals the repositioning calls for
(doc 00/01; roadmap `cb-4`). It follows the standardized lesson architecture
(doc 03) — purpose, learning objective, teaching points, script, example tasks,
safety notes, reflection question, knowledge check, key takeaway — and it's been
through a QA/proofreading review pass.

## Gamification readiness (why this matters for `cb-5`)

`module-01-lessons.json` is already a **structured data model**: an array of
lessons, each with a `knowledge_check` (→ the quiz/challenge), `example_tasks`
(→ interactions), `reflection_question`, and `key_takeaway`. That maps almost
directly onto a gamified skill-tree module:

- **5 lessons → 5 nodes** in the Course 1 branch of the skill tree.
- **`knowledge_check` → the node's check-for-understanding** (XP on pass).
- **`example_tasks` → the one real interaction** per node (e.g. "sort these into
  load-in vs. load-out").
- Progress tracked client-side (localStorage), no backend (doc 05).

So **`cb-5` is a packaging task, not a content task** — wrap this existing JSON in
the static gamified shell.

## Playable Prototypes (the built experiences)

Stored in **Course Data Packages → "Playable Prototypes"** (Drive). Each is one
self-contained HTML file — no install, no backend, no internet needed. The files
are kept out of this public repo on purpose (the repo records that they exist;
the playable content lives in Drive). Rungs of the build ladder (doc 05):

1. **Module 1 — "Your First Work Call"** — cards / skill tree (rung 1).
2. **Dock Sweep** — first 2D look-around scene (rung 2).
3. **Coil Line** — first true 3D / WebXR scene (rung 3); teaches over-under
   coiling skill-first, safety ambient, safe-failure "bird's-nest" consequence.

## Finalization / consolidation (the owner's "which account has what" problem)

1. **Confirm scope** — everything the connector sees is in the owner's **personal
   Google account**. Confirm nothing critical lives only on the owner's computer
   or another account; if it does, move it into "Course Data Packages."
2. **De-duplicate** — one canonical of "course 1, module 1" (there's a "Copy of…"),
   and one syllabus-review sheet (there are three).
3. **Keep the source of truth clear** — the DOCX/JSON packets are canonical
   (doc 07); the WordPress backups are a *deploy target*, not the source.

## Guardrail

Full lesson content is the product and stays in private storage. This inventory
lists titles, structure, and state only — never the lesson bodies.
