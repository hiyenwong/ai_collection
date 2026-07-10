# Europe PMC API Fallback

**Verified 2026-06-03**: Works when arXiv (429), Semantic Scholar (429), AND web_search (Firecrawl NoneType) all fail simultaneously.

## Working Pattern

```python
import urllib.request, json, ssl

ctx = ssl.create_default_context()
url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=quantum+machine+learning+medical+diagnosis&format=json&resultType=core&pageSize=5&sort_date=y'
req = urllib.request.Request(url, headers={'User-Agent': 'ResearchBot/1.0'})
resp = urllib.request.urlopen(req, timeout=30, context=ctx)
data = json.loads(resp.read().decode())
results = data.get('resultList', {}).get('result', [])
for r in results[:5]:
    title = r.get('title', '')
    abstract = (r.get('abstractText', '') or '')[:1000]
    doi = r.get('doi', '')
    pmid = r.get('pmid', '')
    pub_year = r.get('pubYear', '')
    source = r.get('source', '')  # MED, PPR
    print(f"Title: {title}")
    print(f"DOI: {doi}, PMID: {pmid}, Source: {source}, Year: {pub_year}")
    print(f"Abstract: {abstract[:200]}")
    print("---")
```

## Key Fields

| Field | Description |
|-------|-------------|
| `title` | Paper title |
| `abstractText` | Full abstract (may contain HTML tags like `<h4>`) |
| `doi` | DOI identifier |
| `pmid` | PubMed ID (for MED sources) |
| `pubYear` | Publication year |
| `source` | Source type: MED (PubMed-indexed), PPR (preprint), etc. |

## Advantages

- **No aggressive rate limiting** — unlike arXiv (429) and Semantic Scholar (429)
- **Rich metadata** — DOI, PMID, source, abstract all in one call
- **Medical/biomedical focus** — covers Nature, Science, Cell, and medical journals
- **Works without proxy** — direct HTTPS access
- **Preprint support** — includes PPR (preprint server) results

## Limitations

- Primarily biomedical/medical — not for pure CS/quantum/physics papers
- Abstracts may contain HTML tags requiring cleanup
- Fewer preprints than arXiv

## Query Examples

- `quantum+machine+learning+medical+diagnosis`
- `quantum+support+vector+machine+biomarker`
- `neural+network+brain+imaging`
- `deep+learning+cancer+imaging`
