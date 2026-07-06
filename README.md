# Operations Command Center

A repo-backed, AI-assisted roadmap, memory, evidence, and project-state system.

## Dashboard
View the GitHub Pages dashboard here:

https://thecrewblueprint-glitch.github.io/50yearroadmap/

## Purpose
Organize businesses, apps, goals, daily reports, completed work, future plans, and long-term vision into one interactive visual command center.

## Core Principles
1. **Chaos goes in. Auditable roadmap structure comes out.**
2. **Flexible detours without destroying linear progression.**
3. **Always answer: "What is the next thing I should probably focus on?"**

## Structure
- `/data/raw-reports`: Unmodified daily reports (Never overwritten)
- `/data/extracted`: Claims extracted from reports (Evidence layer)
- `/data/roadmap`: Approved state (Vision, Pillars, Projects, Tasks)
- `/docs`: GitHub Pages dashboard (Visual layer)
- `/scripts`: Validation and build tools
- `/schema`: Data validation rules

## How to Use
1. Paste daily AI reports into `/data/raw-reports`.
2. Run the ingestion agent (or manual update) to extract claims.
3. Validate changes in `/data/roadmap`.
4. Run `python scripts/build-roadmap.py` to compile `/docs/roadmap.json`.
5. View the dashboard at `https://thecrewblueprint-glitch.github.io/50yearroadmap/`.

## Agent Rules
See `AGENTS.md` for strict rules on how AI agents must interact with this repo.
