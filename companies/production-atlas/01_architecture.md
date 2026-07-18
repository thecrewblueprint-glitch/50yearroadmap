# 01 — Architecture

**Status:** Documented (architecture defined and settled).

## Shape of the system

Production Atlas is a **static GitHub Pages application** that reads structured
research packages. It is deliberately minimal — the intelligence lives in the
data (the research packages), not in server-side services.

**By design, it has:**

- **No backend**
- **No login system**
- **No database**
- **No payment system**
- **No private contact storage**
- **No automated scraping**

## Why static

The app **reads structured research packages rather than relying on dynamic
services.** This keeps it durable, cheap to host, hard to break, and safe: with
no backend, no accounts, and no private storage, there is no sensitive runtime
surface to protect. The production repository stays a **static application**
while research is **maintained separately** (see docs 02–03).

Consequences that follow from the static model:

- Content updates flow through research packages and manifests (doc 04), not
  database writes.
- Departments can be expanded independently by adding packages (doc 05).
- The public/private data boundary is enforced at authoring time, not at runtime
  (doc 07).

## Modernization / cleanup (completed)

The application has undergone significant cleanup toward a cleaner shared-core
architecture:

- **Manifest-driven branch loader** — active pages load research via manifests.
- **Approximate opportunity date normalization** — a normalized date system for
  approximate dates.
- **Removal of legacy bridge code** from active pages.
- **Migration toward the newer shared core architecture** (shared assets across
  active pages).

Remaining modernization work (finishing the normalized date wiring across all
applicable pages, continued cleanup) is tracked in doc 08.
