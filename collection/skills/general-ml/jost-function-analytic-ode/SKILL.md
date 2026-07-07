---
name: jost-function-analytic-ode
description: "Methodology for analyzing analytic properties of Jost functions in quantum scattering theory via parameter-dependent ODEs (Poincare-Picard theorem). Applies to scattering matrix analytic continuation, complex energy plane analysis, and quantum scattering problems with short-range potentials. Bridges mathematical analysis (ODE theory, complex analysis) with quantum physics. Activation: jost function, quantum scattering theory, analytic continuation scattering matrix, Poincare-Picard theorem, parameter-dependent ODE, radial Schrodinger equation, complex energy plane"
metadata:
  arxiv_id: "2605.28859"
  published: "2026-05-27"
  tags: [quantum, scattering, ode, complex-analysis, jost-function, mathematical-physics]
---

# Jost Function Analytic Properties via ODE Theory

## Core Insight

Jost function analyticity is fundamental in quantum scattering theory and analytic continuation of the scattering matrix into the complex energy plane. This work investigates analyticity from the perspective of **parameter-dependent ordinary differential equations** using the Poincare-Picard theorem.

## Key Concepts

### Jost Functions

Solutions to the radial Schrodinger equation that encode scattering information:
- Analytic in the complex energy plane
- Determine scattering matrix poles (bound states, resonances)
- Essential for understanding short-range central potential scattering

### Poincare-Picard Approach

The Poincare-Picard theorem guarantees existence and uniqueness of solutions to ODEs with parameters. Applied to Jost functions:
1. Formulate radial Schrodinger equation as parameter-dependent ODE
2. Apply Poincare-Picard theorem for analyticity in energy parameter
3. Derive analytic continuation properties
4. Extend to complex energy plane analysis

## Methodology Framework

### Step 1: Problem Setup

Given radial Schrodinger equation for short-range central potential V(r):
```
[-d²/dr² + l(l+1)/r² + V(r) - k²] u_l(r) = 0
```

### Step 2: Jost Solution Construction

Construct Jost solution f_l(k,r) satisfying asymptotic condition:
```
f_l(k,r) → exp(ikr) as r → ∞
```

### Step 3: ODE Analysis

Apply parameter-dependent ODE theory:
- k² is the parameter
- V(r) short-range ensures convergence
- Poincare-Picard gives analyticity in k

### Step 4: Analytic Continuation

Extend results to complex energy plane:
- Upper half-plane: regular scattering
- Lower half-plane: resonances (poles)
- Real axis: physical scattering

## Usage Patterns

### Pattern 1: Scattering Matrix Analysis

When analyzing scattering matrix properties:
```
1. Identify the potential class (short-range, long-range, etc.)
2. Set up parameter-dependent ODE formulation
3. Apply Poincare-Picard for analyticity
4. Derive scattering matrix analytic properties
```

### Pattern 2: Resonance Analysis

When locating resonances in complex energy plane:
```
1. Find zeros of Jost function in lower half-plane
2. These correspond to resonance poles
3. Use analytic continuation from real axis
4. Extract resonance parameters (energy, width)
```

### Pattern 3: Bound State Analysis

When identifying bound states:
```
1. Look for Jost function zeros on positive imaginary k-axis
2. These correspond to bound state energies
3. Use analytic properties to count and characterize
```

## Activation

- jost function analysis
- quantum scattering theory
- analytic continuation scattering matrix
- Poincare-Picard theorem
- parameter-dependent ODE quantum
- radial Schrodinger equation
- complex energy plane scattering
- scattering resonance analysis
- bound state analytic properties

## References

- Paper: https://arxiv.org/abs/2605.28859
