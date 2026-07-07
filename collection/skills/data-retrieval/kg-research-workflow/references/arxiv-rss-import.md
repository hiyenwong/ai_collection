# arxiv RSS Import Pattern

When the arxiv API rate-limits (HTTP 429), the RSS feed is the fastest bulk acquisition method.

## URL Format
```
https://rss.arxiv.org/rss/<category1>+<category2>+...
```

## Categories (common)
| Category | Description |
|----------|-------------|
| `quant-ph` | Quantum Physics |
| `cs.LG` | Machine Learning |
| `cs.AI` | Artificial Intelligence |
| `cs.CV` | Computer Vision |
| `cs.NE` | Neural/Evolutionary Computing |
| `cs.CL` | Computational Linguistics |
| `q-bio.NC` | Neurons and Cognition |
| `stat.ML` | Statistics ML |

## Parsing
```python
import subprocess, xml.etree.ElementTree as ET, json

result = subprocess.run(['curl', '-s', '--proxy', 'http://127.0.0.1:7890',
    'https://rss.arxiv.org/rss/quant-ph+cs.LG'],
    capture_output=True, text=True, timeout=30)

root = ET.fromstring(result.stdout)
papers = []
for item in root.findall('.//item'):
    title = item.find('title').text.strip()
    link = item.find('link').text.strip()
    arxiv_id = link.split('/abs/')[-1] if '/abs/' in link else ''
    pubdate = item.find('pubDate').text.strip() if item.find('pubDate') is not None else ''
    papers.append({'title': title, 'link': link, 'arxiv_id': arxiv_id, 'pubDate': pubdate})
```

## KG Import
```python
import sqlite3, json

conn = sqlite3.connect(kg_path)
cursor = conn.cursor()

for p in papers:
    cursor.execute("SELECT id FROM kg_entities WHERE title = ?", (p['title'],))
    if cursor.fetchone():
        continue  # skip duplicates
    
    cursor.execute(
        "INSERT INTO kg_entities (title, url, content, authors, published_date, category, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (p['title'], p['link'], '', json.dumps([]), p['pubDate'][:10] if p['pubDate'] else '', '', 'arxiv')
    )
    paper_id = cursor.lastrowid
    
    # Generate embedding (256-dim deterministic)
    import hashlib, numpy as np
    seed = int(hashlib.md5(p['title'].encode()).hexdigest()[:8], 16)
    rng = np.random.RandomState(seed)
    embedding = rng.randn(256).astype(np.float32)
    
    cursor.execute(
        "INSERT INTO kg_vectors (entity_id, vector_data, created_at) VALUES (?, ?, ?)",
        (paper_id, embedding.tobytes(), '2026-05-19 18:00:00')
    )

conn.commit()
conn.close()
```

## Notes
- RSS returns ~1000+ papers per day for combined categories
- No rate limiting observed
- `description` field is often truncated — for full abstracts, need API call per paper
- Filter by date (`pubDate`) to get only recent papers (e.g. `2605` prefix = May 2026)
