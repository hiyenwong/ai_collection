# Proven Search and Import Patterns (2026-05)

## arXiv Search via Python httpx with Proxy

```python
import httpx, time, json
from xml.etree import ElementTree as ET

NS = {'atom': 'http://www.w3.org/2005/Atom'}
queries = [
    ('all:"quantum neuroscience" OR all:"quantum brain"', 'quantum_neuro'),
    ('cat:quant-ph AND all:"neural network"', 'quantum_neural'),
    ('all:"quantum" AND all:"cognition"', 'quantum_cognition'),
]

proxy = httpx.Proxy('http://127.0.0.1:7890')
all_papers = []
seen = set()

with httpx.Client(proxy=proxy, timeout=30, follow_redirects=True) as client:
    for query, tag in queries:
        time.sleep(3)  # arXiv allows ~3 queries per 10 seconds
        url = f'https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results=5'
        try:
            resp = client.get(url, headers={'User-Agent': 'ResearchBot/1.0'})
            if resp.status_code == 429:
                time.sleep(10)
                resp = client.get(url, headers={'User-Agent': 'ResearchBot/1.0'})
            if resp.status_code != 200:
                continue
            root = ET.fromstring(resp.text)
            for entry in root.findall('atom:entry', NS):
                aid = entry.find('atom:id', NS).text.split('/')[-1]
                if aid in seen:
                    continue
                seen.add(aid)
                title = entry.find('atom:title', NS).text.strip().replace('\n', ' ')
                abstract = entry.find('atom:summary', NS).text.strip().replace('\n', ' ')
                published = entry.find('atom:published', NS).text[:10]
                authors = [a.find('atom:name', NS).text for a in entry.findall('atom:author', NS)]
                cats = [c.get('term') for c in entry.findall('atom:category', NS)]
                all_papers.append({
                    'id': aid, 'title': title, 'abstract': abstract,
                    'authors': authors, 'published': published, 'categories': cats,
                    'abs_url': f'https://arxiv.org/abs/{aid}'
                })
        except Exception as e:
            pass  # Continue with other queries

print(f'Found {len(all_papers)} papers')
```

**Critical**: Always include `User-Agent` header. Use 3-second delay between queries. Handle 429 with 10s retry. Continue on failure — partial results are valuable.

## Knowledge Graph Import (kg.db)

```python
import sqlite3, json

papers = [...]  # list of paper dicts from arXiv search
conn = sqlite3.connect('kg.db')
conn.execute('PRAGMA journal_mode=WAL')
cursor = conn.cursor()

for p in papers:
    url = p.get('abs_url', f'https://arxiv.org/abs/{p["id"]}')
    cursor.execute('SELECT id FROM kg_entities WHERE url=?', (url,))
    if cursor.fetchone():
        continue  # Already exists
    cursor.execute(
        'INSERT INTO kg_entities (title, url, content, authors, published_date, category, source) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (p['title'], url, p['abstract'], json.dumps(p['authors']),
         p['published'], json.dumps(p['categories']), 'arxiv'))

conn.commit()
```

## Vector Generation

Run existing script: `python3 scripts/generate_vectors.py`
Automatically detects entities without vectors, generates 256-dim embeddings, stores in `kg_vectors`.

## Knowledge Graph Analysis

### PageRank
```python
from collections import defaultdict
# Build graph from kg_relationships (source_id, target_id)
# Standard PageRank with damping=0.85, 20 iterations
```

### Louvain Community Detection (Simple Label Propagation)
```python
labels = {eid: eid for eid in entity_ids}
for iteration in range(15):
    for nid in entity_ids:
        neighbors = graph[nid] + in_graph[nid]
        if not neighbors: continue
        label_counts = defaultdict(int)
        for nb in neighbors:
            label_counts[labels[nb]] += 1
        if label_counts:
            labels[nid] = max(label_counts, key=label_counts.get)
```

### Relationship Creation
```python
relations = [
    (src_id, tgt_id, 'relates_to', 0.7),
    (src_id, tgt_id, 'extends', 0.8),
]
for s, t, rel_type, weight in relations:
    cursor.execute('SELECT COUNT(*) FROM kg_relationships WHERE source_id=? AND target_id=? AND relationship_type=?', (s, t, rel_type))
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO kg_relationships (source_id, target_id, relationship_type, weight) VALUES (?, ?, ?, ?)', (s, t, rel_type, weight))
```

## Vector Storage Format

Vectors stored as 256-dim float32 binary blob in `kg_vectors.vector_data`:
```python
import struct
dim = len(vdata) // 4  # 256 for 1024 bytes
vec = struct.unpack(f'{dim}f', vdata)
```

## Known Issues

- `web_search` tool may return `NoneType` errors (API unavailable)
- `web_extract` blocks arxiv.org URLs (firecrawl not running)
- arXiv API frequently returns 429 — use httpx with proxy and rate limiting
- `read_file` on large files (INDEX.md 100k+) may paginate — read full file before patching
