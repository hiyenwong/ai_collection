---
name: hlbg-hyperbolic-learning-brain-graphs
description: "Hyperbolic Learning on Brain Graphs (HLBG) methodology for brain network analysis using Lorentzian hyperbolic space to model hierarchical ROI-community-whole-brain relationships. Introduces Graph-aware Mamba (GaMamba) for capturing long-range dependencies while preserving graph topology. Achieves SOTA on ABIDE-I and REST-MDD disorder diagnosis. Activation: hyperbolic learning, brain graphs, functional connectivity, disorder diagnosis, Lorentzian space, graph mamba, hierarchical brain networks, biomarker identification"
tags: [hyperbolic-geometry, brain-graphs, functional-connectivity, disorder-diagnosis, graph-neural-networks, mamba]
---

# HLBG - Hyperbolic Learning on Brain Graphs

**Paper**: Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis  
**arXiv**: 2607.07077  
**Authors**: Yapeng Li, Bo Jiang, Ziyan Zhang, Dongdong Chen, Zhengzheng Tu  
**Published**: 2026-07-08  
**Categories**: cs.CV, cs.AI

## Core Contribution

Proposes HLBG framework that exploits hyperbolic geometry to model the hierarchical organization of functional brain networks (ROI → community → whole-brain) for disorder diagnosis and biomarker identification.

## Key Innovations

1. **Hyperbolic Space for Brain Hierarchy**: Projects ROI, community, and whole-brain representations into Lorentzian hyperbolic space, naturally capturing hierarchical relationships
2. **Geometric Entailment Constraints**: Two constraints enforce multi-level hierarchy:
   - ROI-to-community entailment
   - Community-to-whole-brain entailment
3. **Graph-aware Mamba (GaMamba)**: Novel architecture incorporating topology-derived structural prompts into Mamba for:
   - Long-range dependency capture
   - Graph topology preservation
4. **Disorder Biomarker Discovery**: Identifies disorder-relevant functional biomarkers through learned representations

## Methodology

### Pipeline
1. **Brain Graph Construction**: Build functional connectivity graphs from fMRI
2. **Multi-level Representation**: Extract ROI, community, whole-brain features
3. **Hyperbolic Projection**: Map all levels to Lorentzian space (Poincaré ball model)
4. **Geometric Constraints**: Apply entailment losses to preserve hierarchy
5. **GaMamba Processing**: Process with topology-aware Mamba blocks
6. **Classification/Regression**: Downstream disorder diagnosis

### Hyperbolic Geometry
- Uses Lorentz model (hyperboloid) for numerical stability
- Exponential/logarithmic maps for tangent space operations
- Distance metric captures tree-like hierarchy naturally
- Entailment: parent representation "contains" children in hyperbolic space

### GaMamba Architecture
```
Input Graph → Structural Prompt Extraction → Mamba Block → Output
                    ↓
          Topology-aware state space model
          (preserves graph structure in SSM)
```

## Experimental Results

**Datasets**: ABIDE-I (autism), REST-MDD (depression)
- Outperforms SOTA methods on both datasets
- Identifies clinically meaningful biomarkers
- Ablation confirms each component contribution

## Applications

- **Clinical Diagnosis**: Automated brain disorder detection
- **Biomarker Discovery**: Identifying disorder-specific network patterns
- **Brain Network Analysis**: Understanding hierarchical organization
- **Treatment Monitoring**: Tracking network changes over time

## Technical Details

### Lorentz Model Operations
```python
# Lorentz inner product
def lorentz_inner_product(x, y):
    return -x[0]*y[0] + sum(x[i]*y[i] for i in range(1, dim))

# Exponential map (Euclidean → hyperbolic)
def exp_map(v, c=1.0):
    norm_v = sqrt(lorentz_inner_product(v, v))
    return cosh(sqrt(c)*norm_v) * v[0] + sinh(sqrt(c)*norm_v) * v[1:] / (sqrt(c)*norm_v)

# Entailment loss (parent should contain child)
def entailment_loss(parent, child):
    dist = hyperbolic_distance(parent, child)
    return max(0, dist - margin)
```

### GaMamba Integration
- Structural prompts derived from graph Laplacian eigenvectors
- State space model modified to respect graph topology
- Selective scan mechanism for efficient long-range modeling

## Limitations

- Requires pre-defined community structure (parcellation-dependent)
- Hyperbolic optimization can be numerically unstable
- Computational cost of hyperbolic operations
- Limited to static functional connectivity (no temporal dynamics)

## Related Work

- Hyperbolic graph neural networks (Hyperbolic GCN, HAT)
- Brain graph learning (BrainNetGNN, GNN-FC)
- Mamba/state space models for graphs
- Functional connectivity analysis

## Related Skills

- [[hyperbolic-gcn-brain-network]] - Earlier hyperbolic GCN for brain networks
- [[hyperbolic-learning-brain-graphs]] - Related hyperbolic brain analysis
- [[functional-connectivity-graph-neural-networks]] - FC-based GNN methods
- [[gnn-visual-decoding-brain-network]] - GNN for brain decoding
