---
name: constrained-counterdiabatic-qaoa-portfolio
description: "Constrained Counterdiabatic QAOA (CCD-QAOA) methodology for portfolio optimization. Extends QAOA with counterdiabatic driving terms to improve convergence on constrained financial optimization problems. Uses CD terms to suppress diabatic transitions during adiabatic evolution, enabling faster convergence to optimal portfolio weights. Use when: counterdiabatic QAOA, CD-QAOA portfolio, quantum approximate optimization, quantum finance optimization, adiabatic quantum computing finance, constrained QAOA."
---

# Constrained Counterdiabatic QAOA for Portfolio Optimization

## Core Problem

Standard QAOA for portfolio optimization struggles with slow convergence and getting trapped in local minima when handling cardinality and budget constraints. Counterdiabatic (CD) driving can accelerate convergence by suppressing non-adiabatic transitions.

## Key Insight

Adding counterdiabatic terms to the QAOA mixer Hamiltonian provides a shortcut-to-adiabaticity that preserves constraint satisfaction while accelerating convergence to the optimal portfolio.

## Methodology

### Step 1: Define Portfolio QUBO

Formulate portfolio optimization as QUBO:
```
H_C = -∑ μ_i x_i + λ ∑∑ Σ_ij x_i x_j
```
Where x_i ∈ {0,1} indicates asset inclusion.

### Step 2: Add Counterdiabatic Terms

Extend the mixer with CD driving:
```
H_CD(t) = ∑ γ_i(t) [H_D, H_M]_i
```
Where γ_i(t) are time-dependent coefficients that suppress diabatic transitions.

### Step 3: Enforce Constraints

Implement constraints via:
- Penalty terms in cost Hamiltonian for soft constraints
- CD terms that respect the constraint manifold
- Post-processing projection for hard cardinality

### Step 4: Optimize Parameters

Optimize QAOA angles (γ, β) and CD coefficients jointly:
- Use gradient-based optimization
- Initialize with adiabatic schedule
- Exploit parameter concentration for warm start

### Step 5: Sample and Post-Process

- Sample from optimized circuit
- Project to feasible portfolio space
- Compare against classical baselines

## When to Use

- Portfolio optimization with QAOA
- Constrained combinatorial optimization on quantum hardware
- Problems where standard QAOA converges slowly
- Financial optimization with cardinality constraints

## Pitfalls

### CD Term Computation Cost
Computing exact CD terms scales exponentially. Use variational approximation or first-order truncation for practical implementations.

### Parameter Optimization Landscape
Adding CD terms increases parameter space dimension. Use layer-by-layer initialization to avoid barren plateaus.

### Hardware Noise Sensitivity
CD terms amplify circuit depth. On NISQ devices, balance CD benefit against decoherence.

## Activation Keywords

- counterdiabatic QAOA
- CD-QAOA portfolio
- constrained QAOA
- quantum approximate optimization finance
- adiabatic quantum computing portfolio
- shortcut to adiabaticity optimization
- 反绝热驱动量子优化
- 约束QAOA投资组合

## Resources

- Paper: arXiv:2605.06858
- Related: quantum-optimization-qaoa skill
- Hardware: Gate-based quantum processors
