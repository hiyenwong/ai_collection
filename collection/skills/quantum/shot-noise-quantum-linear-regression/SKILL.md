---
name: shot-noise-quantum-linear-regression
description: Finite-shot ill-conditioning in quantum linear regression. Use for QELM or kernel shot budgets.
category: ai_collection
---

# Shot Noise Effects in Quantum Linear Regression

**Paper**: Who can sample forever? Shot noise effects in quantum linear regression (arXiv:2610.12015, Lo Monaco, Lorenzo, Ferraro, Paternostro, Palma, Innocenti — Palermo/Milano/QUB, Oct 2026)

## Core Claim

Quantum linear regression — the shared architecture of quantum fidelity kernels, quantum extreme learning machines (QELM), and quantum reservoir computing, where a **fixed** quantum device generates features and only a classical linear model is trained — is **unavoidably ill-conditioned under finite sampling**.

**Rank discontinuity mechanism**:
- Ideal feature matrix `P` (measurement probabilities) is **rank-deficient**: rank(P) = d² for an n_qubit system with Hilbert dimension d, living in n_out-dimensional output space (d < n_out).
- Empirical estimate `P̂N = P + N^(-1/2)Ξ̂` becomes **full rank** with high probability: shot noise populates the (n_out − d²) "noise-only" directions.
- The pseudoinverse `P̂N⁺` therefore contains terms that **diverge as N → ∞** — training fits directions that vanish in the infinite-statistics limit.

## Resource Laws (the reusable result)

MSE bias–variance decomposition for QELM trained on n_tr states with N shots/state, tested with M shots:

| Term | Scaling | Origin |
|------|---------|--------|
| Systematic bias | **N⁻²** | rank-increasing shot noise (no classical counterpart) |
| Training fluctuation | **(N·n_tr)⁻¹** | random training measurements |
| Test floor | Var(w_O)/M | finite test statistics |
| Label-noise amplification | **γ²NC/M** with C = (n_out − d²)/(n_tr − n_out − 1) | noisy targets × noise-only directions |

**Two regimes**: N ≳ n_tr → fluctuation-dominated (classical-like); N ≲ n_tr → bias-dominated, and **more training data cannot help**: beyond n_tr ~ N the MSE saturates at a floor set by per-state shots. C is exactly the classical finite-sample variance factor p/(n−p−1) with p = n_out − d² noise directions and n = n_tr − d² effective samples.

## Quantum Overfitting (key pitfall)

With noisy training targets (variance γ², e.g. state-preparation error), the MSE contains γ²NC/M: **increasing training shots N at fixed test shots M makes test error GROW linearly**. The MSE is minimized at a finite N*; more precise training features increasingly amplify label noise through the near-singular inverse (double-descent variance-peak mechanism, but the poorly-conditioned directions are *created by shot noise* and worsen as N grows).

## Practical Protocol

1. **Never budget n_tr and N independently** — treat total experimental budget as a joint allocation: fluctuations die as 1/(N·n_tr), bias floor as 1/N². Balance at N ~ n_tr.
2. **Diagnose rank mismatch first**: compute rank(P̂N) vs d². The amplification coefficient C directly counts noise-only directions (n_out − d²).
3. **Scale test shots with training shots** when targets are noisy (the N/M term), or the model will "overfit the shot noise".
4. **Regularization is the natural fix** (ridge/Tikhonov, truncated SVD, early stopping) — cut the spurious N^(-1/2)-scale singular directions before they couple to label noise. Left open by the paper; motivated by this analysis.
5. Applies to **any** non-variational quantum ML where features are estimated from shots (kernels, reservoirs, Gaussian processes) — the argument depends only on feature-space dimension.

## Relation to Classical Statistics

The N⁻² bias is the quantum counterpart of **errors-in-variables attenuation bias**, with two novel twists: (a) noise strength is set by the experimenter's shot budget; (b) noise populates directions orthogonal to the ideal feature span, reshaping the bias through a Schur complement of the noise covariance.

## References
- Companion paper explores finite-sampling-induced double descent.
- Classical background: ridgeless least squares p/(n−p−1) variance factor; errors-in-variables models.
