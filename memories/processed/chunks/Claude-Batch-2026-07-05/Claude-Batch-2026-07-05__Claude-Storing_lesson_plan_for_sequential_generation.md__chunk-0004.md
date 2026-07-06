---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Storing_lesson_plan_for_sequential_generation.md__chunk-0004",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Storing_lesson_plan_for_sequential_generation.md",
  "chunk_index": 4,
  "chunk_count_for_source": 13,
  "char_start": 34049,
  "char_end": 46002,
  "source_sha256": "508042ffaf5287d0ffc17ebad33731043412864dcc8f21a5e99b6532520959db",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---



$$2T\sin(\theta) = W$$

Solving for sling tension:

$$T = \frac{W}{2\sin(\theta)}$$

The sling has to work harder and harder as the angle drops — not because the load got heavier, but because a shrinking share of each leg's tension is actually lifting anything.

---

## Why Sine Is the Key Number

The sine value tells you exactly how efficient each sling leg is as a lifting force.

| Sling Angle (from horizontal) | Sine Value | Lifting Efficiency |
|---|---|---|
| 90° | 1.000 | 100% — all tension lifts |
| 60° | 0.866 | 86.6% lifts |
| 45° | 0.707 | 70.7% lifts |
| 30° | 0.500 | 50% lifts |
| 20° | 0.342 | 34.2% lifts |
| 10° | 0.174 | 17.4% lifts |

At 10°, only **17 cents on the dollar** of sling tension is doing useful lifting work. The sling must pull nearly six times as hard to hold the same load.

---

## Why Cosine Makes It Worse

The horizontal force component — driven by cosine — grows as the sling flattens. That sideways force doesn't disappear. It goes directly into the structure:

$$H = T\cos(\theta)$$

| Sling Angle (from horizontal) | Cosine Value | Effect |
|---|---|---|
| 90° | 0.000 | No horizontal force |
| 60° | 0.500 | Moderate spreading force |
| 45° | 0.707 | Significant spreading force |
| 30° | 0.866 | High horizontal force |
| 20° | 0.940 | Very high horizontal force |
| 10° | 0.985 | Extreme — nearly all tension is sideways |

At shallow angles, the bridle stops behaving like a lifting system and starts behaving like a **sideways compression system.** Lift points get pulled inward, hooks get side-loaded, thin structures get bent, and loads can be crushed by the inward squeeze.

---

## The Full Force Picture: 1,000 lb Load

For a 1,000 lb load on a two-leg bridle — $T = 1000 \div (2\sin\theta)$:

| Sling Angle | Tension Per Leg | Vertical Component Per Leg | Horizontal Component Per Leg |
|---|---|---|---|
| 90° | 500 lb | 500 lb | 0 lb |
| 75° | 518 lb | 500 lb | 134 lb |
| 60° | 577 lb | 500 lb | 289 lb |
| 45° | 707 lb | 500 lb | 500 lb |
| 30° | 1,000 lb | 500 lb | 866 lb |
| 20° | 1,462 lb | 500 lb | 1,374 lb |
| 15° | 1,932 lb | 500 lb | 1,866 lb |
| 10° | 2,879 lb | 500 lb | 2,836 lb |

Notice that the **vertical component per leg never changes** — it stays at 500 lb because two legs always share a 1,000 lb load. What changes is the total sling tension required to *generate* that 500 lb of vertical support. Everything above 500 lb is the angle penalty — and it goes entirely into sideways force.

---

## Scaled Up: 5,000 lb Load

When the load weight scales up, the consequences of shallow angles scale with it:

| Sling Angle | Tension Per Leg | Horizontal Force Per Leg |
|---|---|---|
| 90° | 2,500 lb | 0 lb |
| 60° | 2,887 lb | 1,443 lb |
| 45° | 3,536 lb | 2,500 lb |
| 30° | 5,000 lb | 4,330 lb |
| 20° | 7,310 lb | 6,869 lb |
| 10° | 14,397 lb | 14,179 lb |

At 10°, each sling leg is seeing nearly **three times the full load's half-share.** That's the difference between a sling safely within its Working Load Limit and one that's catastrophically overloaded — on the same lift, with the same gear, just a different angle.

---

## The Load Angle Factor Table

A quick-reference method that packages the same math:

$$T = \left(\frac{W}{2}\right) \times \text{LAF}$$

$$\text{LAF} = \frac{1}{\sin(\theta)}$$

| Angle from Horizontal | Load Angle Factor | Practical Meaning |
|---|---|---|
| 90° | 1.000 | No penalty |
| 75° | 1.035 | Negligible increase |
| 60° | 1.155 | +15.5% per leg |
| 45° | 1.414 | +41.4% per leg |
| 30° | 2.000 | Double — each leg = full load |
| 20° | 2.924 | Nearly triple |
| 15° | 3.864 | Nearly quadruple |
| 10° | 5.759 | Nearly six times |

Use this table in the field when you need a fast multiplier. It doesn't replace calculating — it confirms your calculation and flags when something needs a second look.

---

## The Danger Zone

A practical field framework used across rigging programs:

| Angle Range | Status |
|---|---|
| 60° and above | Preferred operating range |
| 45°–59° | Acceptable — verify all ratings |
| 30°–44° | Serious caution — recalculate, recheck every component |
| Below 30° | Danger zone — requires qualified rigger review or engineered lift plan |

**Why 30° is the hard marker:**

$$\sin(30°) = 0.5$$

$$T = \frac{W}{2(0.5)} = W$$

At 30°, each sling leg carries the full load weight. Below 30°, each leg carries *more* than the total load weight. This is not a gray area — it's a mathematical threshold that demands a higher level of review.

---

## Worked Problem: 3,000 lb Load at 20°

A 3,000 lb load. Two-leg bridle. Sling angle: 20° from horizontal.

**Sling tension per leg:**

$$T = \frac{3000}{2\sin(20°)} = \frac{3000}{2(0.342)} = \frac{3000}{0.684} \approx 4{,}386 \text{ lb per leg}$$

**Horizontal force per leg:**

$$H = T\cos(20°) = 4386 \times 0.940 \approx 4{,}123 \text{ lb per leg}$$

A 3,000 lb load is creating **4,386 lb of sling tension** and **4,123 lb of horizontal spreading force** on each leg. Every component in the system — sling, shackle, hook, lug, anchor — must handle that full tension. The 3,000 lb load weight is almost irrelevant to the hardware rating question.

---

## The Plain-Language Version

> Think of each sling leg as doing two jobs. One part of the force lifts upward. One part pulls sideways. The vertical part is what supports the load. At a steep angle, most of the sling tension is useful lift. At a shallow angle, only a small fraction of the sling tension lifts the load — so the sling must pull much harder to create the same upward support. That extra force goes into the sling, shackles, hooks, lift points, and the load itself.

That's the whole lesson. The math just tells you exactly *how much* harder.

---

## Lesson Summary

| Concept | Key Point |
|---|---|
| Vertical component | $T\sin\theta$ — the share of sling tension actually lifting the load |
| Horizontal component | $T\cos\theta$ — spreading force that stresses structure, hardware, and pick points |
| Core formula | $T = W \div (2\sin\theta)$ — tension per leg in a balanced two-leg bridle |
| Sine and efficiency | Lower angle = lower sine = less lifting efficiency = higher required tension |
| 30° threshold | Each sling leg carries the full load weight — mandatory review below this point |
| Load angle factor | Quick multiplier: $\text{LAF} = 1 \div \sin\theta$ |

---

## Coming Up: Lesson 4

Next lesson focuses on the **120-degree rule** — the geometry behind the most commonly cited angle limit in production rigging — and walks through direct comparisons between vertical and bridle configurations to show exactly when each is appropriate.

---

*Standards referenced: OSHA 29 CFR 1910.184, 29 CFR 1926.251; ASME B30.9, B30.26*

---

**[USER]**



---

**[ASSISTANT]**

# Lesson 4: The 120-Degree Rule and Rigging Comparisons

---

## Lesson Overview

**Course:** Bridle Math & Angle Tension
**Lesson:** 4 of 9
**Duration:** 3–5 minutes
**Type:** Upskilling
**Audience:** Stagehands and riggers — festival and event production environments

---

## Learning Objectives

By the end of this lesson, learners will be able to:

- Define the included angle and explain how it relates to sling angle from horizontal and vertical
- State the 120-degree rule and explain why that threshold matters
- Derive why each sling leg equals the full load weight at a 120° included angle
- Compare tension across included angle configurations for a given load
- Identify common misunderstandings about sling ratings and load sharing
- Apply the 120-degree rule as a practical field warning in production rigging

---

## What Is the 120-Degree Rule?

The 120-degree rule is the most widely cited angle warning in rigging. It states:

> **When the included angle between two sling legs reaches 120°, each sling leg carries tension equal to the full load weight.**

Beyond 120°, each leg carries *more* than the total load weight — a condition that can overload slings, shackles, hooks, master links, and structural attachment points while the load itself appears stable and nothing looks obviously wrong from the ground.

It's a trig fact translated into a field-usable warning.

---

## The Geometry: Three Angles, One Shape

A two-leg bridle creates an inverted V. That shape can be described three ways, and all three are the same geometry:

| Measurement | Symbol | Description |
|---|---|---|
| Included angle between legs | $\beta$ | The angle *between* the two sling legs |
| Sling angle from vertical | $\alpha$ | Each leg's angle measured from straight down |
| Sling angle from horizontal | $\theta$ | Each leg's angle measured from flat |

They are related by:

$$\beta = 2\alpha \qquad \theta = 90° - \alpha \qquad \theta = 90° - \frac{\beta}{2}$$

So when the included angle is 120°:

$$\alpha = 60° \qquad \theta = 30°$$

**A 120° included angle is the same geometry as a 30° sling angle from horizontal.** Different numbers, same lift. This is why Lessons 3 and 4 connect directly — the 30° danger threshold and the 120-degree rule are describing the same critical point from different reference frames.

---

## Why 120° Is the Breaking Point

Start with the balanced two-leg bridle formula. Using included angle $\beta$:

$$T = \frac{W}{2\cos\left(\frac{\beta}{2}\right)}$$

Plug in 120°:

$$T = \frac{W}{2\cos(60°)} = \frac{W}{2(0.5)} = \frac{W}{1} = W$$

Each sling leg tension equals the full load weight — derived directly from the math, no estimation involved.

For a **5,000 lb load** at a 120° included angle:

$$T = 5{,}000 \text{ lb per leg}$$

$$\text{Combined sling-leg tension} = 10{,}000 \text{ lb}$$

The system contains **twice the load weight** in total sling tension, distributed equally across two legs — each of which must be rated accordingly, along with every shackle, hook, master link, and attachment point in the system.

---

## Tension Across the Full Angle Range

For a **1,000 lb load**, two-leg balanced bridle:

| Included Angle | Sling Angle (from horiz.) | Tension Per Leg | Tension as % of Load |
|---|---|---|---|
| 0° | 90° | 500 lb | 50% |
| 30° | 75° | 518 lb | 52% |
| 60° | 60° | 577 lb | 58% |
| 90° | 45° | 707 lb | 71% |
| **120°** | **30°** | **1,000 lb** | **100%** |
| 140° | 20° | 1,462 lb | 146% |
| 150° | 15° | 1,932 lb | 193% |
| 160° | 10° | 2,879 lb | 288% |

Notice the curve: tension climbs gradually from 0° to 90°, then accelerates sharply. By 150°, each leg carries nearly **twice the load.** By 160°, nearly **three times.**

For a **5,000 lb load**:

| Included Angle | Tension Per Leg | Combined System Tension |
|---|---|---|
| 60° | 2,887 lb | 5,774 lb |
| 90° | 3,536 lb | 7,071 lb |
| **120°** | **5,000 lb** | **10,000 lb** |
| 140° | 7,310 lb | 14,619 lb |
| 150° | 9,659 lb | 19,319 lb |
| 160° | 14,397 lb | 28,794 lb |

At 160°, a 5,000 lb load is producing over **28,000 lb** of combined sling-leg tension in the system.

---

## Four Geometry Benchmarks

Use these as practical reference points when evaluating any bridle setup:

---

### ✅ Preferred — 60° Included Angle

$$\beta = 60° \quad \theta = 60° \quad T \approx 0.577W$$

Each leg carries about **58% of the load.** Steep slings, high vertical efficiency, low horizontal force. This is the comfortable operating range.

---

### ⚠️ Acceptable with Checks — 90° Included Angle

$$\beta = 90° \quad \theta = 45° \quad T \approx 0.707W$$

Each leg carries about **71% of the load.** Common in production rigging. Requires confirmation that all components are rated for actual leg tension — not just load weight.

---

### 🔴 Critical Threshold — 120° Included Angle

$$\beta = 120° \quad \theta = 30° \quad T = W$$

Each leg carries **100% of the load.** This is the 120-degree rule limit. Any setup at or approaching this geometry requires a full rating check of every component, and serious consideration of whether the geometry can be improved.

---

### 🚫 Danger Zone — Beyond 120°

$$\beta > 120° \quad \theta < 30° \quad T > W$$

