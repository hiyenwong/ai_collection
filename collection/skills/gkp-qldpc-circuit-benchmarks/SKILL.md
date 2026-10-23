---
name: gkp-qldpc-circuit-benchmarks
description: Benchmark GKP-concatenated qLDPC codes (BB vs tricycle) under circuit-level noise.
category: ai_collection
---

# GKP-Concatenated qLDPC Circuit-Level Benchmarking

Methodology from arXiv:2609.35282 (Yao, Xing, Gao, Yuan — Peking University, Sep 2026): a unified
simulation framework for evaluating GKP-bosonic-inner + qLDPC-outer concatenated QEC codes under
three levels of noise-model fidelity, with analog-informed BP-OSD decoding.

## When to Use

- Comparing qLDPC outer codes (BB, tricycle, lifted-product, hyperbolic surface) for GKP concatenation
- Estimating finite-size crossing / squeezing thresholds (dB) for bosonic QEC architectures
- Deciding whether code-capacity screening is sufficient before expensive circuit-level simulation
- Designing decoders that consume analog GKP homodyne residuals as soft information

## Core Architecture: 4-Component Processing Stack

`C = C_outer ∘ C_GKP` — each outer-code physical qubit is replaced by one GKP-encoded oscillator mode.

1. **Inner GKP correction**: folds continuous displacement ξ into [−s/2, s/2) (s = √π lattice spacing).
   Outputs a binary Pauli-frame transition e_i AND a continuous log-likelihood `L_i = log((1−p_i)/p_i)`.
2. **Outer syndrome extraction**: Tanner-graph edges (a,j) with H_aj = 1 executed as SUM/inverse-SUM
   gates between data modes and GKP ancillas; Z-checks measure ancilla q-quadrature, X-checks measure p.
3. **Analog-information processing**: the folded residual z_i is retained instead of binary rounding.
4. **Global decoding**: BP-OSD on H_X, H_Z (or spacetime matrix), with priors from step 1/3.

**Key systems-engineering insight**: code capacity alone does NOT determine circuit-level performance.
Check weights, Tanner-graph structure, gate-schedule depth, displacement propagation through SUM gates,
and decoder priors jointly determine the effective outer-code noise.

## Three-Level Noise Model Hierarchy

| Model | Rounds | Meas faults | Weight dep. | Schedule | Propagation | Use |
|-------|--------|-------------|-------------|----------|-------------|-----|
| Code capacity | No | No | No | No | No | Cheap screening; isolates GKP↔Tanner compatibility |
| Variance aggregation | T=3 | Yes | Yes (row/col weights) | No | No | Adds matrix-dependent circuit exposure at low cost |
| Full propagated circuit | T=6 | Yes | Yes | Yes | Yes | Quantitative FT claims; resolves ordered circuit |

### Variance-aggregation noise (effective widths)

```
σ²_data,j  = (λ_data·σ)² + w_col,j·(λ_gate·σ)²
σ²_meas,a  = (λ_meas·σ)² + w_row,a·(λ_gate·σ)²
```
with λ_data=1, λ_gate=1/2, λ_meas=1. Spacetime detection events:
`d⁰=Hf⁰+µ⁰; dᵗ=Hfᵗ+µᵗ+µᵗ⁻¹ (1≤t≤T−1); dᵀ=µᵀ⁻¹`, i.e. `d = M_H·u` over F₂.

### Full circuit model

- Edge-coloring partitions Tanner edges into gate layers (no mode in two simultaneous gates).
- Noise widths σ_α = λ_α·σ_gkp with (λ_data, λ_anc, λ_gate, λ_meas, λ_idle) = (0.25, 1, 0.15, 0.50, 0.05).
- SUM gate propagation (control c → target r):
  `q'_c = q_c; q'_r = q_c + q_r; p'_c = p_c − p_r; p'_r = p_r` — displacements propagate continuously
  between data and ancilla modes; ancilla faults back-act on data.
- Spacetime matrix `M_H = [I_{T+1} ⊗ H | B_T ⊗ I_m]`, B_T = open-boundary temporal incidence.
- Decoder priors: frozen effective widths κ_v·σ with κ_data ≈ 1.848, κ_Z-check ≈ 1.273, κ_X-check ≈ 6.679
  (fitted on BB circuits once, transferred unchanged to tricycle — no family-specific calibration).

## Hard vs Analog-Informed Priors

Hard decision (all modes at same noise get same prior):
```
p_hard(σ) = Σ_k ∫_{(2k+1/2)s}^{(2k+3/2)s} exp(−ξ²/2σ²)/√(2πσ²) dξ
```
Analog-informed (conditioned on folded residual z ∈ [−s/2, s/2)):
```
p_ana(z;σ) = Σ_k exp(−(z−(2k+1)s)²/2σ²) / Σ_k exp(−(z−ks)²/2σ²)
```
Each variable gets LLR Λ_i = log((1−p_i)/p_i); clip p to [10⁻¹⁵, 1/2−10⁻¹⁵]. Apply hard and analog decoding
to the SAME sampled noise realization — this isolates the value of retaining the modular GKP outcome.

BP-OSD settings (fixed per model across all code families): capacity (I_max,γ,Λ_max,w,K)=(50,0,50,2,20);
variance (50,0.3,30,0,8); circuit (150,0.5,10,1,12). OSD orders variables by posterior reliability, does
Gaussian elimination on the permuted matrix, searches low-weight assignments among least-reliable free
variables, and picks the minimum-reliability-cost syndrome-consistent candidate.

## Benchmark Results (Selected Instances)

BB sequence: [[18,4,4]], [[72,12,6]], [[144,12,12]]. Tricycle: [[48,6,(8,4)]], [[84,6,(12,5)]], [[108,6,(12,6)]].

| Model | BB hard | BB analog | Tri hard | Tri analog |
|-------|---------|-----------|----------|------------|
| Code capacity | 0.500 | 0.556 | 0.427 | 0.500 |
| Variance agg. | 0.329 | 0.369 | 0.334 | 0.349 |
| Full circuit | 0.198 | **0.212** | 0.130 | **0.142** |

- Circuit-level analog crossings ↔ squeezing: BB ≈ 10.46 dB, tricycle ≈ 13.94 dB.
- Analog information improves crossings in EVERY model and BOTH families.
- BB > tricycle under common assumptions — but finite-length crossing estimates for these instances,
  NOT universal family thresholds (sequences differ in n, k, d).
- Independent consistency check: BB threshold ~10.6 dB from prior circuit-level study ↔ σ≈0.209,
  close to this work's 0.212 analog estimate.

## Reusable Workflow

1. Supply outer code only via binary CSS matrices H_X, H_Z with H_X H_Z^T = 0 (mod 2) — the whole
   pipeline is code-family-agnostic.
2. Screen with code-capacity model; locate relevant σ scan windows cheaply.
3. Add variance-aggregation model to capture check-weight/degree-dependent exposure.
4. Validate with schedule-resolved circuit simulation before making fault-tolerance claims.
5. Compare decoders on identical sampled realizations (paired comparison).
6. Report finite-size crossings with the caveat that 3 non-identically-scaled instances ≠ asymptotic threshold.

## Extensions Noted by Authors

Additional qLDPC constructions; optimized extraction schedules; correlation-aware decoding
(SUM-gate propagation creates non-identical data/Z-check/X-check marginals); hardware-specific
noise and resource models (optical vs microwave vs trapped-ion costs differ substantially).

## Related Skills

- `bf-osd-qldpc-decoding` — Best-First OSD decoder for QLDPC codes
- `barbell-qldpc-superconducting-hardware` — BB codes on superconducting hardware
- `dimer-singlet-covering` (KG neighbor) — lattice-covering code constructions
