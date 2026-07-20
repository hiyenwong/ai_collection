# kg.db Research Fallback Workflow

When arXiv API returns "Rate exceeded" (429) persistently, use the existing knowledge graph (kg.db) as the primary research source.

## Schema

| Table | Key Columns |
|-------|------------|
| `kg_entities` | id, title, url, content, authors, published_date, category, source, created_at |
| `kg_vectors` | id, entity_id, vector_data (BLOB) |
| `kg_relationships` | id, source_id, target_id, relationship_type, weight |
| `kg_relations` | source, target, type, weight |

Note: `kg_relationships` and `kg_relations` are separate tables with different column names. Use `kg_relations` (simpler: source/target/type/weight) for PageRank.

## Step 1: Quick KG Health Check

```python
import sqlite3, os
os.chdir('/Users/hiyenwong/.openclaw/workspace')
conn = sqlite3.connect('kg.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Counts
c.execute("SELECT COUNT(*) FROM kg_entities"); print("Entities:", c.fetchone()[0])
c.execute("SELECT COUNT(*) FROM kg_vectors"); print("Vectors:", c.fetchone()[0])
c.execute("SELECT COUNT(*) FROM kg_relations"); print("Relations:", c.fetchone()[0])

# Recent papers
c.execute("SELECT title, category, published_date FROM kg_entities ORDER BY created_at DESC LIMIT 10")
for r in c.fetchall():
    print(f"  [{r['published_date']}] {r['title'][:70]} ({r['category']})")
```

## Step 2: Query by Topic

```python
# Papers matching today's topic keywords
c.execute("""
    SELECT * FROM kg_entities 
    WHERE content IS NOT NULL AND length(content) > 50
    AND (category LIKE '%quant%' OR category LIKE '%stat%' OR category LIKE '%math%')
    ORDER BY published_date DESC LIMIT 20
""")
```

## Step 3: PageRank on kg_relations

```python
from collections import defaultdict

c.execute("SELECT source, target, weight FROM kg_relations WHERE weight IS NOT NULL")
edges = [(r['source'], r['target'], r['weight']) for r in c.fetchall()]

# Build graph
entity_ids = sorted(set(s for s,t,_ in edges) | set(t for s,t,_ in edges))
N = len(entity_ids)
id_idx = {e: i for i, e in enumerate(entity_ids)}
out_deg = defaultdict(float)
in_links = defaultdict(list)

for s, t, w in edges:
    out_deg[s] += w
    in_links[t].append((s, w))

# PageRank
pr = {e: 1.0/N for e in entity_ids}
damping = 0.85
for _ in range(10):
    new_pr = {}
    for e in entity_ids:
        rank = (1 - damping) / N
        for src, w in in_links.get(e, []):
            rank += damping * pr.get(src, 0) * w / max(out_deg.get(src, 1), 0.001)
        new_pr[e] = rank
    pr = new_pr

top = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:10]
```

## Step 4: Category-Based Clustering

```python
c.execute("SELECT id, title, category FROM kg_entities")
categories = defaultdict(list)
for r in c.fetchall():
    if r['category']:
        for cat in r['category'].replace(';', ',').split(','):
            cat = cat.strip()
            if cat:
                categories[cat].append(r['id'])
```

## Step 5: Keyword-Based Similarity (since vectors are binary BLOBs)

```python
query_terms = {'quantum', 'statistics', 'probability', 'number theory'}
c.execute("SELECT id, title, content, category FROM kg_entities WHERE content IS NOT NULL")
for r in c.fetchall():
    text = (r['content'] or '').lower() + ' ' + (r['title'] or '').lower()
    score = sum(1 for t in query_terms if t in text)
    if score >= 2:
        print(f"  Score={score} | {r['title'][:80]}")
```

## Proven Topics from KG

The KG contains ~500+ papers covering:
- Quantum computing & physics (~181 papers)
- Machine learning & AI (~67 papers)
- Neuroscience (~18 papers)
- Mathematics & statistics (sparse, ~2 papers)

## Pitfalls

1. **kg_entities column names**: Use `title` not `name`, `content` not `abstract` or `description`
2. **Two relation tables**: `kg_relations` has `source/target` (int), `kg_relationships` has `source_id/target_id` (int)
3. **Vector BLOBs**: kg_vectors stores embeddings as binary BLOBs — not human-readable. Use keyword-based similarity instead
4. **Category format**: Multiple categories separated by commas or semicolons — normalize with `.replace(';', ',')`
5. **arXiv rate limits**: Even with proxy and User-Agent headers, arXiv returns persistent 429. Don't waste retries — go directly to kg.db fallback
