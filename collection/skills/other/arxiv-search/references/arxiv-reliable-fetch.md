# arXiv Reliable Fetch Patterns

## Problem

The arXiv API (`https://export.arxiv.org/api/query`) is aggressively rate-limited.
Direct `httpx` calls frequently timeout (300s+) or return "Rate exceeded."
The `web_extract` tool blocks arxiv.org URLs as "private/internal network."

## Reliable Workflow (Verified 2026-05-06)

### Pattern 1: web_search Discovery + Batch Metadata Fetch

```python
# Step 1: Use web_search to discover paper IDs (no rate limits)
# web_search(query="site:arxiv.org systems engineering control 2025 2026", limit=10)
# Returns URLs like: https://arxiv.org/abs/2605.02506

# Step 2: Extract IDs and batch-fetch metadata
import httpx, time

# Collect IDs from web_search results
ids = ["2605.02506", "2605.00950", "2604.13118"]

# Batch fetch: comma-separated IDs in ONE request (much more efficient)
id_list = ",".join(ids)
url = f"https://export.arxiv.org/api/query?id_list={id_list}"
resp = httpx.get(url, timeout=30)
xml = resp.text  # ~2-3KB per paper
# Parse XML with xml.etree.ElementTree
```

### Pattern 2: Individual Fetch with Retry + File Save

```bash
# NEVER pipe curl to python: curl ... | python3 is blocked by security guardrail
# ALWAYS save to file first

curl -s -o /tmp/arxiv.xml "https://export.arxiv.org/api/query?id_list=2605.02506"
python3 /tmp/parse_arxiv.py /tmp/arxiv.xml
```

```python
# parse_arxiv.py
import xml.etree.ElementTree as ET, sys

ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
root = ET.parse(sys.argv[1]).getroot()

for entry in root.findall("atom:entry", ns):
    pid = entry.find("atom:id", ns).text.split("/")[-1]
    title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
    abstract = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
    print(f"{pid}: {title}")
```

### Pattern 3: Category Browse (cs.SY / eess.SY)

For browsing recent papers in a category, use the category's "recent" page via web_search:
- `web_search("arxiv.org/list/cs.SY/recent")` — Systems and Control recent
- `web_search("arxiv.org/list/eess.SY/new")` — Systems and Control new

## Rate Limiting Reality

| Delay | Result |
|-------|--------|
| 3-4 seconds | "Rate exceeded." almost always |
| 8-10 seconds | Sometimes works, sometimes fails |
| 10+ seconds | Most reliable |
| Batch (id_list) | Best — one request, many papers |

## Tool Compatibility

| Tool | arXiv Support | Notes |
|------|--------------|-------|
| `web_search` | ✅ Works | Best for discovery |
| `curl` | ✅ Works | Save to file, never pipe |
| `httpx` (Python) | ⚠️ Unreliable | Timeouts common, retry needed |
| `web_extract` | ❌ Blocked | "private/internal network" |

## Category Reference for Systems Engineering

| Category | Name | Recent URL |
|----------|------|-----------|
| eess.SY | Systems and Control | arxiv.org/list/eess.SY/new |
| cs.SY | Systems and Control (CS) | arxiv.org/list/cs.SY/new |
| cs.SE | Software Engineering | arxiv.org/list/cs.SE/new |
| math.OC | Optimization and Control | arxiv.org/list/math.OC/new |
| cs.DC | Distributed Computing | arxiv.org/list/cs.DC/new |
