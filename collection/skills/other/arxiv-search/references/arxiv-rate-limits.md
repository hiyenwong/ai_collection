# arXiv API Rate Limiting Notes

## Observed Behavior (2026-05-13)

### Rate Limit Response
- **Not HTTP 429**: Returns HTTP 200 with plain text body "Rate exceeded."
- **No Retry-After header**: Must implement client-side backoff

### Working Delays
| Scenario | Minimum Delay | Notes |
|----------|--------------|-------|
| Single query | 3 seconds | Works most of the time |
| Multiple queries in sequence | 5-10 seconds | Required for batch searches |
| After rate limit hit | 10+ seconds | Reset takes time |

### Reliable Search Pattern
```python
import httpx
import time

ARXIV_API = 'https://export.arxiv.org/api/query'

def search_arxiv_safe(query, max_results=5):
    """Search with proper rate limit handling."""
    for attempt in range(3):
        time.sleep(5)  # Always wait before request
        resp = httpx.get(
            ARXIV_API,
            params={
                'search_query': query,
                'max_results': max_results,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            },
            timeout=30
        )
        
        # Check for rate limit (plain text response)
        if 'Rate exceeded' in resp.text:
            wait_time = 10 * (attempt + 1)
            time.sleep(wait_time)
            continue
            
        return resp.text
    
    raise Exception("Rate limit exceeded after retries")

# Example: Multiple queries
queries = [
    'all:quantum AND all:medical',
    'all:quantum AND all:drug',
    'all:quantum AND all:clinical'
]

for q in queries:
    result = search_arxiv_safe(q)
    time.sleep(5)  # Wait between queries
```

### Alternative Search Fields
If `all:` field search is too broad:
- `ti:` - Title only (more specific, fewer results)
- `au:` - Author search
- `ab:` - Abstract search
- `cat:` - Category filter (e.g., `cat:quant-ph`)

### Category Shortcuts for Medical + Quantum
- `cat:quant-ph` - Quantum physics
- `cat:cs.LG` - Machine learning (includes quantum ML)
- `cat:eess.IV` - Image and video processing (medical imaging)
- `cat:cs.AI` - Artificial intelligence
