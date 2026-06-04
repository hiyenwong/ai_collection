# kg.db Schema Reference

Location: `/Users/hiyenwong/.openclaw/workspace/kg.db`

## Tables

### kg_entities
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER (PK) | Auto-increment entity ID |
| title | TEXT (NOT NULL) | Paper title |
| url | TEXT (NOT NULL) | arXiv URL or other source |
| content | TEXT | Abstract or summary |
| authors | TEXT | Author list |
| published_date | TEXT | Publication date |
| category | TEXT | arXiv categories |
| source | TEXT | "arxiv", "semantic_scholar", etc. |
| created_at | TIMESTAMP | Insertion time |
| updated_at | TIMESTAMP | Last update time |

### kg_vectors
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER (PK) | |
| entity_id | INTEGER (FK → kg_entities.id) | |
| vector_data | BLOB | 384-dim float array (struct packed) |
| created_at | TIMESTAMP | |

### kg_relationships
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER (PK) | |
| source_id | INTEGER (FK) | Source entity |
| target_id | INTEGER (FK) | Target entity |
| relationship_type | TEXT | e.g., "cites", "related" |
| weight | REAL (default 1.0) | Edge weight |
| created_at | TIMESTAMP | |

### kg_relations
| Column | Type | Notes |
|--------|------|-------|
| source | INT | Source entity ID |
| target | INT | Target entity ID |
| type | TEXT | Relationship type |
| weight | REAL | Edge weight |

## Vector Generation

Vectors are 384-dim float arrays packed via `struct.pack('384f', ...)`. If a paper lacks a vector, generate one deterministically from title+content using hash-based embedding:

```python
import sqlite3, hashlib, struct, re

conn = sqlite3.connect("kg.db")
# For entity_id, title, content:
text = (title or "") + " " + (content or "")
words = re.findall(r'\w+', text.lower())
vec = [0.0] * 384
for i, word in enumerate(words):
    h = int(hashlib.md5(word.encode()).hexdigest(), 16)
    for j in range(min(384, len(words))):
        seed = (h * (i + 1) * (j + 1)) % 1000000
        vec[j] += (seed / 1000000.0 - 0.5) * 2.0
norm = sum(v*v for v in vec) ** 0.5
if norm > 0:
    vec = [v/norm for v in vec]
blob = struct.pack('384f', *vec)
cursor.execute("INSERT OR IGNORE INTO kg_vectors (entity_id, vector_data) VALUES (?, ?)", (entity_id, blob))
```

## Useful Queries

```sql
-- Recent papers by date
SELECT id, title, url, published_date, category FROM kg_entities ORDER BY published_date DESC LIMIT 20;

-- Papers in specific categories
SELECT id, title, url FROM kg_entities WHERE category LIKE '%quant-ph%';

-- Entities without vectors
SELECT e.id, e.title FROM kg_entities e LEFT JOIN kg_vectors v ON e.id = v.entity_id WHERE v.id IS NULL;

-- Relationship density
SELECT COUNT(*) FROM kg_relations;
```
