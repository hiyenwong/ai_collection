# arXiv API Patterns (research-api-fallback-strategy reference)

When Firecrawl/web_search fail, the arXiv export API is always accessible via plain HTTP (port 80).

## Search

```python
import urllib.request, urllib.parse, ssl, time
ssl._create_default_https_context = lambda: ssl._create_unverified_context()

# Combine queries with AND — use urllib.parse.quote (mandatory!)
search_query = 'all:"quantum computing" AND all:"number theory"'
encoded = urllib.parse.quote(search_query)
url = f'http://export.arxiv.org/api/query?search_query={encoded}&sortBy=submittedDate&sortOrder=descending&max_results=5'

req = urllib.request.Request(url, headers={'User-Agent': 'ResearchBot/1.0'})
response = urllib.request.urlopen(req, timeout=20)
data = response.read().decode('utf-8')

# Parse entries
entries = data.split('<entry>')[1:]
for entry in entries:
    title = entry.split('<title>')[1].split('</title>')[0].strip().replace('\n', ' ')
    arxiv_id = entry.split('<id>')[1].split('</id>')[0].strip().split('/')[-1]
    published = entry.split('<published>')[1].split('</published>')[0].strip()[:10]
    summary = entry.split('<summary>')[1].split('</summary>')[0].strip().replace('\n', ' ')
    authors = []
    for a in entry.split('<author>'):
        if '<name>' in a:
            authors.append(a.split('<name>')[1].split('</name>')[0].strip())
```

## Fetch Abstract by ID

```python
paper_id = '2606.05217'
url = f'http://export.arxiv.org/api/query?id_list={paper_id}'
```

## Pitfalls
- **URL encoding**: `urllib.parse.quote()` is mandatory — spaces cause "URL can't contain control characters" errors
- **Rate limit**: sleep 3 seconds between requests
- **ID format**: arxiv API returns full URL in `<id>` tag, split on '/' to get short ID
