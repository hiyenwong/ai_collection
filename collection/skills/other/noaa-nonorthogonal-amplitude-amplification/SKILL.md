---
name: noaa-nonorthogonal-amplitude-amplification
description: Use when amplitude amplifying with non-orthogonal CV ancilla states in hybrid CV-DV processors.
category: ai_collection
---

# Non-Orthogonal Amplitude Amplification (NOAA) for Hybrid CV-DV Quantum Processors

**Source**: Liu, Bierman, Liu (NC State), arXiv:2610.09353 (Oct 2026)

## Problem

Hybrid CV-DV spectral-filtering oracles (Bell et al.) prepare DV eigenstates via energy-dependent oscillator displacement: |E_n⟩|0⟩ → |E_n⟩|α_n⟩, α_n = α(E_n − E_s), then vacuum postselection = Gaussian spectral filter. Repeat-until-success (RUS) costs 1/|ψ0|² when the initial target amplitude is small. Classical amplitude amplification (AA) would fix this — but AA needs a **selective reflection about the target state**, and in this setting the target DV eigenstate is *unknown* (preparing it is the whole point). The only implementable reflection goes through the CV arm, whose coherent states |α_n⟩ are **non-orthogonal** — the reflection is exact but non-selective. This is a new error mode: the oracle is implemented *exactly*, yet cannot isolate the target.

## Core Theory

**Setting.** Accessible projector Π (matched: contains target + leakage) or Π_mis (mismatch: doesn't even contain the exact target). Final state stays in span{|Ψ0⟩, Π|Ψ0⟩}: |Ψ_f⟩ = γ_l|Ψ0⟩ − θ_l Π|Ψ0⟩.

**Lemma 1 (fidelity ceiling).** F_NOAA = η·P_L with
- η = ⟨Ψ0|Π0|Ψ0⟩ / ⟨Ψ0|Π|Ψ0⟩  — **set by the projector, unreachable by any phase schedule**
- P_L = |γ_l − θ_l|²·⟨Ψ0|Π|Ψ0⟩ — the fixed-point AA transfer factor (Yoder et al. phases, α_j = 2cot⁻¹[tan(2πj/L)]^{1/γ²}, γ⁻¹ = T_{1/L}(1/δ))

Amplification degree and phase optimization only push P_L → 1; **η is the ceiling**. Improvement requires a more selective projector, not more Grover steps.

**Lemma 3 (quasi-fixed-point).** With fixed-point phases and δE_t = 0: η(1−δ²) ≤ F_NOAA ≤ η whenever ⟨Ψ0|Π|Ψ0⟩ ≥ w ≈ (log(2/δ)/L)².

**Coherent-state overlap ratio.** R = Σ_{n≠0} |ψ_n|²|⟨α_n|α0⟩|² / |ψ0|²  →  F = P_L/(1+R). Small individual overlaps are not enough — the **weighted cumulative** overlap must be small relative to the initial target weight. Two-state model: η = 1 + ε²|ψ1|²/|ψ0|² (ε = ⟨α1|α0⟩ = e^{−|α1−α0|²/2}).

**Mismatch effect (δE_t ≠ 0).** Target CV state displaced from vacuum by δα0 = α·δE_t; |c|² = e^{−|δα0|²} multiplies the ceiling; mismatched fidelity ≈ |c|²·F′ with (K−Δ_f)² ≤ F ≤ (K+Δ_f)² bounds (K = |c|²F′, Δ_f = first-order displacement error).

## Mitigation: Squeezing + HQSP Filter (the deliverable)

**1. Squeezed ancilla** |α,r⟩ = D(α)S(r)|0⟩: overlap ⟨α1,r|α2,r⟩ = exp(−e^{2r}(α1−α2)²/2) decays faster — ε drops 0.10 → 10⁻² (r=0.347) → 8.21×10⁻²¹ (r=1.5). **But** effective mismatch δᾱ_t = e^r·α·δE_t grows with r — the squeezed wavepacket is *narrower*, so the same absolute energy-estimate error hurts more (target-projector overlap 0.96→0.91 at fixed displacement). **Squeezing alone trades overlap against mismatch robustness.**

**2. HQSP filter** (hybrid QSP, signal = conditional displacement ŵ = e^{−iκx̂σz/2}, F(ŵ)F(ŵ⁻¹)+G(ŵ)G(ŵ⁻¹)=I):
- Position-space passband F̃(x) ≈ ½[erf(k(x+w_f′)) − erf(k(x−w_f′))], width w_f′ = w_f + 2σ (σ = e^{−r/2}/√2 wavepacket width), transition Δ_H = σ
- Smoothing k = √(2W(2/πε_sm²))/Δ_H via **Lambert W**; degree d = O[(T/Δ_H)·log(1/ε_poly)] — d=60 suffices because NOAA's quasi-fixed-point behavior tolerates moderate filter error
- Phase optimization: symmetric phase factors (ψ_j = ψ_{d−j}), L-BFGS-B on Chebyshev nodes; real-valued response enforced by ±π/4 endpoint shift
- Filtered leakage amplitude ϑ → η = (1−ϑ²)|ψ0|² / [(1−ϑ²)|ψ0|² + ϑ²(1−|ψ0|²)] → 1; **passband absorbs the mismatch**: robust for any sign of δx_t while the target wavepacket stays inside w_f
- Squeezed states are not just orthogonality aids — they are **the resource implementing the filter**

## Results (QuTiP, NBOS=400, convergence < 6e-6)

- Matched: NOAA ≈ AA (ε=0.01 case); RUS wins for large |ψ0| (0.6–0.8) — already efficient, AA adds nothing
- Mismatched (δx_t = ±0.25, 0.35): bare NOAA hits a hard ceiling; **HQSP-NOAA stays high-fidelity across all tested mismatches**
- Small |ψ0| (0.08–0.25): NOAA+HQSP achieves high fidelity at fewer preparation-oracle queries than RUS — the regime where the method matters
- RUS mismatch sensitivity is **sign-asymmetric**: positive δx_t reduces α1²−α0² → helps fidelity; negative hurts. HQSP-NOAA is symmetric
- Cost model: oracle C_P = O(mN) (local spin model) dominates; HQSP O(d) fixed → query count = Grover degree L−1 = 2l

## Reusable Patterns

1. **Ceiling-vs-transfer decomposition**: when an exactly-implemented oracle is non-selective, write F = η·P_L — separate what amplification can fix (P_L) from what it fundamentally cannot (η). Report the ceiling before optimizing phases
2. **Cumulative-overlap criterion R**: fidelity loss scales with Σ|ψ_n|²|overlap_n|²/|ψ0|² — audit the *weighted* sum over all non-target components, not pairwise overlaps
3. **Squeeze-overlap / squeeze-robustness tradeoff**: narrowing basis states improves distinguishability and proportionally amplifies sensitivity to parameter mismatch — mitigate with a passband filter, not more squeezing
4. **Fixed-point phases as mismatch armor**: quasi-fixed-point behavior (Chebyshev T_{1/L}) lets a *moderate-degree* imperfect filter still deliver near-ceiling fidelity — precision budget goes into the projector, not the polynomial
5. **erf-smoothed boxcar via Lambert-W k + symmetric phase factors + Chebyshev-node L-BFGS**: a complete, reusable recipe for real-valued HQSP/QSP filter design
6. **When NOT to amplify**: large initial amplitude → RUS is already optimal; AA pays off exactly in the small-|ψ0|, high-mismatch regime

## Connection Map

- Extends fixed-point AA (Yoder–Low–Chuang) and imperfect-AA literature (Høyer phases, Tulsi robust search, approximate reflections) to the case where the imperfection is *structural* (non-orthogonal CV encoding), not an approximation error
- Builds on hybrid QSP for CV-DV (conditional-displacement signal operator); open: full QSP theory of nonselective reflections — which errors are polynomial-degree-suppressible vs projector-limited
- Open: multi-window/periodic filters exploiting HQSP periodicity instead of avoiding it; sequences of coarse approximate projectors possibly overcoming the single-projector ceiling
