# 02 — Repository Strategy

**Status:** Documented (strategy established).

## Names

- **Product name:** Production Atlas.
- **Repository:** `thecrewblueprint-glitch/festival-atlas`.

The product is called Production Atlas even though the repository is named
`festival-atlas` — a naming detail worth stating up front so a new contributor
finds the right repo.

## Branching

- **Research work belongs on the `research-version` branch.**
- **Production-ready code is kept separate from research.**
- `main` / the production branch is **not** the active research source unless a
  change is explicitly requested there. Research-version changes should target
  `research-version`, not production, unless specifically directed otherwise.

## Why the separation

Keeping research separate from production-ready code means:

- The public, static app (doc 01) stays stable and clean.
- Research can move fast and iterate on its own branch without destabilizing what
  the public sees.
- The public/private data boundary (doc 07) is easier to hold, because internal
  research and the published app are physically separated.

## Practical rule for contributors

When doing research or data work, target `research-version`. When shipping
production-ready application changes, use the production path — and don't cross
the two unless explicitly asked. This discipline is a recurring instruction in
the project's working history and is treated as a standing rule.
