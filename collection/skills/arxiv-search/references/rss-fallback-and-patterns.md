# arXiv Search: Working Code Patterns and RSS Parsers

## RSS Feed Parser (Working)

```python
import requests
from bs4 import BeautifulSoup

# RSS feed - works even when API is rate-limited
url = 'https://rss.arxiv.org/rss/cs.AI,cs.NE,q-bio.NC'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
soup = BeautifulSoup(resp.text, 'html.parser')

for item in soup.find_all('item'):
    title = item.find('title').text
    link = item.find('link').text
    desc = item.find('description').text
    # Parse arxiv ID from link or title
```

## API Search with Retry (Working)

```python
import requests
import time

url = 'https://export.arxiv.org/api/query'
params = {
    'search_query': 'all:neuroscience',
    'sortBy': 'submittedDate',
    'sortOrder': 'descending',
    'max_results': 15
}
headers = {'User-Agent': 'ResearchBot/1.0 (contact@example.com)'}

# Retry with exponential backoff
for attempt in range(3):
    resp = requests.get(url, params=params, headers=headers, timeout=30)
    if resp.status_code == 200:
        break
    elif resp.status_code == 429:
        wait = 60 * (attempt + 1)
        print(f'Rate limited, waiting {wait}s...')
        time.sleep(wait)
    else:
        raise Exception(f'HTTP {resp.status_code}: {resp.text}')

# Parse with xml.etree.ElementTree
ns = {'atom': 'http://www.w3.org/2005/Atom'}
root = ET.fromstring(resp.text)
for entry in root.findall('atom:entry', ns):
    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
    # ... etc
```

## Key Findings

- `submittedDate:[YYYYMMDD TO YYYYMMDD]` returns HTTP 400 — NOT supported
- Semantic Scholar API: `api.semanticscholar.org/graph/v1/paper/search` — also has rate limits (429)
- OpenAlex API: `api.openalex.org/works?search={query}&sort=datePublished:desc` — works but returns all-time results, not recent-only
- arXiv RSS: `rss.arxiv.org/rss/{categories}` — no rate limits, skips weekends
- arXiv category page: `arxiv.org/list/{cat}/new` — HTML, scrapable, shows Friday's papers on weekends
- `pdftotext` works on downloaded PDFs for full-text extraction
