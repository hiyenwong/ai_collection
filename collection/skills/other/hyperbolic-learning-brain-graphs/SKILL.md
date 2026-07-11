---
name: hyperbolic-learning-brain-graphs
description: "Hyperbolic Learning on Brain Graphs (HLBG) framework for brain disorder diagnosis. Uses Lorentzian hyperbolic space to model hierarchical relationships among ROIs, functional communities, and whole-brain network. Introduces Graph-aware Mamba (GaMamba) for capturing long-range dependencies while preserving graph topology. SOTA on ABIDE-I (autism) and REST-MDD (depression) datasets. Use when: brain network analysis for disorder diagnosis, hyperbolic graph learning, brain functional connectivity modeling, hierarchical brain network representation, Graph Mamba applications, biomarker identification from fMRI, autism/depression classification from brain graphs. Trigger words: hyperbolic brain graphs, HLBG, GaMamba, Graph-aware Mamba, brain disorder diagnosis, ABIDE, REST-MDD, hierarchical brain network, Lorentzian space, functional connectivity, brain graph classification."
---

# Hyperbolic Learning on Brain Graphs (HLBG)

## Paper

**Title**: Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis
**arXiv**: 2607.07077v1 (2026-07-08)
**Authors**: Yapeng Li, Bo Jiang, Ziyan Zhang, Dongdong Chen, Zhengzheng Tu
**Categories**: cs.CV, cs.AI

## Problem

Functional brain networks exhibit hierarchical organization across ROI, community, and whole-brain levels. Existing methods struggle to:
1. Model ROI→community interactions adequately
2. Capture long-range dependencies between spatially distant ROIs
3. Exploit the intrinsic hierarchical geometry of brain networks

## Solution: HLBG Framework

### Architecture Overview

```
Global Brain Graph (G^g)
         │
         ├── Hierarchical Brain Graph Construction
         │    ├── Global graph: N ROIs, FC matrix, k-strongest connections
         │    └── C community-specific subgraphs (Yeo 7-network parcellation)
         │
         ├── Brain Graph Embedding via GaMamba
         │    ├── Global branch: captures long-range interactions across all nodes
         │    └── C Local branches: extract intra-community features
         │         └── GaMamba: GAT-derived structural prompts → Mamba output matrix
         │
         ├── Hierarchical Brain Representation Learning (HBRL)
         │    ├── Project ROI/community/whole-brain reps into Lorentzian hyperbolic space
         │    └── Two entailment regularization losses constrain hierarchy
         │
         └── Adaptive Fusion → Classification + Biomarker Detection
              └── Self-attention fuses local + global representations
```

### Key Components

#### 1. Hierarchical Brain Graph Construction

- **Global graph**: `G^g = (X, A)` where X from FC matrix rows, A retains k-strongest connections per node
- **Local subgraphs**: Partition by Yeo 7-network functional communities, extract subgraph `(X^i, A^i)` for each community
- **Hierarchical structure**: `H = {G^g, G^1, ..., G^C}`

#### 2. Graph-aware Mamba (GaMamba)

Core innovation: inject graph structure as structural prompt into Mamba's input-dependent readout matrix.

```
S_i = Norm(GAT({u_j}_{j∈N(i)}))  # Structural prompt from GAT
C' = W_c · (C + S)                # Structure-aware output matrix
y_i = C' x_i + D u_i              # Final output
```

- Uses GAT to derive normalized structural prompts from node neighborhoods
- Prompts integrated into Mamba's output matrix C via linear transformation
- Enables simultaneous modeling of sequential dynamics and graph-aware representations

#### 3. Hierarchical Brain Representation Learning (HBRL)

Projects representations into Lorentzian hyperbolic space and imposes two geometric entailment constraints:

- **ROI → Community entailment**: ROI representations must be entailed by their community representations
- **Community → Whole-brain entailment**: Community representations must be entailed by global representations

This captures the one-to-many hierarchical relationships naturally in hyperbolic geometry.

### Results

| Dataset | Task | Performance |
|---------|------|-------------|
| ABIDE-I | ASD classification | SOTA |
| REST-MDD | MDD classification | SOTA |

- Identifies disorder-relevant functional biomarkers
- Outperforms GNN-based methods (BrainGB, IBGNN, BrainGNN)
- Outperforms Transformer-based methods (BrainNetTF, ALTER, Com-BrainTF, CAGT)

## Implementation Patterns

### GaMamba Module

```python
class GaMamba(nn.Module):
    def __init__(self, d_model, num_layers):
        self.gat = GATConv(d_model, d_model)  # Structural prompt generator
        self.mamba = Mamba(d_model=d_model)    # State space model
        
    def forward(self, X, A):
        # 1. Derive structural prompts from graph topology
        S = norm(self.gat(X, A))
        
        # 2. Integrate prompts into Mamba's output matrix
        # C' = W_c · (C + S)
        
        # 3. Forward through Mamba with structure-aware output
        return self.mamba(X, C_prime)
```

### Hierarchical Entailment Loss

```python
def entailment_loss(x_child, x_parent):
    """Lorentzian entailment regularization in hyperbolic space."""
    # In Lorentz model, entailment is captured by
    # comparing Lorentzian distances to origin
    r_child = lorentz_norm(x_child)
    r_parent = lorentz_norm(x_parent)
    # Child should be "further" from origin (more specific)
    return max(0, r_parent - r_child + margin)
```

### Full Pipeline

```python
def HLBG(global_graph, community_subgraphs):
    # 1. Extract features via GaMamba
    H_global = GaMamba(global_graph.X, global_graph.A)
    H_locals = [GaMamba(G.X, G.A) for G in community_subgraphs]
    
    # 2. Project to hyperbolic space
    h_global = exp_map(H_global)     # Lorentz exponential map
    h_locals = [exp_map(H) for H in H_locals]
    
    # 3. Apply entailment constraints
    loss_entail = sum(entailment_loss(h_roi, h_community) 
                      for roi, community in hierarchy_pairs)
    loss_entail += entailment_loss(h_community, h_global)
    
    # 4. Adaptive fusion + classification
    fused = self_attention([h_global] + h_locals)
    return classifier(fused)
```

## Why Hyperbolic Space?

- **Natural hierarchy encoding**: Hyperbolic space has exponential volume growth, matching tree-like hierarchical structures
- **Lorentzian model**: Mathematically convenient for optimization with gradient-based methods
- **Entailment geometry**: Parent-child relationships in hierarchy map naturally to radial ordering in hyperbolic space

## Activation

Keywords: hyperbolic learning, brain graphs, HLBG, GaMamba, Graph-aware Mamba, Lorentzian space, brain disorder diagnosis, ABIDE-I, REST-MDD, autism classification, depression diagnosis, functional connectivity, hierarchical brain network, biomarker identification, Graph Mamba, entailment regularization

## References

- arXiv: 2607.07077v1
- Full paper text: `/tmp/paper_2607.07077.txt`
