---
name: symplectic-quantum-model-reduction
description: "Symplectic H2 model reduction methodology for high-dimensional linear quantum systems. Uses symplectic Petrov-Galerkin framework and Q-IRKA algorithm to reduce quantum system models while preserving physical realizability (PR) and canonical commutation relations."
---

# Symplectic Quantum Model Reduction

## Description

Symplectic H2 model reduction methodology for high-dimensional linear quantum systems. Addresses the challenge of reducing large-scale quantum system models while strictly preserving physical realizability (PR) constraints, canonical commutation relations (CCR), and quantum input-output structure. Uses a symplectic Petrov-Galerkin framework with the Quantum IRKA (Q-IRKA) algorithm.

**Source**: arXiv:2605.07152 - "Symplectic H2 Model Reduction for High-Dimensional Linear Quantum Systems" by Alfo Borzi, Guofeng Zhang (2026-05-08)

## Activation Keywords
- symplectic model reduction
- quantum model reduction
- Q-IRKA
- quantum IRKA
- physical realizability
- 辛模型约简
- 量子模型降阶
- quantum system reduction
- symplectic Petrov-Galerkin
- quantum H2 norm
- linear quantum systems
- 量子控制系统降阶

## Core Concepts

### Physical Realizability (PR) Constraint
Linear quantum systems must satisfy two fundamental constraints:
1. **Canonical Commutation Relations (CCR)**: Preservation of quantum mechanical commutation relations under state transformation
2. **Quantum Input-Output Structure**: The system must represent a physically realizable quantum system with proper Hamiltonian, coupling, and scattering operators

Standard projection-based model reduction methods violate these constraints, producing unphysical reduced models.

### Symplectic Petrov-Galerkin Framework
The key insight: use **symplectic** projection matrices that automatically satisfy PR identities by construction. A symplectic basis V satisfies:
- V^T J V = J (symplectic structure preservation)
- Reduced system automatically inherits PR properties

### Q-IRKA Algorithm (Quantum Iterative Rational Krylov Algorithm)
A symplectic variant of IRKA specifically designed for quantum systems:
1. **Enriched Tangential Rational Krylov Pool**: Generate from shifted linear solves at interpolation points
2. **Symplectic Basis Extraction**: Gram-Schmidt-type procedure paired with symplectic conjugates
3. **Normalization**: Ensures reduced trial space satisfies canonical symplectic constraint
4. **Pole Mirror Update**: Interpolation points updated from mirror images of reduced model poles
5. **Structure-Preserving Projection**: All reduced matrices obtained exclusively by symplectic projection

## Mathematical Framework

### Linear Quantum System Form
```
dx(t) = A x(t) dt + B u(t) dt    (state equation)
dy(t) = C x(t) dt + D u(t) dt    (output equation)
```
where x(t) are quantum operators satisfying CCR: [x_i, x_j] = i * Theta_{ij}

### PR Identities
The system is physically realizable iff:
```
A*Theta + Theta*A^T + B*J_B*B^T = 0
B*Theta = -C^T*J_D
D + D^# = I
```
where Theta is the CCR matrix and J_B, J_D are quantum noise/scattering matrices.

### H2 Model Reduction Problem
Find a reduced-order model (A_r, B_r, C_r, D_r) of order r << n such that:
- ||G - G_r||_H2 is minimized (H2 norm of transfer function difference)
- Reduced model satisfies PR constraints
- Symplecticity preserved to machine precision

## Usage Patterns

### Pattern 1: High-Dimensional Quantum System Reduction
**When**: You have a large linear quantum system (n > 100 states) and need a computationally tractable reduced model.
**How**:
1. Formulate the quantum system in state-space form (A, B, C, D)
2. Verify physical realizability of the full model
3. Apply symplectic Petrov-Galerkin projection
4. Run Q-IRKA iterations until convergence
5. Extract reduced-order model (A_r, B_r, C_r, D_r)
6. Verify PR constraints on reduced model (should hold to machine precision)

### Pattern 2: Quantum Control System Design
**When**: Designing controllers for quantum systems where full-order models are too complex.
**How**:
1. Build high-fidelity quantum system model
2. Reduce using Q-IRKA to obtain tractable model
3. Design classical/quantum controller on reduced model
4. Validate controller performance on full-order model
5. Reduction quality depends on: dissipation geometry, channel placement, heterogeneity, reduced order

### Pattern 3: Bosonic Kitaev Chain Analysis
**When**: Analyzing topological quantum systems or bosonic Kitaev chain-inspired models.
**How**:
1. Model the system as a linear quantum system
2. Apply Q-IRKA for reduction
3. Analyze topological properties on reduced model
4. Verify that key features (band structure, edge modes) are preserved

## Instructions for Agents

### Step 1: Identify Quantum System
- Check if the system is a linear quantum system (quantum harmonic oscillators, optomechanical systems, superconducting circuits, bosonic systems)
- Verify the system is described by linear differential equations with quantum operators
- Extract the state-space matrices (A, B, C, D)

### Step 2: Verify Physical Realizability
- Check CCR preservation: A*Theta + Theta*A^T + B*J_B*B^T = 0
- Verify quantum input-output structure
- Identify the noise channels and scattering matrix

### Step 3: Select Reduction Order
- Choose target reduced order r based on computational requirements
- Consider the trade-off between accuracy and model size
- For oscillator-chain systems, r is typically 10-50% of original order

### Step 4: Apply Q-IRKA
- Initialize interpolation points (can use random or heuristic placement)
- Iteratively update:
  1. Build enriched Krylov subspace from shifted solves
  2. Extract symplectic basis (Gram-Schmidt + conjugate pairing)
  3. Project system matrices via symplectic transformation
  4. Update interpolation points from mirror images of reduced poles
- Converge when pole changes are below tolerance

### Step 5: Validate Results
- Check PR identities on reduced model (should hold to machine precision)
- Compute H2 error: ||G - G_r||_H2
- Verify symplecticity: V^T J V = J
- Compare frequency responses of full and reduced models

## Error Handling

### PR Violation After Reduction
**Symptom**: Reduced model violates physical realizability constraints.
**Fix**: Ensure symplectic basis extraction preserves the symplectic structure. Check normalization step carefully. The Q-IRKA framework guarantees PR by construction if symplecticity is maintained.

### Non-Convergence of Q-IRKA
**Symptom**: Q-IRKA iterations do not converge.
**Fix**: 
1. Check initial interpolation point selection
2. Verify the system is stable (all eigenvalues of A have negative real part)
3. Consider using a damped system if oscillatory behavior causes issues
4. Increase the size of the Krylov pool

### Poor Reduction Quality
**Symptom**: Reduced model has large H2 error despite many states.
**Fix**: Reduction quality depends on:
1. **Dissipation geometry**: How damping is distributed across the system
2. **Channel placement**: Location of input/output ports
3. **Heterogeneity**: Variation in system parameters
4. **Reduced order**: Too aggressive reduction loses important dynamics
Try increasing reduced order or analyzing system structure before reduction.

## Examples

### Example: Oscillator Chain System
Consider a chain of N coupled quantum harmonic oscillators with nearest-neighbor coupling:
```
H = sum_i omega_i a_i^dag a_i + sum_i g_i (a_i^dag a_{i+1} + h.c.)
```
This gives a 2N-dimensional linear quantum system. For N=50 (100 states):
1. Apply Q-IRKA with target r=20
2. Obtain 20-state reduced model
3. Verify PR: ||PR_residual|| < 1e-14 (machine precision)
4. H2 error typically < 1% for well-conditioned chains

## Resources

- **Paper**: arXiv:2605.07152 "Symplectic H2 Model Reduction for High-Dimensional Linear Quantum Systems"
- **Categories**: quant-ph, eess.SY (Systems and Control), math.NA, math.OC
- **Related**: IRKA (Iterative Rational Krylov Algorithm), symplectic geometry, quantum control theory

## Related Skills
- `quantum-control-engineering` - Engineering patterns for quantum control
- `distributionally-robust-control` - Robust control system design
- `discounted-mpc-control` - Model Predictive Control for quantum systems
