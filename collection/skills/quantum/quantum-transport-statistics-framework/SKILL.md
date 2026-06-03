---
name: quantum-transport-statistics-framework
description: "Exact framework for computing heat, energy, and particle transport statistics in quadratic quantum systems coupled to Gaussian reservoirs — combines full counting statistics with non-Markovian master equations. Use when: analyzing quantum transport in mesoscopic systems, computing full counting statistics for particle/heat currents, studying non-Markovian open quantum systems, evaluating transport between quantum reservoirs, or modeling quantum thermodynamic engines."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2602.21190"
  published: "2026-02-21"
  authors: "Guglielmo Pellitteri, Vittorio Giovannetti, Vasco Cavina"
  tags: [quantum, transport, statistics, full-counting, non-markovian, open-systems, thermodynamics, gaussian]
---

# Quantum Transport Statistics Framework

Exact computational framework for evaluating heat, energy, and particle transport statistics between Gaussian reservoirs mediated by quadratic quantum systems.

## Core Methodology

### Full Counting Statistics (FCS) Setup

For a quadratic system coupled to M Gaussian reservoirs:

1. **Hamiltonian**: H = H_S + Σ_α H_R^α + Σ_α H_{SR}^α
   - H_S = ½ Ψ† h Ψ (quadratic system)
   - H_R^α = Σ_k ε_{αk} c_{αk}† c_{αk} (Gaussian reservoir α)
   - H_{SR}^α = Σ_k (t_{αk} Ψ† c_{αk} + h.c.) (linear coupling)

2. **Counting field**: introduce χ_α for each reservoir to track transferred particles/energy
   - Modified Hamiltonian: H(χ) = e^{iχN/2} H e^{-iχN/2}

3. **Cumulant generating function**: G(χ, t) = ⟨e^{iχQ(t)}⟩ where Q = accumulated current

4. **Levitov-Lesovik formula**: for non-interacting systems, G(χ, t) = det[1 + T(f_L - f_R)(e^{iχ} - 1)]
   where T = transmission matrix, f = Fermi functions

### Non-Markovian Master Equation Approach

For systems where Markov approximation fails:

```
1. Derive time-convolutionless (TCL) master equation:
   ∂_t ρ(t) = ℒ(t)[ρ(t)] where ℒ(t) = Σ_n ℒ_n(t) (Born expansion)

2. Counting-field modified Liouvillian:
   ℒ(χ, t) = ℒ_0(t) + Σ_α (e^{iχ_α} - 1) J_α(t) + (e^{-iχ_α} - 1) J_α†(t)

3. Cumulant generating function:
   ln G(χ, t) = λ_0(χ, t) · t where λ_0 is dominant eigenvalue of ℒ(χ, t)

4. Current moments:
   ⟨I^n⟩ = (-i∂_χ)^n ln G(χ, t)|_{χ=0}
```

### Efficient Computational Method

The framework introduces an algorithm that:
1. Reduces the full counting statistics to solving a set of coupled differential equations
2. Exploits Gaussianity: only first and second moments needed (Wick's theorem)
3. Computational cost: O(N³) for N system modes (vs O(4^N) for general states)
4. Handles arbitrary time-dependent driving and multi-reservoir setups

## Key Results

### Current Statistics

For steady-state transport:
- **Average current**: ⟨I⟩ = Tr[T(E)·(f_L(E) - f_R(E))] (Landauer formula generalization)
- **Noise (variance)**: S = ∫ dE Tr[T(E)(1-T(E))(f_L-f_R)² + T(E)(f_L(1-f_L)+f_R(1-f_R))]
- **Skewness**: higher cumulants encode interaction effects and non-Gaussianity

### Thermal Transport

For heat current between reservoirs at temperatures T_L, T_R:
- Fourier's law emerges in the diffusive limit
- Ballistic transport: heat current independent of system size
- Quantum thermal rectification possible with asymmetric couplings

## Usage Patterns

### Pattern 1: Steady-state transport
Set up Hamiltonian, compute transmission T(E), evaluate Landauer-type integrals.

### Pattern 2: Time-dependent driving
Use the non-Markovian master equation with time-dependent counting fields.

### Pattern 3: Full distribution
Compute all cumulants via ∂_χ^n ln G(χ)|_{χ=0} for complete current statistics.

## Error Handling

### Non-Gaussian Reservoirs
- The framework assumes Gaussian reservoirs; for non-Gaussian (e.g., spin baths), use polaron transformation or reaction coordinate mapping
- For strongly coupled reservoirs, include system-reservoir correlations via reaction coordinate

### Numerical Stability
- For long times, the TCL expansion may diverge — switch to time-convolution (Nakajima-Zwanzig) form
- Use adaptive time-stepping for stiff differential equations
- Verify complete positivity of the reduced dynamics
