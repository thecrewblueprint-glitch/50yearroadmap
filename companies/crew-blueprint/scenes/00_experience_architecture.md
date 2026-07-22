# 00 — Experience Architecture (the framework lessons plug into)

**Status:** Framework **prototype built** 2026-07-22 ("The Shop Floor"). Delivered
privately; content-free. This doc is the durable spec so every future lesson plugs
in the same way and the composable, walkable, VR-ready future stays open.

## Why this exists

The owner asked whether the prototypes could *layer into one seamless, forward-
progressing experience with walking and deeper interaction* — not a pile of
separate click-games. Answer: yes, **if** the shared engine is built once and
lessons plug into it as modules. So we built the engine first, on purpose, before
more content. This is the substrate; lessons are data on top of it.

## What the framework owns (so lessons don't re-solve it)

- **World** — one continuous walkable jobsite (floor, bounds, lighting, ambient
  props), not a per-lesson scene.
- **Player** — a first-person **rig** you **walk** (touch joystick / WASD / arrows)
  and **look** (drag / mouse / headset). Movement is relative to gaze; bounded.
- **Interaction** — a **reticle** (center-screen marker) + **tap** + **VR
  controller ray**. Objects register as *interactables* with a label, a range, and
  an `onActivate`. This is the "deeper than clicking" seam: today it's aim-and-act;
  grab/drag/manipulate extend the same registry later.
- **HUD** — objective, teach banner, toast, reticle affordance, XP/level — shared,
  API-driven. Lessons call `ctx.hud.teach(...)`, never build their own.
- **Progression** — XP, level, per-module completion, **saved to localStorage**.
  One player profile across all lessons.
- **Audio, resize, DPR, WebXR** — all shared.

## The module contract (how a lesson plugs in)

A lesson is a **module** registered with `CB.registerModule({...})`. The engine
places it at a **station** (a glowing pad + floating label) in the world, detects
when the player is near, builds it on approach, routes interaction to it, and
awards XP on completion. The shape:

```js
CB.registerModule({
  id: 'coil-line',                 // unique; also the save key
  title: 'Coiling',                // shown on the station label
  brief: 'Coil the cable over-under.',
  station: { x: -4, z: -3, color: 0x4defa1 },   // where it lives on the floor
  build(ctx) {                     // create meshes into ctx.group (auto-placed)
    const cable = CB.outline(CB.makeBox(...));   // inherits the anime look
    ctx.interactable(cable, { label: 'Coil', onActivate: (ctx, mesh) => { ... } });
  },
  onEnter(ctx) { ctx.hud.objective('Alternate over / under.'); },
  update(ctx, dt) { ... },         // optional per-frame
  // call ctx.complete(score, { title, body }) when the learner finishes
});
```

**The `ctx` an engine hands each module** (its whole SDK surface): `THREE, scene,
group, camera, rig, playerPos(), interactable(mesh, opts), hud {objective, teach,
toast}, beep, progress {xp, addXP, isDone}, complete(score, opts), rng`. Plus
world-building helpers on `CB`: `makeBox`, **`mat(color)`** (anime toon material),
**`outline(mesh)`** (silhouette), `gradientMap`.

**The rule that keeps the vision open:** a lesson only ever touches the world
through `ctx` and `CB` — it never sets up its own renderer/camera/controls. That's
what lets the existing atoms (Coil Line, Make It Safe, truss-pin) become **stations
in one world** instead of separate files, and what makes walking + VR + deeper
interaction upgrades land everywhere at once.

## Migration path for the existing atoms

Coil Line and Make It Safe are today standalone files. To fold them in: move each
one's *scene-building + interaction* into a `build(ctx)` using `ctx.interactable`,
delete its private renderer/camera/HUD (the engine provides those), and register it
at a station. The teaching logic and consequences carry over unchanged.

## Roadmap on the build ladder

- Rung 1 cards ✅ · Rung 2 2D scene ✅ · Rung 3 first-person 3D atoms ✅
- **This framework = the connective tissue that turns rung-3 atoms into one
  walkable world** — and the on-ramp to Rung 4 (full sim / VR), since it's already
  WebXR-enabled and the player is a movable rig.

## Aesthetic

**Anime / cel-shaded** (owner, 2026-07-22): toon materials (banded lighting) +
black inverted-hull **outlines**, a soft gradient sky, and a brighter, more
saturated palette. Baked into the engine's material layer (`CB.mat` / `CB.outline`)
so all content inherits it. See `governance/DECISION_LOG.md` and doc 06 (brand).

## Where it lives

- **The content-free framework is committed to this public repo** at
  `companies/crew-blueprint/experience/the-shop-floor.html`, and is playable at its
  GitHub Pages URL (no download needed). It has no lesson content and no PII — it is
  the engine, safe to publish.
- **Lesson content and the lesson-carrying playable builds stay private** (Drive),
  per doc 09. So: the *engine* is public; the *lessons* that plug into it are not.
  This repo records how modules plug in — never the built lesson content.
