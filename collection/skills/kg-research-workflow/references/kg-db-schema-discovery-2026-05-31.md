# kg.db Schema Discovery (2026-05-31)

Session discovered actual schema mismatch between documented schema and running Hermes kg.db.

## Discovery Context

During neuroscience paper sync cron job, initial INSERT attempts failed because the documented schema (separate columns for `category`, `description`, `source`) did not match the actual running database schema.

## Actual Schema Verified

**Hermes main kg.db**: `/Users/hiyenwong/.hermes/kg.db`

```sql
sqlite3 /Users/hiyenwong/.hermes/kg.db "PRAGMA table_info(entities);"

id|TEXT|0||1
name|TEXT|1||0
type|TEXT|1||0
attributes|TEXT|0||0
created_at|TEXT|0||0
last_accessed|TEXT|0||0
importance_score|REAL|0|0.5|0
```

**Key insight**: ALL metadata (arxiv_id, authors, categories, abstract, published date, etc.) stored in `attributes` TEXT column as JSON blob, NOT in separate columns.

## Correct INSERT Pattern

```python
import sqlite3, json

conn = sqlite3.connect("/Users/hiyenwong/.hermes/kg.db")
c = conn.cursor()

# Entity ID format: 'arxiv:XXXX.XXXXX' (with prefix)
entity_id = f"arxiv:{arxiv_id}"

# Pack all metadata into attributes JSON
attrs = {
    "arxiv_id": arxiv_id,
    "authors": authors_list,
    "categories": categories_list,
    "published": published_date,
    "abstract": abstract_text,
    "source": "arxiv",
    "doi": doi if available
}

c.execute("""
    INSERT INTO entities (id, name, type, attributes, created_at)
    VALUES (?, ?, ?, ?, datetime('now'))
""", (entity_id, title, "paper", json.dumps(attrs)))

conn.commit()
```

## Query Pattern

```python
c.execute("SELECT id, name, type, attributes FROM entities WHERE type='paper' LIMIT 10")
for row in c.fetchall():
    entity_id = row[0]          # 'arxiv:2605.29677'
    name = row[1]               # paper title
    type_val = row[2]           # 'paper'
    attrs_json = row[3]         # JSON string
    attrs = json.loads(attrs_json)
    
    arxiv_id = attrs.get('arxiv_id')
    authors = attrs.get('authors', [])
    categories = attrs.get('categories', [])
    abstract = attrs.get('abstract', '')
```

## Bulk Import Pattern (Verified Working)

```python
import sqlite3, json

papers = [
    {
        "arxiv_id": "2605.29677",
        "title": "Embodied Virtual Reality Feedback...",
        "authors": ["Gao, Y.", "Wang, Z."],
        "categories": ["q-bio.NC", "cs.HC"],
        "published": "2026-05-27",
        "abstract": "VR feedback reshapes neural..."
    },
    {
        "arxiv_id": "2605.28854",
        "title": "LLM Representational Geometry...",
        "authors": ["Li, J.", "Chen, X."],
        "categories": ["cs.CL", "cs.AI"],
        "published": "2026-05-27",
        "abstract": "LLMs reorganize geometry..."
    }
]

conn = sqlite3.connect("/Users/hiyenwong/.hermes/kg.db")
c = conn.cursor()

for p in papers:
    attrs = {
        "arxiv_id": p["arxiv_id"],
        "authors": p["authors"],
        "categories": p["categories"],
        "published": p["published"],
        "abstract": p["abstract"][:1000]  # truncate long abstracts
    }
    
    c.execute("""
        INSERT INTO entities (id, name, type, attributes, created_at)
        VALUES (?, ?, ?, ?, datetime('now'))
    """, (
        f"arxiv:{p['arxiv_id']}",
        p["title"],
        "paper",
        json.dumps(attrs)
    ))

conn.commit()
print(f"Inserted {len(papers)} papers")
```

## Entity Count Verification

```bash
sqlite3 /Users/hiyenwong/.hermes/kg.db "SELECT COUNT(*) FROM entities WHERE type='paper';"
# Returns: 36 (as of 2026-05-31 cron run)

sqlite3 /Users/hiyenwong/.hermes/kg.db "SELECT COUNT(*) FROM entities;"
# Returns: total entity count across all types
```

## Pitfall Avoidance

1. **Wrong schema reference**: Old docs showed `category`, `description`, `source` as separate columns → INSERT failed
2. **Bare IDs**: Use `arxiv:2605.29677`, not bare `2605.29677`
3. **Missing JSON encoding**: `attributes` MUST be `json.dumps(dict)`, not raw dict
4. **Column mismatch**: Primary kg.db has 7 columns (id, name, type, attributes, created_at, last_accessed, importance_score), secondary workspace kg.db has 7 different columns (id, name, type, category, description, source, created_date)

## Secondary kg.db Note

The workspace database at `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` uses the OLD expanded schema (separate columns). This is a LEGACY database — prefer Hermes main kg.db for paper imports.

```bash
# Workspace kg.db schema (legacy)
sqlite3 /Users/hiyenwong/.openclaw/workspace/scripts/kg.db "PRAGMA table_info(entities);"
# Returns: id, name, type, category, description, source, created_date
```

## Related Reference Files

- [kg-schema-2026-05-26.md](kg-schema-2026-05-26.md) — older schema reference (workspace db)
- [kg-import-patterns.md](kg-import-patterns.md) — general import patterns