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

## Instructions for Agents

### Step 1: Search Quantum ML Literature
Use arxiv API to find recent papers on quantum machine learning topics.

### Step 2: Import to Knowledge Graph
Add papers to kg.db with proper entity types and relationships.

### Step 3: Analyze Graph Structure
Run PageRank and Louvain to identify important topics and research clusters.

### Step 4: Extract Patterns
Identify recurring concepts, algorithms, and applications from the analysis.

### Step 5: Generate Insights
Summarize findings and suggest new research directions or skill creation opportunities.

## Examples

### Example 1: Quantum Portfolio Optimization Research

```
User: "Research quantum methods for portfolio optimization"

Agent:
1. Search arxiv for "quantum portfolio optimization"
2. Import 10 relevant papers to kg.db
3. Run pagerank → QAOA papers most influential
4. Run louvain → 3 research clusters identified
5. Extract pattern: QAOA + VQE hybrid approaches trending
6. Suggest: Create quantum-portfolio-optimizer skill
```

### Example 2: Quantum Neural Network Survey

```
User: "Survey quantum neural network architectures"

Agent:
1. Search arxiv for "quantum neural network"
2. Import papers from 2024-2025
3. Analyze with kg_tool: find top authors, key techniques
4. Identify patterns: variational circuits, quantum kernels
5. Report: Current state and future directions
```

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