# 06 — Validation

**Status:** Documented (validation strategy exists; ~90%).

## What validation checks

The repository includes validation rules to verify the app and its research stay
consistent:

- **Active pages load the correct shared assets.**
- **Required manifests are present.**
- **Branch packages correspond to research reports.**
- **Legacy runtime references are removed.**

## Why it matters

Because the app is static and manifest-driven (docs 01, 04), the risks are
structural: a page pointing at the wrong assets, a missing manifest, a package
with no backing report, or leftover legacy references. Validation catches exactly
these — it keeps the manifest-driven system honest so a research package always
has a real report behind it and every active page loads what it should.

## Relationship to data cleanup

Validation and the modernization/cleanup work (doc 01) reinforce each other: the
cleanup removed legacy bridge code and migrated pages toward the shared core, and
the validation rules ensure legacy references stay gone and the shared-asset
wiring stays correct going forward.

## Remaining

Validation is strong (~90%) but not the finish line — as new departments and
pages are added, the rules should keep pace (e.g. covering the normalized date
wiring as it reaches all applicable pages, doc 08).
