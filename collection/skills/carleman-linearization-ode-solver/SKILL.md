---
name: carleman-linearization-ode-solver
description: "Carleman linearization methodology for converting nonlinear ODEs into infinite-dimensional linear systems via tensor powers. C2 (2nd order truncation) recovers both transient and steady-state solutions. Use when: (1) solving nonlinear differential equations, (2) quantum algorithms for ODEs (HHL-based), (3) fluid dynamics steady-state approximation, (4) converting nonlinear systems to linear form for quantum computation, (5) numerical analysis of dynamical systems. Keywords: carleman linearization, ODE solver, nonlinear differential equations, quantum ODE, fluid flow simulation, C2 truncation"
metadata:
  arxiv_id: "2605.23380"
  published: "2026-05-26"
  tags: [numerical-analysis, differential-equations, quantum-algorithms, fluid-dynamics, carleman-linearization]
---

# Carleman Linearization for ODE Solving

## Core Concept

Carleman linearization converts a system of nonlinear ODEs into an infinite-dimensional linear system by embedding the state into tensor powers. The key insight: nonlinear terms like x², x³ become linear in higher-dimensional space.

**C2 (2nd order truncation)**: Truncating at 2nd order recovers both the initial transient AND the steady-state solution — a surprising asymptotic property proved analytically for decaying logistic equations and verified for 2D fluid flows at moderate Reynolds numbers.

## Mathematical Framework

For a nonlinear ODE system:
```
dx/dt = A₁x + A₂(x⊗x) + A₃(x⊗x⊗x) + ...
```

Carleman linearization lifts to infinite dimensions:
```
dX/dt = M·X
```

where X = [x, x⊗x, x⊗x⊗x, ...]ᵀ and M is an infinite block-upper-triangular matrix. The 2nd-order truncation (C2) keeps only x and x⊗x levels.

## Key Findings

1. **C2 captures steady-state**: The 2nd-order truncation recovers not just transient dynamics but also the late-time steady-state solution
2. **Analytical proof**: Proven for decaying logistic equation with external forcing
3. **Empirical validation**: Holds for 2D fluid flows at moderate Reynolds numbers
4. **Quantum relevance**: Carleman linearization is the primary method for encoding nonlinear ODEs into quantum algorithms (HHL-based solvers)

## Usage Patterns

### Pattern 1: Nonlinear ODE → Linear System

Convert a nonlinear system for quantum or classical linear solver:

1. Identify the nonlinear ODE: `dx/dt = f(x)`
2. Decompose f(x) into polynomial terms
3. Construct the Carleman embedding matrix M
4. Truncate at desired order (C2 for steady-state, higher for accuracy)
5. Solve the linear system `dX/dt = M·X`

### Pattern 2: Quantum Algorithm for Nonlinear ODEs

For quantum computation of nonlinear dynamics:

1. Apply Carleman linearization to convert nonlinear ODE to linear system
2. Discretize in time (finite difference)
3. Encode as linear system Ax = b
4. Apply HHL algorithm or variants
5. Extract solution from quantum state

### Pattern 3: Fluid Flow Steady-State Approximation

For fluid dynamics at moderate Reynolds numbers:

1. Write Navier-Stokes in discretized form
2. Apply C2 linearization (2nd order truncation)
3. Solve the resulting linear system for steady-state
4. Verify convergence against full nonlinear simulation

## When to Use C2 vs Higher Orders

| Scenario | Recommended Order |
|----------|-------------------|
| Steady-state approximation | C2 (sufficient) |
| Transient + steady-state | C2 (validated) |
| High nonlinearity / chaos | C3+ (higher truncation) |
| Quantum ODE solver | C2 (dimensionality constraint) |
| Accuracy-critical simulation | C3+ with convergence test |

## Error Handling

### Dimensionality Explosion
Higher-order Carleman truncations cause exponential growth in system size. For n variables at order k: dimension = O(n^k). **Mitigation**: Use C2 as baseline; only increase order if residual error is unacceptable.

### Convergence Domain
Carleman linearization requires the solution to remain within the convergence radius of the Taylor series. **Mitigation**: Monitor solution norm; apply rescaling if approaching divergence boundary.

### Quantum Algorithm Limitations
HHL-based quantum ODE solvers require well-conditioned matrices. Carleman-embedded matrices may be ill-conditioned. **Mitigation**: Apply preconditioning; consider alternative quantum ODE algorithms (e.g., SLAC derivatives).

## Related Skills
- `carleman-vqls` — Carleman linearization + VQLS for quantum linear solvers
- `dolq-ode-discovery-llm` — ODE discovery with LLMs
- `pem-ude-neural-governing-equations` — Governing equation discovery
- `ode-complexity-dynamics` — ODE complexity analysis
