Original URL: https://www.perplexity.ai/search/8fd08c22-1dd0-4620-8d5d-5033014a840a
Conversation Time: 6/13/2026, 9:30:14 AM
Export Time: 7/5/2026, 5:02:39 PM

**[USER]**

Best architecture
Frontend
Use a simple web app hosted on your subdomain:
HTML
CSS
JavaScript
Static invoice template
PDF generation in the browser
Backend
Use PHP because your cPanel already supports it and it is simple to deploy.
The PHP backend would:
Receive your conversational invoice text.
Send it to an AI model or parse it locally.
Return structured JSON.
Validate required fields.
Generate or return the invoice data.
PDF generation
Use one of these two approaches:
Best option: HTML invoice converted to PDF
Create the invoice as fixed HTML and CSS, then convert it to PDF.
For example:
Plain text
Invoice template HTML
+
Structured invoice values
+
Fixed CSS positions
=
Final PDF
This is easier to maintain than drawing text directly onto an image.
Alternative: background image with fixed coordinates
Use the existing invoice image as the page background and place text at predetermined coordinates.
Example:
JavaScript
const positions = {
  invoiceNumber: { x: 720, y: 110 },
  invoiceDate: { x: 720, y: 145 },
  clientName: { x: 90, y: 225 },
  total: { x: 720, y: 920 }
};
The user never sees or adjusts these positions. They are configured once in code.
The application screens
The app only needs three screens.
1. Invoice input
A large text box:
Plain text
Describe the invoice...
Buttons:
Process Invoice
Clear
Load Previous Invoice
2. Review
Display the interpreted values:
Client
Invoice number
Dates
Descriptions
Hours
Rates
Expenses
Total
Payment terms
The user can correct anything that was interpreted incorrectly.
Buttons:
Edit Instructions
Generate Invoice
Save Draft
3. PDF preview
Show the finished invoice.
Buttons:
Download PDF
Go Back
Create Another
Conversational processing options
There are two ways to interpret the pasted information.
Option A: AI parsing
Use an AI API such as OpenRouter to convert natural language into a strict JSON structure.
This gives you flexible input. You could write naturally rather than following a fixed format.
Example instruction to the model:
Plain text
Extract invoice information from the user's message.

Return only valid JSON matching this schema:

{
  "client": "",
  "invoice_number": "",
  "invoice_date": "",
  "payment_terms": "",
  "entries": [
    {
      "date": "",
      "description": "",
      "hours": 0,
      "rate": 0,
      "amount": 0
    }
  ],
  "expenses": [
    {
      "description": "",
      "amount": 0
    }
  ]
}

Do not invent missing financial values.
Use null for anything not provided.
Do not calculate the final total unless all required values are present.
The API key must remain in PHP on the server, never inside browser JavaScript.
Option B: Structured text without AI
Require a predictable format:
Plain text
Client: Guardian Production Services
Invoice: 1047
Terms: Net 30

2026-06-10 | ELO concert | 10 | 35
2026-06-11 | Load-out | 6 | 35

Expense: Parking | 25
JavaScript or PHP can parse this without any AI or internet service.
This is more private and reliable, but less conversational.
Best choice for you
Use a hybrid system:
Allow natural conversational input.
Use AI to convert it into JSON.
Show the extracted values for review.
Calculate all money in normal PHP or JavaScript.
Insert the values into the static invoice.
Generate the PDF.
Download it directly.
The AI should only interpret the wording. It should not control totals or PDF placement.
Simplified build specification
Markdown
# Fixed Invoice Generator Web App

Build a private web application that converts conversational invoice instructions into a completed PDF invoice.

## Core workflow

1. The user pastes or types invoice information into a large text box.
2. The application converts the text into structured invoice fields.
3. The application displays the extracted fields for review.
4. The user corrects any errors.
5. The application calculates all totals deterministically.
6. The values are inserted into a fixed invoice template.
7. The application generates a PDF.
8. The user downloads the PDF directly.

## Do not include

- Dragging
- Field positioning
- Template editing
- Email sending
- Payment tracking
- Cloud file storage
- Client dashboards
- OCR
- Screenshot analysis
- Mobile app packaging

## Technical stack

- HTML
- CSS
- JavaScript
- PHP
- OpenRouter or another AI API for text-to-JSON parsing
- HTML-to-PDF or browser-based PDF generation
- Fixed invoice template

## Required invoice fields

- Contractor name
- Contractor address

---

**[ASSISTANT]**

I’ll analyze your architecture and provide the best recommendations for building this conversational invoice generator web app.

## Architecture Assessment

Your proposed architecture is **solid and well-optimized** for a small business tool. Here's why it works:

| Component | Your Choice | Why It's Good |
|-----------|-------------|---------------|
| Frontend | HTML/CSS/JS static app | Lightweight, phone-friendly, no build process  |
| Backend | PHP | Already supported by cPanel, simple deployment, secure API key handling  |
| PDF Generation | HTML-to-PDF in browser | Easier maintenance than coordinate-based image placement  |
| Parsing | Hybrid (AI + deterministic) | Conversational input + reliable math control  |

## Key Recommendations

### 1. **PDF Generation: Use `pdfmake` or `jspdf` in Browser**
Your "Best option" (HTML-to-PDF) is correct. For browser-based generation:

```javascript
// Using pdfmake (best for HTML-like templates)
import { pdf } from '@pdfmake/app';

const doc = {
  content: [
    { text: 'Invoice #' + invoiceNumber, style: 'header' },
    { text: clientName, style: 'client' },
    // ... rest of template
  ],
  styles: {
    header: { fontSize: 18, bold: true },
    client: { fontSize: 12, margin: [0, 10] }
  }
};

pdf(doc).download('invoice.pdf');
```

**Why browser-based over PHP:**
- API key stays in PHP only (AI parsing)
- PDF generation is instant, no server roundtrip
- Works offline after initial load 

### 2. **AI Parsing: OpenRouter with Strict JSON Schema**
Your Option A approach is correct. Use this PHP structure:

```php
// backend/process.php
<?php
header('Content-Type: application/json');

$conversationalText = $_POST['invoice_text'];
$apiKey = getenv('OPENROUTER_API_KEY'); // Never in JS

$prompt = <<<PROMPT
Extract invoice information from this message. Return ONLY valid JSON:

{
  "client": "",
  "invoice_number": "",
  "invoice_date": "",
  "payment_terms": "",
  "entries": [
    {"date": "", "description": "", "hours": 0, "rate": 0, "amount": 0}
  ],
  "expenses": [
    {"description": "", "amount": 0}
  ]
}

Use null for missing values. Do not calculate totals.
PROMPT;

$response = json_encode([
  'model' => 'openai/gpt-4o',
  'messages' => [['role' => 'user', 'content' => $prompt . "\n\n" . $conversationalText]]
]);

$ch = curl_init('https://openrouter.ai/api/v1/chat/completions');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $response);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  'Authorization: API-Key ' . $apiKey,
  'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
$jsonOutput = json_decode($result, true);

echo json_encode([
  'success' => true,
  'data' => json_decode($jsonOutput['content'][0]['text'])
]);
?>
```

### 3. **Deterministic Totals: Calculate in JavaScript**
Never let AI calculate money. Your hybrid approach is correct:

```javascript
// Frontend: Calculate after AI parsing
function calculateTotals(invoiceData) {
  const lineTotal = invoiceData.entries.reduce((sum, entry) => {
    entry.amount = entry.hours * entry.rate;
    return sum + entry.amount;
  }, 0);
  
  const expenseTotal = invoiceData.expenses.reduce((sum, exp) => sum + exp.amount, 0);
  
  invoiceData.total = lineTotal + expenseTotal;
  invoiceData.lineTotal = lineTotal;
  invoiceData.expenseTotal = expenseTotal;
  
  return invoiceData;
}
```

### 4. **Three-Screen Flow Implementation**

**Screen 1: Input** (`index.html`)
```html
<textarea id="invoiceInput" placeholder="Describe the invoice..."></textarea>
<button onclick="processInvoice()">Process Invoice</button>
<button onclick="clearInput()">Clear</button>
<button onclick="loadPrevious()">Load Previous Invoice</button>
```

**Screen 2: Review** (`review.html`)
```html
<div id="reviewFields">
  <input id="client" value="{{data.client}}">
  <input id="invoiceNumber" value="{{data.invoice_number}}">
  <!-- All fields with edit capability -->
</div>
<button onclick="generateInvoice()">Generate Invoice</button>
<button onclick="saveDraft()">Save Draft</button>
```

**Screen 3: PDF Preview** (`preview.html`)
```html
<div id="pdfPreview"></div>
<button onclick="downloadPDF()">Download PDF</button>
<button onclick="goBack()">Go Back</button>
<button onclick="createAnother()">Create Another</button>
```

### 5. **Static Invoice Template (HTML + Fixed CSS)**

```html
<!-- invoice-template.html -->
<!DOCTYPE html>
<html>
<head>
  <style>
    @page { size: 8.5in 11in; margin: 0.5in }
    .header { position: absolute; top: 0.5in; left: 6in; }
    .client-info { position: absolute; top: 1.5in; left: 0.5in; }
    .total { position: absolute; top: 8in; left: 6in; font-size: 18px; }
  </style>
</head>
<body>
  <div class="header">
    <h1>Invoice #<span id="invNumber"></span></h1>
    <p>Date: <span id="invDate"></span></p>
  </div>
  <div class="client-info">
    <p>Client: <span id="clientName"></span></p>
  </div>
  <!-- Rest of template -->
</body>
</html>
```

Then inject values and convert:

```javascript
function injectValues(template, data) {
  document.getElementById('invNumber').textContent = data.invoice_number;
  document.getElementById('invDate').textContent = data.invoice_date;
  document.getElementById('clientName').textContent = data.client;
  // ... all fields
}

function downloadPDF() {
  const content = document.documentElement.outerHTML;
  window.print(); // Or use pdfmake/jspdf
}
```

## What You're Doing Right

✅ **API key in PHP only** – Critical security practice  
✅ **AI only interprets, doesn't calculate** – Prevents financial errors  
✅ **Fixed HTML template** – Easier than coordinate-based image placement  
✅ **Browser PDF generation** – No server dependency, instant download  
✅ **Three simple screens** – Minimal UX, no friction  
✅ **No unnecessary features** – You correctly excluded drag, email, OCR, etc.  

## Final Build Checklist

```markdown
# Fixed Invoice Generator Web App - Implementation Checklist

## Required Files
- /index.html (Input screen)
- /review.html (Review/edit screen)
- /preview.html (PDF preview screen)
- /invoice-template.html (Fixed HTML/CSS template)
- /backend/process.php (AI parsing API)
- /backend/save.php (Save drafts to local file/Airtable)
- /css/styles.css (Shared styling)
- /js/app.js (Main logic: calculate, inject, generate PDF)

## Environment Variables (in cPanel)
- OPENROUTER_API_KEY
- DRAFT_SAVE_PATH (optional)

## Dependencies (via CDN)
- @pdfmake/app (PDF generation)
- No Node.js build required
```

This architecture is **production-ready** for a solo entrepreneur. It's private (API key server-side), reliable (deterministic math), and maintainable (fixed HTML template). Build it on your subdomain and you'll have a functioning invoice generator in 1-2 days.

---

**[USER]**

That review confirms the general architecture, but do not use its sample code as-is. Several parts are incorrect or unnecessarily complicated.

What it got right

The correct system is:

> Conversational text → PHP AI parser → validated JSON → editable review → deterministic calculations → fixed invoice PDF → direct download



The right stack is still:

HTML

CSS

JavaScript

PHP

OpenRouter for text interpretation

Client-side PDF generation

One fixed invoice layout


No React, Ruby, database, cloud storage, OCR, or native Android application is necessary.

Corrections that matter

1. The OpenRouter PHP example is wrong

OpenRouter uses:

Authorization: Bearer YOUR_API_KEY

—not:

Authorization: API-Key YOUR_API_KEY

The response text is normally found under:

$result['choices'][0]['message']['content']

—not:

$jsonOutput['content'][0]['text']

OpenRouter also supports structured outputs using JSON Schema, which is preferable to merely telling the model to “return JSON.” 

2. pdfmake is not HTML-to-PDF

pdfmake generates documents from its own JavaScript document-definition structure. It does not take your finished invoice HTML and automatically reproduce it as a PDF. 

This matters because the review mixes two different strategies:

Building a PDF programmatically with pdfmake

Converting rendered HTML into a PDF


Those are not the same architecture.

3. Do not use three separate HTML pages

The app should be one page with three views:

Input
Review
Preview

JavaScript can hide and show each section. That avoids passing invoice data between pages and makes mobile use faster.

4. Do not add save.php yet

You said you want direct PDF output and no cloud functionality. Therefore, do not add server-side draft storage.

Use:

localStorage

for a simple current draft, or:

IndexedDB

only if the draft data becomes larger or more complex.

5. Do not use absolute CSS positioning for the entire invoice

Absolute positioning is suitable for a few fixed header fields, but line-item tables need normal document flow.

A better invoice layout uses:

CSS Grid for the header

A real table for work entries

Flexbox or Grid for totals

Fixed letter-page dimensions

Controlled page breaks


This allows the number of invoice entries to vary without overlapping the total section.

6. window.print() is not a dependable PDF generator

window.print() opens Android or desktop print controls, but browser print settings, margins, headers, and scaling can vary.

It may be acceptable as a temporary prototype, but it is not the best final export workflow.

Best PDF method for this app

Use pdfmake directly, not HTML conversion.

Why:

It supports browser-side PDF generation.

It supports tables, columns, images, styling, wrapping, and downloads.

It works in Android Chrome.

It creates structured text rather than merely taking a screenshot of the invoice.

It handles variable line-item rows more predictably. 


The web preview can use HTML and CSS, while the PDF uses an equivalent pdfmake document definition.

That technically creates two renderers, but for a simple fixed invoice, this is manageable and more dependable than browser HTML capture.

Final architecture

invoice.yourdomain.com/
│
├── index.html
├── css/
│   └── styles.css
├── js/
│   ├── app.js
│   ├── invoice-parser.js
│   ├── calculations.js
│   └── pdf-generator.js
├── api/
│   ├── parse-invoice.php
│   └── config.php
├── vendor/
│   ├── pdfmake.min.js
│   └── vfs_fonts.js
└── .htaccess

Exact responsibility of each part

Browser

The browser handles:

Conversational input

Review and corrections

Financial calculations

Invoice preview

PDF construction

PDF download

Temporary local draft storage


PHP

PHP handles only:

Receiving invoice instructions

Authenticating the request

Sending the text to OpenRouter

Enforcing the JSON response schema

Validating the returned structure

Returning clean JSON to the browser


AI

The AI handles only:

Recognizing the client

Interpreting dates

Separating work entries

Identifying hours and rates

Identifying expenses

Extracting invoice terms

Identifying missing or ambiguous information


The AI must not:

Calculate totals

Generate the PDF

Choose invoice field positions

Save files

Invent missing rates or hours


Corrected core workflow

1. Paste conversational invoice information.


2. Press Process Invoice.


3. PHP sends the text to OpenRouter.


4. OpenRouter returns JSON matching a strict schema.


5. PHP validates and sanitizes the JSON.


6. The browser shows every extracted field.


7. You correct anything necessary.


8. JavaScript calculates line totals, expenses, subtotal, and total.


9. The app displays the finished invoice preview.


10. pdfmake generates the final PDF.


11. The browser downloads it directly.



Recommendation

Proceed with:

> Single-page HTML/CSS/JavaScript frontend + minimal PHP parsing endpoint + OpenRouter structured output + pdfmake PDF generation.



That is the smallest architecture that still gives you genuinely conversational entry and dependable invoice output.

---

**[ASSISTANT]**

Perfect—this is a much clearer and more accurate architecture. I'll build out the **corrected implementation** with all your corrections applied.

## Final Corrected Architecture

```
invoice.yourdomain.com/
├── index.html (single page, 3 views)
├── css/styles.css
├── js/
│   ├── app.js (main flow)
│   ├── invoice-parser.js (schema definition)
│   ├── calculations.js (deterministic math)
│   └── pdf-generator.js (pdfmake)
├── api/
│   ├── parse-invoice.php (OpenRouter with JSON Schema)
│   └── config.php (API key only)
├── vendor/
│   ├── pdfmake.min.js
│   └── vfs_fonts.js
```

Let me create the complete, working implementation: