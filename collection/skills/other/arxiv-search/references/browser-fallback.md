# Browser Fallback for arXiv Search

When the arXiv API returns 429 or timeouts, use browser navigation. This has NO rate limits.

## Category Listing Pages

Browse by category for new/recent submissions:

```
https://arxiv.org/list/q-bio.NC/new      # New submissions only
https://arxiv.org/list/q-bio.NC/recent   # Recent (last ~30 days)
https://arxiv.org/list/cs.NE/new         # Neural and Evolutionary Computing
https://arxiv.org/list/cs.LG/new         # Machine Learning
https://arxiv.org/list/stat.ML/new       # Statistics ML
```

**Workflow:**
1. `browser_navigate(url="https://arxiv.org/list/{category}/new")`
2. `browser_snapshot(full=True)` — contains structured `term` (arXiv ID + links) and `definition` (title, authors, subjects) elements
3. Parse the text output directly — each paper has arXiv ID, title, authors, and subject line
4. For abstracts: `browser_navigate(url="https://arxiv.org/abs/{id}")` then `browser_snapshot(full=True)`

## Individual Paper Pages

For full paper details (abstract, metadata):

```
https://arxiv.org/abs/{id}    # Abstract page (use this for details)
https://arxiv.org/html/{id}   # HTML rendering (if available)
```

**Never use** `web_extract` for arXiv URLs — returns "Blocked" or empty content.

## Verified Working (2026-05-07)

- `browser_navigate` → `/list/q-bio.NC/new` — 12 entries, full structure
- `browser_navigate` → `/list/cs.NE/recent` — 41 entries, full structure
- `browser_navigate` → `/abs/2605.04088` — full abstract and metadata
- `browser_snapshot(full=True)` — reliable text extraction from both page types

## What NOT to Do

- ❌ `httpx.get()` against arXiv API — returns 429 or empty responses
- ❌ `curl` with proxy against arXiv API — times out or 429
- ❌ `web_extract` for arxiv.org URLs — returns "Blocked" or empty
- ❌ `web_search` for arxiv.org — returns NoneType errors
- ❌ Piping curl output to Python — blocked by security guardrail
