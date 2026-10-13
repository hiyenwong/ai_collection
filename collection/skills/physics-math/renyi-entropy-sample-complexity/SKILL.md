---
name: renyi-entropy-sample-complexity
description: Settled sample complexity for noninteger-order Renyi entropy estimation. Use for entropy estimators.
category: ai_collection
---

# Settling the Sample Complexity of Rényi Entropy Estimation

**Paper**: Settling the Sample Complexity of Rényi Entropy Estimation (arXiv:2610.10389, Qisheng Wang, Shanghai Jiao Tong University, Oct 2026, cs.IT)

## The Complete Complexity Picture (main reusable table)

For estimating Hα(p) of an unknown discrete distribution over alphabet size d to additive error ε (success ≥ 2/3):

| Order α | Sample complexity | Status |
|---------|-------------------|--------|
| 0 < α ≤ 1/2 | Θ(d^{1/α} / (ε^{1/α} log d)) | **This work** |
| 1/2 < α < 1 | Θ(d^{1/α}/(ε^{1/α} log d) + d^{1/α−1}/ε²) | **This work** |
| α = 1 (Shannon) | Θ(d/(ε log d) + log²d/ε²) | [JVHW15, WY16] |
| α > 1, α ∉ ℕ | Θ(d/(ε log d) + d^{1−1/α}/ε²) | **This work** |
| α ≥ 2 integer | Θ(d^{1−1/α}/ε²) | [AOST17, AK26] |

This closes the decade-old gap from Acharya–Orlitsky–Suresh–Tyagi (SODA 2015): their noninteger upper bounds misbehaved when d is not large relative to ε (ε-dependence 1/α < 2 contradicting the Ω(d^{1−1/α}/ε²) lower bound), and their lower bounds left ε-dependence and polylog(d) factors undetermined. Now optimal up to α-dependent constants.

## Techniques Worth Reusing

### Upper bound: refined polynomial approximation estimator
Poissonization: draw X_i, Y_i ~ Poi(n·p_i) independently. Split symbols by a **count threshold Y_i ≤ 10L** (L = log(ed)):
- **Small-count regime (Y ≤ 10L)**: plug-in estimator L_n(x) = best-approximation polynomial Q_K(x/n) scaled by (40L)^α·x^j/(40L)^j with indicator x ≤ 80L — polynomial approximation of x^α on [0,1] of degree K achieves error ‖Q_K − x^α‖∞ ≤ c_α·K^{−2α} with coefficient bound Σ|a_j| ≤ c_α·8^K (Chebyshev-type; from Lubinsky/Shevaldin). This **reduces the bias** for large probabilities p_i ~ O(1/n).
- **Large-count regime (Y > 10L)**: unbiased estimator H_n(x,y) = α^{−1}·Σ_j(−1)^{j−r}·C(α,j)·C(j,r)·y^{α−r}·x^r (double binomial sum — a finite-difference-style exactly-unbiased estimator of p^α when counts are large).
- Final estimate: Ĥ = (1/(1−α))·log clip_{I_α}(F̂), clipping F̂ into [1, d^{1−α}] (α<1) or [d^{1−α}, 1] (α>1) before the log — variance control at the boundary.

### Lower bound: constructive moment matching
Hard-instance tool of independent interest: for noninteger α and any R > 1, there is a **K-moment matching pair (ν0, ν1) on [0, K²]** with mean μ such that:
- moments up to order K agree: m_t^{(j)} equal for j ≤ K (fools all polynomial statistics of degree ≤ K, TV distance of induced Poisson mixtures ≤ 2eM/L via Wu–Yang Lemma 2.3),
- yet the **α-th moments have a fixed ratio**: m^{(α)} ratio ≤ 2, kept bounded by e^{8|1−α|ε} in the reduction — so Rényi entropy differs by 2ε while low-order tests cannot distinguish.
- Construction uses bounded support [0, K²] (constant-bounded high-order moments), unlike AOST17's unbounded-support matching.

**Pattern**: pair the moment-matching pair with a two-block distribution: t·m "hard" symbols carrying the matched mixture + s·m uniform symbols; tune t so that Chebyshev kills the mixture-detection probability and Markov kills the Fα deviation simultaneously (the split at R_U ≥ 1/2).

## Practical Guidance for Entropy-Estimation Work

1. **ε-dependence changes at α = 1/2 and α = 1**: for α < 1/2 sampling is dominated by d^{1/α}/(ε^{1/α} log d) (rare-symbol discovery); for α > 1 by d^{1−1/α}/ε² (heavy-symbol variance). Never reuse integer-order intuition (Θ(d^{1−1/α}/ε²)) for noninteger α — the d/(ε log d) discovery term is always there.
2. **Best-polynomial-approximation + threshold splitting** is the go-to unbiased-ish estimator pattern for power-sum functionals Fα(p) = Σp_i^α — also usable for other f(p) functionals with ‖f‖-regularity (Hilbert/Hankel matrices, etc.).
3. **Poissonization + independent second sample (X for evaluation, Y for regime selection)** decouples thresholding noise from evaluation noise.
4. Moment-matching pairs with fixed α-moment ratio are the modern lower-bound primitive for distribution-functional estimation — reusable for minimax lower bounds beyond entropy.
