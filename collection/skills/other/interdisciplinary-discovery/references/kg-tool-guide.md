# kg_tool CLI Guide

Complete guide for using the sqlite-knowledge-graph CLI tool.

## Available Commands

```bash
kg_tool <command> <db_path> [args]
```

### Statistics & Query
```bash
kg_tool stats kg.db                 # Graph overview
kg_tool list kg.db [type]           # List entities (limit 20)
kg_tool search kg.db "query"        # Text search
```

### Graph Analysis
```bash
kg_tool pagerank kg.db              # PageRank algorithm
kg_tool louvain kg.db               # Community detection
kg_tool bfs kg.db <start_id> [depth] # BFS traversal
```

### Vector Operations
```bash
kg_tool similar kg.db <entity_id> [k]  # Find similar entities
```

## Command Details

### pagerank
Returns top 10 entities by PageRank score.

**Output format:**
```
PageRank Results (top 10):
  Entity 343: 0.045202
  Entity 342: 0.015659
  ...
```

**Interpretation:**
- Higher score = more influential in the graph
- Topic entities often have highest scores
- Cross-domain entities bridge communities

### louvain
Community detection using Louvain algorithm.

**Output format:**
```
Community Detection (Louvain):
  Entity 1 -> Community 0
  Entity 2 -> Community 1
  ...
```

**Interpretation:**
- Same community = related research area
- Different communities = separate domains
- Check for cross-community connections

### similar
Vector similarity search (cosine similarity).

**Parameters:**
- `entity_id`: Entity with existing vector embedding
- `k`: Number of similar entities to return (default 5)

**Output format:**
```
Entities similar to 128 (top 5):
  [169] quantum economics (0.8764)
  [333] Quantum Economics (0.8764)
  ...
```

**Interpretation:**
- Similarity >0.8: Strong connection, likely same domain
- Similarity 0.5-0.8: Moderate connection, related concepts
- Similarity <0.5: Weak connection, may indicate bridge entity

### search
Text-based search on entity names.

**Example:**
```bash
kg_tool search kg.db "quantum"
```

Returns all entities containing "quantum" in name.

## Database Schema

### kg_entities
```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY,
    entity_type TEXT NOT NULL,  -- paper, topic, keyword, author
    name TEXT NOT NULL,
    properties TEXT,            -- JSON metadata
    created_at INTEGER,
    updated_at INTEGER
);
```

### kg_vectors
```sql
CREATE TABLE kg_vectors (
    entity_id INTEGER PRIMARY KEY,
    vector BLOB                  -- 768-dimensional float array
);
```

### kg_relations
```sql
CREATE TABLE kg_relations (
    id INTEGER PRIMARY KEY,
    source_id INTEGER,
    target_id INTEGER,
    relation_type TEXT,
    weight REAL
);
```

## Direct SQLite Queries

When kg_tool doesn't support needed operations:

### Check vector existence
```sql
SELECT entity_id FROM kg_vectors 
WHERE entity_id IN (
    SELECT id FROM kg_entities 
    WHERE name LIKE '%quantum%'
);
```

### Get entity details
```sql
SELECT id, entity_type, name, properties 
FROM kg_entities WHERE id = 343;
```

### Count statistics
```sql
SELECT COUNT(*) FROM kg_entities;
SELECT COUNT(*) FROM kg_vectors;
SELECT entity_type, COUNT(*) FROM kg_entities GROUP BY entity_type;
```

## Troubleshooting

### Database locked
```
Error: stepping, database is locked (5)
```
**Solution:** Wait for other processes to complete, or use `sleep 2` before retry.

### Invalid column type
```
Error: InvalidColumnType(3, "properties", Null)
```
**Solution:** Entity has NULL properties. Query different columns.

### Unknown command
```
Unknown command: add-entity
```
**Solution:** kg_tool has limited commands. Use sqlite3 for insertions.

## Best Practices

1. **Always start with stats** - Check graph health
2. **Use pagerank first** - Find important nodes before deep analysis
3. **Cross-reference results** - Compare PageRank with similarity
4. **Handle locks gracefully** - Add delays between write operations
5. **Document findings** - Save to memory/ directory

## Integration with Research Workflow

### Typical sequence:
```bash
# 1. Check graph status
kg_tool stats kg.db

# 2. Find important entities
kg_tool pagerank kg.db

# 3. Find communities
kg_tool louvain kg.db

# 4. Search specific domain
kg_tool search kg.db "quantum"

# 5. Find cross-domain connections
kg_tool similar kg.db <high_pagerank_entity> 10
```

### Example session:
```bash
$ kg_tool pagerank kg.db
Entity 343: Quantum Algorithms (0.045)

$ kg_tool search kg.db "quantum finance"
Entity 128: quantum finance

$ kg_tool similar kg.db 128 5
quantum economics (0.87)  # Strong connection!

# Document: Found quantum-finance interdisciplinary link
```