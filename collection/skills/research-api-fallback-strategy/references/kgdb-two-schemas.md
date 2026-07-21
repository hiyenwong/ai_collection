# kg.db Two Databases, Two Schemas

As of 2026-05-26, there are **two separate kg.db files** with **different schemas** on this system:

## Database 1: OpenClaw Workspace kg.db
- **Path**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`
- **Tables**: `entities`, `relationships`, `kg_vectors`, `research_log`
- **`entities` schema**: `(id TEXT PK, name TEXT, type TEXT, category TEXT, description TEXT, source TEXT, created_date TEXT)`
- **Query example**: `SELECT id, name, description FROM entities WHERE type='paper' ORDER BY created_date DESC LIMIT 10;`
- **`relationships` schema**: `(id TEXT PK, source TEXT, target TEXT, relation TEXT, description TEXT, created_date TEXT)`
- **As of 2026-05-26**: 542 entities, 537 vectors

## Database 2: Wiki kg.db (used by kg_tool binary)
- **Path**: `/Users/hiyenwong/wiki/kg.db`
- **Tables**: `kg_entities`, `kg_relations`, `kg_relationships`, `kg_vectors`, `arxiv_papers`, `pagerank`
- **`kg_entities` schema**: `(id INTEGER PK, title TEXT, url TEXT, content TEXT, authors TEXT, published_date TEXT, category TEXT, source TEXT, created_at TIMESTAMP, updated_at TIMESTAMP)`
- **Query example**: `SELECT id, title, content FROM kg_entities WHERE title LIKE '%quantum%' ORDER BY published_date DESC LIMIT 10;`

## How to know which one to use

- **`kg_tool` binary** (`scripts/kg_tool/target/release/kg_tool`) → uses `/Users/hiyenwong/wiki/kg.db` (hardcoded)
- **`sqlite3 kg.db` in workspace** → uses `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`
- **Run `kg_tool stats`** to confirm which DB it's reading
- **If you want the workspace data**: use `sqlite3 /Users/hiyenwong/.openclaw/workspace/scripts/kg.db` directly

## Column name differences

| Concept | Workspace `entities` | Wiki `kg_entities` |
|---------|---------------------|-------------------|
| Paper title | `name` | `title` |
| Paper content | `description` | `content` |
| Paper type | `type` (e.g. 'paper', 'skill') | N/A (all rows are papers) |
| Relationship type | `relation` | `relationship_type` |
| Entity ID | `id` (TEXT like `arxiv_2605.13072`) | `id` (INTEGER auto-increment) |
