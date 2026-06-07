---
name: quantum-neural-topology
description: "Research skill for quantum neural networks and topological field theory - combines quantum computing, neural architecture, and topological mathematics. Use when: (1) Analyzing quantum ML patterns, (2) Synthesizing quantum-neural research, (3) Exploring topological neural architectures, (4) Identifying quantum stability mechanisms, (5) Creating quantum-classical hybrid frameworks. Keywords: quantum neural, quantum topology, QML research, topological neural, quantum architecture, 量子神经网络, 拓扑神经网络."
---

# Quantum Neural Network & Topological Field Theory Research Skill

Research skill for exploring the intersection of quantum computing, neural networks, and topological mathematics. Synthesizes insights from quantum machine learning (QML), neural network field theory, and topological effects to identify emerging patterns and create actionable research frameworks.

## Research Workflow

### Phase 1: Knowledge Graph Analysis

**Step 1: Extract Relevant Papers**
```bash
sqlite3 kg.db "
SELECT id, name, properties 
FROM kg_entities 
WHERE entity_type = 'paper' 
AND (
  name LIKE '%quantum%' 
  OR name LIKE '%neural%'
  OR name LIKE '%topological%'
  OR properties LIKE '%quantum%'
)
ORDER BY created_at DESC 
LIMIT 20;
"
```

**Step 2: PageRank Analysis**
```bash
kg_tool pagerank kg.db
```
Identify most influential papers/topics in quantum-neural domain.

**Step 3: Vector Similarity Search**
```bash
kg_tool similar kg.db [entity_id] 15
```
Find related papers through semantic similarity.

**Step 4: Community Detection**
```bash
kg_tool louvain kg.db
```
Identify research clusters and collaboration patterns.

### Phase 2: Pattern Extraction

**Analyze common patterns across papers:**

| Pattern Type | Indicators | Example Papers |
|--------------|------------|----------------|
| **Quantum Stability** | barren plateaus, expressivity, gradient vanishing | LieTrunc-QNN, Neural Operator Quantum State |
| **Topological Effects** | discrete parameters, field ensemble, manifold | Topological Effects in Neural Network Field Theory |
| **Quantum-Classical Hybrid** | spiking-quantum, federated learning, photonic | QEEGNet, Quantum photonic neural networks |
| **Resource Optimization** | parameter efficiency, error correction, circuit depth | Understanding Resource Cost in QFL |

### Phase 3: Synthesis Framework

**Create synthesis template:**

```markdown
# Quantum Neural Topology Research Synthesis

## Core Theme
[Identified pattern from analysis]

## Key Theoretical Contributions
1. [From PageRank top entities]
2. [From community detection clusters]
3. [From similarity search chains]

## Practical Applications
1. [Extract from paper abstracts]
2. [Identify use cases]
3. [Map to real-world problems]

## Research Gaps
- [Identified from community boundaries]
- [Missing connections in similarity graph]

## Actionable Framework
- [Step-by-step methodology derived from patterns]
```

### Phase 4: Skill Creation

**If pattern is reusable:**
1. Extract core methodology
2. Create SKILL.md with research workflow
3. Add examples from analyzed papers
4. Document theoretical background
5. Store in collection/skills/

## Usage Patterns

### Pattern 1: Quantum Neural Stability Research
```
Analyze quantum neural network stability patterns:
1. Use kg_tool to find QML papers
2. Run PageRank to identify key theoretical papers
3. Extract stability mechanisms (Lie algebra truncation, error correction)
4. Synthesize stability framework
```

### Pattern 2: Topological Field Theory Analysis
```
Explore topological effects in neural networks:
1. Search for "topological neural" papers
2. Find similarity clusters
3. Extract discrete parameter patterns
4. Map topological invariants to neural architectures
```

### Pattern 3: Quantum-Classical Hybrid Design
```
Synthesize quantum-classical hybrid architectures:
1. Identify hybrid papers from communities
2. Analyze integration patterns
3. Extract performance trade-offs
4. Create design guidelines
```

## Pattern Recognition Guide

**Look for these quantum-neural patterns:**

| Pattern | Keywords | Significance |
|---------|----------|--------------|
| Expressivity Phase Transition | "phase transition", "expressivity" | Quantum vs classical capacity |
| Topological Protection | "topological", "invariant", "manifold" | Robustness mechanism |
| Gradient Landscape | "barren plateau", "gradient vanishing" | Optimization challenge |
| Circuit Efficiency | "parameter efficient", "circuit depth" | Resource constraints |
| Hybrid Encoding | "time-bin", "photonic", "spiking" | Implementation strategy |

## Resources

- **Knowledge Graph:** kg.db (sqlite-knowledge-graph)
- **Tool:** scripts/kg_tool/target/release/kg_tool
- **Config:** scripts/weekly_topics.py
- **Memory:** memory/YYYY-MM-DD.md
- **References:** See `references/quantum_patterns.md` for detailed pattern analysis

## Dependencies

```bash
# Required tools
sqlite3
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool
python3 scripts/weekly_topics.py

# Proxy configuration (for arxiv access)
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

## Related Skills

- **arxiv-search:** For paper search
- **skill-extractor:** For pattern extraction
- **skill-creator:** For skill creation
- **knowledge-graph-operations:** For kg.db management