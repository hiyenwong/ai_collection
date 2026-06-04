# Reliable arXiv Search & Extraction Pattern

Verified 2026-05-17. These patterns work consistently for arXiv access in the Hermes agent environment.

## Tool Fallback Chain

1. **arxiv-search skill** (preferred for discovery)
2. **urllib.request** (Python stdlib, reliable for API queries)
3. **browser_navigate + browser_console** (for reading full paper HTML content)

## What Does NOT Work

- **httpx / async requests** → 429 rate limit immediately, even with exponential backoff retries. 300s+ timeout with retry loops.
- **web_extract on arxiv.org URLs** → Blocked as "private/internal network address"
- **Parallel/multi-query in single script** → Rate limits triggered by concurrent requests

## Reliable Search Pattern (urllib.request)

```python
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time

ARXIV_API = "https://export.arxiv.org/api/query"  # ALWAYS https://

def search_arxiv(query, max_results=10):
    """Search arXiv - reliable, rate-limit safe."""
    encoded = urllib.parse.quote(query)
    url = f"{ARXIV_API}?search_query={encoded}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research agent)"})
    response = urllib.request.urlopen(req, timeout=30)
    return response.read().decode("utf-8")

def parse_xml(xml_text, days=None):
    """Parse arXiv API XML response."""
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    papers = []
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=days) if days else None

    for entry in root.findall("atom:entry", ns):
        published = entry.find("atom:published", ns).text
        pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
        if cutoff and pub_date < cutoff.replace(tzinfo=pub_date.tzinfo):
            continue

        paper_id = entry.find("atom:id", ns).text.split("/")[-1]
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
        cats = [c.get("term") for c in entry.findall("atom:category", ns)]

        pdf = f"https://arxiv.org/pdf/{paper_id}"

        papers.append({
            "id": paper_id,
            "title": entry.find("atom:title", ns).text.strip().replace("\n", " "),
            "authors": authors[:6] + (["et al."] if len(authors) > 6 else []),
            "abstract": entry.find("atom:summary", ns).text.strip().replace("\n", " "),
            "published": pub_date.strftime("%Y-%m-%d"),
            "pdf_url": pdf,
            "abs_url": f"https://arxiv.org/abs/{paper_id}",
            "categories": cats
        })
    return papers
```

## Multiple Queries Pattern

Run queries **sequentially** with 3.5s delay between each:

```python
queries = ["cat:q-bio.NC", "cat:cs.NE", "all:spiking+neural+AND+cat:cs.LG"]
all_papers = []
seen = set()

for q in queries:
    xml = search_arxiv(q, 10)
    papers = parse_xml(xml, days=3)
    for p in papers:
        if p["id"] not in seen:
            seen.add(p["id"])
            all_papers.append(p)
    time.sleep(3.5)  # REQUIRED: arXiv rate limit
```

## Reading Paper Content (Fallback Chain)

When you need the full paper text:

1. Try: `browser_navigate("https://arxiv.org/html/{id}")` then `browser_console` to extract article text
2. Fallback: `browser_navigate("https://arxiv.org/abs/{id}")` for abstract + metadata
3. Fallback: curl with proxy for XML metadata

```python
# browser_navigate + browser_console extraction
# After navigating to https://arxiv.org/html/{id}
const article = document.querySelector('article');
const elements = article.querySelectorAll('p, h1, h2, h3, h4, h5, h6, li');
let text = '';
elements.forEach(el => { text += el.innerText + '\n\n'; });
text;  // Returns full paper content
```

## Rate Limit Rules

- **Single query**: Works reliably with urllib.request
- **Multiple queries**: MUST use sequential execution with 3.5s+ delay
- **httpx/async**: NOT reliable — avoid for arXiv API
- **web_search**: No rate limits — good for discovery when API is throttled
