# Scene design — Lighting Hand: Truck to Trim

**Status:** Design target (owner-requested, 2026-07-22). Not built yet.
**Type:** Role-based, end-to-end workflow lesson (see `governance/DECISION_LOG.md`
— "lessons are role-based full workflows" + "safe failure with real consequences").
**Role:** Lighting hand (ground crew / electrician's helper), **US standard.**
**Arc:** Walk a lighting hand all the way from *their fixtures on the truck* to
*a fixture floating at trim, powered on, and answering the board* — the point at
which the show can actually happen.

---

## The two design rules this lesson exists to prove

1. **Foreground = the specific craft the show needs.** Each beat teaches a real,
   named lighting-hand task (case handling, clamp + safety, cable dress, power-up).
   Situational awareness runs *underneath* every beat — never the headline.
2. **Safe failure with visible consequences.** The learner is *allowed* to make
   mistakes. Each mistake shows its **real cost** — a damaged fixture, a blocked
   fire lane, a tripped breaker mid-show, or (the big one) a fixture that falls
   from trim — **safely, with no one hurt.** The learner **assesses the conditions
   themselves** (Did I safety-cable it? Is anyone under the load? Is this circuit
   already loaded?) instead of being told. The consequence is the teacher.

The learner should leave able to *read a jobsite* — not just perform steps.

---

## The workflow, beat by beat

Each beat is an **atomic scene** (some atoms already prototyped). For every beat:
**Objective** (the specific skill) · **Ambient** (the awareness running under it) ·
**Safe-failure consequence** (what a mistake costs, shown safely) · **Assessed by
the learner** (the judgment call they must make themselves).

### Beat 1 — Unload from the truck
- **Objective:** Get lighting cases off the truck safely — control the ramp/liftgate,
  push a rolling case from the **ends** not the sides, two-hand the heavy ones, mind
  the tail of the case, keep it under control the whole way down.
- **Ambient:** Loaders and a forklift working the same truck; a sloped ramp; other
  departments' gear staged tight.
- **Safe-failure consequence:** Let a case get away on the ramp → it runs, tips, and
  a fixture inside is damaged (visible dollar cost) — or it catches a foot. Shown
  safely, then reset.
- **Assessed by the learner:** Is the ramp clear? Is this a one-person or two-person
  case? Who's behind me?
- **Atom status:** Case handling partly prototyped in *Dock Sweep*.

### Beat 2 — Stage / spot the cases
- **Objective:** Move each case to the right spot per the LD's plot / spike marks,
  in **build order**, without blocking paths or egress.
- **Ambient:** Keep the fire lane and walkways clear; other departments need the
  same floor.
- **Safe-failure consequence:** Stage in the wrong place or block a path → rework
  (you move it all again), the chief loses time, or the fire marshal flags the lane.
- **Assessed by the learner:** Does this match the plot? Am I blocking an exit or a
  push path? Will the next step reach this easily?

### Beat 3 — Prep the fixture (the critical-safety beat)
- **Objective:** Open the case and prep a fixture to hang — **proper clamp** on the
  pipe/truss, **safety cable (bond) attached — mandatory**, yoke tightened, cable
  dressed, **address/DMX set.**
- **Ambient:** This gear is about to go overhead; tools should be tethered; fixtures
  are heavy and pinchy.
- **Safe-failure consequence (the big one):** **Skip the safety cable** and it looks
  fine on the ground — but at Beat 4/5, if the clamp fails, the fixture **falls from
  trim.** The learner sees the catastrophic cost of the shortcut **safely**, with the
  lesson made explicit: the safety cable is the difference between a scare and a
  fatality. This is the lesson's spine — a deadly mistake taught without anyone hurt.
- **Assessed by the learner:** Is the clamp rated and fully seated? **Is the safety
  cable on?** Is the address right? Is anything going to swing free?

### Beat 4 — Fly it / send to trim
- **Objective:** The truss goes up on motors. **Running the motors is the rigger's
  job, not the ground hand's** — the lighting hand's job is to **clear the area,
  call/echo "HEADS!", keep everyone out from under the moving load, spot, and watch
  their cable feed** so nothing snags or pulls as it rises.
- **Ambient:** Head on a swivel — a load is moving overhead. This is where "never
  stand under a load" becomes visceral.
- **Safe-failure consequence:** Stand under the load, miss the "heads" call, or let a
  feeder cable snag → a dropped object, a fixture yanked loose, or a near-miss.
  Combined with a skipped Beat-3 safety cable, this is where the fixture falls.
- **Assessed by the learner:** Is anyone under this? Is my cable free to travel? Did
  the call go out? (Rigging boundary respected — this reinforces the positioning:
  ground hands support the fly; riggers rig.)

### Beat 5 — Trim & power on
- **Objective:** At trim, **power distribution basics** — land on the correct circuit,
  don't overload it, dress cable so there are **no trip hazards** (matted/taped in
  walkways), follow the **power-up sequence**, then **confirm the fixture answers its
  address** from the board.
- **Ambient:** Electrical safety; cable in walkways must be managed.
- **Safe-failure consequence:** Overload a circuit or make a bad connection → the
  breaker trips (potentially mid-show); a data/address error → the fixture is **dark
  when the LD calls for it.** Both shown safely, tied to "the show can't happen."
- **Assessed by the learner:** Is this circuit already loaded? Is the run a trip
  hazard? Does it respond when I test the address?

### End state
Fixture **floating at trim, powered, addressed, and answering the board.** The
learner has taken it the whole way — and, more importantly, has had to *judge the
safety of each step themselves,* seeing the safe cost of every shortcut.

---

## How this composes from atoms

| Beat | Atomic scene | Prototype status |
|------|--------------|------------------|
| 1 | Truck unload / case handling | partial (*Dock Sweep*) |
| 2 | Staging to the plot | not built |
| 3 | Clamp + **safety cable** + address | not built — **highest-value atom** |
| 4 | Clearing / spotting the fly to trim | not built |
| 5 | Circuit load + cable dress + power-up | not built |
| (related atom) | Over-under coiling | prototyped (*Coil Line*) |

**Build order recommendation:** Beat 3 (clamp + safety cable) first — it carries the
lesson's most important safe-failure consequence and is the clearest single-skill
scene. Prove the consequence model there, then build outward to the full arc.

## Guardrails carried in
- **US standard**, ground-up, **first-mover** (see doc 03, `DECISION_LOG.md`).
- **Rigging boundary respected:** the lighting hand supports the fly; running motors
  is a rigger's job. The lesson teaches the ground hand's real role, not rigging.
- **Not a certification.** Trains judgment, not credentials; a real call follows the
  lead and the employer's safety rules (doc 02).
