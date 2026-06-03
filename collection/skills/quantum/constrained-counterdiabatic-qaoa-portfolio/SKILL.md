---
name: constrained-counterdiabatic-qaoa-portfolio
description: "Constrained Counterdiabatic QAOA (CCD-QAOA) methodology for portfolio optimization. Incorporates approximate adiabatic gauge potentials from nested commutators of Ising-type portfolio Hamiltonian and XY mixer Hamiltonian into variational ansatz. Achieves improved optimization under budget and risk constraints vs standard QAOA, Grover-mixer QAOA, and penalty-based QAOA. Use when: implementing QAOA for constrained portfolio optimization, designing counterdiabatic extensions, benchmarking QAOA mixers for finance, or optimizing quantum portfolio algorithms with hard constraints."
---

# Constrained Counterdiabatic QAOA for Portfolio Optimization

## Core Idea

Standard QAOA with transverse-field mixers fail to enforce hard constraints (budget, cardinality) on portfolio optimization, requiring soft penalties that distort the energy landscape. CCD-QAOA incorporates counterdiabatic (CD) driving terms derived from nested commutators of the problem Hamiltonian and XY mixer into the variational ansatz, enabling constraint preservation without penalties.

## Key Components

### 1. Portfolio Hamiltonian
Map portfolio optimization to Ising-type Hamiltonian:
- Binary variables x_i = {0,1} for asset inclusion
- Objective: maximize return - λ × risk
- Constraints: budget (∑x_i = K), sector limits

### 2. XY Mixer (Hamming weight-preserving)
The XY mixer preserves Hamming weight (number of selected assets), naturally enforcing budget constraint:
```
H_XY = ½ ∑_{i<j} (X_i X_j + Y_i Y_j)
```
This ensures transitions only between states with same number of assets.

### 3. Counterdiabatic Terms
Derive approximate adiabatic gauge potentials from nested commutators:
```
A_μ ≈ ∑ c_k [H_prob, [H_prob, ... [H_prob, H_XY]...]]
```
The CD terms accelerate convergence by adding shortcuts to adiabaticity.

### 4. Variational Ansatz
CCD-QAOA ansatz at depth p:
```
|ψ(θ)⟩ = ∏_{l=1}^p e^{-iβ_l H_CD} e^{-iγ_l H_prob} e^{-iα_l H_XY} |ψ₀⟩
```
where H_CD contains the counterdiabatic correction terms.

## Benchmarking Results

CCD-QAOA consistently outperforms:
- Standard XY-mixer QAOA (baseline)
- Grover-mixer QAOA (global mixing)
- Penalty-based QAOA (soft constraints)

Key metric: better approximation ratios at fixed QAOA depth p.

## Implementation Workflow

1. **Formulate QUBO**: Map portfolio to Ising Hamiltonian
2. **Choose XY mixer**: For Hamming weight preservation
3. **Compute CD terms**: Nested commutators [H_prob, H_XY], [H_prob, [H_prob, H_XY]], ...
4. **Build ansatz**: Alternating layers of H_prob, H_XY, H_CD
5. **Optimize parameters**: Classical optimizer on quantum circuit
6. **Benchmark**: Compare approximation ratios vs baseline QAOA variants

## Activation Keywords
- CCD-QAOA
- counterdiabatic QAOA
- constrained portfolio optimization quantum
- XY mixer QAOA
- counterdiabatic driving quantum
- adiabatic gauge potential QAOA
- constrained binary optimization quantum
- QAOA portfolio

## Resources
- arXiv: 2605.06858
- Authors: Jose Falla, Ilya Safro
- Published: May 2026
