# Penalty-Free Quantum Annealing for Portfolio Optimization (arXiv: 2605.17628)

## Paper Summary
**Title**: A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization  
**Author**: Luis Lozano  
**Date**: 2026-05-17

## Key Findings
- **Problem**: Standard penalty encoding is the binding constraint for direct-QPU execution on D-Wave Pegasus and Zephyr hardware
- **Root Cause**: Expanding the exact cardinality penalty contributes a dense rank-one term that makes the logical interaction graph complete regardless of covariance density
- **Results**: Chain-break fractions from 83% (small universes) up to 92% (full 49-industry Fama-French universe), zero feasible raw samples at every scale
- **Solution**: Remove penalty entirely → sample objective-only QUBO → enforce cardinality classically through deterministic feasibility projector
- **Outcome**: Reduces mean chain-break fractions from 71-92% down to at most 0.04%, post-processed regret at most 0.03% relative to greedy classical references
- **Important**: Does NOT claim quantum advantage; penalty encoding (not sparse hardware topology) is the limiting factor

## Reusable Patterns

### 1. Penalty-Free QUBO Formulation
```
QUBO = -returns + risk * covariance  (NO cardinality penalty)
```
Enforce cardinality constraint classically after quantum sampling.

### 2. Deterministic Feasibility Projector
- If too many assets selected: remove lowest-return assets
- If too few assets selected: add highest-return unselected assets
- Post-processing step dominates solution quality (not QPU sampling)

### 3. Topology-Aware Sparsification Warning
Removing off-diagonal entries reduces chain breaks but dilutes the cardinality constraint. Sparsify-and-project pipeline is dominated by the classical projector.
