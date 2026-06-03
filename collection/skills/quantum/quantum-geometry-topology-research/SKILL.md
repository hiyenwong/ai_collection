---
name: quantum-geometry-topology-research
description: "Research skill for quantum-geometry-topology interdisciplinary analysis. Search arxiv for quantum geometry/topology papers, import to knowledge graph (kg.db), analyze with PageRank/Louvain, extract reusable patterns. Activation: quantum geometry research, quantum topology analysis, geometry-informed quantum computing, quantum statistical analysis."
---

# Quantum-Geometry-Topology Research Skill

Cross-disciplinary research workflow for quantum mechanics + geometry + topology + statistics.

## Activation Keywords
- quantum geometry research
- quantum topology analysis
- geometry-informed quantum computing
- quantum statistical analysis
- topology quantum information
- quantum Fisher information
- Born rule statistics
- quantum probability
- 拓扑量子研究
- 量子几何分析

## Tools Used
- exec: Run kg_tool, Python scripts, arxiv search
- read: Load existing skills, scripts
- write: Create new skills, save results
- web_search: Search arxiv papers

## Workflow

### Step 1: Search Papers

Search arxiv for quantum-geometry-topology cross-disciplinary papers:

```bash
python3 scripts/search_today_topic.py
# Keywords: quantum geometry, topology, Fisher information, Born rule, statistics
```

### Step 2: Import to Knowledge Graph

Import papers to kg.db:

```bash
python3 scripts/import_arxiv_to_kg.py kg.db <papers_json>
```

### Step 3: Generate Vector Embeddings

```bash
python3 scripts/generate_vectors.py
```

### Step 4: Graph Analysis

Run PageRank and Louvain:

```bash
./scripts/kg_tool/target/release/kg_tool pagerank kg.db
./scripts/kg_tool/target/release/kg_tool louvain kg.db
./scripts/kg_tool/target/release/kg_tool search kg.db "quantum"
```

### Step 5: Pattern Extraction

Identify reusable patterns:
- Quantum Fisher information geometry applications
- Topological quantum state encoding
- Quantum probability for statistics/ML
- Geometry-aware quantum circuit design

### Step 6: Create Skill

Use skill-creator to formalize patterns:

```markdown
Skill candidates:
- quantum-fisher-information-analysis
- topological-quantum-encoding
- quantum-probability-statistics
```

## Key Concepts

### Quantum Fisher Information Geometry
- Geometric viewpoint on quantum states
- Information geometry for quantum estimation
- Bloch sphere differential geometry

### Topological Quantum Computing
- Toric code, loop gases, string nets
- Topological quantum memories
- Quantum Hall effects

### Quantum Probability for Statistics
- Born rule applications
- Kolmogorov vs quantum probability
- Machine learning connections

## Output Format

```markdown
# Research Analysis Summary

## Papers Imported
- Title | arXiv ID | Key Contribution

## Graph Analysis
- PageRank top papers: [IDs]
- Communities detected: [N clusters]
- Cross-domain connections: [topics]

## Extracted Patterns
1. Pattern Name: [description]
2. Pattern Name: [description]

## Skill Recommendations
- [skill-name]: [purpose]
```

## Resources
- kg.db: /Users/hiyenwong/wiki/kg.db
- kg_tool: scripts/kg_tool/target/release/kg_tool
- Papers: scripts/arxiv_*.json

## Related Skills
- skill-creator: Create new skills from patterns
- skill-extractor: Extract patterns from conversations
- arxiv-search: Paper search

## Examples

### Example 1: Using this skill
```
User: [Request related to this skill's domain]
Agent: [Applies skill knowledge to help user]
```
