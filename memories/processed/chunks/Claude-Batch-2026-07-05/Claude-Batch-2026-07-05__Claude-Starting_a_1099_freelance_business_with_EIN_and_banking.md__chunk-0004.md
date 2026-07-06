---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Starting_a_1099_freelance_business_with_EIN_and_banking.md__chunk-0004",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Starting_a_1099_freelance_business_with_EIN_and_banking.md",
  "chunk_index": 4,
  "chunk_count_for_source": 14,
  "char_start": 34062,
  "char_end": 46058,
  "source_sha256": "470b1f10705b5ba9d6b37f3959490d6d820c379957d1c86606620dfbe181421f",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

"middle" dominant-baseline="central">Detect foreign antigens</text>
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
- **Color encodes intensity**, not category. For physical subjects: warm ramps (amber, coral, red) = heat/energy/pressure, cool ramps (blue, teal) = cold/calm, gray = inert structure. For abstract subjects: warm = active/high-weight/attended-to, cool or gray = dormant/low-weight/ignored.
