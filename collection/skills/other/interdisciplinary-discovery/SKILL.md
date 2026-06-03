---
name: interdisciplinary-discovery
description: "Discover interdisciplinary research connections using knowledge graph analysis (PageRank, Louvain, vector similarity). Use when analyzing cross-domain research, finding unexpected connections, or exploring interdisciplinary patterns. Keywords: 跨学科发现, interdisciplinary discovery, kg analysis, 知识图谱分析, find research connections, discover cross-domain patterns."
---

# Interdisciplinary Discovery

Discover unexpected research connections across disciplines using knowledge graph analysis.

## Activation Keywords
- 跨学科发现
- interdisciplinary discovery
- 知识图谱分析
- kg analysis
- 找研究关联
- discover cross-domain patterns
- interdisciplinary research
- 知识图谱发现

## Tools Used
- `exec`: Run kg_tool CLI commands
- `sqlite3`: Direct database queries
- `web_search`: Search related papers
- `read`: Load skill references
- `write`: Save analysis results

## Quick Workflow

### 1. Identify Important Nodes
```bash
kg_tool pagerank kg.db
```
Returns top entities by influence.

### 2. Find Research Communities
```bash
kg_tool louvain kg.db
```
Detects clusters of related research.

### 3. Discover Strong Connections
```bash
kg_tool similar kg.db <entity_id> 5
```
Finds entities with high vector similarity (>0.8 = strong connection).

### 4. Analyze Patterns
- PageRank: Domain influence
- Louvain: Research clusters
- Vector similarity: Cross-domain bridges

### 5. Extract Insights
Document findings in `memory/YYYY-MM-DD.md`.

## When to Use

**Trigger signals:**
- User asks "find connections between X and Y"
- Need to explore interdisciplinary patterns
- Research synthesis tasks
- Knowledge graph exploration

**Typical patterns:**
- Quantum finance connections (0.87 similarity)
- Neuroscience-quantum bridges
- AI-physics intersections

## References

- **kg_tool usage**: See [references/kg-tool-guide.md](references/kg-tool-guide.md)
- **Analysis patterns**: See [references/analysis-patterns.md](references/analysis-patterns.md)

## Best Practices

1. **Start with PageRank** - Find influential nodes first
2. **Check multiple entities** - Don't rely on single similarity search
3. **Threshold >0.8** - Strong connections typically have >0.8 similarity
4. **Cross-reference communities** - Compare Louvain results with similarity
5. **Document patterns** - Always save to memory/

## Examples

### Example: Quantum Finance Discovery
```
kg_tool pagerank kg.db
# Entity 343: Quantum Algorithms (0.045)

kg_tool similar kg.db 128 5
# quantum economics (0.8764)
# Quantum Computing for Finance (0.8445)

# Insight: Strong quantum-finance connection discovered
```

### Example: Neuroscience-Quantum Bridge
```
kg_tool similar kg.db 9 5
# Brain connectivity tools (0.1522)
# Spiking neural networks (0.1413)

# Insight: Quantum cryptography linked to neuroscience
```

## Integration with Research Workflow

This skill integrates with:
- `arxiv-search`: Find papers to add to KG
- `skill-extractor`: Extract patterns from discoveries
- `weekly_topics.py`: Daily research automation

## Limitations

- Requires kg.db with vectors (640+ embeddings)
- Similarity search needs entity with existing vector
- Database may be locked during concurrent writes

## Notes

- Part of hourly research automation workflow
- Works best with sqlite-knowledge-graph
- Use proxy for arXiv searches: http://127.0.0.1:7890