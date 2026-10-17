---
name: bayesian-adaptive-recruitment-curves
description: "Bayesian adaptive design selecting TMS stimulus intensities by expected information gain over a rectified-logistic recruitment curve. Use when estimating neural thresholds/curves with few stimuli. Activation: motor threshold, recruitment curve, TMS, EIG, adaptive design, onMEP."
category: ai_collection
---

# Bayesian Adaptive Design for Neural Recruitment Curves (EIG / onMEP)

> **Source**: Tyagi, Dukkipati, Twili, Mikhaeil, Gelman, Carmel & McIntosh (Columbia, arXiv:2610.15000, Oct 2026) — Bayesian adaptive design for neural recruitment curves
> Sequentially choose stimulation intensity to maximize expected information gain (EIG) about BOTH the threshold and the full recruitment curve, within a <5 s interstimulus budget.

## Problem Setup

Neural recruitment curves: muscle response (MEP size y — peak-to-peak amplitude or AUC) as a non-decreasing S-shaped function of stimulation intensity x (% MSO for TMS; µA/mA for spinal cord stimulation). Conventional acquisition:
- **Uniform sampling**: accurate curve, wasteful threshold (samples below threshold uninformative), no feedback loop, fixed n.
- **ML-PEST** (adaptive threshold hunting): accurate threshold, forfeits the curve.
- **Goal**: <40 stimuli for BOTH accurate threshold (critical for corticospinal excitability) and full curve (slope, saturation = total corticospinal output).

## The Model (rectified-logistic, from companion paper [44])

MEP size y given intensity x and params θ = {a,b,g,h,v,c1,c2} ⊂ (0,∞):

```
y | x, θ ~ gamma(shape=µβ, rate=β)          # gamma (shape–rate) likelihood
β   = 1 / (c1 + c2·µ)                        # noise shrinks with µ
F(x | Ω) = g + max(0, −v + (h+v)/(1 + v·e^(−b(x−a))))
µ  = F(x | Ω),   Ω = {a, b, g, h, v}
```

- **a = threshold**: intensity where response deflects from baseline — an EXPLICIT parameter (smooth 4/5-parameter logistics cannot represent sharp deflection from baseline; they have no threshold parameter and can't derive one).
- **g**: baseline (device/recording) response; **h**: baseline→saturation distance (g+h = saturation); **b**: growth rate; **v**: positions inflection between baseline and saturation (v→0: max gradient near baseline); **c1,c2**: constant + proportional noise.
- Baseline g is removed before curve comparison (Ω̃₀ = (θ∖{c1,c2}) with g=0).
- Real-experiment variant: mixture extension for outliers (Supp. Fig. S4); turn mixture component OFF (z=0) when evaluating EIG.
- Posterior: NUTS (NumPyro), 4 chains × (400 warmup + 400 draws) = 1,600 posterior samples; these same samples serve as S1=S2=S3 in all MC estimators.

## Three Acquisition Objectives

### 1. EIG (full-curve, default)
Information gain of observation (x,y): IG(x,y) = KL[p(θ|D,x,y) ‖ p(θ|D)]. Expected over evidence:
EIG(x) = E_{p(y,θ|D,x)} log[ p(y|θ,x) / p(y|D,x) ].
Nested MC (NMC) estimator: draw θ^(s)∼p(θ|D), y^(s)∼p(y|θ^(s),x); denominator p(y^(s)|D,x) itself MC-estimated with S1 inner samples → O(S1·S2) likelihood evals per candidate x. Costs more per candidate but no kernel machinery.

### 2. Focused EIG (FIG) — arbitrary parameter subset ϕ ⊂ θ
IG_ϕ uses KL between marginal posteriors of ϕ only. The conditional evidence p(y|ϕ^(s),D,x) = E_{p(η|ϕ^(s),D)}[·] estimated by **Nadaraya–Watson kernel regression** over posterior draws: weights k̃_r(ϕ^(s)) from a full-covariance Gaussian kernel on ϕ-samples in unconstrained space, bandwidth H = h·C via multivariate Silverman rule (h = [S/(4/(F+2))]^{−2/(F+4)} with F=|ϕ|... i.e. h ∝ [S(F+2)/4]^{−2/(F+4)}·C). Weights precomputed once per posterior update, reused across candidates. Total O(S2·(S1+S3)).

### 3. EVR — expected variance reduction on f(θ)
Δ(x,y) = Var_prior f(θ) − Var_post f(θ); posterior variance via self-normalized importance weights ω̃_s(y) = p(y|θ^(s),x) / Σ_ℓ p(y|θ^(ℓ),x) (prior as proposal). Average Δ under evidence → O(S1·S2). EVR on threshold (f(θ):=a) matches FIG accuracy with faster proposals.

**Design comparisons use the SAME estimation model** on the data each design collects — differences are attributable to acquisition, not the estimator.

## Multi-Muscle Decomposition (theorem-level simplification)

If priors are independent across muscles p(θ|D)=∏_m p(θ_m|D_m) and observations conditionally independent p(y|θ,x)=∏_m p(y_m|θ_m,x), then ALL THREE acquisition functions decompose:
EIG(x) = Σ_m EIG_m(x), EIG_ϕ(x) = Σ_m EIG_{ϕ_m}(x), EVR(x) = Σ_m EVR_m(x).
⇒ Compute per-muscle acquisition functions in parallel (GPU), sum, argmax over candidate intensities. With enough compute, 3-muscle acquisition ≈ single-muscle time (<4 s total).

## Empirical Results (simulations on hierarchical generative model fit to 14 TMS participants; 2,000 sim participants)

| Comparison | EIG advantage |
|---|---|
| Threshold error @16 stimuli | −1.87 ± 0.03 %MSO vs uniform; −0.67 ± 0.06 vs ML-PEST; +0.13 vs FIG (statistically tie) |
| Curve (integrated abs error) @32 | matches uniform (0.36±0.05, within ±0.5 equivalence band); ML-PEST −11.41, FIG −8.17 (worst) |
| Joint criteria (2% thr / 10% curve rel. error) | EIG minimizes stimuli for BOTH simultaneously; any other design needs more for either |
| Intervention power (threshold shift µ=−3, σ=2.5, 16 stim/phase) | 80% power: uniform 16 → ML 15 → EIG 11 participants (−26.7% vs ML); EIG + hierarchical Bayesian estimation (HBe): 10 participants. FPR ≤ 5% for all |
| Real TMS (8 participants, 40 stim) | locates thresholds >80% MSO even when ALL initial samples fall in baseline; allocates rest along rising limb |
| Prospective comparison study | 12 participants for 80% power to reject both nulls (EIG≠uniform on threshold stimuli; EIG≠ML-PEST on curve stimuli) |

Practical details: 8 free samples at zero intensity (no stimulation event) + 3 uniform initial stimuli shared by all designs (EIG needs none, but equal-start enables fair comparison). Errors in %MSO; relative errors r_a = e_a/a, r_y = e_y/(100−a); crossing analysis via piecewise-power-decay change-point HBe model in log2-space.

## Timing Architecture (why <5 s is achievable)

- **Update step** (NUTS on CPU): dominates total time, grows slowly with n — i9-13900K.
- **Proposal step** (acquisition function over 101 candidates, batched on GPU): constant in n — RTX 4090, JAX.
- Single muscle <3 s; 3 muscles <4 s; FIG slightly costlier (kernel weights) but still <5 s — matches TMS interstimulus interval ≥5 s. For SCS (larger candidate grids, shorter ISI): use importance sampling / SMC for updates, or amortize (deep adaptive design DAD-style policies) offline.

## Implementation Guide

```python
# 1. Generative model (NumPyro sketch)
# y ~ Gamma(concentration=mu*beta, rate=beta); beta = 1/(c1 + c2*mu)
# mu = F(x|a,b,g,h,v) = g + relu(-v + (h+v)/(1 + v*exp(-b*(x-a))))
# priors on (a,b,g,h,v,c1,c2): truncated normal / half-normal / uniform, positive support

# 2. Update: NUTS, 4 chains x (400+400). Current posterior = prior for next pick.
# 3. Proposal (per candidate x in batch):
#    theta_s ~ posterior (S2 draws); y_s ~ p(y|theta_s, x)
#    logden = log p(y_s | D, x)  # inner MC with S1 draws (evidence)
#    eig_x = mean( log p(y_s|theta_s,x) - logden )
#    x_next = argmax_x eig_x
# 4. Focused: replace denominator with NW-kernel conditional evidence over phi-samples
# 5. Stopping (optional, not prescribed): stop when 95% HDI of threshold reaches target width
```

- Candidate grid: 101 integer values over [0,100] %MSO.
- Anti-anticipation: minimum 5 s ISI + exponentially distributed delay (memoryless — participants can't time the next pulse).
- Evaluation metrics: L1 threshold error e_a; integrated absolute curve error over [0,100] (trapezoid, 501 points, baseline removed).
- Companion library: **onMEP** (Python, open source) — EIG, focused EIG, EVR, uniform (nested quasi-random sequences), and a novel round-robin multi-muscle ML-PEST extension (didn't exist before).

## Applicability & Extensions

- **Any sigmoidal input-response curve acquisition**: dose-response (pharmacology), psychometric function estimation (perceptual thresholds), intensity-response in nerve/spinal-cord stimulation, brightness/loudness matching — swap likelihood + curve function, keep EIG machinery.
- **Focused acquisition for nuisance structure**: the FIG partition (ϕ vs η) generalizes to "which parameter subset do I care about" in ANY Bayesian OED — threshold-only, slope-only, saturation-only, or expected response at 1.2× threshold.
- **Identifiability-aware stopping**: posterior HDI width of the target parameter is a natural stopping rule; the paper deliberately does not prescribe one criterion.
- **Myopic → policy**: DAD-style amortized policies could shift cost offline for SCS; open question whether multi-step lookahead beats myopic EIG here.
- **Limitations**: myopic (one-step) objective; threshold drift within session confounds design comparisons; SCS needs faster updates; model misspecification biases all downstream estimates (validated rectified-logistic beats 4/5-param logistics on empirical TMS/SCS cross-validation, [44] Fig. 3).

## Related Skills

- [[calibrated-aif-information-gain-regret]] — when information-gain exploration beats confidence sets in active inference
- [[thsdk-stock]] / other acquisition-pattern skills — unrelated domain, same EIG idea
- [[hcq-quantum-alzheimer-classification]] — TMS-adjacent clinical modeling context
