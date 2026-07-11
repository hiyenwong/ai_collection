# arXiv Search - Proven Patterns & Pitfalls

## Working Search Pattern (urllib with headers)

The arXiv API is aggressively rate-limited. httpx often hangs; urllib with proper User-Agent works reliably.

```python
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, ssl

def search_arxiv(query, max_results=10):
    # Multi-category OR pattern for broad coverage
    search_query = f'all:"{query}" AND (cat:q-bio.NC OR cat:cs.NE OR cat:cs.LG OR cat:cs.AI)'
    encoded = urllib.parse.quote(search_query, safe='():')
    url = f'https://export.arxiv.org/api/query?search_query={encoded}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'
    
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'HermesResearchBot/1.0 (mailto:test@example.com)')
    ctx = ssl.create_default_context()
    resp = urllib.request.urlopen(req, timeout=30, context=ctx)
    data = resp.read().decode('utf-8')
    
    root = ET.fromstring(data)
    ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
    
    papers = []
    for entry in root.findall('atom:entry', ns):
        published = entry.find('atom:published', ns).text[:10]
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)[:3]]
        abstract = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')[:500]
        aid = entry.find('atom:id', ns).text.split('/')[-1]
        cats = [c.get('term') for c in entry.findall('atom:category', ns)]
        papers.append({'id': aid, 'title': title, 'authors': ', '.join(authors), 
                       'abstract': abstract, 'published': published, 'cats': cats})
    return papers
```

## Rate Limiting

- **Minimum sleep: 10 seconds** between requests. The skill previously said 3s — this is wrong.
- If you get "Rate exceeded." — wait 10-15s and retry.
- The `sleep 10` between multi-query searches is mandatory, not optional.

## Tool Fallbacks

| Tool | Works? | Notes |
|------|--------|-------|
| `urllib.request` with headers | ✅ | Most reliable for API queries |
| `curl` with proxy | ⚠️ | Rate-limited aggressively, returns "Rate exceeded." |
| `httpx` | ⚠️ | Often hangs on arxiv API |
| `web_search` | ❌ | Fails with NoneType errors on neuroscience queries |
| `web_extract` | ❌ | Blocks arxiv.org as "private/internal network" |
| `browser_navigate` + `browser_snapshot` | ✅ | **Best for reading paper content** |
| `browser_navigate` to PDF | ✅ | Can read full paper content |

## Multi-Query Pattern

When searching multiple topics, use this pattern to avoid rate limits:

```python
import time

# Query 1
papers1 = search_arxiv('neural dynamics', max_results=5)
print('=== NEURAL DYNAMICS ===')
for p in papers1[:3]:
    print(f"[{p['id']}] {p['title'][:100]}")

time.sleep(12)  # MANDATORY gap between queries

# Query 2
papers2 = search_arxiv('spiking neural network', max_results=3)
print('=== SNN PAPERS ===')
for p in papers2[:3]:
    print(f"[{p['id']}] {p['title'][:100]}")
```

## Reading Full Paper Content

When you need more than the abstract:

```python
# DO NOT use web_extract — it blocks arxiv URLs
# Use browser instead:
browser_navigate(url="https://arxiv.org/abs/2604.11178")
snapshot = browser_snapshot()
# The snapshot contains the full abstract and metadata
```

For PDF content, navigate to the PDF URL:
```python
browser_navigate(url="https://arxiv.org/pdf/2604.11178")
```

## Category Notes

For neuroscience papers, the most productive categories are:
- `q-bio.NC` — Neurons and Cognition
- `cs.NE` — Neural and Evolutionary Computing
- `cs.LG` — Machine Learning (many computational neuroscience papers)
- `cs.AI` — Artificial Intelligence (for SNN papers)

The OR-pattern query works better than single-category searches:
`all:"spiking neural" AND (cat:q-bio.NC OR cat:cs.NE OR cat:cs.LG)`
