# Scene design — Lighting Hand: Truck to Trim

**Status:** Design target (owner-requested, 2026-07-22). Not built yet.
**Type:** Role-based, end-to-end workflow lesson (see `governance/DECISION_LOG.md`
— "lessons are role-based full workflows" + "safe failure with real consequences").
**Role:** Lighting hand (ground crew / electrician's helper), **US standard.**
**Arc:** Walk a lighting hand through the **whole** ground-up process — from
*fixtures on the truck* to a *rig built, wired, ground-checked, flown to trim,
landed on power, and focused where the LD wants it* — the point at which the show
can actually happen. (Every step it takes, in the order it takes them.)

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

> **This sequence is a draft for the owner's correction.** Order and terminology
> below are best-effort; the owner's field knowledge is the source of truth. Items
> flagged **⚠confirm** are ones to verify or rename. Add/reorder freely.

The full arc is a **ground-up flown lighting rig**: build the truss on the deck,
hang and wire the fixtures, ground-check them, fly to trim, then focus. Steps run
in order; each has **objective · ambient · safe-failure consequence · learner's
judgment call.**

### 1 — Unload from the truck
- **Objective:** Get truss and fixture cases off the truck safely — control the
  ramp/liftgate, push a rolling case from the **ends** not the sides, two-hand the
  heavy ones, mind the tail of the case.
- **Ambient:** Loaders and a forklift on the same truck; sloped ramp; tight staging.
- **Consequence:** A case gets away on the ramp → it tips, a fixture is damaged
  ($$), or it catches a foot.
- **Learner judges:** Is the ramp clear? One-person or two-person case? Who's behind me?
- **Atom:** case handling — partly prototyped in *Dock Sweep*.

### 2 — Roll & stage to the build position
- **Objective:** Move truss and cases to **where the rig gets built** (usually under
  where it will fly), laid out in **build order** per the LD's plot, clear of paths
  and egress.
- **Ambient:** Keep fire lanes and walkways clear; other departments share the floor.
- **Consequence:** Staged in the wrong place / blocking a path → you move it all
  again, the chief loses time, the fire marshal flags the lane.
- **Learner judges:** Does this match the plot? Am I under the fly point? Blocking an
  exit or a push path?

### 3 — Lay out & **pin the truss together**
- **Objective:** Lay truss sections end to end in the right order/orientation and
  **connect them** — seat the connectors and **pin each junction** (spigot/connector
  pins + **retaining clips / R-clips**, ⚠confirm your standard hardware), so the truss
  line is one solid, rated structure. Add corner blocks / bases as the plot needs.
- **Ambient:** Pinch points at every junction; heavy sections; partners lifting.
- **Consequence:** A junction left **unpinned or half-pinned** → the truss is not
  rated and can fail under load in the air; caught on the ground it's a two-second
  fix, missed it's catastrophic. A section built in the wrong order/orientation →
  the whole line comes apart to redo.
- **Learner judges:** Is **every** pin in and clipped? Right section, right way round?
  Fingers clear of the junction?

### 4 — Hang & safety the fixtures on the truss
- **Objective:** Clamp each fixture to the truss at its **plotted position**, with the
  **right clamp fully seated**, the **safety cable (bond) attached — mandatory**, yoke
  set, and the **address/DMX set.**
- **Ambient:** Working over the truss; tools tethered; heavy, pinchy fixtures.
- **Consequence (the spine):** **Skip the safety cable** — looks fine now, but if the
  clamp ever fails at trim the fixture **falls.** Taught **safely**; the safety cable
  is the difference between a scare and a fatality. Wrong position/address → it's in
  the wrong place in the light plot and has to be re-hung or re-addressed.
- **Learner judges:** Clamp rated and seated? **Safety cable on — every one?** Right
  position, right address?

### 5 — Run power & data; **plug the fixtures at their breakouts** ⚠confirm "bridges"
- **Objective:** Run the **power** (multicable / socapex fan-outs) and **data** (DMX)
  along the truss, and **plug each fixture into its breakout / distro point** on the
  truss (⚠the owner's term "**bridges**" — confirm whether this means the multicable
  **breakout**, an **opto-splitter**, or the truss **bridge** position). **Dress and
  tie** every run to the truss so nothing hangs, pulls, or fouls when it flies.
- **Ambient:** Live power soon; cable weight on the truss; data topology matters.
- **Consequence:** A fixture **not plugged / plugged to the wrong breakout** → it's
  dark or on the wrong circuit. Cable **left undressed** → it snags or drops on the
  fly. Data run wrong → a whole branch goes dark.
- **Learner judges:** Is every fixture on power **and** data? Is every run tied off?
  Right breakout for this fixture?

### 6 — **Ground-check it powered on** (before anything flies)
- **Objective:** **Power up and confirm the rig works at arm's reach** — each fixture
  **strikes / homes / answers its address** — because a dead fixture is trivial to fix
  on the deck and miserable at trim.
- **Ambient:** Live power on the deck; people around the truss.
- **Consequence:** **Fly it unchecked** and a no-strike / dead / mis-addressed fixture
  only shows **at trim** — now it comes **back down** (or a tech rides up), eating the
  whole load's time. Learner learns to **catch it on the deck.**
- **Learner judges:** Did every fixture power and respond **before** I called it ready
  to fly?

### 7 — Fly to trim (support the rigger; don't be the rigger)
- **Objective:** The truss goes up on motors. **Running motors is the rigger's job.**
  The lighting hand **clears the area, calls/echoes "HEADS!", keeps everyone out from
  under the moving load, spots, tends tag lines, and watches the power/data feed** so
  nothing snags or pulls as it rises.
- **Ambient:** Head on a swivel — a load is moving overhead. "Never stand under a
  load" made visceral.
- **Consequence:** Stand under it, miss the "heads" call, or let a feeder snag → a
  dropped object, a fixture yanked loose, a near-miss. With a skipped safety cable
  (step 4), this is where a fixture falls.
- **Learner judges:** Is anyone under this? Is my cable free to travel? Did the call
  go out? (Rigging boundary respected: ground hands support the fly; riggers rig.)

### 8 — Land power & data at trim; dress; re-confirm
- **Objective:** With the rig at trim, **land the truss circuits on the right
  power** without **overloading**, confirm the data feed, **dress walkway runs (mat /
  tape) so there are no trip hazards**, and **re-confirm the rig still answers** now
  that it's flown.
- **Ambient:** Electrical safety; cable in walkways; work still overhead nearby.
- **Consequence:** Overload a circuit / bad connection → breaker trips (maybe
  mid-show); a run across a walkway → trip hazard; a data cable knocked loose on the
  fly and **not** re-checked → dark on cue.
- **Learner judges:** Is this circuit already loaded? Is the run a trip hazard? Does
  it **still** respond now it's up?

### 9 — Focus: **move & adjust where the lighting tech / LD asks**
- **Objective:** During focus the LD/lighting tech calls fixtures and directions;
  the hand **pans/tilts, adjusts position, shutters/shapes, or nudges the fixture as
  directed** (⚠conventionals are focused by hand; movers are largely focused from the
  board — confirm how much hand-focus your target rigs use). **Listen, repeat back,
  do exactly what's asked**, confirm, move to the next.
- **Ambient:** Working at height / near the rig; taking direction precisely; other
  hands on other fixtures.
- **Consequence:** Mis-hear or guess instead of confirming → the wrong fixture moves,
  the LD loses time, the look is wrong. This is where **listening** (the ambient
  skill) becomes the whole task.
- **Learner judges:** Did I hear the exact fixture and direction? Did I repeat it
  back? Is it doing what they actually asked?

### End state
The rig is **built, wired, ground-checked, flown to trim, landed on power, dressed,
and focused** — powered on and answering the board, exactly where the LD wants it.
**The show can happen.** The learner took it the whole way and, at every step, had to
**judge the safety and readiness themselves** — seeing the safe cost of every shortcut.

---

## How this composes from atoms

| Step | Atomic scene | Prototype status |
|------|--------------|------------------|
| 1 | Truck unload / case handling | partial (*Dock Sweep*) |
| 2 | Roll & stage to the build position | not built |
| 3 | **Pin the truss together** | not built |
| 4 | Clamp + **safety cable** + address the fixture | not built — **highest-value atom** |
| 5 | Run power/data + **plug at breakouts** + dress | not built |
| 6 | **Ground-check powered on** | not built |
| 7 | Support the fly to trim (clear/spot/call) | not built |
| 8 | Land circuit + data + dress + re-confirm | not built |
| 9 | **Focus** — adjust where the LD asks (listening) | not built |
| (related atom) | Over-under coiling | prototyped (*Coil Line*) |

**Build order recommendation:** Build **step 4 (clamp + safety cable + address)**
first — it carries the lesson's most important safe-failure consequence (a fixture
that falls) and is the clearest single-skill scene. Then **step 3 (pinning the
truss)** — the other structural "did you actually secure it?" beat. Prove the
consequence model on those two, then build outward to the full arc.

## Guardrails carried in
- **US standard**, ground-up, **first-mover** (see doc 03, `DECISION_LOG.md`).
- **Rigging boundary respected:** the lighting hand supports the fly; running motors
  is a rigger's job. The lesson teaches the ground hand's real role, not rigging.
- **Not a certification.** Trains judgment, not credentials; a real call follows the
  lead and the employer's safety rules (doc 02).
