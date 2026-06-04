# arXiv Search & Paper Processing — Session Notes (2026-05-16)

## Working arXiv API Patterns

### What Failed
- **httpx** (with or without proxy): Consistently gets 429 rate limits and timeouts on arXiv API
- **web_extract**: Blocks arxiv.org URLs as "private/internal network"
- **Complex queries** with `AND`/`OR` operators: More likely to trigger rate limits

### What Works
1. **urllib.request + proxy**: Most reliable for direct API calls
2. **web_search**: No rate limits, returns arXiv paper metadata in search results
3. **curl to file**: Must save to file first, never pipe to python (security guardrail)

### Rate Limit Reality
- Minimum 5 second sleep between queries (3 seconds is NOT enough)
- Category-only queries (`cat:q-bio.NC`) return 15-20 papers reliably
- Complex queries are more fragile
- On 429: wait 10 seconds before retry

### PDF Download + Text Extraction
```python
import urllib.request
import subprocess

# Download via proxy
proxy = "http://127.0.0.1:7890"
proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

pdf_url = "https://arxiv.org/pdf/2605.14867.pdf"
req = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=60) as resp:
    with open('/tmp/paper.pdf', 'wb') as f:
        f.write(resp.read())

# Extract text
subprocess.run(['pdftotext', '/tmp/paper.pdf', '/tmp/paper.txt'])
```

### Effective Multi-Query Strategy
For comprehensive coverage, run 2-3 category sweeps:
1. `cat:q-bio.NC` (computational neuroscience)
2. `cat:cs.NE` (neural and evolutionary computing)  
3. `all:"spiking neural"` (keyword for specific subfield)

Deduplicate by arXiv ID across results.

## kg.db Import Pitfall: URL Version Suffixes

arXiv URLs come in two forms: `2605.11835` vs `2605.11835v1`.
The `url` column in `kg_entities` has a UNIQUE constraint.

**Symptom**: `sqlite3.IntegrityError: UNIQUE constraint failed: kg_entities.url`

**Fix**: Dedup by checking `url LIKE '%{arxiv_base}%'` before insert, not just title match.
