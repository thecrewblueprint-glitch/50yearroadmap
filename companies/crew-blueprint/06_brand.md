# 06 — Brand

**Status:** Documented (identity decided; exact values referenced to the site
CSS as source of truth).

## Identity

- **Industrial styling** — clean, professional, built for the trade; visual
  language drawn from the live-event/rigging world.
- **Dark theme** — the default look.
- **Professional tone** — credible and grounded, not academic and not hype.
- **Safety-first philosophy** — safety is a visible value, not an afterthought.
- **Field-experience-driven** — the brand reads as written by someone who has
  done the work, for people who do the work.

## Positioning in the voice

- **Practical job readiness over academic instruction.** The brand consistently
  favors "here's how the job actually works" over theory.
- Honest about boundaries — the "not a certifying body" posture (doc 02) is part
  of the brand's credibility, not fine print.

## Design system (its own CSS schema)

The Crew Blueprint maintains **its own CSS/brand schema**, separate from the
other projects (Deadhang Labor, this roadmap/command center, and Production
Atlas each keep their own — see
`companies/deadhang-labor/08_brand.md`). The **live site CSS is the source of
truth** for exact colors and type; values are not hardcoded here, so the brand
stays in sync with the site (industrial *Extendable* theme — see doc 05).

## Game aesthetic — anime / cel-shaded (owner, 2026-07-22)

The **playable experience** has a distinct **anime** look — deliberately not the
grey, corporate feel of most training sims. Baked into the experience framework's
material layer (`CB.mat` / `CB.outline`; see
`scenes/00_experience_architecture.md`) so all lessons inherit it:

- **Toon / cel shading** — banded (stepped) lighting instead of smooth gradients.
- **Outlines** — crisp black inverted-hull silhouettes on hero objects and
  characters.
- **Realistic palette, anime rendering** (owner refinement, 2026-07-22): *real*
  jobsite colors — concrete-grey floors, dark industrial walls, aluminium truss,
  black road cases / fixtures, hi-vis yellow crew, a dim warehouse backdrop — drawn
  in the cel-shaded + outlined style. The goal is "real colors that look like anime
  artwork," not a stylized/neon palette. Gameplay-signal colors stay as clear
  accents (hi-vis, safe-green go-markers, red hazard, safety-amber bond).

This is the *game* aesthetic; the website/marketing brand above (industrial
*Extendable*) still governs the site. Recorded in `governance/DECISION_LOG.md`.

## Asset locations (referenced)

Logos, imagery, and design assets are maintained in the private content
repository, not duplicated here.
