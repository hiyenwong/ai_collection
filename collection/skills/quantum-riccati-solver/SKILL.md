---
name: quantum-riccati-solver
description: "Quantum algorithms for solving algebraic Riccati equations via Riesz projectors and quantum singular value transformations (QSVT). Applications to quantum chemistry RPA and coupled-cluster theory. Activation: quantum riccati, quantum nonlinear matrix, quantum chemistry algorithm, RPA quantum, algebraic riccati equation quantum, quantum singular value transformation chemistry."
---

# Quantum Solvers for Nonlinear Matrix Equations

> Quantum algorithm for solving algebraic Riccati equations using Riesz projectors onto invariant subspaces, implemented via contour-integral resolvents and QSVT, with applications to quantum-chemical RPA and coupled-cluster theory. (arXiv:2605.16189)

## Metadata
- **Source**: arXiv:2605.16189
- **Authors**: Pablo Rodenas-Ruiz, Andrew Zhao, Joonho Lee
- **Published**: 2026-05-15
- **Categories**: quant-ph, physics.chem-ph

## Core Methodology

### Key Innovation
First quantum algorithm framework for solving **algebraic Riccati equations** - a fundamental class of nonlinear matrix equations ubiquitous in control theory, quantum chemistry, and many-body physics. The method achieves **linear scaling in system size** and **polynomial scaling in excitation rank**, suggesting exponential advantage over classical local-correlation heuristics.

### Technical Framework

1. **Block-Encoding via Riesz Projectors**
   - Riccati solutions are encoded as Riesz projectors onto invariant subspaces of an associated non-normal matrix
   - The projector P = (1/2πi) ∮_Γ (zI - A)^(-1) dz captures the stabilizing solution
   - Contour Γ encloses eigenvalues corresponding to the stable invariant subspace

2. **Contour-Integral Resolvent Implementation**
   - The resolvent (zI - A)^(-1) is approximated using quantum linear system algorithms (QLSA)
   - Contour integration discretized via quadrature: sum of weighted resolvent evaluations
   - Each resolvent evaluation implemented as a block-encoded linear system solve

3. **Quantum Singular Value Transformation (QSVT)**
   - Polynomial transformations of block-encoded matrices extract the projector
   - QSVT provides optimal gate complexity for matrix function approximation
   - Enables efficient estimation of correlation-energy density from the solution

4. **Application to RPA (Random-Phase Approximation)**
   - m-particle, m-hole RPA reduces to a Riccati equation for cluster amplitudes
   - Under localized-orbital sparsity: O(N) system-size scaling, poly(m) excitation-rank scaling
   - Exponential advantage in m over classical local-correlation methods

## Implementation Guide

### Prerequisites
- QSVT / quantum signal processing library
- Quantum linear system solver (HHL variant or QSVT-based)
- Block-encoding primitives for the problem matrix A

### Step-by-Step

1. **Formulate the Riccati Equation**
   ```
   A^T X + X A - X B X + C = 0
   ```
   Identify the associated Hamiltonian matrix H = [[A, -B], [-C, -A^T]]

2. **Construct Block-Encoding of H**
   - Decompose H into efficiently implementable unitary blocks
   - Ensure normalization ||H|| ≤ 1 for QSVT compatibility

3. **Define Contour and Quadrature**
   - Choose contour Γ enclosing stable eigenvalues
   - Discretize via trapezoidal or Gauss-Legendre quadrature
   - Number of quadrature points O(log(1/ε)) for ε precision

4. **Implement QSVT-Based Projector**
   - Design polynomial approximation of the indicator function
   - Apply QSVT to block-encoded H
   - Extract projector onto stable subspace

5. **Estimate Observables**
   - Compute correlation-energy density: E_corr = Tr(X · C)
   - Use amplitude estimation for quadratic speedup in sampling

### Code Example (Pseudocode)
```python
# Block-encode the Hamiltonian matrix
H_block = block_encode(H, precision=epsilon)

# Define contour quadrature points
z_points, weights = contour_quadrature(stable_eigenvalues, n_points=O(log(1/eps)))

# Evaluate resolvents via QLSA
projector = sum(w * qlsolve(z_i * I - H_block) for z_i, w in zip(z_points, weights))

# Extract Riccati solution from projector blocks
X = extract_solution(projector)

# Estimate correlation energy
E_corr = amplitude_estimate(lambda X: trace(X @ C))
```

## Applications
- Quantum chemistry: RPA, higher-order RPA, coupled-cluster theory
- Control theory: optimal control, Kalman filtering, LQR
- Many-body physics: Green's function calculations, self-consistent field methods
- Machine learning: discrete-time Riccati equations in filtering/smoothing

## Pitfalls
- **Non-normal matrices**: Standard QSVT assumes normal/Hermitian matrices; non-normal H requires careful block-encoding design
- **Sparsity assumptions**: Linear scaling relies on localized-orbital sparsity; dense systems revert to polynomial scaling
- **Contour selection**: Poor contour choice leads to ill-conditioned resolvents; eigenvalue gap must be bounded away from zero
- **QSVT degree**: Polynomial degree scales with condition number; ill-conditioned problems require high-degree polynomials
- **State preparation**: Input state quality directly affects solution accuracy

## Related Skills
- quantum-block-encoding-linear-algebra
- quantum-linear-algebra-block-encoding
- qsvt-quantum-signal-processing
- quantum-chemistry-algorithms
- quantum-algorithm-framework-designer