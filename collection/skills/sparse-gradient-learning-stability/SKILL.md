---
name: sparse-gradient-learning-stability
description: Use when synaptic learning signals are sparse/intermittent.
version: 1.0.0
source: arXiv:2610.35856 (Vastola, Harvard Medical School / Kempner Institute, Oct 2026)
trigger: sparse gradient arrivals, Poisson credit assignment, learning stability threshold, weight variance divergence, intermittent feedback, biologically plausible learning stability, eligibility trace variance
category: ai_collection
tags: [computational-neuroscience, learning-theory, stability-analysis, biological-plausibility]
---

# Sparse Gradient Arrival Learning Stability

**Core claim (arXiv:2610.35856, numerically verified this session)**: credit assignment that is correct *on average* is not sufficient for reliable learning. If gradient information arrives as sparse Poisson events per synapse, the *mean* weight dynamics converge unconditionally, but the weight *covariance* diverges to infinity below a critical arrival rate ρ_c. Learning rules for biological networks must therefore satisfy a feedback-frequency constraint in addition to unbiasedness.

## When to use
- Evaluating any biologically plausible learning rule where per-synapse feedback is event-based (neuromodulatory, eligibility-trace-gated, dendritic-error-based) rather than continuously available.
- Diagnosing why an unbiased credit-assignment scheme produces wildly variable converged weights.
- Choosing regularization / parameter-sharing / trace-averaging to stabilize sparse-feedback learning.

## Model (jump-process replacement of gradient flow)
Objective `J̃(w) = J(w) + γ/2·‖w‖²`. Replace the continuous gradient with Poisson-coupled arrivals (rate ηρ per synapse, non-dimensional arrival rate ρ):

`∂J/∂w → r(t) ⊙ [∂J/∂w + ξ]/ρ`,  ξ ~ N(0, σ_obs² I)

Per-arrival jumps carry mean −η·∂J/∂w·dt and covariance (η/ρ)(∂J/∂w)²δ_ij. The noise is **multiplicative and sparse** — this is what makes it insidious (additive observation noise ξ alone is benign).

## Scalar intuition (arrival-counted recurrence)
Single weight, quadratic loss s(w−w*)²/2, arrivals counted by n: `e_{n+1} = (1 − s/ρ)·e_n`. Three regimes:
- s/ρ < 1: monotone error decrease
- 1 < s/ρ < 2: sign-alternating but convergent (overshoot)
- s/ρ > 2: **unstable** — error grows while alternating

Critical rate (γ→0): `ρ_c = s/2`.

## Linear-network results (input covariance S)
Mean is **unconditionally stable**: `dw̄/dt = η[S(w*−w̄) − γw̄]` → fixed point w' = (S+γI)⁻¹Sw*. Always converges — the instability lives entirely in the covariance.

Covariance dynamics (Eq 11): `(1/η) dC/dt = −2γC − CS − SC + (σ_obs²/ρ)I + (1/ρ)diag(ḡ_i² + [SCS]_ii)`.

**Diagonal S** (Eq 13): stable iff for all i: `ρ > ρ_ic = s_i²/(2(s_i+γ))`; overall `ρ_c = max_i ρ_ic` (set by the LARGEST input variance). Steady-state variance diverges like 1/(ρ−ρ_ic):
`c_i = (σ_obs² + ḡ_i²) / [(ρ−ρ_ic)·2(s_i+γ)]`  (Eq 14; verified by Monte Carlo: MC/analytic ratio 0.91–1.15 for ρ∈[1.05,3]·ρ_c, divergence confirmed below ρ_c).

**Circulant S** (Eq 16): `ρ_c = (1/2N)·Σ_q s_q²/(s_q+γ)` — whole spectrum of S enters.

## Deep linear networks (depth is benign)
Teacher-student chain w_1…w_L near symmetric fixed point w_i=q, h := v·q^(2L−2). Hessian eigenvalues: h_⊥=γ (mult. L−1), h_∥=γ+L(h−γ) (mult. 1). Circulant structure reuses the above:
`ρ_c(L) = (1/2L)·[h_∥²/(h_∥+γ) + (L−1)·h_⊥²/(h_⊥+γ)]`
γ=0: `ρ_c(L) = v·W*^(2−2/L)/2` — well-behaved as L→∞. Apparent divergence of ρ_c at finite γ is an artifact: the nontrivial fixed point disappears (over-regularization), not a covariance instability.

## Mitigations (all trade something)
1. **Regularization γ** — lowers ρ_c but biases the fixed point away from w*. Biological analog: dendritic spine turnover (~1–2 week timescale in hippocampus) = continual forgetting.
2. **Parameter pooling** (spatial weight sharing via diffusion `Dw` with strength k; Dw|_i = w_{i−1}−2w_i+w_{i+1}) — damps high spatial frequencies of the fixed point and monotonically decreases ρ_c with k. Needs topographic structure to be natural. Biological analogs: gap junctions, extracellular vesicles.
3. **Gradient averaging** (accumulator variable z with timescale τ_z; eligibility-trace-like) — reduces ρ_c **without bias** but slows learning. Biological analog: eligibility traces (He et al. 2015; Gerstner et al. 2018).

## Relation to SGD stability (conceptually distinct)
- Continuous-time model; average dynamics unconditionally stable (SGD instability is about step size affecting the mean too).
- Noise is multiplicative+spatially sparse, not the additive minibatch noise of SGD.
- Interpretation: arrival rate ρ ~ error-communication frequency, not a global learning rate.

## Verification recipe (30 lines of NumPy)
Simulate single weight: dt grid; per step, arrival w.p. ρ·dt → `w += (s(w*−w)+ξ)/ρ`; always `w += −γw·dt`. Check (a) mean→w' for ρ≥0.9ρ_c (empirical mean at ρ≪ρ_c is corrupted by infinite-variance outliers — that IS the finding), (b) MC steady variance vs Eq 14, (c) variance growth over 2nd half of trajectory for ρ<ρ_c. Anchor: s=2, γ=0.5 → ρ_c=0.8 exactly.

## Rules
- Never certify a learning rule by mean-dynamics convergence alone — always derive the covariance fixed point under the actual arrival statistics.
- The binding constraint is the largest input-variance direction: ρ_c = max_i s_i²/2(s_i+γ). Reduce input variance (whitening) or increase γ to lower it.
- Below ρ_c the 1/(ρ−ρ_c) divergence means there is no partial credit: arbitrarily close to ρ_c still yields arbitrarily large weight variance.
- Prefer gradient-averaging (eligibility traces) when bias is unacceptable; accept its slower convergence.
