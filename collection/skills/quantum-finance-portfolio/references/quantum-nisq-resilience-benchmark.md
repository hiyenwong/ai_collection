# NISQ Expressibility-Coherence Trade-off Benchmark

**Source**: arXiv:2606.07727 — "Benchmarking Quantum Algorithmic Resilience for CVaR Portfolio Optimization: The Expressibility-Coherence Trade-off" (Somkuwar, Srinivasan, Raghavan, 2026-06-05)

## Problem

Dense financial optimization (CVaR portfolio with full asset correlations) mapped to sparse quantum hardware (IBM heavy hex topology, ibm_fez 127q).

## Transpilation Metrics (10 assets, ibm_fez)

| Metric | HE-VQNN (2 hidden layers) | WS-QAOA (custom mixer, reps=1) |
|--------|---------------------------|--------------------------------|
| Total Abstract Qubits | 10 | 10 |
| Transpiled Depth | Low | Very High (explosive) |
| CNOT Count | Few | Many (dense Z⊗Z for every J_ij≠0) |
| SWAP Count | Minimal | Massive |
| Theoretical Optimality | Limited | Exact |
| NISQ Feasibility | ✅ Yes | ❌ Decoherence-dominated |

## Key Formulas

### CVaR Discretization
```
CVaR_α(x) = min_ζ [ ζ + 1/(S(1-α)) · Σ_{s=1}^S z_s ]
subject to: z_s ≥ L_s(x) - ζ, z_s ≥ 0
```

### WS-QAOA Mixer (Continuous → Gate decomposition)
```
U_{M,i}(β) = R_Y(θ_i) · R_X(2β) · R_Y(-θ_i)
```

### SPSA Gradient (2 evaluations per step, regardless of N params)
```
ĝ_k(θ_k) = [L(θ_k + c_k·Δ_k) - L(θ_k - c_k·Δ_k)] / (2c_k) · Δ_k^{-1}
```

## Decision Framework

```
Problem Density > Hardware Connectivity?
  → YES  → Use HE-VQNN (sacrifice expressibility for coherence)
  → NO   → Use WS-QAOA (preserve expressibility)
  
Asset Count > Available Qubits?
  → YES  → Classical pre-screening + quantum optimization (two-step)
```

## Pitfall: The Infeasible Choice

**Current NISQ hardware forces an infeasible choice** between:
- Algorithmic inexpressibility (HE-VQNN can't model dense tail risk correlations)
- Hardware decoherence (WS-QAOA's SWAP tax kills fidelity)

This is **not an algorithm problem** — it's a **hardware topology problem**. Until all-to-all connectivity is available (e.g., trapped-ion, photonic), dense financial optimization on superconducting qubits remains fundamentally constrained.

## Optimizer Selection

| Environment | Recommended | Why |
|-------------|-------------|-----|
| NISQ Hardware | SPSA | 2 evals/step, noise-resilient, escapes local minima |
| Noiseless Simulation | Nelder-Mead | Fast, exact, but fails under shot noise |
