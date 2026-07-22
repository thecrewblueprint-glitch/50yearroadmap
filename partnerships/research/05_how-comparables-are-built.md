# 05 — How Comparable Experiences Are Built (manifestation + build insights)

**For:** The Crew Blueprint gamified/3D build (`cb-5`, build ladder in
`companies/crew-blueprint/05_platform.md`).
**Question the owner asked:** don't just find *who* exists — study **how these
things are manifested**, so we build ours with better insight and know **what it's
going to take.** (Companion to `research/01`, which covered the market/whitespace.)
**Researched:** 2026-07-22 (web).

## Bottom line — the build insights that matter for us

1. **Web-first (Three.js) is the right rung for now; VR is a later port, not a
   restart.** The leaders split into two build stacks: **web 3D** (Interplay's
   "SkillMill" runs in a browser on tablet/computer *and* VR) and **native VR on
   standalone headsets** (Transfr on Meta Quest, welding sims). Web 3D is
   progressive, mobile-friendly, light, and speaks WebXR/WebAudio/DOM natively —
   exactly what our self-contained, no-budget, phone-first prototypes need. Unity
   WebGL ships physics/animation for free but costs 10–25 MB and loads slowly on
   phones. **Our Three.js path is the correct, cheap rung** — and because it's
   already WebXR-capable, the same scene is the on-ramp to the headset later.
2. **The proven core loop is exactly what we're doing:** *teach the concept →
   practice the task hands-on in a risk-free space → get feedback → repeat.*
   Interplay explicitly sells "actively practice… before working in the field."
   That's our learn → do → check → result.
3. **Motion/skill sims win on immediate, specific feedback + reps — not graphics.**
   Welding sims teach by tracking a few real KPIs (**angle, speed, distance**) and
   giving **instant feedback + a debrief**, building muscle memory through
   **repetition at rising difficulty** (basic → expert). Fidelity is secondary to
   the feedback loop. (Coil Line already does the cheap version: right/wrong loop →
   instant result → a debrief.)
4. **The learning science backs our instincts hard** (see below) — deliberate
   practice, fading scaffolds, terminal feedback, briefing→scenario→debrief, and
   *fidelity matched to the learner*. We don't need photoreal; we need the loop.
5. **What it's going to take, realistically:** the *engine* is solved (Three.js,
   inlined). The real work is **content fidelity of the procedure** (getting each
   step and its consequence right — which is why the owner's field corrections are
   the actual moat) and **building a small reusable scene kit** (look-around
   camera, tap/act, prompt/teach banner, debrief, WebXR hook) so each new atom is
   assembled, not rebuilt from zero.

## How the leaders manifest it

### Transfr — native VR, standalone headsets
- **Stack/delivery:** built for **standalone Meta Quest** headsets (Unity-class),
  managed fleet deployment (ManageXR); content is heavy (~60 GB across sims).
- **Design:** short, **"day-in-the-life"** experiences; **career exploration** +
  skills; maps to recognized standards (**OSHA, NCCER, ASE**).
- **Takeaway for us:** headset VR gives the deepest immersion but carries hardware,
  fleet-management, and content-weight costs. It's a *destination*, reached once
  the loop is proven — not where you start with no budget.

### Interplay Learning — web 3D **and** VR (the closest model to ours)
- **Stack/delivery:** **"SkillMill"** runs **in a browser on tablet/computer**, and
  also on VR. Same content, multiple devices — device-flexible, web-first.
- **Design:** "online modules, videos, **3D simulations**, and knowledge checks";
  learners **practice troubleshooting/repairs on lifelike equipment in a risk-free
  virtual environment**; **game-like**, points/badges. Has a **crane & rigging**
  pathway (entertainment-adjacent).
- **Takeaway for us:** this is the **template** — web-delivered 3D sim + knowledge
  checks + game layer, portable to VR. Validates our exact ladder (web 3D now,
  headset later) and our loop.

### Welding / forklift sims — motor-skill manifestation
- **Welding:** core loop = **physically manipulate the tool**; system tracks a few
  KPIs (**torch angle, speed, distance**, heat), gives **real-time feedback + a
  performance report**, tiers difficulty **basic → intermediate → advanced →
  expert**. Builds **muscle memory** safely.
- **Forklift:** simulator games used for **classroom accreditation-aligned**
  training.
- **Takeaway for us:** you teach a physical skill by **naming 2–3 measurable things
  that make it right**, giving **instant feedback** on them, and **repeating at
  rising difficulty**. For coiling that's *alternation + rhythm*; for the safety
  cable it's *is it on, is it rated, is it seated*.

## What the learning science says (it validates the plan)

From simulation-based training research (medical/procedural — the most studied):

- **Deliberate practice + mastery learning** are the effective core: repeated,
  focused reps against a standard. → our repeat-until-clean loop.
- **Scaffolding should FADE** — heavy guidance early, then withdrawn so the learner
  internalizes it. → our learn → do → **recall-check** (we already fade the prompt).
- **Terminal feedback (at the end) beats continuous feedback for novices.** → the
  end-of-run **debrief** is pedagogically right; don't over-coach mid-task.
- **Briefing → Scenario → Debriefing (BSD)** is the standard structure. → our start
  overlay → play → debrief maps to it exactly.
- **Rapid Cycle Deliberate Practice (RCDP):** quick reps with immediate reset
  outperform long one-shot runs. → keep scenes short and instantly replayable.
- **Fidelity should be modulated to the learner** — more realism is *not* always
  better, especially for novices. → the cards → 2D → 3D → VR ladder is
  pedagogically sound, not just a budget compromise. Don't over-build fidelity
  before the loop is right.

**And it validates the owner's core instinct:** *safe failure with visible
consequences* is precisely what simulation buys over video/quiz — a risk-free space
to make the mistake and see its cost.

## What this means for our prototypes (design rules to apply now)

1. **Name the 2–3 things that make the skill right**, and give instant feedback on
   each. (Coiling: alternate + rhythm. Safety cable: on / rated / seated.)
2. **Keep the BSD shape:** brief (what + why) → do it → **debrief** with the
   consequence. Fade the guidance across reps; put the real teaching in the debrief.
3. **Short and instantly replayable** (RCDP) — a scene is a 60–120s rep, not a level.
4. **Don't chase fidelity** — a legible low-poly scene with a tight feedback loop
   beats a pretty one that doesn't teach. Match fidelity to the rung.
5. **Build a reusable scene kit**, so atoms are assembled, not rebuilt: shared
   look-around camera, tap/act hit-testing, prompt/teach banner, debrief + ratings,
   WebXR hook, audio. (Coil Line and Dock Sweep already share most of this — next
   step is to factor it into a small common core.)
6. **Web-first, WebXR-ready** — every scene runs on a phone from one file and can
   enter VR later without a rewrite. VR is a port, not a restart.

## Sources
- [Interplay Learning](https://www.interplaylearning.com/) · [SkillMill (Toolkit Technologies)](https://toolkittech.com/shop/interplay-skillmill-elearning/) · [Interplay on Meta Quest](https://www.meta.com/experiences/interplay-learning-player/4325901304108120/)
- [Transfr](https://transfrinc.com/) · [Transfr + ManageXR (deployment)](https://www.managexr.com/customer-stories/transfr-and-managexr-create-classroom-to-career-pathways-for-the-workforce-of-the-future)
- [WeldVR (Meta)](https://www.meta.com/experiences/weldvr/5683349178385056/) · [Guideweld VR case study (Totem Learning)](https://www.totemlearning.com/guideweld-vr-welding-simulation-game) · [Simulanis welding simulator](https://www.simulanis.com/welding-simulator)
- [Industry Lift — forklift/serious sims](https://industrylift.org/welding-simulator-vr-game/)
- Learning science: [Teaching Procedural Skills (MedEdPORTAL)](https://www.mededportal.org/doi/10.15766/mep_2374-8265.11476) · [Rapid Cycle Deliberate Practice (StatPearls/NCBI)](https://www.ncbi.nlm.nih.gov/books/NBK551533/) · [Simulation-based training instructional design (Springer)](https://link.springer.com/article/10.1007/s11251-025-09763-2) · [Video-guided deliberate practice (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8368709/)
- Build stacks: [Three.js vs Unity for Web (Utsubo)](https://www.utsubo.com/blog/threejs-vs-unity-web-comparison) · [Web game engines 2026 (Cinevva)](https://app.cinevva.com/blog/2026-06-09-web-game-engines-2026-comparison.html)
