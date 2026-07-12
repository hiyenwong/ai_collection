# arXiv HTML Section Extraction Pattern

Verified working pattern (2026-05-20) for extracting structured section content from arXiv HTML experimental pages (`https://arxiv.org/html/{id}v1`).

## Problem

arXiv HTML pages render the full paper in the browser. `browser_snapshot` returns the accessibility tree but is hard to parse for structured section content. `browser_console` JavaScript gives direct DOM access.

## Pattern

```javascript
(() => {
  const article = document.querySelector('article');
  if (!article) return 'No article found';
  const sections = [];
  const h2s = article.querySelectorAll('h2');
  for (const h2 of h2s) {
    let content = [];
    let next = h2.nextElementSibling;
    while (next && next.tagName !== 'H2' && next.tagName !== 'H3' && content.join('').length < 3000) {
      content.push(next.textContent.trim().substring(0, 600));
      next = next.nextElementSibling;
    }
    sections.push({heading: h2.textContent.trim().substring(0, 80), content: content.filter(t => t).join('\n').substring(0, 3000)});
  }
  return JSON.stringify(sections.slice(0, 8));
})()
```

### How it works

1. Finds `<article>` element (arXiv HTML wraps paper content in this)
2. Finds all `<h2>` headings (section titles)
3. For each section, collects sibling elements until next heading
4. Truncates to manageable sizes (600 chars per element, 3000 chars per section)
5. Returns first 8 sections as JSON array of `{heading, content}`

### Parameters to tune

- `sections.slice(0, 8)` → number of sections to return (increase for longer papers)
- `content.join('').length < 3000` → per-section character limit
- `.substring(0, 600)` → per-element character limit
- Add `h3` handling if paper uses nested subsections

### Pitfalls

- **Use `var` not `let/const`** in browser_console to avoid "Identifier already declared" errors from previous executions in the same session
- **Some papers use `<section>` instead of `<article>`** — if `article` is null, try `document.querySelector('section')` or `document.querySelector('main')`
- **Math rendering**: arXiv HTML renders math as `<span class="ltx_Math">` — text extraction captures the rendered text, not LaTeX source
- **Very long papers**: the `slice(0, 8)` limit skips appendices; increase or iterate by passing section indices
