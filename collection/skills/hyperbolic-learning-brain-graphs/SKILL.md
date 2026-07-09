---
name: hyperbolic-learning-brain-graphs
description: Hyperbolic Learning on Brain Graphs (HLBG) methodology for modeling hierarchical brain network organization across ROI, community, and whole-brain levels using Lorentzian hyperbolic space.
activation: hyperbolic learning, brain graphs, hierarchical networks, disorder diagnosis, ROI-community hierarchy, Lorentzian space, Graph-aware Mamba
tags: [neuroscience, brain-networks, hyperbolic-geometry, graph-neural-networks, mri-analysis]
version: 1.0.0
author: agent
source: arXiv:2607.07077
---

# Hyperbolic Learning on Brain Graphs (HLBG)

## Paper Reference
- **Title**: Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis
- **Authors**: Yapeng Li, Bo Jiang, Ziyan Zhang, Dongdong Chen, Zhengzheng Tu
- **arXiv**: 2607.07077
- **Published**: 2026-07-08

## Core Methodology

### Key Insight
Functional brain networks exhibit **hierarchical organization** across three levels:
1. **ROI level**: Individual brain regions
2. **Community level**: Functional modules/clusters
3. **Whole-brain level**: Global network integration

Traditional methods fail to model ROI-community interactions and exploit this hierarchy. HLBG uses **hyperbolic geometry** to naturally embed hierarchical structures.

### Architecture Design

#### 1. Hyperbolic Space Projection
- Project representations from all three levels (ROI, community, whole-brain) into **Lorentzian hyperbolic space**
- Hyperbolic geometry naturally encodes hierarchical relationships (tree-like structures)
- Enables hierarchy-aware and discriminative representations

#### 2. Geometric Entailment Constraints
Two constraints impose multi-level hierarchy:
- **ROI → Community**: ROI representations are entailed by their parent community
- **Community → Whole-brain**: Community representations are entailed by whole-brain context
- These constraints enforce hierarchical consistency in the embedding space

#### 3. Graph-aware Mamba (GaMamba)
Novel architecture combining:
- **Mamba backbone**: State space model for long-range dependencies
- **Topology-derived structural prompts**: Graph structure injected as prompts
- Preserves graph topological information while capturing sequential patterns

### Training Pipeline

```
Input: fMRI/DTI brain graphs (ROI connectivity matrices)
    ↓
Multi-level Graph Construction
    - ROI-level graphs
    - Community-level graphs (via clustering)
    - Whole-brain graph
    ↓
Hyperbolic Projection (Lorentzian space)
    ↓
Geometric Entailment Loss
    - ROI → Community entailment
    - Community → Whole-brain entailment
    ↓
GaMamba Encoder
    - Structural prompts from graph topology
    - Long-range dependency modeling
    ↓
Classification/Regression Head
    - Disorder diagnosis (ASD, MDD, etc.)
    - Biomarker identification
```

## Key Contributions

1. **First Hyperbolic Brain Graph Framework**: Exploits natural hierarchy in brain networks
2. **Geometric Entailment**: Novel constraints for multi-level hierarchical consistency
3. **Graph-aware Mamba**: Combines SSM efficiency with graph topology awareness
4. **Biomarker Discovery**: Identifies disorder-relevant functional connections

## Experimental Validation

### Datasets
- **ABIDE-I**: Autism Brain Imaging Data Exchange (ASD diagnosis)
- **REST-MDD**: Major Depressive Disorder dataset

### Results
- Outperforms state-of-the-art brain graph methods
- Achieves superior classification accuracy
- Identifies biologically meaningful biomarkers

## Implementation Patterns

### Hyperbolic Operations
```python
# Lorentzian hyperbolic space operations
def lorentzian_inner_product(x, y):
    """Inner product in Lorentzian space"""
    return -x[0]*y[0] + torch.sum(x[1:]*y[1:], dim=-1)

def hyperbolic_distance(x, y):
    """Distance in hyperbolic space"""
    sq_norm_x = lorentzian_inner_product(x, x)
    sq_norm_y = lorentzian_inner_product(y, y)
    xy = lorentzian_inner_product(x, y)
    return acosh(-xy / (sqrt(sq_norm_x) * sqrt(sq_norm_y)))
```

### Entailment Loss
```python
def geometric_entailment_loss(child, parent, margin=1.0):
    """Enforce child is entailed by parent in hyperbolic space"""
    dist = hyperbolic_distance(child, parent)
    return relu(dist - margin).mean()
```

## Applications

1. **Neurological Disorder Diagnosis**: ASD, MDD, Alzheimer's detection
2. **Biomarker Identification**: Discover disorder-specific connectivity patterns
3. **Brain Network Analysis**: Hierarchical organization studies
4. **Multi-scale Brain Modeling**: Bridge micro (ROI) to macro (whole-brain) scales

## Pitfalls & Considerations

- **Hyperbolic Optimization**: Hyperbolic spaces require Riemannian optimization (e.g., Riemannian Adam)
- **Community Detection**: Quality of hierarchy depends on clustering algorithm choice
- **Computational Cost**: Hyperbolic operations more expensive than Euclidean
- **Interpretability**: Hyperbolic embeddings less intuitive than Euclidean

## Related Concepts

- Hyperbolic neural networks (Ganea et al., 2018)
- Brain graph analysis (fMRI/DTI connectivity)
- State space models (Mamba, S4)
- Hierarchical representation learning
- Geometric deep learning
