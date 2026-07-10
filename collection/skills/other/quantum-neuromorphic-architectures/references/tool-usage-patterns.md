# Tool Usage Patterns for Quantum-Neuromorphic Research

## arXiv API Access
- **Critical**: arXiv API now returns 301 redirect from HTTP to HTTPS
- Use `curl -sL` (follow redirects) not just `curl -s`
- URL format: `https://export.arxiv.org/api/query?search_query=all:"{terms}"&sortBy=submittedDate&sortOrder=descending&max_results={N}`

## kg_tool Commands (Knowledge Graph CLI)
```bash
KG_DB_PATH=/path/to/kg.db python3 scripts/kg_tool/target/release/kg_tool <command>
```
Commands: `import-paper`, `generate-embeddings`, `search`, `pagerank`, `communities`, `stats`

### import-paper
```bash
kg_tool import-paper --title "..." --url "..." --abstract "..." --authors "..."
```

### search
```bash
kg_tool search --query "quantum neuromorphic" --limit 5
```

### pagerank
```bash
kg_tool pagerank --limit 10
```

### communities (uses union-find, not Louvain)
```bash
kg_tool communities --limit 10
```

### stats
```bash
kg_tool stats
# Output: Entities, Relations, Vectors, Papers counts
```

## Environment Variables
- `KG_DB_PATH` overrides default `/Users/hiyenwong/wiki/kg.db`
- DB locations found: `~/.openclaw/workspace/kg.db`, `~/.openclaw/workspace/memory/kg.db`, `~/wiki/kg.db`
