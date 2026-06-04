# Verified arXiv Search Patterns (Updated 2026-05-20)

## Working API Endpoint

```
https://export.arxiv.org/api/query
```

**CRITICAL**: Must use HTTPS. HTTP returns 301 with empty body → XML parse error.

## Verified Working Query Patterns

### By Category (most reliable)
```python
params = {
    "search_query": "cat:q-bio.NC",  # or cat:cs.NE, cat:cs.LG
    "max_results": 10,
    "sortBy": "submittedDate",
    "sortOrder": "descending"
}
response = httpx.get("https://export.arxiv.org/api/query", params=params, follow_redirects=True)
```

### By Keyword
```python
params = {
    "search_query": 'all:"spiking neural"',  # quotes for phrase match
    "max_results": 10,
    "sortBy": "submittedDate",
    "sortOrder": "descending"
}
```

### Batch by IDs
```python
# Use bare IDs without version suffixes
arxiv_ids = "2605.18251,2605.16114,2605.18557"
url = f"https://export.arxiv.org/api/query?id_list={arxiv_ids}"
```

## Rate Limiting
- Space requests 3-4+ seconds apart
- If 429 received, wait longer (10+ seconds)
- Alternative: use `web_search` with `site:arxiv.org` to bypass API

## XML Parsing
```python
import xml.etree.ElementTree as ET

ns = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom"
}
root = ET.fromstring(response.text)
# entry = root.find("atom:entry", ns)
```
