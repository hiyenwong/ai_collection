---
name: graph-pooling-node-features
description: Analyze and optimize graph pooling operations by examining the interaction between node features and graph topology. Ensures effective pooling in GNN-based graph classification.
---

# Graph Pooling Node Feature Alignment

## Description
Framework for analyzing and optimizing graph pooling operations by examining the alignment between node features and graph topology. Reveals that pooling operators require node features well-aligned with graph topology — a condition often overlooked in empirical networks. Based on arXiv:2605.06250 "The Role of Node Features in Graph Pooling".

## Activation Keywords
- graph pooling
- node feature alignment
- GNN pooling optimization
- graph classification pooling
- WL-1 expressivity
- graph topology features

## Instructions for Agents

### Step 1: Identify Pooling Ineffectiveness
Signs that pooling is not effective:
- Marginal or inconsistent gains over standard WL-1 expressive GNNs
- Pooling operator fails to improve graph classification accuracy
- Pooling produces representations that lose important structural information

### Step 2: Analyze Node Feature Alignment
Check if node features are well-aligned with graph topology:
- Compute alignment metric between node features and topological structure
- Identify nodes whose features don't correspond to their structural role
- Quantify the degree of misalignment

### Step 3: Formalize Pooling Requirements
For effective pooling, node features must satisfy:
- **Topology Alignment**: Features should reflect the node's structural position
- **Homophily Consistency**: Similar features should correspond to similar structural roles
- **Pooling Objective Compatibility**: Features should support the specific pooling objective (e.g., cluster identification, coarsening)

### Step 4: Apply Alignment Remediation
If features are misaligned:
- **Feature Engineering**: Incorporate structural information (degree, centrality, role-based features)
- **Feature Transformation**: Learn feature mappings that better align with topology
- **Structure-Aware Pooling**: Use pooling operators that jointly consider features and topology

### Step 5: Quantify Improvement
Measure the improvement using:
- Alignment score before and after remediation
- Pooling effectiveness on downstream tasks
- Comparison with baseline WL-1 GNN performance

## Key Concepts
- **WL-1 Expressivity**: Weisfeiler-Lehman graph isomorphism test — baseline for GNN expressiveness
- **Feature-Topology Alignment**: Degree to which node features reflect the graph's structural organization
- **Pooling Objective**: The goal of pooling (e.g., identify clusters, reduce graph size while preserving information)
- **Empirical Networks**: Real-world graphs where features and topology may not be naturally aligned

## Best Practices
1. Always check feature-topology alignment before applying pooling
2. Use the quantitative alignment measure to diagnose pooling failures
3. When features are misaligned, incorporate structural features before pooling
4. Don't assume pooling will automatically help — validate empirically

## Pitfalls
- Pooling may hurt performance if features are poorly aligned with topology
- Simply increasing model capacity won't fix alignment issues
- Different pooling operators have different alignment requirements

## Related Skills
- brain-graph-neural: For brain network GNN applications
- gnn-transformer-fusion: For multimodal graph-neural architectures
