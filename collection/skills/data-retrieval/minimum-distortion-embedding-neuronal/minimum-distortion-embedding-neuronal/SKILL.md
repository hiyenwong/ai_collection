---
name: minimum-distortion-embedding-neuronal
description: "Minimum-Distortion Embedding (MDE) framework for analyzing evolving neuronal network dynamics. Use when dimensionality-reducing high-dimensional spiking activity, analyzing network development trajectories, or comparing stimulation effects in neuronal cultures."
---

## Minimum-Distortion Embedding for Neuronal Analysis

### Context
MDE with cosine metric captures neuronal network maturation trajectories and preserves activity cloud contraction as connectivity increases — outperforming PCA and t-SNE for neuronal population analysis.

### Key Findings (arXiv:2502.20862)
- **Cosine > Euclidean**: Cosine distance between population activity vectors better reflects changes in population activity patterns
- **Developmental tracking**: MDE captures trajectory from DIV23 to DIV64 in human cortical cultures
- **Stimulation detection**: MDE separates activity phases more clearly than PCA
- **Transient preservation**: Preserves transient within-phase variability changes missed by PCA

### Framework Steps
1. Extract population activity vectors from spiking data
2. Apply MDE with cosine metric (not Euclidean)
3. Quantify cosine-shape radius preservation within conditions
4. Measure pairwise distances between condition centroids
5. Compare with PCA/t-SNE baselines
6. Validate on both in silico and in vitro data

### Metric Selection Guide
- **Cosine distance**: Best for population activity pattern changes
- **Euclidean distance**: May miss important within-phase variability
- **MDE**: Superior to PCA for stimulation experiments
- **t-SNE**: Good for visualization but less quantitative

### Pitfalls
- **Metric mismatch**: Using Euclidean distance may obscure biologically relevant patterns
- **Developmental scale**: DIV23-DIV64 represents significant network maturation window
- **Stimulation types**: Weak vs strong stimulation show different embedding responses

### Activation: neuronal embedding, MDE, dimensionality reduction, cortical cultures, stimulation analysis, network development
