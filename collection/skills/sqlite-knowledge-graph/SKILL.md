---
name: sqlite-knowledge-graph
version: 0.5.0
last_updated: 2026-03-25
description: SQLite-based lightweight graph database with RAG and graph algorithms. Use when working with knowledge graphs, graph traversal, community detection, or semantic search.
---

# SQLite Knowledge Graph

## Description

A lightweight graph database built as a SQLite extension, supporting:
- **Entity/Relation Storage** - Nodes and edges with metadata
- **Graph Traversal** - BFS, DFS, shortest path
- **Graph Algorithms** - PageRank, Louvain, Connected Components
- **Vector Search** - Semantic similarity with embeddings
- **RAG Integration** - Knowledge graph-enhanced retrieval

## Activation Keywords

- sqlite knowledge graph
- sqlite-kg
- graph database
- knowledge graph
- pagerank
- louvain
- community detection
- graph traversal

## Installation

```bash
cd ~/.openclaw/workspace/projects/sqlite-knowledge-graph-gh
cargo build --release
```

## CLI Usage

### Basic Commands

```bash
# Migrate data from knowledge.db
sqlite-kg migrate --source ~/.openclaw/workspace/knowledge/knowledge.db

# Search entities
sqlite-kg search --query "neural network" --top-k 10

# Graph statistics
sqlite-kg stats

# Find shortest path
sqlite-kg path --from 123 --to 456 --max-depth 5

# PageRank analysis
sqlite-kg pagerank --top-k 20

# Community detection
sqlite-kg louvain

# Connected components
sqlite-kg components
```

## Programmatic API

```rust
use sqlite_knowledge_graph::{KnowledgeGraph, PageRankConfig, Direction};

// Open database
let kg = KnowledgeGraph::open("knowledge.db")?;

// Create entities
let id1 = kg.insert_entity(&Entity::new("paper", "Neural Networks Paper"))?;
let id2 = kg.insert_entity(&Entity::new("skill", "neural-networks"))?;

// Create relation
kg.insert_relation(&Relation::new(id1, id2, "derived_from", 0.9)?)?;

// Graph traversal
let neighbors = kg.get_neighbors(id1, 2)?;
let path = kg.kg_shortest_path(id1, id2, 5)?;

// Graph algorithms
let pagerank = kg.kg_pagerank(None)?;
let communities = kg.kg_louvain()?;
let components = kg.kg_connected_components()?;

// Full analysis
let analysis = kg.kg_analyze()?;
```

## Available Functions

### Entity Operations

| Function | Description |
|----------|-------------|
| `insert_entity()` | Create new entity |
| `get_entity()` | Get entity by ID |
| `list_entities()` | List with optional filter |
| `update_entity()` | Update entity properties |
| `delete_entity()` | Delete entity |

### Relation Operations

| Function | Description |
|----------|-------------|
| `insert_relation()` | Create relation between entities |
| `get_neighbors()` | BFS traversal from entity |

### Graph Traversal

| Function | Description |
|----------|-------------|
| `kg_bfs_traversal()` | Breadth-first search |
| `kg_dfs_traversal()` | Depth-first search |
| `kg_shortest_path()` | Find shortest path |
| `kg_graph_stats()` | Get graph statistics |

### Graph Algorithms

| Function | Description |
|----------|-------------|
| `kg_pagerank()` | Compute centrality scores |
| `kg_louvain()` | Detect communities |
| `kg_connected_components()` | Find connected components |
| `kg_analyze()` | Full graph analysis |

### RAG Functions

| Function | Description |
|----------|-------------|
| `kg_semantic_search()` | Vector similarity search |
| `kg_get_context()` | Get entity context |
| `kg_hybrid_search()` | Semantic + graph search |

## When to Use

- Building knowledge graphs
- Graph-based RAG systems
- Community detection in networks
- Centrality analysis
- Path finding in relational data
- Semantic search with graph context

## Example: Knowledge Graph Analysis

```bash
# Analyze your knowledge base
sqlite-kg analyze

# Output:
# Total entities: 2,619
# Total relations: 1,480,951
# Top PageRank entities:
#   1. arxiv:2305.01666 (0.045)
#   2. arxiv:2501.11407 (0.038)
# Communities found: 12
# Largest community: 847 entities
```

## Related Skills

- `memory-retrieval` - For semantic memory search
- `skill-rag-indexer` - For skill RAG indexing
- `indexed-memory` - For memory indexing

## Repository

https://github.com/hiyenwong/sqlite-knowledge-graph

## License

MIT