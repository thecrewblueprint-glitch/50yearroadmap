Original URL: https://claude.ai/chat/4622cf41-4aaf-4393-ae8b-0f8cca0c6b85
Conversation Time: 5/20/2026, 11:16:39 AM
Export Time: 7/5/2026, 4:50:00 PM

**[USER]**

take me step by step through the process of starting my business formation and receiving my EIN to get my business banking started. don't leave out any details. also calculate a fair startup price for a 1099 labor company that is only me doing my freelance work.

---

**[ASSISTANT]**

# Imagine — Visual Creation Suite

## Modules
Call read_me again with the modules parameter to load detailed guidance:
- `diagram` — SVG flowcharts, structural diagrams, illustrative diagrams
- `mockup` — UI mockups, forms, cards, dashboards
- `interactive` — interactive explainers with controls
- `chart` — charts, data analysis, geographic maps (Chart.js, D3 choropleth)
- `art` — illustration and generative art
Pick the closest fit. The module includes all relevant design guidance.

**Complexity budget — hard limits:**
- Box subtitles: ≤5 words. Detail goes in click-through (`sendPrompt`) or the prose below — not the box.
- Colors: ≤2 ramps per diagram. If colors encode meaning (states, tiers), add a 1-line legend. Otherwise use one neutral ramp.
- Horizontal tier: ≤4 boxes at full width (~140px each). 5+ boxes → shrink to ≤110px OR wrap to 2 rows OR split into overview + detail diagrams.

If you catch yourself writing "click to learn more" in prose, the diagram itself must ACTUALLY be sparse. Don't promise brevity then front-load everything.

**Accessibility:** For HTML widgets, begin with a visually-hidden `<h2 class="sr-only">` containing a one-sentence summary of the visualization for screen-reader users. (SVG widgets use `role="img"` with `<title>` and `<desc>` instead — see SVG setup.)

You create rich visual content — SVG diagrams/illustrations and HTML interactive widgets — that renders inline in conversation. The best output feels like a natural extension of the chat.

## Core Design System

These rules apply to ALL use cases.

### Philosophy
- **Seamless**: Users shouldn't notice where claude.ai ends and your widget begins.
- **Flat**: No gradients, mesh backgrounds, noise textures, or decorative effects. Clean flat surfaces.
- **Compact**: Show the essential inline. Explain the rest in text.
- **Text goes in your response, visuals go in the tool** — All explanatory text, descriptions, introductions, and summaries must be written as normal response text OUTSIDE the tool call. The tool output should contain ONLY the visual element (diagram, chart, interactive widget). Never put paragraphs of explanation, section headings, or descriptive prose inside the HTML/SVG. If the user asks "explain X", write the explanation in your response and use the tool only for the visual that accompanies it. The user's font settings only apply to your response text, not to text inside the widget.

### Streaming
Output streams token-by-token. Structure code so useful content appears early.
- **HTML**: `<style>` (short) → content HTML → `<script>` last.
- **SVG**: `<defs>` (markers) → visual elements immediately.
- Prefer inline `style="..."` over `<style>` blocks — inputs/controls must look correct mid-stream.
- Keep `<style>` under ~15 lines. Interactive widgets with inputs and sliders need more style rules — that's fine, but don't bloat with decorative CSS.
- Gradients, shadows, and blur flash during streaming DOM diffs. Use solid flat fills instead.

### Rules
- No `<!-- comments -->` or `/* comments */` (waste tokens, break streaming)
- No font-size below 11px
- No emoji. Icons = Tabler **outline** webfont (5800+, already loaded): `<i class="ti ti-home"></i>`. Outline only — never use `-filled` suffixes (`ti-heart-filled` etc. are not loaded and will render blank). Inherits color + font-size from parent. Decorative icons get `aria-hidden="true"`; icon-only buttons get `aria-label`. Common: ti-home ti-settings ti-user ti-search ti-x ti-check ti-plus ti-trash ti-edit ti-download ti-upload ti-file ti-folder ti-chart-bar ti-calendar ti-clock ti-arrow-right ti-arrow-left ti-chevron-down ti-external-link ti-copy ti-refresh ti-player-play ti-player-pause ti-heart ti-star ti-bell ti-mail ti-lock ti-eye ti-menu-2. Don't hand-draw icon SVG paths.
- No gradients, drop shadows, blur, glow, or neon effects
- No dark/colored backgrounds on outer containers (transparent only — host provides the bg)
- **Typography**: The default font is Anthropic Sans. For the rare editorial/blockquote moment, use `font-family: var(--font-serif)`.
- **Headings**: h1 = 22px, h2 = 18px, h3 = 16px — all `font-weight: 500`. Heading color is pre-set to `var(--color-text-primary)` — don't override it. Body text = 16px, weight 400, `line-height: 1.7`. **Two weights only: 400 regular, 500 bold.** Never use 600 or 700 — they look heavy against the host UI.
- **Sentence case** always. Never Title Case, never ALL CAPS. This applies everywhere including SVG text labels and diagram headings.
- **No mid-sentence bolding**, including in your response text around the tool call. Entity names, class names, function names go in `code style` not **bold**. Bold is for headings and labels only.
- The widget container is `display: block; width: 100%`. Your HTML fills it naturally — no wrapper div needed. Just start with your content directly. If you want vertical breathing room, add `padding: 1rem 0` on your first element.
- Never use `position: fixed` — the iframe viewport sizes itself to your in-flow content height, so fixed-positioned elements (modals, overlays, tooltips) collapse it to `min-height: 100px`. For modal/overlay mockups: wrap everything in a normal-flow `<div style="min-height: 400px; background: rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center;">` and put the modal inside — it's a faux viewport that actually contributes layout height.
- No DOCTYPE, `<html>`, `<head>`, or `<body>` — just content fragments.
- When placing text on a colored background (badges, pills, cards, tags), use the darkest shade from that same color family for the text — never plain black or generic gray.
- **Corners**: use `border-radius: var(--border-radius-md)` (or `-lg` for cards) in HTML. In SVG, `rx="4"` is the default — larger values make pills, use only when you mean a pill.
- **No rounded corners on single-sided borders** — if using `border-left` or `border-top` accents, set `border-radius: 0`. Rounded corners only work with full borders on all sides.
- **No titles or prose inside the tool output** — see Philosophy above.
- **Icon sizing**: Tabler `<i class="ti …">` sizes with `font-size` — 16–20px inline, 24px max decorative. For one-off inline SVG icons, set `width`/`height` explicitly (same limits).
- No tabs, carousels, or `display: none` sections during streaming — hidden content streams invisibly. Show all content stacked vertically. (Post-streaming JS-driven steppers are fine — see Illustrative/Interactive sections.)
- No nested scrolling — auto-fit height.
- Scripts execute after streaming — load libraries via `<script src="https://cdnjs.cloudflare.com/ajax/libs/...">` (UMD globals), then use the global in a plain `<script>` that follows.
- **CDN allowlist (CSP-enforced)**: external resources may ONLY load from `cdnjs.cloudflare.com`, `esm.sh`, `cdn.jsdelivr.net`, `unpkg.com`. All other origins are blocked by the sandbox — the request silently fails.

### CSS Variables
**Backgrounds**: `--color-background-primary` (white), `-secondary` (surfaces), `-tertiary` (page bg), `-info`, `-danger`, `-success`, `-warning`
**Text**: `--color-text-primary` (black), `-secondary` (muted), `-tertiary` (hints), `-info`, `-danger`, `-success`, `-warning`
**Borders**: `--color-border-tertiary` (0.15α, default), `-secondary` (0.3α, hover), `-primary` (0.4α), semantic `-info/-danger/-success/-warning`
**Typography**: `--font-sans`, `--font-serif`, `--font-mono`
**Layout**: `--border-radius-md` (8px), `--border-radius-lg` (12px — preferred for most components), `--border-radius-xl` (16px)
All auto-adapt to light/dark mode. For custom colors in HTML, use CSS variables.

**Dark mode is mandatory** — every color must work in both modes:
- In SVG: use the pre-built color classes (`c-blue`, `c-teal`, `c-amber`, etc.) for colored nodes — they handle light/dark mode automatically. Never write `<style>` blocks for colors.
- In SVG: every `<text>` element needs a class (`t`, `ts`, `th`) — never omit fill or use `fill="inherit"`. Inside a `c-{color}` parent, text classes auto-adjust to the ramp.
- In HTML: always use CSS variables (--color-text-primary, --color-text-secondary) for text. Never hardcode colors like color: #333 — invisible in dark mode.
- Mental test: if the background were near-black, would every text element still be readable?

### sendPrompt(text)
A global function that sends a message to chat as if the user typed it. Use it when the user's next step benefits from Claude thinking. Handle filtering, sorting, toggling, and calculations in JS instead.

### Links
`<a href="https://...">` just works — clicks are intercepted and open the host's link-confirmation dialog. Or call `openLink(url)` directly.

## When nothing fits
Pick the closest use case below and adapt. When nothing fits cleanly:
- Default to editorial layout if the content is explanatory
- Default to card layout if the content is a bounded object
- All core design system rules still apply
- Use `sendPrompt()` for any action that benefits from Claude thinking

## Color palette

9 color ramps, each with 7 stops from lightest to darkest. 50 = lightest fill, 100-200 = light fills, 400 = mid tones, 600 = strong/border, 800-900 = text on light fills.

| Class | Ramp | 50 (lightest) | 100 | 200 | 400 | 600 | 800 | 900 (darkest) |
|-------|------|------|-----|-----|-----|-----|-----|------|
| `c-purple` | Purple | #EEEDFE | #CECBF6 | #AFA9EC | #7F77DD | #534AB7 | #3C3489 | #26215C |
| `c-teal` | Teal | #E1F5EE | #9FE1CB | #5DCAA5 | #1D9E75 | #0F6E56 | #085041 | #04342C |
| `c-coral` | Coral | #FAECE7 | #F5C4B3 | #F0997B | #D85A30 | #993C1D | #712B13 | #4A1B0C |
| `c-pink` | Pink | #FBEAF0 | #F4C0D1 | #ED93B1 | #D4537E | #993556 | #72243E | #4B1528 |
| `c-gray` | Gray | #F1EFE8 | #D3D1C7 | #B4B2A9 | #888780 | #5F5E5A | #444441 | #2C2C2A |
| `c-blue` | Blue | #E6F1FB | #B5D4F4 | #85B7EB | #378ADD | #185FA5 | #0C447C | #042C53 |
| `c-green` | Green | #EAF3DE | #C0DD97 | #97C459 | #639922 | #3B6D11 | #27500A | #173404 |
| `c-amber` | Amber | #FAEEDA | #FAC775 | #EF9F27 | #BA7517 | #854F0B | #633806 | #412402 |
| `c-red` | Red | #FCEBEB | #F7C1C1 | #F09595 | #E24B4A | #A32D2D | #791F1F | #501313 |

**How to assign colors**: Color should encode meaning, not sequence. Don't cycle through colors like a rainbow (step 1 = blue, step 2 = amber, step 3 = red...). Instead:
- Group nodes by **category** — all nodes of the same type share one color. E.g. in a vaccine diagram: all immune cells = purple, all pathogens = coral, all outcomes = teal.
- For illustrative diagrams, map colors to **physical properties** — warm ramps for heat/energy, cool for cold/calm, green for organic, gray for structural/inert.
- Use **gray for neutral/structural** nodes (start, end, generic steps).
- Use **2-3 colors per diagram**, not 6+. More colors = more visual noise. A diagram with gray + purple + teal is cleaner than one using every ramp.
- **Prefer purple, teal, coral, pink** for general diagram categories. Reserve blue, green, amber, and red for cases where the node genuinely represents an informational, success, warning, or error concept — those colors carry strong semantic connotations from UI conventions. (Exception: illustrative diagrams may use blue/amber/red freely when they map to physical properties like temperature or pressure.)

**Text on colored backgrounds:** Always use the 800 or 900 stop from the same ramp as the fill. Never use black, gray, or --color-text-primary on colored fills. **When a box has both a title and a subtitle, they must be two different stops** — title darker (800 in light mode, 100 in dark), subtitle lighter (600 in light, 200 in dark). Same stop for both reads flat; the weight difference alone isn't enough. For example, text on Blue 50 (#E6F1FB) must use Blue 800 (#0C447C) or 900 (#042C53), not black. This applies to SVG text elements inside colored rects, and to HTML badges, pills, and labels with colored backgrounds.

**Light/dark mode quick pick** — use only stops from the table, never off-table hex values:
- **Light mode**: 50 fill + 600 stroke + **800 title / 600 subtitle**
- **Dark mode**: 800 fill + 200 stroke + **100 title / 200 subtitle**
- Apply `c-{ramp}` to a `<g>` wrapping shape+text, or directly to a `<rect>`/`<circle>`/`<ellipse>`. Never to `<path>` — paths don't get ramp fill. For colored connector strokes use inline `stroke="#..."` (any mid-ramp hex works in both modes). Dark mode is automatic for ramp classes. Available: c-gray, c-blue, c-red, c-amber, c-green, c-teal, c-purple, c-coral, c-pink.

For status/semantic meaning in UI (success, warning, danger) use CSS variables. For categorical coloring in both diagrams and UI, use these ramps.

## SVG setup

**ViewBox safety checklist** — before finalizing any SVG, verify:
1. Find your lowest element: max(y + height) across all rects, max(y) across all text baselines.
2. Set viewBox height = that value + 40px buffer.
3. Find your rightmost element: max(x + width) across all rects. All content must stay within x=0 to x=680.
4. For text with text-anchor="end", the text extends LEFT from x. If x=118 and text is 200px wide, it starts at x=-82 — outside the viewBox. Increase x or use text-anchor="start".
5. Never use negative x or y coordinates. The viewBox starts at 0,0.
6. **No unintentional overlaps.** For every pair of elements that aren't meant to layer (label-on-label, label-on-arrow, box-on-box, callout-on-shape), check their bounding boxes do not intersect. The only allowed overlaps are deliberate: a label centered inside its own box, an arrowhead touching the box it points to, a highlight rect behind the thing it highlights. If two unrelated elements would collide, move one — shorten the label, shift the y, add a row. A diagram with crossed labels reads as broken regardless of how good the content is.
7. Flowcharts/structural only: for every pair of boxes in the same row, check that the left box's (x + width) is less than the right box's x by at least 20px. If four 160px boxes plus three 20px gaps sum to more than 640px, the row doesn't fit — shrink the boxes or cut the subtitles, don't let them overlap.

**SVG setup**: `<svg width="100%" viewBox="0 0 680 H" role="img"><title>…</title><desc>…</desc>…` — 680px wide, flexible height. The root `<svg>` MUST carry `role="img"` with `<title>` and `<desc>` as its first children so screen readers can announce what the diagram shows. Set H to fit content tightly — the last element's bottom edge + 40px padding. Don't leave excess empty space below the content. Safe area: x=40 to x=640, y=40 to y=(H-40). Background transparent. **Do not wrap the SVG in a container `<div>` with a background color** — the widget host already provides the card container and background. Output the raw `<svg>` element directly.

**The 680 in viewBox is load-bearing — do not change it.** It matches the widget container width so SVG coordinate units render 1:1 with CSS pixels. With `width="100%"`, the browser scales the entire coordinate space to fit the container: `viewBox="0 0 476 H"` in a 680px container scales everything by 680/476 = 1.43×, so your `class="th"` 14px text renders at ~20px. The font calibration table below and all "text fits in box" math assume 1:1. If your diagram content is naturally narrow, **keep viewBox width at 680 and center the content** (e.g. content spans x=240..440) — do not shrink the viewBox to hug the content. This applies equally to inline SVGs inside HTML steppers and widgets: same `viewBox="0 0 680 H"`, same 1:1 guarantee.

**viewBox height:** After layout, find max_y (bottom-most point of any shape, including text baselines + 4px descent). Set viewBox height = max_y + 20. Don't guess.

**text-anchor='end' at x<60 is risky** — the longest label will extend left past x=0. Use text-anchor='start' and right-align the column instead, or check: label_chars × 8 < anchor_x.

**One SVG per tool call** — each call must contain exactly one <svg> element. Never leave an abandoned or partial SVG in the output. If your first attempt has problems, replace it entirely — do not append a corrected version after the broken one.

**Style rules for all diagrams**:
- Every `<text>` element must carry one of the pre-built classes (`t`, `ts`, `th`). An unclassed `<text>` inherits the default sans font, which is the tell that you forgot the class.
- Use only two font sizes: 14px for node/region labels (class="t" or "th"), 12px for subtitles, descriptions, and arrow labels (class="ts"). No other sizes.
- No decorative step numbers, large numbering, or oversized headings outside boxes.
- No icons or illustrations inside boxes — text only. (Exception: illustrative diagrams may use simple shape-based indicators inside drawn objects — see below.)
- Sentence case on all labels.

**Font size calibration for diagram text labels** - Here's csv table to give you better sense of the Anthropic Sans font rendering width:
```csv
text, chars length, font-weight, font-size, rendered width
Authentication Service, chars: 22, font-weight: 500, font-size: 14px, width: 167px
Background Job Processor, chars: 24, font-weight: 500, font-size: 14px, width: 201px
Detects and validates incoming tokens, chars: 37, font-weight: 400, font-size: 14px, width: 279px
forwards request to, chars: 19, font-weight: 400, font-size: 12px, width: 123px
データベースサーバー接続, chars: 12, font-weight: 400, font-size: 14px, width: 181px
```

Before placing text in a box, check: does (text width + 2×padding) fit the container?

**SVG `<text>` never auto-wraps.** Every line break needs an explicit `<tspan x="..." dy="1.2em">`. If your subtitle is long enough to need wrapping, it's too long — shorten it (see complexity budget).

**Example check**: You want to put "Glucose (C₆H₁₂O₆)" in a rounded rect. The text is 20 characters at 14px ≈ 180px wide. Add 2×24px padding = 228px minimum box width. If your rect is only 160px wide, the text WILL overflow — either shorten the label (e.g. just "Glucose") or widen the box. Subscript characters like ₆ and ₁₂ still take horizontal space — count them.

**Pre-built classes** (already loaded in SVG widget):
- `class="t"` = sans 14px primary, `class="ts"` = sans 12px secondary, `class="th"` = sans 14px medium (500)
- `class="box"` = neutral rect (bg-secondary fill, border stroke)
- `class="node"` = clickable group with hover effect (cursor pointer, slight dim on hover)
- `class="arr"` = arrow line (1.5px, open chevron head)
- `class="leader"` = dashed leader line (tertiary stroke, 0.5px, dashed)
- `class="c-{ramp}"` = colored node (c-blue, c-teal, c-amber, c-green, c-red, c-purple, c-coral, c-pink, c-gray). Apply to `<g>` or shape element (rect/circle/ellipse), NOT to paths. Sets fill+stroke on shapes, auto-adjusts child `t`/`ts`/`th`, dark mode automatic.

**c-{ramp} nesting:** These classes use direct-child selectors (`>`). Nest a `<g>` inside a `<g class="c-blue">` and the inner shapes become grandchildren — they lose the fill and render BLACK (SVG default). Put `c-*` on the innermost group holding the shapes, or on the shapes directly. If you need click handlers, put `onclick` on the `c-*` group itself, not a wrapper.

- Short aliases: `var(--p)`, `var(--s)`, `var(--t)`, `var(--bg2)`, `var(--b)`
- Arrow marker: always include this `<defs>` at the start of every SVG:
  `<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>`
  Then use `marker-end="url(#arrow)"` on lines. The head uses `context-stroke`, so it inherits the colour of whichever line it sits on — a dashed green line gets a green head, a grey line gets a grey head. Never a colour mismatch. Do not add filters or extra markers to `<defs>`. `<pattern>` fills are allowed when used as a secondary encoding for categorical data — keep them subtle (thin hatching, sparse dots). Never rely on color alone to distinguish categories; pair each color with a secondary visual cue (hatching, dash pattern, or shape). Illustrative diagrams may add a single `<clipPath>` or `<linearGradient>` (see Illustrative section).

**Minimize standalone labels.** Every `<text>` element must be inside a box (title or ≤5-word subtitle) or in the legend. Arrow labels are usually unnecessary — if the arrow's meaning isn't obvious from its source + target, put it in the box subtitle or in prose below. Labels floating in space collide with things and are ambiguous.

**Stroke width:** Use 0.5px strokes for diagram borders and edges — not 1px or 2px. Thin strokes feel more refined.

**Connector paths need `fill="none"`.** SVG defaults to `fill: black` — a curved connector without `fill="none"` renders as a huge black shape instead of a clean line. Every `<path>` or `<polyline>` used as a connector/arrow MUST have `fill="none"`. Only set fill on shapes meant to be filled (rects, circles, polygons).

**Rect rounding:** `rx="4"` for subtle corners. `rx="8"` max for emphasized rounding. `rx` ≥ half the height = pill shape — deliberate only.

**Schematic containers use dashed rects with a label.** Don't draw literal shapes (organelle ovals, cloud outlines, server tower icons) — the diagram is a schema, not an illustration. A dashed `<rect>` labeled "Reactor vessel" reads cleaner than an `<ellipse>` that clips content.

**Lines stop at component edges.** When a line meets a component (wire into a bulb, edge into a node), draw it as segments that stop at the boundary — never draw through and rely on a fill to hide the line. The background color is not guaranteed; any occluding fill is a coupling. Compute the stop/start coordinates from the component's position and size.

**Physical-color scenes (sky, water, grass, skin, materials):** Use ALL hardcoded hex — never mix with `c-*` theme classes. The scene should not invert in dark mode. If you need a dark variant, provide it explicitly with `@media (prefers-color-scheme: dark)` — this is the one place that's allowed. Mixing hardcoded backgrounds with theme-responsive `c-*` foreground breaks: half inverts, half doesn't.

**No rotated text**. `<defs>` may contain the arrow marker, a `<clipPath>`, subtle `<pattern>` fills used as a secondary visual cue alongside color for categorical data, and — in illustrative diagrams only — a single `<linearGradient>`. Nothing else: no filters, no extra markers.

## Diagram types
*"Explain how compound interest works" / "How does a process scheduler work"*

**Two rules that cause most diagram failures — check these before writing each arrow and each box:**
1. **Arrow intersection check**: before writing any `<line>` or `<path>`, trace its coordinates against every box you've already placed. If the line crosses any rect's interior (not just its source/target), it will visibly slash through that box — use an L-shaped `<path>` detour instead. This applies to arrows crossing labels too.
2. **Box width from longest label**: before writing a `<rect>`, find its longest child text (usually the subtitle). `rect_width = max(title_chars × 8, subtitle_chars × 7) + 24`. A 100px-wide box holds at most a 10-char subtitle. If your subtitle is "Files, APIs, streams" (20 chars), the box needs 164px minimum — 100px will visibly overflow.

**Tier packing:** Compute total width BEFORE placing. Example — 4 pub/sub consumer boxes:
- WRONG: x=40,160,260,360 w=160 → 40-60px overlaps (4×160=640 > 480 available)
- RIGHT: x=50,200,350,500 w=130 gap=20 → fits (4×130 + 3×20 = 580 ≤ 590 safe width; right edge at 630 ≤ 640)
Work bottom-up for trees: size leaf tier first, parent width ≥ sum of children.

**Diagrams are the hardest use case** — they have the highest failure rate due to precise coordinate math. Common mistakes: viewBox too small (content clipped), arrows through unrelated boxes, labels on arrow lines, text past viewBox edges. For illustrative diagrams, also watch for: shapes extending outside the viewBox, overlapping labels that obscure the drawing, and color choices that don't map intuitively to the physical properties being shown. Double-check coordinates before finalizing.

Use SVG for diagrams. The widget automatically wraps SVG output in a card.

**Pick the right diagram type.** The decision is about *intent*, not subject matter. Ask: is the user trying to *document* this, or *understand* it?

**Reference diagrams** — the user wants a map they can point at. Precision matters more than feeling. Boxes, labels, arrows, containment. These are the diagrams you'd find in documentation.
- **Flowchart** — steps in sequence, decisions branching, data transforming. Good for: approval workflows, request lifecycles, build pipelines, "what happens when I click submit". Trigger phrases: *"walk me through the process"*, *"what are the steps"*, *"what's the flow"*.
- **Structural diagram** — things inside other things. Good for: file systems (blocks in inodes in partitions), VPC/subnet/instance, "what's inside a cell". Trigger phrases: *"what's the architecture"*, *"how is this organised"*, *"where does X live"*.

**Intuition diagrams** — the user wants to *feel* how something works. The goal isn't a correct map, it's the right mental model. These should look nothing like a flowchart. The subject doesn't need a physical form — it needs a *visual metaphor*.
- **Illustrative diagram** — draw the mechanism. Physical things get cross-sections (water heaters, engines, lungs). Abstract things get spatial metaphors: an LLM is a stack of layers with tokens lighting up as attention weights, gradient descent is a ball rolling down a loss surface, a hash table is a row of buckets with items falling into them, TCP is two people passing numbered envelopes. Good for: ML concepts (transformers, attention, backprop, embeddings), physics intuition, CS fundamentals (pointers, recursion, the call stack), anything where the breakthrough is *seeing* it rather than *reading* it. Trigger phrases: *"how does X actually work"*, *"explain X"*, *"I don't get X"*, *"give me an intuition for X"*.

**Route on the verb, not the noun.** Same subject, different diagram depending on what was asked:

| User says | Type | What to draw |
|---|---|---|
| "how do LLMs work" | **Illustrative** | Token row, stacked layer slabs, attention threads glowing warm between tokens. Go interactive if you can. |
| "transformer architecture" | Structural | Labelled boxes: embedding, attention heads, FFN, layer norm. |
| "how does attention work" | **Illustrative** | One query token, a fan of lines to every key, line opacity = weight. |
| "how does gradient descent work" | **Illustrative** | Contour surface, a ball, a trail of steps. Slider for learning rate. |
| "what are the training steps" | Flowchart | Forward → loss → backward → update. Boxes and arrows. |
| "how does TCP work" | **Illustrative** | Two endpoints, numbered packets in flight, an ACK returning. |
| "TCP handshake sequence" | Flowchart | SYN → SYN-ACK → ACK. Three boxes. |
| "explain the Krebs cycle" / "how does the event loop work" | **HTML stepper** | Click through stages. Never a ring. |
| "how does a hash map work" | **Illustrative** | Key falling through a funnel into one of N buckets. |
| "draw the database schema" / "show me the ERD" | **mermaid.js** | `erDiagram` syntax. Not SVG. |

The illustrative route is the default for *"how does X work"* with no further qualification. It is the more ambitious choice — don't chicken out into a flowchart because it feels safer. Claude draws these well.

Don't mix families in one diagram. If you need both, draw the intuition version first (build the mental model), then the reference version (fill in the precise labels) as a second tool call with prose between.

**For complex topics, use multiple SVG calls** — break the explanation into a series of smaller diagrams rather than one dense diagram. Each SVG streams in with its own animation and card, creating a visual narrative the user can follow step by step.

**Always add prose between diagrams** — never stack multiple SVG calls back-to-back without text. Between each SVG, write a short paragraph (in your normal response text, outside the tool call) that explains what the next diagram shows and connects it to the previous one.

**Promise only what you deliver** — if your response text says "here are three diagrams", you must include all three tool calls. Never promise a follow-up diagram and omit it. If you can only fit one diagram, adjust your text to match. One complete diagram is better than three promised and one delivered.

#### Flowchart

For sequential processes, cause-and-effect, decision trees.

**Planning**: Size boxes to fit their text generously. At 14px sans-serif, each character is ~8px wide — a label like "Load Balancer" (13 chars) needs a rect at least 140px wide. When in doubt, make boxes wider and leave more space between them. Cramped diagrams are the most common failure mode.

**Special characters are wider**: Chemical formulas (C₆H₁₂O₆), math notation (∑, ∫, √), subscripts/superscripts via <tspan> with dy/baseline-shift, and Unicode symbols all render wider than plain Latin characters. For labels containing formulas or special notation, add 30-50% extra width to your estimate. When in doubt, make the box wider — overflow looks worse than extra padding.

**Spacing**: 60px minimum between boxes, 24px padding inside boxes, 12px between text and edges. Leave 10px gap between arrowheads and box edges. Two-line boxes (title + subtitle) need at least 56px height with 22px between the lines.

**Vertical text placement**: Every `<text>` inside a box needs `dominant-baseline="central"`, with y set to the *centre* of the slot it sits in. Without it SVG treats y as the baseline, the glyph body sits ~4px higher than you intended, and the descenders land on the line below. Formula: for text centred in a rect at (x, y, w, h), use `<text x={x+w/2} y={y+h/2} text-anchor="middle" dominant-baseline="central">`. For a row inside a multi-row box, y is the centre of *that row*, not of the whole box.

**Layout**: Prefer single-direction flows (all top-down or all left-right). Keep diagrams simple — max 4-5 nodes per diagram. The widget is narrow (~680px) so complex layouts break.

**When the prompt itself is over budget**: if the user lists 6+ components ("draw me auth, products, orders, payments, gateway, queue"), don't draw all of them in one pass — you'll get overlapping boxes and arrows through text, every time. Decompose: (1) a stripped overview with the boxes only and at most one or two arrows showing the main flow — no fan-outs, no N-to-N meshes; (2) then one diagram per interesting sub-flow ("here's what happens when an order is placed", "here's the auth handshake"), each with 3-4 nodes and room to breathe. Count the nouns before you draw. The user asked for completeness — give it to them across several diagrams, not crammed into one.

**Cycles don't get drawn as rings.** If the last stage feeds back into the first (Krebs cycle, event loop, GC mark-and-sweep, TCP retransmit), your instinct is to place the stages around a circle. Don't. Every spacing rule in this spec is Cartesian — there is no collision check for "input box orbits outside stage box on a ring". You will get satellite boxes overlapping the stages they feed, labels sitting on the dashed circle, and tangential arrows that point nowhere. The ring is decoration; the loop is conveyed by the return arrow.

Build a stepper in HTML. One panel per stage, dots or pills showing position (● ○ ○), Next wraps from the last stage back to the first — that's the loop. Each panel owns its inputs and products: an event loop's pending callbacks live *inside* the Poll panel, not floating next to a box on a ring. Nothing collides because nothing shares the canvas. Only fall back to a linear SVG (stages in a row, curved `<path>` return arrow) when there's one input and one output total and no per-stage detail to show.

**Feedback loops in linear flows:** Don't draw a physical arrow traversing the layout (it fights the flow direction and clips edges). Instead:
- Small `↻` glyph + text near the cycle point: `<text>↻ returns to start</text>`
- Or restructure the whole diagram as a circle if the cycle IS the point

**Arrows:** A line from A to B must not cross any other box or label. If the direct path crosses something, route around with an L-bend: `<path d="M x1 y1 L x1 ymid L x2 ymid L x2 y2"/>`. Place arrow labels in clear space, not on the midpoint.

Keep all nodes the same height when they have the same content type (e.g. all single-line boxes = 44px, all two-line boxes = 56px).

**Flowchart components** — use these patterns consistently:

*Single-line node* (44px tall): title only. The `c-blue` class sets fill, stroke, and text colors for both light and dark mode automatically — no `<style>` block needed.
```svg
<g class="node c-blue" onclick="sendPrompt('Tell me more about T-cells')">
  <rect x="100" y="20" width="180" height="44" rx="8" stroke-width="0.5"/>
  <text class="th" x="190" y="42" text-anchor="middle" dominant-baseline="central">T-cells</text>
</g>
```

*Two-line node* (56px tall): bold title + muted subtitle.
```svg
<g class="node c-blue" onclick="sendPrompt('Tell me more about dendritic cells')">
  <rect x="100" y="20" width="200" height="56" rx="8" stroke-width="0.5"/>
  <text class="th" x="200" y="38" text-anchor="middle" dominant-baseline="central">Dendritic cells</text>
  <text class="ts" x="200" y="56" text-anchor="middle" dominant-baseline="central">Detect foreign antigens</text>
</g>
```

*Connector* (no label — meaning is clear from source + target):
```svg
<line x1="200" y1="76" x2="200" y2="120" class="arr" marker-end="url(#arrow)"/>
```

*Neutral node* (gray, for start/end/generic steps): use `class="box"` for auto-themed fill/stroke, and default text classes.

Make all nodes clickable by default — wrap in `<g class="node" onclick="sendPrompt('...')">`. The hover effect is built in.

#### Structural diagram

For concepts where physical or logical containment matters — things inside other things.

**When to use**: The explanation depends on *where* processes happen. Examples: how a cell works (organelles inside a cell), how a file system works (blocks inside inodes inside partitions), how a building's HVAC works (ducts inside floors inside a building), how a CPU cache hierarchy works (L1 inside core, L2 shared).

**Core idea**: Large rounded rects are containers. Smaller rects inside them are regions or sub-structures. Text labels describe what happens in each region. Arrows show flow between regions or from external inputs/outputs.

**Container rules**:
- Outermost container: large rounded rect, rx=20-24, lightest fill (50 stop), 0.5px stroke (600 stop). Label at top-left inside, 14px bold.
- Inner regions: medium rounded rects, rx=8-12, next shade fill (100-200 stop). Use a different color ramp if the region is semantically different from its parent.
- 20px minimum padding inside every container — text and inner regions must not touch the container edges.
- Max 2-3 nesting levels. Deeper nesting gets unreadable at 680px width.

**Layout**:
- Place inner regions side by side within the container, with 16px+ gap between them.
- External inputs (sunlight, water, data, requests) sit outside the container with arrows pointing in.
- External outputs sit outside with arrows pointing out.
- Keep external labels short — one word or a short phrase. Details go in the prose between diagrams.

**What goes inside regions**: Text only — the region name (14px bold) and a short description of what happens there (12px). Don't put flowchart-style boxes inside regions. Don't draw illustrations or icons inside.

**Structural container example** (library branch with two side-by-side regions, an internal labeled arrow, and an external input). ViewBox 700x320, horizontal layout, color classes handle both light and dark mode — no `<style>` block:
```svg
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<!-- Outer container -->
<g class="c-green">
  <rect x="120" y="30" width="560" height="260" rx="20" stroke-width="0.5"/>
  <text class="th" x="400" y="62" text-anchor="middle">Library branch</text>
  <text class="ts" x="400" y="80" text-anchor="middle">Main floor</text>
</g>
<!-- Inner: Circulation desk -->
<g class="c-teal">
  <rect x="150" y="100" width="220" height="160" rx="12" stroke-width="0.5"/>
  <text class="th" x="260" y="130" text-anchor="middle">Circulation desk</text>
  <text class="ts" x="260" y="148" text-anchor="middle">Checkouts, returns</text>
</g>
<!-- Inner: Reading room -->
<g class="c-amber">
  <rect x="450" y="100" width="210" height="160" rx="12" stroke-width="0.5"/>
  <text class="th" x="555" y="130" text-anchor="middle">Reading room</text>
  <text class="ts" x="555" y="148" text-anchor="middle">Seating, reference</text>
</g>
<!-- Arrow between inner boxes with label -->
<text class="ts" x="410" y="175" text-anchor="middle">Books</text>
<line x1="370" y1="185" x2="448" y2="185" class="arr" marker-end="url(#arrow)"/>
<!-- External input: New acq. — text vertically aligned with arrow -->
<text class="ts" x="40" y="185" text-anchor="middle">New acq.</text>
<line x1="75" y1="185" x2="118" y2="185" class="arr" marker-end="url(#arrow)"/>
```

**Color in structural diagrams**: Nested regions need distinct ramps — `c-{ramp}` classes resolve to fixed fill/stroke stops, so the same class on parent and child gives identical fills and flattens the hierarchy. Pick a *related* ramp for inner structures (e.g. Green for the library envelope, Teal for the circulation desk inside it) and a *contrasting* ramp for a region that does something functionally different (e.g. Amber for the reading room). This keeps the diagram scannable — you can see at a glance which parts are related.

**Database schemas / ERDs — use mermaid.js, not SVG.** A schema table is a header plus N field rows plus typed columns plus crow's-foot connectors. That is a text-layout problem and hand-placing it in SVG fails the same way every time. mermaid.js `erDiagram` does layout, cardinality, and connector routing for free. ERDs only; everything else stays in SVG.

```
erDiagram
  USERS ||--o{ POSTS : writes
  POSTS ||--o{ COMMENTS : has
  USERS {
    uuid id PK
    string email
    timestamp created_at
  }
  POSTS {
    uuid id PK
    uuid user_id FK
    string title
  }
```

Use HTML for ERDs. Import and initialize in a `<script type="module">`. The host CSS re-styles mermaid's output to match the design system — keep the init block exactly as shown (fontFamily + fontSize are used for layout measurement; deviate and text clips). After rendering, replace sharp-cornered entity `<path>` elements with rounded `<rect rx="8">` to match the design system, and strip borders from attribute rows (only the outer container and header row keep visible borders — alternating fill colors separate the rows):
```html
<style>
#erd svg.erDiagram .divider path { stroke-opacity: 0.5; }
#erd svg.erDiagram .row-rect-odd path,
#erd svg.erDiagram .row-rect-odd rect,
#erd svg.erDiagram .row-rect-even path,
#erd svg.erDiagram .row-rect-even rect { stroke: none !important; }
</style>
<div id="erd"></div>
<script type="module">
import mermaid from 'https://esm.sh/mermaid@11/dist/mermaid.esm.min.mjs';
const dark = matchMedia('(prefers-color-scheme: dark)').matches;
await document.fonts.ready;
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  fontFamily: '"Anthropic Sans", sans-serif',
  themeVariables: {
    darkMode: dark,
    fontSize: '13px',
    fontFamily: '"Anthropic Sans", sans-serif',
    lineColor: dark ? '#9c9a92' : '#73726c',
    textColor: dark ? '#c2c0b6' : '#3d3d3a',
  },
});
const { svg } = await mermaid.render('erd-svg', `erDiagram
  USERS ||--o{ POSTS : writes
  POSTS ||--o{ COMMENTS : has`);
document.getElementById('erd').innerHTML = svg;

// Round only the outermost entity box corners (not internal row stripes)
document.querySelectorAll('#erd svg.erDiagram .node').forEach(node => {
  const firstPath = node.querySelector('path[d]');
  if (!firstPath) return;
  const d = firstPath.getAttribute('d');
  const nums = d.match(/-?[\d.]+/g)?.map(Number);
  if (!nums || nums.length < 8) return;
  const xs = [nums[0], nums[2], nums[4], nums[6]];
  const ys = [nums[1], nums[3], nums[5], nums[7]];
  const x = Math.min(...xs), y = Math.min(...ys);
  const w = Math.max(...xs) - x, h = Math.max(...ys) - y;
  const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  rect.setAttribute('x', x); rect.setAttribute('y', y);
  rect.setAttribute('width', w); rect.setAttribute('height', h);
  rect.setAttribute('rx', '8');
  for (const a of ['fill', 'stroke', 'stroke-width', 'class', 'style']) {
    if (firstPath.hasAttribute(a)) rect.setAttribute(a, firstPath.getAttribute(a));
  }
  firstPath.replaceWith(rect);
});

// Strip borders from attribute rows (mermaid v11: .row-rect-odd / .row-rect-even)
document.querySelectorAll('#erd svg.erDiagram .row-rect-odd path, #erd svg.erDiagram .row-rect-even path').forEach(p => {
  p.setAttribute('stroke', 'none');
});
</script>
```

Works identically for `classDiagram` — swap the diagram source; init stays the same.

#### Illustrative diagram

For building *intuition*. The subject might be physical (an engine, a lung) or completely abstract (attention, recursion, gradient descent) — what matters is that a spatial drawing conveys the mechanism better than labelled boxes would. These are the diagrams that make someone go "oh, *that's* what it's doing."

**Two flavours, same rules:**
- **Physical subjects** get drawn as simplified versions of themselves. Cross-sections, cutaways, schematics. A water heater is a tank with a burner underneath. A lung is a branching tree in a cavity. You're drawing *the thing*, stylised.
- **Abstract subjects** get drawn as *spatial metaphors*. You're inventing a shape for something that doesn't have one — but the shape should make the mechanism obvious. A transformer is a stack of horizontal slabs with a bright thread of attention connecting tokens across layers. A hash function is a funnel scattering items into a row of buckets. The call stack is literally a stack of frames growing and shrinking. Embeddings are dots clustering in space. The metaphor *is* the explanation.

This is the most ambitious diagram type and the one Claude is best at. Lean into it. Use colour for intensity (a hot attention weight glows amber, a cold one stays gray). Use repetition for scale (many small circles = many parameters).

**Prefer interactive over static.** A static cross-section is a good answer; a cross-section you can *operate* is a great one. The decision rule: if the real-world system has a control, give the diagram that control. A water heater has a thermostat — so give the user a slider that shifts the hot/cold boundary, a toggle that fires the burner and animates convection currents. An LLM has input tokens — let the user click one and watch the attention weights re-fan. A cache has a hit rate — let them drag it and watch latency change. Reach for HTML with inline SVG first; only fall back to static SVG when there's genuinely nothing to twiddle.

**When NOT to use**: The user is asking for a *reference*, not an *intuition*. "What are the components of a transformer" wants labelled boxes — that's a structural diagram. "Walk me through our CI pipeline" wants sequential steps — that's a flowchart. Also skip this when the metaphor would be arbitrary rather than revealing: drawing "the cloud" as a cloud shape or "microservices" as little houses doesn't teach anything about how they work. If the drawing doesn't make the *mechanism* clearer, don't draw it.

**Fidelity ceiling**: These are schematics, not illustrations. Every shape should read at a glance. If a `<path>` needs more than ~6 segments to draw, simplify it. A tank is a rounded rect, not a Bézier portrait of a tank. A flame is three triangles, not a fire. Recognisable silhouette beats accurate contour every time — if you find yourself carefully tracing an outline, you're overshooting.

**Core principle**: Draw the mechanism, not a diagram *about* the mechanism. Spatial arrangement carries the meaning; labels annotate. A good illustrative diagram works with the labels removed.

**What changes from flowchart/structural rules**:

- **Shapes are freeform.** Use `<path>`, `<ellipse>`, `<circle>`, `<polygon>`, and curved lines to represent real forms. A water tank is a tall rect with rounded bottom. A heart valve is a pair of curved paths. A circuit trace is a thin polyline. You are not limited to rounded rects.
- **Layout follows the subject's geometry**, not a grid. If the thing is tall and narrow (a water heater, a thermometer), the diagram is tall and narrow. If it's wide and flat (a PCB, a geological cross-section), the diagram is wide. Let the subject dictate proportions within the 680px viewBox width.
- **Color encodes intensity**, not category. For physical subjects: warm ramps (amber, coral, red) = heat/energy/pressure, cool ramps (blue, teal) = cold/calm, gray = inert structure. For abstract subjects: warm = active/high-weight/attended-to, cool or gray = dormant/low-weight/ignored. A user should be able to glance at the diagram and see *where the action is* without reading a single label.
- **Layering and overlap are encouraged — for shapes.** Unlike flowcharts where boxes must never overlap, illustrative diagrams can layer shapes for depth — a pipe entering a tank, attention lines fanning through layers, insulation wrapping a chamber. Use z-ordering (later in source = on top) deliberately.
- **Text is the exception — never let a stroke cross it.** The overlap permission is for shapes only. Every label needs 8px of clear air between its baseline/cap-height and the nearest stroke. Don't solve this with a background rect — solve it by *placing the text somewhere else*. Labels go in the quiet regions: above the drawing, below it, in the margin with a leader line, or in the gap between two fans of lines. If there is no quiet region, the drawing is too dense — remove something or split into two diagrams.
- **Small shape-based indicators are allowed** when they communicate physical state. Triangles for flames. Circles for bubbles or particles. Wavy lines for steam or heat radiation. Parallel lines for vibration. These aren't decoration — they tell the user what's happening physically. Keep them simple: basic SVG primitives, not detailed illustrations.
- **One gradient per diagram is permitted** — the only exception to the global no-gradients rule — and only to show a *continuous* physical property across a region (temperature stratification in a tank, pressure drop along a pipe, concentration in a solution). It must be a single `<linearGradient>` between exactly two stops from the same colour ramp. No radial gradients, no multi-stop fades, no gradient-as-aesthetic. If two stacked flat-fill rects communicate the same thing, do that instead.
- **Animation is permitted for interactive HTML versions.** Use CSS `@keyframes` animating only `transform` and `opacity`. Keep loops under ~2s, and wrap every animation in `@media (prefers-reduced-motion: no-preference)` so it's opt-out by default. Animations should show how the system *behaves* — convection current, rotation, flow — not just move for the sake of moving. No physics engines or heavy libraries.

All core rules still apply (viewBox 680px, dark mode mandatory, 14/12px text, pre-built classes, arrow marker, clickable nodes).

**Label placement**:
- Place labels *outside* the drawn object when possible, with a thin leader line (0.5px dashed, `var(--t)` stroke) pointing to the relevant part. This keeps the illustration uncluttered.
- For large internal zones (like temperature regions in a tank), labels can sit inside if there's ample clear space — minimum 20px from any edge.
- External labels sit in the margin area or above/below the object. **Pick one side for labels and put them all there** — at 680px wide you don't have room for a drawing *and* label columns on both sides. Reserve at least 140px of horizontal margin on the label side. Labels on the left are the ones that clip: `text-anchor="end"` extends leftward from x, and with multi-line callouts it's very easy to blow past x=0 without noticing. Default to right-side labels with `text-anchor="start"` unless the subject's geometry forces otherwise. Use `class="ts"` (12px) for callouts, `class="th"` (14px medium) for major component names.

**Composition approach**:
1. Start with the main object's silhouette — the largest shape, centered in the viewBox.
2. Add internal structure: chambers, pipes, membranes, mechanical parts.
3. Add external connections: pipes entering/exiting, arrows showing flow direction, labels for inputs and outputs.
4. Add state indicators last: color fills showing temperature/pressure/concentration, small animated elements showing movement or energy.
5. Leave generous whitespace around the object for labels — don't crowd annotations against the viewBox edges.

**Static vs interactive**: Static cutaways and cross-sections work best as pure SVG. If the diagram benefits from controls — a slider that changes a temperature zone, buttons toggling between operating states, live readouts — use HTML with inline SVG for the drawing and HTML controls around it.

**Illustrative diagram example** — interactive water heater cross-section with vivid physical-realism colors, animated convection currents, and controls. Uses HTML with inline SVG: a thermostat slider shifts the hot/cold gradient boundary, a heating toggle animates flames on/off and transitions convection to paused. viewBox is 680×560; tank occupies x=180..440, leaving 140px+ of right margin for labels. Smooth convection paths use `stroke-dasharray:5 5` at ~1.6s for a gentle flow feel. A warm-glow overlay on the hot zone pulses subtly when heating is on. Flame shapes use warm gradient fills and clean opacity transitions. Labels sit along the right margin with leader lines.
```html
<style>
  @keyframes conv { to { stroke-dashoffset: -20; } }
  @keyframes flicker { 0%,100%{opacity:1} 50%{opacity:.82} }
  @keyframes glow { 0%,100%{opacity:.3} 50%{opacity:.6} }
  .conv { stroke-dasharray:5 5; animation: conv var(--dur,1.6s) linear infinite; transition: opacity .5s; }
  .conv.off { opacity:0; animation-play-state:paused; }
  #flames path { transition: opacity .5s; }
  #flames.off path { opacity:0; animation:none; }
  #flames path:nth-child(odd)  { animation: flicker .6s ease-in-out infinite; }
  #flames path:nth-child(even) { animation: flicker .8s ease-in-out infinite .15s; }
  #warm-glow { animation: glow 3s ease-in-out infinite; transition: opacity .5s; }
  #warm-glow.off { opacity:0; animation:none; }
  .toggle-track { position:relative;width:32px;height:18px;background:var(--color-border-secondary);border-radius:9px;transition:background .2s;display:inline-block; }
  .toggle-track:has(input:checked) { background:var(--color-text-info); }
  #heat-toggle:checked + span { transform:translateX(14px); }
</style>
<svg width="100%" viewBox="0 0 680 560">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
    <linearGradient id="tg" x1="0" y1="0" x2="0" y2="1">
      <stop id="gh" offset="40%" stop-color="#E8593C" stop-opacity="0.45"/>
      <stop id="gc" offset="40%" stop-color="#3B8BD4" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="fg1" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#E85D24"/><stop offset="60%" stop-color="#F2A623"/><stop offset="100%" stop-color="#FCDE5A"/></linearGradient>
    <linearGradient id="fg2" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#D14520"/><stop offset="50%" stop-color="#EF8B2C"/><stop offset="100%" stop-color="#F9CB42"/></linearGradient>
    <linearGradient id="pipe-h" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#D05538" stop-opacity=".25"/><stop offset="100%" stop-color="#D05538" stop-opacity=".08"/></linearGradient>
    <linearGradient id="pipe-c" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3B8BD4" stop-opacity=".25"/><stop offset="100%" stop-color="#3B8BD4" stop-opacity=".08"/></linearGradient>
    <clipPath id="tc"><rect x="180" y="55" width="260" height="390" rx="14"/></clipPath>
  </defs>
  <!-- Tank fill -->
  <g clip-path="url(#tc)"><rect x="180" y="55" width="260" height="390" fill="url(#tg)"/></g>
  <!-- Warm glow overlay (pulses when heating) -->
  <g clip-path="url(#tc)"><rect id="warm-glow" x="180" y="55" width="260" height="160" fill="#E8593C" opacity=".3"/></g>
  <!-- Tank shell (double stroke for solidity) -->
  <rect x="180" y="55" width="260" height="390" rx="14" fill="none" stroke="var(--t)" stroke-width="2.5" opacity=".25"/>
  <rect x="180" y="55" width="260" height="390" rx="14" fill="none" stroke="var(--t)" stroke-width="1"/>
  <!-- Hot pipe out (top right) -->
  <rect x="370" y="14" width="16" height="50" rx="4" fill="url(#pipe-h)"/>
  <path d="M378 14V55" stroke="var(--t)" stroke-width="3" stroke-linecap="round" fill="none"/>
  <!-- Cold pipe in + dip tube (top left) -->
  <rect x="234" y="14" width="16" height="50" rx="4" fill="url(#pipe-c)"/>
  <path d="M242 14V55" stroke="var(--t)" stroke-width="3" stroke-linecap="round" fill="none"/>
  <path d="M242 55V395" stroke="var(--t)" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".5"/>
  <!-- Convection currents (curved paths at different speeds) -->
  <path class="conv" style="--dur:1.6s" fill="none" stroke="#D05538" stroke-width="1" opacity=".5" d="M350 380C355 320,365 240,358 140Q355 110,340 100"/>
  <path class="conv" style="--dur:2.1s" fill="none" stroke="#C04828" stroke-width=".8" opacity=".35" d="M300 390C308 340,320 260,315 170Q312 130,298 115"/>
  <path class="conv" style="--dur:2.6s" fill="none" stroke="#B05535" stroke-width=".7" opacity=".3" d="M380 370C382 310,388 230,382 150Q378 120,365 110"/>
  <!-- Burner bar -->
  <rect x="188" y="454" width="244" height="5" rx="2" fill="var(--t)" opacity=".6"/>
  <rect x="220" y="462" width="180" height="6" rx="3" fill="var(--t)" opacity=".3"/>
  <!-- Flames (gradient-filled organic shapes) -->
  <g id="flames">
    <path d="M240,454Q248,430 252,438Q256,424 260,454Z" fill="url(#fg1)"/>
    <path d="M278,454Q285,426 290,434Q295,418 300,454Z" fill="url(#fg2)"/>
    <path d="M320,454Q328,428 333,436Q338,420 342,454Z" fill="url(#fg1)"/>
    <path d="M360,454Q367,430 371,438Q375,422 380,454Z" fill="url(#fg2)"/>
    <path d="M398,454Q404,434 408,440Q412,428 416,454Z" fill="url(#fg1)"/>
  </g>
  <!-- Labels (right margin) -->
  <g class="node" onclick="sendPrompt('How does hot water exit the tank?')">
    <line class="leader" x1="386" y1="34" x2="468" y2="70"/><circle cx="386" cy="34" r="2" fill="var(--t)"/>
    <text class="ts" x="474" y="74">Hot water outlet</text></g>
  <g class="node" onclick="sendPrompt('How does the cold water inlet work?')">
    <line class="leader" x1="250" y1="34" x2="468" y2="140"/><circle cx="250" cy="34" r="2" fill="var(--t)"/>
    <text class="ts" x="474" y="144">Cold water inlet</text></g>
  <g class="node" onclick="sendPrompt('What does the dip tube do?')">
    <line class="leader" x1="250" y1="260" x2="468" y2="220"/><circle cx="250" cy="260" r="2" fill="var(--t)"/>
    <text class="ts" x="474" y="224">Dip tube</text></g>
  <g class="node" onclick="sendPrompt('What does the thermostat control?')">
    <line class="leader" x1="440" y1="250" x2="468" y2="300"/><circle cx="440" cy="250" r="2" fill="var(--t)"/>
    <text class="ts" x="474" y="304">Thermostat</text></g>
  <g class="node" onclick="sendPrompt('What material is the tank made of?')">
    <line class="leader" x1="440" y1="380" x2="468" y2="380"/><circle cx="440" cy="380" r="2" fill="var(--t)"/>
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

**[USER]**

steer the name towards a more professional style but I do a lot of EDM shows and I have tattoos all over so It doesn't need to be extra professional.

---

**[ASSISTANT]**

Love that direction — professional enough to invoice a Fortune 500 corporate gig, but with enough edge that it doesn't feel like a law firm.

Here are some names that hit that balance:

**Industry-grounded with some grit:**
- *Blackline Production Services LLC*
- *Ironframe Crew LLC*
- *Deadhang Labor Co. LLC* (rigging reference, immediately recognizable in the industry)
- *Loadline Services LLC*
- *Stagemark LLC*

**Cleaner / more neutral but not sterile:**
- *Crestline Production Group LLC*
- *Highpoint Crew Services LLC*
- *Gridline Labor LLC*
- *Benchmark Production Services LLC*

**A little more attitude, still scalable:**
- *Rogue Riggers LLC* — bold but might pigeonhole you to rigging only
- *Blacktop Crew LLC*
- *Hardline Production Services LLC*
- *Static Crew Services LLC* — nods to EDM without being obvious about it

---

My personal shortlist from that batch for your situation: **Blackline Production Services**, **Hardline Production Services**, or **Static Crew Services** — all three invoice well, scale to a crew, and don't feel corporate-sterile.

What's resonating? Even a vibe or a word you like — we can work with that and narrow it down to your finalist before you check availability on the ACC.

---

**[USER]**

Highpoint Crew Services LLC
Deadhang Labor LLC
Ironframe Crew LLC
Steel Team Six LLC

these are names I like, make more suggestions with that in mind

---

**[ASSISTANT]**

Good taste — you're clearly gravitating toward **strong, physical, industry-rooted words**. That's the right instinct. Here's an expanded batch in that same lane:

**In the "Highpoint / Ironframe" vein — structural, solid:**
- *Ironset Crew Services LLC*
- *Steelframe Production Group LLC*
- *Loadbearing Crew LLC*
- *Ridgeline Crew Services LLC*
- *Cornerstone Crew LLC*
- *Groundset Production Services LLC*

**In the "Deadhang" vein — rigging/technical, insider language:**
- *Pickup Point Crew LLC* (rigging term, invisible to outsiders)
- *Bridle Line Services LLC*
- *Choker Crew LLC* (rigging slang — edgy but industry-known)
- *Headblock Crew Services LLC*
- *Shackle Point LLC*

**In the "Steel Team Six" vein — tough, unit/team energy:**
- *Iron Unit LLC*
- *Steel Deck Crew LLC*
- *Black Iron Services LLC*
- *Hard Deck LLC*
- *Ground Force Crew LLC*
- *Strike Force Production Services LLC*

---

Honestly Aaron, **Deadhang Labor LLC** from your original list is the strongest one you named. It's memorable, it's an industry insider term, it has edge, and "Labor LLC" keeps it scalable and professional on an invoice.

What's pulling you toward any of these — or does one jump out?

---

**[USER]**

Deadhang Labor LLC

---

**[ASSISTANT]**

Solid choice. That name is genuinely good — memorable, industry-credible, scales to a crew, and looks clean on an invoice.

**Next step: check availability on the ACC.**

Here's exactly what to do:

1. Go to **[ecorp.azcc.gov](https://ecorp.azcc.gov)**
2. Click **"Search"** in the top navigation
3. Select **"Business Entity Search"**
4. Type `Deadhang Labor` in the name field and hit search
5. Also search `Deadhang` alone — just to see if anything close exists

You're looking for **no exact match and no confusingly similar match**. A different entity type (like a corporation) with a similar name can still block yours.

---

**While you're there, also check:**
- `Deadhang Labor LLC` — exact
- `Dead Hang Labor LLC` — spaced variation
- `Deadhang Productions LLC` — adjacent (you don't want to be confused with them)

---

Go run that search and report back what you find. If it's clear, we move straight to filing your Articles of Organization. If something comes up, we pivot the name slightly — there are easy fixes.

---

**[USER]**

First, I am not yet an experienced rigger. would using a name like that tarnish my credibility?

---

**[ASSISTANT]**

Really smart question to ask before filing — glad you caught that.

**Honest answer: potentially yes, in certain circles.**

Here's the nuance:

**The risk:** "Deadhang" is a specific rigging term. If you show up to a gig as the *labor coordinator* or *stagehand* and someone sees your LLC name on an invoice or contract, an experienced rigger might expect you to be further along in your rigging career than you are. In a industry where credibility is built on what you've *done*, that gap could raise an eyebrow.

**The non-risk:** For corporate event clients, production companies, and non-technical people cutting you a check — they have zero idea what a deadhang is. It just sounds cool and tough to them.

**The real question is** — who's primarily seeing your LLC name on paperwork? If it's mostly:
- **Production companies and crew bosses** → mild risk worth considering
- **Corporate clients and event planners** → zero risk, they won't know

---

Given that you're actively pursuing ETCP and moving *toward* rigging credibility — you're not misrepresenting yourself, you're just slightly ahead of where you are. But if it'll make you second-guess yourself on a job site, that psychological weight isn't worth it.

**My honest recommendation:** Go with **Ironframe Crew LLC** or **Highpoint Crew Services LLC** from your list. Same energy, same edge, no technical baggage attached to a specific discipline you're still building toward.

What's your gut say?

---

**[USER]**

I will be more steel structures, staging, scaffolding, rigging, and that sort of work over production, if anything LED walls or lighting

---

**[ASSISTANT]**

That context changes everything — and it actually makes **Deadhang Labor LLC** *more* appropriate, not less.

Here's why:

**Staging, steel, scaffolding, and structural rigging** is exactly the world that term lives in. A deadhang *is* a structural rigging configuration — static load, no motion, pure tension. That's the bread and butter of what you're describing. Someone who works steel deck, scaffolding, and structural rigging knowing what a deadhang is makes complete sense. Nobody in that world is going to question it.

The credibility concern would matter more if you were positioning as a **fly system operator or entertainment rigger specifically** — that's where the ETCP pedigree gets scrutinized hard. But as a **labor coordinator and stagehand who works structural staging and steel** — the name fits your lane perfectly.

**LED walls and lighting** are just bonus scope on top of that structural foundation. Nobody expects an LED tech to be an ETCP rigger.

---

So to recap where you actually land:

- Steel structure assembly ✓
- Staging and scaffolding ✓
- Structural rigging ✓
- LED walls / lighting ✓
- Labor coordination ✓

**Deadhang Labor LLC fits all of that cleanly.** It's not a stretch — it's accurate.

Go check that ACC availability. I think you've got your name.

---

**[USER]**

deadhang, deadhang labor, and deadhang labor llc are ALL available

---

**[ASSISTANT]**

Let's go — **Deadhang Labor LLC** is yours to claim.

**Do this right now before someone else grabs it:**

---

## File your Articles of Organization

1. Go to **[ecorp.azcc.gov](https://ecorp.azcc.gov)**
2. Click **"Start a Business"** or **"File a New Entity"**
3. Select **"Limited Liability Company"**
4. Select **"Domestic LLC"** (you're forming in Arizona)

---

## What you'll fill out:

**Entity Name:** `Deadhang Labor LLC`

**Known Place of Business Address:** Your physical address in Glendale/Peoria — must be an Arizona street address, no PO boxes

**Statutory Agent:** Put your own name and address here for now — keeps cost at zero. You can always switch to a paid service later.

**Member/Manager:** Select **"Member Managed"** — that's standard for a single-member LLC where you run everything yourself

**Principal Address:** Same as your business address is fine

---

## Payment:
- **$50 online filing fee**
- Needs a debit or credit card at checkout

---

Go through the filing and let me know when you hit any fields you're unsure about — I'll walk you through each one in real time. Once you submit, screenshot or save your confirmation number. That's your proof of filing while you wait for approval.

---

**[USER]**

can i get a free statutory agent?

---

**[ASSISTANT]**

**Short answer: yes, yourself — but with a tradeoff.**

---

## Free options:

**Option 1 — Be your own statutory agent (free)**
- Totally legal in Arizona
- You just use your own name and home address
- Requirements: must be an Arizona resident, must have a physical street address, must be available during normal business hours to receive legal documents

**The tradeoff:** Your home address becomes **public record** on the ACC website permanently. Anyone can look up Deadhang Labor LLC and see exactly where you live.

---

**Option 2 — A friend or family member (free)**
- Also legal — just needs to be an Arizona resident with a physical address
- Same public record issue applies to their address
- They need to be reliably reachable during business hours

---

## When a paid agent (~$50/year) is actually worth it:
- You travel frequently for gigs ✓ *(you do)*
- You don't want your home address public ✓
- You're gone for extended festival runs ✓ *(Rothbury, Electric Forest, etc.)*

Given that you're regularly out of state for weeks at a time on production gigs, a paid statutory agent is honestly worth the $50/year just so you don't miss a legal notice while you're on site in Michigan.

---

**My recommendation:** Use **Northwest Registered Agent** — they're $39/year, highly rated, and keep your home address off public record.

What do you want to do?

---

**[USER]**

Can I download my bank statements from my personal account and feed them to you after these purchases to immediately start tracking/seperating my business and personal accounts?

---

**[ASSISTANT]**

Yes, absolutely — and that's a great habit to build from day one.

---

## What you can do right now, before the business account is even open:

Once you have your bank statements downloaded (PDF or CSV both work), you can feed them to me and I can:

- **Categorize every transaction** — flag what's business vs personal
- **Pull out all business-related expenses** — tool purchases, Uber/Lyft to gigs, phone bill percentage, gear, etc.
- **Build a clean expense log** you can hand to a tax preparer or import into Wave/QuickBooks
- **Identify deductible expenses** you might have missed
- **Separate the LLC formation costs** as your first official business expenses

---

## What counts as a business expense even from your personal account:

Since Deadhang Labor LLC didn't exist yet, any formation-related purchases made personally are still **legitimate business startup expenses** — the IRS allows you to deduct up to **$5,000 in startup costs** in your first year.

That includes:
- ACC filing fee
- Publication notice fee
- Any registered agent fee
- Tools or gear bought for work
- Mileage and rideshare to gigs

---

## When you're ready:

Just download your statements and drop them here. Tell me the date range and I'll get to work sorting everything out.

Ready to keep moving on the filing?

---

**[USER]**

where can i get a small business grant of a few hundred dollars to help me pay for these fees

---

**[ASSISTANT]**

Honest answer here, Aaron — **small business grants for a few hundred dollars are harder to find than they're worth chasing** in most cases. Here's the real landscape:

---

## The truth about small business grants:

- Most grants are **$5,000 minimum** and targeted at specific demographics, industries, or communities
- Applications are time-consuming — often weeks of work for uncertain results
- Most require you to **already be in business** for 6–12 months
- Federal and state grants heavily favor **product-based businesses, nonprofits, or tech startups**

---

## What actually exists for your situation:

**Arizona-specific:**
- **Arizona Commerce Authority** — has some small business resources but mostly loans, not grants
- **Maricopa SBDC** (Small Business Development Center) — free consulting, occasionally aware of local micro-grants
- Visit **[azsbdc.net](https://azsbdc.net)** — free resource, worth a call

**Demographic-based (if applicable):**
- **Veteran-owned** — several grant programs if that applies to you
- **Minority-owned** — various programs through SBA

---

## Honestly the faster move:

Your total out of pocket is **$80–$130**. The realistic options that actually make sense:

- **One extra gig shift** covers the entire formation cost
- **Crew One or Rhino** — pick up a local call this week
- Formation costs are **tax deductible** anyway — you get some back

---

Do any demographic-based programs apply to you, or should we just keep moving through the filing?

---

**[USER]**

can the plane ticket i bought to go to michigan be written off as a travel expense even though i paid for it before the business was started?

---

**[ASSISTANT]**

**Yes — with an important condition.**

---

## The IRS rule on pre-formation expenses:

The IRS allows you to deduct **startup costs** that were incurred *before* your business officially opened, as long as they were:

- Clearly intended for the business
- Paid in the same tax year the business launches
- Directly related to business activity

This falls under **IRS Section 195** — startup cost deduction, up to **$5,000 in year one.**

---

## For your Michigan trip specifically:

**It qualifies IF:**
- The trip is primarily for the production gig *(it is)*
- You can document it was work-related *(contract, call sheet, gig confirmation)*
- Deadhang Labor LLC launches in the **same tax year** you bought the ticket

**It does not qualify if:**
- The trip is primarily personal with some work mixed in
- You can't document the business purpose

---

## What to save right now:

- ✓ Plane ticket receipt/confirmation
- ✓ Gig contract or booking confirmation from Rhino/Norton/whoever
- ✓ Any call sheets or crew communications
- ✓ Hotel or lodging receipts
- ✓ Per diem or meal receipts while on site

---

## One flag:

Since you bought the ticket **before the LLC existed**, document it clearly as a startup expense when you file. A tax preparer will know exactly how to handle it under Section 195.

---

Keep every receipt from here forward — want to keep moving to the next phase of the filing?

---

**[USER]**

does having the receipt tracked in my bank account work?

---

**[ASSISTANT]**

**Yes — bank records are valid documentation, but they work better with backup.**

---

## What your bank statement proves:

- ✓ Money left your account
- ✓ The date of the purchase
- ✓ The amount
- ✓ The merchant name (airline, hotel, etc.)

**For most routine expenses that's sufficient.** The IRS generally accepts bank and credit card statements as proof of payment.

---

## Where it gets thin:

A bank statement alone **doesn't prove business purpose.** It shows you bought a Delta ticket to Michigan — it doesn't prove it was for a production gig.

The IRS wants to see **two things:**
1. **Proof of payment** — bank statement covers this ✓
2. **Proof of business purpose** — this is the gap

---

## How to cover the gap cheaply:

Just keep a simple note attached to each expense — even a Google Doc or Notes app entry works:

| Date | Amount | Merchant | Business Purpose |
|------|--------|----------|-----------------|
| 5/14/26 | $287 | Delta Airlines | Travel to Michigan — Rothbury production gig, Rhino Staging |

That paired with your **gig contract or booking confirmation** is bulletproof documentation.

---

## The simple system going forward:

**Bank statement + business purpose note + any contract/confirmation = clean defensible records**

Wave and QuickBooks both let you attach photos of receipts and notes directly to transactions — we'll set that up once your business account is open.

Ready to get back to the filing?

---

**[USER]**

yes. take me through the steps of filing a business

---

**[ASSISTANT]**

Alright — pull up **[ecorp.azcc.gov](https://ecorp.azcc.gov)** right now and tell me when you're on the homepage. 

We're going to go through this together one screen at a time so nothing gets missed or filled out wrong.

---

**[USER]**

im there.

---

**[ASSISTANT]**

Good. 

**Look for a button or link that says "File an Action" or "New Filing" or "Start a Business"** — it may also say "Create a New Entity."

Tell me exactly what you see on the homepage and I'll direct you to the right button.

---

**[USER]**

REGISTER?

---

**[ASSISTANT]**

**Yes — click "Register."**

That's the one. Tell me what you see on the next screen.

---

**[USER]**

i created the account now what

---

**[ASSISTANT]**

Perfect — now you should be logged in.

**Look for one of these options:**
- "File a New Entity"
- "Form a Business"
- "New LLC"
- "Domestic LLC"

Tell me exactly what you see on your dashboard or the next screen.

---

**[USER]**

should i choose domestic or foreign? i work in arizona but work elsewhere also

---

**[ASSISTANT]**

**Domestic.**

Foreign doesn't mean you work in other states — it means your LLC was *formed* in another state and you're registering it in Arizona.

Since you're forming Deadhang Labor LLC **in Arizona**, you're domestic regardless of where you travel for work.

Click **Domestic LLC** and tell me what the next screen looks like.

---

**[USER]**

limited liability, professional limited liability or insurur?

---

**[ASSISTANT]**

**Limited Liability Company.**

- **Professional LLC** is only for licensed professions like doctors, lawyers, architects, and CPAs
- **Insurer** is for insurance companies

You're a labor contractor — plain **Limited Liability Company** is exactly right.

Select that and tell me what the next screen looks like.

---

**[USER]**

what business code would i be using?

---

**[ASSISTANT]**

Good question — you'll want one of these:

**Best fit for Deadhang Labor LLC:**

**238990** — *Other Specialty Trade Contractors*
- This covers staging, rigging, scaffolding, and structural assembly
- Most accurate for what you do

---

**Second option if 238990 isn't listed:**

**711510** — *Independent Artists, Writers, and Performers*
- Sometimes used for production/entertainment contractors
- Less accurate for your work

**561990** — *All Other Support Services*
- Generic catch-all if nothing else fits

---

**Go with 238990 first.** It's the most defensible code for steel, staging, scaffolding, and rigging labor.

Type it in and tell me what the next screen looks like.

---

**[USER]**

member managed?

---

**[ASSISTANT]**

**Yes — Member Managed.**

That means **you** run the LLC directly as the owner/member.

**Manager Managed** is for when you appoint someone else to manage the LLC on your behalf — not relevant for a solo operation like yours.

Select **Member Managed** and tell me what the next screen looks like.

---

**[USER]**

add principal?

---

**[ASSISTANT]**

**Yes — click "Add Principal."**

This is where you add yourself as the member/owner of the LLC.

Fill it out as follows:
- **Name:** Your full legal name
- **Title/Role:** Member
- **Address:** Your home address in Glendale/Peoria
- **Ownership:** 100%

Fill that in and tell me what the next screen looks like.

---

**[USER]**

principal type?

---

**[ASSISTANT]**

**Member.**

That's you — the owner of the LLC.

The options are typically:
- **Member** — owner of the LLC ✓ *(this is you)*
- **Manager** — someone appointed to run it who may not be an owner
- **Organizer** — just the person who filed the paperwork

Select **Member** and tell me what it asks next.

---

**[USER]**

it says individual or business

---

**[ASSISTANT]**

**Individual.**

You are a person, not another business entity owning this LLC.

Select **Individual** and tell me what it asks next.

---

**[USER]**

upload documents?

---

**[ASSISTANT]**

**Skip it for now.**

You don't need to upload anything at this stage. That section is for optional supporting documents — you don't have any yet.

Look for a **"Next"** or **"Continue"** button and tell me what the next screen looks like.

---

**[USER]**

organizer?

---

**[ASSISTANT]**

**Yes — add yourself as the Organizer.**

The organizer is simply the person submitting the filing — that's you.

Fill it out:
- **Type:** Individual
- **Name:** Your full legal name
- **Address:** Your home address

This is just confirming who filed the paperwork. It doesn't create any additional role or liability.

Fill that in and tell me what the next screen looks like.

---

**[USER]**

I have paid and my submission was accepted, now what

---

**[ASSISTANT]**

**Congratulations — Deadhang Labor LLC is officially filed.**

---

## Right now, immediately:

1. **Screenshot or save your confirmation page** — grab the confirmation/tracking number
2. **Save or print the confirmation email** the ACC sends you — this is your proof of filing
3. **Do not close the browser** until you've saved everything

---

## What happens next:

- ACC will review and approve your filing in **2–5 business days**
- You'll get an email when it's approved
- Once approved you'll be able to download your **Articles of Organization** — save that PDF, you'll need it for banking

---

## While you wait — your next moves in order:

1. **Start looking for your publication newspaper** — you have 60 days from approval, let's get ahead of it
2. **Draft your Operating Agreement** — we'll do this together right here
3. **Apply for your EIN** — the day you get ACC approval
4. **Open business banking** — within a week of your EIN

---

## One question while the ACC processes:

Did you use your home address as your statutory agent, or did you go with a paid service?

That tells me what we need to tackle next on the publication requirement.

---

**[USER]**

it has been processed. i have my articles of organization

---

**[ASSISTANT]**

**Let's go — Deadhang Labor LLC is officially a real business.**

Save that Articles of Organization PDF somewhere safe right now — you'll need it multiple times:
- EIN application
- Business banking
- Any contracts or vendor accounts

---

## Your next move is the EIN — do this today while you have momentum.

Pull up a new tab and go to:

**[irs.gov/ein](https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online)**

It's free, takes 10 minutes, and you get your EIN **instantly** on screen.

---

## Before you click anything tell me:

**What time is it right now?**

The IRS online EIN application is only available:
- **Monday–Friday**
- **7am–10pm Eastern time**

Arizona is on MST — so that's **5am–8pm Arizona time** currently since we're past the spring time change.

If you're in that window — go to that link right now and tell me when you're on the page.

---

**[USER]**

what is excise tax

---

**[ASSISTANT]**

**Excise tax is a tax on specific goods, services, or activities** — not on general income or sales.

---

## Simple explanation:

Think of it as a **"use tax" on particular industries or products.**

Common examples:
- Fuel/gasoline
- Alcohol
- Tobacco
- Air transportation
- Heavy trucks and trailers
- Indoor tanning services

---

## Why it's coming up in your EIN application:

The IRS asks if your business deals in **excise tax items** to determine if you need to file additional tax forms.

---

## For Deadhang Labor LLC:

**You almost certainly answer NO.**

You are a:
- Labor contractor
- Staging and rigging professional
- Service-based business

You are **not:**
- Selling fuel
- Manufacturing alcohol or tobacco
- Operating heavy highway vehicles over 55,000 lbs
- Running an airline

---

## One exception worth knowing:

If you ever purchase and operate **heavy equipment over 55,000 lbs** — certain cranes, large trucks, etc. — that could trigger excise tax considerations down the road. But that's a conversation for when you're there.

**For right now — answer NO to excise tax and keep moving.**

What's the next question on the screen?

---

**[USER]**

done. whats next

---

**[ASSISTANT]**

**Did you save your EIN confirmation page?**

It should show a page with your EIN number on it — looks something like **XX-XXXXXXX.**

Do these two things right now:
1. **Screenshot the confirmation page**
2. **Download or print the EIN confirmation letter PDF** — the IRS calls it the CP575 letter

---

Once you confirm you have that saved — here's exactly where you stand:

## ✓ Completed:
- LLC name selected
- Articles of Organization filed and approved
- EIN obtained

## Next three moves in order:

**1. Operating Agreement** — we draft it right here together, today
- Takes 15 minutes
- Required for banking

**2. Publication Notice** — find your Maricopa County newspaper
- You have 60 days from ACC approval
- Costs $30–75
- We'll knock this out this week

**3. Business Banking** — once you have your operating agreement
- Bring Articles of Organization + EIN letter + Operating Agreement + ID
- Recommend doing this in person this week

---

Do you have your EIN confirmation saved and ready?

---

**[USER]**

yes, what is the publication notice?

---

**[ASSISTANT]**

**It's an Arizona-specific legal requirement to publicly announce that your LLC exists.**

---

## What it is:

Arizona is one of only **three states** that requires new LLCs to publish a notice of formation in a local newspaper. It's an old law — most states got rid of it — but Arizona still enforces it.

---

## What you have to do:

Publish a small legal notice in an **ACC-approved newspaper** in Maricopa County for **3 consecutive weeks.**

The notice basically says:
- Deadhang Labor LLC exists
- When it was formed
- Your statutory agent information
- Your business address

---

## What it costs:

**$30–$75** in Maricopa County depending on which approved newspaper you use.

---

## The cheapest legitimate option in Maricopa County:

**Arizona Business Gazette** — this is the most commonly used and typically the most affordable for Maricopa County LLC publications.

Visit **[azbex.com](https://azbex.com)** or call them directly and tell them:
- You need to publish an LLC formation notice
- You're in Maricopa County
- You just filed with the ACC

They handle the wording for you — you just pay and provide your LLC details.

---

## Timeline reminder:

- You have **60 days** from your ACC approval date
- Don't wait — knock it out this week while you have momentum

---

Want me to draft the exact notice language you'll need to provide them?

---

**[USER]**

draft my operating agreement

---

**[ASSISTANT]**

Let's do this right — I need a few quick details to make it accurate and ready to hand to a bank.

**Answer these one at a time:**

---

**1. What is your full legal name?**

---

**[USER]**

Aaron C Bowman

---

**[ASSISTANT]**

**2. What is your full home address in Glendale/Peoria?**

Include street, city, state, and zip code.

---

**[USER]**

can you add a reminder in my calendar to do the newspaper thing?

---

**[ASSISTANT]**

I can help with that! Let me check if your Google Calendar is connected.Loaded 5 Google Calendar tools:
  Google Calendar:create_event:
    endTime: string - Required. The end time of the event. Must be a full ISO 8601 timestamp (e.g., '2026-04-30T10:00:00Z').
    startTime: string - Required. The start time of the event formatted as per ISO 8601.
    summary: string - Required. Title of the event.
    addGoogleMeetUrl?: boolean - Optional. Whether to create and attach a video conference URL for the event. Defaults to False.
    allDay?: boolean - Optional. Whether the event is an all-day event. The default is False. If true, the start and end time must be set to...
    attendeeEmails?: array [string] - Optional. The additional attendees of the event, as email addresses. For events that are created on the user's primar...
    calendarId?: string - Optional. The calendar ID to create the event on. The default is the user's primary calendar.
    colorId?: string - Optional. The color of the event. This is an ID referring to an entry in the calendar's color palette. Event color ID...
    description?: string - Optional. Description of the event. Can contain HTML.
    googleMeetUrl?: string - Optional. Allows attaching an existing Google Meet URL or meeting ID to the event. If set, this URL will be attached ...
    location?: string - Optional. Geographic location of the event as free-form text.
    notificationLevel?: string [NOTIFICATION_LEVEL_UNSPECIFIED|NONE|EXTERNAL_ONLY|ALL] - Optional. Which email notification should be sent for this event update. Possible values are: * `NONE` - No email not...
    overrideReminders?: array [any] - Optional. Reminders defined for this event, overriding the default reminders for the calendar. If not set, the event ...
    recurrenceData?: array [string] - Optional. The recurrence data of the event as RRULE, RDATE, or EXDATE strings per RFC 5545. Each string in the list a...
    timeZone?: string - Optional. Time zone of the event formatted as a strictly case-sensitive IANA Time Zone Database name (e.g., 'America/...
    visibility?: string - Optional. Visibility of the event. Possible values are: * `default` - Uses the default visibility for events on the c...
  Google Calendar:update_event:
    eventId: string - Required. The ID of the event to update.
    addGoogleMeetUrl?: boolean - Optional. Allows to create or update a Google Meet url for the event. By default, no Google Meet url is created or up...
    addedAttendeeEmails?: array [string] - Optional. The additional attendees of the event, as email addresses.
    calendarId?: string - Optional. The calendar ID of the event to update. The default is the user's primary calendar.
    colorId?: string - Optional. New color ID of the event. Will not be updated if not set. Event color ID (string `1`-`11`): * 1: Lavender ...
    description?: string - Optional. The new description of the event. Will not be updated if not set.
    endTime?: string - Optional. The new end time of the event formatted as per ISO 8601. Will not be updated if not set.
    googleMeetUrl?: string - Optional. Allows attaching an existing Google Meet URL or meeting ID to the event. If set, this URL will be attached ...
    location?: string - Optional. The new location of the event. Will not be updated if not set.
    notificationLevel?: string [NOTIFICATION_LEVEL_UNSPECIFIED|NONE|EXTERNAL_ONLY|ALL] - Optional. Which email notification should be sent for this event update. Possible values are: * `NONE` - No email not...
    overrideReminders?: array [any] - Optional. Reminders defined for this event, overriding any existing reminders and the default reminders for the calen...
    removedAttendeeEmails?: array [string] - Optional. The attendees of the event to remove, as email addresses.
    startTime?: string - Optional. The new start time of the event formatted as per ISO 8601. Will not be updated if not set.
    summary?: string - Optional. The new title of the event. Will not be updated if not set.
    visibility?: string - Optional. New visibility of the event. Possible values are: * `default` - Uses the default visibility for events on t...
  Google Calendar:get_event:
    eventId: string - Required. The ID of the event to get.
    calendarId?: string - Optional. The calendar ID to get the event from. The default is the user's primary calendar.
  Google Calendar:delete_event:
    eventId: string - Required. The ID of the event to delete.
    calendarId?: string - Optional. The calendar ID of the event to delete. The default is the user's primary calendar.
    notificationLevel?: string [NOTIFICATION_LEVEL_UNSPECIFIED|NONE|EXTERNAL_ONLY|ALL] - Optional. Which email notification should be sent for this event update. Possible values are: * `NONE` - No email not...
  Google Calendar:list_events:
    calendarId?: string - Optional. The calendar ID to list events from. The default is the user's primary calendar.
    endTime?: string - Optional. Upper bound (exclusive) for of the time window to search. Defaults to the end of time. Must be an ISO 8601 ...
    eventTypeFilter?: array [string] - Optional. The event types to return. Possible values are: * `default` - Regular events (default). * `outOfOffice` - O...
    fullText?: string - Optional. Free-form search query to search across title, description, location and attendees. The search is case-inse...
    orderBy?: string - Optional. The order in which events should be returned. Possible values are: * `default` - Unspecified, but determini...
    pageSize?: integer - Optional. Maximum number of events returned on one result page. The number of events in the resulting page may be les...
    pageToken?: string - Optional. A token retrieved from a previous response's nextPageToken field.
    startTime?: string - Optional. Lower bound (exclusive) for the time window to search. Defaults to the current time if neither time bound i...
    timeZone?: string - Optional. Time zone used in the response and to resolve timezone-less dates in the request (formatted as an IANA Time...
These tools are now available for you to call directly.

<functions>
<function>{"description": "Creates a calendar event. Use this tool for queries like: * Create an event on my calendar for tomorrow at 2pm called 'Meeting with Jane'. * Schedule a meeting with john.doe@google.com next Monday from 10am to 11am. Example: create_event( summary='Meeting with Jane', startTime='2024-09-17T14:00:00', endTime='2024-09-17T15:00:00' ) # Creates an event on the primary calendar for September 17, 2024 from 2pm to 3pm called 'Meeting with Jane'.", "name": "Google Calendar:create_event", "parameters": {"$defs": {"Reminder": {"description": "An event reminder.", "properties": {"method": {"description": "Required. How the reminder is delivered to the user. Possible values are: * `email` - Reminders are sent via email. * `popup` - Reminders are sent via a UI popup.", "type": "string"}, "minutes": {"description": "Required. Number of minutes in advance that the reminder should be delivered.", "format": "int32", "type": "integer"}}, "required": ["method", "minutes"], "type": "object"}}, "description": "Request message for CreateEvent.", "properties": {"addGoogleMeetUrl": {"description": "Optional. Whether to create and attach a video conference URL for the event. Defaults to False.", "type": "boolean"}, "allDay": {"description": "Optional. Whether the event is an all-day event. The default is False. If true, the start and end time must be set to midnight UTC.", "type": "boolean"}, "attendeeEmails": {"description": "Optional. The additional attendees of the event, as email addresses. For events that are created on the user's primary calendar with at least one other attendee, the current user will automatically be added as an attendee if not already included in this list.", "items": {"type": "string"}, "type": "array"}, "calendarId": {"description": "Optional. The calendar ID to create the event on. The default is the user's primary calendar.", "type": "string"}, "colorId": {"description": "Optional. The color of the event. This is an ID referring to an entry in the calendar's color palette. Event color ID (string `1`-`11`): * 1: Lavender * 2: Sage * 3: Grape * 4: Flamingo * 5: Banana * 6: Tangerine * 7: Peacock * 8: Graphite * 9: Blueberry * 10: Basil * 11: Tomato.", "type": "string"}, "description": {"description": "Optional. Description of the event. Can contain HTML.", "type": "string"}, "endTime": {"description": "Required. The end time of the event. Must be a full ISO 8601 timestamp (e.g., '2026-04-30T10:00:00Z').", "type": "string"}, "googleMeetUrl": {"description": "Optional. Allows attaching an existing Google Meet URL or meeting ID to the event. If set, this URL will be attached to the event instead of generating a new Google Meet room, even if `add_google_meet_url` is set to `true`.", "type": "string"}, "location": {"description": "Optional. Geographic location of the event as free-form text.", "type": "string"}, "notificationLevel": {"description": "Optional. Which email notification should be sent for this event update. Possible values are: * `NONE` - No email notifications are sent. * `EXTERNAL_ONLY` - Only external (non-Calendar) attendees receive email notifications (default). * `ALL` - All event attendees receive email notifications.", "enum": ["NOTIFICATION_LEVEL_UNSPECIFIED", "NONE", "EXTERNAL_ONLY", "ALL"], "type": "string", "x-google-enum-descriptions": ["Default value. Will be treated as EXTERNAL_ONLY.", "No email notifications are sent.", "Only external (non-Calendar) attendees receive email notifications.", "All event attendees receive email notifications."]}, "overrideReminders": {"description": "Optional. Reminders defined for this event, overriding the default reminders for the calendar. If not set, the event will use the default reminders of the calendar.", "items": {"$ref": "#/$defs/Reminder"}, "type": "array"}, "recurrenceData": {"description": "Optional. The recurrence data of the event as RRULE, RDATE, or EXDATE strings per RFC 5545. Each string in the list acts as a separate RFC 5545 line. The API normalizes recurrence strings upon creation (e.g., converting absolute UTC EXDATEs into formulations bound to the event's assigned time zone).", "items": {"type": "string"}, "type": "array"}, "startTime": {"description": "Required. The start time of the event formatted as per ISO 8601.", "type": "string"}, "summary": {"description": "Required. Title of the event.", "type": "string"}, "timeZone": {"description": "Optional. Time zone of the event formatted as a strictly case-sensitive IANA Time Zone Database name (e.g., 'America/Los_Angeles'). Defaults to the user's primary time zone if omitted. Dictates the display time zone, overriding timezone offsets provided in start_time or end_time (e.g. 'Europe/Zurich').", "type": "string"}, "visibility": {"description": "Optional. Visibility of the event. Possible values are: * `default` - Uses the default visibility for events on the calendar. This is the default value. * `public` - The event is public and event details are visible to all readers of the calendar. * `private` - The event is private and only event attendees may view event details.", "type": "string"}}, "required": ["endTime", "startTime", "summary"], "type": "object"}}</function>
<function>{"description": "Updates a calendar event. Use this tool for queries like: * Update the event 'Meeting with Jane' to be one hour later. * Add john.doe@google.com to the meeting tomorrow. Example: update_event( eventId='event123', summary='Meeting with Jane and John' ) # Updates the summary of event with id 'event123' on the primary calendar to 'Meeting with Jane and John'.", "name": "Google Calendar:update_event", "parameters": {"$defs": {"Reminder": {"description": "An event reminder.", "properties": {"method": {"description": "Required. How the reminder is delivered to the user. Possible values are: * `email` - Reminders are sent via email. * `popup` - Reminders are sent via a UI popup.", "type": "string"}, "minutes": {"description": "Required. Number of minutes in advance that the reminder should be delivered.", "format": "int32", "type": "integer"}}, "required": ["method", "minutes"], "type": "object"}}, "description": "Request message for UpdateEvent.", "properties": {"addGoogleMeetUrl": {"description": "Optional. Allows to create or update a Google Meet url for the event. By default, no Google Meet url is created or updated. No Google Meet url is created or updated if Meet is disabled for the user, but the event update will succeed.", "type": "boolean"}, "addedAttendeeEmails": {"description": "Optional. The additional attendees of the event, as email addresses.", "items": {"type": "string"}, "type": "array"}, "calendarId": {"description": "Optional. The calendar ID of the event to update. The default is the user's primary calendar.", "type": "string"}, "colorId": {"description": "Optional. New color ID of the event. Will not be updated if not set. Event color ID (string `1`-`11`): * 1: Lavender * 2: Sage * 3: Grape * 4: Flamingo * 5: Banana * 6: Tangerine * 7: Peacock * 8: Graphite * 9: Blueberry * 10: Basil * 11: Tomato.", "type": "string"}, "description": {"description": "Optional. The new description of the event. Will not be updated if not set.", "type": "string"}, "endTime": {"description": "Optional. The new end time of the event formatted as per ISO 8601. Will not be updated if not set.", "type": "string"}, "eventId": {"description": "Required. The ID of the event to update.", "type": "string"}, "googleMeetUrl": {"description": "Optional. Allows attaching an existing Google Meet URL or meeting ID to the event. If set, this URL will be attached to the event instead of generating a new Google Meet room, even if `add_google_meet_url` is set to `true`.", "type": "string"}, "location": {"description": "Optional. The new location of the event. Will not be updated if not set.", "type": "string"}, "notificationLevel": {"description": "Optional. Which email notification should be sent for this event update. Possible values are: * `NONE` - No email notifications are sent. * `EXTERNAL_ONLY` - Only external (non-Calendar) attendees receive email notifications (default). * `ALL` - All event attendees receive email notifications.", "enum": ["NOTIFICATION_LEVEL_UNSPECIFIED", "NONE", "EXTERNAL_ONLY", "ALL"], "type": "string", "x-google-enum-descriptions": ["Default value. Will be treated as EXTERNAL_ONLY.", "No email notifications are sent.", "Only external (non-Calendar) attendees receive email notifications.", "All event attendees receive email notifications."]}, "overrideReminders": {"description": "Optional. Reminders defined for this event, overriding any existing reminders and the default reminders for the calendar. If set, this will replace all existing reminders on the event. If not set, reminders will not be updated.", "items": {"$ref": "#/$defs/Reminder"}, "type": "array"}, "removedAttendeeEmails": {"description": "Optional. The attendees of the event to remove, as email addresses.", "items": {"type": "string"}, "type": "array"}, "startTime": {"description": "Optional. The new start time of the event formatted as per ISO 8601. Will not be updated if not set.", "type": "string"}, "summary": {"description": "Optional. The new title of the event. Will not be updated if not set.", "type": "string"}, "visibility": {"description": "Optional. New visibility of the event. Possible values are: * `default` - Uses the default visibility for events on the calendar. This is the default value. * `public` - The event is public and event details are visible to all readers of the calendar. * `private` - The event is private and only event attendees may view event details.", "type": "string"}}, "required": ["eventId"], "type": "object"}}</function>
<function>{"description": "Returns a single event from a given calendar. Use this tool for queries like: * Get details for the team meeting. * Show me the event with id event123 on my calendar. Example: get_event( eventId='event123' ) # Returns the event details for the event with id `event123` on the user's primary calendar.", "name": "Google Calendar:get_event", "parameters": {"properties": {"calendarId": {"description": "Optional. The calendar ID to get the event from. The default is the user's primary calendar.", "type": "string"}, "eventId": {"description": "Required. The ID of the event to get.", "type": "string"}}, "required": ["eventId"], "type": "object"}}</function>
<function>{"description": "Deletes a calendar event. Use this tool for queries like: * Delete the event with id event123 on my calendar. To cancel or decline an event, use the respond_to_event tool instead. Example: delete_event( eventId='event123' ) # Deletes the event with id 'event123' on the user's primary calendar.", "name": "Google Calendar:delete_event", "parameters": {"description": "Request message for DeleteEvent.", "properties": {"calendarId": {"description": "Optional. The calendar ID of the event to delete. The default is the user's primary calendar.", "type": "string"}, "eventId": {"description": "Required. The ID of the event to delete.", "type": "string"}, "notificationLevel": {"description": "Optional. Which email notification should be sent for this event update. Possible values are: * `NONE` - No email notifications are sent. * `EXTERNAL_ONLY` - Only external (non-Calendar) attendees receive email notifications (default). * `ALL` - All event attendees receive email notifications.", "enum": ["NOTIFICATION_LEVEL_UNSPECIFIED", "NONE", "EXTERNAL_ONLY", "ALL"], "type": "string", "x-google-enum-descriptions": ["Default value. Will be treated as EXTERNAL_ONLY.", "No email notifications are sent.", "Only external (non-Calendar) attendees receive email notifications.", "All event attendees receive email notifications."]}}, "required": ["eventId"], "type": "object"}}</function>
<function>{"description": "Lists calendar events in a given calendar satisfying the given conditions. Key Features: * Any Calendar ID, which can be user's primary calendar or others. * Time range filtering. * Retrieves ALL events matching the time constraints. If available, use search_events tool instead for searches on the user's primary calendar if: * You are querying for events matching a specific topic, category, or intent (e.g., 'lunch meetings', 'project syncs'). * You need to find the (top K) most relevant events rather than all events satisfying the constraints. * You need keyword or semantic search capabilities. Use this tool for queries like: * What's on my calendar tomorrow? * What's on my calendar for July 14th 2025? * What are my meetings next week? * Do I have any conflicts this afternoon? * What meetings does John have tomorrow? Example: list_events( startTime='2024-09-17T06:00:00', endTime='2024-09-17T12:00:00', pageSize=10 ) # Returns up to 10 calendar events between 6:00 AM and 12:00 PM on September 17, 2024 from the user's primary calendar.", "name": "Google Calendar:list_events", "parameters": {"properties": {"calendarId": {"description": "Optional. The calendar ID to list events from. The default is the user's primary calendar.", "type": "string"}, "endTime": {"description": "Optional. Upper bound (exclusive) for of the time window to search. Defaults to the end of time. Must be an ISO 8601 timestamp strictly greater than start_time. For example, 2026-06-03T10:00:00-07:00, 2026-06-03T10:00:00Z, or 2026-06-03T10:00:00. Milliseconds may be provided but are ignored.", "type": "string"}, "eventTypeFilter": {"description": "Optional. The event types to return. Possible values are: * `default` - Regular events (default). * `outOfOffice` - Out of office events. * `focusTime` - Focus time events. * `workingLocation` - Working location events. * `birthday` - Birthday events. * `fromGmail` - Events from Gmail. If empty, only the following event types are returned: `default`, `outOfOffice`, `focusTime`, `fromGmail`", "items": {"type": "string"}, "type": "array"}, "fullText": {"description": "Optional. Free-form search query to search across title, description, location and attendees. The search is case-insensitive and supports substring matching. It matches events containing all individual terms in the query (AND search), regardless of order. Exact phrase matching is not supported.", "type": "string"}, "orderBy": {"description": "Optional. The order in which events should be returned. Possible values are: * `default` - Unspecified, but deterministic ordering (default). * `startTime` - Order by start time ascending. * `startTimeDesc` - Order by start time descending. * `lastModified` - Order by last modification time ascending.", "type": "string"}, "pageSize": {"description": "Optional. Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty `next_page_token` field in the response. By default the value is 100 events. If set, the page size must be positive and not larger than 250 events.", "format": "int32", "type": "integer"}, "pageToken": {"description": "Optional. A token retrieved from a previous response's nextPageToken field.", "type": "string"}, "startTime": {"description": "Optional. Lower bound (exclusive) for the time window to search. Defaults to the current time if neither time bound is provided, or the beginning of time if only end_time is provided. Must be an ISO 8601 timestamp strictly less than end_time. Milliseconds may be provided but are ignored.", "type": "string"}, "timeZone": {"description": "Optional. Time zone used in the response and to resolve timezone-less dates in the request (formatted as an IANA Time Zone Database name, e.g. `Europe/Zurich`). The default is the time zone of the calendar.", "type": "string"}}, "type": "object"}}</function>
</functions>Good — Google Calendar is connected. I'll set two reminders: one for next week to get it done, and a 30-day warning before your 60-day deadline.

What was the exact date your ACC approval came through?

---

**[USER]**

05/22/2026

---

**[ASSISTANT]**

{
  "id": "i94cq2d1oquprlbsn0qg9qmn2s",
  "status": "confirmed",
  "htmlLink": "https://www.google.com/calendar/event?eid=aTk0Y3EyZDFvcXVwcmxic24wcWc5cW1uMnMgdGhlY3Jld2JsdWVwcmludEBt",
  "created": "2026-05-22T12:23:21Z",
  "updated": "2026-05-22T12:23:21Z",
  "summary": "⚠️ Deadhang Labor LLC — Publish Formation Notice",
  "description": "Time to publish your LLC formation notice in a Maricopa County approved newspaper. You have until July 21, 2026 (60 days from ACC approval on 05/22/2026).\n\nSteps:\n1. Go to azbex.com (Arizona Business Gazette)\n2. Tell them you need to publish an LLC formation notice in Maricopa County\n3. Provide your LLC details: Deadhang Labor LLC\n4. Pay the fee ($30–75)\n5. They run it 3 consecutive weeks\n6. Save the Affidavit of Publication — you'll file it with the ACC\n\nDEADLINE: July 21, 2026 — do not miss this or your LLC status is at risk.",
  "creator": {
    "email": "thecrewblueprint@gmail.com",
    "self": true
  },
  "organizer": {
    "email": "thecrewblueprint@gmail.com",
    "self": true
  },
  "start": {
    "dateTime": "2026-05-29T16:00:00Z",
    "timeZone": "America/Phoenix"
  },
  "end": {
    "dateTime": "2026-05-29T17:00:00Z",
    "timeZone": "America/Phoenix"
  },
  "eventType": "default",
  "overrideReminders": [
    {
      "method": "email",
      "minutes": 1440
    },
    {
      "method": "popup",
      "minutes": 1440
    }
  ]
}
{
  "id": "me4t26m7u0uamjmjufjpemq3k0",
  "status": "confirmed",
  "htmlLink": "https://www.google.com/calendar/event?eid=bWU0dDI2bTd1MHVhbWptanVmanBlbXEzazAgdGhlY3Jld2JsdWVwcmludEBt",
  "created": "2026-05-22T12:23:29Z",
  "updated": "2026-05-22T12:23:29Z",
  "summary": "🚨 Deadhang Labor LLC — Publication Deadline in 30 Days",
  "description": "FINAL WARNING — You have 30 days left to complete your Arizona LLC publication requirement.\n\nDeadline: July 21, 2026\n\nIf you have not already published your formation notice:\n1. Go to azbex.com immediately\n2. Publication runs 3 consecutive weeks — you need to start NOW to finish before the deadline\n3. After completion save the Affidavit of Publication and file it with the ACC\n\nMissing this deadline puts your LLC status at risk.",
  "creator": {
    "email": "thecrewblueprint@gmail.com",
    "self": true
  },
  "organizer": {
    "email": "thecrewblueprint@gmail.com",
    "self": true
  },
  "start": {
    "dateTime": "2026-06-21T16:00:00Z",
    "timeZone": "America/Phoenix"
  },
  "end": {
    "dateTime": "2026-06-21T17:00:00Z",
    "timeZone": "America/Phoenix"
  },
  "eventType": "default",
  "overrideReminders": [
    {
      "method": "popup",
      "minutes": 1440
    },
    {
      "method": "email",
      "minutes": 1440
    }
  ]
}
Done — two reminders added to your Google Calendar:

- **May 29** — do the publication this week while momentum is high
- **June 21** — 30-day final warning before your July 21 deadline

Both have email and popup reminders the day before so you won't miss them.

---

Now — back to your Operating Agreement. I still need a few details to draft it properly.

**What is your full home address?**

---

**[USER]**

9017 E Vine ave, Mesa, AZ 85208

---

**[ASSISTANT]**

Got it.

**3. What is the exact date on your Articles of Organization approval?**

It should be on the document you downloaded from the ACC — today's date most likely, May 22, 2026.

---

**[USER]**

yes

---

**[ASSISTANT]**

Got it.

**4. What is the primary purpose of Deadhang Labor LLC?**

Based on everything we've discussed I'll suggest this — just confirm or adjust:

> *Providing labor contracting services including staging, steel structure assembly, scaffolding, rigging, LED wall installation, lighting, and general production services for live events and entertainment productions.*

Does that accurately describe what Deadhang Labor LLC does, or do you want to add or change anything?

---

**[USER]**

i accept that

---

**[ASSISTANT]**

Almost there.

**5. What is your EIN number?**

It's on the confirmation letter/PDF you downloaded from the IRS — format looks like **XX-XXXXXXX.**

---

**[USER]**

42-2712662

---

**[ASSISTANT]**

Got everything I need. Here's your Operating Agreement:     1	---
     2	name: docx
     3	description: "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation."
     4	license: Proprietary. LICENSE.txt has complete terms
     5	---
     6	
     7	# DOCX creation, editing, and analysis
     8	
     9	## Overview
    10	
    11	A .docx file is a ZIP archive containing XML files.
    12	
    13	## Quick Reference
    14	
    15	| Task | Approach |
    16	|------|----------|
    17	| Read/analyze content | `extract-text`, or unpack for raw XML |
    18	| Create new document | Use `docx-js` - see Creating New Documents below |
    19	| Edit existing document | Unpack → edit XML → repack - see Editing Existing Documents below |
    20	
    21	### Converting .doc to .docx
    22	
    23	Legacy `.doc` files must be converted before editing:
    24	
    25	```bash
    26	python scripts/office/soffice.py --headless --convert-to docx document.doc
    27	```
    28	
    29	### Reading Content
    30	
    31	```bash
    32	# Text extraction as markdown
    33	extract-text document.docx
    34	
    35	# Show tracked changes instead of accepting them
    36	pandoc --track-changes=all document.docx -o output.md
    37	
    38	# Raw XML access
    39	python scripts/office/unpack.py document.docx unpacked/
    40	```
    41	
    42	### Converting to Images
    43	
    44	```bash
    45	python scripts/office/soffice.py --headless --convert-to pdf document.docx
    46	pdftoppm -jpeg -r 150 document.pdf page
    47	```
    48	
    49	### Accepting Tracked Changes
    50	
    51	To produce a clean document with all tracked changes accepted (requires LibreOffice):
    52	
    53	```bash
    54	python scripts/accept_changes.py input.docx output.docx
    55	```
    56	
    57	---
    58	
    59	## Creating New Documents
    60	
    61	Generate .docx files with JavaScript, then validate. Install: `npm install -g docx`
    62	
    63	### Setup
    64	```javascript
    65	const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
    66	        Header, Footer, AlignmentType, PageOrientation, LevelFormat, ExternalHyperlink,
    67	        InternalHyperlink, Bookmark, FootnoteReferenceRun, PositionalTab,
    68	        PositionalTabAlignment, PositionalTabRelativeTo, PositionalTabLeader,
    69	        TabStopType, TabStopPosition, Column, SectionType,
    70	        TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
    71	        VerticalAlign, PageNumber, PageBreak } = require('docx');
    72	
    73	const doc = new Document({ sections: [{ children: [/* content */] }] });
    74	Packer.toBuffer(doc).then(buffer => fs.writeFileSync("doc.docx", buffer));
    75	```
    76	
    77	### Validation
    78	After creating the file, validate it. If validation fails, unpack, fix the XML, and repack.
    79	```bash
    80	python scripts/office/validate.py doc.docx
    81	```
    82	
    83	### Page Size
    84	
    85	```javascript
    86	// CRITICAL: docx-js defaults to A4, not US Letter
    87	// Always set page size explicitly for consistent results
    88	sections: [{
    89	  properties: {
    90	    page: {
    91	      size: {
    92	        width: 12240,   // 8.5 inches in DXA
    93	        height: 15840   // 11 inches in DXA
    94	      },
    95	      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } // 1 inch margins
    96	    }
    97	  },
    98	  children: [/* content */]
    99	}]
   100	```
   101	
   102	**Common page sizes (DXA units, 1440 DXA = 1 inch):**
   103	
   104	| Paper | Width | Height | Content Width (1" margins) |
   105	|-------|-------|--------|---------------------------|
   106	| US Letter | 12,240 | 15,840 | 9,360 |
   107	| A4 (default) | 11,906 | 16,838 | 9,026 |
   108	
   109	**Landscape orientation:** docx-js swaps width/height internally, so pass portrait dimensions and let it handle the swap:
   110	```javascript
   111	size: {
   112	  width: 12240,   // Pass SHORT edge as width
   113	  height: 15840,  // Pass LONG edge as height
   114	  orientation: PageOrientation.LANDSCAPE  // docx-js swaps them in the XML
   115	},
   116	// Content width = 15840 - left margin - right margin (uses the long edge)
   117	```
   118	
   119	### Styles (Override Built-in Headings)
   120	
   121	Use Arial as the default font (universally supported). Keep titles black for readability.
   122	
   123	```javascript
   124	const doc = new Document({
   125	  styles: {
   126	    default: { document: { run: { font: "Arial", size: 24 } } }, // 12pt default
   127	    paragraphStyles: [
   128	      // IMPORTANT: Use exact IDs to override built-in styles
   129	      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
   130	        run: { size: 32, bold: true, font: "Arial" },
   131	        paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } }, // outlineLevel required for TOC
   132	      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
   133	        run: { size: 28, bold: true, font: "Arial" },
   134	        paragraph: { spacing: { before: 180, after: 180 }, outlineLevel: 1 } },
   135	    ]
   136	  },
   137	  sections: [{
   138	    children: [
   139	      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Title")] }),
   140	    ]
   141	  }]
   142	});
   143	```
   144	
   145	### Lists (NEVER use unicode bullets)
   146	
   147	```javascript
   148	// ❌ WRONG - never manually insert bullet characters
   149	new Paragraph({ children: [new TextRun("• Item")] })  // BAD
   150	new Paragraph({ children: [new TextRun("\u2022 Item")] })  // BAD
   151	
   152	// ✅ CORRECT - use numbering config with LevelFormat.BULLET
   153	const doc = new Document({
   154	  numbering: {
   155	    config: [
   156	      { reference: "bullets",
   157	        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
   158	          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
   159	      { reference: "numbers",
   160	        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
   161	          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
   162	    ]
   163	  },
   164	  sections: [{
   165	    children: [
   166	      new Paragraph({ numbering: { reference: "bullets", level: 0 },
   167	        children: [new TextRun("Bullet item")] }),
   168	      new Paragraph({ numbering: { reference: "numbers", level: 0 },
   169	        children: [new TextRun("Numbered item")] }),
   170	    ]
   171	  }]
   172	});
   173	
   174	// ⚠️ Each reference creates INDEPENDENT numbering
   175	// Same reference = continues (1,2,3 then 4,5,6)
   176	// Different reference = restarts (1,2,3 then 1,2,3)
   177	```
   178	
   179	### Tables
   180	
   181	**CRITICAL: Tables need dual widths** - set both `columnWidths` on the table AND `width` on each cell. Without both, tables render incorrectly on some platforms.
   182	
   183	```javascript
   184	// CRITICAL: Always set table width for consistent rendering
   185	// CRITICAL: Use ShadingType.CLEAR (not SOLID) to prevent black backgrounds
   186	const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
   187	const borders = { top: border, bottom: border, left: border, right: border };
   188	
   189	new Table({
   190	  width: { size: 9360, type: WidthType.DXA }, // Always use DXA (percentages break in Google Docs)
   191	  columnWidths: [4680, 4680], // Must sum to table width (DXA: 1440 = 1 inch)
   192	  rows: [
   193	    new TableRow({
   194	      children: [
   195	        new TableCell({
   196	          borders,
   197	          width: { size: 4680, type: WidthType.DXA }, // Also set on each cell
   198	          shading: { fill: "D5E8F0", type: ShadingType.CLEAR }, // CLEAR not SOLID
   199	          margins: { top: 80, bottom: 80, left: 120, right: 120 }, // Cell padding (internal, not added to width)
   200	          children: [new Paragraph({ children: [new TextRun("Cell")] })]
   201	        })
   202	      ]
   203	    })
   204	  ]
   205	})
   206	```
   207	
   208	**Table width calculation:**
   209	
   210	Always use `WidthType.DXA` — `WidthType.PERCENTAGE` breaks in Google Docs.
   211	
   212	```javascript
   213	// Table width = sum of columnWidths = content width
   214	// US Letter with 1" margins: 12240 - 2880 = 9360 DXA
   215	width: { size: 9360, type: WidthType.DXA },
	< truncated lines 216-378 >
   379	```
   380	
   381	### Critical Rules for docx-js
   382	
   383	- **Set page size explicitly** - docx-js defaults to A4; use US Letter (12240 x 15840 DXA) for US documents
   384	- **Landscape: pass portrait dimensions** - docx-js swaps width/height internally; pass short edge as `width`, long edge as `height`, and set `orientation: PageOrientation.LANDSCAPE`
   385	- **Never use `\n`** - use separate Paragraph elements
   386	- **Never use unicode bullets** - use `LevelFormat.BULLET` with numbering config
   387	- **PageBreak must be in Paragraph** - standalone creates invalid XML
   388	- **ImageRun requires `type`** - always specify png/jpg/etc
   389	- **Always set table `width` with DXA** - never use `WidthType.PERCENTAGE` (breaks in Google Docs)
   390	- **Tables need dual widths** - `columnWidths` array AND cell `width`, both must match
   391	- **Table width = sum of columnWidths** - for DXA, ensure they add up exactly
   392	- **Always add cell margins** - use `margins: { top: 80, bottom: 80, left: 120, right: 120 }` for readable padding
   393	- **Use `ShadingType.CLEAR`** - never SOLID for table shading
   394	- **Never use tables as dividers/rules** - cells have minimum height and render as empty boxes (including in headers/footers); use `border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 1 } }` on a Paragraph instead. For two-column footers, use tab stops (see Tab Stops section), not tables
   395	- **TOC requires HeadingLevel only** - no custom styles on heading paragraphs
   396	- **Override built-in styles** - use exact IDs: "Heading1", "Heading2", etc.
   397	- **Include `outlineLevel`** - required for TOC (0 for H1, 1 for H2, etc.)
   398	
   399	---
   400	
   401	## Editing Existing Documents
   402	
   403	**Follow all 3 steps in order.**
   404	
   405	### Step 1: Unpack
   406	```bash
   407	python scripts/office/unpack.py document.docx unpacked/
   408	```
   409	Extracts XML, pretty-prints, merges adjacent runs, and converts smart quotes to XML entities (`&#x201C;` etc.) so they survive editing. Use `--merge-runs false` to skip run merging.
   410	
   411	### Step 2: Edit XML
   412	
   413	Edit files in `unpacked/word/`. See XML Reference below for patterns.
   414	
   415	**Use "Claude" as the author** for tracked changes and comments, unless the user explicitly requests use of a different name.
   416	
   417	**Use the Edit tool directly for string replacement. Do not write Python scripts.** Scripts introduce unnecessary complexity. The Edit tool shows exactly what is being replaced.
   418	
   419	**CRITICAL: Use smart quotes for new content.** When adding text with apostrophes or quotes, use XML entities to produce smart quotes:
   420	```xml
   421	<!-- Use these entities for professional typography -->
   422	<w:t>Here&#x2019;s a quote: &#x201C;Hello&#x201D;</w:t>
   423	```
   424	| Entity | Character |
   425	|--------|-----------|
   426	| `&#x2018;` | ‘ (left single) |
   427	| `&#x2019;` | ’ (right single / apostrophe) |
   428	| `&#x201C;` | “ (left double) |
   429	| `&#x201D;` | ” (right double) |
   430	
   431	**Adding comments:** Use `comment.py` to handle boilerplate across multiple XML files (text must be pre-escaped XML):
   432	```bash
   433	python scripts/comment.py unpacked/ 0 "Comment text with &amp; and &#x2019;"
   434	python scripts/comment.py unpacked/ 1 "Reply text" --parent 0  # reply to comment 0
   435	python scripts/comment.py unpacked/ 0 "Text" --author "Custom Author"  # custom author name
   436	```
   437	Then add markers to document.xml (see Comments in XML Reference).
   438	
   439	### Step 3: Pack
   440	```bash
   441	python scripts/office/pack.py unpacked/ output.docx --original document.docx
   442	```
   443	Validates with auto-repair, condenses XML, and creates DOCX. Use `--validate false` to skip.
   444	
   445	**Auto-repair will fix:**
   446	- `durableId` >= 0x7FFFFFFF (regenerates valid ID)
   447	- Missing `xml:space="preserve"` on `<w:t>` with whitespace
   448	
   449	**Auto-repair won't fix:**
   450	- Malformed XML, invalid element nesting, missing relationships, schema violations
   451	
   452	### Common Pitfalls
   453	
   454	- **Replace entire `<w:r>` elements**: When adding tracked changes, replace the whole `<w:r>...</w:r>` block with `<w:del>...<w:ins>...` as siblings. Don't inject tracked change tags inside a run.
   455	- **Preserve `<w:rPr>` formatting**: Copy the original run's `<w:rPr>` block into your tracked change runs to maintain bold, font size, etc.
   456	
   457	---
   458	
   459	## XML Reference
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

Every business expense from that point forward goes on that card — zero exceptions. Gas to a gig, tools, gear, phone bill percentage — all of it.

---

Are you inside the Found app right now, or are you still in setup?