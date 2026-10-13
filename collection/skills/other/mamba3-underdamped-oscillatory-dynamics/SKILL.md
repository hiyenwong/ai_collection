---
name: mamba3-underdamped-oscillatory-dynamics
description: Use when analyzing input-dependent rotations in SSMs, oscillatory recurrent dynamics, or phase interventions in Mamba-style models.
category: ai_collection
metadata:
  arxiv_id: "2610.13341"
  published: "2026-10-09"
  authors: "Shutian Liang, Yue Song (Tsinghua)"
  tags: [mamba-3, state-space-model, underdamped-dynamics, phase-intervention, length-generalization]
---

# Mamba-3 Through Oscillatory (Underdamped Second-Order) Dynamics

Source: arXiv:2610.13341 (cs.LG, 9 Oct 2026, Tsinghua). Interprets Mamba-3's input-dependent
decay–rotation transition Ā_t = ρ_t R(θ_t) as an **underdamped second-order system**, giving a
framework to isolate what learned oscillation contributes beyond state retention.

## The second-order reduction (exact, per interval)

For a rotary state pair z_t=(H_t, P_t), z_{t+1}=ρ_t R(θ_t)z_t with a=−log ρ/Δt, ν=θ/Δt:

- Continuous generator: A_rot = −aI + νJ, J²=−I, so e^{A Δt} = ρ R(θ) — discrete update is the exact flow.
- Differentiating out P gives: **Ḧ + 2aḦ + (a²+ν²)H = 0** — a damped second-order ODE with
  ω₀=√(a²+ν²), **ζ = a/√(a²+ν²) < 1** for any ν≠0 → always underdamped.
- Modal parameterization for controlled comparisons: A_t(κ) with eigenvalues λ±=−a_t±√κ_t;
  κ<0 underdamped, κ=0 critically damped, 0<κ<a² overdamped — same second-order state structure,
  only oscillation differs.

## Key results

1. **Mode persistence geometry** (proofs in App C.2):
   - Overdamped: mode collapse — |μ₋/μ₊|^n → 0; slow eigendirection dominates.
   - Critically damped: fastest asymptotic attenuation at fixed ω₀; propagation → rank-one (I+tN)e^{−ω₀t}.
   - Underdamped: z_n = e^{−anΔ}R(nνΔ)z₀ — **lengths and angles preserved up to common decay**,
     no directional collapse; slower decay than critical damping (a<ω₀).
2. **State tracking** (Parity/Mod 3/Arithmetic w/o brackets, scaled accuracy):
   Underdamped 100/95.26/95.68 ≫ overdamped 0.58/81.60/3.22 ≈ critically damped 3.27/3.22/0.32.
   Data-dependent rotation also beats static rotation (Parity 4.05→100) — both oscillation AND
   input-adaptivity required.
3. **Language modeling** (187M/444M, 100B FineWeb-Edu tokens, 2K train context):
   - Oscillatory models lower PG-19 perplexity beyond training context at both scales; LongBench-E
     10.61→13.22 at 444M (comparable at 187M). Length generalization without retraining.
   - Removing rotation from pretrained 1.5B models hurts **LAMBADA (context-dependent) far more than
     Relation (factual)** — oscillation specifically supports contextual integration.
4. **Phase interventions** (PG-19 perplexity multipliers):
   - SISO @64K: phase reversal 74.10×, removal 41.33×, shuffle 7.25× — grows with context length.
   - MIMO: weaker length dependence (removal ~15×) but consistently worse than decay permutation.
5. **Constructive accumulation regulation**: removing phase increases history–update cosine similarity
   (0.293→0.429 SISO @16K) and state RMS norm (7.6→8.9) — learned rotation **reorients retained
   information relative to incoming updates**, preventing runaway constructive accumulation.
   (Links to Lu et al. 2025 / Shen et al. 2026 state-norm growth explaining poor Mamba extrapolation.)
6. **Write–read phase consistency**: removing rotation from B (writing) or C (readout) alone is severe
   (9.04×/12.18× SISO); removing from BOTH partially restores (2.08×) — writing and readout must share
   phase coordinates. Residual gap = mismatch with natively-accumulated context.

## Implementation guidance

- To test whether a recurrent architecture uses oscillation: build the κ-parameterized second-order
  family (Eq. 18-21: Ā_t(κ)=exp(Δt·A_t(κ))) — isolates oscillatory from non-oscillatory with identical
  state structure.
- Phase interventions are cheap causal probes for any rotary/complex-transition model: removal, reversal,
  shuffle, decay permutation (control), and window-wise layer ablation.
- Diagnostics for phase role: history–update cosine similarity + state RMS norm at multiple context
  lengths; phase-channel trajectories (slow/median/fast timescales all appear naturally).
- Note the asymmetry: from-scratch non-oscillatory models still extrapolate stably — oscillation
  *improves* long-context but is not *required* for stability. Don't conflate the two claims.

## Pitfalls

- Don't attribute gains to second-order coupling alone — critically/overdamped variants share the same
  coupled state and fail; oscillation is the operative variable.
- Static (fixed-angle) rotations underperform input-dependent ones; the phase must adapt per token.
- Intervention asymmetry: phase removal in a pretrained model ≠ training without oscillation.
- Complex eigenvalues alone don't guarantee the benefit — Grazzi et al. negative-eigenvalue work and
  Keller-Welling neural wave machines are the adjacent baselines to cite.

## Applications

- Design dimension for SSMs / linear attention / any recurrent model: input-dependent oscillation
  (decay controls how much persists; phase controls how it combines and is accessed).
- Cheap interpretability probes for rotary SSM checkpoints (phase windows, B/C consistency).
- Length-generalization interventions: rotate to regulate state accumulation instead of norm-clipping.

## Related skills

- `meg-mamba-ssm-foundation`, `spiking-brain-oscillation` family, `oscillatory-snn-time-delayed-coordination`
