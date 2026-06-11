---
name: dynamical-quantum-optimal-transport
description: "Dynamical quantum optimal transport (QOT) methodology based on Benamou-Brenier formulation for computing geodesics between positive semidefinite matrices. Use when: computing quantum state transport distances, solving quantum chemistry problems via optimal transport, analyzing numerical convergence of QOT distances, or implementing interior-point methods for quantum density matrix geodesics. Activation: quantum optimal transport, dynamical QOT, Benamou-Brenier, quantum chemistry optimal transport, density matrix geodesic, interior-point quantum transport, positive semidefinite transport"
metadata:
  arxiv_id: "2606.10075"
  published: "2026-06-08"
  authors: "Genevieve Dusson, Virginie Ehrlacher, Etienne Obermeyer"
---

# Dynamical Quantum Optimal Transport

**Source**: arXiv:2606.10075 — "An algorithm for dynamical quantum optimal transport with applications to quantum chemistry" by Genevieve Dusson, Virginie Ehrlacher, Etienne Obermeyer (2026-06-08)

## Overview

Numerical study of dynamical quantum optimal transport distances based on the Benamou-Brenier formulation adapted to spaces of density matrices. Introduces an interior-point regularized method to compute geodesics between positive semidefinite matrices with applications to quantum chemistry.

## Core Methodology

### Benamou-Brenier Formulation for Quantum States

The classical Benamou-Brenier formulation expresses the Wasserstein-2 distance as a dynamical optimization problem over continuous paths of probability measures. The quantum extension replaces probability measures with density matrices (positive semidefinite matrices with unit trace):

```
W_2(ρ_0, ρ_1)² = inf ∫₀¹ Tr(ρ_t · L_{ρ_t}⁻¹(v_t)²) dt
```

where ρ_t is a path of density matrices, v_t is the velocity field, and L_{ρ_t} is a quantum transport operator.

### Interior-Point Regularized Method

1. **Parameterize the path**: Represent ρ_t as a smooth curve in the space of PSD matrices
2. **Add barrier function**: Log-det barrier to enforce positive definiteness: `-μ · log det(ρ_t)`
3. **Discretize time**: Split [0,1] into N intervals, optimize over discrete sequence {ρ_k}
4. **Solve via interior-point**: Use Newton-type method with barrier parameter μ → 0

### Numerical Properties

- **Convergence**: Objects converge as matrix size increases
- **Visualization**: Results expressed as integral kernels and densities
- **Parameter tuning**: Appropriate parameters approximate certain quantum chemistry problems

## Implementation Steps

### Step 1: Define the QOT Problem

```python
import numpy as np
from scipy.linalg import sqrtm

def qot_cost(rho0, rho1, n_steps=10, mu=1e-4):
    """Compute dynamical QOT distance between two density matrices."""
    # Discretize path: rho_k for k = 0, ..., n_steps
    # Interior-point objective: sum of kinetic + barrier terms
    pass
```

### Step 2: Interior-Point Optimization

```python
def interior_point_qot(rho0, rho1, n_steps, mu_init, tol=1e-8):
    """Interior-point method for dynamical QOT."""
    mu = mu_init
    # Initialize path as linear interpolation
    path = [rho0 + (rho1 - rho0) * k / n_steps for k in range(n_steps + 1)]
    
    while mu > tol:
        # Newton step on regularized objective
        # Decrease mu
        # Check convergence
        pass
    return path
```

### Step 3: Quantum Chemistry Application

The dynamical QOT distance can approximate:
- Electronic structure comparisons
- Molecular orbital transport costs
- State preparation costs in quantum algorithms

## Key Results

1. **Interior-point method** successfully computes geodesics between PSD matrices
2. **Numerical convergence** established as matrix size increases
3. **Quantum chemistry approximation** possible with appropriate parameter tuning
4. **Visualization framework** via integral kernels and densities

## Pitfalls

1. **Parameter sensitivity**: QOT distances depend critically on the choice of regularization parameter μ and discretization resolution N
2. **Positive definiteness**: The barrier method requires strictly positive definite matrices — near-singular density matrices need regularization
3. **Computational cost**: Interior-point methods scale as O(n³) per Newton step for n×n matrices
4. **Not a replacement for all quantum chemistry methods**: QOT approximation is complementary to standard quantum chemistry methods (DFT, coupled cluster)

## Activation

- quantum optimal transport, dynamical QOT, Benamou-Brenier
- quantum chemistry optimal transport
- density matrix geodesic
- interior-point quantum transport
- positive semidefinite transport
- 量子最优传输, 动力学量子最优传输, 量子化学最优传输
