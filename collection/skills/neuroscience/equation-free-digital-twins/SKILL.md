---
name: equation-free-digital-twins
description: >
  Equation-free digital twin framework using Koopman operator theory and Hankel-matrix embeddings
  for real-time structural state reconstruction without physical models. Use when: (1) building
  digital twins for complex engineering structures, (2) virtual sensing from partial observations,
  (3) Koopman-based system identification, (4) real-time monitoring of nonlinear structural dynamics.
---

# Equation-Free Digital Twins via Koopman-Hankel Framework

## Core Methodology (arXiv:2605.00950)

Build digital twins for high-dimensional engineering structures using **Koopman operator theory**,
**Hankel-matrix embeddings**, and **dynamic mode decomposition (DMD)** — no mass/stiffness matrices required.

## Key Concepts

### Koopman Operator Theory
- Lifts nonlinear dynamics into a linear invariant subspace
- Enables linear analysis tools on inherently nonlinear systems
- Infinite-dimensional operator approximated via finite-dimensional projection

### Hankel-Matrix Embedding
- Constructs trajectory-based state-space from input-output data
- Captures system dynamics through time-delayed observations
- Rank-optimized to separate physical modes from noise/harmonics

### Virtual Sensing
- Reconstruct unmeasured states from limited sensor data
- Rolling-horizon strategy for real-time estimation
- Achieves R-squared > 0.95 at 1 Hz, > 0.99 at higher rates

## Workflow

### Step 1: Collect Operational Data
Gather time-series from available sensors. No input measurements needed (input-blind).

### Step 2: Build Hankel Matrix
Construct trajectory-based Hankel matrix from time-delayed sensor observations.
Use past/future windows to capture system dynamics.

### Step 3: Koopman-Hankel Decomposition
1. SVD of Hankel matrix: H = U * S * V^T
2. Truncate to dominant modes via rank optimization (gap statistic)
3. Extract Koopman eigenvalues and modes
4. Separate structural resonances from deterministic harmonics (e.g., 3P rotor)

### Step 4: Virtual Sensing (Rolling-Horizon)
Project partial observations into Koopman subspace, evolve using Koopman dynamics,
map back to physical coordinates for full-state reconstruction.

### Step 5: Predictability Analysis
Estimate Lyapunov time from Koopman eigenvalues to define predictability horizon.
Example: ~1.0 s for floating offshore wind turbine.

## Validation Metrics
- R-squared at 1 Hz: > 0.95
- R-squared at higher rates: > 0.99
- Mode separation: reliable with rank optimization
- Predictability horizon: ~1.0 s Lyapunov time

## Applications
- Floating offshore wind turbine monitoring
- Bridge and building structural health monitoring
- Aerospace structure vibration analysis
- Any system with partial observability + nonlinear dynamics

## Pitfalls
- Rank selection critical: too low loses dynamics, too high overfits noise
- 3P rotor harmonics can mask structural resonances without proper separation
- Requires sufficient data length for reliable Hankel construction
- Predictability horizon limits forecasting range

## Reference
arXiv:2605.00950 — Abaei, BahooToroody, Polojarvi, Remes (2026)
