---
name: policy-gradient-baselines-score-centering
description: "Policy gradient covariance view - baselines and score centering."
category: reinforcement-learning
---

# Baselines and Score Centering in Policy Gradient Estimation

Source: arXiv:2610.22263 (Han & Hu, UIC + Perplexity AI, Oct 2026). The covariance view of policy gradient estimation that settles WHEN the group-mean baseline (RLOO/Dr.GRPO) suffices and WHEN score centering is mandatory in off-policy LLM RL.

Use when: auditing or tuning GRPO/PPO/RLOO baseline choices, debugging biased token-level importance sampling, deciding whether to add score centering to a regularized IS pipeline, or analyzing variance of policy gradient estimators.

## Core Insight

Policy gradient is a covariance: ∇J(θ) = Cov(R, s̃) where s̃ = f(w)·sθ, f = importance ratio regularizer (clip/mask/truncate). Choosing covariance (not E[R·s̃]) as the estimand RECOVERS reward-shift invariance that regularized IS destroys.

Two unbiased covariance estimators exist, differing in which mean is subtracted:
- **Sample-mean estimator** σ̂₁ = (1/(n-1))Σ(Xᵢ-X̄)(Yᵢ-Ȳ): subtracts sample means. This IS RLOO; Dr.GRPO equals it up to factor (G-1)/G absorbed into lr (Prop 10).
- **Known-mean estimator** σ̂μY(b) = (1/n)Σ(Xᵢ-b)(Yᵢ-μY): subtracts population mean μY (score centering). Unbiased for ANY constant b, defined even at n=1 (Props 8).

## Variance Theory (Prop 9)

- Var(σ̂μY(b)) = (μ₂₂ - ‖μ₁₁‖² + q(m))/n, where m = μX - b, q(m) = m²μ₀₂ + 2mμ₁₂
- Var(σ̂₁) = (μ₂₂-‖μ₁₁‖²)/n + ‖μ₁₁‖²·(μ₂₀μ₀₂)/(n(n-1))
- Minimum-variance baseline: b* = μX + μ₁₂/μ₀₂ = E[X‖Y-μY‖²]/E‖Y-μY‖² (Greensmith 2004 optimal baseline)
- σ̂μY(b) beats σ̂₁ iff |m - m*| < ρn; degrades unboundedly as baseline moves away from b*
- Group-mean reward baseline is variance-optimal ONLY if μ₁₂ = Cov(R, ‖s‖²) = 0 — false in practice since ‖s‖² grows with length and length correlates with reward ⇒ optimal baseline lies ABOVE mean reward

## Decision Rules (the practical payload)

1. **Sequence-level IS + group-mean baseline → score centering is REDUNDANT** (Prop 11). The intractable population mean μY is absorbed by Σ(Xᵢ-X̄)=0. Omit score centering; sequence-level ratio itself is the bigger problem (product of |y| token ratios ⇒ variance explosion on long traces).
2. **Token-level IS + regularized ratio (clip/mask/truncate) → score centering is MANDATORY** (Prop 15). Group-mean baseline WITHOUT score centering is biased: expectation acquires extra term Cov(R, Σₜs̄(hₜ)) ≠ 0. Token-level mean score s̄(h) = Eπ̂[f(w(v|h))∇log πθ(v|h)] is a FINITE vocab sum — computable in one extra pass.
3. With sample-mean centering on R (group baseline), centering the score too is equivalent (Prop 5) — at most one of the two centerings matters per estimator family.
4. Both estimator families degrade with training-inference mismatch (FSDP/Megatron vs vLLM/SGLang numerics): also fix the source — matched kernels, batch-invariant computation, consistent precision.

## Key Formulas

- Weighted score: s̃(y|x) = f(πθ(y|x)/π̂(y|x))·∇θ log πθ(y|x), f(1)=1
- Sequence estimand: σseq = Covπ̂(R, s̃)
- Token-level estimand (Prop 14): σtok = Covπ̂(R, D), D = Σₜ(s̃ₜ - s̄(hₜ)) — a single covariance despite per-token structure; E[D]=0 via martingale argument
- Token-level optimal baseline (31): b* = E[R‖D‖²]/E‖D‖², prompt-dependent, needs multiple rollouts to estimate

## Relationship to prior work

- Dr.GRPO (Liu et al. 2025) ≡ RLOO up to lr-absorbed factor — both are σ̂₁
- Score centering (Marek & Ryabinin, arXiv:2609.20807) = known-mean estimator σ̂μY — the two papers' methods are the two estimator families unified here
- PPO's clipped objective biases toward surrogate ∇Ĵ, not ∇J; sequence-level targets true ∇J but suffers ratio variance, token-level targets surrogate ∇Ĵ but is numerically tame

## Verification anchors

- At f = id (no regularization): s̄(h) = 0 ∀h, both families coincide with policy gradient — sanity check for implementations
- Sequence-level: Σᵢ(Xᵢ-X̄)μY term vanishes identically; token-level: does NOT vanish when f ≠ id — this asymmetry is the whole point
