---
name: probability-geometry-schwinger-dyson
description: Score-mismatch field methodology for probing probability geometry using Schwinger-Dyson identities. Bridges statistical mechanics, information theory, and quantum field theory through geometric interpretation of equilibrium violations.
version: 1.0
created: 2026-06-26
tags: [statistics, probability, schwinger-dyson, fisher-information, equilibrium, quantum-field-theory]
source: arXiv:2606.27360
trigger_words: [schwinger-dyson, score mismatch, fisher information, probability geometry, configurational temperature, equilibrium detection]
---

# Probability Geometry via Schwinger-Dyson Identities

## Overview

Geometric interpretation of Schwinger-Dyson identities using a universal score-mismatch field that characterizes departure from equilibrium. Connects statistical mechanics, information theory, and field theory.

## Core Framework

### Score-Mismatch Field

For any sampled distribution Q and equilibrium measure P_eq, define:

```
δs = ∇log(Q / P_eq)
```

This single field controls ALL Schwinger-Dyson violations.

### Key Theorems

1. **Universality**: Every Schwinger-Dyson violation = projection of δs onto a probe direction
2. **Fisher Identity**: Relative Fisher information = ||δs||² (squared norm)
3. **Universal Bound**: Fisher information bounds all Schwinger-Dyson violations simultaneously

### Practical Formula

```
SD_violation(probe_direction) = <δs, probe_direction>
Fisher_information = E[||δs||²]
```

## Applications

### MCMC Equilibrium Monitoring
- Compute score-mismatch field from MCMC samples
- Fisher information gives single-number convergence diagnostic
- More sensitive than traditional autocorrelation measures

### Statistical Model Validation
- Compare empirical distribution Q to model P_eq
- Score-mismatch reveals specific directions of misfit
- Fisher information quantifies overall model adequacy

### Quantum Field Theory
- Check consistency of sampled field configurations
- Schwinger-Dyson violations indicate systematic errors
- Configurational temperature as observable diagnostic

### Non-equilibrium Detection
- δs ≠ 0 iff system is out of equilibrium
- Direction of δs indicates which observables are most biased
- Magnitude ||δs|| gives overall departure strength

## Implementation Steps

1. **Define equilibrium measure** P_eq for your system
2. **Sample distribution** Q from your process
3. **Compute score-mismatch** δs = ∇log(Q/P_eq)
4. **Calculate Fisher information** as ||δs||²
5. **Project onto probes** to identify specific violations
6. **Use universal bound** to certify overall consistency

## Pitfalls

- Fisher information may diverge if Q has support outside P_eq
- Numerical estimation of ∇log(Q/P_eq) requires careful density estimation
- High-dimensional systems need dimension reduction for tractable δs
- Configurational temperature assumes ergodicity

## References

- arXiv:2606.27360 - Probing Probability Geometry with Schwinger-Dyson Identities