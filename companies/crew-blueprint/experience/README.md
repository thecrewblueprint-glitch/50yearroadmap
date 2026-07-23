# Experience — playable prototypes

> **New here? Read [`OVERVIEW.md`](OVERVIEW.md)** — a one-page digest of the whole
> experience effort (what it is, the decisions, what exists, how it's built, and
> what's next). This README covers just the files in this folder.

Playable prototypes of The Crew Blueprint learning experience — the walkable,
anime/cel-shaded, WebXR-ready engine and the lessons that plug into it. Each is a
single self-contained file (no backend, no build step, runs offline; open it in a
browser). Because this repo publishes GitHub Pages, each is playable at its Pages
URL.

## What's here

- **`the-shop-floor.html`** — the **framework** (engine only). A walkable jobsite
  where lessons plug in as modules at stations. Ships with placeholder stations to
  show the loop (walk → interact → complete → earn XP → save). Content-free.
- **`lighting-hand.html`** — the **lighting-hand lesson arc** on that framework:
  five stations — **Load-In** (carry a road case to its spike mark), **Coil**
  (over-under), **Pin the Truss**, **Hang & Make Safe** (skip the bond and it
  falls), **Fly to Trim** (walk clear of the drop-zone before calling the fly).
  Controls: floating joystick / WASD to walk, drag / mouse to look, reticle + tap
  (or **E**/click, or a VR controller ray) to interact.

## How lessons plug in

See the architecture + module contract: `../scenes/00_experience_architecture.md`.
A lesson registers with `CB.registerModule({...})` and only touches the world
through the `ctx` / `CB` SDK — never its own renderer, camera, or controls.

## What's public here vs. private

**Playable prototypes live here (public)** — they are the transparent showcase of
what's being built, and are protected by the repository `LICENSE` (all rights
reserved; visibility is not a licence to use). **The full course content** — the
canonical DOCX/JSON course packets, complete curriculum, and lesson scripts (the
actual product) — **stays in private storage (Drive)**, per `../09_content_inventory.md`
(doc 09). So: prototypes = public showcase; full course product = private.
