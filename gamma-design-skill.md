# Gamma Design System Skill

## Overview
This skill enables the creation of beautiful, serene web artifacts using the **Gamma** design system — a light-themed, cloud-inspired aesthetic that evokes calm, trust, and approachability.

**Theme:** Light, airy, optimistic
**Primary Use Cases:** Landing pages, verification screens, onboarding flows, confirmation dialogs, calm data presentation

---

## Design Philosophy

The Gamma design system embodies a "Serene Cloud Sanctuary" — a single white card floating effortlessly within a tranquil sky-blue gradient, cradled by soft, cartoon-like clouds.

### Core Principles
1. **Airy Calm** — Spacious layouts with generous whitespace create breathing room for content
2. **Visual Trust** — Deep blue branding and high contrast ensure clarity and credibility
3. **Minimal Embellishment** — Typography and layout do the work; unnecessary elements are removed
4. **Optimistic Atmosphere** — Sky-blue gradients and cloud imagery evoke openness and possibility

---

## Color Palette

### Primary Colors

| Name | Hex | Usage | CSS Token |
|------|-----|-------|-----------|
| **Gamma Blue** | `#002253` | Brand text, headings, interactive elements, links, CTAs | `--color-gamma-blue` |
| **Cloud White** | `#ffffff` | Card surfaces, primary content backgrounds | `--color-cloud-white` |
| **Coal Black** | `#000000` | Body text, secondary headings, standard content | `--color-coal-black` |
| **Sky Gradient** | `linear-gradient(to top, rgb(255, 255, 255), rgb(198, 230, 250))` | Page background | `--gradient-sky-gradient` |

### Guidance
- **Text on White:** Use Coal Black (#000000) for maximum readability (AAA contrast)
- **Interactive Elements:** Always use Gamma Blue (#002253) to signal interactivity
- **Backgrounds:** Stick to the Sky Gradient or Cloud White; avoid dark backgrounds
- **Avoid:** Harsh, saturated colors; multiple brand colors; sharp color contrasts

---

## Typography System

### Font Stack 1: PPMori (Body & Links)
- **Purpose:** Primary body text, links, UI labels
- **Weight:** 500 (medium)
- **Size:** 16px
- **Line Height:** 1.5
- **Letter Spacing:** normal
- **OpenType Features:** `kern`
- **Fallbacks:** Inter, ui-sans-serif, system-ui, sans-serif
- **CSS Token:** `--font-ppmori`

**Example Usage:**
```css
.body-text {
  font-family: var(--font-ppmori);
  font-size: 16px;
  font-weight: 500;
  line-height: 1.5;
  color: #000000;
  font-feature-settings: "kern";
}
```

### Font Stack 2: ESBuild (Headings & Brand)
- **Purpose:** Main headings, section titles, key brand elements
- **Weight:** 500 (medium)
- **Size:** 30px (or scale proportionally)
- **Line Height:** 1.2
- **Letter Spacing:** normal
- **OpenType Features:** `ss02` (stylistic set for custom glyphs)
- **Fallbacks:** Roboto, ui-sans-serif, system-ui, sans-serif
- **CSS Token:** `--font-esbuild`

**Example Usage:**
```css
.heading-primary {
  font-family: var(--font-esbuild);
  font-size: 30px;
  font-weight: 500;
  line-height: 1.2;
  color: #000000;
  font-feature-settings: "ss02";
}
```

### Typography Hierarchy

| Level | Font | Size | Weight | Line Height | Color | Use Case |
|-------|------|------|--------|------------|-------|----------|
| H1 (Primary) | ESBuild | 30px | 500 | 1.2 | #000000 | Main page heading, hero text |
| H2 (Secondary) | ESBuild | 24px | 500 | 1.2 | #000000 | Section headers |
| Body | PPMori | 16px | 500 | 1.5 | #000000 | Standard text content |
| Link | PPMori | 16px | 500 | 1.5 | #002253 | Interactive text |
| Caption | PPMori | 14px | 500 | 1.5 | #000000 | Supporting text, metadata |

---

## Spacing & Layout

### Base Unit
**8px** — All spacing is measured in multiples of 8px for consistency and rhythm.

### Spacing Scale

| Name | Value | CSS Token | Use |
|------|-------|-----------|-----|
| XS | 8px | `--spacing-8` | Element gaps, small margins |
| SM | 20px | `--spacing-20` | Component gaps, vertical spacing |
| MD | 32px | `--spacing-32` | Section gaps, card padding |

### Default Spacing Rules

- **Card Padding:** 32px (all sides)
- **Section Gap:** 32px (vertical gap between major sections)
- **Element Gap:** 8px (gap between inline elements, buttons, form fields)
- **Text Spacing:** 20px (vertical gap between heading and body text)

### Density
**Spacious** — The design favors generous whitespace over compactness, creating a breathing, calm aesthetic.

---

## Border Radius

All rounded elements use a consistent **12px border-radius**.

| Element | Radius |
|---------|--------|
| Cards | 12px |
| Form fields | 12px |
| Buttons | 12px |
| Modals | 12px |

**CSS Token:** `--radius-xl` or `--radius-cards`

---

## Components

### 1. Centered Content Card

**Role:** Container for focal content or primary interaction.

**Specifications:**
- Background: Cloud White (#ffffff)
- Border Radius: 12px
- Padding: 32px (all sides)
- Max Width: 400px–600px (depending on content)
- Box Shadow: Soft shadow (e.g., `0 4px 16px rgba(0, 0, 0, 0.08)`)
- Vertical Alignment: Centered on page with Sky Gradient background

**Internal Spacing:**
- Text elements: 20px vertical gap (heading to body)
- Body sections: 32px gap between groups
- Inline elements: 8px horizontal gap

**Example HTML:**
```html
<div class="centered-card">
  <h1 class="heading-primary">Just a moment...</h1>
  <p class="body-text">Verifying your request.</p>
</div>
```

**Example CSS:**
```css
.centered-card {
  background: var(--color-cloud-white);
  border-radius: var(--radius-cards);
  padding: var(--spacing-32);
  max-width: 500px;
  margin: 0 auto;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-20);
}
```

### 2. Main Heading

**Role:** Introduces sections or key messages.

**Specifications:**
- Font: ESBuild
- Size: 30px
- Weight: 500
- Line Height: 1.2
- Color: Coal Black (#000000)
- Text Alignment: Center (typically)
- Margin: 0 (use gaps from parent container)

**Example HTML:**
```html
<h1 class="heading-primary">Welcome to Serenity</h1>
```

**Example CSS:**
```css
.heading-primary {
  font-family: var(--font-esbuild);
  font-size: 30px;
  font-weight: 500;
  line-height: 1.2;
  color: var(--color-coal-black);
  text-align: center;
  margin: 0;
}
```

### 3. Body Text

**Role:** Standard informational text content.

**Specifications:**
- Font: PPMori
- Size: 16px
- Weight: 500
- Line Height: 1.5
- Color: Coal Black (#000000)
- Text Alignment: Left or center
- Margin: 0 (use gaps from parent container)

**Example HTML:**
```html
<p class="body-text">Everything is being verified securely in the background.</p>
```

**Example CSS:**
```css
.body-text {
  font-family: var(--font-ppmori);
  font-size: 16px;
  font-weight: 500;
  line-height: 1.5;
  color: var(--color-coal-black);
  margin: 0;
  font-feature-settings: "kern";
}
```

### 4. Link Text

**Role:** Interactive text elements that invite action.

**Specifications:**
- Font: PPMori
- Size: 16px
- Weight: 500
- Line Height: 1.5
- Color: Gamma Blue (#002253)
- Text Decoration: None (default); underline on hover
- Cursor: pointer

**Example HTML:**
```html
<a href="#" class="link-text">Learn more about this process</a>
```

**Example CSS:**
```css
.link-text {
  font-family: var(--font-ppmori);
  font-size: 16px;
  font-weight: 500;
  line-height: 1.5;
  color: var(--color-gamma-blue);
  text-decoration: none;
  cursor: pointer;
  font-feature-settings: "kern";
  transition: text-decoration 0.2s ease;
}

.link-text:hover {
  text-decoration: underline;
}
```

### 5. Loading Indicator Region

**Role:** Communicates background processing status.

**Specifications:**
- Layout: Horizontal flexbox arrangement
- Components: Animated spinner + "Verifying..." text + optional logo
- Font: PPMori, 16px, #000000
- Gap: 8px between elements
- Alignment: Center

**Example HTML:**
```html
<div class="loading-region">
  <span class="spinner"></span>
  <span class="body-text">Verifying...</span>
</div>
```

**Example CSS:**
```css
.loading-region {
  display: flex;
  align-items: center;
  gap: var(--spacing-8);
  justify-content: center;
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid #e0e0e0;
  border-top-color: var(--color-gamma-blue);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### 6. Primary Button

**Role:** Call-to-action for primary interactions.

**Specifications:**
- Background: Gamma Blue (#002253)
- Text: Cloud White (#ffffff)
- Font: PPMori, 16px, weight 500
- Padding: 12px 24px (vertical × horizontal)
- Border Radius: 12px
- Border: None
- Box Shadow: Soft (on hover: slightly elevated)
- Cursor: pointer
- Transition: smooth (0.2s)

**Example HTML:**
```html
<button class="button-primary">Continue</button>
```

**Example CSS:**
```css
.button-primary {
  background-color: var(--color-gamma-blue);
  color: var(--color-cloud-white);
  font-family: var(--font-ppmori);
  font-size: 16px;
  font-weight: 500;
  padding: 12px 24px;
  border-radius: var(--radius-buttons);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 34, 83, 0.1);
}

.button-primary:hover {
  box-shadow: 0 4px 16px rgba(0, 34, 83, 0.2);
  transform: translateY(-2px);
}

.button-primary:active {
  transform: translateY(0);
}
```

---

## Background & Imagery

### Page Background
Always use the Sky Gradient:
```css
background: linear-gradient(to top, rgb(255, 255, 255), rgb(198, 230, 250));
```

This creates a soft, expansive, optimistic atmosphere that suggests an open sky.

### Decorative Elements
- **Soft 3D Cloud Shapes:** Pastel pink and blue clouds positioned around the page (typically bottom and sides)
- **Purpose:** Atmospheric framing, reinforces the "Serene Cloud Sanctuary" theme
- **Technique:** SVG, CSS, or subtle PNG with low opacity
- **Important:** Decorative only; do not obstruct content

### Content Areas
- Keep content centered in a white card (Cloud White background)
- Let the gradient and clouds frame the content without competing for attention
- Minimal use of additional graphics; text and layout are primary

---

## Do's ✓

✓ Use the Sky Gradient (`linear-gradient(to top, rgb(255, 255, 255), rgb(198, 230, 250))`) for all page backgrounds  
✓ Apply 12px border-radius consistently to cards, buttons, and form fields  
✓ Use PPMori font at 16px with weight 500 for all body text  
✓ Use ESBuild font at 30px with weight 500 for main headings  
✓ Apply 32px padding inside primary content containers  
✓ Use Gamma Blue (#002253) exclusively for interactive elements (links, buttons, CTAs)  
✓ Maintain high contrast ratios (#000000 on #ffffff = AAA; #002253 on #ffffff = AAA)  
✓ Prioritize generous whitespace and spacious layouts  
✓ Use soft, subtle shadows (0 4px 16px rgba(0, 0, 0, 0.08)) for depth  
✓ Center content vertically and horizontally within the viewport  
✓ Test all text for readability against the gradient background  

---

## Don'ts ✗

✗ Avoid harsh, saturated, or non-brand colors  
✗ Do not use sharp corners or border-radius other than 12px on grouped/interactive elements  
✗ Do not use thin font weights (<500) for primary text  
✗ Do not deviate from specified font families (PPMori, ESBuild) or their weights/sizes  
✗ Do not use dark backgrounds for main content areas; stick to Cloud White (#ffffff)  
✗ Do not add excessive shadows or complex visual effects  
✗ Do not introduce additional brand or accent colors beyond Gamma Blue  
✗ Do not clutter layouts; maintain 32px section gaps  
✗ Do not place content at the very edges; use centered cards with padding  
✗ Do not override the Sky Gradient background for aesthetic reasons  

---

## CSS Custom Properties (Copy-Paste Ready)

```css
:root {
  /* ===== COLORS ===== */
  --color-gamma-blue: #002253;
  --color-sky-gradient: #c6e6fa;
  --gradient-sky-gradient: linear-gradient(to top, rgb(255, 255, 255), rgb(198, 230, 250));
  --color-cloud-white: #ffffff;
  --color-coal-black: #000000;

  /* ===== TYPOGRAPHY: FONT FAMILIES ===== */
  --font-ppmori: 'PPMori', 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  --font-esbuild: 'ESBuild', 'Roboto', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /* ===== TYPOGRAPHY: SCALE ===== */
  --text-base: 16px;
  --text-3xl: 30px;
  --text-2xl: 24px;
  --leading-base: 1.5;
  --leading-headings: 1.2;

  /* ===== TYPOGRAPHY: WEIGHTS ===== */
  --font-weight-medium: 500;

  /* ===== SPACING ===== */
  --spacing-unit: 8px;
  --spacing-8: 8px;
  --spacing-20: 20px;
  --spacing-32: 32px;

  /* ===== LAYOUT ===== */
  --section-gap: 32px;
  --card-padding: 32px;
  --element-gap: 8px;

  /* ===== BORDER RADIUS ===== */
  --radius-base: 12px;
  --radius-xl: 12px;
  --radius-cards: 12px;
  --radius-buttons: 12px;
  --radius-fields: 12px;

  /* ===== SHADOWS ===== */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 4px 16px rgba(0, 34, 83, 0.2);

  /* ===== TRANSITIONS ===== */
  --transition-standard: all 0.2s ease;
  --transition-fast: all 0.15s ease;
}
```

---

## Tailwind Configuration (Tailwind v4)

```css
@theme {
  /* Colors */
  --color-gamma-blue: #002253;
  --color-sky-gradient: #c6e6fa;
  --color-cloud-white: #ffffff;
  --color-coal-black: #000000;

  /* Typography */
  --font-ppmori: 'PPMori', 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  --font-esbuild: 'ESBuild', 'Roboto', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /* Typography Scale */
  --text-base: 16px;
  --text-3xl: 30px;
  --text-2xl: 24px;
  --leading-base: 1.5;
  --leading-headings: 1.2;

  /* Spacing */
  --spacing-8: 8px;
  --spacing-20: 20px;
  --spacing-32: 32px;

  /* Border Radius */
  --radius-xl: 12px;
}
```

---

## Quick Start Examples

### Example 1: Centered Verification Card

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Verifying</title>
  <style>
    :root {
      --color-gamma-blue: #002253;
      --gradient-sky-gradient: linear-gradient(to top, rgb(255, 255, 255), rgb(198, 230, 250));
      --color-cloud-white: #ffffff;
      --color-coal-black: #000000;
      --font-ppmori: 'PPMori', 'Inter', ui-sans-serif, system-ui, sans-serif;
      --font-esbuild: 'ESBuild', 'Roboto', ui-sans-serif, system-ui, sans-serif;
      --spacing-8: 8px;
      --spacing-20: 20px;
      --spacing-32: 32px;
      --radius-cards: 12px;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: var(--gradient-sky-gradient);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-ppmori);
    }

    .centered-card {
      background: var(--color-cloud-white);
      border-radius: var(--radius-cards);
      padding: var(--spacing-32);
      max-width: 500px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
      text-align: center;
    }

    .heading-primary {
      font-family: var(--font-esbuild);
      font-size: 30px;
      font-weight: 500;
      line-height: 1.2;
      color: var(--color-coal-black);
      margin-bottom: var(--spacing-20);
    }

    .body-text {
      font-size: 16px;
      font-weight: 500;
      line-height: 1.5;
      color: var(--color-coal-black);
      margin-bottom: var(--spacing-20);
    }

    .loading-region {
      display: flex;
      align-items: center;
      gap: var(--spacing-8);
      justify-content: center;
    }

    .spinner {
      width: 20px;
      height: 20px;
      border: 2px solid #e0e0e0;
      border-top-color: var(--color-gamma-blue);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }
  </style>
</head>
<body>
  <div class="centered-card">
    <h1 class="heading-primary">Just a moment...</h1>
    <p class="body-text">We're verifying your request securely.</p>
    <div class="loading-region">
      <span class="spinner"></span>
      <span class="body-text">Verifying...</span>
    </div>
  </div>
</body>
</html>
```

### Example 2: Gamma-Styled React Component

```jsx
export default function GammaCard() {
  return (
    <div className="min-h-screen bg-gradient-to-t from-white to-sky-blue flex items-center justify-center">
      <div className="bg-white rounded-3xl p-8 max-w-md shadow-lg text-center">
        <h1 className="font-esbuild text-3xl font-medium text-black mb-5">
          Welcome
        </h1>
        <p className="font-ppmori text-base font-medium text-black mb-6">
          Discover serene, calm design that builds trust.
        </p>
        <button className="bg-gamma-blue text-white font-ppmori font-medium px-6 py-3 rounded-3xl hover:shadow-lg transition">
          Get Started
        </button>
      </div>
    </div>
  );
}
```

---

## Similar Design Systems for Inspiration

- **Figma** — Soft, welcoming gradients with clean, minimal content blocks
- **Notion** — Clear typography and structured information in light-themed, bordered containers
- **Linear** — High-contrast dark text on light backgrounds with functional, understated UI
- **Calm** — Soft gradients and spaciousness creating serene, focused experience

---

## Accessibility Checklist

- [ ] All text meets WCAG AAA contrast ratios (#000000 on #ffffff, #002253 on #ffffff)
- [ ] Font sizes are at least 16px for body text
- [ ] Line heights are 1.5+ for readability
- [ ] Focus states are visible on interactive elements
- [ ] Animations respect `prefers-reduced-motion` preference
- [ ] Color is not the only means of conveying information (e.g., links are underlined on hover)
- [ ] Images have descriptive alt text
- [ ] Form fields have associated labels

---

## When to Use This Skill

✓ Creating calm, serene user experiences  
✓ Onboarding flows and verification screens  
✓ Landing pages with a trustworthy aesthetic  
✓ Confirmation dialogs and success states  
✓ Information-dense pages needing visual clarity  
✓ Brand pages emphasizing trust, security, or peace  
✓ Any interface where a light, spacious, airy feel is desired  

---

## When NOT to Use This Skill

✗ Dark-mode interfaces or high-energy branding  
✗ Complex, information-heavy dashboards requiring density  
✗ Systems needing multiple accent colors  
✗ Applications targeting bold, modern, or edgy aesthetics  
✗ Interfaces requiring very small text or compact layouts  

---

## Version History

**v1.0** — Initial Gamma design system skill file  
Created: 2026  
Based on: "Gamma — Style Reference: Serene Cloud Sanctuary"
