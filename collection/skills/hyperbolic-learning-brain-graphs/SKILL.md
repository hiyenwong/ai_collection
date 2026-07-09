---
name: hyperbolic-learning-brain-graphs
description: Hyperbolic Learning on Brain Graphs (HLBG) methodology for brain disorder diagnosis. Exploits hierarchical geometry of hyperbolic space to model ROI→community→whole-brain relationships.
trigger_words:
  - hyperbolic space
  - brain graph
  - hierarchical brain network
  - Lorentzian space
  - brain disorder diagnosis
  - functional connectivity
  - Graph-aware Mamba
  - GaMamba
categories:
  - neuroscience
  - brain network
  - graph neural network
  - hyperbolic geometry
  - medical AI
arxiv_id: "2607.07077v1"
date_added: "2026-07-10"
---

# Hyperbolic Learning on Brain Graphs (HLBG) for Disorder Diagnosis

## Overview

This methodology introduces **Hyperbolic Learning on Brain Graphs (HLBG)**, a novel framework that exploits the inherent hierarchical geometry of hyperbolic space to model the hierarchical relationships among ROIs, functional communities, and the whole-brain network for brain disorder analysis.

**Paper**: Li, Jiang, Zhang, Chen & Tu (2026). Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis. arXiv:2607.07077v1

## Core Innovation

### The Hierarchical Brain Network Problem

Functional brain networks exhibit hierarchical organization across three levels:
1. **ROI level**: Individual brain regions
2. **Community level**: Functional communities/subnetworks
3. **Whole-brain level**: Global network integration

**Challenge**: Existing methods struggle to model ROI–community interactions and fail to exploit the full hierarchy.

### Hyperbolic Space Solution

Hyperbolic space (constant negative curvature) naturally encodes hierarchical relationships:
- **Radial dimension**: Encodes hierarchy depth (ROI → community → whole-brain)
- **Angular dimension**: Encodes similarity within hierarchy level
- **Exponential capacity**: Can represent tree-like structures without distortion

## Methodology

### 1. Hierarchical Brain Graph Construction

```
fMRI → FC Matrix → Community Parcellation → Hierarchical Graph
         ↓
    ROI-level features
         ↓
    Community-level features (aggregated from ROIs)
         ↓
    Whole-brain features (aggregated from communities)
```

**Community Detection**: Uses standardized functional network mapping (Yeo 7/17 networks)

### 2. Graph-aware Mamba (GaMamba)

**Innovation**: Integrates topology-derived structural prompts into Mamba's input-dependent readout matrix.

**Architecture**:
- **Global branch**: Captures topology-aware whole-brain representations
- **Local branches** (parallel): Extract community-specific features
- **Attention fusion**: Adaptive fusion of local and global representations

**Key Formula**:
```
GaMamba: u_t = A_t ⊙ x_t + B_t ⊙ s_t
where A_t, B_t are topology-conditioned parameters
```

### 3. Hierarchical Brain Representation Learning (HBRL)

**Core Mechanism**: Projects ROI, community, and whole-brain representations into unified Lorentzian hyperbolic space.

**Lorentzian Hyperbolic Space**:
```
L^n = {x ∈ R^{n+1} | -x_0² + x_1² + ... + x_n² = -1, x_0 > 0}
```

**Entailment Constraints**: Two geometric losses enforce hierarchy:
1. **ROI → Community**: Community embedding should entail its constituent ROIs
2. **Community → Whole-brain**: Whole-brain embedding should entail all communities

**Entailment Loss**:
```
L_entail = ||c - proj_L(r)||² + ||w - proj_L(c)||²
where r = ROI, c = community, w = whole-brain
```

### 4. Training Objective

```
L_total = L_classification + λ_1 * L_entail + λ_2 * L_regularization
```

## Experimental Results

### Datasets
- **ABIDE-I**: Autism Spectrum Disorder (ASD) vs. controls (n=1035)
- **REST-MDD**: Major Depressive Disorder (MDD) vs. controls

### Performance
- **ABIDE-I**: 78.2% accuracy (SOTA: 76.8%)
- **REST-MDD**: 82.5% accuracy (SOTA: 80.1%)

### Biomarker Discovery
Identifies disorder-relevant functional connections:
- **ASD**: Default mode network, salience network disruptions
- **MDD**: Fronto-limbic circuit abnormalities

## Key Advantages

1. **Hierarchical Modeling**: First to explicitly model ROI→community→whole-brain in hyperbolic space
2. **Long-range Dependencies**: GaMamba captures distant interactions while preserving topology
3. **Interpretability**: Hyperbolic coordinates reveal hierarchical organization
4. **Efficiency**: Linear complexity (Mamba) vs. quadratic (Transformer)

## Implementation Details

### Hyperbolic Operations
- **Exponential map**: Project Euclidean → hyperbolic
- **Logarithmic map**: Project hyperbolic → Euclidean
- **Hyperbolic distance**: d_L(x,y) = arccosh(-⟨x,y⟩_L)

### Training
- **Optimizer**: Adam (lr=1e-4)
- **Hyperparameters**: λ_1=0.1, λ_2=0.01
- **Epochs**: 100 with early stopping

## Activation Triggers

Use this skill when working on:
- Brain network analysis and fMRI classification
- Hierarchical graph representation learning
- Hyperbolic neural networks
- Brain disorder diagnosis (ASD, MDD, etc.)
- Functional connectivity analysis
- Biomarker discovery

## Related Concepts

- Hyperbolic neural networks (Ganea et al., 2018)
- Graph neural networks for brain networks
- Mamba / state space models
- Community detection in brain networks
- Functional connectivity (FC) analysis

## Code Structure

```
HLBG/
├── hierarchical_graph_construction.py
├── gamamba_model.py
├── hyperbolic_operations.py
├── entailment_loss.py
└── training_pipeline.py
```

## Limitations & Future Work

- **Limitation**: Requires pre-defined community parcellation
- **Future**: Learn hierarchical structure end-to-end
- **Future**: Extend to dynamic functional connectivity
