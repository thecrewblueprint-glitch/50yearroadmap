# 05 — Platform

**Status:** Documented. Foundation in place; next-generation platform
**intentionally deferred** (roadmap `cb-3`).

The key strategic fact: **The Crew Blueprint is no longer blocked by software
development.** The website stays a **lightweight presentation layer** until there
is enough content to justify building the next-generation platform. Content, not
engineering, is the priority (see doc 08).

## Website foundation (in place)

- **Domain** secured.
- **Hosting** in place (WordPress.com).
- **Theme** selected — *Extendable* — carrying the industrial visual direction
  (see doc 06).
- **Staging-first workflow** — changes are made on staging before production.
- **Industrial visual direction** applied.
- **Coming Soon strategy implemented** — public front while content is built.

## Plugin architecture (defined)

A **modular** architecture is decided (build deferred with the platform). The
modules:

- **Crew Blueprint Core** — shared foundation/services.
- **Site Shell** — presentation/navigation frame.
- **LMS** — course delivery and progression.
- **Resource Hub** — supporting resources and references.
- **Safety Notices** — surfacing safety callouts/disclaimers consistently.
- **Content Studio / Content Engine** — authoring and content generation.

The modular philosophy is settled; the point is to keep concerns separate so the
platform can be built incrementally when the time comes.

## Deferred (intentionally parked, not failed)

These were consciously paused so effort goes to content first:

- **Legacy WordPress LMS** — deferred.
- **JSON import system** — deferred.
- **Plugin debugging** — deferred.

## Future projects (next-generation platform)

Explicitly out of scope for now; revisited once content volume justifies it:

- **Laravel backend**
- **AWS infrastructure**
- **Database redesign**
- **RAG implementation**
- **Advanced search**
- **User accounts**
- **Mobile application**

## Interim content surface

Until the next-gen platform exists, finished course content is presented
lightly — generated from the canonical DOCX packets (doc 07) onto the website /
Coming-Soon surface. The packet remains the source of truth; the website is a
view of it.
