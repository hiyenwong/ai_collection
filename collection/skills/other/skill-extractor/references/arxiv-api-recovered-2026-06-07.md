# arXiv API Recovery Note (2026-06-07)

## Status: RECOVERED

The arXiv API previously returned persistent HTTP 429 across all cron sessions (first noted 2026-06-01). As of 2026-06-07, the API works normally again.

## Verified Working Pattern
```python
import urllib.request, urllib.parse

proxy = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
})
opener = urllib.request.build_opener(proxy)
url = 'http://export.arxiv.org/api/query?' + urllib.parse.urlencode(params)
response = opener.open(url, timeout=30)
xml_data = response.read().decode('utf-8')
```

- 4 queries executed with zero errors
- No 429 responses observed
- No User-Agent header required

## Crossref Remains Useful Fallback

Crossref API (`https://api.crossref.org/works?query=...`) is still valuable for:
- Papers with DOIs but no arXiv preprint
- BioRxiv and other preprint server articles
- Applied/experimental papers

When both APIs work, prefer arXiv (XML format) for cron jobs since it provides more structured paper metadata.
