# kg.db Actual Schemas 2026-06-11 (VERIFIED)

**Verification date**: Thursday, June 11, 2026
**Method**: Direct PRAGMA table_info queries via sqlite3 CLI
**Location**: `/Users/hiyenwong/Library/Application Support/knowledge-graph/kg.db`

## CRITICAL: Schema Drift Pattern

kg.db schema has drifted multiple times across sessions. **ALWAYS run `PRAGMA table_info({table})` before inserting**. Do NOT rely on previous documentation or assumptions.

## Papers Table Schema (VERIFIED 2026-06-11)

```sql
sqlite3 kg.db "PRAGMA table_info(papers)"

0|id|INTEGER|0||1
1|arxiv_id|TEXT|0||0
2|title|TEXT|0||0
3|authors|TEXT|0||0
4|categories|TEXT|0||0
5|publication_date|TEXT|0||0
6|skill_created|TEXT|0||0
7|key_findings|TEXT|0||0
8|activation_keywords|TEXT|0||0
9|applications|TEXT|0||0
10|created_at|TIMESTAMP|0|CURRENT_TIMESTAMP|0
```

**Schema interpretation**:
- `id` is INTEGER PRIMARY KEY AUTOINCREMENT (not TEXT)
- `arxiv_id` is TEXT with UNIQUE constraint (confirmed by separate query)
- **NOT** `arxiv_id TEXT PRIMARY KEY` — id handles auto-increment
- Fields: title, authors, categories, publication_date, skill_created, key_findings, activation_keywords, applications, created_at

**Correct insert pattern**:
```sql
INSERT OR REPLACE INTO papers 
(arxiv_id, title, authors, publication_date, categories, skill_created, 
 key_findings, activation_keywords, applications, created_at)
VALUES 
('2606.10891', 'Bilinear gating of motor primitives...', 'Capone et al.', 
 '2026-06-09', 'q-bio.NC', 'bilinear-gating-motor-primitives-dendritic-computation',
 'burst fraction encodes goal information; Layer-5 pyramidal neurons implement bilinear gating via dendritic coincidence detection',
 'bilinear gating, motor primitives, dendritic computation, Layer-5 pyramidal, burst fraction',
 'motor control, decision-making, neural dynamics modeling, goal-conditioned behavior',
 datetime('now'));
```

**Wrong insert pattern (from older sessions)**:
```sql
-- WRONG: arxiv_id TEXT PRIMARY KEY assumption
INSERT INTO papers (arxiv_id, ...) VALUES (...);  -- Works but id is auto-generated

-- WRONG: id stores arxiv:XXXX.XXXXX format
INSERT INTO papers (id, ...) VALUES ('arxiv:2606.10891', ...);  -- Type mismatch
```

## kg_entities Table Schema (VERIFIED 2026-06-11)

```sql
sqlite3 kg.db "PRAGMA table_info(kg_entities)"

0|id|INTEGER|0||1
1|title|TEXT|0||0
2|url|TEXT|0||0
3|content|TEXT|0||0
4|authors|TEXT|0||0
5|published_date|TEXT|0||0
6|category|TEXT|0||0
7|source|TEXT|0||0
8|created_at|TIMESTAMP|0||0
9|updated_at|TIMESTAMP|0||0
```

**NOT** `(name TEXT, type TEXT, description TEXT, metadata TEXT)` — that schema is stale from older sessions.

**Correct insert pattern**:
```sql
INSERT INTO kg_entities 
(title, url, content, authors, published_date, category, source, created_at)
VALUES 
('Bilinear gating of motor primitives', 'https://arxiv.org/abs/2606.10891', 
 'Abstract content...', 'Capone et al.', '2026-06-09', 'q-bio.NC', 'arxiv', datetime('now'));
```

## kg_vectors Table Schema (VERIFIED 2026-06-11)

```sql
sqlite3 kg.db "PRAGMA table_info(kg_vectors)"

0|id|INTEGER|0||1
1|entity_id|INTEGER|0||0
2|vector_data|BLOB|0||0
3|created_at|TIMESTAMP|0||0
```

**Column is `vector_data` NOT `embedding`**. BLOB type holds binary vector data.

**Insert pattern**:
```python
import struct

# Generate vector (example: 128-dim from SHA256 hash)
hash_hex = hashlib.sha256(title.encode()).hexdigest()
vector = [int(hash_hex[i:i+2], 16) / 255.0 for i in range(0, 256, 2)]
packed = struct.pack(f'{len(vector)}f', *vector)

# Insert
sqlite3 kg.db "INSERT INTO kg_vectors (entity_id, vector_data, created_at) VALUES (123, X'...hex...', datetime('now'))"
```

**Pitfall**: Python `fetchone()` may return BLOB as `str` (latin-1 encoded) rather than `bytes`. Check and convert:
```python
data = cursor.fetchone()[0]
if isinstance(data, str):
    data = data.encode('latin-1')
vector = struct.unpack(f'{len(data)//4}f', data)
```

## kg_relationships Table Schema (VERIFIED 2026-06-11)

```sql
sqlite3 kg.db "PRAGMA table_info(kg_relationships)"

0|id|INTEGER|0||1
1|source_id|INTEGER|0||0
2|target_id|INTEGER|0||0
3|relationship_type|TEXT|0||0
4|weight|REAL|0||0
5|created_at|TIMESTAMP|0||0
```

**Insert pattern**:
```sql
INSERT INTO kg_relationships 
(source_id, target_id, relationship_type, weight, created_at)
VALUES 
(123, 456, 'derived_from', 1.0, datetime('now'));
```

## Auxiliary/Legacy Tables (MAY EXIST BUT NOT CURRENT)

These may be from older sessions or different database versions:
- `arxiv_papers` (TEXT id = raw arxiv ID)
- `entities` (TEXT id, name, type, category, description, source, created_date)
- `vectors` (TEXT id, embedding BLOB, metadata TEXT)
- `relationships` (TEXT source_id/target_id/relation_type/weight/created_date)

**Recommendation**: Use `kg_entities`, `kg_vectors`, `kg_relationships` for current workflow. Auxiliary tables may be legacy.

## Location Pitfall (VERIFIED 2026-06-11)

**Wrong location**: `~/Library/Application Support/knowledge/kg.db`
**Correct location**: `/Users/hiyenwong/Library/Application Support/knowledge-graph/kg.db`

**Discovery method**: 
```bash
find ~/Library -name "kg.db" 2>/dev/null
ls -la ~/Library/Application\ Support/knowledge-graph/
```

## Verification Workflow (RECOMMENDED)

Before any kg.db operation in future sessions:

1. **Locate database**: `find ~/Library -name "kg.db" 2>/dev/null`
2. **Verify schema**: `sqlite3 kg.db "PRAGMA table_info(papers)"`
3. **Check constraints**: `sqlite3 kg.db "SELECT sql FROM sqlite_master WHERE type='table' AND name='papers'"`
4. **Insert with correct column names**: Use verified schema, not assumptions

**Pattern**: Schema drift is a recurring issue. Previous session documentation can be stale. Always verify before inserting.

## Session References

- 2026-06-09: kg.db schema correction (NO arxiv_id column, id stores arxiv:XXXX.XXXXX format) — **OUTDATED, superseded by 2026-06-11**
- 2026-06-10: kg.db verified schema (papers.arxiv_id as TEXT PK) — **VERIFIED, still current**
- 2026-06-11: Complete PRAGMA verification, location confirmed, papers table schema finalized

## Related References

- [kg-db-entities-insert-pattern.md](kg-db-entities-insert-pattern.md) — entities table insert pattern with importance_score extraction
- [kg-db-actual-schemas-2026-06-09.md](kg-db-actual-schemas-2026-06-09.md) — June 9 schema (superseded)
- [neuroscience-cron-2026-06-11-complete-workflow.md](neuroscience-cron-2026-06-11-complete-workflow.md) — kg.db insert examples using verified schema