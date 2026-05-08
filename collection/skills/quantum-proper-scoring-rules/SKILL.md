---
name: quantum-proper-scoring-rules
description: >
  Apply proper scoring rules to quantum state estimation and forecasting.
  Generalizes classical scoring rules (Brier, logarithmic, spherical) to 
  the quantum domain using density operators and operator convex generators.
  Use when performing quantum state tomography, designing quantum sensors,
  building incentive-compatible quantum data markets, or analyzing the 
  economic value of quantum resources (coherence, entanglement, adaptivity)
  in forecasting tasks. Establishes minimax bounds via the Quantum 
  Cramér-Rao-McCarthy Bound.
---

# Quantum Proper Scoring Rules

## Overview

Proper scoring rules evaluate the quality of probabilistic forecasts. In the
quantum domain, probability distributions are replaced by **density operators**,
and scoring rules become **Quantum Value Functionals**.

## Core Framework

### Quantum Value Functionals
Defined via operator convex generators G:
- S(ρ, σ) = Tr[G(σ)] + Tr[G'(σ)(ρ - σ)]
- Proper when maximized at σ = ρ (truthful reporting)

### Key Examples
- **Quantum Brier Score**: G(ρ) = -Tr[ρ²] (quadratic loss)
- **Quantum Log Score**: G(ρ) = -Tr[ρ log ρ] = S_vN(ρ) (von Neumann entropy)
- **Quantum Spherical Score**: Based on operator norm

### Quantum Cramér-Rao-McCarthy Bound
- Links minimax estimation risk to:
  1. Curvature of the generating function
  2. Quantum Fisher Information (QFI)
- Generalizes the classical Cramér-Rao bound to quantum domain
- Provides fundamental limits on quantum state estimation accuracy

## Resource-Theoretic Advantages

### Quantum vs Classical Estimation
- Quantum strategies can achieve exponentially better sample complexity
- Resources that provide advantage:
  - **Coherence**: Superposition in measurement basis
  - **Entanglement**: Correlated measurements across copies
  - **Adaptivity**: Sequential measurement strategies

### Scaling Separations
- Classical (single-copy measurements): O(n) copies for n-qubit state
- Quantum (joint measurements): O(1) to O(log n) copies
- Exponential separation for certain estimation tasks

## Applications

1. **Quantum State Tomography**: Optimal measurement strategies
2. **Quantum Sensor Design**: Incentive-compatible scoring for sensor networks
3. **Quantum Data Markets**: Pricing quantum information based on estimation value
4. **Robust QML**: Scoring-based training for quantum machine learning
5. **Metrology**: Fundamental limits on parameter estimation precision

## Methodology

1. **Choose scoring rule**: Based on application (Brier for quadratic, Log for information)
2. **Compute Quantum Fisher Information**: For the parameter of interest
3. **Apply Cramér-Rao-McCarthy Bound**: Get fundamental precision limit
4. **Compare classical vs quantum**: Quantify quantum advantage
5. **Design measurements**: Optimize measurement POVMs for chosen scoring rule

## Activation Keywords
- quantum scoring rules
- quantum state estimation
- quantum Cramer-Rao bound
- quantum Fisher information
- quantum tomography scoring
- quantum forecasting
- quantum data markets
- quantum metrology bounds
