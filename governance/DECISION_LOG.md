# Decision Log

Durable strategic decisions and their reasoning. These are *decisions*, not
tasks — record them so they aren't re-litigated or accidentally reversed.
Newest first.

---

## 2026-07-22 — Homestead: don't build it — keep a light care seed
**Decision:** The physical **Homestead build is retired**, and **land acquisition
is off the table.** The abundance of existing US van-life resources (The Dyrt,
Harvest Hosts, Escapees, Workamper, free campsites) already solves lodging &
travel for the caravan at scale, for free or cheap — there is **no need to build
a framework, buy land, or run a business.** What remains is a **light care seed
(Homes for Hands):** (1) a curated "live & travel free" resource guide pointing
the caravan at what already exists, and (2) a mutual-aid / ally ethos for crew who
need help (Roadie Clinic / Backline style). Care and information, **not capital.**
The `land-acquisition` branch is retired; the `homestead` branch is reframed as
the care seed; the north star, end goal, Phase 2, and the final journey milestone
are reframed away from "acquire land + build a home base."
**Why:** Applying the ecosystem's own discipline (don't build what you can use;
rent the infrastructure; stay demand-pulled) to the plan's most capital-intensive
branch. The logistics problem the Homestead was meant to solve is already solved
by others at scale; rebuilding it would cost years and serious capital for no
added value. The part existing resources *don't* cover — care for the crew member
with nothing — is preserved in the effortless care seed, which is also the part
closest to the owner's stated purpose ("for others, out of love").

## 2026-07-21 — Crew Blueprint positioning: US-standard, ground-up, first-mover
**Decision:** The Crew Blueprint is built to **US industry standards** and taught
**ground-up** — starting with **field-hand / ground-crew fundamentals** (general
labor, load-in/out, gear handling, jobsite safety & professionalism), the owner's
**real lived expertise**. Specialized disciplines and **rigging come much later**;
rigging is the owner's *personal* goal, **not** the platform's foundation
(corrects earlier "lead with rigging" guidance). The aim is to be the **first
US-standard gamified training** for the trade.
**Why:** (1) **Authenticity/credibility** — teach from where the owner actually
has depth (ground work), not rigging he's still learning. (2) **Market** — the one
close analog, **Tech Crew HQ, is Australia-only** (Australian standards); the
American-standard version doesn't exist, so building it is genuine first-mover
whitespace. (3) **Reach + speed** — ground/field hands are the biggest audience
and the easiest content to gamify first, so the MVP ships faster. Updated
`cb-4`/`cb-5`, the crew-blueprint branch, docs 00/01/03, and
`partnerships/research/01`.

## 2026-07-18 — Partnerships: build first, partner later
**Decision:** The owner will **build more of the ecosystem himself before
approaching partners.** Partnership *research and leads* are captured (the
`partnerships/` playbook + `partnerships/research/`, and the cross-company
`data/roadmap/connections.md` registry), but **active outreach is deliberately
deferred** — the leads are future considerations, not a to-do now. Exception:
The Roadie Clinic (already contacted). Reflected in the roadmap by setting the
partnership-lead items to `moved_later` (`dh-13`, `cb-6`, `pa-4`; Homestead
`hs-4` continues at a slow pace).
**Why:** The owner wants a stronger, more-built foundation to show before
bringing his ideas "to the eyes of those I am seeking help from" — better
leverage, a more credible offer, and less risk of pitching before there's
something compelling to point to. Capture the map now; walk it later.

## 2026-07-18 — Crew Blueprint delivery: gamified static, not an LMS
**Decision:** The Crew Blueprint's delivery is a **gamified, static, browser-based
experience — not a traditional LMS.** The discipline/pathway map (`cb-2`) becomes a
**skill tree**; learner progress is stored **client-side (localStorage)**, so there
are **no accounts, database, or backend.** Mechanics start **highly simplified**
(XP, streaks, progress, one interaction per node) and grow later. Course DOCX
packets remain the content source of truth; gamified modules wrap them. First
step: one MVP module from an existing packet (`cb-5`). Resolves **OD-4** and
reframes `cb-3` (was "next-generation platform/LMS").
**Why:** A static, client-side gamified experience is *simpler* than an LMS and
**sidesteps the exact platform instability that blocked the LMS** (accounts +
DB + backend). It also fits the Blueprint's existing model better — the pathway
map is already a skill tree, and XP/badges reward *skill* without implying
certification (consistent with the no-cert stance). Simplify the mechanics first;
add depth once the format is proven.

## 2026-07-17 — Business structure: remain an Arizona single-member LLC
**Decision:** Deadhang Labor LLC remains an **Arizona LLC**, single-member,
**Schedule C**, **cash basis**, owner-operated, live-event production labor.
**Do not** drift business assumptions toward Wisconsin or any other state.
**Why:** Correcting a drift noticed in earlier planning. The AZ structure is the
established, correct basis for all roadmap and documentation work.

## 2026-07-17 — Tax: do not elect S-Corporation yet
**Decision:** Keep the current structure (AZ LLC / Schedule C / cash basis). Do
**not** elect S-Corp at this time. Continue *evaluating* (not yet acting on):
retirement planning, Section 179, bonus depreciation, estimated taxes, and a
future payroll transition.
**Why:** S-Corp election isn't justified at the current scale; these items are
strategic options to revisit as revenue and structure evolve — documented as
decisions/considerations, not active tasks.

## 2026-07-17 — Insurance: deferred, not forgotten
**Decision:** Business insurance is **deferred until the business reaches the
appropriate scaling stage**. Tracked as work item `dh-9` with status
`moved_later` — visible but off the active path. Do **not** mark it complete;
do **not** drop it.
**Why:** Not needed at the current solo-operator stage, but must remain on the
radar for when team deployment / scaling begins.

## 2026-07-17 — Print-on-demand operates under Deadhang Labor LLC
**Decision:** The print-on-demand clothing line runs **under Deadhang Labor
LLC** as an additional revenue stream. **No new LLC.** Tracked as `dh-12`.
**Why:** Keep entity structure simple; it's a revenue stream, not a separate
business requiring its own formation and tax treatment.

## 2026-07-17 — Repository is the single source of truth (Stage 0 first)
**Decision:** Evolve the repo from a roadmap into an operational knowledge
system, governance-first. Complete **Stage 0** (stabilize + synchronize +
govern) before further project development. Continue committing directly to
`main`; validate `roadmap.json` on every change.
**Why:** Without governance, future work accumulates technical and
organizational debt. Governance is the foundation for everything after.

## 2026-07-17 — DH-1 (business structure audit) is ~90% complete
**Decision:** Do not mark `dh-1` complete yet; treat it as ~90% (`in_progress`).
Remaining gates: insurance (deferred), independent-contractor framework, safety
documentation. Everything else in the business audit is effectively complete.
**Why:** Accurately represents reality — the structural foundation is nearly
done but a few named items remain.
