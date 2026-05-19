---
name: carleman-vqls
description: "Carleman linearization + Variational Quantum Linear Solver (VQLS) methodology for solving nonlinear differential equations on quantum hardware. Converts weakly nonlinear ODEs to high-dimensional linear systems via Carleman embedding, then solves with VQLS using symmetry-grouped Hadamard Tests. Use when: (1) solving nonlinear differential equations with quantum algorithms, (2) designing hybrid quantum-classical ODE solvers, (3) benchmarking quantum advantage for numerical computation."
---

# Carleman-VQLS for Nonlinear Dynamics

## Description
Hybrid quantum-classical pipeline for solving nonlinear differential equations by combining Carleman linearization (nonlinear → high-dimensional linear) with Variational Quantum Linear Solver (VQLS) on quantum hardware.

## Activation Keywords
- Carleman linearization
- VQLS nonlinear equations
- quantum differential equation solver
- quantum nonlinear dynamics
- variational quantum linear solver
- Duffing equation quantum

## Core Pipeline

### Step 1: Carleman Linearization
Transform nonlinear ODE dx/dt = f(x) into infinite-dimensional linear system:
- Truncate at order N for finite approximation
- Error decreases with truncation order N
- Applicable to polynomial nonlinearities (Duffing, Lorenz, etc.)

### Step 2: VQLS Formulation
Solve Ax = b variationally:
- Ansatz circuit U(θ) generates trial solution |x(θ)⟩
- Minimize cost function C(θ) = ||A|x(θ)⟩ - |b⟩||²
- Use Hadamard Test for matrix element estimation

### Step 3: Symmetry-Grouped Measurement
- Group Pauli terms by commuting symmetries
- Reduces measurement rounds
- Compare global vs local cost formulations

### Step 4: Cost Function Comparison
- **Global cost**: C_global = ⟨ψ|A†A|ψ⟩ - ⟨ψ|A†|b⟩ - ...
  - Suffers from barren plateaus for deep circuits
- **Local cost**: C_local = sum of local terms
  - More resilient to barren plateaus
  - Better gradient scaling

## Platform Considerations
- Tested on IBM (superconducting) and Xanadu (photonic) platforms
- Distillation techniques for noise mitigation
- Shot budget allocation for Hadamard Tests

## Advantages
1. Extends quantum advantage to nonlinear problems
2. Carleman approximation converges for weakly nonlinear systems
3. VQLS avoids HHL's deep circuit requirements

## Limitations
- Carleman dimension grows exponentially with truncation order
- VQLS optimization landscape depends on ans choice
- Requires careful cost function selection to avoid barren plateaus

## Related Concepts
- Variational Quantum Linear Solver
- HHL algorithm
- Carleman embedding
- Barren plateaus in VQAs

## Resources
- arXiv:2605.15366 - Measurement-Efficient VQLS for Carleman-Linearized Nonlinear Dynamics
