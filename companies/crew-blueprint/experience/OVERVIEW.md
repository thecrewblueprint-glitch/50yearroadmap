# The Crew Blueprint — Playable Experience (digest)

**One-page digest of the gamified learning experience: what it is, how it got
here, what exists, how it's built, and where it's going.** The detail lives in the
docs mapped at the bottom; this is the hub.

_Last digested: 2026-07-22._

---

## What it is

A **gamified, first-person, walkable, cel-shaded ("anime") jobsite** that teaches
live-event field-hand skills. Learners walk a shop floor and do the real jobs at
**stations**; each station is a **lesson** that plugs into one shared engine.
Web-first (Three.js), runs from a **single self-contained file offline**, and is
**WebXR-ready** so the same scenes can enter VR later.

The bet, in one line: **teach a specific skill, let people fail safely and see the
cost, in a place they can actually move through** — the thing simulation buys over
a video or a quiz.

---

## How it got here — the decisions (see `governance/DECISION_LOG.md`)

- **Gamified, static, browser-based — not an LMS.** Simpler, and it sidesteps the
  platform instability that stalled the LMS.
- **Teach a specific skill first; safety is the ambient layer** (corrects the early
  "make awareness the objective" prototype).
- **Safe failure with real, visible consequences** — learners fail safely, see the
  cost, and assess the safety conditions themselves. The consequence is the teacher.
- **Full lessons are role-based, end-to-end workflows** — first target: the
  **lighting hand from truck to trim** (`scenes/lighting-hand-truck-to-trim.md`).
- **3D / VR is the destination; web-first is the on-ramp.** VR is a *port*, not a
  restart (the player is a movable rig; WebXR is wired in).
- **Build the composable framework first**, so lessons plug in as modules and every
  upgrade (walking, VR, deeper interaction) lands everywhere at once.
- **Aesthetic: anime, with a realistic palette** — cel shading + black outlines, but
  believable jobsite colors (concrete, aluminium truss, black cases, hi-vis).
- **Playable prototypes are public (a showcase); full course content is private.**

---

## The build ladder — where we are

1. **Cards** — skill tree + XP. ✅ (Module 1)
2. **2D scene** — look-around jobsite. ✅ (Dock Sweep)
3. **First-person 3D** — atoms + the **framework** + **first lessons on the
   framework**. ✅ (this is the current rung)
4. **Full simulation / VR** — the far-future endgame. ⏳

Rung 3 is proven: real lessons run inside one walkable world.

---

## What exists now (playable)

**In this repo, public, live on GitHub Pages** (`experience/`):

- **`the-shop-floor.html`** — the **framework** (engine + placeholder stations).
- **`lighting-hand.html`** — the **lighting-hand arc**, five stations:
  1. **Load-In** — pick up a road case and **carry** it to its spike mark (staging).
  2. **Coil** — coil a cable over-under (wrong rhythm builds twists).
  3. **Pin the Truss** — seat all 4 pins, then call it ready (early = warned).
  4. **Hang & Make Safe** — clamp / bond / address / check, then fly; **skip the
     bond and it falls to the deck** (safe failure).
  5. **Fly to Trim** — **walk out of the red drop-zone**, then call the fly.

**Private, in Drive** (earlier prototypes + the product): the Module 1 skill tree,
Dock Sweep, the standalone Coil Line & Make It Safe atoms, and the full course
packets.

---

## How it's built (architecture — see `scenes/00_experience_architecture.md`)

- The **engine owns** world · player (walk + look) · interaction (reticle + tap +
  VR ray + **grab/carry**) · HUD · **progression (XP, levels, saved)** · WebXR.
- A **lesson is a module** — `CB.registerModule({ id, title, station, build(ctx),
  onEnter, update, ... })` — and it only ever touches the world through the
  **`ctx` / `CB` SDK** (never its own renderer/camera/controls). That's what lets
  the atoms become stations in one world.
- **Deeper-than-tapping** is live: `ctx.hold` / `release` / `held` (pick up, carry,
  set down). Next: drag-to-fit, two-hand manipulation.
- **Look/feel:** cel-shaded `CB.mat` toon materials + `CB.outline` silhouettes,
  realistic palette, a **floating joystick** (spawns under the thumb, steers by
  drag direction, stops instantly on release).

**Controls:** floating joystick / **WASD** to walk · drag / mouse to look ·
reticle + **tap** / **E** / click / VR trigger to interact.

---

## Research backing (see `partnerships/research/05_how-comparables-are-built.md`)

The stack and loop are validated against how the field actually builds this:
Interplay (web 3D + VR) and Transfr (native VR), plus the simulation-training
learning science (deliberate practice, fading scaffolds, terminal feedback,
briefing→scenario→debrief, fidelity matched to the learner). Conclusion:
**Three.js web-first now, VR later as a port**, with the learn → do → check →
debrief loop.

---

## Open threads / next steps

- **Owner input still owed** (feeds the workflow doc): what "**bridges**" means when
  plugging fixtures; how much of **focus** is hand-work vs board-work.
- **Next frontiers** (owner to steer): drag-to-fit **manipulation**; chaining the
  stations into **one continuous run** (carry → build → hang → fly as a flow); more
  of the truck-to-trim workflow as stations; polish toward the VR rung.
- **Iterate on feel** from the owner's playtests.

---

## Doc map (where the detail lives)

| Doc | What it covers |
| --- | --- |
| `experience/README.md` | The playable files + public/private split |
| `scenes/00_experience_architecture.md` | Module contract, engine, carry SDK |
| `scenes/lighting-hand-truck-to-trim.md` | The full 9-step lighting-hand workflow design |
| `05_platform.md` | Delivery decision + the build ladder |
| `06_brand.md` | Anime / realistic-palette aesthetic |
| `09_content_inventory.md` | Content map + the public/private guardrail |
| `partnerships/research/05_how-comparables-are-built.md` | How the field builds this + learning science |
| `governance/DECISION_LOG.md` | Every decision, with reasoning |
| `CHANGELOG.md` | Chronological build log |
