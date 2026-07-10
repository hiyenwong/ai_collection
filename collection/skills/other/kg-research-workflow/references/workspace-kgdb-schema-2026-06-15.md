# Workspace kg.db Verified Schema — 2026-06-15

## Location
`/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`

## Tables

### kg_entities (REAL TABLE — INTEGER id)
```
0|id|INTEGER|0||1          ← auto-increment PRIMARY KEY
1|name|TEXT|1||0           ← paper title or entity name
2|type|TEXT|1||0           ← 'paper', 'keyword', 'author', etc.
3|description|TEXT|0||0    ← abstract or description
4|metadata|TEXT|0||0       ← JSON blob
5|created_at|TIMESTAMP|0|CURRENT_TIMESTAMP|0
6|source|TEXT|0|''|0       ← URL
7|created_date|TEXT|0|''|0 ← YYYY-MM-DD
```

### kg_documents (REAL TABLE)
```
0|id|INTEGER|0||1          ← auto-increment
1|arxiv_id|TEXT|0||0       ← bare arxiv ID (e.g. '2606.07657')
2|title|TEXT|0||0
3|authors|TEXT|0||0
4|abstract|TEXT|0||0
5|categories|TEXT|0||0
6|pdf_url|TEXT|0||0
7|abs_url|TEXT|0||0
8|published|TEXT|0||0
9|created_at|TIMESTAMP|0|CURRENT_TIMESTAMP|0
```

### kg_relations (REAL TABLE — INTEGER IDs)
```
0|id|INTEGER|0||1
1|source_id|INTEGER|0||0   ← FK to kg_entities.id
2|target_id|INTEGER|0||0   ← FK to kg_entities.id
3|relation_type|TEXT|1||0  ← 'HAS_KEYWORD', 'CITES', 'authored_by'
4|weight|REAL|0|1.0|0
5|metadata|TEXT|0||0       ← JSON
6|created_at|TIMESTAMP|0|CURRENT_TIMESTAMP|0
```

### kg_vectors (REAL TABLE)
```
0|id|INTEGER|0||1
1|entity_id|INTEGER|0||0   ← FK to kg_documents.id (NOT kg_entities!)
2|embedding|BLOB|0||0      ← struct.pack('128d', *vec)
3|text|TEXT|0||0
4|created_at|TIMESTAMP|0|CURRENT_TIMESTAMP|0
```

### arxiv_papers (REAL TABLE)
```
exists but unused — use kg_documents instead
```

### Views (NOT writable)
- `entities` → view over kg_entities
- `documents` → view over kg_documents
- `vectors` → view over kg_vectors
- `relationships` → view over kg_relations
- `relationships_v2` → view
- `kg_relations_compat` → view

## CRITICAL: Insert Pattern

```python
import sqlite3, struct

db = sqlite3.connect("/Users/hiyenwong/.openclaw/workspace/scripts/kg.db")
cur = db.cursor()

# 1. Insert into kg_documents first (needed for kg_vectors.entity_id)
cur.execute("""
    INSERT INTO kg_documents (arxiv_id, title, authors, abstract, categories, abs_url, published)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", ("2606.07657", "Paper Title", "", "Abstract...", "cs.NE, cs.LG", 
      "https://arxiv.org/abs/2606.07657", "2026-06-15"))
doc_id = cur.lastrowid

# 2. Insert into kg_entities
cur.execute("""
    INSERT INTO kg_entities (name, type, description, metadata, source, created_date)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("Paper Title", "paper", "Abstract...", "{}", 
      "https://arxiv.org/abs/2606.07657", "2026-06-15"))
entity_id = cur.lastrowid

# 3. Create keyword relationships
cur.execute("SELECT id FROM kg_entities WHERE name = ?", ("cs.NE",))
kw_row = cur.fetchone()
if not kw_row:
    cur.execute("""
        INSERT INTO kg_entities (name, type, description, metadata)
        VALUES (?, ?, ?, ?)
    """, ("cs.NE", "keyword", "Topic: cs.NE", "{}"))
    kw_id = cur.lastrowid
else:
    kw_id = kw_row[0]

cur.execute("""
    INSERT INTO kg_relations (source_id, target_id, relation_type, weight, metadata)
    VALUES (?, ?, ?, ?, ?)
""", (entity_id, kw_id, "HAS_KEYWORD", 1.0, "{}"))

# 4. Generate embedding for kg_vectors
import hashlib, math
text = "Paper Title Abstract... cs.NE, cs.LG"
words = text.lower().split()
vec = [0.0] * 128
for word in words:
    h = int(hashlib.md5(word.encode()).hexdigest(), 16)
    for i in range(min(3, 128)):
        idx = (h + i * 7919) % 128
        vec[idx] += 1.0
norm = math.sqrt(sum(v*v for v in vec)) or 1.0
vec = [v/norm for v in vec]
packed = struct.pack('128d', *vec)

cur.execute("""
    INSERT INTO kg_vectors (entity_id, embedding, text)
    VALUES (?, ?, ?)
""", (doc_id, packed, "Paper Title"))

db.commit()
```

## Common Pitfall
- **`entities` is a VIEW** — cannot INSERT into it directly. Use `kg_entities`.
- **`kg_vectors.entity_id` references `kg_documents.id`**, NOT `kg_entities.id` — this mismatch means you need both tables populated.
- **Embedding is BLOB** — use `struct.pack('128d', *vec)`, not JSON strings.
