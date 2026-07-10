# kg.db Schema & kg_tool Commands — Verified 2026-05-14

## Primary Database: `kg.db` (workspace root)

### kg_entities
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK AUTOINCREMENT | |
| title | TEXT NOT NULL | Paper title or keyword name |
| url | TEXT UNIQUE NOT NULL | arXiv URL or empty for keywords |
| content | TEXT | Paper abstract |
| authors | TEXT | JSON array: `["Author 1"]` |
| published_date | TEXT | `YYYY-MM-DD` |
| category | TEXT | `quant-ph,cs.LG` |
| source | TEXT | `arxiv`, `keyword`, `anthropic` |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

### kg_relations
| Column | Type | Notes |
|--------|------|-------|
| source | INT | entity_id |
| target | INT | entity_id |
| type | TEXT | `HAS_KEYWORD`, `CITES`, `AUTHORED_BY` |
| weight | REAL | |

### kg_vectors
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK AUTOINCREMENT | |
| entity_id | INTEGER | FK to kg_entities |
| vector_data | BLOB | numpy float32 bytes |
| created_at | TIMESTAMP | |

Read vectors: `np.frombuffer(blob, dtype=np.float32)`

## kg_tool Commands

| Command | Status | Notes |
|---------|--------|-------|
| `stats` | ✅ | Entity/relation/vector counts |
| `pagerank` | ✅ | PageRank centrality |
| `communities --limit N` | ⚠️ | May crash on NoneType |
| `search --query "..."` | ✅ | Vector similarity |
| `generate-embeddings` | ✅ | Fill missing vectors |
| `import-paper --title T --url U` | ✅ | Add new paper |
| `louvain` | ❌ | Does not exist |
| `list` | ❌ | Does not exist |
| `--help` | ❌ | Does not exist |
