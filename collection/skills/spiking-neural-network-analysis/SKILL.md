---
name: spiking-neural-network-analysis
version: v1.0.0
last_updated: 2026-04-06
description: Analyze Spiking Neural Network (SNN) papers, extract technical patterns from knowledge graph, and identify reusable research methodologies for neuromorphic computing.
---

# Spiking Neural Network Analysis

Analyze SNN research papers from knowledge graph and extract reusable technical patterns.

## Activation Keywords

- spiking neural network
- SNN analysis
- 脉冲神经网络分析
- spiking neuron
- neuromorphic computing
- SNN papers

## Tools Used

- `exec` - Run kg_tool and sqlite3 commands
- `read` - Read skill docs and paper content
- `write` - Save analysis reports

## Workflow Decision Tree

```
User Request → Identify Task Type
├── Search Papers → Search kg.db for SNN papers
├── Analyze Patterns → Extract technical patterns
├── Knowledge Graph → Run PageRank/Louvain/Similarity
└── Generate Report → Create analysis summary
```

## Core Commands

### Step 1: Search SNN Entities

```bash
# Search knowledge graph
sqlite3 /Users/hiyenwong/.openclaw/workspace/kg.db \
  "SELECT id, name FROM kg_entities WHERE name LIKE '%spiking%' OR name LIKE '%neuromorphic%'"
```

### Step 2: Get Paper Details

```bash
# Get paper properties (keywords, topics, category)
sqlite3 /Users/hiyenwong/.openclaw/workspace/kg.db \
  "SELECT id, name, properties FROM kg_entities WHERE entity_type='paper' AND name LIKE '%spiking%'"
```

### Step 3: Knowledge Graph Analysis

```bash
# PageRank
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool pagerank \
  --db /Users/hiyenwong/.openclaw/workspace/kg.db

# Louvain community detection
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool louvain \
  --db /Users/hiyenwong/.openclaw/workspace/kg.db

# Vector similarity
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool similar \
  --db /Users/hiyenwong/.openclaw/workspace/kg.db <entity_id>
```

### Step 4: Extract Technical Patterns

Common SNN patterns:
- **energy-efficient** - Energy optimization
- **brain-inspired** - Biological inspiration
- **forward-forward** - Biologically plausible learning
- **backpropagation-free** - No backpropagation
- **temporal dynamics** - Time-series processing
- **low-latency** - Fast inference

## Instructions for Agents

Follow these steps to analyze SNN papers:
1. Identify the user's task type (search, pattern extraction, knowledge graph analysis, or report generation)
2. Use the Workflow Decision Tree to select the appropriate path
3. Execute the Core Commands in order
4. Present results using the format shown in Usage Examples

## Usage Examples

### Example 1: Basic Analysis

```
User: "分析 SNN 论文"

Execute:
1. Search "spiking neural" papers
2. Get Top 5 paper properties
3. Run pagerank
4. Extract patterns
5. Generate report
```

### Example 2: Pattern Extraction

```
User: "从 SNN 论文中提取技术模式"

Execute:
1. List all SNN papers
2. Parse keywords from properties
3. Identify common patterns
4. Create pattern summary
```

### Example 3: Cross-domain Analysis

```
User: "找出与 SNN 相关的量子计算论文"

Execute:
1. Search "spiking" AND "quantum"
2. Find intersection entities
3. Analyze hybrid approaches
```

## Key Findings from Analysis

### Top SNN Papers in KG

| Paper | Category | Pattern |
|-------|----------|---------|
| Energy-Efficient SNN | Medical AI | energy-efficient |
| Brain-Inspired Computing | Neuromorphic | brain-inspired |
| PSPM (Pre-Synaptic Pool) | Supervised Learning | forward-forward |

### SNN-Quantum Intersection

- Hybrid spiking-quantum CNN
- Quantum memristor for brain computing
- Neural operator quantum states

## Related Skills

- `brain-connectivity-analysis` - Brain network analysis
- `quantum-neural-hybrid` - Quantum-classical NN
- `quantized-snn-hardware-optimization` - Hardware acceleration

## Limitations

- Requires kg.db with SNN papers
- Vector embeddings needed for similarity search
- Manual pattern interpretation

## Resources

- Knowledge Graph: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- KG Tool: `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool`
- Daily Research: `memory/2026-04-06.md`