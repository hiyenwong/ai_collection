---
name: neural-field-bumps-interneuron-subtypes
description: >
  Three-population (E/PV/SST) stochastic neural field model of working-memory
  bump attractors with interneuron subtypes. Use when analyzing bump stability
  in neural fields, modeling PV/SST inhibitory subtypes, studying working-memory
  diffusion/wandering, or applying interface-based Heaviside neural field analysis.
metadata:
  arxiv_id: "2609.13074"
  published: "2026-09-11"
  authors: "Bilal Ahmed, Heather Cihak, Gregory Handy"
  tags: [neural-fields, working-memory, bump-attractor, interneuron-subtypes, pv-sst, linear-stability, diffusion, wandering]
---

# Stability and Wandering of Bumps in Neural Fields with Interneuron Subtypes

## Overview

**Core innovation**: Extends the bipartite E/I bump-attractor neural field (Laing–Chow style) to a **three-population stochastic field with distinct excitatory (E), parvalbumin-expressing (PV), and somatostatin-expressing (SST) populations**, then derives in closed form: (1) stationary bump solutions, (2) linear stability decomposed into shifting vs scaling modes, and (3) an effective diffusion coefficient for noise-driven bump wandering.

**Biological motivation**: PV cells give fast perisomatic inhibition with a *local* footprint; SST cells target distal dendrites with a *broader* spatial footprint; canonical motif = PV self-inhibition + SST→PV inhibition, no SST self-inhibition, weak PV→SST. Existing bump models collapse inhibition into one homogeneous population — this paper shows subtype structure is not decorative but reshapes both deterministic stability and stochastic memory precision.

**Key findings**:
1. Population thresholds and inhibitory *timescales* determine both bump stability AND the mechanism by which stability is lost (shifting vs scaling instability, incl. Hopf)
2. Inhibitory connection strengths and spatial scales substantially reshape the stable parameter region; **broader SST connectivity promotes and stabilizes bump states**
3. Increasing the SST spatial footprint **reduces the effective diffusion coefficient** of noise-driven memory wandering — broad SST inhibition makes memories more precise

## Model Framework

Three coupled stochastic integro-differential equations on the ring x ∈ [−180°, 180°] (angular feature space, e.g. orientation preference):
```
τ_e du_e = [−u_e + w_ee*f_e(u_e) − w_ep*f_p(u_p) − w_es*f_s(u_s)] dt + ε^{1/2} dW_e
τ_p du_p = [−u_p + w_pe*f_e(u_e) − w_pp*f_p(u_p) − w_ps*f_s(u_s)] dt + ε^{1/2} dW_p
τ_s du_s = [−u_s + w_se*f_e(u_e) − w_sp*f_p(u_p) − w_ss*f_s(u_s)] dt + ε^{1/2} dW_s
```
- Firing rate: sigmoid → **high-gain limit Heaviside** f_n = H(u_n − θ_n) (interface-based analysis)
- Kernels: symmetric exponential on the ring, w_mn(x−y) = A_mn·exp(−min{|x−y|, 360−|x−y|}/σ_mn)
- Noise: spatially correlated (von Mises-filtered), temporally white, independent across populations (cross-covariances can be retained if correlated)
- Baseline (Table 1): A_ee=0.6 σ_ee=1; inhibitory outgoing weaker (A_ep=0.15, A_es=0.15, A_pe=0.2, A_se=0.1); PV local (σ_ep=1.5), SST broad (σ_es=σ_ps=2.0); A_pp=A_ps=0.01; A_sp=A_ss=0 (relaxed in Sec 5.2); τ_e=1 (=10 ms), ε=0.0001, κ=1017

## Stationary Bump Solutions (Sec 3)

Single contiguous active region per population: U_n(x) > θ_n for x ∈ (−a_n, a_n), half-widths (a_e, a_p, a_s), center pinned to origin by translational invariance.

Self-consistency: threshold matched at interfaces θ_n = U_n(±a_n). For exponential kernels the convolution integrals are closed-form:
```
∫_{−c}^{c} w_mn(x−y) dy = 2 A_mn σ_mn e^{−x/σ_mn} sinh(c/σ_mn)            if x > c
                        = 2 A_mn σ_mn (1 − e^{−c/σ_mn} cosh(x/σ_mn))     if |x| < c
                        = 2 A_mn σ_mn e^{x/σ_mn} sinh(c/σ_mn)             if x < −c
```
The threshold conditions are **piecewise in the ordering of (a_e, a_p, a_s)** — each of θ_e, θ_p, θ_s has 4 cases depending on whether a_n lies inside or outside the other active regions (using S_mn = e^{−a_m/σ_mn} sinh(a_n/σ_mn) and C_mn = 1 − e^{−a_n/σ_mn} cosh(a_m/σ_mn)).

Solve either direction: prescribe half-widths → compute thresholds; or prescribe thresholds → Levenberg–Marquardt for half-widths. Always verify the assumed single-active-region structure holds.

## Linear Stability (Sec 4) — Shift/Scale Decomposition

Perturb u_n = U_n + νΨ_n, linearize; Heaviside derivative is distributional:
```
f'(U_n(x)) = (1/|U_n'(a_n)|)·[δ(x−a_n) + δ(x+a_n)]
```
→ perturbations localize at the 6 threshold interfaces; defining interface values ψ_n^± = ψ_n(±a_n) and interaction coefficients
```
K_mn^± = χ_n · A_mn/|U_n'(a_n)| · exp(−|a_m ± a_n|/σ_mn),   χ_e=1, χ_p=χ_s=−1
```
(K^−: same-side interfaces; K^+: opposite-side coupling) gives a closed 6D eigenvalue problem. Reflection symmetry splits it into TWO 3D problems:

**Shifting (odd, ψ_n^+ = −ψ_n^−)**: matrix M_shift with entries (K_mn^− − K_mn^+) and diagonal −1 − τ_nλ. Contains the translational zero eigenvalue λ=0 (neutral mode = memory encoding); stable iff all OTHER shift eigenvalues have Re < 0.

**Scaling (even, ψ_n^+ = ψ_n^−)**: matrix M_scale with entries (K_mn^− + K_mn^+) and diagonal −1 − τ_nλ. Expansion/contraction of active regions; stable iff all scale eigenvalues have Re < 0.

Stability metrics: Λ_shift = max Re(λ_j^shift) over nonzero modes, Λ_scale = max Re(λ_j^scale), Λ = max of the two. Bump linearly stable iff Λ < 0; comparison of Λ_shift vs Λ_scale identifies the instability mechanism as parameters vary.

## Deterministic Effects of Subtype Structure (Sec 5)

- **Threshold slice (θ_s = θ_p)**: raising common inhibitory threshold generally stabilizes; boundary is a Hopf bifurcation (complex-conjugate pair crossing the imaginary axis) — consistent with the 2-population model, but the extra inhibitory degree of freedom enriches instability dynamics
- **Timescales τ_p, τ_s**: increasing either destabilizes eventually; the TYPE of instability (shifting vs scaling) depends on τ_p vs τ_s comparison — two distinct loss mechanisms identified
- **Spatial scales**: broader SST projections (increasing σ_es = σ_ps) expand and deepen the stable parameter region — SST breadth is stabilizing
- **Weak I/I connections (Sec 5.2)**: even small A_sp, A_ss (SST self-inhibition, PV→SST) have substantial and NON-MONOTONIC effects on stability — routinely-neglected connections are not negligible
- **Instability mechanism taxonomy**: parameter changes can hit the shift boundary or the scale boundary first; which one determines the qualitative failure mode (drift instability vs collapse/expand)

## Diffusion of Wandering Bumps (Sec 6)

Weak-noise (ε ≪ 1) stochastic reduction: linearize about the stationary bump; the nullspace of the deterministic operator is spanned by (U_e', U_p', U_s')ᵀ. Bounded solutions require the Fredholm solvability condition — project inhomogeneous terms onto the adjoint null vector φ(x), which for the Heaviside model is a sum of δ's at the six interfaces:
```
φ(x) = ( δ(x+a_e)−δ(x−a_e);  β_p[δ(x+a_p)−δ(x−a_p)];  β_s[δ(x+a_s)−δ(x−a_s)] )
```
with β_p, β_s closed-form ratios of interface weights W_mn^± = w_mn(a_m ± a_n) (E-component normalized to unit amplitude).

Result: bump displacement Δ(t) is an effective Brownian motion, ⟨Δ²⟩ = ε·𝒟·t with
```
𝒟 = (𝒩_e + 𝒩_p + 𝒩_s) / (2·[|U_e'(a_e)| + τ_p β_p |U_p'(a_p)| + τ_s β_s |U_s'(a_s)|]²)
𝒩_e = C_ee(0) − C_ee(2a_e);  𝒩_p = β_p²[C_pp(0) − C_pp(2a_p)];  𝒩_s = β_s²[C_ss(0) − C_ss(2a_s)]
```
(C_nn = spatial noise covariances; cross-population noise correlations would add cross terms.)

**Verified**: linear variance growth matches direct Euler–Maruyama simulations (10⁴ trials) across threshold space. **Key stochastic finding**: increasing SST spatial footprint (σ_es = σ_ps = σ_ss from 1→10) monotonically DECREASES 𝒟 — broader SST inhibition slows memory diffusion, quantitatively linking inhibitory architecture to behavioral precision (delay-period error accumulation).

## Implementation Notes (from Appendix A)

- Python 3 / numpy / scipy / matplotlib; code to Zenodo upon acceptance
- Forward Euler (deterministic) / Euler–Maruyama (stochastic); dt = 0.025 (=0.25 ms); time unit 10 ms
- Ring discretized with n = 2^14 even points; convolutions via FFT/IFFT
- Half-widths via linear interpolation of zero crossings (profile minus threshold); thresholds→half-widths via Levenberg–Marquardt
- Diffusion coefficient estimated from slope between final two sampled times; 10⁴ simulations per parameter point

## Pitfalls

- **Single-active-region assumption**: construction excludes multi-bump solutions (multiple stored items) and large perturbations (distractors) — the weak-noise diffusion reduction is invalid there
- **Only 2 inhibitory subtypes**: VIP interneurons (third major disinhibitory pathway) omitted; adding them changes the motif algebra
- **Static synapses**: no short-term facilitation/depression — activity-dependent efficacy could shift the PV/SST balance and the stability boundaries with network state
- **Long-time shared diffusion only**: the reduction is built on the common translational zero mode; transient population-specific wandering (E vs PV vs SST centers separating before converging) exists in some parameter sets but is not captured — retaining stable shifting modes alongside the neutral mode would address this
- **Correlated cross-population noise**: default derivation assumes independent noise; keep cross-covariance terms if inputs are shared
- **Heaviside high-gain limit**: all closed forms rely on it; finite-gain sigmoid requires numerical treatment of f'

## Applications & Extensions

- Working-memory precision: predict how PV/SST-targeted manipulations (optogenetics, pharmacology) alter delay-period error accumulation via 𝒟
- Multi-item memory: extend to multi-bump solutions and bump interactions (memory competition, distractor-induced errors)
- Add VIP population → 4-population disinhibitory motif; state-dependent (STF/STD) synapses → state-dependent PV/SST balance
- Testbed for dynamical-systems questions: symmetry, Hopf bifurcations, interacting shift/scale modes, neutral-direction noise-driven motion
- Bridge to behavior: Λ (deterministic robustness) + 𝒟 (stochastic precision) give circuit-level predictions for delayed-response error variance growth

## Related Skills

- `working-memory-heterogeneous-delays` / `snn-working-memory-*` — spiking-network working memory with delays (complementary substrate)
- `neural-critical-dynamics-theory` — criticality framing of persistent activity
- `bipartite-oscillator-synchronization-modes` — E/I oscillator synchronization (rate/phase level)
- `heteroclinic-neural-field-cognition` — other neural-field attractor structures

## Source

arXiv:2609.13074 — "Stability and Wandering of Bumps in Neural Fields with Interneuron Subtypes", Bilal Ahmed, Heather Cihak, Gregory Handy (University of Minnesota), math.DS / q-bio.NC, submitted 2026-09-11. Supported by Burroughs Wellcome Fund Career Award at the Scientific Interface.
