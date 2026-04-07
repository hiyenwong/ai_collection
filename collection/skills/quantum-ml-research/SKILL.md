---
name: quantum-ml-research
description: Quantum Machine Learning research assistant. Searches arxiv for quantum ML papers, analyzes patterns from knowledge graph (kg.db), extracts concepts from quantum circuits, neural networks, and finance applications. Use when researching quantum computing applications, quantum algorithms, quantum portfolio optimization, quantum Monte Carlo, quantum neural networks, or analyzing quantum ML literature. Activation: quantum ML research, quantum machine learning, quantum circuit learning, quantum neural network, 量子机器学习, quantum finance research.
---

# Quantum Machine Learning Research

Research assistant for quantum computing applications in machine learning and finance.

## Activation Keywords

- quantum ML research
- quantum machine learning
- quantum circuit learning
- quantum neural network
- quantum portfolio optimization
- quantum Monte Carlo
- quantum algorithms
- 量子机器学习
- 量子神经网络

## Tools Used

- `exec`: Run kg_tool CLI, Python scripts for arxiv search
- `read`: Load skill files, analyze papers
- `web_search`: Search for quantum ML papers
- `sqlite3`: Query knowledge graph (kg.db)

## Workflow

### Step 1: Search Literature

```python
# arxiv quantum ML search
url = 'http://export.arxiv.org/api/query?search_query=ti:quantum+machine+learning&max_results=10&sortBy=relevance'
```

Categories to search:
- `quant-ph` - Quantum Physics
- `cs.LG` - Machine Learning
- `cs.NE` - Neural and Evolutionary Computing

### Step 2: Analyze Knowledge Graph

```bash
# kg.db queries
kg_tool pagerank kg.db          # Find important topics
kg_tool louvain kg.db           # Detect research clusters
kg_tool search kg.db quantum    # Find quantum-related entities
```

Key entities to look for:
- `quantum algorithms` (topic)
- `quantum portfolio optimization` (keyword)
- `quantum Monte Carlo` (keyword)
- `quantum circuit` (keyword)

### Step 3: Extract Patterns

From quantum ML papers, extract:
1. **Quantum Circuit Architecture**: Gate types, circuit depth, qubit count
2. **Learning Paradigm**: Variational quantum eigensolver, QAOA, quantum annealing
3. **Application Domain**: Finance, chemistry, optimization, simulation
4. **Performance Metrics**: Quantum advantage, error rates, speedup factor

### Step 4: Synthesize Insights

Generate summary including:
- Key research themes (PageRank top topics)
- Research clusters (Louvain communities)
- Emerging trends (recent arxiv papers)
- Practical applications (finance, optimization)

## Key Research Areas

### Quantum Circuit Learning

Papers focus on:
- Parameterized quantum circuits as neural networks
- Structure optimization for shallow circuits
- Quantum circuit optimization with RL
- Framework-agnostic quantum ML

### Quantum Finance

Applications:
- Portfolio optimization (QAOA, quantum annealing)
- Risk analytics (quantum Monte Carlo)
- Derivative pricing
- Option pricing

### Quantum Monte Carlo

Use cases:
- Financial risk metrics (VaR)
- Symmetry-resolved entanglement detection
- Ground state observables
- Circuit depth optimization

## Output Format

```markdown
# Quantum ML Research Summary

## Top Research Themes (PageRank)
1. {topic1} - {score}
2. {topic2} - {score}

## Research Clusters (Louvain)
- Cluster A: {papers} - {theme}
- Cluster B: {papers} - {theme}

## Recent Papers (arxiv)
- {paper1}: {title}
- {paper2}: {title}

## Key Insights
- {insight1}
- {insight2}
```

## Related Skills

- `arxiv-search`: General arxiv search
- `skill-extractor`: Extract patterns from papers
- `stock-analysis`: Financial analysis (complements quantum finance)

## Notes

- Proxy may be needed for arxiv API (http://127.0.0.1:7890)
- kg.db location: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- kg_tool: `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool`