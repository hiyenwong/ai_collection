# arXiv API Rate Limit Fallback

## Problem

The arXiv API (`export.arxiv.org/api/query`) frequently returns HTTP 429 (rate exceeded), especially when queried from cron jobs or with multiple rapid requests. The standard `curl`/`httpx`/`arxiv` Python package approaches all fail under rate limits.

## Fallback: HTML Scraping

When the API is rate-limited, fall back to scraping arXiv category pages:

### Step 1: Fetch category listing

```
URL: https://arxiv.org/list/{category}/recent
Categories: q-bio.NC, cs.NE, cs.LG, etc.
```

### Step 2: Parse paper entries from HTML

```python
import re, httpx

with httpx.Client(timeout=20, follow_redirects=True) as c:
    r = c.get(f"https://arxiv.org/list/{cat}/recent")
    html = r.text

# Extract all dt/dd pairs (each paper = one dt + one dd)
dts = list(re.finditer(r'<dt>.*?</dt>', html, re.DOTALL))
dds = list(re.finditer(r'<dd>.*?</dd>', html, re.DOTALL))
```

### Step 3: Extract paper metadata from dt

```python
# arxiv ID from dt
id_match = re.search(r'/abs/(\d+\.\d+)', dt_text)
arxiv_id = id_match.group(1).split("v")[0]

# Title from dt
title_match = re.search(r'"list-title[^"]*">(.*?)</div>', dt_text, re.DOTALL)
title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
title = re.sub(r'^Title:\s*', '', title)
```

### Step 4: Fetch full abstracts from /abs pages

```python
# The listing page only shows truncated abstracts
# Fetch full abstract from individual paper pages
time.sleep(3)  # Rate limit between requests
r = c.get(f"https://arxiv.org/abs/{arxiv_id}")
abs_match = re.findall(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', r.text, re.DOTALL)
if abs_match:
    abstract = re.sub(r'<[^>]+>', '', abs_match[0]).strip()
    abstract = re.sub(r'\s+', ' ', abstract)
```

### Rate Limit Guidelines

- Wait **3-4 seconds** between requests to arXiv
- Use `httpx.Client` with `follow_redirects=True`
- Prefer `http://` endpoint over `https://` for slightly better availability
- Max ~5-10 papers per cron job to avoid aggressive rate limiting

## Alternative: Semantic Scholar API

If arXiv is completely unavailable, try:
```
https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&sort=year:desc
```
Note: Also rate-limited without an API key (anonymous limit is low).
