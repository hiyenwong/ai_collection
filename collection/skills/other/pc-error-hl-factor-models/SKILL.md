---
name: pc-error-hl-factor-models
description: Use when estimating factor models by PCA in high dimension.
category: ai_collection
---

# Principal Component Error in High-Dimensional Factor Models (HL Regime)

**Paper**: "Principal component error in high-dimensional factor models" — Bernstein, Goldberg, Gunther, Kercheval, Lan, Lin, Yao, arXiv:2609.20550v2 (v1 17 Sep 2026, v2 15 Oct 2026). math.ST / q-fin.PM / q-fin.ST.

## Setting

Latent factor model y = Bf + z, only y observed (p × n data matrix). Estimating principal directions (true variance-maximizing linear combos of exposures B) via leading eigenvectors h_j of the sample covariance S. **HL regime**: p → ∞ with n (sample size) FIXED — the realistic finance case where regime changes leave only limited time series (n = 63 trading days, p = 3,000 Russell-3000-scale assets).

## Main Result (Theorem 1 — Error Decomposition)

Conditional on the factor path F, almost surely as p → ∞, with fixed n:

sin²∠(h_j, b_j) → **OE_j + IE_j**, where

- **Out-of-subspace error** OE_j = δ² / (nλ_j + δ²) = 1 / (1 + SNR_j), with SNR_j = nλ_j/δ²
  - δ² = asymptotic average specific (idiosyncratic) variance; λ_j = realized variance of the jth systematic component over the n observations.
  - Caused by SPECIFIC returns; equals the share of the jth sample eigenvalue contributed by noise. Vanishes iff δ² = 0. **Estimable from data** (Theorem 2): consistently estimated by ℓ/θ_j = (average non-zero bulk eigenvalue) / (jth leading eigenvalue) of the sample covariance — a computable **lower bound (floor) for total error**.
- **In-subspace error** IE_j = (1 − OE_j) · RE_j, where rotation error RE_j = sin²∠(ω_j, β_j) is the angle between the realized direction ω_j (eigenvector of realized factor second-moment F F^⊤/n) and population direction β_j.
  - Caused by the FINITE SAMPLE of factor returns; exactly the error PCA would make on noise-free data BF (Remark 5). **NOT estimable from data alone** (Theorem 3, non-estimability) — requires a model for the law of factor returns.

Mechanism: as p grows, specific returns add an ISOTROPIC term to the n×n dual Gram matrix — shifts eigenvalues without moving eigenvectors. This gives the clean separation.

## Key Practical Numbers (US-equity-calibrated 3-factor simulation, t-distributed returns, 1000 paths)

- Factor vols 16%/8%/6% annualized, specific vol 40%; GB = diag(1.25, 1, 1).
- **n = 63 days (one quarter), p = 500**: total direction error ≈ 17° (factor 1), 39° (factor 2), 50° (factor 3). Even at p = 50,000 errors stay large.
- **p = 3,000, n: 20 → 250 days**: error falls only 30° → 8.5° (factor 1), 56° → 19° (factor 2), 66° → 24° (factor 3). **Even a year of daily data leaves errors demanding attention.**
- Out-of-subspace error accounts for **80–93% of total** across the tested range — the dominant, estimable component.
- The data-driven floor ℓ/θ_j tends to UNDERESTIMATE the true OE at small p — use it as a lower bound, not a point estimate.

## Reusable Decision Rules

1. **Compute the estimable floor** ℓ/θ_j (bulk-average / leading eigenvalue ratio) whenever using PCA on p >> n data; it bounds from below the error in every direction you estimate.
2. **Estimation-window choice**: short window = single regime (smaller rotation error) but larger OE via small n; long window reduces error but requires a factor-volatility-change model because RE is non-estimable without one.
3. **Subspace vs direction**: the span of factor exposures IS estimable (Corollary 1: OE answers "how accurately have we identified span(B)?"); individual directions within it are not pinned down by data alone — with n fixed, sample eigenvectors within a spike group "can't be asymptotically distinguished" (Shen-Shen-Zhu-Marron; made exact by Theorem 3).
4. Any use of estimated principal directions (risk management, portfolio construction, control vectors in regressions, attribution) should carry the OE floor as an uncertainty quantification.

## Relation to Prior Work

- Jung et al. (2012): joint limiting distribution of sample-vs-population eigenvector inner products via dual Gram matrices; here generalized to unrestricted factor serial dependence/nonstationarity with a.s. path-conditional limits + estimability split.
- Wang & Fan (2017): large-n counterpart with the same in/out-subspace split; their "correction for eigenvector biases is almost impossible" remark anticipates Theorem 3 informally.
- Gurdogan & Shkolnik (2024): noise-free non-estimability counterpart of Theorem 3.
- Shen-Shen-Zhu-Marron (2016): spiked HL angles to subspace; Theorem 3 makes their "can't distinguish" observation exact.

**Activation**: principal component error, factor model estimation, high-dimension low-sample, PCA eigenvector error, out-of-subspace error, bulk eigenvalue, estimable error floor, rotation error, estimation window, financial factor model, HL asymptotics, spiked covariance