# Decision Log

Durable strategic decisions and their reasoning. These are *decisions*, not
tasks — record them so they aren't re-litigated or accidentally reversed.
Newest first.

---

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
