# Cover Prompt Templates

## Master Formula
```
[Subject] + [Metaphorical Context] + [Tactile Material] + [Lighting Description] + [Composition Constraint]
```

## Generation Locks (append to EVERY prompt)
```
High contrast, clean composition. Centered focal point.
Exact 5.5 x 8.5 inch book cover proportions, tall portrait rectangle, significantly taller than wide, standard paperback book shape.
Professional book cover quality.
{CATEGORY_PALETTE_LOCK}
```

## Market Palette Compliance (MANDATORY)

Before generating ANY cover, you MUST have a Category Palette Lock from Phase 2 market research. Insert the palette direction into EVERY prompt. Example palette lock phrases:

- **Warm/light market:** `"BRIGHT and WARM color palette: soft golden yellows, warm creams, light sage greens. Light airy atmosphere, NOT dark or moody."`
- **Dark/bold market:** `"BOLD and DRAMATIC color palette: deep navy, rich gold accents, strong contrast. Authoritative and premium feel."`
- **Soft/muted market:** `"SOFT and MUTED color palette: dusty rose, sage green, cream. Gentle and contemplative, no harsh contrasts."`

**NEVER generate without explicit palette direction.** Different AI models default to different aesthetics (Imagen tends darker, Gemini tends warmer). Always specify the palette to override model defaults.

**Instant disqualifier:** Any cover whose color temperature or brightness contradicts the Category Palette Lock gets rejected, no matter how good the composition is.

---

## Structure 1: Symbolic Minimal

### Template
```
Book cover for "{TITLE}" by {AUTHOR}. {SUBTITLE_LINE}
Single {OBJECT} {OBJECT_CONTEXT}.
{MATERIAL_TEXTURE} background.
{LIGHTING}, {MOOD} mood.
{COMPOSITION_SPACE} negative space for large title placement.
{GENRE} aesthetic. High contrast, clean composition.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "{TITLE}" in {FONT_STYLE}, author name "{AUTHOR}" smaller below.
```

### Example
```
Book cover for "The Master Key" by Dan Smith. Subtitle "Unlocking God's Purpose for Your Life."
Single antique brass key resting on rough linen cloth.
Natural linen textile background with visible woven fabric texture.
Warm golden hour side-lighting, peaceful mood.
65% negative space above for large title placement.
Christian devotional aesthetic. High contrast, clean composition.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "The Master Key" in bold serif font, author name "Dan Smith" smaller below.
```

### Object Bank (Christian Nonfiction)
- Keys (authority, unlocking, Kingdom access)
- Anchors (hope, stability — Hebrews 6:19)
- Single candle/flame (Holy Spirit, presence)
- Mustard seed (faith, growth)
- Crown (identity, authority, inheritance)
- Compass (guidance, direction)
- Open book/Bible (Word-centered)
- Sword (spiritual warfare, Word of God)
- Oil lamp (anointing, wisdom)
- Shield (faith, protection)

---

## Structure 2: Environmental

### Template
```
Book cover for "{TITLE}" by {AUTHOR}. {SUBTITLE_LINE}
{SCENE_DESCRIPTION}.
{ATMOSPHERE} atmosphere, {MOOD} mood.
{LIGHTING}.
{FOCAL_DIRECTION}.
{GENRE} aesthetic. High contrast, clean composition.
Room for title text in {TEXT_ZONE}.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "{TITLE}" in {FONT_STYLE}, author name "{AUTHOR}" smaller.
```

### Example
```
Book cover for "The Narrow Path" by Dan Smith. Subtitle "A Journey Into Deeper Faith."
Misty forest path with soft morning light filtering through ancient trees.
Contemplative, serene atmosphere, hopeful mood.
Volumetric light rays through canopy, warm golden tones.
Path leading from foreground into illuminated distance.
Christian spiritual growth aesthetic. High contrast, clean composition.
Room for title text in upper third.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "The Narrow Path" in bold serif font, author name "Dan Smith" smaller.
```

### Scene Bank
- Forest path with light breaking through
- Mountain peak at dawn
- Weathered wooden door (slightly open, light behind)
- Still water reflecting sky
- Desert oasis
- Garden with morning light
- Stone pathway through ruins
- Lighthouse in storm
- River flowing through valley
- Ancient stone archway with light beyond

---

## Structure 3: Human Presence (Implied)

### Template
```
Book cover for "{TITLE}" by {AUTHOR}. {SUBTITLE_LINE}
{HUMAN_ELEMENT} {ACTION_CONTEXT}.
{MOOD} mood, {EMOTIONAL_TONE}.
{LIGHTING}.
{COMPOSITION_PLACEMENT}.
{GENRE} aesthetic. High contrast, clean composition.
No full faces visible. Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "{TITLE}" in {FONT_STYLE}, author name "{AUTHOR}" smaller.
```

### Example
```
Book cover for "Surrender" by Dan Smith. Subtitle "When Letting Go Becomes Your Greatest Strength."
Silhouetted hands releasing a white dove into golden sunset light.
Hopeful, uplifting mood, sense of freedom and release.
Dramatic backlighting creating strong silhouette with warm rim light.
Hands in lower third, dove rising toward upper center.
Christian worship aesthetic. High contrast, clean composition.
No full faces visible. Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "Surrender" in large bold sans-serif, author name "Dan Smith" smaller.
```

### Human Element Bank
- Silhouetted hands raised in worship
- Hands releasing a dove
- Single figure walking toward light (back to viewer)
- Hands holding/breaking chains
- Kneeling silhouette
- Hands cupped around small flame
- Figure standing at cliff edge facing sunrise
- Hands planting a seed
- Arms outstretched (silhouette, from behind)

---

## Structure 4: Abstract Tension

### Template
```
Book cover for "{TITLE}" by {AUTHOR}. {SUBTITLE_LINE}
{ABSTRACT_IMAGERY}.
{MOOD} mood, {ENERGY_LEVEL} energy.
{LIGHTING}, dramatic contrast.
{COMPOSITION_DIRECTION}.
{GENRE} aesthetic. High contrast, clean composition.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "{TITLE}" in {FONT_STYLE}, author name "{AUTHOR}" smaller.
```

### Example
```
Book cover for "Breakthrough" by Dan Smith. Subtitle "Breaking Every Chain That Holds You Back."
Dramatic golden light breaking through a cracked black surface,
shards of darkness falling away to reveal brilliant warm illumination.
Powerful, triumphant mood, high energy.
Intense rim lighting on crack edges, deep shadows contrasting with warm amber light.
Light source in upper center, cracks radiating outward.
Christian spiritual warfare aesthetic. High contrast, clean composition.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "Breakthrough" in massive bold sans-serif, author name "Dan Smith" smaller.
```

### Abstract Imagery Bank
- Light breaking through cracked darkness
- Fire consuming chains/barriers
- Water parting (Red Sea imagery)
- Storm clearing to reveal sky
- Shattered glass with light behind
- Rising phoenix-like flame
- Colliding waves of light and shadow
- Fractured wall with garden behind
- Lightning illuminating landscape
- Earthquake crack with light emerging

---

## Structure 5: Authority Signal (Typography-First)

### Template
```
Book cover for "{TITLE}" by {AUTHOR}. {SUBTITLE_LINE}
{BACKGROUND_TEXTURE} background in {COLOR_PALETTE}.
{SUBTLE_ACCENT_ELEMENT}.
{LIGHTING}, premium mood.
Large centered negative space dominated by typography.
{GENRE} aesthetic. Clean, authoritative, premium feel.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "{TITLE}" occupying 60-70% of cover in {FONT_STYLE}.
Subtitle and author name "{AUTHOR}" secondary.
```

### Example
```
Book cover for "The Word Study Method" by Dan Smith. Subtitle "A Practical Guide to Deeper Bible Understanding."
Rich linen texture background in deep navy blue with subtle gold leaf accents.
Thin gold foil line border element framing the text area.
Soft directional lighting catching the linen weave, premium mood.
Large centered negative space dominated by typography.
Christian Bible study aesthetic. Clean, authoritative, premium feel.
Professional book cover, exact 5.5 x 8.5 inch proportions, tall portrait rectangle, significantly taller than wide.
Title "The Word Study Method" occupying 60-70% of cover in bold modern serif.
Subtitle and author name "Dan Smith" secondary.
```

---

## Premium Material Treatment (Add to ANY structure)

### Linen/Cloth
```
...on a natural linen textile background, visible woven fabric texture,
soft directional lighting that catches the fabric weave...
```

### Gold Leaf/Foil
```
...with subtle gold leaf accents, slightly irregular metallic finish,
warm reflective highlights, aged patina on gold elements...
```

### Letterpress/Deboss
```
...with pressed indentation effect, subtle shadows suggesting depth
into the surface, embossed typography with dimensional shadows...
```

### Paper Grain
```
...on heavy cotton paper stock, visible paper fiber texture,
slightly uneven surface catching soft light...
```

### Oil Paint/Impasto
```
...heavy impasto brushstrokes with three-dimensional paint texture,
visible brush marks, thick paint catching directional light...
```

---

## Emotion-to-Visual Quick Reference

| Emotion | Colors | Lighting | Imagery Direction |
|---------|--------|----------|-------------------|
| Relief | Soft warm tones, cream, sage | Gentle diffused | Open space, calm water, clearing sky |
| Authority | Navy, gold, deep green | Structured, even | Clean lines, strong typography, texture |
| Strength | Bold contrast, red/gold/black | Dramatic, directional | Dynamic composition, swords, fire |
| Curiosity | Muted with one bright accent | Mysterious, spotlit | Symbolic objects, doors, keys |
| Peace | Cream, lavender, soft blue | Soft, warm | Minimal elements, open space, still water |
| Hope | Gold, amber, warm white | Light breaking through | Upward movement, dawn, growth |

---

## Children's Book Template

```
Children's book cover for "{TITLE}" by {AUTHOR}.
{CHARACTER_DESCRIPTION} with exaggerated emotional expression showing {EMOTION}.
Watercolor illustration style with visible brush strokes and color blooms.
Soft diffused lighting with no harsh shadows.
{CHARACTER_PLACEMENT}.
Bright, warm, child-friendly color palette with strong color separation.
Pastel background with room for large playful title in {TEXT_ZONE}.
Christian children's storybook aesthetic. Friendly, inviting, joyful.
Title "{TITLE}" in large playful rounded font, author name smaller.
```
