# 04 — Governance

**Status:** Documented.

Governance is what lets multiple AI collaborators (and the owner) work on this
repo without stepping on each other or leaking sensitive data. It is the rules,
the log, and the safety controls.

## The collaboration standard

- **`AGENTS.md`** — the operating law. Key rules: **commit to `main`, never
  branch** (single-trunk — the cause of a past stranded-work incident); the data
  model; integrity rules; and the start/work/finish checklist. Any agent reads
  this first.
- **`CHANGELOG.md`** — the shared work/decision log (newest first) plus an "open
  threads" section. Every working session records what changed and why, so the
  next collaborator picks up with full context.
- **`CHATGPT_HANDOFF.md`** — the standing AI-onboarding handoff (summary of the
  law).

## The governance folder

`governance/` holds the durable decision layer:

- **`CURRENT_STATE.md`** — plain-language snapshot of where things stand.
- **`DECISION_LOG.md`** — durable strategic decisions (structure, tax, direction)
  with reasoning, so they aren't re-litigated.
- **`OPEN_DECISIONS.md`** — decisions still open (e.g. OD-5 database migration).
- **`KNOWN_RISKS.md`**, **`LESSONS_LEARNED.md`** — risk and learning registers.
- **`STAGE_*_SCOPE.md`** — the staged documentation plan (see below).
- **`handoffs/`** — dated AI/human context transfers.
- **`AUDIT_2026-07-18.md`** — the repository audit.

## Public-safety model

The repo is **public**, so nothing private may be committed:

- **`DATA_SAFETY_POLICY.md`** — the policy (no PII, financials, private contacts,
  raw exports).
- **`data/schema/roadmap-public-safety.json`** — forbidden-pattern rules.
- **The validator's PII scan** (doc 03) — enforces it automatically:
  email/phone/SSN/card/street-address/HTML are hard errors.
- Principle 3/4: raw memory and deep context are **evidence, not public output**.

## The Stage model (documentation build-out)

The repo evolves in stages, each scoped in `governance/STAGE_*_SCOPE.md`:

- **Stage 0** — stabilization & governance (roadmap synced to reality, governance
  framework established). ✅ complete.
- **Stages 1–5** — canonical documentation, one company per stage: Deadhang
  Labor, The Crew Blueprint, Production Atlas, Contractor Tools, and Personal
  Operations (this system). ✅ all built (see each `companies/<company>/`).

## Why this matters

Governance is the difference between a pile of files and a **durable,
collaborative knowledge system.** It is what makes the repo safe to hand to
another AI — or to future-you — and trust that the rules will hold.
