# Lessons Learned

Hard-won lessons from building this repository, so we don't repeat them. Each is
a short "what happened → what we do now." Newest first.

## Branching stranded real work
A whole watcher pipeline + digests were built on a side branch and never merged
while `main` evolved past its data model. → **Commit directly to `main`, no
branching** (`AGENTS.md` §0). Single-trunk keeps collaborators in sync.

## Two sources of truth drift apart
The 30/60/90 layer shipped as a `ninety.js` sidecar holding its own data while
`roadmap.json` had none, so a dead renderer and a sidecar both fought over the
same box. → **One source of truth (`roadmap.json`), one renderer.** Fold
prototypes into the canonical model quickly.

## Serving location matters
The site served from the repo **root**, but edits went into a `docs/` copy, so
changes didn't show up. → Root is the served product; there is exactly one copy.

## Sensitive reports need sanitizing before they're committed
A public repo means income, bank details, PII, and secrets must be redacted
before storage; the unredacted version stays private. → Sanitize first, verify
with a PII scan, keep the original out of the repo.

## Don't dump the backlog into the roadmap
Promoting all watcher proposals at once made the dashboard dense and lost focus.
→ Promote deliberately; keep the roadmap lean; use the prioritizer as the queue.

## Title-only dedup misses reworded items
The watcher's title dedup didn't recognize a promotion that had been reworded,
so it re-surfaced "done" work. → Added a token-containment check in the
prioritizer to hide already-covered candidates.

## Validate before you commit
Reference breaks and enum/PII slips are easy to introduce by hand. → Run
`scripts/validate-roadmap.py` on every `roadmap.json` change; it gates the commit.

## The owner is the executive
Agents move faster by making technical/UX calls directly, but direction
(what's on the roadmap, what to focus on, entity/tax choices) is the owner's. →
Confirm on directional changes; act on clearly-delegated execution.

## Reality drifts from the roadmap
Work gets done in the field faster than the roadmap records it (website, invoice
system, courses, taxes). → Sync the roadmap to reality regularly; a stale
roadmap erodes trust in the whole system.
