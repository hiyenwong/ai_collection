---
name: lindblad-ground-state-resource-estimation
description: Use when costing fault-tolerant Lindblad state preparation.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.08667
source_title: "Fault-tolerant resource estimation for ground-state preparation via Lindblad simulation"
authors: "Marius Bothe, Patrick Schoepf, Nick S. Blunt (Riverlane, Astex Pharmaceuticals)"
published: 2026-10-06
categories: quant-ph, quantum-algorithms
trigger_words:
  - Lindblad simulation
  - ground state preparation
  - resource estimation
  - fault-tolerant
  - T gate count
  - dissipative state preparation
  - single-ancilla
  - filter function
  - error budget
  - Qualtran
  - Hubbard model
---

# Fault-Tolerant Resource Estimation for Lindblad Ground-State Preparation

## Overview

Methodology from arXiv:2610.08667 (Bothe, Schoepf, Blunt — Riverlane/Astex, Oct 2026). Bridges the gap
between asymptotic Lindblad-based ground-state-preparation theory and practical fault-tolerant costs:
full constant-prefactor error bounds + circuit-level empirical calibration + gate-level compilation
(Qualtran) + T-gate accounting in the Pauli-based computation (PBC) model.

**Headline result**: one unit of Lindblad evolution targeting the low-energy subspace of a 36-site
fermionic Hubbard model costs **7.7 × 10^8 T gates** (empirical parameters) vs **3.3 × 10^15** under
rigorous bounds — empirical calibration buys ~6 orders of magnitude. The **energy-filter integral
(H evolution) dominates the cost**; the cost of a full run scales as `M ∝ T_mix²` with the mixing time.

## When to Use

- Costing dissipative / Lindbladian ground-state or Gibbs-state preparation in the early fault-tolerant regime
- Deciding whether Lindblad state prep beats phase-estimation-based alternatives for a target system
- Allocating a total error budget across heterogeneous error sources of a compiled quantum algorithm
- Calibrating rigorous worst-case bounds with small-system exact simulations before extrapolating

## Core Method

### 1. Single-ancilla dilation-based Lindblad simulation
Evolve `dρ/dt = L[ρ] = L_H[ρ] + L_K[ρ]` with one ancilla per step. Dilation operator
`K̃ = [[0, K†], [K, 0]]`; one dissipative step is
`Φ(τ)[ρ] := Tr_a[e^{-iK̃τ} (|0⟩⟨0| ⊗ ρ) e^{iK̃τ}]`,
implementing the Lindblad evolution to **second order in τ** (`O(τ²)` trace-norm error per step).
Multiple jump operators are handled by **classical stochastic sampling** of `K_k` per step — no extra ancillas.

### 2. Filter-function transition operator
Design step: convolve a generic jump operator `A` (Pauli or hopping term) with time-domain filter `f(s)`:
`K = ∫ f(s) A(s) ds`, where `A(s) = e^{iHs} A e^{-iHs}`. In the energy domain, `f̂(ω)` gates transitions.
Set `f̂(ω) = 0` for `ω > 0` ⟹ `K|ψ₀⟩ = 0` ⟹ the ground state is a fixed point (cooling-only dynamics).

Practical filter: **bump function** with support `[-S_ω, 0]`:
`f̂(ω) = 1_{[-S_ω,0]} exp(-a / (1 - (2ω/S_ω + 1)²))`, with `S_ω ≥ 2‖H‖` (spectral width) and
steepness `a ≃ ln(1/p_min) · (Δ/S_ω)` for gap Δ (Eq. 12–13).

### 3. Quadrature (the dominant cost)
The filter integral is truncated to `2M_S + 1` quadrature points: `K ≃ K_S = Σ_l f(s_l) e^{iHs_l} A e^{-iHs_l} w_l`.
- **Nyquist-optimal time step**: `τ_S = π / S_ω` (filter has finite support in frequency).
- Quadrature error **decays exponentially**: `ε_{M_S} ∝ e^{-√(a·M_S)}`.
- Time-bandwidth relation: resolving spectral gap Δ requires sampling window `M_S·τ_S ∝ 1/Δ`.
- Each quadrature point costs a Hamiltonian evolution `e^{±iHs_l}` — this **H-evolution for the filter
  dominates total runtime** (Fig. 9): filter integral ≫ coherent evolution ≫ jump-operator evolution.

### 4. Rigorous vs empirical parameter regimes
Three costing regimes (Table I):
| Regime | S_ω | a | M_S scaling |
|---|---|---|---|
| Rigorous bounds | 2.2‖H‖_max (spectral-norm bound) | conservative ln(1/0.05) formula | ∝ a⁻¹ log²(1/ε) |
| Empirical (general) | 2‖H‖ (exact diagonalization of ≤8-site systems, power-law extrapolation) | 10⁻⁴–10⁻⁶ fitted | 1.23·S_ω/Δ_eff − 0.5 |
| Empirical (known gap) | 2‖H‖ | fitted | 0.55·(S_ω/Δ_eff)^1.03 |

**Effective gap trick**: when the target (extensive) energy error exceeds the true gap, replace
`Δ → Δ_eff = max(0.005·n_sites, Δ)` — no need to resolve fine structure looser than the target error.
This is what flattens the scaling to ~linear-in-sites at large sizes.

### 5. Error budget allocation (transferable pattern)
Total budget `ε_Tr = 0.005·n_sites / ‖H‖` split by **cost elasticity**, not evenly:
- **70% → Lindblad step τ** (cost scales linearly in 1/τ; the dominant lever)
- **15% → filter quadrature M_S** (larger budget only reduces cost polylogarithmically)
- **10% → Hamiltonian Trotter splitting** (MT,1, MT,2 steps for e^{-iτH}, e^{-iτ_S H})
- **1% → jump-operator Trotter** (A does not scale with system size — never needs more steps)
- **4% → rotation synthesis precision** (exponentially suppressed in T count — cheap to control)

Principle: give the largest share to the error source whose cost scales worst with tightness;
give small shares to sources suppressed exponentially or already bounded by other small parameters.

### 6. Trotter compilation to gates
- Jordan–Wigner mapping; **chemically-shifted Hubbard Hamiltonian** makes the interaction term
  `(U/4)Σ Z_{i,↑}Z_{i,↓}` — all terms commute, implemented as single-qubit Z-rotations up to Cliffords.
- 1D: second-order product formula with two hopping sections so **no Z-strings / fermionic swaps needed**.
- 2D: S₁ tiling (one tile per edge, `2L₁L₂ − L₁ − L₂` tiles), four Trotter partitions + fermionic swap layers;
  cost per unit time differs from 1D by only a modest constant (geometry enters via edge count only).
- Jump operator = randomly sampled hopping term with imaginary coefficient → weight-3 Pauli rotations.

### 7. T-gate accounting (Pauli-based computation model)
- Cost metric = **non-Clifford (T) gate count** (Bravyi–Smith–Smolin / Litinski PBC model).
- Rotation synthesis (mixed-fallback): `N_T ≃ 0.53·log₂(1/ε) + 4.86` T gates per single-qubit rotation,
  one shared ancilla for fallback.
- Distribute synthesis budget evenly over all rotations: ≤37 T/rotation (rigorous, 75 sites),
  ≤26 T/rotation (empirical).
- Identity-sampling in mixed-fallback gives only a few percent improvement — usually not worth modeling.

## Key Results (Hubbard benchmark)

| System | Rigorous | Empirical (general) | Empirical (known gap) |
|---|---|---|---|
| 6 sites (14 logical qubits) | 1.0×10¹³ | 6.6×10⁶ | 9.8×10⁵ |
| 36 sites (74 logical qubits) | 3.3×10¹⁵ | 7.7×10⁸ | 1.2×10⁸ |

- Simulated small systems converge at 10⁶–10⁹ T gates (Table II); 8-site model needs ~30 time units.
- Full-run cost grows as `M ∝ T_mix²` (longer time AND smaller per-step τ under fixed budget).
- **Qubit requirements are modest** (74 logical qubits for 36 sites — single ancilla, Trotter, no QSVT
  block-encodings) but T cost is "often much higher than the subsequent phase estimation routine" the
  state would feed.

## Pitfalls & Findings

1. **Algorithmic contractiveness ≠ device-noise protection.** Simulations show the dissipative evolution's
   contractive (cooling) structure offers NO protection against physical device noise — do not advertise
   Lindblad state prep as having built-in "algorithm-level error correction".
2. **Worst-case bounds are ~6 orders of magnitude pessimistic.** Always calibrate with exact small-system
   simulations (2–8 sites) + power-law extrapolation before quoting resource estimates.
3. **The filter integral is the bottleneck**, bounded below by time-bandwidth uncertainty: resolving S_ω/Δ
   per dissipative step. Optimization targets: cheaper filter-integral approximation, locality-based
   spatial truncation (Mizuta patch-and-merge, Elman locality-aware filter design).
4. **Mixing time dominates total cost** and depends strongly on mixer choice; system-spanning jump
   operators can induce rapid (logarithmic) mixing but cost more per step. One time unit is a
   conservative lower bound for benchmarking.
5. **Asymptotically "worse" methods win in practice**: Trotterization beats QSVT-based simulation at
   these scales (prefactors dominate); the same applies to dilation (1 ancilla) vs LCU constructions.
6. **Announce-type awareness**: this is a first-round costing — open items are mixer exploration and
   locality-exploiting filter approximations before numbers can be treated as tight.

## Reusable Patterns

### Pattern: Elasticity-weighted error budgeting
When an algorithm has multiple heterogeneous error sources, allocate budget by cost elasticity:
linear-cost sources get the largest share (τ: 70%), polylogarithmic ones get moderate shares
(quadrature: 15%), exponentially-suppressed ones get token shares (synthesis: 4%).

### Pattern: Rigorous-bound + empirical-calibration costing
1. Derive full-constant error bounds (not just big-O).
2. Simulate exactly at small sizes where ground truth (energy, gap) is available.
3. Fit power-law scalings for the free parameters.
4. Extrapolate to target sizes; compile both regimes to gates (Qualtran-style).
5. Report the spread as an honest uncertainty band on resource estimates.

### Pattern: Effective-gap substitution
When target error tolerance exceeds the spectral fine structure, substitute Δ_eff = max(ε_target, Δ)
into all resolution-dependent parameter formulas — provably safe and collapses scaling exponents.

### Pattern: Stochastic jump-operator sampling
Implement k>1 Lindblad operators with a single ancilla by sampling K_k per step from a classical
distribution — second-order accurate in τ without ancilla overhead scaling.

## Verification Checklist

- [ ] Filter support covers full spectral width (S_ω ≥ 2‖H‖ for symmetric spectra)
- [ ] f̂(ω>0) = 0 verified (ground state fixed point)
- [ ] Nyquist step τ_S = π/S_ω used for quadrature
- [ ] Error-budget shares sum to 100% and each enters its correct error channel
- [ ] Empirical parameters validated against exact small-system energies (not just fitted)
- [ ] T counts reported per unit time AND per full run (mixing-time-scaled)
- [ ] 2D transfer argued via edge count, not silently assumed identical

## Related Skills

- `lindbladian-sample-complexity` — sample-complexity view of Lindbladian simulation
- `near-optimal-lindbladian-learning` — learning Lindbladians from black-box access
- `dissipative-thermal-state-prep` — rigorous error bounds for dissipative thermal prep
- `early-fault-tolerant` costing literature: Campbell 2021 (Hubbard), Bay-Smidt 2025 (generalized Hubbard)
- `hardware-tailored-qec-resource-estimation` — resource estimation for the QEC layer itself

## Sources

- arXiv:2610.08667 — this paper
- Ding, Chen, Lin — Single-ancilla ground state preparation via Lindbladians, PRR 6, 033147 (2024) [algorithm]
- Cleve & Wang — dilation-based Lindblad simulation (2019)
- Zhan et al. — Rapid Quantum Ground State Preparation via Dissipative Dynamics, PRX 16, 011004 (2026) [mixing times]
- Litinski — A Game of Surface Codes (PBC model) / Bravyi-Smith-Smolin — trading classical and quantum resources
