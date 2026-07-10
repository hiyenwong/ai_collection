---
name: fmri-dictionary-learning-optimal-transport
description: "Novel approach to dictionary learning on fMRI data that explicitly accounts for individual brain geometry variability using optimal transport (Fused Gromov-Wasserstein distance) with amortized optimization for computational efficiency."
arxiv_id: "2605.20883"
published: "2026-05-20"
authors: "Sonia Mazelet, Rémi Flamary, Bertrand Thirion"
tags: [dictionary-learning, fmri, optimal-transport, brain-geometry, fgw-distance, individual-variability, functional-alignment]
---

# Learning fMRI Activation Dictionaries Across Individual Geometries via Optimal Transport

## Core Concept

Introduces a novel **dictionary learning** approach for fMRI data that explicitly accounts for **individual brain geometry variability** using **optimal transport** (Fused Gromov-Wasserstein distance) instead of projecting all brains onto a common template. Uses **amortized optimization** to learn a neural network that predicts optimal transport plans at substantially reduced computational cost.

## Key Contributions

1. **Geometry-Aware Dictionary Learning**: Unlike standard approaches that warp individual brains to a common template (losing subject-specific information), this method preserves individual geometry by comparing brains via optimal transport.

2. **Fused Gromov-Wasserstein Distance**: Uses FGW distance to compare fMRI graphs with different geometries and features, balancing feature alignment (node attributes) with structural consistency (graph topology).

3. **Amortized Optimization**: Learns a neural network to predict approximations of optimal transport plans, making FGW-based dictionary learning computationally feasible for large-scale fMRI graphs.

4. **Controllable Geometric Abstraction**: Dictionary atoms can be learned at different levels of geometric variability by varying the FGW trade-off parameter, controlling the balance between feature alignment and structural consistency.

## Methodology

### Framework

1. **Input**: fMRI data from multiple subjects with individual brain geometries (3D coordinates, connectivity)
2. **Graph Construction**: Each subject's brain → graph with node features (fMRI activations) and edge structure (spatial/functional connectivity)
3. **FGW Dictionary Learning**:
   - Compare graphs across individuals using FGW distance
   - Learn dictionary atoms that balance feature alignment vs. structural consistency
   - Trade-off parameter α controls this balance
4. **Amortized Transport**: Neural network predicts optimal transport plans, avoiding expensive per-pair FGW computations

### Key Innovation

Instead of: Project individual → common template → dictionary learning
The method does: Dictionary learning directly on individual geometries, connected via optimal transport

### Validation
- **Dataset**: HCP (Human Connectome Project) dataset
- **Results**: Captures different levels of geometric variability; preserves essential information for downstream tasks

## Applications

- **Population-level fMRI analysis**: Identifying shared activation patterns while preserving individual geometry
- **Brain state classification**: Learned dictionaries provide interpretable representations
- **Individual differences research**: Understanding how brain geometry variability relates to functional differences
- **Multi-subject fMRI alignment**: Alternative to standard template-based registration

## Relationship to Existing Methods

- **Vs. Template-based registration**: Preserves individual geometry rather than discarding it
- **Vs. Hyperalignment**: Different mathematical foundation (optimal transport vs. Procrustes)
- **Vs. Shared response model**: More flexible geometry handling

## Activation Keywords
- fmri-dictionary-learning, optimal-transport-fmri, fgw-brain, individual-brain-geometry, fmri-alignment, amortized-transport, dictionary-learning-fmri, brain-graph-optimal-transport, fmri-subject-variability, fused-gromov-wasserstein-brain
