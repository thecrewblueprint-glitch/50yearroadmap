# Data Safety Policy

**Effective:** 2026-07-06  
**Scope:** All roadmap data committed to this repository and published to GitHub Pages

---

## Purpose

The Operations Command Center roadmap is **public** at: https://thecrewblueprint-glitch.github.io/50yearroadmap/

This policy ensures that only **business/project-safe** data is committed and displayed.

---

## What IS Allowed

✅ **Allowed in roadmap:**
- Project titles and purposes
- Status (active, completed, moved_later, blocked, etc.)
- Priority levels (critical, high, medium, low)
- Pillar mappings
- Evidence links to memory sources (file paths only)
- General descriptions of work/goals

**Examples:**
```
- "Deadhang website SSL/security implementation"
- "Crew Blueprint course content creation (83-lesson outline)"
- "Production Atlas deep research (festivals, vendors, logistics)"
```

---

## What IS NEVER Allowed

❌ **FORBIDDEN — will be caught by validation:**

| Category | Examples | Why |
|----------|----------|-----|
| **Contact Info** | Phone, email, mailing address, contact names | Personal privacy |
| **Financial** | Bank accounts, routing numbers, credit cards, pay rates, tax info | Security + privacy |
| **Health/Personal** | DOB, medical info, personal relationships, struggles | Privacy |
| **Work Details** | Specific jobsite names, crew members, client names | Confidentiality |
| **Travel/Hotels** | Hotel names, locations, trip details | Privacy + security |
| **Account Credentials** | API keys, passwords, tokens, secrets | Security |
| **Specific Names** | Aaron, Bowman, client names, employer names | Privacy |

**Examples of FORBIDDEN text:**
```
❌ "Contact (623) 280-3415 for work"
❌ "Tax filing due by 2026-08-15 (owed $2,500)"
❌ "Stay at Rodeway Inn Grand Rapids for festival runs"
❌ "Aaron's DOB: 01/26/1990"
❌ "Invoice to smith.enterprises@company.com"
```

---

## Validation Process

All roadmap files pass through **two gates** before commit:

### 1. Automated Validation (`validate-roadmap.py`)

Runs on every update. **MUST PASS** to proceed.

Checks:
- ✓ No phone numbers, emails, addresses
- ✓ No forbidden keywords (names, locations, account terms)
- ✓ No credit cards, SSNs, API keys
- ✓ Valid schema (status, priority, tracks)
- ✓ All references resolvable

**Run before commit:**
```bash
python scripts/validate-roadmap.py
```

Exit code `0` = safe, `1` = BLOCKED

### 2. Human Review (You)

Before pushing, **you** review:
- Are the project descriptions generic enough?
- Do titles avoid specific names/contacts?
- Are evidence links safe?
- Would this be OK if someone shared it publicly?

---

## Workflow

```
Memory Chunk
    ↓
Roadmap Watcher (roadmap-watcher.py)
    ↓ [extracts safe claims]
    ↓
watcher-proposals.json
    ↓
YOU REVIEW & DECIDE
    ↓ [approve/modify]
    ↓
data/roadmap/*.json
    ↓
validate-roadmap.py ← MUST PASS
    ↓
build-roadmap.py
    ↓
docs/roadmap.json (public dashboard)
```

---

## What to Do If Validation Fails

**Error:** `SENSITIVE DATA DETECTED`

```
ERROR: SENSITIVE DATA DETECTED in projects[0].title: person
  Value: "Invoice system for Aaron Bowman's 1099 work"
```

**Fix:**
1. Re-word without the name: `"Personal invoice generator app"`
2. Re-run validation
3. If it still fails, check the forbidden patterns list above

**Never commit if validation fails.** The GitHub Action will reject it.

---

## Memory Chunk Policy

The `memories/` folder is **not public** — those ZIP files stay local.

What CAN be referenced in roadmap:
- Memory file names (e.g., "festival-atlas-research-version")
- Summary descriptions (e.g., "6 research batches")
- General evidence categories (e.g., "context documented")

What CANNOT be referenced:
- Specific quotes from memories
- Person names from memory chunks
- Specific email/contact details

---

## For the Roadmap Watcher

The watcher (`roadmap-watcher.py`) is **designed to output public-safe data only**.

It:
- ✅ Extracts claims from memories
- ✅ Strips names, contacts, financial details
- ✅ Links to general evidence categories
- ✅ Maps work to pillars
- ✅ Flags blockers for decision

The watcher **never outputs** names, contacts, or sensitive context.

---

## Emergency Override

If you need to commit something that DOESN'T pass validation:

```bash
# DON'T USE THIS LIGHTLY
git commit --no-verify -m "OVERRIDE: reason"
```

This **will fail deployment** and is intentional — acts as a second gate at the GitHub Action level.

Instead:
1. Talk to the watcher or me about rewording
2. Move the sensitive task to a private `data/private/` folder
3. Reference it in the roadmap only by ID

---

## Questions?

If unsure, ask: **"Can this data be shared publicly without harm?"**

If the answer is no, it doesn't go in the roadmap.

---

**Last updated:** 2026-07-06
