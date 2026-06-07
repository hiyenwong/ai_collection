# arXiv API Retry & Fallback Patterns

## Problem
arXiv API (`export.arxiv.org`) frequently returns HTTP 429 (rate limit) or times out, especially through proxies.

## Working Patterns

### Pattern 1: httpx with proxy (recommended)
```python
import httpx
with httpx.Client(timeout=60, proxy="http://127.0.0.1:7890") as client:
    response = client.get("https://export.arxiv.org/api/query", params={...})
```

### Pattern 2: Cache fallback (when API is unavailable)
```python
# If arxiv API fails (429/timeout), check workspace for cached results:
import json, os
for cache_file in ['arxiv_economics_quantum.json', 'arxiv_results.json']:
    path = os.path.join("/Users/hiyenwong/.openclaw/workspace", cache_file)
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        break
```

### Pattern 3: Use kg.db as fallback
```python
import sqlite3
conn = sqlite3.connect("/Users/hiyenwong/.openclaw/workspace/kg.db")
cursor = conn.cursor()
cursor.execute("SELECT id, title, content FROM kg_entities WHERE title LIKE '%quantum%' ORDER BY published_date DESC LIMIT 5")
```

## Rate Limiting
- Add `time.sleep(3)` between consecutive arXiv API calls
- Max 3 requests per minute to avoid 429
