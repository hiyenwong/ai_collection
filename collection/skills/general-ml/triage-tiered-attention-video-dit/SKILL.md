---
name: triage-tiered-attention-video-dit
description: Use when video DiT attention dominates inference cost.
category: ai_collection
version: 1.0
author: hermes-dl-cron
license: MIT
trigger: video diffusion transformer attention, per-tile precision tiers, NVFP4, marginal gain router, training-free acceleration, Wan2.2, HunyuanVideo, LTX, SageAttention
arxiv: "2610.35706"
---

# Triage — Skip, Skim, or Refine Attention Tiles in Video Diffusion Transformers

arXiv 2610.35706. Training-free. Targets FP4 tensor cores (RTX Blackwell).

## When to Use
Use when attention over tens of thousands of visual tokens dominates video-DiT inference and single-strategy sparsity or uniform low precision leaves quality or speed on the table.

## Key empirical facts
- Row entropy H = −Σ m_t ln m_t / ln N_t (tile-mass entropy) predicts the best strategy at fixed cost: sharp rows (low H) → sparse BF16; intermediate → INT8/FP8 sparse+low-bit; diffuse rows (high H) → all tiles in NVFP4.
- Single-tile approximation error grows roughly in proportion to tile mass; NVFP4 error ≈ 1/5–1/4 of the block-mean (skip) error.
- Refinement as residual correction with BOTH terms in NVFP4 (three products total) beats falling back to BF16 on FP4-native hardware.

## Method

### Planning (no attention scores computed)
1. **Clustering-tree tiling**: repeatedly split query/key tokens along their principal direction until blocks of 128 queries / 64 keys — tiles have low internal variation → small approximation error. Trees rebuilt every 5 sparse steps.
2. **Block statistics**: per block collect means, variances, key covariance Σ_K, key–value covariance Σ_KV, mean value v̄.
3. **Closed-form error model** (first-order in the shared softmax normalizer; Gaussian-score assumptions):
   - Skip: E_t(skip) ≈ m_t·(J_t + R_t), with J_t = 1 − exp(−‖q‖²⟨tr Σ_K⟩_t/(2D²)) (convexity shrinkage of the softmax normalizer by mean keys) and R_t = (‖q‖/D)·D·‖Σ_KV‖_F/‖v̄‖ (mean-value weighting shift)
   - Skim (NVFP4): E_t(skim) ≈ α·E_t(skip), α ≈ 1/5
   - Refine: treated as exact
4. **Marginal-gain router**: minimize Σ_t [E_t(k_t) + π·c(k_t)/N_t] with compute c(k): skip=0, skim=1, refine=c_rf; single price π is the smallest marginal gain justifying extra compute. First-order approximation decouples tile choices (approximating one tile does not change the effect of others).

### Execution
Single fused kernel, one pass on FP4 tensor cores: skipped tiles use cluster mean keys/values; skimmed tiles one NVFP4 product; refined tiles three products adding residuals (X_hi + X_lo both NVFP4).

## Results
- Wan2.2, HunyuanVideo, LTX-2.5: up to 2.32× end-to-end over dense FlashAttention
- Faster than every baseline in all five settings while reaching 0.3–3.0 dB higher PSNR than the highest-PSNR baseline

## Reusable patterns
1. Multi-tier per-tile allocation by marginal gain — minimize error + π·compute/num_tiles; one price knob trades quality for speed; generalizes to any per-block approximate compute.
2. Error prediction from block statistics — mean/covariance summaries predict softmax-normalizer shrinkage (convexity) and value-weighting shift in closed form, avoiding the scores you are trying to skip.
3. Low-precision residual refinement — X = X_hi + X_lo with both terms quantized to FP4 gives high effective precision without leaving FP4 kernels.

## Related
SageAttention2/3, sparse video attention, FP8/FP4 quantized attention; distinct from token-merging skills (datme-dynamics-aware-token-merging) — Triage keeps all tokens and varies per-tile COMPUTE precision.
