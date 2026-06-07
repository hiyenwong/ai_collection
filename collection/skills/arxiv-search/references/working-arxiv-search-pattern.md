# Working arXiv Search Pattern (Cron / Background Jobs)

Verified 2026-05-17. The key issues: rate limiting (429), proxy support, redirect handling, timezone comparison.

## Critical Requirements

1. **HTTPS only** — HTTP redirects to HTTPS, causing failures without `follow_redirects=True`
2. **OR-combine queries** — don't make multiple separate calls; arXiv rate-limits at ~4 calls
3. **Transport-based proxy** — `httpx.Client(proxies=...)` is wrong syntax
4. **Timezone-aware cutoff** — use `datetime.now(timezone.utc)`

## Minimal Working Code

```python
import httpx
import xml.etree.ElementTree as ET
import time
from datetime import datetime, timedelta, timezone

ARXIV_API = "https://export.arxiv.org/api/query"
proxy_url = "http://127.0.0.1:7890"  # or None

# Combine all keywords in ONE query to avoid 429
search_query = 'cat:q-bio.NC'  # or: 'all:"spiking neural network" OR all:"neural dynamics"'

params = {
    "search_query": search_query,
    "max_results": 10,
    "sortBy": "submittedDate",
    "sortOrder": "descending"
}

proxy = httpx.Proxy(url=proxy_url) if proxy_url else None
transport = httpx.HTTPTransport(proxy=proxy) if proxy else None

with httpx.Client(transport=transport, timeout=60, follow_redirects=True) as client:
    resp = client.get(ARXIV_API, params=params)
    resp.raise_for_status()

ns = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom"
}
root = ET.fromstring(resp.text)
cutoff = datetime.now(timezone.utc) - timedelta(days=14)

papers = []
for entry in root.findall("atom:entry", ns):
    published = entry.find("atom:published", ns).text
    pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
    if pub_date < cutoff:
        continue
    
    title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
    abstract = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
    paper_id = entry.find("atom:id", ns).text.split("/")[-1]
    authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
    categories = [c.get("term") for c in entry.findall("atom:category", ns)]
    
    papers.append({
        "id": paper_id, "title": title, "abstract": abstract,
        "authors": authors, "categories": categories,
        "published": pub_date.strftime("%Y-%m-%d"),
        "abs_url": f"https://arxiv.org/abs/{paper_id}",
        "pdf_url": f"https://arxiv.org/pdf/{paper_id}"
    })
```

## Retry Pattern (for 429)

```python
for attempt in range(3):
    try:
        resp = client.get(ARXIV_API, params=params)
        resp.raise_for_status()
        break
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            time.sleep(5 * (attempt + 1))
        else:
            raise
```

## Common Failure Modes

| Error | Cause | Fix |
|-------|-------|-----|
| `proxies` unexpected keyword | Wrong httpx API | Use `HTTPTransport(proxy=...)` |
| 301 redirect | HTTP → HTTPS | Use HTTPS URL + `follow_redirects=True` |
| 429 Too Many Requests | Rate limiting | Combine queries with OR, add delays |
| can't compare offset-naive/aware | `datetime.now()` vs `fromisoformat` | Use `datetime.now(timezone.utc)` |
| curl_pipe_shell security | Terminal pipes curl to python | Use `execute_code` instead |
