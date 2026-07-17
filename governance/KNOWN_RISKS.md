# Known Risks

Risks to the businesses and to this repository, with how each is currently
mitigated. Review periodically; raise the likelihood/impact when something
changes. Newest/most-active first.

| # | Risk | Impact | Mitigation / status |
| --- | --- | --- | --- |
| R-1 | **Sensitive data in a public repo** — reports/digests can carry income, bank, PII, secrets. | High | `DATA_SAFETY_POLICY.md` + `scripts/validate-roadmap.py` PII scan + manual sanitization before commit (July report was stored redacted; full version kept private). Ongoing discipline required. |
| R-2 | **Tax closeout incomplete** — returns filed (self-prepared) but may need amendment; balance owed unconfirmed. | High | Tracked as `dh-8` (in progress). Confirm balance, amend if needed, pay or set a plan. See tax notes. |
| R-3 | **Single-operator bandwidth** — many parallel projects; risk of half-built sprawl and lost sequence. | Med-High | Linear roadmap + `moved_later` status + 30/60/90 windows + proposal prioritizer keep work sequenced and deferrals visible. |
| R-4 | **Insurance deferred while operating** — a gap if an incident or scaling happens before coverage. | Medium | Explicit, tracked decision (`dh-9`, `moved_later`); revisit at the scaling stage, not forgotten. |
| R-5 | **Crew Blueprint platform instability** — blocks deploying finished course content. | Medium | Content-first approach; static course-preview workflow as an interim path (see OD-4). |
| R-6 | **Publishing unverified research** (Production/Festival Atlas) as if confirmed. | Medium | Public-safe rule + "Unknown publicly. Human verification needed." labels; verification pipeline planned. |
| R-7 | **Over-building before validation** (e.g. Laravel backend, enterprise invoice features). | Medium | MVP-first discipline; scope-down work items; watcher/prioritizer favor near-term. |
| R-8 | **Multi-AI drift / stranded work** — happened once (watcher stranded on a side branch). | Medium | Commit-to-`main`, no branching (`AGENTS.md` §0); handoffs stored in `/governance/handoffs/`. |
| R-9 | **AI inaccuracy** — an agent records something as done/confirmed that isn't. | Medium | Validator gate + human-in-the-loop promotion + owner-as-executive on direction. |
| R-10 | **Secret / credential exposure** — API tokens referenced in work (e.g. print automation). | High if leaked | Never commit secret *values*; use platform secret stores; scrub secret names from digests. |

_This is a living register. When a risk is retired, note it here before removing._
