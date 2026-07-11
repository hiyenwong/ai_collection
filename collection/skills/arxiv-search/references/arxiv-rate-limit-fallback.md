# arXiv API Rate Limiting & RSS Fallback

## Problem
arXiv API enforces strict rate limits. Both the XML API (`/api/query`) and `web_extract` against arXiv URLs can return 429 or "Rate exceeded" even with delays.

## Recommended Discovery Order for Cron Jobs

### 1. RSS Feed (fastest, zero rate limit)
```bash
curl -s --max-time 15 "https://rss.arxiv.org/rss/quant-ph"
```

Category feeds: `quant-ph`, `cs.AI`, `cs.LG`, `cs.CV`, `q-bio.NC`, `cs.NE`, `cond-mat.mes-hall`.
Multiple: `https://rss.arxiv.org/rss/quant-ph+cs.AI`

RSS fields: `title`, `link` (arxiv.org/abs/ID), `description` (contains abstract), `dc:creator` (authors), `category`, `pubDate`.

### 2. API with retry (when RSS is insufficient)
- Sleep 3-5s between requests
- On 429: sleep 15-30s, retry once
- After 3+ failures: fall back to RSS

### 3. Browser navigation (last resort)
Use `browser_navigate` + `browser_snapshot` on `https://arxiv.org/list/{category}/recent`.

## Parse Example (Python)
```python
import xml.etree.ElementTree as ET

ns = {"dc": "http://purl.org/dc/elements/1.1/"}
root = ET.fromstring(rss_xml)
for item in root.findall(".//item"):
    title = item.find("title").text
    link = item.find("link").text
    desc = item.find("description").text
    authors = item.find("dc:creator", ns).text if item.find("dc:creator", ns) else ""
```
