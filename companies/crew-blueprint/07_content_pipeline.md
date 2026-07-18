# 07 — Content Pipeline (Multi-AI Workflow)

**Status:** Documented. This is one of the most mature parts of the project — the
workflow is **approved and repeatable.**

The core insight: **don't make one AI do everything.** Each AI system has a
defined role — research, organization, writing, QA, packaging — and the course
moves through them in a fixed order. The output is a canonical packet that
becomes the single source of truth.

## The approved workflow

1. **Topic selection** — choose the course/topic.
2. **Course planning** — define scope, objectives, and structure (against the
   standardized architecture in doc 03).
3. **NotebookLM research prompts** — structured research to gather and ground the
   material.
4. **Claude lesson drafting** — write the lessons from the research and plan.
5. **Manus QA / review** — quality-assurance and review pass.
6. **Final DOCX course packet generation** — assemble the reviewed content into
   the canonical course packet.
7. **Archive as the canonical source** — the packet is stored as the single
   source of truth.

## Roles by system (responsibility split)

- **Research** — NotebookLM (structured research prompts).
- **Organization** — course planning against the standard architecture.
- **Writing** — Claude (lesson drafting).
- **QA** — Manus (review pass; e.g. a scored quality gate before a packet is
  considered publication-ready).
- **Final packaging** — DOCX course-packet generation and archival.

Defining these responsibilities clearly — instead of trying to make one tool do
research *and* writing *and* review — is treated as a major accomplishment of the
project.

## Direction of truth

- The **course packet is the single source of truth.**
- **Website and platform content are generated from the packets — not the other
  way around.** Downstream surfaces (the site, the future LMS) present the packet;
  they never become an independent source that the packet has to chase.

## Where packets live

Canonical packets are archived in the private content repository. This public
documentation describes the **workflow and catalog** (doc 03), not the full
packet contents.
