---
name: reduced-basis-quantum-ode-solver
description: "Reduced Basis Algorithm (RBA) methodology for solving polynomial nonlinear ODEs and PDEs on quantum computers. Converts nonlinear dynamics into linear RBA operators via reduced monomial basis construction. Use when: implementing quantum algorithms for nonlinear differential equations, solving ODEs/PDEs on quantum hardware, analyzing qubit requirements for quantum scientific computing, or composing timestep update maps for quantum simulation."
---

# Reduced Basis Quantum ODE Solver

## Overview

Methodology from arXiv:2606.13457 (Lăcătuş, Möller, Succi, June 2026). Introduces a Reduced Basis Algorithm (RBA) that solves polynomial nonlinear ODEs and spatially discretized PDEs on quantum computers by composing polynomial update maps, identifying reduced monomial bases, and constructing linear RBA operators.

## Core Methodology

### Algorithm Steps

1. **Time Discretization**: Discretize the nonlinear ODE/PDE system with chosen timestep Δt
2. **Polynomial Composition**: Compose the resulting polynomial update map over m timesteps
3. **Reduced Basis Identification**: Identify the reduced monomial basis appearing in the composed map
4. **Linear RBA Construction**: Construct a linear RBA operator whose action recovers the exact m-timestep nonlinear dynamics
5. **Quantum Execution**: Execute the linear RBA on quantum hardware

### Qubit Requirements

- **ODEs** (n-dimensional, degree p>1): `q_m = O(nm log p)` qubits (full basis)
- **PDEs** (N^D grid points): `q_m = O(D log N + n m^{D+1} log p)` qubits (locality-based)
- Grid size dependence is **logarithmic** for PDEs
- Nonlinear overhead controlled by local reduced basis size

### Key Properties

- **No additional approximation error** beyond time discretization error
- Computational burden moved to **classical preprocessing** (basis construction)
- Trade-off: timestep composition ↔ reduced basis growth ↔ locality
- Verified on Lorenz system and 1D Burgers equation

## When to Use

- Solving nonlinear differential equations on quantum computers
- Quantum scientific computing applications
- Polynomial ODE/PDE systems where exact m-timestep dynamics are needed
- Cases where classical preprocessing is acceptable but quantum execution is desired

## Pitfalls

- Reduced monomial basis grows exponentially with m for general systems
- Locality assumptions critical for PDE qubit efficiency
- Classical preprocessing cost must be justified by quantum speedup
- Not suitable for non-polynomial nonlinearities without polynomial approximation

## Verification

- Numerical tests should reproduce discrete time nonlinear dynamics exactly
- Compare against classical solver for the same timestep window
- Verify reduced basis size matches theoretical bounds
