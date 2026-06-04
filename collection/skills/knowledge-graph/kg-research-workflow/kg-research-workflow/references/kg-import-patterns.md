# KG Import Patterns & Arxiv Access Fallbacks (Verified 2026-05-18)

## kg.db Verified Schema

```sql
-- kg_entities (wiki/kg.db and workspace kg.db)
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,          -- UNIQUE constraint!
    content TEXT,                       -- JSON with keywords, abstract
    authors TEXT,
    published_date TEXT,
    category TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- kg_relations (simple 4-col table, NO primary key)
CREATE TABLE kg_relations (
    source INT,
    target INT,
    type TEXT,           -- 'HAS_KEYWORD', 'similarity', etc.
    weight REAL
);

-- kg_relationships (with autoincrement id)
CREATE TABLE kg_relationships (
    id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    target_id INTEGER NOT NULL,
    relationship_type TEXT,
    weight REAL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Key points:**
- NO `entity_type` column — use `category` field ('keyword' for keywords)
- NO `name` column — use `title`
- `url` has UNIQUE constraint — keyword entities need unique pseudo-URLs

## Keyword Import Pattern

```python
kw_url = f"keyword://{kw.lower().replace(' ', '-')}"
cursor.execute(
    "INSERT INTO kg_entities (title, url, category) VALUES (?, ?, 'keyword')",
    (kw, kw_url)
)
cursor.execute(
    "INSERT OR IGNORE INTO kg_relations (source, target, type, weight) VALUES (?, ?, ?, ?)",
    (paper_id, kw_id, "HAS_KEYWORD", 1.0)
)
```

## Arxiv API Access Fallback Chain

When the arxiv API is rate-limited (HTTP 429 "Rate exceeded" or timeout):

1. **curl with proxy + delays**: `curl -s --proxy http://127.0.0.1:7890 --max-time 20` with 15-30s delays. Still often rate-limited after 2-3 requests.
2. **browser_navigate**: Most reliable. Browse `https://arxiv.org/list/q-bio.NC/new` or `https://arxiv.org/abs/{id}` for full abstracts.
3. **Mine existing kg.db**: 1000+ papers already imported. Query:
   ```sql
   SELECT id, title, url, category FROM kg_entities 
   WHERE category LIKE '%q-bio%' OR category LIKE '%cs.NE%' 
   ORDER BY id DESC LIMIT 20
   ```
4. **web_search**: Sometimes returns NoneType errors (unreliable in cron context).

## Two kg.db Locations

- Primary workspace: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- Wiki location: `/Users/hiyenwong/wiki/kg.db`

Both have similar schemas. The wiki kg.db was used in this session.
