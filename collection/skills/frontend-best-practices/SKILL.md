---
name: frontend-best-practices
description: Senior Front-End Developer guidance for ReactJS, NextJS, JavaScript, TypeScript, HTML, CSS and modern UI/UX frameworks. Use when building front-end applications, writing React/Next.js code, or implementing UI components. Triggers on: frontend, react, nextjs, typescript, tailwindcss, ui development.
---

# Front-End Best Practices

Senior Front-End Developer guidance for modern web development.

## Coding Environment

The user asks questions about the following coding languages:
- ReactJS
- NextJS
- JavaScript
- TypeScript
- TailwindCSS
- HTML
- CSS

## Code Implementation Guidelines

### Early Returns

```typescript
// ✅ Good - early return
function getUserName(user: User | null): string {
  if (!user) return 'Anonymous';
  if (!user.name) return 'Unknown';
  return user.name;
}

// ❌ Bad - nested conditions
function getUserName(user: User | null): string {
  if (user) {
    if (user.name) {
      return user.name;
    } else {
      return 'Unknown';
    }
  } else {
    return 'Anonymous';
  }
}
```

### TailwindCSS Styling

```tsx
// ✅ Good - use Tailwind classes
<button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
  Click me
</button>

// ❌ Bad - avoid inline CSS
<button style={{ padding: '8px 16px', backgroundColor: 'blue' }}>
  Click me
</button>
```

### Descriptive Naming

```typescript
// ✅ Good - descriptive names with auxiliary verbs
const isLoading = false;
const hasError = true;
const canEdit = true;

// Event handlers with "handle" prefix
const handleClick = () => {};
const handleKeyDown = () => {};
const handleSubmit = () => {};

// ❌ Bad - unclear names
const flag = false;
const err = true;
const edit = true;

const click = () => {};
const keyDown = () => {};
```

### Accessibility Features

```tsx
// ✅ Good - accessible interactive element
<div
  role="button"
  tabIndex={0}
  aria-label="Toggle menu"
  onClick={handleClick}
  onKeyDown={handleKeyDown}
>
  Menu
</div>

// ❌ Bad - not accessible
<div onClick={handleClick}>
  Menu
</div>
```

### Const Over Function

```typescript
// ✅ Good
const toggle = () => setIsOpen(!isOpen);
const fetchData = async () => { /* ... */ };

// ❌ Bad
function toggle() {
  setIsOpen(!isOpen);
}
```

### No Semicolons (Optional)

```typescript
// ✅ Good (if configured)
const name = 'John'
const greeting = `Hello ${name}`

// ❌ Bad (if configured for no semicolons)
const name = 'John';
const greeting = `Hello ${name}`;
```

## Commit Guidelines

### Commit Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Description | Version |
|------|-------------|---------|
| `feat` | New feature | MINOR |
| `fix` | Bug fix | PATCH |
| `chore` | Maintenance | - |
| `docs` | Documentation | - |
| `style` | Formatting | - |
| `refactor` | Code refactoring | - |
| `perf` | Performance | - |
| `test` | Tests | - |

### Examples

```bash
feat(auth): add OAuth2 login support
fix(api): resolve race condition in data fetching
docs(readme): update installation instructions
refactor(utils): simplify date formatting logic
```

## Best Practices

1. **Follow the user's requirements carefully & to the letter**
2. **Think step-by-step** - describe your plan in pseudocode first
3. **Confirm, then write code**
4. **Always write correct, best practice, DRY principle, bug free, fully functional code**
5. **Focus on easy and readability code, over being performant**
6. **Fully implement all requested functionality**
7. **Leave NO todo's, placeholders or missing pieces**
8. **Ensure code is complete! Verify thoroughly**
9. **Include all required imports, and ensure proper naming of key components**
10. **Be concise - minimize any other prose**
## Activation Keywords

- `frontend-best-practices`
- `frontend-best-practices`
- `frontend best practices`

## Tools Used

- `exec`
- `read`
- `write`
- `edit`

## Instructions for Agents

1. Read the task description carefully
2. Follow the step-by-step process
3. Use the appropriate tools
4. Verify the results

## Examples

### Example 1: Basic Usage

**User:** <example user request>

**Agent:** <example agent response>

### Example 2: Advanced Usage

**User:** <example user request>

**Agent:** <example agent response>
