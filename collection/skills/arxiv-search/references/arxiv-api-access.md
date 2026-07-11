# arXiv API Access Patterns

## Working Methods

### Direct urllib (recommended)
```python
import urllib.request
url = "https://export.arxiv.org/api/query?search_query=cat:q-bio.NC&sortBy=submittedDate&sortOrder=descending&start=0&max_results=30"
with urllib.request.urlopen(url, timeout=30) as resp:
    data = resp.read().decode("utf-8")
```
- Works without proxy
- Direct HTTPS connection

### curl via terminal
```bash
curl -s "https://export.arxiv.org/api/query?search_query=..."
```
- Also works directly
- Use with proxy if needed: `curl --proxy http://127.0.0.1:7890 https://...`

## Known Failures

### Proxy with HTTP protocol → "Misdirected Request"
Using `req.set_proxy("127.0.0.1:7890", "https")` with `urllib` causes HTTP 421 errors.
**Fix**: Skip proxy entirely for arXiv API — direct connection works.

### web_extract blocked
The `web_extract` tool may block arXiv URLs as "private or internal network address".
**Fix**: Use `urllib` or `curl` instead.

## XML Parsing
arXiv returns Atom XML. Required namespaces:
```python
ns = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom"
}
# Note: These are HTTP URLs in the XML schema, not actual HTTP requests
```

## Query Categories
- `cat:q-bio.NC` — Computational Neuroscience (most relevant)
- `cat:q-bio` — All Quantitative Biology
- `cat:cs.NE` — Neural and Evolutionary Computing
- `cat:cs.AI` — Artificial Intelligence
