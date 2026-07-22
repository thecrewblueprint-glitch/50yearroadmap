# Experience — playable framework

This folder holds the **playable experience framework** for The Crew Blueprint —
the walkable, anime/cel-shaded, WebXR-ready engine that skill lessons plug into as
modules at stations.

## What's here

- **`the-shop-floor.html`** — the framework prototype, a single self-contained file
  (no backend, no build step, runs offline; open it in a browser). Walk with a
  touch joystick / WASD, look by dragging / mouse, and interact with a center
  reticle + tap (or VR controller ray on a headset). It ships with **three
  throwaway placeholder stations** only to prove the loop (walk → interact →
  complete → earn XP → save). **No lesson content.**

## Live

Because this repo publishes GitHub Pages, this file is playable at its Pages URL
(project path `companies/crew-blueprint/experience/the-shop-floor.html`).

## How lessons plug in

See the architecture + module contract: `../scenes/00_experience_architecture.md`.
A lesson registers with `CB.registerModule({...})` and only touches the world
through the `ctx` / `CB` SDK — it never builds its own renderer, camera, or
controls. That's what lets the standalone atoms (Coil Line, Make It Safe) become
stations in this one world.

## Guardrail

**Only the content-free framework lives in this public repo.** Full **lesson
content** and the lesson-carrying playable builds stay in private storage (Drive),
per `../09_content_inventory.md` (doc 09). This file has no lesson content, no PII —
it is the engine, safe to publish.
