---
name: leggett-garg-neural-dynamics
description: "Leggett-Garg inequality testing methodology for neural dynamics — probing non-diffusive stochastic structure in single neurons. Applies quantum temporal correlation analysis to distinguish diffusive (Wiener/cable-equation) models from persistent stochastic models in neural systems."
tags: ["quantum", "neuroscience", "leggett-garg", "neural-dynamics", "temporal-correlations"]
---

# Leggett-Garg Neural Dynamics Testing

## Description

Leggett-Garg inequality (LGI) testing methodology for probing non-diffusive stochastic structure in single-neuron dynamics. The LGI serves as a temporal analogue of Bell-type constraints, distinguishing between Markovian diffusive models (Wiener/cable-equation) and non-diffusive persistent stochastic models based on Kac-type finite-velocity processes leading to the Telegrapher's equation.

## Activation Keywords

- leggett-garg neural
- temporal correlations neuron
- non-diffusive neural dynamics
- quantum-like neural testing
- LGI neuron dynamics
- Kac process neural
- Telegrapher equation brain
- persistent stochastic neuron

## Theoretical Foundation

### Two Classes of Stochastic Neural Dynamics

**Class 1: Diffusive Models**
- Based on Wiener noise and cable equation
- Markovian, trajectory-based
- Monotonic decay of temporal correlations
- Always satisfies Leggett-Garg inequalities

**Class 2: Persistent Stochastic Models**
- Finite-velocity stochastic processes (Kac-type)
- Non-Markovian, memory effects
- Oscillatory temporal correlations
- Can violate Leggett-Garg inequalities

### Key Mathematical Objects

- **Telegrapher's Equation**: Arises from Kac-type finite-velocity processes
- **Analytic Continuation**: Connection between Kac processes and Dirac-like envelope equations
- **Leggett-Garg Inequality**: Temporal analogue of Bell constraints
- **Temporal Correlations**: Measure persistence and memory in neural dynamics

## Methodology

### Step 1: Define Measurement Protocol

Select three measurement times t1 < t2 < t3 for temporal correlation testing.
The LGI tests: K = C(t1,t2) + C(t2,t3) - C(t1,t3) <= 1
where C(ti,tj) are two-time correlation functions.

### Step 2: Experimental Design

- Record single-neuron voltage or spike dynamics
- Perform repeated measurements at specified time intervals
- Compute two-time correlation functions C(ti,tj)
- Test whether K exceeds the classical bound of 1

### Step 3: Interpretation

**LGI Satisfied (K <= 1)**: Dynamics consistent with trajectory-based diffusive models
**LGI Violated (K > 1)**: Evidence of non-diffusive temporal correlations, memory effects, and contextual temporal structure

### Conservative Interpretation

Violation is NOT evidence of microscopic quantum coherence in the brain. Rather, it indicates:
- Persistence in stochastic dynamics
- Non-Markovian memory structure
- Contextual temporal correlations analogous to quantum systems

## Tools Used

- Statistical analysis: Correlation function computation
- Stochastic process modeling: Kac process simulation
- Telegrapher's equation: Finite-velocity transport modeling
- Time-series analysis: Neural dynamics measurement

## Applications

1. **Neural Dynamics Characterization**: Distinguish diffusive vs persistent stochastic models
2. **Memory Effect Detection**: Identify non-Markovian structure in neurons
3. **Quantum-Classical Boundary**: Probe classical systems with quantum-like temporal structure
4. **Brain-Computer Interfaces**: Better models of neural signal propagation
5. **Computational Neuroscience**: Refined models beyond cable equation

## Error Handling

### Insufficient Data
- Need sufficient repeated measurements for statistical significance
- Use bootstrapping for confidence intervals on K

### Measurement Noise
- Account for experimental noise in correlation estimation
- Use noise-robust correlation estimators

### Finite Sampling
- Discrete time sampling may miss fine temporal structure
- Use interpolation or continuous-time estimation methods

## References

- arXiv:2605.12126 - "Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons" (May 2026)
- Kac, M. (1956) - "Probability and Some of Its Applications"
- Leggett, A.J. & Garg, A. (1985) - "Quantum mechanics versus macroscopic realism"

## Examples

### Example: Single Neuron Testing

**Scenario**: Test whether hippocampal CA1 neuron dynamics show persistent stochastic behavior.

1. Record membrane potential at high temporal resolution
2. Select measurement times t1, t2, t3 spaced by ~10ms
3. Compute C(t1,t2), C(t2,t3), C(t1,t3) over repeated trials
4. Calculate K = C(t1,t2) + C(t2,t3) - C(t1,t3)
5. If K > 1 (with statistical significance), evidence of non-diffusive dynamics
