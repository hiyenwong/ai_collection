# arXiv API Working Patterns for execute_code

## Python/httpx Pattern (Execute Code)

When running arXiv searches from `execute_code` (not the CLI), use this pattern:

```python
import httpx
import xml.etree.ElementTree as ET

ARXIV_API = "https://export.arxiv.org/api/query"  # MUST be https://

def search_arxiv(query, max_results=10):
    params = {
        "search_query": query,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    response = httpx.get(ARXIV_API, params=params, timeout=30, follow_redirects=True)
    response.raise_for_status()
    return parse_response(response.text)

def parse_response(xml_text):
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall("atom:entry", ns):
        papers.append({
            "id": entry.find("atom:id", ns).text.split("/")[-1],
            "title": entry.find("atom:title", ns).text.strip().replace("\n", " "),
            "authors": [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)],
            "abstract": entry.find("atom:summary", ns).text.strip().replace("\n", " "),
            "published": entry.find("atom:published", ns).text[:10],
            "pdf_url": f"https://arxiv.org/pdf/{entry.find('atom:id', ns).text.split('/')[-1]}",
        })
    return papers
```

### Multi-Category Search Pattern

For comprehensive coverage, search multiple queries sequentially:

```python
queries = [
    ('cat:q-bio.NC', 15),       # Neuroscience
    ('cat:cs.NE', 15),           # Neural/Evolutionary Computing
]
```

### Critical Gotchas

1. **Always use `https://`** — `http://` returns 301 and fails without follow_redirects
2. **Always set `follow_redirects=True`** in httpx even with https:// (belt-and-suspenders)
3. **Parse XML namespaces** — arXiv uses `atom:` namespace, bare `find()` returns None
4. **Date filtering is client-side** — arXiv API doesn't support date range natively
