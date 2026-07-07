---
name: topology-dependent-polychronous-neuronal-groups
description: Topology-Dependent Emergence of Polychronous Neuronal Groups using Recurrence-Plot characterization. Small-world topology as structural optimum for polychronization with label-free PNG identification via sparse-dot-product Recurrence Plot framework.
version: 1.0
author: extracted from arXiv 2606.25874v1 (Carneiro, Jiofack, Ferreira)
date_created: 2026-06-25
source: arXiv 2606.25874v1
categories: [neuroscience, spiking-neural-networks, computational-neuroscience, neural-dynamics, brain-network]
tags: [polychronous-neuronal-groups, PNG, recurrence-plot, STDP, axonal-delays, Izhikevich-neurons, watts-strogatz, small-world-topology, network-structure]
activation_keywords:
  - polychronous neuronal groups
  - PNG emergence
  - recurrence plot neural networks
  - topology neural computation
  - STDP polychronization
  - axonal delays PNG
  - small-world neural network
  - Izhikevich PNG
  - clustering coefficient neural
  - recurrence quantification analysis neuroscience
related_skills:
  - spiking-neural-network-analysis
  - stdp-spiking-transformer-attention
  - spiking-oscillation-mapping
  - brain-inspired-snn-pattern-analysis
---

# Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization

## Overview

**Core Discovery**: Small-world topology is the structural optimum for polychronization in neural networks. The clustering coefficient C is the primary structural driver of Polychronous Neuronal Group (PNG) yield, with transition from ring-lattice to random graph reducing representational capacity by >90%.

**Methodological Innovation**: Sparse-dot-product Recurrence Plot (RP) framework for label-free PNG identification — identifies PNGs as unit-slope diagonal structures in phase-space recurrence matrix, independent of anatomical neuron labeling.

## Key Findings

### 1. PNG Structural Determinants
- **N=1000 Izhikevich neurons** simulated over 10 hours biological time
- **1545 unique PNGs** identified via offline event-driven detection
- **Clustering coefficient C** drives PNG yield: C~0.35 (ring-lattice) → ~850 PNGs; C~0.20 (random) → <50 PNGs
- **>90% representational capacity reduction** from structured to random topology

### 2. Small-World Topology as Optimum
- Ring-lattice (high clustering) supports rich PNG repertoire
- Random graphs (low clustering) drastically reduce PNG diversity
- Small-world networks optimize trade-off between local structure and global connectivity

### 3. Recurrence Plot PNG Decoder
- **Sparse-dot-product RP** identifies PNGs without neuron labeling
- PNGs appear as **unit-slope diagonal structures** in phase-space recurrence matrix
- **Recurrence Quantification Analysis**: DET~0.65 quantifies trajectory reproducibility
- **Label-free, principled** approach to PNG identification

## Technical Implementation

### Izhikevich Network Simulation
```python
# Izhikevich neuron model parameters
# N = 1000 neurons
# STDP plasticity with heterogeneous axonal delays
# Watts-Strogatz topology sweep: p ∈ [0, 1]
# Clustering coefficient C as structural metric

# PNG detection algorithm (event-driven, offline)
# 1. Track spike timings across all neurons
# 2. Identify time-locked firing cascades
# 3. Verify reproducibility via STDP stabilization
```

### Recurrence Plot Framework
```python
# Phase-space reconstruction from spike trains
# Sparse dot-product for recurrence matrix
# Diagonal structures = PNG signatures
# Recurrence Quantification Analysis (RQA)
#   - DET (determinism): PNG reproducibility
#   - LAM (laminarity): cascade stability
#   - TT (trapping time): PNG duration
```

### Structural Sweep Methodology
```python
# Watts-Strogatz rewiring probability sweep
for p in [0.0, 0.05, 0.1, 0.15, 0.2, ..., 1.0]:
    network = watts_strogatz(N=1000, k=10, p=p)
    C = clustering_coefficient(network)
    PNGs = detect_polychronous_groups(network, duration=10h)
    yield[p] = len(PNGs)
```

## Mechanistic Explanation

### Why Clustering Drives PNG Emergence
1. **Local loops** enable precise timing relationships
2. **Heterogeneous delays** + **STDP** require structured connectivity
3. **Clustered neighborhoods** support multiple stable firing cascades
4. **Random rewiring** disrupts timing chains, collapses PNG diversity

### Why Recurrence Plots Detect PNGs
1. **Phase-space embedding** captures collective dynamics
2. **Diagonal structures** indicate repeatable sequences
3. **Unit-slope diagonals** = fixed timing relationships
4. **No neuron labels needed** — purely dynamical signature

## Novel Contributions

1. **Structural-dynamics link**: First quantitative demonstration that clustering coefficient drives PNG yield
2. **Label-free PNG detection**: Recurrence Plot decoder bypasses anatomical labeling requirements
3. **Combinatorial capacity**: PNG count as measure of network representational richness
4. **Small-world optimum**: Structural sweet spot for polychronization validated empirically

## Applications

### Network Design
- Optimize clustering coefficient for maximum PNG diversity
- Small-world topology for neuromorphic hardware
- Structure-aware SNN architecture design

### PNG Detection
- Recurrence Plot decoder for experimental data
- Label-free analysis of neural recordings
- RQA metrics for cascade reproducibility

### Brain Connectivity
- Explain why cortical networks exhibit small-world properties
- Link structural motifs to functional repertoire
- Predict PNG capacity from connectome topology

## Pitfalls & Limitations

1. **Izhikevich simplification**: More biologically detailed models may differ
2. **Offline detection**: Real-time PNG identification remains challenging
3. **Fixed N=1000**: Scaling laws for PNG yield unknown
4. **No functional validation**: PNG representational role not tested

## Validation Steps

1. Simulate Izhikevich network with Watts-Strogatz sweep
2. Detect PNGs via event-driven offline algorithm
3. Compute clustering coefficient C
4. Plot PNG yield vs C (expect 90% drop from C~0.35 → C~0.20)
5. Apply RP decoder: verify diagonal structures
6. Compute RQA metrics: confirm DET~0.65

## Related Papers

- Izhikevich (2006): Polychronous groups original discovery
- Watts-Strogatz (1998): Small-world network theory
- Marwan et al. (2007): Recurrence plot methodology
- STDP literature: plasticity timing windows

## Key Equations

- **Clustering coefficient**: C = (3 × number of triangles) / (number of connected triples)
- **Recurrence matrix**: R(i,j) = Θ(ε - ||x_i - x_j||) sparse-dot-product formulation
- **Determinism (DET)**: percentage of recurrence points forming diagonals

## Implementation Checklist

- [ ] Izhikevich neuron simulation (N=1000, 10h)
- [ ] Watts-Strogatz topology sweep
- [ ] PNG offline detection algorithm
- [ ] Recurrence Plot decoder
- [ ] RQA metric computation
- [ ] C-PNG yield relationship plot

## Experiments to Run

1. **Scaling test**: N = 100, 500, 1000, 5000 — PNG yield scaling?
2. **Delay distribution**: Gamma vs uniform axonal delays
3. **STDP variants**: Different plasticity rules impact?
4. **Topology families**: Scale-free, modular, hierarchical

## Citation

Carneiro, L. A. T. X., Jiofack, A. D., & Ferreira, F. F. (2026). Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization. arXiv:2606.25874v1.