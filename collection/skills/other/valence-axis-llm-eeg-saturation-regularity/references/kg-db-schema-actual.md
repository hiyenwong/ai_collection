# kg.db Schema for Neuroscience Paper Imports

**Critical Finding (2026-06-03 Cron Session)**: The loaded `ai_collection/arxiv-search` skill's `references/kg-db-schema.md` documents a legacy `kg_entities` schema, but the **actual Hermes kg.db schema** is different.

## Actual Hermes kg.db Schema

**Location**: `/Users/hiyenwong/.hermes/kg.db`

### papers table
```sql
CREATE TABLE papers (
  arxiv_id TEXT PRIMARY KEY,
  title TEXT,
  authors TEXT,
  skill TEXT,
  date_added TEXT
);
```

### paper_insights table
```sql
CREATE TABLE paper_insights (
  paper_id TEXT,
  insight TEXT,
  ranking INTEGER
);
```

### paper_tags table
```sql
CREATE TABLE paper_tags (
  paper_id TEXT,  -- TEXT FK, NOT INTEGER
  tag TEXT
);
```

## Verified Working Pattern

```python
import sqlite3

conn = sqlite3.connect("/Users/hiyenwong/.hermes/kg.db")
c = conn.cursor()

# Insert paper (arxiv_id WITHOUT "arxiv:" prefix)
c.execute("""
    INSERT INTO papers (arxiv_id, title, authors, skill, date_added)
    VALUES (?, ?, ?, ?, datetime('now'))
""", ("2606.00129", "Paper Title", "Author 1, Author 2", "valence-axis-llm-eeg"))

# Insert tags
tags = ["valence axis", "LLM-EEG alignment", "saturation regularity"]
for tag in tags:
    c.execute("INSERT INTO paper_tags (paper_id, tag) VALUES (?, ?)",
              ("2606.00129", tag))

conn.commit()
```

## Key Points

1. **arxiv_id format**: Just the ID number (e.g., "2606.00129"), NOT "arxiv:2606.00129"
2. **paper_id in paper_tags**: TEXT type matching papers.arxiv_id (NOT INTEGER FK)
3. **Database path**: `/Users/hiyenwong/.hermes/kg.db` for Hermes main KG
4. **Other kg.db paths**: `/Users/hiyenwong/wiki/kg.db` (kg_tool), `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` (legacy) — do NOT use for new paper imports

## Session Evidence (2026-06-03)

Successfully inserted arXiv:2606.00129 into Hermes kg.db:
```bash
sqlite3 ~/.hermes/kg.db "SELECT arxiv_id, title FROM papers WHERE arxiv_id='2606.00129';"
# Output: 2606.00129|A Shared Valence Axis...

sqlite3 ~/.hermes/kg.db "SELECT tag FROM paper_tags WHERE paper_id='2606.00129';"
# Output: valence axis|LLM-EEG alignment|saturation regularity
```

## Action Required

The `ai_collection/arxiv-search` skill's `references/kg-db-schema.md` needs updating to reflect this actual schema. Future sessions reading that file will use wrong schema or wrong database paths.

---

**Created**: 2026-06-03
**Session**: Neuroscience cron job (valence-axis-llm-eeg-saturation-regularity skill creation)
**Related**: `ai_collection/arxiv-search` skill needs patching for schema mismatch