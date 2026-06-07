# RSS Feed — Verified Working Pattern (2026-05-19)

## Zero-Proxy RSS Fetching

RSS feeds at `https://rss.arxiv.org/rss/` work **without any proxy** when using `urllib.request`:

```python
import urllib.request, ssl

def fetch_rss(categories):
    url = f'https://rss.arxiv.org/rss/{"+".join(categories)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()) as resp:
        return resp.read().decode('utf-8')

# Fetch 6 categories at once — no proxy, no rate limits
rss = fetch_rss(['cs.AI', 'cs.LG', 'cs.NE', 'cs.SE', 'cs.DS', 'quant-ph'])
```

## Why This Works

- RSS endpoint uses different infrastructure than the API (`export.arxiv.org`)
- No rate limiting on RSS — returns 100-300 entries/category/day
- `urllib.request` with SSL context is sufficient — no proxy needed
- Combining categories with `+` fetches all in one request

## Parsing RSS XML

Standard RSS 2.0 format:
```python
import xml.etree.ElementTree as ET

root = ET.fromstring(rss_text)
items = root.findall('.//item')
for item in items:
    title = item.find('title').text
    link = item.find('link').text
    desc = item.find('description').text
    arxiv_id = link.split('/')[-1].split('v')[0]
    abstract = desc.split(arxiv_id, 1)[1].strip() if arxiv_id in desc else ''
```

## Full Abstracts via abs Page

RSS descriptions are truncated. For full abstracts:

```python
def fetch_abstract(paper_id):
    url = f'https://arxiv.org/abs/{paper_id}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode('utf-8')
    import re
    title_m = re.search(r'<h1 class="title mathjax">(.*?)</h1>', html, re.DOTALL)
    abs_m = re.search(r'<blockquote class="abstract mathjax">(.*?)</blockquote>', html, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip().replace('Title:', '').strip() if title_m else ''
    abstract = re.sub(r'<[^>]+>', '', abs_m.group(1)).replace('\n', ' ').strip().replace('Abstract:', '').strip() if abs_m else ''
```

## Pitfall: Title/Abstract Prefix

arXiv HTML pages include "Title:" and "Abstract:" as literal text in the matched elements. Always strip these prefixes after tag removal.

## Throughput

Fetching 6 categories via RSS: ~3s total. 14 individual abstracts: ~30s (2s each). Total pipeline: under 1 minute for 65+ papers.
