# kg_tool CLI Reference

Knowledge graph tool for the research automation pipeline. Binary at `scripts/kg_tool/target/release/kg_tool`.

## DB Location
- Symlink: `/Users/hiyenwong/wiki/kg.db` → `~/.openclaw/workspace/kg.db`
- SQLite database with tables: `kg_entities`, `kg_relations`, `kg_vectors`

## Commands

### Import Paper
```bash
kg_tool import-paper --title "<title>" --url "<url>" [--abstract "<text>"] [--authors "<text>"]
```
- `--url` must be unique (SQLite UNIQUE constraint)
- Returns "Imported: <truncated title>"

### Generate Embeddings
```bash
kg_tool generate-embeddings
```
- Generates vectors for entities without them
- Returns "All entities already have embeddings." if complete

### Search
```bash
kg_tool search --query "<query>" --limit <n>
```
- Vector similarity search against kg_vectors
- Returns ranked list of matching entities

### PageRank
```bash
kg_tool pagerank --limit <n>
```
- Computes PageRank on kg_relations graph
- Returns top N entities by importance score

### Community Detection
```bash
kg_tool communities --limit <n>
```
- Louvain community detection on knowledge graph
- Returns top N communities with entity counts

### Stats
```bash
kg_tool stats
```
- Shows entity count, relation count, vector count
- Note: "Papers: 0" is normal if arxiv_papers table not created

## Schema
```sql
kg_entities: id, title, url (UNIQUE), content, authors, published_date, category, source, created_at, updated_at
kg_relations: source (INT), target (INT), type (TEXT), weight (REAL)
kg_vectors: id, entity_id (FK), vector_data (BLOB), created_at
```

## Relation Types
- `related` — general similarity/topic overlap
- `category_overlap` — shared arXiv categories
- `related_topic` — explicit topic relationship
