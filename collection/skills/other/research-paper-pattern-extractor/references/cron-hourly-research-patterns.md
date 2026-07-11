# Cron Hourly Research Job - Verified Patterns

## Session: 2026-06-26 Round 8 (Friday: Number Theory + Quantum)

### Working arXiv Search Pattern (No Shell Pipes)

```python
import urllib.request, urllib.parse, ssl, xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({'https': 'http://127.0.0.1:7890'}),
    urllib.request.HTTPSHandler(context=ctx)
)

def search_arxiv(query_str, max_results=5):
    encoded = urllib.parse.quote(query_str)
    url = f"https://export.arxiv.org/api/query?search_query={encoded}&max_results={max_results}"
    response = opener.open(urllib.request.Request(url), timeout=20)
    data = response.read().decode('utf-8')
    root = ET.fromstring(data)
    ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
    results = []
    for entry in root.findall('atom:entry', ns):
        id_text = entry.find('atom:id', ns).text
        arxiv_id = id_text.split('/abs/')[-1].split('v')[0]
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')[:500]
        published = entry.find('atom:published', ns).text
        cats = [c.get('term') for c in entry.findall('atom:category', ns)]
        results.append({'arxiv_id': arxiv_id, 'title': title, 'summary': summary,
                        'published': published, 'categories': cats})
    return results
```

### kg.db Import Schema

| Table | Key Columns | Notes |
|-------|------------|-------|
| `arxiv_papers` | id (TEXT), title, authors, published, categories, summary, pdf_url, abs_url | id is arxiv ID string |
| `papers` | arxiv_id (TEXT), title, authors, published_date, categories, abstract, created_at | |
| `kg_entities` | id (INTEGER PK), title (TEXT NOT NULL), url, content, authors, published_date, category, source | source can be 'arxiv' or 'arxiv-cron' |
| `kg_vectors` | id (INTEGER PK), entity_id (INTEGER FK), vector_data (BLOB), created_at | 128-float32 packed |

### Verification Checklist
1. arxiv_search_today.py exists and compiles
2. import_today_papers.py exists and compiles
3. 6+ target papers in arxiv_papers
4. kg_entities has entries for key papers (check both 'arxiv' and 'arxiv-cron' sources)
5. kg_vectors has entries for new entities
6. SKILL.md files exist with frontmatter (name, trigger_words, >500 chars)
7. ai_collection sync matches workspace
8. INDEX.md updated
9. Git committed and pushed
