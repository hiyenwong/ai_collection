# arXiv API Working Pattern (Verified 2026-05-18)

## Critical: httpx/python FAILS

Every attempt to use httpx or python requests against the arXiv API results in:
- Connection timeouts (even with proxy)
- Immediate 429 "Rate exceeded" (even with 10s+ delays between requests)

**This is consistent across all attempts in this session.**

## Only curl works

```bash
# Direct curl — NO proxy, https://, 15-20s delay between requests
curl -s "https://export.arxiv.org/api/query?search_query=all:spiking+neural+network&max_results=10&sortBy=submittedDate&sortOrder=descending" --connect-timeout 15 --max-time 30 -o /tmp/arxiv.xml
```

## Rate limit reality

- arXiv returns "Rate exceeded." on most requests even with 10s delays
- **Minimum 15-20s between requests** to avoid 429
- Proxy (`127.0.0.1:7890`) does NOT bypass rate limits and adds timeout risk
- Category searches (`cat:cs.NE`, `cat:q-bio.NC`) get rate-limited faster than keyword searches

## Retry pattern

```bash
sleep 20 && curl -s "https://export.arxiv.org/api/query?..." -o /tmp/arxiv.xml
```

## Parsing (save to file first)

Security guardrail blocks `curl ... | python3`. Always:
```bash
curl -s "https://..." -o /tmp/arxiv.xml
python3 parse.py /tmp/arxiv.xml
```

Parse with:
```python
import xml.etree.ElementTree as ET
ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
root = ET.parse('/tmp/arxiv.xml').getroot()
for entry in root.findall('atom:entry', ns):
    paper_id = entry.find('atom:id', ns).text.split('/')[-1]
    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
    # ... etc
```

## Multi-query session pattern

When searching multiple topics, space them out:
```bash
# Query 1: SNN papers
curl -s "https://export.arxiv.org/api/query?search_query=all:%22spiking+neural+network%22&max_results=10&sortBy=submittedDate" -o /tmp/q1.xml
sleep 20
# Query 2: Brain network papers
curl -s "https://export.arxiv.org/api/query?search_query=all:%22brain+network%22&max_results=10&sortBy=submittedDate" -o /tmp/q2.xml
sleep 20
# Query 3: q-bio.NC category
curl -s "https://export.arxiv.org/api/query?search_query=cat:q-bio.NC&max_results=10&sortBy=submittedDate" -o /tmp/q3.xml
```
