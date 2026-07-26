# kg_tool Verified Commands

Verified on 2026-05-12 by actually running each command against the production database.

## Binary Path
```
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool
```

## Database Path
```
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/kg.db
```
Note: kg_tool has its database path compiled in. There is NO `--db` flag.

## Available Commands (verified)

### search
```bash
kg_tool search --query 'quantum machine learning'
```
Output format: `[id] Title (categories)`
Works. Returns results ranked by vector similarity.

### pagerank
```bash
kg_tool pagerank --limit 10
```
Output format: `Top 10 entities by PageRank: [id] Title  PR=0.xxxx`
Works. Returns entities ranked by PageRank algorithm.

### stats
```bash
kg_tool stats
```
Output format: `Entities: N\nRelations: N\nVectors: N\nPapers: N (arxiv_papers table not created yet)`
Works. Returns database statistics.

## Commands That DON'T Exist

- `kg_tool louvain` → "Unknown command: louvain"
- `kg_tool embed` → "Unknown command: embed"  
- `kg_tool list` → "Unknown command: list"
- `kg_tool --help` → "Unknown command: --help"
- `kg_tool help` → "Unknown command: help"

## Key Takeaway

Only **3 commands** are available: `search`, `pagerank`, `stats`. 
Any documentation claiming louvain, embed, list, or help commands is outdated or aspirational.
For community detection or embedding generation, use direct sqlite3 + Python instead.
