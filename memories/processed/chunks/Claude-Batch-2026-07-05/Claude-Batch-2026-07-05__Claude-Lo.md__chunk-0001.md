---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Lo.md__chunk-0001",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Lo.md",
  "chunk_index": 1,
  "chunk_count_for_source": 1,
  "char_start": 0,
  "char_end": 11147,
  "source_sha256": "4bc1d4c372560749d97b7f32f6cc0536d8b3fd6591b222e062b3c0cc3ef506e9",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

Original URL: https://claude.ai/chat/a0535007-aad0-49c5-b0e0-83d96f9ccc70
Conversation Time: 6/13/2026, 9:42:32 AM
Export Time: 7/5/2026, 4:49:51 PM

**[USER]**



---

**[ASSISTANT]**

Looks like this message came in with a technical document about a PHP/JavaScript invoice app architecture — not exactly a rigging angle or crew blueprint content drop.

What are you working on? A few possibilities:

- **Wrong chat** — you meant to paste this somewhere else
- **Deadhang Labor invoicing** — you want to build a conversational invoice tool for your 1099 work
- **Something else entirely** — let me know

What's the move?

---

**[USER]**

Build the 1099 invoicing tool please. Your my cleanest coder/writer

---

**[ASSISTANT]**

Let me read the skill files and architecture doc before writing a single line.     1	---
     2	name: frontend-design
     3	description: Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defaults.
     4	license: Complete terms in LICENSE.txt
     5	---
     6	
     7	# Frontend Design
     8	
     9	Approach this as the design lead at a small studio known for giving every client a visual identity that could not be mistaken for anyone else's. This client has already rejected proposals that felt templated, and is paying for a distinctive point of view: make deliberate, opinionated choices about palette, typography, and layout that are specific to this brief, and take one real aesthetic risk you can justify.
    10	
    11	## Ground it in the subject
    12	
    13	If the brief does not pin down what the product or subject is, pin it yourself before designing: name one concrete subject, its audience, and the page's single job, and state your choice. If there's any information in your memory about the human's preferences, context about what they're building, or designs you've made before – use that as a hint. The subject's own world, its materials, instruments, artifacts, and vernacular, is where distinctive choices come from. Build with the brief's real content and subject matter throughout.
    14	
    15	## Design principles
    16	
    17	For web designs, the hero is a thesis. Open with the most characteristic thing in the subject's world, in whatever form makes sense for it: a headline, an image, an animation, a live demo, an interactive moment. Be deliberate with your choice: a big number with a small label, supporting stats, and a gradient accent is the template answer, only use if that's truly the best option.
    18	
    19	Typography carries the personality of the page. Pair the display and body faces deliberately, not the same families you would reach for on any other project, and set a clear type scale with intentional weights, widths, and spacing. Make the type treatment itself a memorable part of the design, not a neutral delivery vehicle for the content.
    20	
    21	Structure is information. Structural devices, numbering, eyebrows, dividers, labels, should encode something true about the content, not decorate it. Many generic designs use numbered markers (01 / 02 / 03), but that's only appropriate if the content actually is a sequence - like a real process or a typed timeline where order carries information the reader needs. Question if choices like numbered markers actually make sense before incorporating them.
    22	
    23	Leverage motion deliberately. Think about where and if animation can serve the subject: a page-load sequence, a scroll-triggered reveal, hover micro-interactions, ambient atmosphere. An orchestrated moment usually lands harder than scattered effects; choose what the direction calls for. However, sometimes less is more, and extra animation contributes to the feeling that the design is AI-generated.
    24	
    25	Match complexity to the vision. Maximalist directions need elaborate execution; minimal directions need precision in spacing, type, and detail. Elegance is executing the chosen vision well.
    26	
    27	Consider written content carefully. Often a design brief may not contain real content, and it's up to you to come up with copy. Copy can make a design feel as templated as the design itself. See the below section on writing for more guidance.
    28	
    29	## Process: brainstorm, explore, plan, critique, build, critique again
    30	
    31	For calibration: AI-generated design right now clusters around three looks: (1) a warm cream background (near #F4F1EA) with a high-contrast serif display and a terracotta accent; (2) a near-black background with a single bright acid-green or vermilion accent; (3) a broadsheet-style layout with hairline rules, zero border-radius, and dense newspaper-like columns. All three are legitimate for some briefs, but they are defaults rather than choices, and they appear regardless of subject. Where the brief pins down a visual direction, follow it exactly — the brief's own words always win, including when it asks for one of these looks. Where it leaves an axis free, don't spend that freedom on one of these defaults. Just like a human designer who's hired, there's often a careful balance between doing what you're good at and taking each project as a chance to experiment and learn.
    32	
    33	Work in two passes. First, brainstorm a short design plan based on the human's design brief: create a compact token system with color, type, layout, and signature. Color: describe the palette as 4–6 named hex values. Type: the typefaces for 2+ roles (a characterful display face that's used with restraint, a complementary body face, and a utility face for captions or data if needed). Layout: a layout concept, using one-sentence prose descriptions and ASCII wireframes to ideate and compare. Signature: the single unique element this page will be remembered by that embodies the brief in an appropriate way.
    34	
    35	Then review that plan against the brief before building: if any part of it reads like the generic default you would produce for any similar page (work through a similar prompt to see if you arrive somewhere similar) rather than a choice made for this specific brief — revise that part, say what you changed and why. Only after you've confirmed the relative uniqueness of your design plan should you start to write the code, following the revised plan exactly and deriving every color and type decision from it.
    36	
    37	When writing the code, be careful of structuring your CSS selector specificities. It's easy to generate CSS classes that cancel each other out (especially with a type-based selector like .section and a element-based selector like .cta). This can happen often with paddings/margins between sections.
    38	
    39	Try to do a lot of this planning and iteration in your thinking, and only show ideas to the user when you have higher confidence it'll delight them.
    40	
    41	## Restraint and self-critique
    42	
    43	Spend your boldness in one place. Let the signature element be the one memorable thing, keep everything around it quiet and disciplined, and cut any decoration that does not serve the brief. Not taking a risk can be a risk itself! Build to a quality floor without announcing it: responsive down to mobile, visible keyboard focus, reduced motion respected. Critique your own work as you build, taking screenshots if your environment supports it – a picture is worth 1000 tokens. Consider Chanel's advice: before leaving the house, take a look in the mirror and remove one accessory. Human creators have memory and always try to do something new, so if you have a space to quickly jot down notes about what you've tried, it can help you in future passes.
    44	
    45	## More on writing in design
    46	
    47	Words appear in a design for one reason: to make it easier to understand, and therefore easier to use. They are design material, not decoration. Bring the same intentionality to copy that you would bring to spacing and color. Before writing anything, ask what the design needs to say, and how it can best be said to help the person navigate the experience.
    48	
    49	Write from the end user's side of the screen. Name things by what people control and recognize, never by how the system is built. A person manages notifications, not webhook config. Describe what something does in plain terms rather than selling it. Being specific is always better than being clever.
    50	
    51	Use active voice as default. A control should say exactly what happens when it's used: "Save changes," not "Submit." An action keeps the same name through the whole flow, so the button that says "Publish" produces a toast that says "Published." The vocabulary of an interface is the signposting for someone navigating the product. Cohesion and consistency are how people learn their way around.
    52	
    53	Treat failure and emptiness as moments for direction, not mood. Explain what went wrong and how to fix it, in the interface's voice rather than a person's. Errors don't apologize, and they are never vague about what happened. An empty screen is an invitation to act.
    54	
    55	Keep the register conversational and tuned: plain verbs, sentence case, no filler, with tone matched to the brand and the audience. Let each element do exactly one job. A label labels, an example demonstrates, and nothing quietly does double duty.
    56	Now let me build this. Based on the architecture doc, I know exactly what to make: single HTML file, three views, pdfmake for PDF, and a clean dark-theme UI that matches the Deadhang Labor brand (navy/gold).{"returncode":0,"stdout":"exists\n","stderr":""}File created successfully: /mnt/user-data/outputs/deadhang-invoice.htmlHere's your full standalone invoice tool. Everything runs in a single HTML file — drop it anywhere, no server needed except for the AI parse step.

---

**What it does:**

**Step 1 — Describe the gig** in plain language (or hit the hint chips for common gig types). Paste your OpenRouter key once and it saves locally. Hit "Parse with AI →" and it sends your text to GPT-4o-mini via OpenRouter, extracting client, dates, hours, rates, mileage, and expenses into structured JSON. No API key? Hit "Fill manually instead."

**Step 2 — Review everything.** Every parsed field is editable. Add/remove work entries and expense lines. Totals calculate in real time, deterministically — the AI never touches math. Draft auto-saves to localStorage so you don't lose work.

**Step 3 — Preview + Download.** Clean invoice preview with your Deadhang navy/gold branding. Hit "⬇ Download PDF" and pdfmake generates a proper structured PDF (not a browser print screenshot) that downloads directly.

---

**Setup notes:**
- Get a free OpenRouter key at `openrouter.ai` — GPT-4o-mini costs pennies per invoice
- Your API key saves in your browser's localStorage, never leaves your device except to OpenRouter
- Mileage auto-calculates at the 2024 IRS rate ($0.67/mi) when you mention miles in your description
- Invoice numbers auto-increment per browser session
- Works on mobile Chrome
