# Browser Console JavaScript for arXiv Listing Extraction

Verified patterns for extracting paper metadata from arXiv listing pages via `browser_console(expression=...)`.

## Pattern 1: Extract IDs + Titles from `<dt>/<dd>` listing

Works on `https://arxiv.org/list/{category}/recent` pages.

```javascript
Array.from(document.querySelectorAll('div#content dl dt')).map(dt => {
  const links = dt.querySelectorAll('a');
  const arxivLink = Array.from(links).find(a => a.href.includes('arxiv.org/abs'));
  const id = arxivLink ? arxivLink.textContent.replace('arXiv:', '').trim() : '';
  const dd = dt.nextElementSibling;
  const title = dd ? dd.childNodes[0].textContent.trim() : '';
  return { id, title };
}).filter(p => p.id).slice(0, 20)
```

**Verified 2026-05-22** — returns clean `{id, title}` pairs from quant-ph listing.

## Pattern 2: IDs + Titles + Authors

```javascript
Array.from(document.querySelectorAll('div#content dl dt')).map(dt => {
  const idEl = dt.querySelector('a[href*="arXiv:"]');
  const id = idEl ? idEl.textContent.trim() : '';
  const dd = dt.nextElementSibling;
  const title = dd ? dd.childNodes[0].textContent.trim() : '';
  const authors = dd ? Array.from(dd.querySelectorAll('a')).map(a => a.textContent).join(', ') : '';
  return { id, title, authors };
}).slice(0, 20)
```

## Pattern 3: Quick ID regex scan

```javascript
Array.from(document.querySelectorAll('a[href*="arxiv.org/abs/"]'))
  .map(a => a.href.match(/abs\/([0-9.]+)/))
  .filter(Boolean)
  .map(m => m[1])
```

## Usage
```
browser_navigate("https://arxiv.org/list/quant-ph/recent")
browser_console(expression="<javascript>")
```

## Notes
- Use `var` not `let`/`const` across multiple console expressions in same session
- `<dt>/<dd>` structure consistent across most arxiv listing pages; `<li.arxiv-result>` used on search pages
- First text node in `<dd>` is always the title; `<a>` elements are authors

## Pitfall: ancestor-qualified `dt` selectors fail but bare `dt` works (2026-06-03 + 2026-07-03)
**Problem (2026-06-03)**: Standard qualified selectors like `div#content dl dt` return **empty results** on `arxiv.org/list/quant-ph/recent`.
**Correction (2026-07-03)**: The failure is specific to the **qualified selector** `div#content dl dt`. The **bare selector** `document.querySelectorAll('dt')` works reliably on the same page (verified 2026-07-03, returned 11 ML-relevant papers from a 426-entry quant-ph listing). The ancestor-qualified selector fails because the DOM nesting doesn't match; the bare selector bypasses the issue.

**Universal fallback** (works regardless of selector issues) — parse `document.body.innerText` with regex:
```javascript
var text = document.body.innerText;
var lines = text.split('\n');
var papers = [];
var currentId = '';
for (var i = 0; i < lines.length; i++) {
  var line = lines[i].trim();
  var idMatch = line.match(/arXiv:(\d{4}\.\d{5})/);
  if (idMatch) {
    currentId = idMatch[1];
  } else if (currentId && line.length > 15 && line.length < 300 && !line.includes('Comments:') && !line.includes('Subjects:') && !line.includes('Authors:')) {
    papers.push({id: currentId, title: line});
    currentId = '';
  }
}
JSON.stringify(papers.slice(0, 50));
```

## Pattern 4: Extract from arXiv Search UI page (`/search/` — 2026-05-24 verified)

The search results page uses `<li class="arxiv-result">`.

```javascript
(() => {
  var out = [];
  var items = document.querySelectorAll('li.arxiv-result');
  items.forEach(function(li) {
    var id = '';
    var links = li.querySelectorAll('a');
    for (var i = 0; i < links.length; i++) {
      var t = links[i].textContent.trim();
      if (t.startsWith('arXiv:') && id === '') { id = t.replace('arXiv:', ''); break; }
    }
    var paras = li.querySelectorAll('p');
    var title = '';
    for (var j = 0; j < paras.length; j++) {
      var txt = paras[j].textContent.trim();
      if (txt && !txt.startsWith('Authors:') && !txt.startsWith('Submitted') && !txt.startsWith('Comments:')) { title = txt.substring(0, 250); break; }
    }
    out.push({ id: id, title: title });
  });
  return JSON.stringify(out);
})()
```

**Pitfall**: `.list-title a:first-of-type` grabs `[pdf, ps, other]` instead of the arXiv ID on the search page. Fix: iterate all links and filter by `text.startsWith('arXiv:')`.

## Pattern 5: Bare `dt` selector + inline keyword filter (2026-07-03 verified) — FIRST CHOICE for listing scans

The most token-efficient pattern for scanning a large listing page (e.g., 426 entries) and returning only domain-relevant papers. Uses the bare `dt` selector (not the ancestor-qualified one that fails) and filters browser-side via regex so irrelevant papers never enter the agent context.

```javascript
[...document.querySelectorAll('dt')].map(dt => {
  const dd = dt.nextElementSibling;
  return `${dt.textContent.replace(/\s+/g,' ').trim()} :: ${dd ? dd.textContent.replace(/\s+/g,' ').trim().substring(0,160) : ''}`;
}).filter(l => /learn|neural|reservoir|kernel|classif|reinforce|trainab|variational|qml|qaoa|optimi|benchmark|decoher|error/gi.test(l)).join('\n').substring(0, 4000)
```

**Advantages**:
- Returns a compact string (not JSON array), typically <4KB even from a 426-entry listing
- Keyword filtering happens browser-side, so irrelevant papers never enter the agent context
- The `::` separator makes output human-readable for quick scanning

**Tuning the keyword regex per domain**:
- Quantum-ML: `learn|neural|reservoir|kernel|classif|reinforce|trainab|variational|qml|qaoa|optimi|benchmark`
- Neuroscience: `brain|neural|spike|eeg|fmri|cortex|synap|hippocam|cognit`
- Systems engineering: `control|consensus|mpc|robust|stability|lyapunov|distributed|observer`
- Adjust per domain.

**Selection order**: Pattern 5 (bare `dt` + inline filter) → universal innerText fallback → Pattern 1 (if DOM structure is clean). Pattern 5 is the first choice because it is both reliable and token-efficient.
