---
{
  "chunk_id": "kimi-batch-2026-07-05__md_handoff_bundle__99_COMBINED.md__chunk-0004",
  "archive_id": "kimi-batch-2026-07-05",
  "archive_filename": "kimi-batch-2026-07-05.zip",
  "source_path": "md_handoff_bundle/99_COMBINED.md",
  "chunk_index": 4,
  "chunk_count_for_source": 11,
  "char_start": 34154,
  "char_end": 46114,
  "source_sha256": "9772a55e6bd39feb19ba3cd97e82a79ceb707555954f39f31d7c675db0f025a1",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

es and API details to ensure the guide is up-to-date and accurate.

I've created a comprehensive 54,000+ character framework and step-by-step build guide for your custom invoice generator. Here's the complete overview:

---

## SYSTEM ARCHITECTURE

The system uses a **microservices architecture** with these layers:

- **Client Layer**: React web app, mobile app, admin dashboard, customer portal
- **API Gateway**: Kong/AWS API Gateway with rate limiting and auth
- **Application Layer**: Invoice Service, Payment Service (Stripe), Bank Service (Plaid), Reconciliation Engine, Notification Service
- **Data Layer**: PostgreSQL (primary), Redis (cache), S3 (PDFs), Elasticsearch (search)
- **External Services**: Stripe, Plaid, SendGrid, Avalara (tax)

---

## CORE INTEGRATIONS

### Payment Processor: Stripe

- **Stripe Connect** for marketplace-style payouts to your bank account
- **Stripe Invoicing API** for branded invoice emails with payment links
- **PaymentIntents** for immediate card/ACH processing
- **Webhook handling** for `invoice.paid`, `payment_intent.succeeded`, `payout.paid` events
- **Application fees** (e.g., 2.5%) if you're building for multiple users

### Bank Account: Plaid

- **Plaid Link** for secure bank authentication (no credential storage)
- **Auth product** for account/routing number verification
- **Transactions product** for automatic reconciliation
- **Balance checks** before ACH debits to prevent failures
- **Token exchange flow**: public_token → access_token (encrypted at rest)

---

## 12-WEEK BUILD PHASES

| Phase | Weeks | Focus |
| --- | --- | --- |
| 1. Foundation | 1-2 | Project setup, database schema, entity definitions |
| 2. Core Invoice | 3-4 | CRUD API, PDF generation, invoice numbering, status workflow |
| 3. Payment Integration | 5-6 | Stripe Connect onboarding, PaymentIntents, webhook handlers |
| 4. Bank Integration | 7-8 | Plaid Link, account connection, transaction syncing |
| 5. Frontend Dashboard | 9-10 | React app, invoice list, analytics, payment pages |
| 6. Testing & Deploy | 11-12 | Unit/integration/E2E tests, Docker, CI/CD, Kubernetes |

---

## KEY TECHNICAL DECISIONS

- **Never store raw card data** — Use Stripe Elements (PCI SAQ A compliance)
- **Encrypt Plaid access tokens** with AES-256 before database storage
- **Use message queues** (RabbitMQ/Bull) for PDF generation and email sending
- **Implement idempotency keys** for all payment operations to prevent double-charges
- **Daily automated reconciliation** between Stripe payouts and bank transactions

---

## ESTIMATED COSTS

- **Development**: $21,000–$42,000 (3–6 months, 1–2 developers)
- **Monthly Infrastructure**: $205–$690 fixed + ~2.9% Stripe transaction fees
- **Per Transaction**: Stripe (2.9% + $0.30) + Plaid ($0.30/connection)

---

The full guide includes complete code examples for:

- Database schema with TypeORM entities
- Stripe service implementation (customers, invoices, PaymentIntents, refunds)
- Plaid Link integration with token exchange
- Reconciliation engine with cron jobs
- PDF generation with Puppeteer + Handlebars
- React frontend with payment forms
- Docker + Kubernetes deployment configs
- GitHub Actions CI/CD pipeline
- Comprehensive testing strategy

**Referenced output from original chat:** `invoice_generator_framework.md`


<!-- END 02_custom_invoice_generator_framework_summary.md -->


---

<!-- BEGIN 03_production_atlas_research_handoff_review_and_v2.md -->

# Production Atlas — Research Handoff Review and Revised V2

Source file: `Pasted markdown(3).md`

---

Original URL: https://www.kimi.com/chat/19ef7afe-9032-804c-8000-09e2d8602934?chat_enter_method=history
Export Time: 7/5/2026, 5:10:32 PM

**[USER]**

I am giving you a handoff document for Production Atlas / Festival Atlas research.

Your job is to use the document as the full project context and produce public-safe research results for the event or producer batch I name next.

Do not include private contacts, phone numbers, personal emails, pay rates, hotel/lodging details, rumors, login-only information, or copied scraped text.

Focus only on:
1. crew lodging / camping / accommodation signals
2. travel / per diem / mileage / housing support signals
3. labor and staffing routes
4. IATSE/local jurisdiction verification language
5. public production vendor stack

Use only public sources. If something is not publicly confirmed, say:
“Unknown publicly. Human verification needed.”

Use “possible” only when the pattern is strong but not directly confirmed.

Return results in the JavaScript-style output format from the handoff document, with source labels and URLs included.

Start with this target:
[PASTE EVENT NAME OR PRODUCER BATCH HERE]

---

**[ASSISTANT]**

I understand the project context. I'm ready to research any event or producer batch you name.

Please paste the event name or producer batch you'd like me to start with. For example:

-   **Producer batch:** "Danny Wimmer Presents" (Batch 1)
    
-   **Individual event:** "Louder Than Life 2026" or "EDC Las Vegas 2026"
    
-   **Tier list:** "All Tier 1 events"
    

What should I research first?

---

**[USER]**

Find flaws in the research packet and make it better.

---

**[ASSISTANT]**

I need to see the research packet you're referring to. Could you paste it here? Once I have it, I'll review it against the handoff document requirements and flag any issues with:

-   **Public-safety violations** (private contacts, pay rates, hotel details, rumors, etc.)
    
-   **Status value misuse** (confirmed vs. possible vs. unknown)
    
-   **Missing source URLs** or weak attribution
    
-   **IATSE/local jurisdiction wording** that isn't cautious enough
    
-   **Vendor claims** that aren't tied to public evidence
    
-   **Producer-level patterns** overstated as event-specific facts
    
-   **Template compliance** (missing fields, wrong format)
    

Paste the packet and I'll give you a clean critique plus suggested fixes.

---

**[USER]**

The research handoff document

---

**[ASSISTANT]**

I understand — you'd like me to review the research handoff document itself for flaws and suggest improvements.

Here is my critique, organized by severity and section:

* * *

## Critical Flaws

### 1\. No Event-Specific Date Fields

The template (Section 10) lacks `eventDates`, `loadInDates`, or `strikeDates`. For a traveling 1099 contractor, knowing when load-in starts and when strike ends is essential for booking travel and deciding if accommodation costs are justified. Without dates, the "can I afford to work this event?" question cannot be answered.

**Fix:** Add `loadInStart`, `showDates`, `strikeEnd`, and `totalDaysOnSite` to the output template.

### 2\. "Possible" Is Over-Used and Under-Defined

Section 4 allows `possible` for lodging, travel, and labor routes when "strong venue/producer pattern supports it but no source confirms it." This is a judgment call with no criteria. Two researchers will apply it differently.

**Fix:** Add a decision rubric for `possible`:

-   At least 2 prior events by the same producer with the same pattern?
    
-   Same venue used in prior years with confirmed pattern?
    
-   Same vendor ecosystem with public statements about their standard terms?
    
-   Otherwise, default to `unknown`.
    

### 3\. No Deduplication Rule for Producer Batches

Section 6 says research by producer batch first, but Section 10's output template has no field to flag "this is a producer-level pattern, not event-specific." This risks event blocks being inflated with unconfirmed producer assumptions.

**Fix:** Add a `evidenceLevel` field to each source object: `'event-specific' | 'producer-pattern' | 'industry-standard'`.

### 4\. Vendor Stack Departments Are Too Narrow

`site_ops_power` is one field, but site ops and power are often separate vendors (e.g., one company does fencing/site logistics, another does generators/utility tie-ins). Collapsing them loses actionable detail.

**Fix:** Split into `site_ops` and `power`, or add an `other_vendors` catch-all array for departments not in the fixed list.

* * *

## Moderate Flaws

### 5\. Search Query Bank Is Under-Indexed for 2026

Section 9 suggests generic queries like `<festival name> production crew jobs 2026` but doesn't include year-specific operators, date-restricted searches, or LinkedIn/Glassdoor as explicit sources. Many festivals haven't announced 2026 details yet.

**Fix:** Add queries like:

-   `"<festival name>" "2026" "production crew" after:2025-09-01`
    
-   `site:linkedin.com "<festival name>" "production"`
    
-   `site:glassdoor.com "<producer name>" "festival" "per diem"`
    

### 6\. No "Not Applicable" Status

Some fields genuinely don't apply. For example, a single-day urban festival at a permanent venue may have no crew camping at all — not "unlikely," but structurally irrelevant. "Unlikely" implies it was considered and rejected.

**Fix:** Add `not_applicable` as an allowed status for lodging/travel fields, with a note explaining why.

### 7\. Missing "Last Verified" Timestamp

The document says "Current as of 2026-06-23" but the output template has no per-event `lastVerified` field. A contractor looking at data from January vs. June needs to know freshness.

**Fix:** Add `lastVerified: 'YYYY-MM-DD'` to every output block.

### 8\. No Escalation Path for "Human Verification Needed"

Section 12 says "Unknown publicly. Human verification needed" but never says *who* does the verification or *how* it gets back into the database. This is a process gap, not a template gap, but it will cause stale `unknown` fields to persist.

**Fix:** Add a Section 13: "Human Verification Protocol" — define who contacts the producer/vendor, what questions to ask, and how verified data is re-submitted.

* * *

## Minor / Polish Issues

### 9\. Inconsistent Score Granularity

Tier 1 is 60+, Tier 2 is 50–59, but some Tier 2 events (Austin City Limits at 58, Welcome to Rockville at 58, Hulaween at 58) score higher than Tier 3 events (Sick New World at 48, Oceans Calling at 48). The scoring methodology isn't explained, so a researcher can't verify or challenge a score.

**Fix:** Document the scoring formula in Section 8 or move it to an appendix.

### 10\. "Public-Safe" Is Defined by Negation

Section 3 lists what *not* to include but doesn't define what *is* acceptable. For example, is a public LinkedIn post by a vendor naming a festival a valid source? Is a festival's official "partners" page sufficient for vendor confirmation?

**Fix:** Add a positive definition: "Public-safe sources include: official festival/producer/venue websites, verified social media accounts, press releases, industry publications (TPi, IQ, Mondo\*dr, Pollstar), public LinkedIn case studies, and IATSE.org local directory listings."

### 11\. No Handling of Cancelled / Postponed / TBD Events

Okeechobee 2026 already has "Verify current status" in the notes. But the template has no `eventStatus` field (confirmed, postponed, cancelled, TBD).

**Fix:** Add `eventStatus: 'confirmed|postponed|cancelled|tbd'` at the top of each event block.

### 12\. Template Uses Single Quotes and Backslashes

The Section 10 template uses `\'` escaping throughout, which is JavaScript-legal but error-prone for copy-paste handoffs. A malformed paste will break `npm run validate:all`.

**Fix:** Provide a clean JSON template alongside the JS-style block, or add a "Copy this exactly" warning.

* * *

## Summary Table of Fixes

| Priority | Issue | Fix |
| --- | --- | --- |
| Critical | No date fields | Add load-in/show/strike dates |
| Critical | "Possible" undefined | Add rubric with minimum evidence |
| Critical | No producer vs. event distinction | Add evidenceLevel to sources |
| Critical | Vendor departments too narrow | Split site_ops_power |
| Moderate | Search queries outdated | Add 2026-specific operators |
| Moderate | No "not applicable" status | Add to allowed values |
