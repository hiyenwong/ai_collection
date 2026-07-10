---
name: sd3mf-multimodal-brain-network
description: >
  Supervised Deep Multimodal Matrix Factorization (SD3MF) methodology for
  interpretable brain network analysis. Generalizes SNMTF from unsupervised
  single-graph clustering to supervised prediction over populations of
  multimodal graphs. Learns deep hierarchical factorizations with shared
  latent representations that align subjects across modalities via
  encoder-decoder formulation. Use when: analyzing multimodal connectome
  data, building interpretable brain network classifiers, performing
  supervised prediction with population-level graph data, integrating
  multiple neuroimaging modalities with biological interpretability, or
  improving over GNN/CNN baselines on brain network tasks. Activation:
  SD3MF, multimodal matrix factorization brain network, interpretable
  connectome analysis, supervised graph prediction, multimodal brain
  network classification, SNMTF supervised extension, community-level
  brain interaction matrices, encoder-decoder brain network, adaptive
  multimodal fusion connectome.
---

# SD3MF: Supervised Deep Multimodal Matrix Factorization for Brain Network Analysis

Interpretable framework for integrative brain network analysis that generalizes
Symmetric Nonnegative Matrix Tri-Factorization (SNMTF) to supervised prediction
over populations of multimodal graphs.

## Paper Reference

- **Title**: Supervised Deep Multimodal Matrix Factorization for Interpretable Brain Network Analysis
- **Authors**: Amjad Seyedi, Lifang He, Songlin Zhao, Akwum Onwunta, Nicolas Gillis
- **arXiv**: 2605.13312
- **Date**: 2026-05-13
- **Categories**: cs.LG
- **Code**: https://github.com/amjadseyedi/SD3MF

## Core Problem

Existing brain network analysis methods face a trade-off: deep learning (CNNs,
GNNs) achieves strong predictive performance but lacks interpretability, while
traditional matrix factorization (SNMTF) provides interpretable community
structure but cannot perform supervised prediction or handle multiple modalities.

## Key Contributions

### 1. SD3MF Architecture

Extends SNMTF from unsupervised single-graph clustering to supervised
prediction over populations of multimodal graphs:

- **Deep hierarchical factorization**: Each modality gets its own deep factorization chain
- **Shared latent representation**: Aligns subjects across different views/modalities
- **Encoder-decoder formulation**: Jointly optimizes graph reconstruction + supervised prediction
- **Adaptive weights**: Data-driven multimodal fusion — learns which modalities matter most

### 2. Community-Level Features

Each subject is represented through **community-level interaction matrices**:

```
Subject_i → [Community interaction matrix] → Interpretable + Discriminative features
```

- Communities correspond to biologically meaningful brain network modules
- Interaction matrices capture between-community connectivity patterns
- Features are both interpretable (can trace back to brain regions) and discriminative (useful for prediction)

### 3. Adaptive Multimodal Fusion

Unlike fixed-weight fusion, SD3MF learns adaptive weights per subject:

- Data-driven importance of each modality
- Handles missing modalities gracefully
- Subject-specific fusion weights enable personalized analysis

### 4. Performance

Experiments on multimodal connectome datasets show:

- Consistently outperforms CNN and GNN baselines
- Maintains full biological interpretability
- Enables identification of discriminative brain network patterns

## Architecture Details

### Matrix Factorization Foundation

SNMTF decomposes adjacency matrix A ≈ F S F^T where:
- F: community membership matrix (nonnegative)
- S: community-community interaction matrix

SD3MF extends this:
1. **Deep hierarchy**: Multiple factorization layers F₁, F₂, ..., Fₙ
2. **Multimodal**: Separate factorizations for each modality (fMRI, DTI, etc.)
3. **Supervised**: Joint loss = reconstruction + prediction
4. **Shared representation**: Bottleneck that aligns all modalities

### Loss Function

```
L = Σ_m α_m · L_recon(m) + L_predict + L_reg
```

Where:
- α_m: adaptive weight for modality m
- L_recon: graph reconstruction error per modality
- L_predict: supervised prediction loss
- L_reg: regularization for nonnegativity and sparsity

### Workflow

```
Input: Population of multimodal brain networks
  ↓
Deep factorization per modality
  ↓
Shared latent space (subject alignment)
  ↓
Community-level interaction matrices
  ↓
Supervised prediction + Graph reconstruction
  ↓
Interpretable features + Predictions
```

## When to Use This Skill

- Analyzing multimodal connectome datasets (fMRI + DTI + structural)
- Building interpretable classifiers for neurological conditions
- Identifying discriminative brain network communities
- Supervised prediction with population-level graph data
- Cases where GNNs are too opaque and matrix factorization is too simple
- Need to understand which brain connections drive predictions

## Comparison with Alternatives

| Method | Interpretability | Multimodal | Supervised | Performance |
|--------|-----------------|-----------|-----------|-------------|
| CNN | Low | Requires alignment | Yes | Good |
| GNN | Low | Requires alignment | Yes | Good |
| SNMTF | High | No | No | Moderate |
| **SD3MF** | **High** | **Yes (adaptive)** | **Yes** | **Best** |

## Implementation Considerations

1. **Number of communities**: Choose based on brain parcellation (e.g., 7, 17, or 44 communities)
2. **Modality weighting**: Initialize uniformly, let model learn adaptive weights
3. **Regularization**: Nonnegativity constraint is critical for interpretability
4. **Missing data**: Can handle subjects with incomplete modalities via adaptive weighting

## Related Skills

- `brain-graph-neural` - GNN methods for brain connectivity
- `brain-connectivity-analysis` - General brain network analysis
- `multimodal-brain-connectivity-gnn` - Multimodal brain network analysis with GNNs
- `functional-connectivity-graph-neural-networks` - FC-GNN methodology
- `brain-higher-order-structures` - Higher-order brain network analysis
