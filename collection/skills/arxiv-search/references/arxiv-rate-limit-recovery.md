# arXiv Rate Limit Recovery Pattern (Updated 2026-05-19)

## Problem
The arXiv API aggressively rate-limits automated queries, returning HTTP 429 "Rate exceeded" or timeouts even with modest request volumes.

## Working Retry Pattern

```python
import urllib.request, urllib.parse, time, ssl

def search_arxiv_with_retry(query, max_results=5, max_retries=5):
    url = f"https://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&max_results={max_results}&sortBy=submittedDate"
    headers = {
        'User-Agent': 'ResearchAgent/1.0 (+mailto:research@example.com)',
        'Accept': 'application/xml'
    }
    
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            ctx = ssl.create_default_context()
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                return resp.read().decode('utf-8')
        except Exception as e:
            if '429' in str(e) or 'Rate' in str(e):
                wait = 10 * (attempt + 1)  # 10s, 20s, 30s, 40s, 50s
                time.sleep(wait)
            elif 'timeout' in str(e).lower():
                wait = 5 * (attempt + 1)
                time.sleep(wait)
            else:
                time.sleep(3)
    return None
```

## Key Findings

1. **Custom User-Agent is mandatory** — requests without one get blocked faster
2. **Exponential backoff starting at 10s** — 3-5s delays trigger immediate re-rate-limit
3. **urllib.request > httpx** — urllib survives 429/503 more reliably (httpx connection pooling can carry stale state)
4. **Insert 3s sleep between consecutive queries** even after successful responses
5. **Save intermediate results** — partial progress survives when later queries fail

## Practical Multi-Query Pattern

```python
import time

queries = ['all:"quantum machine learning"', 'all:"quantum neural network"', 'cat:quant-ph']
results = []

for q in queries:
    xml = search_arxiv_with_retry(q, max_results=3)
    if xml:
        results.append(parse_arxiv_xml(xml))
    time.sleep(3)  # Between successful queries

# Deduplicate by arXiv ID
all_papers = {}
for paper_list in results:
    for p in paper_list:
        all_papers[p['id']] = p
```
