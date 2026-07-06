---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Storing_lesson_plan_for_sequential_generation.md__chunk-0005",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Storing_lesson_plan_for_sequential_generation.md",
  "chunk_index": 5,
  "chunk_count_for_source": 13,
  "char_start": 45402,
  "char_end": 57391,
  "source_sha256": "508042ffaf5287d0ffc17ebad33731043412864dcc8f21a5e99b6532520959db",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

$$

Each leg carries about **71% of the load.** Common in production rigging. Requires confirmation that all components are rated for actual leg tension — not just load weight.

---

### 🔴 Critical Threshold — 120° Included Angle

$$\beta = 120° \quad \theta = 30° \quad T = W$$

Each leg carries **100% of the load.** This is the 120-degree rule limit. Any setup at or approaching this geometry requires a full rating check of every component, and serious consideration of whether the geometry can be improved.

---

### 🚫 Danger Zone — Beyond 120°

$$\beta > 120° \quad \theta < 30° \quad T > W$$

Each leg carries **more than the full load weight.** Without a qualified rigger review and engineered lift plan, this geometry should not proceed.

---

## Visual Way to Think About It

Picture the inverted V of a two-leg bridle:

- **Narrow V** = steep slings, small included angle, most tension works vertically = efficient
- **Wide V** = shallow slings, large included angle, most tension becomes horizontal force = dangerous

When the V opens to 120°, the legs are spread so flat that each one has only 50% vertical efficiency. Both legs together are just barely supporting the load — and each individual leg must equal the full load weight to do it.

When the V opens past 120°, the geometry is working *against* the lift. The slings are pulling more sideways than upward.

---

## Four Common Misunderstandings

**"Two slings split the load in half."**
Only true when both slings are perfectly vertical. At 120°, each leg carries the full load. At 150°, nearly double.

---

**"The included angle is the same as the sling angle."**
No. The included angle is measured *between* the two legs. The sling angle is measured from horizontal or vertical on a *single* leg. Confusing these produces incorrect calculations.

---

**"If the sling is rated for the load weight, the lift is safe."**
The sling must be rated for the **calculated leg tension** under the actual hitch type and angle — not the load weight on the weight ticket. At 120°, those two numbers are the same. At 150°, the leg tension is nearly double the load weight.

---

**"The crane capacity is the only rating that matters."**
The crane may be well within its capacity while a single shackle, lifting lug, or sling leg is overloaded. The weakest rated component controls the lift — regardless of what the crane chart says.

---

## Classroom Discussion Prompt

> *"A load weighs 1,000 lb. The rigging crew uses two sling legs at a 150° included angle. Each leg is rated for 1,500 lb. Is the lift safe?"*

Calculate first:

$$T = \frac{1000}{2\cos(75°)} = \frac{1000}{2(0.259)} = \frac{1000}{0.518} \approx 1{,}932 \text{ lb per leg}$$

Each leg is rated for 1,500 lb. The calculated tension is 1,932 lb. **The slings are overloaded by nearly 29%** — and the load still weighs exactly 1,000 lb.

The load didn't change. The angle made it unsafe.

---

## Lesson Summary

| Concept | Key Point |
|---|---|
| Included angle | The angle between two sling legs — not the same as sling angle from horizontal |
| Angle relationships | $\beta = 2\alpha$, $\theta = 90° - \beta/2$ |
| 120-degree rule | At 120° included angle, each leg tension = full load weight |
| Formula | $T = W \div (2\cos(\beta/2))$ |
| Beyond 120° | Each leg carries more than the total load — requires engineered review |
| Common error | Confusing load weight with leg tension when checking component ratings |

---

## Coming Up: Lesson 5

The math tells you what your slings and hardware are seeing. Lesson 5 covers how to verify that your hardware is actually fit to handle it — walking through a systematic inspection process for shackles, spansets, and master links before any production lift.

---

*Standards referenced: OSHA 29 CFR 1910.184, 29 CFR 1926.251; ASME B30.9, B30.26*

---

**[USER]**



---

**[ASSISTANT]**

# Lesson 5: Equipment and Hardware Inspection

---

## Lesson Overview

**Course:** Bridle Math & Angle Tension
**Lesson:** 5 of 9
**Duration:** 3–5 minutes
**Type:** Upskilling
**Audience:** Stagehands and riggers — festival and event production environments

---

## Learning Objectives

By the end of this lesson, learners will be able to:

- Identify required markings on shackles, synthetic roundslings, and master links
- Explain the difference between WLL, rated load, and calculated sling-leg tension
- Inspect shackles, spansets/synthetic roundslings, and master links against removal-from-service criteria
- Recognize conditions that require immediate removal from service
- Explain why component compatibility matters beyond individual ratings
- Connect inspection findings to the lift plan before the load leaves the ground

---

## The Central Principle

> **Inspection is part of the load calculation.**

The previous lessons showed how to calculate exactly what your slings and hardware are seeing. This lesson is about confirming that your hardware can actually handle it.

A mathematically correct lift plan means nothing if the shackle pin is bent, the sling tag is missing, or the master link is point-loaded on the hook tip. Inspection is not a bureaucratic step that happens before the real work. It *is* real work — and skipping it turns a well-planned lift into an uncontrolled one.

---

## Inspection Types: When and How Often

**Initial Inspection**
Before equipment is first placed into service. Verify the item matches its specification, has proper identification and markings, shows no shipping or storage damage, and has documentation where required.

**Pre-Use / Frequent Inspection**
Before each use. Usually visual and tactile. Check for obvious damage, deformation, missing tags, heat exposure, corrosion, cuts, and any condition that creates doubt.

> *Before the lift, inspect what will carry the force.*

**Periodic Inspection**
More formal. Performed by a designated or qualified person based on service severity, frequency of use, and environment. Documented according to OSHA requirements, ASME standards, employer policy, and manufacturer instructions. Minimum frequency follows the most restrictive applicable requirement.

---

## Shackles

Shackles are connection points throughout a bridle system — linking sling eyes to master links, connecting to lifting lugs, and transferring load between components. They are frequently subject to multi-directional forces and must be inspected accordingly.

### What to Check

**Markings**
The shackle must have legible manufacturer identification and WLL or rated load marking. If either is missing or unreadable, the shackle cannot be used — there is no way to verify its capacity.

**Pin Condition**
The pin must be the correct pin for that shackle body. Never substitute a bolt or unapproved replacement. Inspect for bent pins, worn or damaged threads, mushroomed heads, shoulder damage, corrosion, and incomplete engagement. A pin that does not seat fully can disengage under load.

**Body Deformation**
Spreading at the ears, bending, twisting, elongation, or any visible distortion indicates the shackle has been overloaded or side-loaded. Deformed shackles are removed from service.

**Wear**
Inspect the crown and pin contact surfaces. Wear reduces cross-sectional area, which directly reduces load capacity.

**Cracks, Nicks, and Gouges**
Cracks are an immediate removal condition. Deep gouges and sharp notches become stress risers — points where metal is more likely to fail under load.

**Heat Damage**
Weld spatter, arc strikes, discoloration, or evidence of unauthorized heating compromise the metallurgy of the shackle, reducing its strength in ways that are not visible from the surface.

**Corrosion**
Surface rust may be acceptable depending on severity. Pitting, heavy corrosion, or visible metal loss requires removal.

**Side Loading**
Most shackles are rated for in-line loading only. Side loading can reduce capacity significantly. Only use a shackle for side-loaded configurations if the manufacturer explicitly permits it and the appropriate capacity reduction is applied.

### Shackle Removal-from-Service Criteria

| Condition | Why It Matters |
|---|---|
| Missing or illegible markings | Capacity cannot be verified |
| Bent, twisted, stretched, or distorted body | Evidence of overload or misuse |
| Bent, damaged, or incorrect pin | Pin may fail or disengage |
| Damaged threads | Pin may not seat properly |
| Excessive wear | Reduces load-bearing cross-section |
| Cracks | Immediate failure risk |
| Severe corrosion or pitting | Reduces metal section |
| Weld spatter or arc strike | Metallurgical damage |
| Unauthorized modification | Original rating no longer valid |
| Any condition creating doubt | Evaluate before use |

---

## Synthetic Roundslings and Spansets

**A note on terminology:** *SpanSet* is a manufacturer name that has become widely used in the field as a generic term for synthetic roundslings, similar to how "Sharpie" refers to any permanent marker. In this course, the correct term is **synthetic roundsling** — but you will hear "spanset" on nearly every production floor.

A synthetic roundsling consists of load-bearing core yarns enclosed inside a protective outer cover. The cover's job is to protect the core. Damage to the cover is always taken seriously because it may indicate core damage that is not visible from the outside.

### What to Check

**Sling Tag**
The tag is the sling's identity. It identifies rated capacities for each hitch type, material, manufacturer, length, and other critical information. A missing or unreadable tag is an immediate removal condition — without it, you cannot verify the sling's capacity for the actual configuration you're using.

**Cuts, Tears, Holes, and Punctures**
Any breach of the cover that reaches or exposes the core is a removal condition. Snags and tears may also indicate internal fiber damage that is not visible.

**Abrasion**
Heavy abrasion wears down the cover and may damage the load-bearing core beneath it. Pay attention to areas that contact sharp truss edges, concrete, or rough steel.

**Heat Damage**
Melting, charring, glazing, hardened fibers, or burn marks indicate that the sling has been exposed to heat that may have weakened its synthetic fibers. This is a removal condition.

**Chemical Damage**
Discoloration, brittleness, softening, stiffening, or visible fiber breakdown may indicate chemical exposure. Acids and caustic materials can degrade synthetic fibers rapidly. OSHA 29 CFR 1910.184 specifically lists acid and caustic burns as a removal condition.

**UV Damage**
Fading, surface powdering, brittleness, or loss of flexibility can indicate ultraviolet degradation. Slings stored outdoors or in sunny environments for extended periods should be inspected carefully.

**Knots**
Synthetic slings must never be knotted. Knots create severe stress concentration and dramatically reduce rated capacity.

**Exposed Core Yarn**
For roundslings, exposed core yarn is a removal condition. The load-bearing fibers are no longer protected.

**Embedded Particles**
Metal chips, grit, glass, concrete, or abrasive debris embedded in the cover can cut internal fibers during loading — damage that is completely invisible from the outside.

**Edge Protection**
Where slings contact sharp edges, corners, or rough surfaces, edge protection must be used. A sling routed across a sharp truss plate without protection may fail at a tension well below its rated capacity.

### Synthetic Roundsling Removal-from-Service Criteria

| Condition | Why It Matters |
|---|---|
| Missing or illegible tag | Rated capacity cannot be verified |
| Acid or caustic burns | Chemical weakening of fibers |
| Melting, charring, or weld spatter | Fiber strength loss |
| Holes, tears, cuts, punctures, or snags | Possible core damage |
| Exposed load-bearing yarns | Sling integrity compromised |
| Excessive abrasive wear | Strength reduction |
| Knots | Severe strength reduction |
| Chemical damage | Fiber degradation |
