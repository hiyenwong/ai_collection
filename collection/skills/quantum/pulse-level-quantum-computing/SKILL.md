---
name: pulse-level-quantum-computing
description: >
  Pulse-level quantum computing skill — design, optimize, and analyze pulse-level
  variational quantum algorithms beyond the gate abstraction.
  Covers pulse parameterization, expressibility, Fourier coefficient correlation (FCC),
  composite gate sub-angle decomposition, and training landscape optimization.
  Use when: pulse-level quantum computing, variational quantum algorithms,
  quantum machine learning at pulse level, Fourier quantum models,
  QFM optimization, pulse parameterization, quantum compilation optimization.
  Triggered by papers like "Beyond Gates: Pulse Level Quantum Fourier Models" (arXiv:2605.04945).
---

# Pulse-Level Quantum Computing

## Overview

Pulse-level quantum computing bypasses the gate abstraction layer and operates directly
on microwave/hardware parameters. This provides finer control over quantum operations
and fundamentally changes the optimization landscape for variational quantum algorithms.

## Core Concepts

### Pulse Parameterization

- Traditional gate-level: single logical angle per gate
- Pulse-level: multiple independently tunable sub-angles per composite gate
- Independent pulse scalings replace rigid monomial couplings
- Provides higher-dimensional escape routes for gradient descent

### Expressibility & Fourier Coefficient Correlation (FCC)

- Control over pulse shapes does NOT significantly alter global expressibility
- Structural correlations of the Ansatz remain largely unchanged
- Key benefit: local optimization landscape is fundamentally altered
- FCC measures correlation structure in Fourier coefficient space

### Composite Gate Sub-Angle Decomposition

- A single gate angle is decomposed into multiple sub-angles via pulse control
- Decouples local parameter constraints
- Significantly boosts training performance
- Analytically provable advantage over gate-level parameterization

## Workflow

### Step 1: Analyze Pulse vs Gate Trade-offs

- Global expressibility: similar between pulse and gate level
- Local optimization: pulse level provides significant advantage
- Training performance: pulse level outperforms due to relaxed constraints
- Hardware cost: pulse level requires direct hardware access

### Step 2: Design Pulse-Level Ansatz

1. Start from existing gate-level circuit
2. Decompose each gate into pulse parameters
3. Add independent pulse scaling parameters
4. Identify which gates benefit most from pulse control

### Step 3: Optimize Training

- Use gradient descent with expanded parameter space
- Monitor Fourier coefficient correlation for overfitting
- Compare convergence speed with gate-level baseline
- Validate on target Fourier series with matching frequencies

### Step 4: Validate Results

- Check expressibility metrics remain comparable
- Verify training speedup is statistically significant
- Ensure physical realizability on target hardware
- Document pulse parameters for reproducibility

## Key Findings from Literature

### Beyond Gates: Pulse Level QFMs (arXiv:2605.04945)

- Pulse shapes do not significantly alter global expressibility
- Independent pulse scalings replace single logical angles
- Relaxes rigid monomial couplings from gate-level parameterization
- Provides gradient descent with higher-dimensional escape routes
- Numerically validated on exponential (ternary) feature maps

## Practical Applications

- Variational quantum algorithms (VQAs)
- Quantum machine learning with Fourier models
- Quantum circuit optimization
- Near-term NISQ device optimization
- Quantum control optimization

## References

- Beyond Gates: Pulse Level Quantum Fourier Models — Strobl et al. (arXiv:2605.04945)
