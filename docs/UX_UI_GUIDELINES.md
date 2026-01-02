# UX/UI Design System

**Version 2.0** | File Uploader & Clipboard Manager

---

## Table of Contents

1. [Design Tokens](#1-design-tokens)
2. [Color System](#2-color-system)
3. [Typography](#3-typography)
4. [Spacing & Layout](#4-spacing--layout)
5. [Borders & Radius](#5-borders--radius)
6. [Shadows & Elevation](#6-shadows--elevation)
7. [Motion & Animation](#7-motion--animation)
8. [Interactive States](#8-interactive-states)
9. [UI Components](#9-ui-components)
10. [Navigation & Sitemap](#10-navigation--sitemap)
11. [Forms & Validation](#11-forms--validation)
12. [Feedback & Notifications](#12-feedback--notifications)
13. [Icons](#13-icons)
14. [Images & Media](#14-images--media)
15. [Responsive Design](#15-responsive-design)
16. [Accessibility](#16-accessibility)
17. [Error Handling & Edge Cases](#17-error-handling--edge-cases)
18. [Design Principles](#18-design-principles)
19. [Implementation Checklist](#19-implementation-checklist)

---

## 1. Design Tokens

Design tokens are the single source of truth for all design decisions. Use CSS custom properties for maintainability and theme switching.

### Token Architecture

```css
:root {
  /* ========== COLOR TOKENS ========== */
  
  /* Primary */
  --color-primary: #007bff;
  --color-primary-hover: #0056b3;
  --color-primary-active: #004494;
  --color-primary-light: #f0f7ff;
  
  /* Semantic */
  --color-success: #28a745;
  --color-success-hover: #218838;
  --color-danger: #dc3545;
  --color-danger-hover: #c82333;
  --color-warning: #ffc107;
  --color-warning-hover: #e0a800;
  --color-info: #17a2b8;
  --color-info-hover: #138496;
  
  /* Neutral */
  --color-text-primary: #212529;
  --color-text-secondary: #6c757d;
  --color-text-muted: #868e96;
  --color-text-inverse: #ffffff;
  
  /* Backgrounds */
  --color-bg-primary: #ffffff;
  --color-bg-secondary: #f8f9fa;
  --color-bg-tertiary: #e9ecef;
  --color-bg-elevated: #ffffff;
  
  /* Borders */
  --color-border-default: #dee2e6;
  --color-border-light: #e9ecef;
  --color-border-focus: #007bff;
  
  /* ========== TYPOGRAPHY TOKENS ========== */
  
  --font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-family-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  --line-height-tight: 1.25;
  --line-height-base: 1.5;
  --line-height-relaxed: 1.75;
  
  /* ========== SPACING TOKENS ========== */
  
  --space-0: 0;
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  
  /* ========== BORDER TOKENS ========== */
  
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-full: 9999px;
  
  --border-width-default: 1px;
  --border-width-thick: 2px;
  
  /* ========== SHADOW TOKENS ========== */
  
  --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1), 0 2px 4px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1), 0 10px 10px rgba(0, 0, 0, 0.04);
  
  /* ========== ANIMATION TOKENS ========== */
  
  --duration-instant: 0ms;
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 400ms;
  --duration-slower: 600ms;
  
  --easing-default: cubic-bezier(0.4, 0, 0.2, 1);
  --easing-in: cubic-bezier(0.4, 0, 1, 1);
  --easing-out: cubic-bezier(0, 0, 0.2, 1);
  --easing-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --easing-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
  
  /* ========== Z-INDEX TOKENS ========== */
  
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-modal-backdrop: 300;
  --z-modal: 400;
  --z-popover: 500;
  --z-tooltip: 600;
  --z-toast: 700;
}
```

### Dark Mode Tokens

```css
[data-theme="dark"] {
  /* Colors */
  --color-primary: #4da3ff;
  --color-primary-hover: #7ab8ff;
  --color-primary-light: #1a2d42;
  
  /* Text */
  --color-text-primary: #f8f9fa;
  --color-text-secondary: #adb5bd;
  --color-text-muted: #6c757d;
  
  /* Backgrounds */
  --color-bg-primary: #121212;
  --color-bg-secondary: #1e1e1e;
  --color-bg-tertiary: #2d2d2d;
  --color-bg-elevated: #242424;
  
  /* Borders */
  --color-border-default: #3d3d3d;
  --color-border-light: #2d2d2d;
  
  /* Shadows (reduced intensity for dark mode) */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.5);
}
```

### Theme Toggle Implementation

```javascript
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
}

// Initialize on load
const saved = localStorage.getItem('theme');
const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
document.documentElement.setAttribute('data-theme', saved || preferred);
```

---

## 2. Color System

### Primary Palette

| Token | Light Mode | Dark Mode | Usage |
|-------|------------|-----------|-------|
| `--color-primary` | `#007bff` | `#4da3ff` | Primary actions, links, focus states |
| `--color-primary-hover` | `#0056b3` | `#7ab8ff` | Hover states for primary elements |
| `--color-primary-light` | `#f0f7ff` | `#1a2d42` | Subtle backgrounds, highlights |

### Semantic Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-success` | `#28a745` | Confirmations, positive actions, upload complete |
| `--color-danger` | `#dc3545` | Errors, destructive actions, delete buttons |
| `--color-warning` | `#ffc107` | Warnings, pending states, attention needed |
| `--color-info` | `#17a2b8` | Informational messages, tips |

### Accent Gradient

```css
.gradient-accent {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

Reserved for premium sections, clipboard header, feature highlights.

### Color Contrast Requirements

All color combinations must meet WCAG 2.1 AA standards:

| Foreground | Background | Contrast Ratio | Status |
|------------|------------|----------------|--------|
| `#212529` | `#ffffff` | 16.1:1 | ✓ AAA |
| `#ffffff` | `#007bff` | 4.5:1 | ✓ AA |
| `#ffffff` | `#28a745` | 4.5:1 | ✓ AA |
| `#ffffff` | `#dc3545` | 4.6:1 | ✓ AA |
| `#212529` | `#ffc107` | 12.6:1 | ✓ AAA |

---

## 3. Typography

### Type Scale

| Name | Size | Line Height | Weight | Usage |
|------|------|-------------|--------|-------|
| Display | `2.25rem` (36px) | 1.2 | 700 | Hero sections, landing pages |
| H1 | `1.875rem` (30px) | 1.25 | 700 | Page titles |
| H2 | `1.5rem` (24px) | 1.3 | 600 | Section headers |
| H3 | `1.25rem` (20px) | 1.4 | 600 | Subsections, card titles |
| H4 | `1.125rem` (18px) | 1.4 | 600 | Minor headers |
| Body | `1rem` (16px) | 1.5 | 400 | Default text |
| Body Small | `0.875rem` (14px) | 1.5 | 400 | Secondary text, metadata |
| Caption | `0.75rem` (12px) | 1.4 | 400 | Timestamps, file sizes, hints |
| Code | `0.875rem` (14px) | 1.6 | 400 | Preformatted, technical |

### Heading Styles

```css
h1, h2 {
  color: var(--color-primary);
  font-weight: var(--font-weight-bold);
}

h3, h4, h5, h6 {
  color: var(--color-text-primary);
  font-weight: var(--font-weight-semibold);
}
```

### Text Truncation

```css
/* Single line truncation */
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Filename in tables */
.filename-cell {
  max-width: 300px;
}

/* Filename in cards */
.filename-truncate {
  max-width: 200px;
  display: inline-block;
}

/* Multi-line truncation (2 lines) */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

---

## 4. Spacing & Layout

### Spacing Scale

Use the 4px base unit consistently:

| Token | Value | Common Usage |
|-------|-------|--------------|
| `--space-1` | 4px | Icon gaps, tight padding |
| `--space-2` | 8px | Button icon gaps, list item spacing |
| `--space-3` | 12px | Form field gaps |
| `--space-4` | 16px | Card padding, section gaps |
| `--space-5` | 20px | Container padding |
| `--space-6` | 24px | Card body padding |
| `--space-8` | 32px | Section margins |
| `--space-10` | 40px | Major section gaps |
| `--space-12` | 48px | Page section separation |

### Container Widths

| Container | Max Width | Usage |
|-----------|-----------|-------|
| Main | `1140px` | Primary content area |
| Narrow | `720px` | Forms, focused content |
| Wide | `1320px` | Dashboards, data tables |
| Clipboard View | `900px` | Clipboard detail pages |

### Component Spacing Reference

| Component | Padding | Margin |
|-----------|---------|--------|
| Page container | `20px` | — |
| Card body | `24px` (`30px` desktop) | `16px` top |
| Card header | `20px 24px` | — |
| Toast | `12px 16px` | `8px` bottom (stacking) |
| Drag-drop area | `32px 16px` | — |
| Table cell | `12px 16px` | — |
| Button | `8px 16px` | — |
| Button (small) | `4px 8px` | — |

---

## 5. Borders & Radius

### Border Radius Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | `4px` | Small elements, chips, tags |
| `--radius-md` | `6px` | Buttons, inputs, small cards |
| `--radius-lg` | `8px` | Cards, modals, containers |
| `--radius-xl` | `12px` | Large cards, feature sections |
| `--radius-full` | `9999px` | Pills, avatars, circular buttons |

### Border Styles

```css
/* Default border */
.border-default {
  border: 1px solid var(--color-border-default);
}

/* Interactive/focus border */
.border-focus {
  border: 2px solid var(--color-border-focus);
}

/* Dashed upload area */
.border-dashed {
  border: 2px dashed var(--color-primary);
}

/* Divider */
.divider {
  border-top: 1px solid var(--color-border-light);
}
```

---

## 6. Shadows & Elevation

### Elevation Levels

| Level | Token | Usage |
|-------|-------|-------|
| 0 | None | Flat elements, disabled states |
| 1 | `--shadow-xs` | Subtle lift, input focus |
| 2 | `--shadow-sm` | Cards at rest, buttons |
| 3 | `--shadow-md` | Card hover, dropdowns |
| 4 | `--shadow-lg` | Modals, popovers |
| 5 | `--shadow-xl` | Toasts, critical overlays |

### Elevation Transitions

```css
.card {
  box-shadow: var(--shadow-sm);
  transition: box-shadow var(--duration-normal) var(--easing-default);
}

.card:hover {
  box-shadow: var(--shadow-md);
}
```

---

## 7. Motion & Animation

### Motion Principles

1. **Purposeful**: Animation should communicate state changes, not decorate
2. **Quick**: Most interactions should feel instant (150-250ms)
3. **Natural**: Use easing curves that mimic physical movement
4. **Consistent**: Same action = same animation everywhere
5. **Reducible**: Respect `prefers-reduced-motion`

### Duration Guidelines

| Duration | Usage |
|----------|-------|
| `0ms` | Instant feedback (color changes on active state) |
| `150ms` | Micro-interactions (button press, checkbox toggle) |
| `250ms` | Standard transitions (hover, focus, collapse) |
| `400ms` | Emphasis animations (success states, toasts entering) |
| `600ms` | Complex animations (page transitions, large modals) |

### Easing Functions

| Easing | Curve | Usage |
|--------|-------|-------|
| Default | `cubic-bezier(0.4, 0, 0.2, 1)` | Most transitions |
| Ease-out | `cubic-bezier(0, 0, 0.2, 1)` | Elements entering |
| Ease-in | `cubic-bezier(0.4, 0, 1, 1)` | Elements exiting |
| Bounce | `cubic-bezier(0.68, -0.55, 0.265, 1.55)` | Playful confirmations |

### Standard Animations

```css
/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Slide up (for toasts) */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Scale in (for modals) */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Pulse (for loading states) */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. Interactive States

### State Hierarchy

Every interactive element must have these states:

| State | Description |
|-------|-------------|
| Default | Resting state |
| Hover | Mouse over (desktop) |
| Focus | Keyboard navigation |
| Active | Being clicked/pressed |
| Disabled | Not interactive |
| Loading | Action in progress |

### Button States

```css
.btn-primary {
  background-color: var(--color-primary);
  color: var(--color-text-inverse);
  transition: all var(--duration-fast) var(--easing-default);
}

.btn-primary:hover {
  background-color: var(--color-primary-hover);
}

.btn-primary:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}

.btn-primary:active {
  background-color: var(--color-primary-active);
  transform: translateY(1px);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  pointer-events: none;
}

.btn-primary.is-loading {
  color: transparent;
  pointer-events: none;
  position: relative;
}

.btn-primary.is-loading::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}
```

### Drag & Drop States

```css
.drag-drop-area {
  background-color: var(--color-bg-primary);
  border: 2px dashed var(--color-primary);
  border-radius: var(--radius-lg);
  transition: all var(--duration-normal) var(--easing-default);
}

.drag-drop-area:hover {
  background-color: var(--color-primary-light);
  border-color: var(--color-primary-hover);
}

.drag-drop-area.drag-over {
  background-color: var(--color-bg-tertiary);
  border-color: var(--color-primary-hover);
  transform: scale(1.02);
}

.drag-drop-area.is-uploading {
  pointer-events: none;
  opacity: 0.7;
}
```

### Focus Visible

```css
/* Only show focus ring for keyboard navigation */
:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

---

## 9. UI Components

### Buttons

#### Button Variants

| Variant | Class | Usage |
|---------|-------|-------|
| Primary | `.btn-primary` | Main CTA, form submit |
| Secondary | `.btn-secondary` | Alternative actions |
| Success | `.btn-success` | Positive actions, share |
| Danger | `.btn-danger` | Destructive actions |
| Info | `.btn-info` | Download, view |
| Outline | `.btn-outline-*` | Lower emphasis |
| Ghost | `.btn-ghost` | Minimal UI actions |

#### Button Sizes

| Size | Class | Padding | Font Size |
|------|-------|---------|-----------|
| Small | `.btn-sm` | `4px 8px` | `0.875rem` |
| Default | `.btn` | `8px 16px` | `1rem` |
| Large | `.btn-lg` | `12px 24px` | `1.125rem` |

#### Icon Buttons

```css
.btn-icon {
  padding: var(--space-2);
  line-height: 1;
}

.btn i,
.btn svg {
  pointer-events: none; /* Prevent click issues */
}

/* Icon + text spacing */
.btn i + span,
.btn svg + span {
  margin-left: var(--space-2);
}
```

### Cards

```
.card
├── .card-header (optional)
│   └── Title, actions
├── .card-img-top (optional)
│   └── Image/thumbnail
├── .card-body
│   ├── .card-title
│   ├── .card-text / metadata
│   └── .card-actions
└── .card-footer (optional)
    └── Secondary info, timestamps
```

```css
.card {
  background: var(--color-bg-elevated);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  transition: box-shadow var(--duration-normal) var(--easing-default);
}

.card:hover {
  box-shadow: var(--shadow-md);
}

.card-body {
  padding: var(--space-6);
}

.card-img-top {
  width: 100%;
  max-height: 300px;
  object-fit: contain;
  background: var(--color-bg-secondary);
}
```

### Tables

```css
.table-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.table {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
}

.table th,
.table td {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  border-bottom: 1px solid var(--color-border-light);
}

.table th {
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-secondary);
  font-size: var(--font-size-sm);
}

.table tbody tr:hover {
  background: var(--color-bg-secondary);
}
```

#### Column Widths

| Column | Width | Responsive |
|--------|-------|------------|
| Type icon | `50px` | Fixed |
| Filename | `auto` (flex) | Truncate |
| Size | `100px` | Hide on mobile |
| Date | `160px` | Hide on mobile |
| Actions | `130px` | Wrap |

### Progress Bar

```css
.progress {
  height: 8px;
  background: var(--color-bg-tertiary);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: var(--color-primary);
  transition: width var(--duration-normal) var(--easing-out);
}

.progress-bar.is-animated {
  background-image: linear-gradient(
    45deg,
    rgba(255, 255, 255, 0.15) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.15) 50%,
    rgba(255, 255, 255, 0.15) 75%,
    transparent 75%
  );
  background-size: 1rem 1rem;
  animation: progress-stripes 1s linear infinite;
}

@keyframes progress-stripes {
  from { background-position: 1rem 0; }
  to { background-position: 0 0; }
}

/* Large progress (for uploads) */
.progress-lg {
  height: 24px;
}

.progress-lg .progress-bar {
  line-height: 24px;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-inverse);
}
```

### Modals

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: var(--z-modal-backdrop);
  animation: fadeIn var(--duration-normal) var(--easing-out);
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  background: var(--color-bg-elevated);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  z-index: var(--z-modal);
  animation: scaleIn var(--duration-normal) var(--easing-out);
  overflow: hidden;
}

.modal-header {
  padding: var(--space-5) var(--space-6);
  border-bottom: 1px solid var(--color-border-light);
}

.modal-body {
  padding: var(--space-6);
  overflow-y: auto;
}

.modal-footer {
  padding: var(--space-4) var(--space-6);
  border-top: 1px solid var(--color-border-light);
  display: flex;
  justify-content: flex-end;
  gap: var(--space-2);
}
```

---

## 10. Navigation & Sitemap

### Information Architecture

#### Application Structure

```
File Uploader & Clipboard Manager
│
├── Home / Dashboard
│   ├── Quick Upload Area
│   ├── Recent Files List
│   └── Quick Actions
│
├── Files
│   ├── All Files (default view)
│   ├── File Detail View
│   │   ├── Preview
│   │   ├── Metadata
│   │   └── Actions (download, share, delete)
│   └── Search Results
│
├── Clipboard
│   ├── Clipboard List
│   ├── Clipboard Item Detail
│   │   ├── Content Preview
│   │   ├── Metadata
│   │   └── Actions (copy, share, delete)
│   └── Quick Paste
│
└── Settings (optional)
    ├── Preferences
    └── Account
```

#### URL Structure

| Page | URL Pattern | Example |
|------|-------------|---------|
| Home | `/` | `/` |
| All Files | `/files` | `/files` |
| File Detail | `/files/:id` | `/files/abc123` |
| File Download | `/files/:id/download` | `/files/abc123/download` |
| Clipboard List | `/clipboard` | `/clipboard` |
| Clipboard Item | `/clipboard/:id` | `/clipboard/xyz789` |
| Search Results | `/search?q=:query` | `/search?q=report` |
| 404 Page | `/404` | — |

### Navigation Components

#### Primary Navigation (Header)

```css
.navbar {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background: var(--color-bg-elevated);
  border-bottom: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-xs);
}

.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  padding: 0 var(--space-5);
  max-width: var(--container-max-width, 1140px);
  margin: 0 auto;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  color: var(--color-primary);
  text-decoration: none;
}

.navbar-brand:hover {
  color: var(--color-primary-hover);
}

.navbar-brand-icon {
  width: 32px;
  height: 32px;
}
```

#### Navigation Menu

```css
.nav {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-item {
  position: relative;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  border-radius: var(--radius-md);
  transition: all var(--duration-fast) var(--easing-default);
}

.nav-link:hover {
  color: var(--color-text-primary);
  background: var(--color-bg-secondary);
}

.nav-link:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.nav-link.is-active {
  color: var(--color-primary);
  background: var(--color-primary-light);
}

.nav-link .nav-icon {
  font-size: var(--font-size-lg);
}
```

#### Navigation States

| State | Style |
|-------|-------|
| Default | `color-text-secondary`, transparent background |
| Hover | `color-text-primary`, `bg-secondary` |
| Active/Current | `color-primary`, `bg-primary-light` |
| Focus | 2px primary outline |
| Disabled | 50% opacity, no pointer events |

#### Breadcrumbs

```css
.breadcrumb {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--space-1);
  padding: var(--space-3) 0;
  font-size: var(--font-size-sm);
  list-style: none;
  margin: 0;
}

.breadcrumb-item {
  display: flex;
  align-items: center;
}

.breadcrumb-item + .breadcrumb-item::before {
  content: '/';
  margin-right: var(--space-1);
  color: var(--color-text-muted);
}

.breadcrumb-link {
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast);
}

.breadcrumb-link:hover {
  color: var(--color-primary);
  text-decoration: underline;
}

.breadcrumb-item.is-current {
  color: var(--color-text-primary);
  font-weight: var(--font-weight-medium);
}
```

**Breadcrumb Examples:**

| Page | Breadcrumb |
|------|------------|
| Home | — (none) |
| All Files | Home / Files |
| File Detail | Home / Files / document.pdf |
| Clipboard Item | Home / Clipboard / Text snippet |

#### Tabs

```css
.tabs {
  display: flex;
  gap: var(--space-1);
  border-bottom: 1px solid var(--color-border-light);
  margin-bottom: var(--space-5);
}

.tab {
  position: relative;
  padding: var(--space-3) var(--space-4);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  background: transparent;
  border: none;
  cursor: pointer;
  transition: color var(--duration-fast);
}

.tab:hover {
  color: var(--color-text-primary);
}

.tab.is-active {
  color: var(--color-primary);
}

.tab.is-active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-primary);
  border-radius: var(--radius-full) var(--radius-full) 0 0;
}

.tab:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: -2px;
}
```

#### Pagination

```css
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-1);
  margin: var(--space-6) 0;
}

.pagination-item {
  min-width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  background: transparent;
  border: 1px solid var(--color-border-default);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--duration-fast);
}

.pagination-item:hover:not(:disabled) {
  color: var(--color-primary);
  border-color: var(--color-primary);
  background: var(--color-primary-light);
}

.pagination-item.is-active {
  color: var(--color-text-inverse);
  background: var(--color-primary);
  border-color: var(--color-primary);
}

.pagination-item:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-ellipsis {
  padding: 0 var(--space-2);
  color: var(--color-text-muted);
}
```

#### Back Navigation

```css
.back-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) 0;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast);
}

.back-link:hover {
  color: var(--color-primary);
}

.back-link-icon {
  transition: transform var(--duration-fast);
}

.back-link:hover .back-link-icon {
  transform: translateX(-2px);
}
```

### Mobile Navigation

#### Mobile Header

```css
@media (max-width: 767px) {
  .navbar-container {
    height: 56px;
    padding: 0 var(--space-4);
  }
  
  .nav-desktop {
    display: none;
  }
  
  .nav-mobile-toggle {
    display: flex;
  }
}

@media (min-width: 768px) {
  .nav-mobile-toggle {
    display: none;
  }
}
```

#### Mobile Menu (Off-Canvas)

```css
.mobile-nav {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 280px;
  max-width: 85vw;
  background: var(--color-bg-elevated);
  box-shadow: var(--shadow-xl);
  z-index: var(--z-modal);
  transform: translateX(-100%);
  transition: transform var(--duration-normal) var(--easing-out);
}

.mobile-nav.is-open {
  transform: translateX(0);
}

.mobile-nav-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: calc(var(--z-modal) - 1);
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--duration-normal), visibility var(--duration-normal);
}

.mobile-nav-backdrop.is-visible {
  opacity: 1;
  visibility: visible;
}

.mobile-nav-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-border-light);
}

.mobile-nav-body {
  padding: var(--space-4);
  overflow-y: auto;
  max-height: calc(100vh - 60px);
}

.mobile-nav-link {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  font-size: var(--font-size-base);
  color: var(--color-text-primary);
  text-decoration: none;
  border-radius: var(--radius-md);
  transition: background var(--duration-fast);
}

.mobile-nav-link:hover,
.mobile-nav-link.is-active {
  background: var(--color-bg-secondary);
}

.mobile-nav-link.is-active {
  color: var(--color-primary);
  font-weight: var(--font-weight-semibold);
}

.mobile-nav-icon {
  width: 20px;
  text-align: center;
  color: var(--color-text-secondary);
}

.mobile-nav-link.is-active .mobile-nav-icon {
  color: var(--color-primary);
}
```

#### Bottom Navigation (Mobile Alternative)

```css
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-around;
  background: var(--color-bg-elevated);
  border-top: 1px solid var(--color-border-light);
  padding: var(--space-2) 0;
  padding-bottom: calc(var(--space-2) + env(safe-area-inset-bottom));
  z-index: var(--z-sticky);
}

.bottom-nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-4);
  font-size: var(--font-size-xs);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast);
}

.bottom-nav-item:hover,
.bottom-nav-item.is-active {
  color: var(--color-primary);
}

.bottom-nav-icon {
  font-size: 20px;
}

/* Hide bottom nav on desktop */
@media (min-width: 768px) {
  .bottom-nav {
    display: none;
  }
}

/* Add padding to main content when bottom nav is present */
@media (max-width: 767px) {
  .main-content {
    padding-bottom: calc(70px + env(safe-area-inset-bottom));
  }
}
```

### Navigation Patterns

#### Page Transitions

```javascript
// Simple fade transition between pages
function navigateTo(url) {
  const main = document.querySelector('.main-content');
  
  main.style.opacity = '0';
  main.style.transition = `opacity ${getComputedStyle(document.documentElement).getPropertyValue('--duration-fast')}`;
  
  setTimeout(() => {
    window.location.href = url;
  }, 150);
}

// Restore opacity on page load
document.addEventListener('DOMContentLoaded', () => {
  const main = document.querySelector('.main-content');
  main.style.opacity = '1';
});
```

#### Scroll Behavior

```css
html {
  scroll-behavior: smooth;
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
}

/* Scroll to top button */
.scroll-to-top {
  position: fixed;
  bottom: var(--space-5);
  right: var(--space-5);
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-primary);
  color: var(--color-text-inverse);
  border: none;
  border-radius: var(--radius-full);
  box-shadow: var(--shadow-md);
  cursor: pointer;
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--duration-normal), visibility var(--duration-normal);
  z-index: var(--z-sticky);
}

.scroll-to-top.is-visible {
  opacity: 1;
  visibility: visible;
}

.scroll-to-top:hover {
  background: var(--color-primary-hover);
}

/* Adjust position when bottom nav is present */
@media (max-width: 767px) {
  .scroll-to-top {
    bottom: calc(80px + env(safe-area-inset-bottom));
  }
}
```

#### Active Link Detection

```javascript
function setActiveNavLink() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    
    // Exact match for home
    if (href === '/' && currentPath === '/') {
      link.classList.add('is-active');
    }
    // Starts with match for other pages
    else if (href !== '/' && currentPath.startsWith(href)) {
      link.classList.add('is-active');
    }
    else {
      link.classList.remove('is-active');
    }
  });
}

document.addEventListener('DOMContentLoaded', setActiveNavLink);
```

### Navigation Accessibility

#### ARIA Landmarks

```html
<header role="banner">
  <nav aria-label="Main navigation">
    <!-- Primary nav -->
  </nav>
</header>

<main role="main" id="main-content">
  <nav aria-label="Breadcrumb">
    <ol class="breadcrumb">
      <!-- Breadcrumb items -->
    </ol>
  </nav>
  
  <!-- Page content -->
</main>

<nav class="bottom-nav" aria-label="Mobile navigation">
  <!-- Bottom nav items -->
</nav>
```

#### Skip Link

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: var(--space-4);
  padding: var(--space-3) var(--space-4);
  background: var(--color-primary);
  color: var(--color-text-inverse);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-md);
  z-index: calc(var(--z-toast) + 1);
  transition: top var(--duration-fast);
}

.skip-link:focus {
  top: var(--space-4);
}
```

```html
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <!-- Rest of page -->
</body>
```

#### Keyboard Navigation

| Key | Action |
|-----|--------|
| `Tab` | Move through nav items |
| `Enter` / `Space` | Activate link |
| `Escape` | Close mobile menu |
| `Home` | First nav item (within nav) |
| `End` | Last nav item (within nav) |

#### Mobile Menu Toggle

```html
<button 
  class="nav-mobile-toggle"
  aria-expanded="false"
  aria-controls="mobile-nav"
  aria-label="Open menu"
>
  <i class="fa fa-bars" aria-hidden="true"></i>
</button>
```

```javascript
function toggleMobileNav() {
  const toggle = document.querySelector('.nav-mobile-toggle');
  const nav = document.getElementById('mobile-nav');
  const backdrop = document.querySelector('.mobile-nav-backdrop');
  const isOpen = nav.classList.contains('is-open');
  
  nav.classList.toggle('is-open');
  backdrop.classList.toggle('is-visible');
  toggle.setAttribute('aria-expanded', !isOpen);
  toggle.setAttribute('aria-label', isOpen ? 'Open menu' : 'Close menu');
  
  // Trap focus when open
  if (!isOpen) {
    nav.querySelector('.mobile-nav-link').focus();
    document.body.style.overflow = 'hidden';
  } else {
    toggle.focus();
    document.body.style.overflow = '';
  }
}
```

### Sitemap (HTML)

For SEO and user reference, provide an HTML sitemap page:

```html
<div class="sitemap">
  <h1>Sitemap</h1>
  
  <section class="sitemap-section">
    <h2>Main Pages</h2>
    <ul class="sitemap-list">
      <li><a href="/">Home</a></li>
      <li>
        <a href="/files">Files</a>
        <ul>
          <li><a href="/files">All Files</a></li>
        </ul>
      </li>
      <li>
        <a href="/clipboard">Clipboard</a>
        <ul>
          <li><a href="/clipboard">All Items</a></li>
        </ul>
      </li>
    </ul>
  </section>
  
  <section class="sitemap-section">
    <h2>Actions</h2>
    <ul class="sitemap-list">
      <li>Upload File (from Home)</li>
      <li>Paste Content (from Clipboard)</li>
      <li>Search (global)</li>
    </ul>
  </section>
</div>
```

```css
.sitemap-section {
  margin-bottom: var(--space-8);
}

.sitemap-section h2 {
  font-size: var(--font-size-lg);
  margin-bottom: var(--space-3);
  padding-bottom: var(--space-2);
  border-bottom: 1px solid var(--color-border-light);
}

.sitemap-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sitemap-list li {
  padding: var(--space-2) 0;
}

.sitemap-list ul {
  margin-left: var(--space-6);
  margin-top: var(--space-2);
}

.sitemap-list a {
  color: var(--color-primary);
  text-decoration: none;
}

.sitemap-list a:hover {
  text-decoration: underline;
}
```

---

## 11. Forms & Validation

### Input Styling

```css
.form-control {
  width: 100%;
  padding: var(--space-2) var(--space-3);
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
  color: var(--color-text-primary);
  background: var(--color-bg-primary);
  border: 1px solid var(--color-border-default);
  border-radius: var(--radius-md);
  transition: border-color var(--duration-fast), box-shadow var(--duration-fast);
}

.form-control:hover {
  border-color: var(--color-text-muted);
}

.form-control:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.15);
}

.form-control:disabled {
  background: var(--color-bg-secondary);
  cursor: not-allowed;
  opacity: 0.7;
}

.form-control::placeholder {
  color: var(--color-text-muted);
}
```

### Validation States

```css
/* Error state */
.form-control.is-invalid {
  border-color: var(--color-danger);
}

.form-control.is-invalid:focus {
  box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.15);
}

/* Success state */
.form-control.is-valid {
  border-color: var(--color-success);
}

.form-control.is-valid:focus {
  box-shadow: 0 0 0 3px rgba(40, 167, 69, 0.15);
}

/* Error message */
.form-error {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  margin-top: var(--space-1);
  font-size: var(--font-size-sm);
  color: var(--color-danger);
}

/* Help text */
.form-help {
  margin-top: var(--space-1);
  font-size: var(--font-size-sm);
  color: var(--color-text-muted);
}
```

### Inline Validation Rules

| Trigger | Behavior |
|---------|----------|
| On blur | Validate when field loses focus |
| On input (after error) | Re-validate on each keystroke once an error is shown |
| On submit | Validate all fields |

### Character Counter

```css
.char-counter {
  font-size: var(--font-size-xs);
  color: var(--color-text-muted);
  text-align: right;
}

.char-counter.is-warning {
  color: var(--color-warning);
}

.char-counter.is-error {
  color: var(--color-danger);
}
```

### Form Layout

```css
.form-group {
  margin-bottom: var(--space-4);
}

.form-label {
  display: block;
  margin-bottom: var(--space-1);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
}

.form-label.is-required::after {
  content: ' *';
  color: var(--color-danger);
}
```

### Submit Button States

```css
/* Disable submit until form is valid */
.btn-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Loading state during submission */
.btn-submit.is-submitting {
  pointer-events: none;
}
```

---

## 12. Feedback & Notifications

### Toast Notifications

#### Toast Container

```css
.toast-container {
  position: fixed;
  top: var(--space-5);
  right: var(--space-5);
  z-index: var(--z-toast);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  pointer-events: none;
}

.toast-container > * {
  pointer-events: auto;
}
```

#### Toast Component

```css
.toast {
  min-width: 280px;
  max-width: 400px;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  animation: slideUp var(--duration-slow) var(--easing-out);
}

.toast-icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.toast-content {
  flex: 1;
  min-width: 0;
}

.toast-title {
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--space-1);
}

.toast-message {
  font-size: var(--font-size-sm);
  opacity: 0.9;
}

.toast-close {
  flex-shrink: 0;
  padding: var(--space-1);
  opacity: 0.7;
  cursor: pointer;
  transition: opacity var(--duration-fast);
}

.toast-close:hover {
  opacity: 1;
}
```

#### Toast Variants

| Variant | Background | Icon |
|---------|------------|------|
| Success | `--color-success` | `fa-check-circle` |
| Error | `--color-danger` | `fa-exclamation-circle` |
| Warning | `--color-warning` | `fa-exclamation-triangle` |
| Info | `--color-info` | `fa-info-circle` |

#### Toast Timing

| Property | Value |
|----------|-------|
| Auto-dismiss | `4000ms` |
| Pause on hover | Yes |
| Entry animation | `400ms` |
| Exit animation | `250ms` |

### Button Feedback Pattern

1. User clicks action button
2. Button shows loading state (spinner)
3. On success: Change to success icon/color
4. Hold success state for `1500ms`
5. Revert to original state

```javascript
async function handleAction(button) {
  const originalHTML = button.innerHTML;
  
  // Loading state
  button.classList.add('is-loading');
  button.disabled = true;
  
  try {
    await performAction();
    
    // Success state
    button.classList.remove('is-loading');
    button.classList.add('btn-success');
    button.innerHTML = '<i class="fa fa-check"></i>';
    
    // Revert after delay
    setTimeout(() => {
      button.classList.remove('btn-success');
      button.innerHTML = originalHTML;
      button.disabled = false;
    }, 1500);
    
  } catch (error) {
    // Error state
    button.classList.remove('is-loading');
    button.disabled = false;
    showToast('error', error.message);
  }
}
```

### Confirmation Dialogs

Required for destructive actions:

```javascript
async function confirmDelete(itemName) {
  return new Promise((resolve) => {
    showModal({
      title: 'Delete Item',
      message: `Are you sure you want to delete "${itemName}"? This action cannot be undone.`,
      confirmText: 'Delete',
      confirmClass: 'btn-danger',
      cancelText: 'Cancel',
      onConfirm: () => resolve(true),
      onCancel: () => resolve(false)
    });
  });
}
```

---

## 13. Icons

### Icon Library

Font Awesome 5.15.4 via CDN

### File Type Icons

| File Type | Icon | Color Token |
|-----------|------|-------------|
| Image (png, jpg, gif, webp) | `fa-file-image` | `--color-info` |
| PDF | `fa-file-pdf` | `--color-danger` |
| Text/Markdown | `fa-file-alt` | `--color-text-secondary` |
| Word | `fa-file-word` | `#2b579a` |
| Excel | `fa-file-excel` | `#217346` |
| PowerPoint | `fa-file-powerpoint` | `#d24726` |
| Archive (zip, rar) | `fa-file-archive` | `--color-warning` |
| Code | `fa-file-code` | `--color-primary` |
| Email/PST | `fa-envelope` | `--color-warning` |
| Generic | `fa-file` | `--color-text-muted` |

### Action Icons

| Action | Icon | Shortcut (if applicable) |
|--------|------|--------------------------|
| Upload | `fa-cloud-upload-alt` | — |
| Download | `fa-download` | — |
| Share | `fa-share-alt` | — |
| Delete | `fa-trash` | `Del` |
| Copy | `fa-copy` | `Ctrl+C` |
| Paste | `fa-paste` | `Ctrl+V` |
| View | `fa-eye` | — |
| Edit | `fa-edit` | — |
| Close | `fa-times` | `Esc` |
| Back | `fa-arrow-left` | — |
| Expand | `fa-chevron-down` | — |
| Collapse | `fa-chevron-up` | — |
| Settings | `fa-cog` | — |
| Search | `fa-search` | `Ctrl+K` |

### Icon Sizing

| Size | Class | Dimensions |
|------|-------|------------|
| Small | `fa-sm` | 14px |
| Default | — | 16px |
| Large | `fa-lg` | 20px |
| 2x | `fa-2x` | 32px |

---

## 14. Images & Media

### Image Containers

```css
/* Standard image container */
.image-container {
  background: var(--color-bg-secondary);
  padding: var(--space-5);
  border-radius: var(--radius-lg);
  text-align: center;
}

/* Card thumbnail */
.card-img-top {
  width: 100%;
  max-height: 300px;
  object-fit: contain;
  background: var(--color-bg-secondary);
}

/* Full-width content image */
.content-image {
  max-width: 100%;
  height: auto;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}

/* Clipboard preview */
.clipboard-image {
  max-width: 100%;
  max-height: 400px;
  object-fit: contain;
  border-radius: var(--radius-md);
  margin: var(--space-4) 0;
}
```

### Image Loading States

```css
/* Skeleton placeholder */
.image-skeleton {
  background: linear-gradient(
    90deg,
    var(--color-bg-secondary) 25%,
    var(--color-bg-tertiary) 50%,
    var(--color-bg-secondary) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Error state */
.image-error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-8);
  background: var(--color-bg-secondary);
  color: var(--color-text-muted);
}
```

### Aspect Ratio Containers

```css
.aspect-square { aspect-ratio: 1 / 1; }
.aspect-video { aspect-ratio: 16 / 9; }
.aspect-photo { aspect-ratio: 4 / 3; }
```

---

## 15. Responsive Design

### Breakpoints

| Name | Width | Target |
|------|-------|--------|
| `xs` | < 576px | Small phones |
| `sm` | ≥ 576px | Large phones |
| `md` | ≥ 768px | Tablets |
| `lg` | ≥ 992px | Small laptops |
| `xl` | ≥ 1200px | Desktops |
| `xxl` | ≥ 1400px | Large screens |

### Breakpoint Variables

```css
:root {
  --breakpoint-sm: 576px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 992px;
  --breakpoint-xl: 1200px;
  --breakpoint-xxl: 1400px;
}
```

### Media Query Mixins (SCSS)

```scss
@mixin sm { @media (min-width: 576px) { @content; } }
@mixin md { @media (min-width: 768px) { @content; } }
@mixin lg { @media (min-width: 992px) { @content; } }
@mixin xl { @media (min-width: 1200px) { @content; } }
@mixin xxl { @media (min-width: 1400px) { @content; } }

// Usage
.card {
  padding: var(--space-4);
  
  @include md {
    padding: var(--space-6);
  }
}
```

### Responsive Adjustments

#### Mobile (< 768px)

| Component | Adjustment |
|-----------|------------|
| Container padding | `16px` |
| Card padding | `16px` |
| Filename truncation | `150px` max |
| Table columns | Hide Size, Date |
| Button groups | Stack vertically |
| Modal | Full width, bottom sheet |
| Toast container | Bottom center |

#### Tablet (768px - 991px)

| Component | Adjustment |
|-----------|------------|
| Container | Max width `720px` |
| Grid | 2 columns for cards |
| Sidebar | Collapsible |

#### Desktop (≥ 992px)

| Component | Adjustment |
|-----------|------------|
| Container | Max width `960px` - `1140px` |
| Grid | 3-4 columns for cards |
| Sidebar | Always visible |
| Table | All columns visible |

### Touch Targets

Minimum touch target size: **44x44px**

```css
/* Ensure minimum touch target */
.btn,
.form-control,
.nav-link {
  min-height: 44px;
}

/* Increase spacing between touch targets */
@media (max-width: 767px) {
  .btn-group {
    gap: var(--space-2);
  }
}
```

---

## 16. Accessibility

### ARIA Requirements

| Element | Required Attributes |
|---------|---------------------|
| Toast container | `aria-live="polite"`, `role="region"`, `aria-label="Notifications"` |
| Individual toasts | `role="alert"`, `aria-live="assertive"` |
| Progress bar | `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-label` |
| Modal | `role="dialog"`, `aria-modal="true"`, `aria-labelledby` |
| Close buttons | `aria-label="Close"` |
| Expandable content | `aria-expanded`, `aria-controls` |
| Icon buttons | `aria-label` describing action |
| Loading buttons | `aria-busy="true"` |

### Keyboard Navigation

| Key | Action |
|-----|--------|
| `Tab` | Move focus forward |
| `Shift + Tab` | Move focus backward |
| `Enter` / `Space` | Activate button/link |
| `Escape` | Close modal/dropdown |
| `Arrow keys` | Navigate within component |

### Focus Management

```javascript
// Trap focus in modal
function trapFocus(modal) {
  const focusable = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;

    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });

  first.focus();
}
```

### Screen Reader Text

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

### Color Accessibility

- Never use color as the only indicator of state
- Always pair color with icons, text, or patterns
- Test with color blindness simulators

---

## 17. Error Handling & Edge Cases

### Error State Hierarchy

| Level | Display | Example |
|-------|---------|---------|
| Field | Inline below input | "Email is required" |
| Form | Alert above form | "Please fix 3 errors below" |
| Page | Full page error | 404, 500 pages |
| Global | Toast notification | "Network error" |

### Empty States

```css
.empty-state {
  text-align: center;
  padding: var(--space-12) var(--space-6);
  color: var(--color-text-secondary);
}

.empty-state-icon {
  font-size: 48px;
  margin-bottom: var(--space-4);
  opacity: 0.5;
}

.empty-state-title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--space-2);
}

.empty-state-description {
  margin-bottom: var(--space-6);
  max-width: 360px;
  margin-left: auto;
  margin-right: auto;
}
```

### Loading States

| Context | Pattern |
|---------|---------|
| Page load | Full page skeleton |
| Component | Skeleton placeholder |
| Button | Spinner, disabled state |
| Infinite scroll | Loading indicator at bottom |
| Refresh | Pull-to-refresh (mobile) |

### Skeleton Screens

```css
.skeleton {
  background: var(--color-bg-secondary);
  border-radius: var(--radius-md);
  animation: pulse 1.5s ease-in-out infinite;
}

.skeleton-text {
  height: 1em;
  margin-bottom: var(--space-2);
}

.skeleton-text:last-child {
  width: 70%;
}

.skeleton-title {
  height: 1.5em;
  width: 60%;
  margin-bottom: var(--space-3);
}

.skeleton-image {
  aspect-ratio: 16 / 9;
}
```

### Offline State

```css
.offline-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: var(--space-3) var(--space-4);
  background: var(--color-text-primary);
  color: var(--color-text-inverse);
  text-align: center;
  font-size: var(--font-size-sm);
  z-index: var(--z-toast);
}
```

### Error Messages

| Type | Tone | Example |
|------|------|---------|
| Validation | Helpful | "Please enter a valid email address" |
| Permission | Explanatory | "You don't have access to this file" |
| Network | Reassuring | "Connection lost. We'll retry automatically." |
| Server | Apologetic | "Something went wrong on our end. Please try again." |
| Not found | Guiding | "This page doesn't exist. Here's some helpful links." |

---

## 18. Design Principles

### Core Principles

1. **Clarity over cleverness** — Users should immediately understand what they can do
2. **Consistency builds trust** — Same actions, same patterns, everywhere
3. **Feedback is mandatory** — Every action gets a visible response
4. **Progressive disclosure** — Show basics first, details on demand
5. **Accessibility is non-negotiable** — Design for everyone from the start
6. **Performance is UX** — Fast interfaces feel better
7. **Mobile-first, not mobile-only** — Start small, enhance for larger screens
8. **Reduce cognitive load** — Fewer choices = faster decisions
9. **Forgiveness by design** — Make undo easy, confirmations for destructive actions
10. **Content-first hierarchy** — Design serves content, not the other way around

### Interaction Patterns

| Pattern | Implementation |
|---------|----------------|
| Drag & Drop | Visual feedback (scale, color), drop zone highlighting |
| Copy to Clipboard | Icon change → toast → revert (1.5s) |
| Delete | Confirm dialog → loading → toast → UI update |
| Upload | Progress bar → completion toast → list refresh |
| Collapse/Expand | Smooth height animation, chevron rotation |
| Double-click | Select all text in content areas |
| Long press (mobile) | Context menu for additional actions |

### Content Guidelines

| Element | Rule |
|---------|------|
| Buttons | Action verbs: "Upload", "Delete", "Save" |
| Labels | Nouns or noun phrases: "File name", "Upload date" |
| Placeholders | Examples, not labels: "example@email.com" |
| Errors | Specific, actionable: "File too large (max 10MB)" |
| Success | Confirm what happened: "File uploaded successfully" |
| Empty states | Explain and guide: "No files yet. Drop files here to upload." |

---

## 19. Implementation Checklist

### New Component Checklist

- [ ] Uses design tokens (no hardcoded values)
- [ ] All interactive states defined (default, hover, focus, active, disabled)
- [ ] Focus visible outline present
- [ ] Touch target ≥ 44px
- [ ] Works with keyboard navigation
- [ ] ARIA attributes added
- [ ] Responsive at all breakpoints
- [ ] Loading state defined
- [ ] Error state defined
- [ ] Empty state defined (if applicable)
- [ ] Animation respects `prefers-reduced-motion`
- [ ] Tested in dark mode
- [ ] Color contrast passes WCAG AA

### Page/View Checklist

- [ ] Page title set
- [ ] Heading hierarchy correct (h1 → h2 → h3)
- [ ] Focus management for modals/overlays
- [ ] Loading skeleton while fetching
- [ ] Error boundary with fallback UI
- [ ] Empty state for no data
- [ ] Offline state handling
- [ ] Mobile layout tested
- [ ] Print styles (if applicable)

### Accessibility Audit

- [ ] Lighthouse accessibility score ≥ 90
- [ ] VoiceOver/NVDA tested
- [ ] Keyboard-only navigation tested
- [ ] Color contrast verified
- [ ] Motion reduced mode tested
- [ ] Focus order logical
- [ ] Images have alt text
- [ ] Form labels associated

---

## External Dependencies

| Library | Version | CDN |
|---------|---------|-----|
| Bootstrap CSS | 4.3.1+ | stackpath.bootstrapcdn.com |
| Bootstrap JS | 4.3.1+ | stackpath.bootstrapcdn.com |
| Font Awesome | 5.15.4 | cdnjs.cloudflare.com |
| jQuery | 3.7.1 | code.jquery.com |
| Popper.js | 1.14.7+ | cdnjs.cloudflare.com |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2025-01 | Design tokens, dark mode, expanded breakpoints, motion guidelines, validation patterns |
| 1.0 | Initial | Original design guidelines |