# arXiv HTML Fallback Methods

When the arXiv XML API returns HTTP 429 (rate limited), use these HTML-based alternatives.

## Method 1: Category Listing Page

Fetch the HTML listing for a category to get paper IDs, titles, and authors:

```python
import urllib.request
from html.parser import HTMLParser

url = "https://arxiv.org/list/quant-ph/new"  # replace category as needed
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})
```

Parse the HTML listing — structure uses `<dt>` for paper IDs and `<dd>` for metadata:
- Paper ID: `<a href="/abs/XXXX.XXXXX">` inside `<dt>`
- Title: `<div class="list-title">` inside `<dd>`
- Authors: `<div class="authors">` inside `<dd>`
- Abstract: `<blockquote class="abstract">` or `<p class="abstract">`

This returns ~220 papers per listing page with IDs and titles (abstracts may require individual page fetches).

## Method 2: Individual Paper Abstract Pages

Fetch individual paper details from the abstract page:

```python
import re

url = f"https://arxiv.org/abs/{paper_id}"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# Extract metadata from meta tags
title = re.search(r'<meta name="citation_title" content="([^"]+)"', html).group(1)
authors = re.findall(r'<meta name="citation_author" content="([^"]+)"', html)
abstract_match = re.search(r'<blockquote class="abstract[^"]*">\s*(.*?)\s*</blockquote>', html, re.DOTALL)
if abstract_match:
    abstract = re.sub(r'<[^>]+>', '', abstract_match.group(1)).strip()
    abstract = abstract.replace('Abstract:', '').strip()
```

## Method 3: ar5iv Full-Text HTML

For full paper content (including extended abstracts, sections):

```python
url = f"https://ar5iv.labs.arxiv.org/html/{paper_id}"
```

This renders the full paper as HTML. Extract the title from `<title>` tag and abstract from `<blockquote class="abstract">`.

## Method 4: Semantic Scholar API (Alternative)

```python
import urllib.request, json

url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={topic}&limit=5&fields=title,authors,abstract,year,externalIds,url,publicationDate"
```

Note: Semantic Scholar also has rate limits (~100 requests/5 min without API key). Use the `externalIds.ArXiv` field to get the arXiv ID.

## Rate Limit Notes

- arXiv XML API: ~3 second interval recommended, but can still return 429 from shared IPs
- HTML pages are more tolerant than the API endpoint
- Adding a proper `User-Agent` header helps avoid immediate blocking
- For cron jobs doing bulk searches, prefer HTML listing over individual API calls
