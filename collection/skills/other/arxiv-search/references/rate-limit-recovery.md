# arXiv API Rate Limiting and Recovery

## Observed Patterns

- HTTP 429 "Rate exceeded" after ~2-3 rapid requests from same IP
- Plain HTTP (not HTTPS) triggers security scan blocks (H-level security warnings)
- 5-second delays between requests may still not be enough during peak hours
- Broad keyword searches are more likely to be rate-limited than ID-based lookups

## Recovery Strategies

### 1. Always use HTTPS
```
https://export.arxiv.org/api/query
```
HTTP may trigger security blocks or be rejected by agent tooling.

### 2. URL-encode all queries
```python
import urllib.parse
query = 'all:"quantum medicine" OR all:"quantum healthcare"'
encoded = urllib.parse.quote(query)
url = f'https://export.arxiv.org/api/query?search_query={encoded}'
```

### 3. Use proxy (if available)
**curl:**
```bash
curl -s -x http://127.0.0.1:7890 "https://export.arxiv.org/api/query?..."
```

**Python httpx:** Set `ALL_PROXY` env var. Do NOT use `proxies=` kwarg — `httpx.get()` rejects it:
```python
import os
os.environ['ALL_PROXY'] = 'http://127.0.0.1:7890'
resp = httpx.get(url, timeout=60)
```

### 4. Fetch by ID when searches fail
ID-based queries are less likely to be rate-limited:
```bash
curl -s -x http://127.0.0.1:7890 "https://export.arxiv.org/api/query?id_list=2605.10856"
```

### 5. Fallback to kg.db
If the API is fully blocked, query the local knowledge graph:
```bash
sqlite3 kg.db "SELECT id, title, content, category FROM kg_entities WHERE category LIKE '%quant%';"
```

## Delays

Minimum 5 seconds between requests. 10+ seconds during peak hours or after a 429 response.
