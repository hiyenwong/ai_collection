---
name: geodesic-optimal-control-leakage-qubits
description: Use when synthesizing superconducting-qubit pulses that suppress leakage. Sub-Riemannian geodesic search with envelope.
category: ai_collection
---

# Geodesic-Based Optimal Control for Leakage Suppression in Superconducting Qubits

**Source**: da Silva, Pandit, Cosco (VTT Technical Research Centre of Finland), arXiv:2610.09666 (Oct 2026)

## Problem

Transmon qubits are the first two levels of an anharmonic LC oscillator. Because anharmonicity (−191 MHz) is far below the energy gaps, fast gates leak population to |2⟩. Leakage is not a Pauli error, so it evades standard QEC. Time-optimal control (fastest gates) makes it worse: abrupt turn-on/off broadens the control spectrum right onto higher-transition frequencies. DRAG pulses split the objective — DRAG-F (δ=0.5) optimizes fidelity, DRAG-L (δ=1) optimizes leakage — you cannot have both.

## Core Method: Sub-Riemannian Geodesic Search

Unitary evolution U(t) is a curve on a Lie group; gates are target points; H(t) is the tangent vector. The control Hamiltonian Hc only spans a **distribution** V of the full algebra g = V ⊕ V⊥ — so the reachable optimal paths are **sub-Riemannian** geodesics.

1. **Cost functional** (energy in the controllable subspace only):
   - E(H) = ½ ∫₀^τ ⟨Hc(t), Hc(t)⟩ dt, with ⟨x,y⟩ = tr(x·y)/dc
2. **Constrained geodesic equation** (costate Λ enforces Schrödinger dynamics; only Λ(0) matters):
   - dU/dt = −i[Hnc(t) + S(t)·P_V·U(t)Λ(0)U†(t)]·U(t)
   - Hnc = uncontrollable part in the co-rotating frame; P_V projects onto the distribution
3. **The key modification (this paper)**: multiply the control term by a smooth envelope
   - S(t) = θ_r(t − t_off)·θ_r(τ − t − t_off), sigmoid θ_r(t) = 1/(1+e^{−rt})
   - r = 2.4, t_off = 6 ns → ~4 ns buffer where amplitude < 0.1 MHz
   - This bakes "smooth turn-on/off" into the geodesic equation itself — earlier geodesic-control works produced pulses with unphysical square edges that re-introduce leakage when synthesized on an AWG
4. **Shooting method**: sample many random Λ(0), integrate, then gradient-ascent the best on process fidelity. Λ(0) has dim(g) real components (80 for two qutrits = su(9))

## Physical Pipeline (realistic platform)

- Two Duffing oscillators + tunable coupler (each 3-level: {|0⟩,|1⟩,|2⟩}), capacitive direct + coupler-mediated coupling, individual microwave drives (I/Q modulation)
- **Schrieffer-Wolff** (coupler in dispersive regime, ω_c ≫ ω_k → only virtual population): dressed frequencies ω̃_k = ω_k + g_k²/Δ_k + g_k²/Σ_k − g12²/(Σ_k+α_k)·2... and dressed anharmonicities; then **RWA** (qubits near-resonant) → effective two-qutrit Hamiltonian, SU(9) problem (dim 80)
- Effective couplings Γ_jk (↓ = lower transition, ↑ = higher): all tunable via ω_c; coupler frequency ω_c/2π = 7.945 GHz nulls all couplings (~240 Hz / ~4 Hz → truncate to zero, qubits decoupled for single-qubit gates); ω_c/2π = 5.862 GHz enables exchange (iSWAP) while staying dispersive
- Control subspace V = span{λx⊗I, λy⊗I, I⊗λx, I⊗λy} with λx = (λ1+√2λ6)/√3, λy = (λ2+√2λ7)/√3 — dim(V)=4, so single-qubit optimization reduces to SU(3)
- Thermal dissipation via Lindblad: D_k(ρ) = γ(1+n̄)D[a_k] + γn̄D[a_k†], γ/2π = 10 kHz, n̄ = 0.01 — sets the floor curves in all plots

## Metrics (state-independent)

- Leakage L1(E) = tr[P_ℓ E(ρ)], Seepage L2(E) = tr[P_c E(ρ)] (population that enters/leaves the computational subspace), both Haar-averaged → L1 = L1(E(P_c/dc)), L2 = L2(E(P_ℓ/d_ℓ)), dc=4, d_ℓ=5
- Average fidelity F = [dc·F_pro + 1 − L1]/(dc + 1), where F_pro uses the superoperator restricted to the computational subspace

## Key Results

**Single-qubit Rx(π/2), 14–38 ns sweep (24 pulses):**
- Geodesic pulses **saturate the thermal-dissipation limit** for infidelity, leakage, AND seepage simultaneously at τ = 17 ns: F = 0.9996, L1 = 1.08×10⁻⁵, L2 = 2.12×10⁻³
- Beats both DRAG variants for pulses < 20 ns; DRAG catches up only at longer durations
- Ω_y(t) is NOT ∝ −(1/α)dΩ_x/dt (the DRAG ansatz) — the optimal quadrature is a genuinely different shape; open question whether it matches higher-order derivative corrections (would unify geodesic search with generalized DRAG design)

**Two-qubit iSWAP (coupler-mediated exchange):**
- Control-free: F = 0.9548 at 79.5 ns. Geodesic control on (off-resonant fast-oscillating pulses = real-time dressed-frequency corrections compensating g1≠g2 mismatch): F = 0.9942 at 86 ns — +0.04 fidelity for +6 ns
- Leakage slightly increases (L1: 4.55→6.69×10⁻⁴), seepage flat — negligible vs the fidelity gain
- Fast oscillations in Ω(t) in the co-rotating frame = detuned drives doing frequency correction, not rotations

## Reusable Patterns

1. **Envelope-constrained geodesics**: any optimal-control trajectory meant for hardware should carry the rise/fall constraint inside the dynamics (S(t) factor), not as post-hoc pulse shaping
2. **Dressed-parameter SW+RWA reduction**: collapse a coupler architecture to an effective 2-body Hamiltonian before choosing the optimization algebra; coupler frequency is the on/off knob (null-coupling point for idle, near-resonant point for entangling)
3. **Fidelity decomposition F = [dc·F_pro + 1 − L1]/(dc+1)** separates coherent-control quality from irreversible leakage — always report both
4. **Tradeoff-metric benchmarking**: compare against each single-objective specialist (DRAG-F vs DRAG-L), not just one baseline — the win claim is "both objectives at once"
5. **Truncation validation**: recompute leakage with ladder operators truncated one/two levels higher (|3⟩, |4⟩) to confirm the 3-level model wasn't the leak
6. Practical limits: AWG synthesis precision + Hamiltonian-parameter measurement error, not the method, gate the experimental realization

## Connection Map

- Generalizes geometric quantum-control (time-optimality on Lie groups) to leakage-aware realistic pulse synthesis
- DRAG ansatz = first-derivative correction; geodesic pulses are a strictly larger family (open: higher-der DRAG ↔ geodesic equivalence)
- iSWAP relevance: fixed-connectivity superconducting chips need swaps for qLDPC codes — leakage-managed swap quality is a QEC bottleneck
