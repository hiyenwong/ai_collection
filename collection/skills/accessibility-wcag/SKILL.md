---
name: accessibility-wcag
description: Expert guidance for web accessibility (WCAG 2.2). Treat a11y violations as compile errors. Use when implementing accessibility features, auditing a11y compliance, or working with screen readers. Triggers on: accessibility, wcag, a11y, aria, screen reader, keyboard navigation.
---

# Accessibility (WCAG 2.2)

Expert guidance for web accessibility. Treat a11y violations as compile errors.

## Required Patterns

### Icon Buttons

```typescript
// ✅ Required
<IconButton aria-label="Close dialog">
  <CloseIcon />
</IconButton>

// ❌ Violation - blocks PR
<IconButton>
  <CloseIcon />
</IconButton>
```

### Custom Interactive Elements

```typescript
// ✅ Required for non-button clickable elements
<div
  role="button"
  tabIndex={0}
  onKeyDown={handleKeyDown}
  onClick={handleClick}
  aria-pressed={isActive}
>
  Toggle
</div>
```

### Images

```typescript
// ✅ Meaningful images
<img src="chart.png" alt="Q4 sales increased 25%" />

// ✅ Decorative images
<img src="decoration.png" alt="" role="presentation" />

// ❌ Missing alt
<img src="chart.png" />
```

### Form Fields

```typescript
// ✅ Associated label
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// ✅ Or aria-label
<input aria-label="Search products" type="search" />
```

### Error Announcements

```typescript
// ✅ Announce errors to screen readers
<div role="alert" aria-live="polite">
  {error && <span>{error}</span>}
</div>
```

### Focus Management

```css
/* ✅ Visible focus indicator */
:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* ❌ Never do this */
:focus {
  outline: none;
}
```

### Modal Focus Trap

```typescript
// ✅ Required for modals
useEffect(() => {
  const modal = modalRef.current;
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];
  
  firstElement?.focus();
  
  // Trap focus within modal
}, [isOpen]);
```

### Keyboard Navigation

```typescript
// ✅ Support keyboard
onKeyDown={(e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    handleAction();
  }
  if (e.key === 'Escape') {
    handleClose();
  }
}}
```

## WCAG 2.2 New Requirements

| Criterion | Description |
|-----------|-------------|
| **2.5.8 Target Size** | Minimum 24x24 CSS pixels |
| **2.4.12 Focus Not Obscured** | Focus indicator not hidden |
| **3.3.7 Redundant Entry** | Don't ask for same info twice |

## Quick Checklist

- [ ] All images have meaningful alt text
- [ ] Form fields have associated labels
- [ ] Interactive elements are keyboard accessible
- [ ] Focus indicators are visible
- [ ] Errors are announced to screen readers
- [ ] Modals trap focus
- [ ] Touch targets are at least 24x24px