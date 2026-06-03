---
name: brain-critical-dynamics-hierarchical
version: v1.0.0
last_updated: 2026-05-29
description: Hierarchical organization of critical brain dynamics. Analyze how brain networks exhibit critical behavior across multiple scales, including neuronal avalanches, power-law distributions, and long-range temporal correlations. Use when studying brain criticality, neural avalanches, scale-free dynamics, phase transitions in neural systems, or multi-scale brain network analysis. Combines renormalization group theory, statistical physics, and network science approaches.
---

# Brain Critical Dynamics - Hierarchical Organization

## Overview

This skill provides methodology for analyzing hierarchical organization of critical brain dynamics. Brain networks exhibit critical behavior at multiple scales, from neuronal avalanches to large-scale functional connectivity patterns, enabling optimal information processing and adaptability.

## Key Concepts

### Critical Brain Hypothesis
- Brain operates near a critical point between ordered and disordered states
- Criticality maximizes information capacity, transmission, and computational capabilities
- Evidence: neuronal avalanches, power-law scaling, long-range temporal correlations

### Hierarchical Organization
- **Microscale**: Single neurons, local circuits, synaptic dynamics
- **Mesoscale**: Cortical columns, brain regions, functional modules
- **Macroscale**: Whole-brain networks, global functional connectivity

### Criticality Measures
- Neuronal avalanche size distribution (power-law: P(S) ~ S^(-α))
- Branching parameter σ ≈ 1 (critical branching process)
- Long-range temporal correlations (detrended fluctuation analysis)
- Phase synchronization dynamics

## Research Methodology

### 1. Avalanche Analysis
```python
# Detect neuronal avalanches from time series
import numpy as np

def detect_avalanches(activity, threshold):
    # Activity above threshold
    supra_threshold = activity > threshold
    
    # Avalanche boundaries
    avalanche_starts = np.where(supra_threshold & ~supra_threshold[:-1])[0]
    avalanche_ends = np.where(supra_threshold & ~supra_threshold[1:])[0]
    
    # Calculate avalanche sizes and durations
    avalanches = []
    for start, end in zip(avalanche_starts, avalanche_ends):
        size = np.sum(activity[start:end])
        duration = end - start
        avalanches.append({'size': size, 'duration': duration})
    
    return avalanches

def power_law_fit(sizes, min_size=None):
    # Fit power-law: P(S) ~ S^(-α)
    import scipy.stats as stats
    
    sizes = np.array(sizes)
    if min_size is None:
        min_size = sizes.min()
    
    sizes = sizes[sizes >= min_size]
    log_sizes = np.log(sizes)
    
    # Maximum likelihood estimation
    alpha = 1 + len(sizes) / np.sum(log_sizes - np.log(min_size))
    
    return alpha
```

### 2. Branching Parameter Analysis
```python
def branching_parameter(activity_history):
    # σ = ⟨A(t+1)⟩ / ⟨A(t)⟩ for activity propagation
    # Critical point: σ ≈ 1
    
    mean_next = np.mean(activity_history[1:])
    mean_current = np.mean(activity_history[:-1])
    
    sigma = mean_next / mean_current
    
    return sigma

def criticality_test(sigma, n_trials=1000):
    # Bootstrap confidence interval
    bootstrap_sigmas = []
    for _ in range(n_trials):
        sample = np.random.choice(activity_history, size=len(activity_history))
        bootstrap_sigmas.append(branching_parameter(sample))
    
    ci_lower = np.percentile(bootstrap_sigmas, 2.5)
    ci_upper = np.percentile(bootstrap_sigmas, 97.5)
    
    # Critical if 1 is within CI
    is_critical = ci_lower <= 1 <= ci_upper
    
    return is_critical, (ci_lower, ci_upper)
```

### 3. Multi-Scale Analysis
```python
def renormalization_group_analysis(network, scales):
    # Apply RG transformation across scales
    # Coarse-grain network while preserving critical properties
    
    coarse_grained_networks = []
    for scale in scales:
        # Block transformation
        blocks = create_blocks(network, scale)
        coarse_network = aggregate_blocks(blocks)
        coarse_grained_networks.append(coarse_network)
    
    # Check scale-invariant properties
    for net in coarse_grained_networks:
        alpha = power_law_fit(get_avalanche_sizes(net))
        # α should be constant across scales
    
    return coarse_grained_networks
```

### 4. Phase Transition Analysis
```python
def detect_phase_transition(connectivity_matrix, control_parameter):
    # Critical point detection
    # Control parameter: coupling strength, synaptic weight
    
    eigenvalues = np.linalg.eigvals(connectivity_matrix)
    max_eigenvalue = np.max(np.abs(eigenvalues))
    
    # Phase transition when λ_max approaches 1
    distance_to_critical = abs(1 - max_eigenvalue)
    
    return distance_to_critical, max_eigenvalue
```

## Experimental Framework

### Data Collection
- **MEG/EEG**: High temporal resolution, detect avalanches
- **fMRI**: Large-scale functional networks
- **Multi-electrode arrays**: Local circuit criticality

### Analysis Pipeline
1. Preprocess data (artifact removal, filtering)
2. Detect events/avalanches
3. Calculate size and duration distributions
4. Fit power-law exponents
5. Test criticality criteria
6. Multi-scale comparison

## Theoretical Background

### Critical Branching Process
- Each active neuron activates ~1 downstream neuron
- σ = ⟨descendants⟩ / ⟨ancestors⟩ = 1 at criticality
- Subcritical (σ < 1): rapid extinction
- Supercritical (σ > 1): runaway activation

### Universal Critical Exponents
- Avalanche size: α ~ 1.5 (mean-field)
- Avalanche duration: τ ~ 2.0 (mean-field)
- Size-duration relation: S ~ D^(γ), γ = (α-1)/(τ-1)

### Griffiths Phase
- Extended critical region in modular networks
- Slow dynamics, broad distribution of relaxation times
- Explains variability across individuals

## Applications

### Clinical
- **Seizure prediction**: deviation from criticality
- **Neurodegeneration**: loss of critical dynamics
- **Depression**: altered brain criticality

### Cognitive
- **Decision making**: optimal information processing
- **Learning**: criticality enables plasticity
- **Consciousness**: critical brain hypothesis

### Computational
- **Neural network design**: criticality-inspired architectures
- **Reservoir computing**: critical dynamics for memory
- **Spiking networks**: self-organized criticality

## Key References

1. Beggs & Plenz (2003) - Neuronal avalanches in neocortical circuits
2. Chialvo (2010) - Emergent complex neural dynamics
3. Haldeman & Beggs (2005) - Critical branching in cultured networks
4. Linkenkaer-Hansen et al. (2001) - Long-range temporal correlations
5. Friedman et al. (2012) - Universal critical exponents

## Pitfalls

1. **False power-law**: Check goodness-of-fit, compare with alternative distributions
2. **Finite-size effects**: Scale-dependent exponents in small systems
3. **Stationarity assumption**: Brain criticality may be dynamic
4. **Noise contamination**: Avalanche detection requires careful thresholding
5. **Indirect measures**: fMRI temporal resolution limits avalanche detection

## Verification Steps

1. Bootstrap confidence intervals for exponents
2. Compare with log-normal/exponential distributions
3. Check scale-invariance across resolutions
4. Validate branching parameter with surrogate data
5. Cross-validate with multiple criticality measures

## Activation Triggers

- Keywords: neuronal avalanche, critical brain, power-law, brain criticality, phase transition, scale-free dynamics
- Tasks: analyze brain network dynamics, test criticality hypothesis, multi-scale brain analysis
- Data: MEG avalanche data, fMRI functional connectivity, neural spike trains

---

**Created**: 2026-05-29
**Category**: neuroscience
**Tags**: criticality, brain-dynamics, multi-scale, avalanches, phase-transitions
