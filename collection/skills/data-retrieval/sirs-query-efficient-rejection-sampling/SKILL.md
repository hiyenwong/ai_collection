---
name: sirs-query-efficient-rejection-sampling
version: v1.0.0
last_updated: 2026-10-17
description: "Unbiased parallel diffusion sampling, one query per block."
arxiv_id: "2610.22238"
authors: "Shiyuan Zhang, Xuheng Li, Qiwei Di, Quanquan Gu"
tags: [diffusion-models, sampling, unbiased-estimation, parallel-decoding, bernoulli-factory]
---

# SIRS: Query-Efficient Rejection Sampling for Parallel Masked Diffusion

From arXiv:2610.22238 (2026-10-15).

## Problem

Masked diffusion models (MDMs) unmask multiple tokens in parallel, but independent per-token sampling ignores within-block correlations and biases output. Exact correction (Anari et al. 2026) needs one score query per unmasked token — expensive.

## Method

**Single-Increment Rejection Sampler (SIRS):**

1. Decompose log acceptance probability into token-level terms; estimate it from a **single randomly sampled increment** at the cost of one query (instead of one query per token).
2. Convert a **Poisson number of clipped estimates** into a final accept/reject decision via a Bernoulli factory (adapted from Chen et al. 2026) — unbiased accept/reject from noisy biased-clip estimates.
3. **Rao-Blackwellize** each increment by averaging over the conditionals of all remaining tokens in the block (each query returns them at no extra cost), reducing clipping frequency.

Guarantee: KL(data ‖ SIRS output) ≤ clipping term + model training error. With exact scores, naive parallel decoding pays the full within-block dependence; SIRS pays only the part beyond the clipping range.

## Results

- One score query per block instead of per-token.
- Bounded KL divergence; Rao-Blackwellization strictly reduces clipping.

## Reusable Pattern

**Unbiased decisions from single-query randomized estimators.** Three composable tricks for expensive-oracle accept/reject: (1) sample a random increment of the acceptance statistic instead of computing all of it; (2) use a Bernoulli factory to convert a Poisson number of clipped (biased) estimates into an exact coin flip; (3) Rao-Blackwellize each increment over the by-products the oracle already returns. Applicable to any parallel-sampling or subset-acceptance setting where the exact statistic factorizes over items (speculative decoding, batched MCMC, constraint checking).

## Resources

- Paper: https://arxiv.org/abs/2610.22238
