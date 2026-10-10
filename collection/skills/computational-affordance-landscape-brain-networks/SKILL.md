---
name: computational-affordance-landscape-brain-networks
description: Computational Affordance Landscape framework for quantifying neural network computation costs using control theory. Use when analyzing brain network structure-function relationships, neural circuit computations, or applying control theory to quantify computational costs in biological and artificial neural networks.
license: Complete terms in LICENSE.txt
---

# Computational Affordance Landscape Framework

This skill implements the methodology from arXiv:2607.29537 "Quantifying the cost of network computations to unpack structure-function relationships in the brain" by Kulkarni et al. (2026).

## Core Concept

The framework frames computation as a **goal-directed transition of activity** and quantifies its cost on a given network using **control theory**. The distribution of costs across all possible transitions defines a **computational affordance landscape** that encodes which computations a network structure readily supports.

## Key Applications

### 1. Insect Navigation Circuits
- Apply to circuit models for maintaining sense of direction
- Show that updating orientation is the least costly computation
- Predict inputs consistent with known biological circuitry

### 2. Human Brain Networks  
- Analyze how affordance landscapes vary with functional network roles
- **Sensory networks**: More heterogeneous landscapes (specialized information processing)
- **Association networks**: More homogeneous landscapes (generalized information processing)

### 3. Artificial Neural Networks
- Track how learning reshapes computational affordance landscapes
- Show that training progressively increases landscape heterogeneity
- Analyze distribution of affordable computations during cognitive task learning

## Implementation Steps

### Step 1: Define Network Structure
- Represent neural circuit as weighted adjacency matrix A
- Ensure proper normalization for control theory application
- Consider directed vs undirected connectivity based on biological plausibility

### Step 2: Frame Computation as State Transition
- Define initial state x₀ and target state xₜ
- Compute minimum energy control input u(t) using linear quadratic regulator (LQR)
- Cost = ∫‖u(t)‖²dt represents computational cost

### Step 3: Generate Affordance Landscape
- Sample diverse state transitions across network
- Compute cost distribution for all possible transitions
- Visualize as histogram or density plot showing affordable vs expensive computations

### Step 4: Analyze Landscape Properties
- **Heterogeneity**: Measure variance in cost distribution
- **Specialization**: Identify clusters of low-cost computations
- **Generalization**: Assess uniformity of affordable computations

## Mathematical Foundation

The control-theoretic cost is computed using:
```
Cost = x₀ᵀ W⁻¹ x₀
```
where W is the controllability Gramian:
```
W = ∫₀^∞ e^(At)BBᵀe^(Aᵀt) dt
```

For discrete networks, use numerical integration or analytical solutions when available.

## Practical Considerations

### Data Requirements
- Structural connectivity matrix (from DTI, tracer studies, or model architecture)
- Functional validation data (optional but recommended)
- Task-specific state definitions for targeted analysis

### Computational Complexity
- O(n³) for Gramian computation where n = number of nodes
- Monte Carlo sampling recommended for large networks (>1000 nodes)
- Parallelize transition sampling for efficiency

### Validation Strategies
- Compare predicted low-cost computations with empirical neural activity patterns
- Test consistency with known biological circuitry constraints
- Validate against behavioral performance on computational tasks

## Activation Keywords
- computational affordance landscape
- neural computation cost
- brain network control theory
- structure-function relationships neuroscience
- affordance landscape heterogeneity

## References
- Kulkarni, S. S., Kim, J. Z., Fotiadis, P., Pasqualetti, F., & Bassett, D. S. (2026). Quantifying the cost of network computations to unpack structure-function relationships in the brain. arXiv:2607.29537