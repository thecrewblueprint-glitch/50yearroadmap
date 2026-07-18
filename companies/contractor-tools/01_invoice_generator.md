# 01 — Invoice Generator

**Status:** Documented (built — production-ready; scoped to MVP, roadmap `ct-2`
completed).

## What it is

A production-ready **1099 invoice generator** — a single-file HTML tool that
produces professional, branded invoices with PDF output. It is deliberately
**narrow**: a focused invoicing tool, not an accounting suite.

## Features

- **Professional invoice generation** with PDF output and direct download.
- **Multiple payment terms** — Net 15 / Net 30 / Net 45 / Net 60 / Due on Receipt.
- **Branded output** consistent with Deadhang's identity (see
  `companies/deadhang-labor/08_brand.md`).
- Built for the **1099 / independent-contractor** use case.

## Architecture (deterministic and narrow)

The invoice pipeline is intentionally simple and deterministic:

1. **Conversational text input** — paste job/line-item text.
2. **Parser** — a PHP / OpenRouter parser turns the text into **validated JSON**.
3. **Editable review** — the parsed data is shown for human review/correction
   before anything is calculated.
4. **Deterministic calculations** — totals are computed by code, **never by the
   AI**.
5. **Fixed invoice preview → PDF → direct download.**

## What it deliberately avoids

To keep the tool stable and trustworthy, the architecture explicitly **avoids**:
React, Ruby, a database, cloud/server-side storage, OCR, native Android,
drag/drop or absolute-positioning builders, server-side draft storage, and
AI-controlled totals. It favors a **narrow offline/static workflow** with fixed
layout and deterministic math.

## Guardrails (must not drift)

The invoice parser/PDF architecture is called out as something that **must not
drift** (roadmap blocker). Known risks to avoid: incorrect OpenRouter usage,
confusing HTML-to-PDF with `pdfmake`, using too many pages, adding storage too
early, absolute positioning for variable-length rows, or relying on browser print
as the final PDF method. The tool stays narrow and deterministic — new features
are weighed against that discipline (doc 04).

## Scope discipline

The generator was **scoped down to MVP** (roadmap `ct-2`, completed): an earlier
"enterprise" plan was judged overbuilt for current needs. Core invoicing first;
enterprise features only if and when validated.
