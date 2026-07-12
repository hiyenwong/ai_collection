# kg.db Entities Insert Pattern (CORRECTED 2026-06-08)

## Working Schema — Verified in Session

**Session 2026-06-08**: Successfully inserted 2 neuroscience papers using this working schema.

**Verified schema** (via PRAGMA and successful INSERTs):

```sql
entities(id TEXT PRIMARY KEY,
         type TEXT NOT NULL,
         name TEXT NOT NULL,
         arxiv_id TEXT,
         created TEXT DEFAULT CURRENT_TIMESTAMP)
```

**Key facts**:
- `id` is TEXT PRIMARY KEY (format `arxiv:{arxiv_id}`), NOT INTEGER AUTOINCREMENT
- `name` stores the paper title (TEXT)
- `type` stores entity type (TEXT, e.g., 'paper', 'skill', 'concept')
- `arxiv_id` stores raw arXiv ID (TEXT, e.g., '2606.07336')
- `created` auto-populates with CURRENT_TIMESTAMP

## Correct Insert Pattern

```bash
sqlite3 ~/.hermes/kg.db \
  "INSERT INTO entities (id, type, name, arxiv_id, created)
   VALUES ('arxiv:2606.07336',
           'paper',
           'Fixed Point Compositionality via Low-Rank Gluing Rules in Inhibition-Dominated Threshold-Linear Networks',
           '2606.07336',
           datetime('now'));"
```

**Batch insert pattern** (multiple papers):

```bash
sqlite3 ~/.hermes/kg.db \
  "INSERT INTO entities (id, type, name, arxiv_id, created) VALUES 
   ('arxiv:2606.07336', 'paper', 'Fixed Point Compositionality...', '2606.07336', datetime('now')),
   ('arxiv:2606.06647', 'paper', 'The Identity Trap in EEG Foundation Models...', '2606.06647', datetime('now'));"
```

## Verify Insert

```bash
# Check inserted rows
sqlite3 ~/.hermes/kg.db \
  "SELECT id, name, arxiv_id FROM entities WHERE arxiv_id LIKE '2606.%';"

# Count total entities
sqlite3 ~/.hermes/kg.db \
  "SELECT COUNT(*) FROM entities;"
```

Expected output (2026-06-08 session):
```
arxiv:2606.07336|Fixed Point Compositionality...|2606.07336
arxiv:2606.06647|The Identity Trap in EEG Foundation Models...|2606.06647

Total: 10
```

## Why Previous Documentation Was Wrong

**Error source**: Earlier session documentation (2026-06-06, 2026-06-08 compaction summary) listed WRONG schema:
- Listed `id INTEGER PRIMARY KEY AUTOINCREMENT` — but actual is TEXT PRIMARY KEY
- Listed `importance_score REAL`, `attributes TEXT`, `category TEXT`, `description TEXT` — but actual schema has NO these columns
- Listed complex JSON serialization pattern — but actual insert is simple string values

**Root cause**: Multiple kg.db instances exist in different project directories. The complex schema belonged to `/Users/hiyenwong/.openclaw/workspace/kg.db`, NOT `~/.hermes/kg.db` (the Hermes-internal one).

**Lesson**: ALWAYS run `PRAGMA table_info(entities)` on the specific kg.db path before INSERT. Never trust documentation or session summaries — verify schema in current session.

## Session 2026-06-08 Success Proof

Commands executed:
```bash
sqlite3 ~/.hermes/kg.db "INSERT INTO entities (id, type, name, arxiv_id, created) VALUES ('arxiv:2606.07336', 'paper', 'Fixed Point Compositionality...', '2606.07336', datetime('now'));"
sqlite3 ~/.hermes/kg.db "INSERT INTO entities (id, type, name, arxiv_id, created) VALUES ('arxiv:2606.06647', 'paper', 'The Identity Trap...', '2606.06647', datetime('now'));"
sqlite3 ~/.hermes/kg.db "SELECT COUNT(*) FROM entities;"
```

Result: `10` (2 new papers + 8 existing entities)

## Future Session Checklist

1. Run `PRAGMA table_info(entities)` on `~/.hermes/kg.db` first
2. Use `id TEXT PRIMARY KEY` format (`arxiv:{arxiv_id}`)
3. Use `name` column for title, NOT `title` column
4. Simple string insert, no JSON serialization needed
5. Verify with `SELECT COUNT(*) FROM entities;` after insert