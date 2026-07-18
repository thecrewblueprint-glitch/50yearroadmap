# 04 — Application (Navigation & Package System)

**Status:** Documented (structure defined; navigation ~95%).

## Navigation model

The application structure is defined around these active pages:

- **Home**
- **Opportunities**
- **Employers**
- **Branches**
- **IATSE**
- **Matrix**
- **Analytics**
- **Sources**
- **Guide**
- **Map**
- **Schedule**

Together these establish the overall navigation model — from landing (Home) to
discovery (Opportunities, Employers, Map), structure (Branches, Matrix, IATSE),
insight (Analytics), and support (Sources, Guide, Schedule).

## Research package system (manifest-driven)

The package architecture is complete and is what makes the static app work:

- **Branch research is manifest-driven.** The app loads structured research
  packages via manifests rather than hard-coded datasets.
- **Departments expand independently.** Because content is loaded from packages,
  a department (doc 05) can be added or extended without touching the rest of the
  app.
- **Branch loader.** A manifest-driven branch loader wires packages into the
  active pages (see doc 01 modernization).

## How a page gets its data

1. A page references the manifests for the branches/departments it shows.
2. The loader reads the manifests and pulls in the corresponding public-safe
   research packages.
3. The page renders from that structured data — no backend call, no database.

This is why the app can be static yet content-rich: the "intelligence" is in the
packages and manifests, and the pages are views over them.
