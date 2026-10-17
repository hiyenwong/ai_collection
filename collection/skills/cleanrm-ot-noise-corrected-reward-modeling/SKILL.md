---
name: cleanrm-ot-noise-corrected-reward-modeling
description: "Calibrate sample-wise preference noise via optimal transport for RLHF."
category: reinforcement-learning
---

# CleanRM: Reward Modeling from Noisy Feedback with a Few Clean Feedback

Source: arXiv:2610.21138 (Pan et al., Oct 2026). Reward modeling under SAMPLE-WISE (heterogeneous) preference noise — uses a small clean set to calibrate per-sample noise ratios via optimal transport, then trains with a provably unbiased noise-corrected surrogate loss.

Use when: preference data has sample-wise noise (subjective judgments, annotation errors, imperfect LLM judges), classical uniform-noise denoising underperforms, or reward models memorize noise patterns that GRPO/PPO then propagates into policies.

## Why sample-wise noise breaks standard denoising

Classical label-noise methods assume ONE uniform noise ratio. Feedback noise is intrinsically sample-wise: instruction-violating responses get consistent judgments (low noise), tradeoff responses (helpfulness vs empathy) get variable judgments (high noise). Theorem 2.1: naive risk = clean risk + E[ρr*(x)·(ℓnoisy - ℓclean)] — high-noise samples dominate gradient with the WRONG loss, RM memorizes corrupted preferences.

## Method

**Step 1 — Noise ratio estimator pφ (two-head, [256,64,2] MLP on LLM embeddings):**
- Predicts directional noise ratios (μ̂(x), ν̂(x)) per sample: μ = P(r=0|r*=1) flip 1→0, ν = P(r=1|r*=0) flip 0→1
- Invert binary transition P(r=1|x) = (1-μ-ν)·P(r*=1|x) + ν to recover estimated clean preference: r̂* = (r - ν̂)/(1 - μ̂ - ν̂)  (Eq. 5)
- Train pφ by aligning JOINT distribution (x, r̂*) of recovered noisy data with (x, r*) of clean set via Wasserstein OT: cost C_ij = ℓ(r̂*(xᵢ), rⱼ*) + d(xᵢ,xⱼ), d = LLM-encoder L2, min-max normalized per batch, Sinkhorn reg 0.1 (Alg. 1)
- Joint OT (not marginal): marginal alignment matches global histogram but pairs unrelated samples; joint gives provable upper bound on conditional discrepancy (Lemma B.2) with reliable finite-sample estimation
- Theorem 3.2: if recovered posteriors converge to clean posteriors, μ̂→μ, ν̂→ν (identifiability under local identifiability assumption)

**Step 2 — Noise-corrected surrogate RM loss:**
- Solve E[ℓ̃(rθ(x), r)] = ℓ(rθ(x), r*) for the 2×2 system (requires μ+ν<1):
  - ℓ̃(rθ,1) = ((1-ν)/ε)·ℓ(rθ,1) - (μ/ε)·ℓ(rθ,0)
  - ℓ̃(rθ,0) = ((1-μ)/ε)·ℓ(rθ,0) - (ν/ε)·ℓ(rθ,1),  ε = 1-μ-ν
- Plug in μ̂,ν̂; train RM on E_sur = (1/N)Σ[rᵢ·ℓ̃(rθ,1) + (1-rᵢ)·ℓ̃(rθ,0)] (Alg. 2)
- Theorem 3.3: with TRUE ratios the surrogate is unbiased for clean risk; with consistent estimates → asymptotically unbiased

## Results

- Benchmarks: HelpSteer / UltraFeedback / PKU-SafeRLHF, 5% clean feedback, sample-wise noise injected via naive-RM probability-proportional flipping
- RM accuracy: best R² on ALL three (+0.052/+0.013/+0.032 over strongest baseline TrainRef); Naive collapses to R²=-0.187 on HelpSteer
- Robust across backbone scales (LLaMA3.1, Qwen3 at 8B tested) and across clean-budget × noise grid: R²>0.80, MSE<0.05 even at ρ=0.20 noise with 20% clean budget
- Downstream GRPO (safety): FFT safety score +79.5% over Naive RM (Qwen3-8B), +16.3% over TrainRef; on HarmBench jailbreaks, CleanRM-trained policies refuse where naive/denoising-baseline RMs comply
- Limitations: needs SOME clean feedback (5%); pointwise formulation only (pairwise/listwise extension open)

## Reuse pattern

Any pipeline ingesting noisy binary/preference labels with a small trusted subset: (1) train a small two-head noise estimator, (2) recover clean-posterior estimates via transition inversion, (3) align joint (input, recovered-label) distribution with clean distribution via OT (semantic cost = label loss + embedding distance), (4) train with the corrected 2×2 surrogate loss. Applicable beyond RM: classification with instance-dependent noise where uniform-noise correction (F-Correction/GLC/FasTEN) underfits.

Related: FasTEN (clean-set noise estimation without OT), SelectiveRM, TrainRef (strongest baseline), Im & Grigas binary transition lemma.
