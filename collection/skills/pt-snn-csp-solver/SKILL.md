---
name: pt-snn-csp-solver
description: "Parallel Tempering integration for Spiking Neural Network-based CSP solvers — overcoming local-minimum traps in stochastic SNN optimization. From arXiv:2607.08897 (Uludag et al., Jul 2026)."
tags: ["spiking-neural-network", "constraint-satisfaction", "parallel-tempering", "stochastic-optimization", "neuromorphic"]
---

## Overview

This skill encodes the methodology from **"Breaking Local-Minimum Traps in Spiking Neural Network-Based Solvers for CSPs via Parallel Tempering"** (arXiv:2607.08897, Jul 2026) — the first integration of parallel tempering into an SNN-based CSP solver.

**Problem**: SNNs with stochastic neurons solve CSPs by encoding constraints as connectivity weights and performing probabilistic search via spike dynamics. However, fixed-temperature stochastic dynamics get trapped in local minima (near-satisfying configurations), especially on hard instances.

**Solution**: Run multiple parallel SNN replicas at varying inverse temperatures (β). Periodically exchange *temperatures* between replicas (not network states), enabling exploration of energy barriers unreachable by single-temperature dynamics.

## Core Methodology

### 1. SNN-CSP Encoding

- Map each CSP variable to a group of neurons (one-hot or binary encoding)
- Encode constraints as synaptic weights: satisfying assignments → lower energy
- Stochastic spiking provides Monte Carlo sampling of the solution space
- System converges to low-energy (near-satisfying) configurations

### 2. Parallel Tempering Integration

```
Replica 1: β₁ (high temperature) → broad exploration
Replica 2: β₂
Replica 3: β₃
Replica 4: β₄ (low temperature) → concentration near minima
```

- Each replica runs an independent SNN-CSP solver at its own inverse temperature β
- Every K steps, attempt temperature swap between adjacent replicas (Metropolis criterion)
- Accept swap with probability: `min(1, exp((β_i - β_j)(E_j - E_i)))`
- Crucially: exchange *temperatures*, not network states — preserves spike-based computation

### 3. Key Results

- **332/1000** SATLIB uf20-91 instances improved vs only **5 worsened**
- Gains concentrated on **hard instances** where fixed-temperature solvers fail
- Violation trajectory analysis confirms mechanism: temperature exchanges enable crossing energy barriers
- Equal computational budget comparison: PT vs 4 independent fixed-temperature solvers

## Implementation Patterns

### Temperature Schedule Design

- Geometric spacing: `β_i = β_min * (β_max/β_min)^(i/(n-1))`
- β_min ≈ 0.1 (high temp, uniform exploration)
- β_max ≈ 1.0+ (low temp, greedy search)
- Number of replicas scales with problem difficulty

### Swap Frequency

- Too frequent → replicas don't equilibrate at their temperature
- Too rare → insufficient mixing between temperature levels
- Empirical sweet spot: swap every 10-100 SNN timesteps

### Energy Function

- For CSP: `E = number of violated constraints`
- Can extend to weighted CSPs with constraint-specific penalties
- Energy computed from spike counts or membrane potentials

## Use Cases

- SNN-based optimization on neuromorphic hardware
- Constraint satisfaction on edge devices with low power budgets
- Any scenario where SNN energy-based search gets stuck in local minima
- Hybrid neuromorphic-classical solvers

## Pitfalls

### Temperature Exchange vs State Exchange
**Key insight**: PT exchanges *temperatures* (β values) between replicas, NOT network states. Exchanging states would break the asynchronous spike-based computation. Temperature exchange is computationally cheap and preserves the SNN's intrinsic dynamics.

### Equal-Budget Comparison
**Critical**: When evaluating PT vs baseline, use equal computational resources. A 4-replica PT system should be compared against 4 independent fixed-temperature solvers, not 1. This is the fair comparison that demonstrates PT's true value.

### Hard Instance Focus
**Finding**: PT gains concentrate on hard CSP instances. For easy instances, single-temperature solvers already perform well. PT's advantage emerges when the energy landscape has narrow basins and high barriers.

### Violation Trajectory Analysis
**Diagnostic tool**: Track constraint violations over time for each replica. PT replicas that receive higher temperatures should show violation count increases (exploration), then decreases after receiving lower temperatures (exploitation).

## Activation

spiking neural network parallel tempering, SNN CSP solver, stochastic optimization local minima, neuromorphic constraint satisfaction, energy-based SNN search, arxiv 2607.08897
