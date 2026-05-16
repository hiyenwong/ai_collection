---
name: dual-axis-zebrafish-circuits
description: >
  Dual-axis attribution methodology for zebrafish tectal microcircuits. Maps biological
  subcircuits to computational functions (energy-efficient processing vs robustness-preserving
  stabilization) through SNN ablation and transfers insights to artificial neural architectures.
  Use when: bio-inspired neural architecture design, circuit-level attribution, energy-efficient
  computation, robust neural networks, zebrafish visual-motor system, subcircuit ablation,
  biological-to-ANN transfer.
---

# Dual-Axis Zebrafish Circuit Attribution

## Overview

A systematic methodology for attributing computational functions to biological neural subcircuits
along two axes: **energy-efficient information processing** and **robustness-preserving stabilization**.
Bridges biological circuit organization with artificial neural architecture design.

**Paper**: Dual-axis attribution of zebrafish tectal microcircuits for energy-efficient and robust neurocomputing (arXiv:2605.13924v1)

**Authors**: Ningping Li, Hao Zhang, Yi Zhou (USTC)

## Methodology Framework

### Stage 1: Biological Graph Construction
Reconstruct a directed brain abstraction from anatomical and electrophysiological connection priors.
- Nodes: neural categories/subpopulations (e.g., RGC, TIN, TPN)
- Edges: directed connection probabilities between categories
- Connection matrix: A ∈ R^(n×n) where A_ij = P(connection from j → i)

### Stage 2: Mesoscopic Substructure Definition
Group microscopic cell-category nodes into anatomical/functional substructures.
- Example substructures: ns_TIN (non-superficial tectal interneurons), superficial_TIN, deep_TIN
- Groups capture functional coherence rather than individual neurons

### Stage 3: Dynamic Feasibility Checking
Verify signal propagation through the reconstructed graph using LIF spiking neural network simulation.
- Ensure the graph topology supports realistic neural dynamics
- Validate retinotectal signal flow patterns

### Stage 4: SNN-Based Substructure Ablation
Use a leaky integrate-and-fire SNN as nonlinear perturbation testbed.

**Dual-Axis Metrics**:

1. **Energy Sensitivity Index (ESI)**: Identifies energy-efficient substructures
   - ESI = |ΔPerformance| / (1 + SpikeFootprint)
   - High ESI = significant performance impact with low spike cost
   - Finds "sparse but important" subcircuits

2. **Robustness Sensitivity Index (RSI)**: Identifies robustness-preserving substructures  
   - RSI = normalized performance degradation after substructure removal
   - High RSI = critical for system-level stability under perturbation
   - Finds "feedback-like stabilizing" subcircuits

### Stage 5: ANN Transfer
Transfer attributed functions to artificial neural network modules:

| Subcircuit | Computational Role | ANN Module Design |
|-----------|-------------------|-------------------|
| ns_TIN | Energy-efficient gating | Adaptive computation gating for budget reduction |
| superficial_TIN | Robustness stabilization | Feedback-like refinement for noise robustness |

## Key Findings

### Functional Dissociation
- **ns_TIN**: Low spike footprint + measurable prediction error influence → spike-efficient internal information gate
- **superficial_TIN**: Highest robustness sensitivity → feedback-like role in system stability
- These subcircuits serve computationally distinct roles

### Transfer Validation (CIFAR-10)
- ResNet18WithNsTIN: Slower performance degradation under inference-budget reduction
- ResNet18WithSuperficialTIN: Higher accuracy under Gaussian noise corruption

## Activation Keywords
- dual-axis attribution
- zebrafish tectal circuit
- energy-efficient neural architecture
- robust neural network design
- bio-inspired subcircuit transfer
- SNN ablation analysis
- biological-to-ANN transfer
- circuit-level functional attribution
- 斑马鱼神经回路
- 能量高效计算
- 鲁棒神经网络

## Implementation Notes

1. **Graph Construction**: Use connection probability matrices from biological atlases
2. **Ablation Protocol**: Systematically remove subcircuits, measure ESI and RSI
3. **Transfer Design**: Map biological roles to architectural mechanisms (gating, feedback)
4. **Evaluation**: Match evaluation to attributed function (budget reduction for energy, noise for robustness)

## Pitfalls
- Naive lesion analysis only measures global performance loss — use dual-axis to distinguish computational roles
- Low activity ≠ unimportant: a subcircuit may be sparse but functionally critical
- Transfer should validate under conditions matching the attributed function
