# ArXiv API Direct Access (Python)

When both web_search and web_extract fail on arxiv.org (Firecrawl errors, URL blocking to private/internal network), fall back to the arxiv API directly via Python.

## Pattern

```python
import urllib.request, xml.etree.ElementTree as ET

url = "https://export.arxiv.org/api/query?search_query=all:%22{query}%22&sortBy=submittedDate&sortOrder=descending&max_results=10"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=30) as resp:
    data = resp.read().decode('utf-8')

root = ET.fromstring(data)
ns = {'atom': 'http://www.w3.org/2005/Atom'}
for entry in root.findall('atom:entry', ns):
    title = entry.find('atom:title', ns).text.strip()
    published = entry.find('atom:published', ns).text
    arxiv_id = entry.find('atom:id', ns).text
    summary = entry.find('atom:summary', ns).text.strip()[:300]
```

## Key Points
- Uses `https://export.arxiv.org/api/query` (HTTPS required)
- Set `User-Agent` header to avoid blocks
- Parse Atom XML with ElementTree
- Works inside execute_code sandbox (no curl, no network proxy issues)
- Max 300 chars for summary — sufficient for initial paper triage
