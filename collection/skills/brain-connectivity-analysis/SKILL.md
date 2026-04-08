---
name: brain-connectivity-analysis
version: v1.0.0
last_updated: 2026-04-06
description: Brain network connectivity analysis using knowledge graph tools. Analyze brain connectivity patterns, neural networks, and graph-based brain models. Use when working with brain graphs, connectivity matrices, neural network analysis, or integrating neuroscience papers into knowledge graphs. Supports PageRank for important nodes, Louvain community detection, and similarity search for related research.
---

# Brain Connectivity Analysis

## Overview

Brain connectivity analysis skill enables graph-based analysis of brain networks, neural connectivity patterns, and neuroscience research integration. Combines knowledge graph tools with neuroscience domain knowledge for systematic brain network analysis.

## Activation Keywords

- brain connectivity
- 脑连接
- brain network
- 脑网络
- neural connectivity
- 神经连接
- graph analysis brain
- 知识图谱 脑网络
- PageRank brain
- Louvain brain
- brain graph analysis

## Workflow

### Step 1: Import Neuroscience Papers

Import brain connectivity papers to knowledge graph:

```python
# Example: Import arxiv papers to kg.db
import sqlite3
import json

conn = sqlite3.connect('kg.db')
cursor = conn.cursor()

paper = {
    'title': 'Brain connectivity paper title',
    'arxiv_id': '1234.5678',
    'authors': ['Author1', 'Author2'],
    'abstract': 'Paper abstract...',
    'category': 'neuroscience'
}

cursor.execute('''
    INSERT INTO kg_entities (entity_type, name, properties)
    VALUES (?, ?, ?)
''', ('paper', paper['title'], json.dumps(paper)))
```

### Step 2: Generate Vector Embeddings

Generate embeddings for similarity search:

```bash
# Use kg_tool similar command
./scripts/kg_tool/target/release/kg_tool similar kg.db <entity_id> 5
```

### Step 3: Run Graph Analysis

**PageRank for important nodes:**
```bash
./scripts/kg_tool/target/release/kg_tool pagerank kg.db
```

**Louvain community detection:**
```bash
./scripts/kg_tool/target/release/kg_tool louvain kg.db
```

**BFS traversal:**
```bash
./scripts/kg_tool/target/release/kg_tool bfs kg.db <start_id> <depth>
```

### Step 4: Analyze Connectivity Patterns

Extract patterns from papers:
- **Spiking neural networks**: Event-driven computation
- **Brain connectivity matrices**: Graph representation
- **Neural dynamics**: Temporal patterns
- **Synaptic plasticity**: Learning mechanisms

### Step 5: Generate Insights

Summarize findings:
- Top PageRank entities (key research topics)
- Community clusters (research domains)
- Similar papers (related work)
- Extracted patterns (reusable skills)

## Tools Used

- **kg_tool**: Knowledge graph CLI tool at `scripts/kg_tool/target/release/kg_tool`
- **sqlite3**: Database operations for kg.db
- **arxiv API**: Paper search via `http://export.arxiv.org/api/query`
- **kg.db**: Knowledge graph database at workspace root

## Common Commands

```bash
# Statistics
./scripts/kg_tool/target/release/kg_tool stats kg.db

# List entities
./scripts/kg_tool/target/release/kg_tool list kg.db

# Text search
./scripts/kg_tool/target/release/kg_tool search kg.db "brain"

# Similarity search
./scripts/kg_tool/target/release/kg_tool similar kg.db <id> 5
```

## Key Papers

Reference papers in kg.db:
- `Disentangling Brain Graphs: A Note on the Conflation of Network and Connectivity Analyses`
- `Training a Hidden Markov Model with a Bayesian Spiking Neural Network`
- `NeuroCoreX: FPGA-Based Spiking Neural Network Emulator`

## Instructions for Agents

### Step 1: Import Papers to Knowledge Graph
Add brain connectivity papers: `kg_tool add-entity kg.db paper <arxiv_id>`

### Step 2: Generate Embeddings
Run `kg_tool similar` to find related work and generate vector embeddings.

### Step 3: Run Graph Analysis
- PageRank for important nodes: `kg_tool pagerank kg.db`
- Louvain for community detection: `kg_tool louvain kg.db`
- BFS traversal: `kg_tool bfs kg.db <start_id> <depth>`

### Step 4: Extract and Report Patterns
Summarize top papers, connectivity patterns, and research clusters.

## Examples

### Example 1: Analyze Brain Network Papers

```
User: "Analyze brain connectivity papers in the knowledge graph"

Agent:
1. Run `kg_tool stats kg.db` to see current entities
2. Execute PageRank to find most influential papers
3. Run Louvain to identify research clusters
4. Summarize top papers and connectivity patterns
```

### Example 2: Find Related Research

```
User: "Find papers similar to spiking neural networks in brain connectivity"

Agent:
1. Search kg.db: `kg_tool search kg.db "spiking"`
2. Run similarity search on top result entity IDs
3. Extract BFS traversal for related papers
4. Report research clusters and key findings
```

## Related Skills

- **spiking-neural-network**: SNN training and simulation
- **neuromorphic-hardware**: FPGA and neuromorphic chips
- **brain-network-controllability**: Control theory for brain networks
- **kg Tool**: `~/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool`

## References

See `references/brain_connectivity_methods.md` for detailed analysis methods.
