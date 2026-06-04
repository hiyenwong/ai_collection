# arXiv Multi-Query Search Pattern

## Problem

A single query rarely captures the full landscape of a research area. Running multiple keyword queries produces overlapping results that need deduplication and filtering.

## Pattern

```python
import httpx
import xml.etree.ElementTree as ET
import time
import json
from datetime import datetime

ARXIV_API = "https://export.arxiv.org/api/query"

def search_arxiv(query, max_results=10):
    """Search arXiv with proxy and rate-limit awareness."""
    params = {
        "search_query": query,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    # Use HTTPTransport for proxy (proxies= kwarg may fail)
    transport = httpx.HTTPTransport(proxy="http://127.0.0.1:7890")
    with httpx.Client(transport=transport, timeout=30) as client:
        resp = client.get(ARXIV_API, params=params)
        resp.raise_for_status()
    return parse_response(resp.text)

def parse_response(xml_text):
    ns = {"atom": "http://www.w3.org/2005/Atom"}
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
            "categories": [c.get("term") for c in entry.findall("atom:category", ns)]
        })
    return papers

# Multi-query with deduplication
queries = [
    "all:neuroscience",
    "all:\"brain network\"",
    "all:\"neural dynamics\"",
    "all:\"spiking neural network\"",
    "all:\"computational neuroscience\"",
    "cat:q-bio.NC",
]

all_papers = []
seen_ids = set()

for q in queries:
    try:
        papers = search_arxiv(q, max_results=10)
        for p in papers:
            if p["id"] not in seen_ids:
                seen_ids.add(p["id"])
                all_papers.append(p)
        time.sleep(3)  # Rate-limit avoidance
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            time.sleep(15)
            # Retry once with longer delay
            try:
                papers = search_arxiv(q, max_results=10)
                for p in papers:
                    if p["id"] not in seen_ids:
                        seen_ids.add(p["id"])
                        all_papers.append(p)
            except Exception:
                pass

# Save cache for future runs
with open("/tmp/arxiv_results.json", "w") as f:
    json.dump(all_papers, f, indent=2)

print(f"Found {len(all_papers)} unique papers from {len(queries)} queries")
```

## PDF Extraction

```python
import subprocess

def extract_pdf_text(pdf_path):
    """Use pdftotext (poppler) — works in sandbox where pymupdf may not."""
    txt_path = pdf_path.replace(".pdf", ".txt")
    subprocess.run(["pdftotext", pdf_path, txt_path], check=True)
    with open(txt_path) as f:
        return f.read()
```

## Screening Heuristics

After collecting papers, score and rank by:
1. **Novelty signals**: "new", "novel", "first", "we propose", "we introduce" in abstract
2. **Methodological contribution**: Introduces a new architecture, algorithm, or framework
3. **Empirical strength**: Benchmarked against strong baselines, large-scale evaluation
4. **Cross-domain relevance**: Bridges multiple fields (e.g., neuroscience + quantum computing)
5. **Practical impact**: Has clear implementation path, open-source code, or hardware relevance
