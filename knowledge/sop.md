# MARKET-FIRST WORKFLOW FOR NANO BANANA
## Quick-Start Cover Generation SOP

**Purpose:** Tactical 8-step workflow for efficient cover creation
**Time:** 1-2 hours from concept to final
**Companion Document:** Amazon Cover Strategy Knowledge File (for deep dives)

---

## BEFORE YOU START

**This workflow assumes you have:**
- Already chosen your strategy (if not, see Knowledge File Part XVII)
- Basic familiarity with your category (if not, do Deep Research first)
- Access to Google Nano Banana

**When to use Knowledge File instead:**
- Entering a new category → Knowledge File Part VIII
- Print cover needs → Print Cover Wrap Workflow (below) + Knowledge File Parts XII-XIII
- Multi-language publishing → Knowledge File Parts XVIII-XIX
- Brand consistency planning → Knowledge File Part XI
- Cover refresh decisions → Knowledge File Part XX
- Technical specifications → Knowledge File Part XII

---

## PHASE 1: MARKET INTELLIGENCE (25-30 Minutes)

### Step 1: Market Scan (Amazon-Only)

**Action:** Search your primary keyword on Amazon. Screenshot the top 20-30 organic covers.

**The Filter:** Ignore blurbs and reviews. Extract only these four signals:

| Signal | What to Look For | Example Output |
|--------|------------------|----------------|
| **Color Families** | Dominant palette patterns | "High-contrast navy/gold" or "Muted earth tones" |
| **Dominant Objects** | Recurring imagery types | "Single symbolic object" or "Environmental scenes" |
| **Typography Style** | Font patterns | "Bold sans-serif" or "Elegant serif" or "Textured/distressed" |
| **Layout Pattern** | Composition trends | "Top-heavy text, bottom-third focal point" |

**Output:** A "Visual Rule List" AND a "Category Palette Lock"

Example:
```
Category: Christian Prayer
- Colors: Deep blue + gold accents, OR cream/white + earth tones
- Objects: Keys, light rays, open doors, hands (implied)
- Typography: Bold serif titles, minimal subtitle, author name small
- Layout: 60-70% title area top, 30-40% imagery bottom

CATEGORY PALETTE LOCK:
Temperature: Warm (golden, amber, cream)
Brightness: Light/bright (NOT dark or moody)
Dominant colors: Cream, soft gold, sage green, warm white
Avoid: Dark backgrounds, heavy shadows, black/navy dominance
```

**The Rule:** If the market uses bold white text on dark blue, you do too (unless you're deliberately using Pattern Interrupt strategy).

**The Palette Rule:** The Category Palette Lock is a BINDING CONSTRAINT on all image generation. Every prompt must explicitly include color/mood directions that match it. Never let the AI model choose its own palette — different models default to different aesthetics (e.g., Imagen tends darker, Gemini tends warmer). Always specify.

*→ For deeper research, see Knowledge File Part VIII*

---

### Step 2: Audience Compression (Emotional Anchor)

**Action:** Read only the Intro, Chapter 1, and the Final Chapter of your book.

**The Question:** What feeling does the reader want when they click "Buy"?

| Core Emotion | Visual Direction |
|--------------|------------------|
| Relief | Soft colors, open space, calming imagery |
| Authority | Bold typography, structured layout, premium textures |
| Strength | Dynamic composition, strong contrast, solid imagery |
| Curiosity | Symbolic/metaphorical imagery, visual mystery |
| Peace | Minimal elements, gentle light, serene colors |
| Hope | Light breaking through, warm tones, upward movement |

**Output:** One sentence:

> "This cover must signal **[EMOTION]** in under 1 second at thumbnail size."

*→ For audience research frameworks, see Knowledge File Part V (Strategy 3)*

---

## PHASE 2: STRUCTURAL DESIGN (15 Minutes)

### Step 3: Concept Framing (5 Structures)

**Don't iterate on colors; iterate on structure.**

Create five one-line concepts using these five structural approaches:

| # | Structure | Description | Example Concept |
|---|-----------|-------------|-----------------|
| 1 | **Symbolic Minimal** | One object, clean negative space | "Single brass key on linen, 70% negative space" |
| 2 | **Environmental** | A specific place or heavy atmosphere | "Misty forest path with morning light breaking through" |
| 3 | **Human Presence (Implied)** | Silhouette, posture, or hands (avoid full faces) | "Silhouetted hands releasing a dove into golden light" |
| 4 | **Abstract Tension** | Motion, fractures, high-contrast shadows | "Light piercing through cracked darkness, dramatic contrast" |
| 5 | **Authority Signal** | Typography-first, layout-driven design | "Bold centered title on subtle textured background" |

**Write your five concepts:**
1. Symbolic Minimal: _________________________________
2. Environmental: _________________________________
3. Human Presence: _________________________________
4. Abstract Tension: _________________________________
5. Authority Signal: _________________________________

*→ For detailed structure explanations, see Knowledge File Part IV*

---

### Step 4: Controlled Generation (Nano Banana Phase)

For each of your 5 concepts, generate 4-6 variations.

**Generation Locks (Non-Negotiable):**

| Lock | Setting | Why |
|------|---------|-----|
| Aspect Ratio | 2:3 | Standard book cover proportion |
| Camera | Medium or Wide | Avoid macro/extreme close-ups |
| Layout Logic | Professional nonfiction | Prevents "artistic" failures |
| Text | No text in image | Typography added separately |
| **Palette** | **Match Category Palette Lock** | **Prevents genre-mismatched covers** |

**Palette Enforcement:** Every prompt MUST include explicit color and mood keywords from the Category Palette Lock. Example: if the lock says "warm/light," your prompt must include phrases like "BRIGHT and WARM palette, soft golden tones, cream sky, NOT dark or moody." Never rely on the model's default color choices.

**Quick Prompt Template:**

```
Book cover design for Amazon Kindle. [Your Concept Line].
[Lighting + Mood]. High contrast, clean composition.
No text artifacts. Centered focal point.
[Genre] aesthetic. Aspect ratio 2:3.
```

**Example Prompts for Each Structure:**

**Symbolic Minimal:**
```
Book cover design for Amazon Kindle. Single antique brass key
resting on rough linen cloth. Warm golden hour side-lighting,
peaceful mood. High contrast, clean composition. No text artifacts.
Centered focal point. Christian devotional aesthetic. Aspect ratio 2:3.
```

**Environmental:**
```
Book cover design for Amazon Kindle. Misty forest path with
soft morning light filtering through trees. Atmospheric, contemplative mood.
High contrast, clean composition. No text artifacts.
Path leading to light in center. Christian spiritual growth aesthetic.
Aspect ratio 2:3.
```

**Human Presence (Implied):**
```
Book cover design for Amazon Kindle. Silhouetted hands releasing
a white dove into golden sunset light. Hopeful, uplifting mood.
High contrast, clean composition. No text artifacts.
Hands in lower third, dove rising to center. Christian worship aesthetic.
Aspect ratio 2:3.
```

**Abstract Tension:**
```
Book cover design for Amazon Kindle. Dramatic light breaking through
cracked darkness, golden rays piercing through black fractured surface.
Powerful, breakthrough mood. High contrast, clean composition.
No text artifacts. Light source in upper center.
Christian spiritual warfare aesthetic. Aspect ratio 2:3.
```

**Authority Signal:**
```
Book cover design for Amazon Kindle. Rich linen texture background
in deep navy blue with subtle gold leaf accents. Premium, authoritative mood.
High contrast, clean composition. No text artifacts.
Large centered negative space for typography.
Christian Bible study aesthetic. Aspect ratio 2:3.
```

**Generation Count:** 5 concepts × 4-6 variations = 20-30 images

*→ For detailed prompt architecture, see Knowledge File Part IX*

---

## PHASE 3: THE "COLD CRITERIA" SELECTION

### Step 5: The Thumbnail Test (Non-Negotiable)

**Action:** Shrink every candidate to **60px height**. View them at arm's length.

**Discard Instantly If:**
- [ ] The focal point is muddy or unclear
- [ ] It feels "artistic" but doesn't tell a story in 1 second
- [ ] The contrast is too low to pop against a white background
- [ ] You can't immediately tell what genre it belongs to
- [ ] The color palette contradicts the Category Palette Lock (e.g., dark/moody when market is warm/light)

**Survivors:** You should have 5-10 candidates remaining.

*→ For complete thumbnail testing, see Knowledge File Part XVI*

---

### Step 6: Sales Likelihood Decision

**The Rule:** Choose the cover that looks the most **boringly legitimate** next to the Top 10 bestsellers.

**The Criteria:**
1. Does it match the category pattern from Step 1? □ Yes □ No
2. Does it signal the emotion from Step 2? □ Yes □ No
3. Is it "too clever"? □ Yes (kill it) □ No (keep it)

**Decision Framework:**

| Score | Meaning | Action |
|-------|---------|--------|
| 3 Yes | Strong candidate | Proceed to refinement |
| 2 Yes, 1 No | Acceptable | Consider if time allows improvement |
| 1 Yes, 2 No | Weak | Likely regenerate or pivot |
| 0 Yes | Wrong direction | Return to Step 3 |

**Output:** One winner (or 2-3 close finalists for micro-iteration)

*→ For detailed decision rubric with calibration, see Knowledge File Part XVI*

---

## PHASE 4: SURGICAL REFINEMENT

### Step 7: Micro-Iteration Loop

Now use Nano Banana's edit functions to **polish, not reinvent**.

**What TO Change:**
- Contrast (increase if needed)
- Scale of the object (bigger focal point)
- Lighting direction (optimize for drama/clarity)
- Background clutter (simplify)

**What NOT to Change:**
- The core concept
- The subject matter
- The overall composition

**Limit:** Run **3-5 micro-generations maximum**. Stop once clarity is maximized.

**Stop When:**
- Thumbnail test passes completely
- Further changes are lateral moves, not improvements
- You've hit 5 micro-iterations

*→ For detailed iteration strategies, see Knowledge File Part XV*

---

### Step 8: Final Amazon Prep

**A. Typography (Outside Nano Banana)**

Add your final Title/Author name using Photoshop, Canva, or similar for 100% control over kerning and legibility.

**Typography Checklist:**
- [ ] Title is largest element
- [ ] Author name is readable but secondary
- [ ] Subtitle (if any) doesn't compete with title
- [ ] Font matches category norms from Step 1
- [ ] Text placement leaves breathing room

**B. The Stress Tests**

| Test | Action | Pass Criteria |
|------|--------|---------------|
| Thumbnail | Shrink to 60px height, view at arm's length | Title readable, focal point clear |
| Grayscale | Convert temporarily to grayscale | Title still pops, contrast holds |
| Competitor Grid | Place next to top 5 competitors | Yours fits in but stands out slightly |

**C. Export**

| Format | Specs | Use |
|--------|-------|-----|
| Kindle eBook | JPEG, 1600×2560px (W×H), RGB | Primary listing |
| Paperback | PDF preferred, 300 DPI, with bleed | Print version |

*→ For complete specifications and print cover details, see Knowledge File Parts XII-XIV*

---

## QUICK REFERENCE CARD

### The 8 Steps at a Glance

| Phase | Step | Time | Output |
|-------|------|------|--------|
| **1. Intel** | 1. Market Scan | 15 min | Visual Rule List |
| | 2. Audience Compression | 10 min | Emotion sentence |
| **2. Design** | 3. Concept Framing | 5 min | 5 concept lines |
| | 4. Controlled Generation | 10 min | 20-30 images |
| **3. Select** | 5. Thumbnail Test | 5 min | 5-10 survivors |
| | 6. Sales Likelihood | 5 min | 1 winner |
| **4. Refine** | 7. Micro-Iteration | 10 min | Polished image |
| | 8. Final Prep | 15 min | Upload-ready files |

**Total: ~75 minutes** (varies with generation speed)

---

### Generation Locks (Copy-Paste Reference)

```
Dimensions: 5.5 x 8.5 inches (11:17 ratio, tall portrait)
Imagen models: --aspect-ratio 3:4 (closest supported)
Camera: Medium or Wide
Layout: Professional nonfiction
Focal Point: Centered or rule-of-thirds
```

### Quick Prompt Template (Copy-Paste Reference)

```
Book cover design for Amazon Kindle. [CONCEPT].
[LIGHTING + MOOD]. High contrast, clean composition.
No text artifacts. Centered focal point.
[GENRE] aesthetic. Aspect ratio 2:3.
```

---

## SERIES WORKFLOW (Quick Reference)

### Before You Start: Is This a Series Book?

| Situation | Action |
|-----------|--------|
| **Standalone book** | Normal workflow, no series logic |
| **Book 1 of new series** | Normal workflow → save Series Template Lock in Phase 6 |
| **Book 2+ of existing series** | Load Series Template Lock → constrained workflow |
| **"This is actually a series" (after the fact)** | Retroactive Extraction → create template from finished cover |

### If Series Template Lock Exists (Book 2+)

1. Load the template from `templates/series/[series-name].json`
2. Market research still happens, but the template overrides visual identity
3. **Skip concept structure selection** — use the locked structure
4. **Change ONLY:** title, subtitle, and the designated swap element (e.g., different scene)
5. **Keep LOCKED:** color palette, typography, composition, lighting, material treatment
6. Add scoring criterion: **Series Consistency** (1-5) — "Same series as book 1?"

### After Finalizing Book 1

Save a Series Template Lock capturing:
- Concept structure and imagery style
- Color palette (temperature, brightness, specific colors, colors to avoid)
- Typography (style, placement, hierarchy)
- Composition (layout zones, focal direction)
- Lighting and material treatment
- Model and settings used
- The exact prompt

### Retroactive Extraction

When a finished cover needs to become a series template after the fact:
1. Read the final cover image + its `metadata.json`
2. Extract all visual DNA (palette, typography, composition, lighting, etc.)
3. Save to `templates/series/[series-name].json`
4. Confirm with user before using as a constraint

**See CLAUDE.md "Series Cover Workflow" for full schema and detailed instructions.**

### Existing Covers Workflow (Unified Entry Point)

Use when the user has existing covers that need updating — whether harmonizing, refreshing, or fully redesigning. **Always audit first, then branch.**

**Phase 1: Audit (ALWAYS runs)**

1. **H1: Visual Audit** — Import all existing covers, score each, extract visual DNA from each, build comparison matrix
2. **H2: Common DNA Extraction** — Find shared traits (color, typography, composition, imagery, lighting), identify divergent traits, assess strength:
   - **Strong (3+ shared):** Recommend Harmonization
   - **Medium (1-2 shared):** Recommend Harmonization (with heavy frame work)
   - **Weak (0 shared):** Recommend Full Regeneration
3. **H2.5: Branch Point** — Present the audit report and recommend a path. User chooses:

**Path A: Harmonization** (preserve existing identity, add cohesion)

4. **H3: Define Unified Frame** — Lock: palette, typography, author treatment, layout zones, background/border. Flex: central imagery, title, accent color per book
5. **H4: Regenerate** — Generate 4 candidates per book using locked frame + unique imagery. Score for Series Consistency AND Original Identity Preservation (both must be 4+/5). Present all covers side-by-side as a set.
6. **H5: Final Output** — Export all together, generate series grid thumbnail, save as Series Template Lock for future books

**Path B: Full Regeneration** (start fresh, discard existing designs)

4. **R1: Anchor Selection** — Use best existing cover as inspiration OR clean slate. Run fresh market research.
5. **R2: Anchor Book Generation** — Full standard pipeline for the lead cover. Create Series Template Lock.
6. **R3: Series Rollout** — Generate all remaining covers using the new template. Score for Series Consistency (4+/5).
7. **R4: Final Output** — Export all together, series grid thumbnail, template already saved.

**Key scoring:**
- Harmonization: Series Consistency (4+) AND Original Identity Preservation (4+)
- Full Regeneration: Standard rubric (22+) AND Series Consistency (4+)

**See CLAUDE.md "Existing Covers Workflow" for full schema, template format, and quality gates.**

### Pre-Written Series (Titles + Descriptions, No Manuscripts)

Use when the user provides titles, subtitles, and short descriptions for books that haven't been written yet.

**The 6-Phase Process:**

1. **P1: Series Analysis** — Collect metadata for all books. Analyze as a whole: series theme, core emotion, sub-genre, visual thread. Map each book to a unique visual element.
2. **P2: Market Research** — Standard Amazon scan for the category. Select ONE concept structure for the entire series.
3. **P3: Series Blueprint** — Build a unified design spec: locked elements (palette, typography, composition, lighting) + per-book flexible elements (unique imagery). Present to user for approval.
4. **P4: Anchor Book Generation** — Generate the lead cover using full pipeline. Create Series Template Lock from the finalized anchor.
5. **P5: Series Rollout** — Generate remaining covers using the template. Score for Series Consistency (4+/5). Present full lineup side-by-side.
6. **P6: Final Output** — Export all covers, series grid, blueprint document, and template.

**Key scoring:** Standard rubric (22+) AND Series Consistency (4+)

**Thin descriptions?** Ask clarifying questions. Default to Environmental or Symbolic Minimal structures.

**See CLAUDE.md "Pre-Written Series Workflow" for full blueprint schema and quality gates.**

### Single Cover Refresh (Underperforming Cover)

Use when a single book's cover isn't selling and needs redesigning. Not a series situation.

**The 3-Phase Process:**

1. **F1: Diagnosis** — Import existing cover, score it, run fresh market research, diagnose why it's failing (Palette Mismatch, Weak Thumbnail, Genre Misread, Dated Design, Technical Issues, or Concept Failure). Present diagnosis and recommend: Iterate (fix execution) or Pivot (new concept).
2. **F2: Redesign** — If iterating: same concept, fix diagnosed issues, 4-6 variations, score with "Improvement Over Original" (4+). If pivoting: full concept development from scratch.
3. **F3: Comparison and Output** — Side-by-side old vs new, stress tests, export. Archive old cover to `output/[book-title]/previous/`.

**See CLAUDE.md "Single Cover Refresh Workflow" for diagnosis table and quality gates.**

### Box Set / Omnibus Cover

Use when combining multiple books into one product (e.g., "Complete Collection: Books 1-4").

**The 3-Phase Process:**

1. **B1: Collection Analysis** — Gather individual covers, extract series DNA, determine strategy by book count:
   - 2-3 books → Mini-Grid (show individual cover thumbnails)
   - 4-6 books → Elevated Series Identity (amplified series DNA, "Complete Collection" branding)
   - 7+ books → Abstract Collection Signal (premium typography-dominant, no individual covers)
2. **B2: Concept Development** — Build the box set concept, research competing box sets in category. Present to user.
3. **B3: Generation and Output** — Generate 4-6 candidates. Score with "Collection Signal" (4+/5): must clearly read as a collection, not a single book.

**See CLAUDE.md "Box Set / Omnibus Cover Workflow" for approach details and quality gates.**

### Companion Product Covers (Workbook, Journal, Study Guide)

Use when creating a cover for a supplementary product that accompanies a main book.

**The 3-Phase Process:**

1. **C1: Parent Book Analysis** — Import parent cover, extract visual DNA, determine companion type (Workbook, Journal, Study Guide, Devotional Companion, Leader's Guide). Define what's inherited (locked) vs what's modified (adjusted).
2. **C2: Concept Development** — Three approaches:
   - Shared Scene + Type Overlay (same imagery + companion visual layer)
   - Palette Match + Different Imagery (same palette, new imagery signaling product type)
   - Abstracted Parent (simplified/softened version of parent imagery)
3. **C3: Generation and Output** — Generate 4-6 candidates. Score with "Parent Relationship" (4+) AND "Product Type Signal" (4+): must look related to parent but NOT be confused with it.

**See CLAUDE.md "Companion Product Cover Workflow" for companion type table and quality gates.**

### Print Cover Wrap (Paperback / Hardcover)

Use when the user has a finalized front cover and needs a full print wrap (front + spine + back) for KDP paperback or hardcover.

**The 4-Phase Process:**

1. **W1: Dimension Calculation** — Calculate spine width from page count + paper type using KDP formulas. Spine = (pages × paper_thickness) + 0.06". Full wrap = back + spine + front + bleed. If user provided a KDP template, parse it to verify. Present dimensions for confirmation.
2. **W2: Content Preparation** — Validate front cover resolution. Prepare back cover content (blurb, author bio, author photo). Prepare spine content (title + author if pages >= 79). Confirm design decisions (background color, typography, photo treatment).
3. **W3: Compositing** — Use `scripts/print_cover_wrap.py compose` to assemble: back cover (left) + spine (center) + front cover (right) + bleed extension. Outputs PNG + PDF at 300 DPI. Overlay KDP template if provided.
4. **W4: Review and Output** — Present full wrap for review. Verify: front cover positioning, spine centering, blurb legibility, barcode zone clear, bleed correct, nothing in unsafe margins. Export to `output/[book-title]/print/`.

**Key specs:** 300 DPI, 0.125" bleed, 0.25" safe margin, barcode zone 2"×1.2" lower-right back, min 79 pages for spine text.

**See CLAUDE.md "Print Cover Wrap Workflow" for full KDP specs table and quality gates.**

---

## WHEN TO GO DEEPER

**Stop and consult Knowledge File if:**

| Situation | Knowledge File Section |
|-----------|----------------------|
| None of your concepts are working | Part IV (Structures), Part V (Strategies) |
| Thumbnail test keeps failing | Part XVI (Decision Tools) |
| Need print cover with spine | Parts XII-XIII |
| Creating Spanish/German version | Parts XVIII-XIX |
| Cover for series (need consistency) | Part XI |
| Existing series covers need updating | Existing Covers Workflow (above) + CLAUDE.md |
| Series covers from titles only (no manuscripts) | Pre-Written Series Workflow (above) + CLAUDE.md |
| Single cover underperforming | Single Cover Refresh (above) + CLAUDE.md |
| Need a box set / collection cover | Box Set Workflow (above) + CLAUDE.md |
| Need a workbook / journal / study guide cover | Companion Product Workflow (above) + CLAUDE.md |
| Need a print cover (paperback/hardcover wrap) | Print Cover Wrap Workflow (above) + CLAUDE.md |
| Entering unfamiliar category | Part VIII (Deep Research) |
| Unsure about KDP requirements | Part XII, Appendix C |
| Cover is underperforming | Part XX (Refresh Strategy) |

---

## THE "BORING" TRUTH

> The winner is usually the **least "creative" image** and the **most "pattern-compliant" one**.

Your job is not to make art. Your job is to make a conversion tool that:
1. Belongs in the category
2. Signals the right emotion
3. Wins the click
4. Converts to a sale

Everything else is vanity.

---

*Quick-Start Workflow Version 2.0 | February 2026*

*For comprehensive reference: See "Amazon Cover Strategy Knowledge File"*
