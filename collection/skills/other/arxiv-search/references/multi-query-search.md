# arXiv Multi-Query Search Pattern

## Problem
arXiv API returns 429 rate limits on rapid queries. Single query returns limited results. Query strings with spaces cause `urllib.request` to fail with "URL can't contain control characters."

## Solution: Multi-Query with Proper URL Encoding + Dedup + Rate Limiting

### Preferred Pattern: execute_code with urllib + proxy (most reliable for cron jobs)

```python
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time

# CRITICAL: arXiv query strings with spaces MUST be URL-encoded
# urllib.request will throw "URL can't contain control characters" otherwise.
proxy_handler = urllib.request.ProxyHandler(
    {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
)
opener = urllib.request.build_opener(proxy_handler)

def search_arxiv(query, max_results=15):
    """Search arXiv — query is automatically URL-encoded"""
    encoded = urllib.parse.quote(query)  # ← REQUIRED for queries with spaces
    url = f'http://export.arxiv.org/api/query?search_query={encoded}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        resp = opener.open(req, timeout=30)
        return resp.read().decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def parse_response(xml_text):
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    if xml_text.startswith("Error"):
        return []
    root = ET.fromstring(xml_text)
    entries = root.findall('atom:entry', ns)
    results = []
    for entry in entries:
        id_elem = entry.find('atom:id', ns)
        title_elem = entry.find('atom:title', ns)
        summary_elem = entry.find('atom:summary', ns)
        published = entry.find('atom:published', ns)
        authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
        categories = [c.attrib.get('term', '') for c in entry.findall('atom:category', ns)]
        arxiv_id = id_elem.text.strip().split('/abs/')[-1].split('v')[0] if id_elem is not None else ''
        results.append({
            'id': arxiv_id,
            'title': title_elem.text.strip().replace('\n', ' ') if title_elem is not None else '',
            'summary': summary_elem.text.strip().replace('\n', ' ') if summary_elem is not None else '',
            'published': published.text[:10] if published is not None else '',
            'authors': authors[:5],
            'categories': categories,
        })
    return results

# Multi-query with deduplication
queries = [
    ('cat:q-bio.NC', 'neuroscience'),
    ('cat:cs.NE', 'neural-evolutionary'),
    ('all:neural-dynamics AND all:brain', 'neural-dynamics'),
    ('all:spiking-neural-network AND all:learning', 'spiking'),
    ('all:cognitive-neuroscience', 'cognitive'),
]

all_entries = []
for q, label in queries:
    xml_data = search_arxiv(q, max_results=15)
    if xml_data.startswith("Error"):
        print(f"  {label}: {xml_data}")
        continue
    papers = parse_response(xml_data)
    all_entries.extend(papers)
    time.sleep(3)  # CRITICAL: avoid 429 — 3s minimum between queries

# Deduplicate by arxiv ID
seen = set()
unique = []
for e in all_entries:
    if e['id'] not in seen:
        seen.add(e['id'])
        unique.append(e)
unique.sort(key=lambda x: x['published'], reverse=True)
```

### Alternative: httpx Client Pattern

```python
import httpx
import xml.etree.ElementTree as ET
import time

ARXIV_API = "https://export.arxiv.org/api/query"

def search_arxiv(query, max_results=10):
    params = {
        "search_query": query,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    with httpx.Client(timeout=30, proxy="http://127.0.0.1:7890") as client:
        resp = client.get(ARXIV_API, params=params, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        return resp.text
```

## Rate Limiting Strategy
- **Minimum delay**: 3 seconds between queries
- **429 recovery**: Wait 10+ seconds, then retry with exponential backoff
- **Bulk operations**: Use `sleep(10)` between each query for safety
- **Proxy**: If behind proxy, add `proxy="http://127.0.0.1:7890"` to httpx.Client, or use `urllib.request.ProxyHandler` for urllib

## Alternative: Use web_search
When arxiv API is heavily rate-limited, fall back to `web_search` for discovery, then use API only for specific paper IDs.
