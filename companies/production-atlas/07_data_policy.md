# 07 — Public Data Policy

**Status:** Documented (policy established — 100%).

This is the rule that governs everything the public Production Atlas app is
allowed to show. It is the reason the project can be candid in internal research
while staying safe in public.

## The public app must NOT expose

- **Private contact information**
- **Internal notes**
- **Pay rates**
- **NDA-protected information**
- **Client-sensitive information**
- **Rumors or unverified claims**

## Internal research stays separate

**Internal research remains separate from the public-facing application.** The
public/private separation from the research methodology (doc 03) and the
repository/branch separation (doc 02) exist precisely to enforce this policy:
sensitive material lives in internal research (research-version branch), and only
public-safe, verified information reaches the published app.

## How it's enforced

- **At authoring time** — research is categorized public-safe vs internal
  (doc 03); only public-safe items are manifested into the app.
- **Structurally** — production code and internal research are separate (doc 02),
  and the static app has no private storage or backend (doc 01), so there is no
  mechanism by which private data would leak at runtime.
- **By validation** — validation rules (doc 06) keep the app loading only intended
  packages/manifests.

## Consistency with the wider system

This mirrors the public-safety discipline applied across the whole command center
(the repository's `DATA_SAFETY_POLICY.md` and roadmap public-safety schema):
nothing private, no unverified claims, in any public surface. Production Atlas's
data policy is the domain-specific expression of that same principle.
