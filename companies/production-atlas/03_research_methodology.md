# 03 — Research Methodology

**Status:** Documented (methodology complete).

## Structured packages, not notes

Research is organized into **structured packages** instead of free-form notes.
This is the core methodological decision: information is captured in a consistent,
machine-loadable structure so the static app can read it (doc 04) and so
departments can grow independently (doc 05).

## Categorized by confidence and verification

Information is categorized by **confidence and verification status.** Not all
research is equal — the methodology tracks how well-verified each piece is, so
the app can respect those gradations rather than presenting everything as equally
certain.

## Public-safe vs internal separation

There is a **clear separation between public-safe information and internal
research.** The public-facing app publishes only what passes the public-data
policy (doc 07); everything else stays internal (on the research-version branch,
doc 02). This boundary is the backbone of the whole approach: research can be
thorough and candid internally while the published surface stays safe.

## How it fits together

1. Research is gathered and written into structured packages.
2. Each item is tagged with confidence / verification status.
3. Public-safe items flow to the published app via manifests (doc 04); internal
   items stay internal.
4. Validation (doc 06) checks that packages, manifests, and reports line up.

The result is a methodology that scales: new research is added as packages, its
trustworthiness is explicit, and the public/private line is enforced by
construction.
