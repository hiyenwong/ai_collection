# KG Research — Operational Notes

*Current as of 2026-05-05*

## Actual Database Schema

### kg_entities
```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    content TEXT,
    authors TEXT,
    published_date TEXT,
    category TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### kg_relations
```sql
CREATE TABLE kg_relations(source INT, target INT, type TEXT, weight REAL);
```

### kg_relationships (used alongside kg_relations)
```sql
CREATE TABLE kg_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER,
    target_id INTEGER,
    relationship_type TEXT,
    weight REAL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_id) REFERENCES kg_entities (id),
    FOREIGN KEY (target_id) REFERENCES kg_entities (id)
);
```

### kg_vectors
```sql
CREATE TABLE kg_vectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER,
    vector_data BLOB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entity_id) REFERENCES kg_entities (id)
);
```

**Key difference from older docs**: The table uses `title/url/content/authors/published_date/category/source`, NOT `entity_type/name/properties`.

## kg_tool Binary

**Path**: `scripts/kg_tool/target/release/kg_tool` (relative to workspace)

**DB path**: `/Users/hiyenwong/wiki/kg.db` — this is a symlink to `/Users/hiyenwong/.openclaw/workspace/kg.db`

**Commands**:
```
kg_tool import-paper  --title <t> --url <u> [--abstract <a>] [--authors <a>]
kg_tool generate-embeddings    # Generate embeddings for entities without them
kg_tool search        --query <q> [--limit <n>]
kg_tool pagerank      [--limit <n>]
kg_tool communities   [--limit <n>]
kg_tool stats
```

**NOT**: `kg_tool list`, `kg_tool pagerank kg.db`, etc. — no DB path argument needed.

## Arxiv Access (2026-05)

- `web_extract` returns "Blocked: URL targets a private or internal network" for ALL arxiv URLs
- `terminal` + `curl` to arxiv API returns empty responses
- **Working method**: `browser_navigate` → `browser_snapshot` for paper abstract/metadata
- Use arxiv HTML pages: `https://arxiv.org/html/{id}v1` (also blocked by web_extract)
- For discovery: `web_search` with `site:arxiv.org` works well

## Weekly Topics Script

**Path**: `scripts/weekly_topics.py` (relative to workspace)

**Output**: Prints weekday number, topic name, and keywords. Used to drive daily research focus.

**Schedule**: Mon=Neuroscience, Tue=Computer Science, Wed=Medicine, Thu=Systems Engineering, Fri=Math, Sat=Economics, Sun=Informatics

## Direct SQL Insert Pattern

When `kg_tool import-paper` doesn't fit, use direct SQLite:
```bash
sqlite3 kg.db "INSERT OR IGNORE INTO kg_entities (title, url, content, authors, published_date, category, source)
VALUES ('Title', 'https://arxiv.org/abs/XXXX.XXXXX', 'abstract...', 'Authors', 'YYYY-MM-DD', 'quant-ph, cs.AI', 'arxiv');"
```

## Relationship Insert Pattern

Use `kg_relationships` table (not `kg_relations`):
```sql
INSERT OR IGNORE INTO kg_relationships (source_id, target_id, relationship_type, weight)
VALUES (source_id, target_id, 'related_to', 0.9);
```

Common relationship types: `related_to`, `cites`, `shares_category`, `related_topic`, `same_domain`, `extends`, `cross_domain`, `similar`, `co_cited`

## Proxy

Agent proxy: `http://127.0.0.1:7890` (set via environment, not needed for web_search)
