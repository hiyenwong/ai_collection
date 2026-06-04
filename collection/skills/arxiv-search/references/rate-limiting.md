# arXiv API Troubleshooting

## Rate Limiting

The arXiv API returns **429 (Too Many Requests)** or **503 (Service Unavailable)** aggressively.

### Mitigation Pattern

```python
import urllib.request
import time

def arxiv_search_safe(url, max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearchBot/1.0'})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                delay = base_delay * (2 ** attempt)  # Exponential backoff
                print(f"Rate limited ({e.code}), retrying in {delay}s...")
                time.sleep(delay)
            else:
                raise
    raise Exception("Max retries exceeded")
```

### Proxy Configuration (macOS)

When behind a local proxy (e.g., Clash/Shadowsocks on 127.0.0.1:7890):

```python
proxy = urllib.request.ProxyHandler({
    'https': 'http://127.0.0.1:7890',
    'http': 'http://127.0.0.1:7890'
})
opener = urllib.request.build_opener(proxy)
with opener.open(req, timeout=60) as resp:
    data = resp.read().decode('utf-8')
```

### Key Constraints

- Max ~3 requests per 30 seconds to `export.arxiv.org`
- Use `sortBy=submittedDate` + `max_results=10` for recent papers
- Always set a `User-Agent` header
- Parse XML with `xml.etree.ElementTree`, namespace: `atom`, `arxiv`
