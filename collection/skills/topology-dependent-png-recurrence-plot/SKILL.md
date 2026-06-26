---
name: topology-dependent-png-recurrence-plot
description: Topology-Dependent Emergence of Polychronous Neuronal Groups (PNGs) via Recurrence-Plot Characterization — structural determinants and label-free PNG detection methodology
version: 1.0.0
author: Lucas A. T. Carneiro, Armand D. Jiofack, Fernando F. F. Ferreira
arxiv_id: 2606.25874v1
published: 2026-06-24
categories: [neuroscience, neural-networks, spiking-neural-networks, computational-neuroscience]
tags: [polychronous-neuronal-groups, png, recurrence-plot, topology, clustering-coefficient, watts-strogatz, izhikevich-neurons, stdp, axonal-delays]
activation_words: [polychronous neuronal groups, PNG, recurrence plot, network topology, clustering coefficient, STDP, axonal delays]
---

# Topology-Dependent Emergence of Polychronous Neuronal Groups

## Summary

Polychronous Neuronal Groups (PNGs) are reproducible, time-locked spatiotemporal firing cascades stabilized by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays, providing a combinatorially rich substrate for neural computation. This methodology introduces:

1. **Parametric topology sweep**: Watts-Strogatz model to identify structural determinants of PNG emergence
2. **Recurrence Plot (RP) decoder**: Label-free PNG identification via sparse-dot-product recurrence matrix analysis
3. **Key finding**: Clustering coefficient C is the primary structural driver of PNG yield

**Critical Discovery**: Transition from ring-lattice (C~0.35, ~850 PNGs) to random graph (C~0.20, <50 PNGs) reduces representational capacity by >90%. Small-world topology is optimal for polychronization.

## Core Methodology

### 1. Network Simulation
```python
# Izhikevich neuron network
N = 1000 neurons
# Simulation duration: 10 hours biological time
# PNG detection: offline event-driven algorithm
# Output: 1545 unique PNGs identified
```

### 2. Watts-Strogatz Topology Sweep
- **Ring-lattice**: High clustering (C~0.35), high PNG yield (~850 PNGs)
- **Small-world**: Intermediate clustering, optimal PNG diversity
- **Random graph**: Low clustering (C~0.20), minimal PNG yield (<50)

**Key parameter**: Rewiring probability controls clustering coefficient

### 3. Recurrence Plot Framework
```
Sparse-dot-product RP = sparse_dot_product(phase_space_matrix)
PNG signature = unit-slope diagonal structures in RP
DET metric ≈ 0.65 → quantifies trajectory reproducibility
```

**Advantages**: 
- Label-free detection (no anatomical neuron labeling required)
- Principled identification via phase-space recurrence matrix
- Recurrence Quantification Analysis (RQA) for validation

## Key Equations

### PNG Yield vs Clustering
```
PNG_count ≈ f(clustering_coefficient C)
Optimal: C ≈ 0.35 (ring-lattice regime)
Critical transition: C < 0.25 → PNG collapse
```

### Recurrence Plot Construction
```
RP[i,j] = δ(φ[i] - φ[j])  # phase-space distance
PNGs detected as diagonal structures with slope ≈ 1
DET = Σ(diagonal_elements) / Σ(all_elements)
```

## Practical Applications

### 1. Network Topology Design
- **Goal**: Maximize PNG yield for neural computation
- **Method**: Optimize clustering coefficient via Watts-Strogatz rewiring
- **Target**: C ≈ 0.35 for high PNG diversity

### 2. PNG Detection Pipeline
```python
def detect_pngs(spike_trains, tolerance=0.01):
    # Build phase-space trajectory
    phase_matrix = extract_phase_trajectory(spike_trains)
    
    # Compute sparse recurrence plot
    rp = sparse_dot_product(phase_matrix, tolerance)
    
    # Extract unit-slope diagonal structures
    pngs = extract_diagonal_structures(rp, slope=1.0)
    
    # RQA validation
    det = compute_determinism(rp)
    
    return pngs, det
```

### 3. Memory Capacity Analysis
- **Metric**: PNG count × temporal precision
- **Structural optimum**: Small-world topology
- **Combinatorial explosion**: 1545 PNGs from 1000 neurons

## Pitfalls & Considerations

### 1. Simulation Duration
- **Requirement**: >10 hours biological time for PNG stabilization
- **Warning**: Shorter simulations may miss late-emerging PNGs
- **Recommendation**: Use event-driven detection for efficiency

### 2. STDP Parameters
- Critical for PNG stabilization
- Heterogeneous axonal delays essential
- Default: STDP window ±20ms, delay distribution 1-20ms

### 3. Recurrence Plot Interpretation
- Unit-slope diagonals = PNG signatures
- DET ~0.65 indicates good reproducibility
- Avoid: over-interpreting short diagonal segments

## Experimental Validation

### Dataset
- N=1000 Izhikevich neurons
- 10 hours simulated activity
- 1545 unique PNGs detected
- 34 Watts-Strogatz topology configurations

### Metrics
1. PNG count: structural capacity measure
2. DET: trajectory reproducibility (RQA)
3. Clustering coefficient: topology control parameter

## Related Concepts

- **STDP (Spike-Timing-Dependent Plasticity)**: PNG stabilization mechanism
- **Axonal Delays**: Temporal diversity for PNG formation
- **Small-world Networks**: Optimal topology for polychronization
- **Recurrence Quantification Analysis (RQA)**: PNG validation framework

## Cross-references

- [[topology-neural-networks]]: Network topology effects
- [[spiking-neural-network-analysis]]: SNN computational frameworks
- [[stdp-spiking-transformer-attention]]: STDP in modern architectures
- [[neural-manifold-learning-dynamics]]: Manifold-based neural analysis

## References

1. Carneiro et al. (2026). arXiv:2606.25874v1
2. Izhikevich (2006). Polychronization: computation with spikes
3. Watts & Strogatz (1998). Collective dynamics of small-world networks
4. Marwan et al. (2007). Recurrence plots for complex systems analysis