---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Starting_a_1099_freelance_business_with_EIN_and_banking.md__chunk-0013",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Starting_a_1099_freelance_business_with_EIN_and_banking.md",
  "chunk_index": 13,
  "chunk_count_for_source": 14,
  "char_start": 136439,
  "char_end": 148401,
  "source_sha256": "470b1f10705b5ba9d6b37f3959490d6d820c379957d1c86606620dfbe181421f",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

9	## XML Reference
   460	
   461	### Schema Compliance
   462	
   463	- **Element order in `<w:pPr>`**: `<w:pStyle>`, `<w:numPr>`, `<w:spacing>`, `<w:ind>`, `<w:jc>`, `<w:rPr>` last
   464	- **Whitespace**: Add `xml:space="preserve"` to `<w:t>` with leading/trailing spaces
   465	- **RSIDs**: Must be 8-digit hex (e.g., `00AB1234`)
   466	
   467	### Tracked Changes
   468	
   469	**Insertion:**
   470	```xml
   471	<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   472	  <w:r><w:t>inserted text</w:t></w:r>
   473	</w:ins>
   474	```
   475	
   476	**Deletion:**
   477	```xml
   478	<w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   479	  <w:r><w:delText>deleted text</w:delText></w:r>
   480	</w:del>
   481	```
   482	
   483	**Inside `<w:del>`**: Use `<w:delText>` instead of `<w:t>`, and `<w:delInstrText>` instead of `<w:instrText>`.
   484	
   485	**Minimal edits** - only mark what changes:
   486	```xml
   487	<!-- Change "30 days" to "60 days" -->
   488	<w:r><w:t>The term is </w:t></w:r>
   489	<w:del w:id="1" w:author="Claude" w:date="...">
   490	  <w:r><w:delText>30</w:delText></w:r>
   491	</w:del>
   492	<w:ins w:id="2" w:author="Claude" w:date="...">
   493	  <w:r><w:t>60</w:t></w:r>
   494	</w:ins>
   495	<w:r><w:t> days.</w:t></w:r>
   496	```
   497	
   498	**Deleting entire paragraphs/list items** - when removing ALL content from a paragraph, also mark the paragraph mark as deleted so it merges with the next paragraph. Add `<w:del/>` inside `<w:pPr><w:rPr>`:
   499	```xml
   500	<w:p>
   501	  <w:pPr>
   502	    <w:numPr>...</w:numPr>  <!-- list numbering if present -->
   503	    <w:rPr>
   504	      <w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z"/>
   505	    </w:rPr>
   506	  </w:pPr>
   507	  <w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   508	    <w:r><w:delText>Entire paragraph content being deleted...</w:delText></w:r>
   509	  </w:del>
   510	</w:p>
   511	```
   512	Without the `<w:del/>` in `<w:pPr><w:rPr>`, accepting changes leaves an empty paragraph/list item.
   513	
   514	**Rejecting another author's insertion** - nest deletion inside their insertion:
   515	```xml
   516	<w:ins w:author="Jane" w:id="5">
   517	  <w:del w:author="Claude" w:id="10">
   518	    <w:r><w:delText>their inserted text</w:delText></w:r>
   519	  </w:del>
   520	</w:ins>
   521	```
   522	
   523	**Restoring another author's deletion** - add insertion after (don't modify their deletion):
   524	```xml
   525	<w:del w:author="Jane" w:id="5">
   526	  <w:r><w:delText>deleted text</w:delText></w:r>
   527	</w:del>
   528	<w:ins w:author="Claude" w:id="10">
   529	  <w:r><w:t>deleted text</w:t></w:r>
   530	</w:ins>
   531	```
   532	
   533	### Comments
   534	
   535	After running `comment.py` (see Step 2), add markers to document.xml. For replies, use `--parent` flag and nest markers inside the parent's.
   536	
   537	**CRITICAL: `<w:commentRangeStart>` and `<w:commentRangeEnd>` are siblings of `<w:r>`, never inside `<w:r>`.**
   538	
   539	```xml
   540	<!-- Comment markers are direct children of w:p, never inside w:r -->
   541	<w:commentRangeStart w:id="0"/>
   542	<w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
   543	  <w:r><w:delText>deleted</w:delText></w:r>
   544	</w:del>
   545	<w:r><w:t> more text</w:t></w:r>
   546	<w:commentRangeEnd w:id="0"/>
   547	<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>
   548	
   549	<!-- Comment 0 with reply 1 nested inside -->
   550	<w:commentRangeStart w:id="0"/>
   551	  <w:commentRangeStart w:id="1"/>
   552	  <w:r><w:t>text</w:t></w:r>
   553	  <w:commentRangeEnd w:id="1"/>
   554	<w:commentRangeEnd w:id="0"/>
   555	<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>
   556	<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="1"/></w:r>
   557	```
   558	
   559	### Images
   560	
   561	1. Add image file to `word/media/`
   562	2. Add relationship to `word/_rels/document.xml.rels`:
   563	```xml
   564	<Relationship Id="rId5" Type=".../image" Target="media/image1.png"/>
   565	```
   566	3. Add content type to `[Content_Types].xml`:
   567	```xml
   568	<Default Extension="png" ContentType="image/png"/>
   569	```
   570	4. Reference in document.xml:
   571	```xml
   572	<w:drawing>
   573	  <wp:inline>
   574	    <wp:extent cx="914400" cy="914400"/>  <!-- EMUs: 914400 = 1 inch -->
   575	    <a:graphic>
   576	      <a:graphicData uri=".../picture">
   577	        <pic:pic>
   578	          <pic:blipFill><a:blip r:embed="rId5"/></pic:blipFill>
   579	        </pic:pic>
   580	      </a:graphicData>
   581	    </a:graphic>
   582	  </wp:inline>
   583	</w:drawing>
   584	```
   585	
   586	---
   587	
   588	## Dependencies
   589	
   590	- **pandoc**: Text extraction
   591	- **docx**: `npm install -g docx` (new documents)
   592	- **LibreOffice**: PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
   593	- **Poppler**: `pdftoppm` for images
   594	{"returncode":0,"stdout":"","stderr":""}File created successfully: /home/claude/operating_agreement.js{"returncode":0,"stdout":"Done\n","stderr":""}{"returncode":0,"stdout":"\nParagraphs: 0 → 113 (+113)\nAll validations PASSED!\n","stderr":""}Your Operating Agreement is done — download it and save it somewhere safe.

---

## What to do with this document:

- **Print and sign it** — date it today, May 22, 2026
- **Do not file it anywhere** — it's an internal document, not submitted to the ACC or IRS
- **Save a digital copy** — Google Drive, iCloud, wherever you keep important files
- **Bring it to the bank** — along with your Articles of Organization and EIN letter when you open your business account

---

## Where you stand right now:

- ✅ LLC name chosen — Deadhang Labor LLC
- ✅ Articles of Organization filed and approved
- ✅ EIN obtained
- ✅ Operating Agreement drafted
- ⏳ Publication notice — reminder set for May 29
- ⏳ Business banking — next step

**Ready to tackle the banking, or do you want to handle the publication notice first?**

---

**[USER]**

can you create a signed copy for me? i dont have a printer

---

**[ASSISTANT]**

I can add a digital signature line to the document, but I have to be straight with you —

**A typed or digitally inserted name is not a legally executed signature** in the traditional sense. For an Operating Agreement to be properly executed you need either:

- A **wet signature** (physical pen on paper)
- A **legally recognized e-signature** (DocuSign, Adobe Sign, HelloSign)

---

## Your best free option right now:

**DocuSign** has a free tier that lets you sign documents yourself at no cost.

1. Go to **[docusign.com](https://docusign.com)**
2. Create a free account
3. Upload the Operating Agreement I just created
4. Sign it digitally — legally recognized in Arizona and all 50 states
5. Download the signed copy as a PDF

That signed PDF is what you bring to the bank along with your Articles of Organization and EIN letter.

---

## Second free option:

**Adobe Acrobat free** at **[adobe.com](https://adobe.com)**
- Upload the Word doc, convert to PDF, add a signature
- Also legally recognized

---

## Fastest option if you have an iPhone:

- Open the document in the **Files app**
- Use **Markup** to draw your signature directly on it
- Save as PDF

---

Both DocuSign and Adobe are free for self-signing a single document. DocuSign is the cleanest option and what most banks are most familiar with.

Want me to walk you through anything else while you get that signed?

---

**[USER]**

what are my next steps?

---

**[ASSISTANT]**

Here's exactly where you stand and what's left in order of priority:

---

## ✅ Completed:
- LLC name — Deadhang Labor LLC
- Articles of Organization — filed and approved
- EIN — obtained and saved
- Operating Agreement — drafted and ready to sign

---

## Your next steps in order:

**1. Sign your Operating Agreement — today**
- Use DocuSign free tier or Adobe
- Takes 10 minutes
- You need this signed before banking

**2. Open your business bank account — this week**
- Bring these four things:
   - Signed Operating Agreement
   - Articles of Organization PDF
   - EIN confirmation letter
   - Your personal ID
- Recommended: Relay Financial (online, free) or Chase Business Complete (in person, Glendale/Mesa area)

**3. Get a business debit card**
- Comes with your bank account
- Every single business expense and income runs through this from day one

**4. Publish your formation notice — before May 29**
- Go to azbex.com
- Tell them you need an LLC formation notice in Maricopa County
- $30–75, they handle the wording
- Calendar reminder already set

**5. Set up invoicing — this week**
- Sign up for Wave at wave.com — completely free
- Set up your first invoice template as Deadhang Labor LLC
- You need this ready before your next gig

**6. Open a tax savings account — within 30 days**
- Separate savings account, business or personal
- Every payment you receive — move 25–30% into it immediately
- This covers your quarterly estimated taxes

**7. File your first quarterly estimated taxes**
- Due dates: April, June, September, January
- Next deadline: **June 16, 2026** — coming up fast
- IRS Form 1040-ES
- Pay at irs.gov/payments

---

## Longest pole in the tent right now:

**The June 16 estimated tax deadline.** That's 25 days away. Once your bank account is open we need to look at what you've earned so far this year as a 1099 contractor and make sure you're not caught short.

What do you want to tackle first — banking or getting your invoicing set up?

---

**[USER]**

banking

---

**[ASSISTANT]**

Let's get this done this week.

---

## First — which banking option fits you best?{
  "questions": [
    {
      "question": "Do you want to open your business account online or in person?",
      "options": [
        "Online \u2014 fastest, no branch needed",
        "In person \u2014 I want to talk to someone face to face"
      ],
      "type": "single_select"
    },
    {
      "question": "What matters most to you in a business bank account?",
      "options": [
        "Zero fees",
        "Physical branch nearby",
        "Integrates with accounting software",
        "Earns interest on balance"
      ],
      "type": "single_select"
    }
  ]
}

---

**[USER]**

signed up for banking that has accounting in it

---

**[ASSISTANT]**

Which bank or platform did you sign up with?

---

**[USER]**

found

---

**[ASSISTANT]**

Perfect — which one did you go with?

---

**[USER]**

it is called "Found" business banking

---

**[ASSISTANT]**

Great choice for your situation — Found is purpose-built for self-employed 1099 contractors. Smart pick.

---

## What Found gives you that matters for Deadhang Labor LLC:

- ✅ Built-in expense tracking and categorization
- ✅ Automatic tax savings — it sets aside a percentage of every deposit automatically
- ✅ Invoicing built in — you may not even need Wave
- ✅ Schedule C preparation built in
- ✅ No monthly fees
- ✅ Business debit card

---

## Right now inside Found, set these up immediately:

**1. Set your tax savings rate**
- Found will ask you what percentage to auto-set aside
- Set it at **28–30%** for your situation as a single-member LLC
- This is non-negotiable — do it before your first deposit hits

**2. Connect your business profile**
- Enter Deadhang Labor LLC as your business name
- Enter your EIN — 42-2712662
- Select your business type — Single Member LLC
- Industry — Specialty Trade Contractor

**3. Set up your first invoice template**
- Business name: Deadhang Labor LLC
- Your address: 9017 E Vine Ave, Mesa AZ 85208
- Payment terms: Net 15 (you get paid within 15 days)

---

## Once your debit card arrives:

Every business expense from that point forward goes on that card — zero exceptions.
