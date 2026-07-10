---
name: geometric-quantum-pinn
description: >
  Geometric Quantum Physics-Informed Neural Network (GQPINN) methodology for
  solving PDEs with symmetry-aware quantum circuits. Combines geometric quantum
  machine learning with physics-informed neural networks. Use when solving PDEs
  with quantum circuits, incorporating symmetry/inductive biases into quantum
  models, or designing equivariant quantum ansatzes for scientific ML.
  Activation: geometric quantum, symmetry-aware PINN, quantum PDE solver,
  equivariant quantum circuit, GQPINN, quantum physics-informed neural network.
---

# Geometric Quantum Physics-Informed Neural Network (GQPINN)

## Overview

GQPINNs extend Quantum PINNs (QPINNs) by encoding the geometric structure of
the underlying PDE directly into the quantum circuit ansatz. This produces
symmetry-preserving predictions that respect the governing equation's
invariances, achieving better accuracy with fewer trainable parameters.

## Core Methodology

### Step 1: Identify PDE Symmetries

Analyze the target PDE for symmetries:
- **Finite group symmetries**: Discrete transformations (reflections, permutations)
- **Compact Lie group symmetries**: Continuous transformations (rotations, translations)
- **Scale invariances**: Rescaling of independent/dependent variables

### Step 2: Construct Equivariant Generator Sets

For each identified symmetry, build parametrized circuit generators:

```python
# For a finite group G = {g_1, ..., g_k}:
# Build generators U(θ) that satisfy: U(θ) · ρ(g) = ρ(g) · U(θ)
# where ρ(g) is the group representation on the quantum state

# For Lie groups: use exponential map exp(i·θ·X) where X are Lie algebra generators
```

### Step 3: Twirling-Based Symmetry Preservation

Apply group twirling to enforce symmetry:

```
U_sym(θ) = (1/|G|) Σ_{g∈G} ρ(g)† · U(θ) · ρ(g)
```

This ensures model predictions respect PDE symmetries when boundary/initial
data are symmetry-compatible.

### Step 4: Quantum Circuit Ansatz Design

Combine symmetry generators with trainable parameters:
- **Equivariant layers**: Apply symmetry-preserving transformations
- **Physics loss terms**: PDE residuals at collocation points
- **Boundary conditions**: Enforced via penalty or hard constraints

### Step 5: Training Protocol

1. Sample collocation points from domain
2. Evaluate quantum circuit at each point → prediction u_θ(x,t)
3. Compute PDE residual via automatic differentiation
4. Loss = PDE_residual + BC_penalty + IC_penalty
5. Optimize with gradient-based methods

## Advantages Over Standard PINNs/QPINNs

| Metric | PINN | QPINN | GQPINN |
|--------|------|-------|--------|
| Parameters | High | Medium | Low |
| Symmetry compliance | No | Partial | Guaranteed |
| Generalization | Baseline | Improved | Best |
| Training cost | High | Medium | Lower |

## Key Design Patterns

### Pattern 1: Symmetry Detection → Circuit Construction

```
PDE Analysis → Symmetry Group → Generator Sets → Twirling → Ansatz
```

### Pattern 2: Matched Training Protocols

When benchmarking GQPINNs against baselines:
- Use identical training point distributions
- Match optimization hyperparameters
- Compare at equal parameter counts
- Report mean absolute error (MAE) as primary metric

## PDE Categories for Application

- **Linear PDEs**: Heat equation, wave equation, Schrödinger equation
- **Nonlinear PDEs**: Burgers equation, KdV equation, Navier-Stokes
- **Geometric PDEs**: Problems on manifolds with intrinsic symmetries

## Implementation Notes

- Use parameterized quantum circuits (PQCs) as base ansatz
- Number of qubits scales with problem complexity
- Twirling can be approximated via random sampling for large groups
- For continuous groups, discretize to finite subgroup for practical twirling

## References

- GQPINN paper: arxiv:2605.02352 (Tam, Safari, Matsuyama, 2026)
- Geometric Quantum Machine Learning: Meyer et al. (2022)
- Physics-Informed Neural Networks: Raissi et al. (2019)
