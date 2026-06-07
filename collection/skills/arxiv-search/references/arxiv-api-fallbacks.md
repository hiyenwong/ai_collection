# arXiv API Fallback Strategies

## Problem
arXiv API aggressively rate-limits (HTTP 429) — returns "Rate exceeded." on most requests even with 10s delays between calls.

## Fallback Chain (try in order)

### 1. API with Retry + Long Delay
```python
import httpx, time
proxy = httpx.Proxy("http://127.0.0.1:7890")
client = httpx.Client(proxy=proxy, timeout=30)
for attempt in range(3):
    r = client.get(url)
    if r.status_code == 429:
        time.sleep(10 * (attempt + 1))
        continue
    break
```

### 2. Browser-based arXiv Search
Use `browser_navigate` to `https://arxiv.org/search/?searchtype=all&query=KEYWORDS&order=-announced_date_first`
- Then `browser_snapshot` to extract paper listings
- Navigate to individual papers via `https://arxiv.org/abs/{id}`

### 3. Browse arXiv Category Listings
`https://arxiv.org/list/{category}/recent` — shows recent submissions by category
- q-bio.NC: Neurons and Cognition
- cs.NE: Neural and Evolutionary Computing
- cs.AI: Artificial Intelligence

### 4. q-bio.NC Specific Listing
`https://arxiv.org/list/q-bio.NC/recent` — direct recent listing for neuroscience

## Pitfalls
- **arXiv API returns 429 on almost every request** even with proxy and 10s delays
- **curl to arXiv API returns empty response** on timeout — check exit code
- **web_search for arxiv fails** with 'NoneType' status_code errors
- **browser_navigate to arxiv.org/search can timeout** on heavy searches
- **Never pipe curl output to python** — security guardrail blocks it
