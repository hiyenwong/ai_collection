---
name: leggett-garg-neural-dynamics
description: Methodology for testing Leggett-Garg temporal correlations in neural dynamics to distinguish diffusive from non-diffusive stochastic models. Use when analyzing single-neuron dynamics, testing quantum-like temporal correlations in neural systems, probing non-Markovian structure in biological data, or distinguishing between diffusive and persistent stochastic processes. Triggered by: Leggett-Garg inequality, neural dynamics testing, Kac process, Telegrapher equation, non-diffusive neural models, temporal correlations in neurons.
---

# Leggett-Garg Neural Dynamics Testing

## Description
Test Leggett-Garg temporal correlations in single-neuron dynamics to distinguish
diffusive (Wiener/cable-equation) models from non-diffusive persistent stochastic
models based on Kac-type finite-velocity processes.

## Activation Keywords
- Leggett-Garg inequality
- neural dynamics testing
- non-diffusive neural models
- Kac process analysis
- Telegrapher equation
- temporal correlations neurons
- non-Markovian neural structure

## Core Methodology

### Step 1: Define Observable
Select neural observable O(t) (e.g., membrane potential, firing rate) at times t1, t2, t3.

### Step 2: Compute Two-Time Correlations
Calculate K(t1, t2) = <O(t1)O(t2)> from experimental or simulated data.

### Step 3: Construct Leggett-Garg Quantity
K_LG = K(t1,t2) + K(t2,t3) - K(t1,t3)

### Step 4: Test Inequality
For macrorealistic (diffusive) systems: K_LG <= 1
Violation indicates non-diffusive persistent stochastic dynamics.

### Step 5: Interpret Results
- Violation → evidence against trajectory-based diffusive description
- NOT evidence of microscopic quantum coherence
- Indicates persistence, memory, contextual temporal structure

## Mathematical Framework
- Diffusive dynamics: Wiener process, cable equation
- Non-diffusive: Kac-type finite-velocity processes → Telegrapher's equation
- Analytic continuation: Kac processes ↔ Dirac-like envelope equations

## Implementation
```python
import numpy as np

def leggett_garg_correlation(time_series, t1, t2, t3):
    """Compute Leggett-Garg correlations from time series."""
    def two_time_corr(data, ti, tj):
        return np.mean(data[ti] * data[tj])
    
    K12 = two_time_corr(time_series, t1, t2)
    K23 = two_time_corr(time_series, t2, t3)
    K13 = two_time_corr(time_series, t1, t3)
    
    return K12 + K23 - K13

# Test: violation if K_LG > 1 indicates non-diffusive dynamics
```

## Error Handling
- Ensure sufficient temporal resolution to capture correlations
- Account for measurement noise in experimental data
- Multiple measurements needed for statistical significance

## References
- Paper: arXiv:2605.12126 (Partha Ghose, 2026-05-12)
- Leggett-Garg inequalities: temporal analogues of Bell inequalities
- Kac processes: finite-velocity random walks
