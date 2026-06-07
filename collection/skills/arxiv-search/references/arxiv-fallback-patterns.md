# arXiv Tool Fallback Patterns

## Problem
The arXiv API is heavily rate-limited (429 "Rate exceeded.") and both `web_search` and `web_extract` fail for arxiv URLs. This session documented three reliable fallback methods.

## Method 1: Browser Category Listings
Most reliable for discovering recent papers. Each category listing page shows all recent papers with full abstracts in the DOM.

```
browser_navigate → https://arxiv.org/list/{category}/new
```

Common categories: `q-bio.NC` (Neurons & Cognition), `cs.NE` (Neural & Evolutionary Computing), `cs.AI`, `cs.LG`, `cs.CV`, `cs.CL`.

## Method 2: HTML Paper Reading
For reading full paper content:

```
browser_navigate → https://arxiv.org/html/{paper_id}
browser_console → extract article text
```

The paper ID format is `2605.08014` (YYMM.NNNNN). Use `v1` suffix if needed.

## Method 3: Abstract Pages
For metadata only:

```
browser_navigate → https://arxiv.org/abs/{paper_id}
```

## What Doesn't Work
- `curl`/`httpx` to `export.arxiv.org/api/query` → 429 rate limit
- `web_search` with arxiv queries → NoneType errors
- `web_extract` with arxiv URLs → "Blocked: private/internal network"
