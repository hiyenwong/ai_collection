---
name: core-cross-site-ood-brain-network
description: >
  CORE (Cross-site OOD Robust brain nEtwork) framework for brain network
  learning across unseen sites. Addresses cross-site out-of-distribution
  degradation in fMRI graph-based learning through site-aware confounder
  decoupling, transient pathway dynamics profiling, line graph organization
  for transferable pathway-level modeling, and prior-guided subject-adaptive
  gating. Use when working with cross-site fMRI brain network analysis,
  OOD generalization in neuroimaging, site-conditioned bias mitigation,
  transient neurodynamics modeling, or multi-site brain disorder classification.
  Triggers: cross-site OOD, brain network generalization, site bias, confounder
  decoupling, CORE framework, transient pathway, line graph brain, multi-site fMRI.
---

# CORE: Cross-site OOD Robust brain nEtwork

Unified framework for brain network learning across unseen sites. Addresses
two key failures in existing methods: (1) site-conditioned confounders induce
non-pathological shortcuts, and (2) temporal averaging obscures transient
neurodynamics, limiting generalization.

## Problem Statement

Graph-based learning on fMRI shows strong potential but degrades under
cross-site OOD settings because:
1. **Site-conditioned confounders** create non-pathological shortcuts
2. **Temporal averaging** in FC construction obscures transient neurodynamics

## Three-Stage Architecture

### Stage 1: Site-Aware Confounder Decoupling

Extracts cross-site population scaffold of reproducible diagnostic connectivity
edges by mitigating site-conditioned bias.

```
Raw FC → Site confounder removal → Scaffold edges (diagnostic, reproducible)
```

Key insight: Separate site-specific variation from population-level disease
signal.

### Stage 2: Transient Pathway Dynamics Profiling

Profiles transient dynamics over the scaffold using lightweight temporal
descriptors and organizes scaffold edges into a line graph for transferable
pathway-level modeling.

```
Scaffold edges → Line graph → Pathway dynamics → Transferable representations
```

**Line Graph Construction**: Each edge in the original brain network becomes
a node in the line graph, enabling pathway-level (edge-to-edge) analysis.

### Stage 3: Prior-Guided Subject-Adaptive Gating

Leverages scaffold-derived population priors while preserving subject-specific
connectivity variability through an adaptive gating mechanism.

```
Population prior ⊗ Subject-specific gating → Final representation
```

## Implementation Pattern

```python
import torch
import torch.nn as nn

class CORE(nn.Module):
    def __init__(self, n_regions, n_sites, scaffold_edge_dim, pathway_dim):
        super().__init__()
        # Stage 1: Confounder decoupling
        self.site_encoder = nn.Embedding(n_sites, 64)
        self.decoupler = nn.Sequential(
            nn.Linear(n_regions * n_regions, 256),
            nn.ReLU(),
            nn.Linear(256, scaffold_edge_dim)
        )

        # Stage 2: Line graph + pathway dynamics
        self.line_graph_conv = nn.Sequential(
            nn.Linear(scaffold_edge_dim, pathway_dim),
            nn.ReLU(),
            nn.Linear(pathway_dim, pathway_dim)
        )
        self.temporal_descriptor = nn.GRU(
            input_size=pathway_dim,
            hidden_size=pathway_dim,
            batch_first=True
        )

        # Stage 3: Subject-adaptive gating
        self.gate = nn.Sequential(
            nn.Linear(scaffold_edge_dim, 64),
            nn.ReLU(),
            nn.Linear(64, scaffold_edge_dim),
            nn.Sigmoid()
        )

        self.classifier = nn.Linear(pathway_dim, 2)

    def forward(self, fc_matrix, site_id, time_series=None):
        # Stage 1: Decouple site confounders
        site_embed = self.site_encoder(site_id)
        scaffold = self.decoupler(fc_matrix.view(fc_matrix.size(0), -1))

        # Stage 2: Line graph + temporal dynamics
        pathway = self.line_graph_conv(scaffold)
        if time_series is not None:
            temporal_out, _ = self.temporal_descriptor(pathway.unsqueeze(1))
            pathway = temporal_out[:, -1]

        # Stage 3: Adaptive gating
        gate_weights = self.gate(scaffold)
        representation = pathway * gate_weights

        return self.classifier(representation), scaffold, gate_weights
```

## Line Graph for Brain Networks

Transform edge-level brain connectivity to pathway-level representations:

```python
def build_line_graph(adjacency):
    """Convert brain network adjacency to line graph.

    Each edge (i,j) in original graph becomes a node in line graph.
    Two line-graph nodes are connected if their corresponding edges
    share a vertex in the original graph.
    """
    n = adjacency.shape[0]
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if adjacency[i, j] > 0:
                edges.append((i, j))

    n_edges = len(edges)
    line_adj = torch.zeros(n_edges, n_edges)
    for a in range(n_edges):
        for b in range(a+1, n_edges):
            # Share a vertex?
            if (edges[a][0] == edges[b][0] or
                edges[a][0] == edges[b][1] or
                edges[a][1] == edges[b][0] or
                edges[a][1] == edges[b][1]):
                line_adj[a, b] = line_adj[b, a] = 1
    return line_adj
```

## Key Datasets

- **ABIDE**: Autism Brain Imaging Data Exchange
- **REST-meta-MDD**: Resting-state MDD dataset
- **SRPBS**: Suzuki Resting-State fMRI Database
- **ABCD**: Adolescent Brain Cognitive Development

## Evaluation Protocol

Leave-one-site-out evaluation: Train on N-1 sites, test on held-out site.

Results show up to 6.7% relative gain over baselines, robust to atlas
variations across different brain parcellation schemes.

## Advantages Over Baselines

| Method | Cross-site OOD | Transient Dynamics | Subject Variability |
|--------|---------------|-------------------|-------------------|
| Standard GNN | ❌ Degrades | ❌ Averaged | ❌ Lost |
| Site-conditioned | ⚠️ Partial | ❌ Averaged | ⚠️ Partial |
| **CORE** | ✅ Robust | ✅ Profiled | ✅ Preserved |

## Workflow

1. **Collect multi-site fMRI data**: Gather FC matrices + temporal series
2. **Build scaffold**: Apply confounder decoupling to extract reproducible edges
3. **Construct line graph**: Transform edge-level to pathway-level representation
4. **Profile transient dynamics**: Use temporal descriptors over time windows
5. **Apply adaptive gating**: Combine population prior with subject variability
6. **Evaluate cross-site**: Leave-one-site-out protocol

## Activation Keywords

- cross-site brain network
- OOD neuroimaging
- site confounder decoupling
- transient pathway dynamics
- line graph brain network
- multi-site fMRI generalization
- CORE framework
- subject-adaptive gating
- brain network transfer learning