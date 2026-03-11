---
name: react-components
description: Expert guidance for React component architecture, maintainability, and best practices. Use when building React components, reviewing component structure, optimizing component performance, or working with React hooks. Triggers on: react component, component architecture, react best practices, component size, react hooks.
---

# React Components

Expert guidance for React component architecture and maintainability.

## Component Size Limits

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Lines of code | < 150 | 150-300 | > 300 |
| Imports | < 20 | 20-35 | > 35 |
| useState calls | < 4 | 4-6 | > 6 |
| useEffect calls | < 3 | 3-5 | > 5 |

**If exceeded:** Stop and suggest decomposition.

## Hook Patterns

### AbortController for async useEffect

```typescript
useEffect(() => {
  const controller = new AbortController();
  
  const fetchData = async () => {
    try {
      const result = await api.getData({ signal: controller.signal });
      setData(result);
    } catch (err) {
      if (!controller.signal.aborted) {
        setError(err);
      }
    }
  };
  
  fetchData();
  return () => controller.abort();
}, [dependency]);
```

### useWatch over watch()

```typescript
// ✅ Good - reactive, no full re-render
const value = useWatch({ name: 'field', control });

// ❌ Bad - causes full form re-render
const value = methods.watch();
```

### Memoize schemas

```typescript
// ✅ Good
const schema = useMemo(() => yup.object({
  field: yup.string().required()
}), []);

// ❌ Bad - recreated every render
const schema = yup.object({ field: yup.string().required() });
```

### No components inside render

```typescript
// ✅ Good - defined outside or memoized
const InfoTrigger = memo(({ onClick }) => (
  <button onClick={onClick}>Info</button>
));

// ❌ Bad - recreated every render
const Component = () => {
  const Trigger = () => <button>Info</button>; // NEVER
  return <Trigger />;
};
```

## File Structure

```
ComponentName/
├── ComponentName.tsx       # Logic (< 100 lines)
├── ComponentName.styled.ts # Styles only
├── ComponentName.types.ts  # Types/interfaces
├── ComponentName.test.tsx  # Tests
└── hooks/
    └── useComponentData.ts # Extracted logic
```

## Best Practices

1. **Keep components small** - Under 150 lines
2. **Extract custom hooks** - Reusable logic
3. **Use TypeScript** - Proper type definitions
4. **Memoize expensive computations** - useMemo, useCallback
5. **Handle cleanup** - AbortController for async operations