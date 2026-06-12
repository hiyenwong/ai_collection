---
name: reduced-basis-quantum-ode-solver
category: quantum-computing
description: Reduced basis algorithm (RBA) for solving polynomial nonlinear ODEs and PDEs on quantum computers — composes update maps over timesteps and identifies minimal monomial basis.
tags: [quantum, differential-equations, reduced-basis, nonlinear-ODE, quantum-algorithms]
created: 2026-06-12
source: arxiv:2606.13457
---

# Reduced Basis Algorithm for Nonlinear Differential Equations on Quantum Computers

## Summary
Addresses the challenge of solving nonlinear differential equations on quantum computers where quantum evolution is intrinsically linear. The reduced basis algorithm (RBA) handles polynomial nonlinear ODEs and spatially discretized PDEs by composing polynomial update maps over timesteps and identifying a reduced monomial basis.

## Key Contributions

### Nonlinear Problem Reformulation
- Converts nonlinear ODEs/PDEs into a form suitable for quantum computation
- Time discretization followed by composition of polynomial update maps
- Identifies the minimal monomial basis needed for the composed map

### Reduced Basis Identification
- The number of monomial terms grows with composition depth
- RBA identifies and eliminates redundant monomials
- Keeps the quantum circuit size manageable for practical applications

### Algorithm Steps
1. Discretize time domain
2. Compose polynomial update map over m timesteps
3. Identify reduced monomial basis for the composed map
4. Encode the reduced system on quantum computer
5. Solve using quantum linear system algorithms

## Application Scenarios
- Nonlinear dynamical systems simulation
- Fluid dynamics on quantum computers
- Chemical kinetics and reaction-diffusion equations
- Nonlinear wave equations

## Complexity Analysis
- Classical preprocessing: polynomial in number of variables and timesteps
- Quantum advantage: logarithmic scaling in system dimension
- Reduced basis size grows sub-exponentially with composition depth

## When to Use
- Need to solve nonlinear ODEs/PDEs on quantum hardware
- Classical methods are too slow for high-dimensional systems
- Problem has polynomial nonlinearity structure
- Working with spatially discretized PDEs

## Implementation Considerations
- Requires careful basis selection to avoid exponential blowup
- Compatible with HHL and other quantum linear system solvers
- Works best for sparse or structured systems
- Preprocessing step can be done classically

## Related Concepts
- Carleman linearization
- Quantum linear system algorithms (HHL)
- Polynomial chaos expansion
- Operator splitting methods
- Quantum simulation of nonlinear dynamics