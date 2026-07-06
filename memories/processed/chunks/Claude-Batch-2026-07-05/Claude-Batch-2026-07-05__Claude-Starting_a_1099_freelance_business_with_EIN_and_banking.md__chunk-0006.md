---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Starting_a_1099_freelance_business_with_EIN_and_banking.md__chunk-0006",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Starting_a_1099_freelance_business_with_EIN_and_banking.md",
  "chunk_index": 6,
  "chunk_count_for_source": 14,
  "char_start": 56840,
  "char_end": 68838,
  "source_sha256": "470b1f10705b5ba9d6b37f3959490d6d820c379957d1c86606620dfbe181421f",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

440" cy="380" r="2" fill="var(--t)"/>
    <text class="ts" x="474" y="384">Tank wall</text></g>
  <g class="node" onclick="sendPrompt('How does the gas burner heat water?')">
    <line class="leader" x1="432" y1="454" x2="468" y2="454"/><circle cx="432" cy="454" r="2" fill="var(--t)"/>
    <text class="ts" x="474" y="458">Heating element</text></g>
</svg>
<div style="display:flex;align-items:center;gap:16px;margin:12px 0 0;font-size:13px;color:var(--color-text-secondary)">
  <label style="display:flex;align-items:center;gap:6px;cursor:pointer;user-select:none">
    <span class="toggle-track">
      <input type="checkbox" id="heat-toggle" checked onchange="toggleHeat(this.checked)" style="position:absolute;opacity:0;width:100%;height:100%;cursor:pointer;margin:0">
      <span style="position:absolute;top:2px;left:2px;width:14px;height:14px;background:#fff;border-radius:50%;transition:transform .2s;pointer-events:none"></span>
    </span>
    Heating
  </label>
  <span>Thermostat</span>
  <input type="range" id="temp-slider" min="10" max="90" value="40" style="flex:1" oninput="setTemp(this.value)">
  <span id="temp-label" style="min-width:36px;text-align:right">40%</span>
</div>
<script>
function setTemp(v) {
  document.getElementById('gh').setAttribute('offset', v+'%');
  document.getElementById('gc').setAttribute('offset', v+'%');
  document.getElementById('temp-label').textContent = v+'%';
}
function toggleHeat(on) {
  document.getElementById('flames').classList.toggle('off', !on);
  document.getElementById('warm-glow').classList.toggle('off', !on);
  document.querySelectorAll('.conv').forEach(p => p.classList.toggle('off', !on));
}
</script>
```

**Illustrative example — abstract subject** (attention in a transformer). Same rules, no physical object. A row of tokens at the bottom, one query token highlighted, weight-scaled lines fanning to every other token. Caption sits below the fan — clear of every stroke — not inside it.
```svg
<rect class="c-purple" x="60" y="40"  width="560" height="26" rx="6" stroke-width="0.5"/>
<rect class="c-purple" x="60" y="80"  width="560" height="26" rx="6" stroke-width="0.5"/>
<rect class="c-purple" x="60" y="120" width="560" height="26" rx="6" stroke-width="0.5"/>
<text class="ts" x="72" y="57" >Layer 3</text>
<text class="ts" x="72" y="97" >Layer 2</text>
<text class="ts" x="72" y="137">Layer 1</text>

<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="116" y2="146" stroke-width="1"   opacity="0.25"/>
<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="228" y2="146" stroke-width="1.5" opacity="0.4"/>
<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="340" y2="146" stroke-width="4"   opacity="1.0"/>
<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="452" y2="146" stroke-width="2.5" opacity="0.7"/>
<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="564" y2="146" stroke-width="1"   opacity="0.2"/>

<g class="node" onclick="sendPrompt('What do the attention weights mean?')">
  <rect class="c-gray"  x="80"  y="230" width="72" height="36" rx="6" stroke-width="0.5"/>
  <rect class="c-gray"  x="192" y="230" width="72" height="36" rx="6" stroke-width="0.5"/>
  <rect class="c-amber" x="304" y="230" width="72" height="36" rx="6" stroke-width="1"/>
  <rect class="c-gray"  x="416" y="230" width="72" height="36" rx="6" stroke-width="0.5"/>
  <rect class="c-gray"  x="528" y="230" width="72" height="36" rx="6" stroke-width="0.5"/>
  <text class="ts" x="116" y="252" text-anchor="middle">the</text>
  <text class="ts" x="228" y="252" text-anchor="middle">cat</text>
  <text class="th" x="340" y="252" text-anchor="middle">sat</text>
  <text class="ts" x="452" y="252" text-anchor="middle">on</text>
  <text class="ts" x="564" y="252" text-anchor="middle">the</text>
</g>

<text class="ts" x="340" y="300" text-anchor="middle">Line thickness = attention weight from "sat" to each token</text>
```

Note what's *not* here: no boxes labelled "multi-head attention", no arrows labelled "Q/K/V". Those belong in the structural diagram. This one is about the *feeling* of attention — one token looking at every other token with varying intensity.

These are starting points, not ceilings. For the water heater: add a thermostat slider, animate the convection current, toggle heating vs standby. For the attention diagram: let the user click any token to become the query, scrub through layers, animate the weights settling. The goal is always to *show* how the thing works, not just *label* it.
Here's the full roadmap, Aaron — from zero to business banking, broken into clean phases. Then I'll hit the cost breakdown right after.

---

## Phase 1 — Choose your business structure

For a solo freelance 1099 operation like yours, your two real options are:

**Sole Proprietorship** — simplest, zero formation cost, no paperwork. But you're personally liable for everything, and it looks less professional to clients.

**Single-Member LLC** — still just you, but creates a legal separation between personal and business assets. This is what most working stagehand/production contractors choose, and it's what I'd recommend. Most clients and production companies also prefer invoicing an LLC.

> For what you're doing — labor coordination, rigging, corporate events — an **LLC is the better call**. Minimal extra cost, meaningfully better protection.

---

## Phase 2 — Form your LLC in Arizona

**Step 1: Choose your LLC name**
- Must include "LLC" or "Limited Liability Company"
- Check availability at the [Arizona Corporation Commission (ACC)](https://ecorp.azcc.gov)
- Can't conflict with existing Arizona entities

**Step 2: File Articles of Organization**
- Go to [azcc.gov](https://ecorp.azcc.gov) → online filing
- Filing fee: **$50 (online)** or $85 (paper)
- You'll fill out: LLC name, statutory agent, member/manager info
- Approval is typically **within 2–5 business days** online

**Step 3: Appoint a Statutory Agent**
- Required in Arizona — this is someone with a physical AZ address who accepts legal documents
- You can be your own if you have a street address (not PO box)
- Or pay a registered agent service (~$50–$100/year) for privacy and reliability

**Step 4: Arizona Publication Requirement** ⚠️
- Arizona is one of very few states with this quirk
- You must publish a Notice of Formation in a newspaper in the county where your LLC is based for **3 consecutive weeks**
- Maricopa County (Peoria/Glendale area) has an approved newspaper list — look for affordable legal notice publishers
- Cost: typically **$30–$75** for Maricopa County
- You have **60 days** from approval to complete this
- Submit the Affidavit of Publication to the ACC when done

**Step 5: Create an Operating Agreement**
- Not required by Arizona law, but critical for banking and legitimacy
- A single-member LLC operating agreement is a short document that defines ownership and how the business runs
- Free templates exist at LegalZoom, Rocket Lawyer, or just draft your own — it doesn't need to be filed anywhere

---

## Phase 3 — Get your EIN (Employer Identification Number)

Your EIN is basically a Social Security Number for your business. Banks require it to open a business account.

**How to get it:**
1. Go to [irs.gov/ein](https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online)
2. Click **"Apply Online Now"**
3. Select entity type: **LLC**
4. Select reason: "Started a new business"
5. Fill in your info — takes about 10 minutes
6. You receive your EIN **immediately** on screen and via PDF confirmation

> **Important:** Wait until your LLC is officially approved by the ACC before applying for your EIN. The IRS will ask for your LLC formation date.

**Cost: $0** — the IRS does not charge for EINs.

---

## Phase 4 — Open your business bank account

Once you have your **EIN + ACC approval confirmation + Operating Agreement**, you're ready to bank.

**What you'll need to bring:**
- EIN confirmation letter (print the IRS PDF)
- Arizona LLC Articles of Organization (ACC approval)
- Your Operating Agreement
- Your personal ID
- Opening deposit (varies by bank — some require $0, some $25–$100)

**Best options for a solo 1099 LLC in Phoenix metro:**
- **Relay Financial** (online) — zero fees, great for freelancers, integrates with accounting tools
- **Chase Business Complete** — wide ATM network, works well for cash deposits from gigs
- **Wells Fargo Initiate** — solid option, branches all over the Valley
- **Bluevine** or **Mercury** (online) — good if you want no-fee business checking with interest

> Get a dedicated business debit card ASAP. Every production payment and every business expense runs through it — this makes your taxes and any future audits clean and simple.

---

## Phase 5 — Post-banking setup (don't skip these)

- **Get a business credit card** — even a low-limit one. Builds business credit and separates expenses further.
- **Set up invoicing** — Wave (free), QuickBooks Self-Employed, or even a Google Docs template
- **Open a tax savings account** — as a 1099 sole LLC member, set aside ~25–30% of every payment. No employer is withholding for you.
- **File quarterly estimated taxes** — due in April, June, September, January (IRS Form 1040-ES)

---

## Startup Cost Estimate

Here's a realistic budget for your situation:

| Item | Cost |
|------|------|
| Arizona LLC filing (online) | $50 |
| Statutory agent (optional, 1st year) | $0–$75 |
| Publication requirement (Maricopa Co.) | $30–$75 |
| Operating Agreement (DIY) | $0 |
| EIN | $0 |
| Business bank account opening deposit | $0–$100 |
| Basic invoicing software (first year) | $0 (Wave free tier) |
| **Total realistic range** | **$80–$300** |

If you want to keep it lean and DIY the operating agreement, **$100–$130** is a very achievable all-in number for a Maricopa County LLC.

---

Here's a visual summary of the full flow:Content rendered and shown to the user. Please do not duplicate the shown content in text because it's already visually represented.[This tool call rendered an interactive widget in the chat. The user can already see the result — do not repeat it in text or with another visualization tool.]---

The one thing most people miss is the **Arizona publication requirement** — it's obscure, it's annoying, and skipping it can void your LLC status. Don't sleep on it.

What name are you thinking for the LLC — something branded or just your name?

---

**[USER]**

walk me through this I will respond to you in step by step answers and responses. 

phase 1. I am choosing LLC I need to come up with a business name that will not be weird later on if I start to hire other contractors for help at gigs.

---

**[ASSISTANT]**

Smart thinking ahead, Aaron. A name that works for solo *and* scaled is the move.

Here's the framework for picking a good one:

**Avoid names that box you in:**
- Your full name + "Stagehand" = too personal, weird when others work under it
- Too narrow (e.g. "Phoenix Staging Co.") = limits you geographically or by service type
- Too vague (e.g. "AZ Productions LLC") = forgettable, hard to brand

**What works well for a production/labor contractor that can scale:**
- A short, neutral word or phrase + "Productions", "Crew", "Labor", "Group", "Services", or "Works"
- Something that sounds like an operation, not a person
- Ideally something that could also anchor The Crew Blueprint brand later if you want crossover

**A few directional examples** (not recommendations, just to spark ideas):
- *Ironset Group LLC*
- *Groundworks Production Services LLC*
- *Apex Crew Services LLC*
- *Ridgeline Labor LLC*
- *Stageframe LLC*

---

What's your instinct — do you want the name to feel **production/industry-specific** (staging, rigging, events), more **neutral and professional** (could pass for any labor/contractor company), or something that **nods to your personal brand** (Crew Blueprint adjacent)?

---

