---
name: hawkes-common-signal-spurious-excitation
description: "Audit spurious Hawkes cross-excitation from common signals."
category: ai_collection
---

# Spurious Cross-Excitation in Multivariate Hawkes Processes

Methodology from arXiv:2610.19428 (Jung & Lee, 2026): latent common signals generate apparent directional cross-excitation in multivariate Hawkes fits even with zero structural interaction. Use when interpreting fitted cross-kernels as contagion/reflexivity/leadership in financial event data, order flow, or any multivariate point process with a shared latent environment.

## Core Identification Problem

A fitted cross-excitation coefficient is evidence of interaction only relative to a stated information set. Three objects must be kept distinct:
1. **Predictive representation** — best affine predictor on observed history (always exists, may have signed entries)
2. **Admissible Hawkes counterpart** — same mean + Bartlett spectrum, nonnegative kernel, stable (a genuine alternative DGP)
3. **Structural mechanism identification** — requires information beyond second order

None substitutes for another. A good spectral fit validates NONE of them as structural.

## Model (Cox immigration)

λ_it = μ_i + β_i ∫ Y_{t-u} g_i(du) + Σ_j ∫ φ_ij(t−s) dN_js

- Y: latent nonnegative common signal, stationary, exogenous, cov v·e^(−κ|τ|) for closed forms
- (β_i, g_i): common-information channel (loading + response measure; g_i can be density or fixed delay δ_i)
- φ_ij: excitation channel; stability ρ(Φ) < 1, Φ = ∫φ
- Mean intensity Λ = (I−Φ)^(−1) ν̄, ν̄_i = μ_i + β_i·E[Y]
- Bartlett spectrum: S(ω) = (I−φ̂(ω))^(−1) [D_Λ + b̂(ω) S_Y b̂(ω)*] (I−φ̂(ω))^(−1)*, b̂_i(ω) = β_i·ĝ_i(ω)

## Bias Mechanism (Theorem 1)

The observed-history projection inflates the kernel:

**φ̃ = φ + Ψ − Ψ*φ**  (projected = structural + omitted-signal filter − filter*structural)
**Φ̃ = Φ + Ψ̄(I−Φ)**,  Ψ(u) = H·e^(Fu)·K (Kalman filter of the latent signal given residual counts; P solves the filtering Riccati equation, K = PH'D_Λ^(−1), F = A−KH)

Ψ is a bias-generating filter, not the bias itself. When φ ≡ 0, the ENTIRE fitted kernel is common-signal artifact.

## Quantitative Benchmarks

**Univariate apparent criticality (Cor 1)**: with zero excitation and instantaneous response, F_c = 1 + 2β²v/(κΛ); fitted branching ratio ñ = 1 − F_c^(−1/2), decay rate κ√F_c. Persistent regimes (κ→0) drive ñ→1 — reproducing Filimonov–Sornette apparent criticality. Example: signal SD 0.5, persistence 10 min, Λ=1/s → F_c=301, ñ≈0.94 (spurious 35 s kernel). NEVER interpret a branching ratio near 1 as endogeneity without a common-factor audit.

**Directional asymmetry (Cor 2/3)**: two equal streams, delays 0 and Δ, no excitation:
- Weak signal: Ψ̄21/Ψ̄12 asymmetry index D = 1 − e^(−κΔ) (fast→slow dominates)
- Exact pure-delay: D(r,x) = [Q(r,x)−1]/[Q(r,x)+1], strictly increasing in r = 2β²v/(κΛ) and x = κΔ; limits 1−e^(−x) and 1
- All four projected kernels provably NONNEGATIVE and stable → exact second-order-equivalent Hawkes process exists (not just a signed predictor). ρ(Φ̃) ≈ 0.83 achievable with Φ = 0.
- Zero-frequency factorization: det(I−Φ̃) = det(I−Ψ̄)·det(I−Φ)

**Audit protocol**: a fitted cross-kernel's direction and temporal shape reveal reaction-time ordering to common information, not imitation. Ask: could both streams be responding to the same latent signal at different speeds?

## Third-Order Identification (Theorem 3)

Integrated cumulants with Cox immigration (R = (I−Φ)^(−1), u = Rβ, C^H = RD_ΛR', D_u = R·diag(u)·R'):
- C = C^H + σ²uu'
- K_ijk = K^H_ijk + σ²[(D_u)_ij·u_k + (D_u)_ik·u_j + (D_u)_jk·u_i] + s3·u_i·u_j·u_k

After scale normalization σ²=1, θ=(vec Φ, β, s3) is generically LOCALLY identified from (Λ, C, K): d=2 → 7 moments/7 params, d=3 → 16/13. Proof: rational Jacobian minors, exact-arithmetic rank witnesses.

**Practical warning (weak identification)**: median smallest/largest singular ratio ≈ 3×10⁻⁴; third-order window cumulants have ~10% sampling error even at 6.8M events; s3 often hits search bounds. Identification ≠ estimability. Default estimator = restricted parametric Whittle spectrum; cumulants establish that identification is possible, not a plug-in estimator.

## Proxy Conditioning (Prop 3)

An exogenous proxy Z loading on the same signal (exclusion: no direct N↔Z excitation, no Z self-excitation):
- Proxy reduces filter covariance in Loewner order: P_Z ⪯ P̄ — NOT entrywise: individual cross-kernels may rise
- High-precision limit: ‖φ̃−φ‖_L2 = O(r_Z^(−1/4)), r_Z = 2γ²v/(κΛ_Z)
- **Two failure modes**: (1) Z excited by N → proxy absorbs structural feedback (reverse-direction fits are sensitivity diagnostics, not exogeneity tests); (2) direct response to Z's events → mixes channels. A decline in within-N cross-excitation after adding a proxy bounds NOTHING without extra assumptions.

## Whittle Estimation on Binned Counts

- Discrete spectrum via exact alias sum f_h(λ) = hD_Λ + Σ_m [S(ω_m)−D_Λ]·[(2sin(ω_m h/2)/ω_m)²]; Poisson part aliases exactly to hD_Λ
- Criterion: Σ_k [log det f + tr(f⁻¹ J_k J_k*)], Λ estimated as X̄/h — include the estimated-mean correction
- Feasible sandwich SEs contain higher-order score covariances AND score–mean cross-covariances
- Honest coverage report: delays in short records 84.4% (undercovered; log-Wald barely helps); interior params 92–95%; omitting the plug-in mean correction → overcoverage; Gaussian inverse-info → 88.8%. Report both.

## Empirical Adequacy Discipline (SOL illustration)

Fitted spectral radii 0.9588 vs 0.999 had nearly identical WITHIN-HOUR criteria, but imply hourly-count dispersions 1,593 vs 346,286 (observed variance-to-mean ≈ 10,007). Frequencies <1 Hz carried 0.42% of criterion weight — a small criterion difference hid a massive frequency-local difference.

**Rule**: always check unfitted moments (hourly totals, long-lag covariances) against the frozen fit. Good within-hour fit does NOT validate a long-run excitation decomposition. State the fitted frequency range and the information set in every claim.

## Reusable Audit Checklist

1. Before interpreting cross-excitation: model the alternative — shared latent signal + heterogeneous response speeds
2. Compute the directional asymmetry index (Ψ̄21−Ψ̄12)/(Ψ̄21+Ψ̄12); ask if delay structure can explain it
3. Check apparent criticality against signal persistence: is ñ ≈ 1 − (1+2β²v/(κΛ))^(−1/2) plausible?
4. Estimate third-order cumulants as a mechanism contrast (not a plug-in estimator); report weak conditioning
5. If using a proxy: verify BOTH exclusions; remember Loewner ≠ entrywise
6. Whittle: include estimated-mean sandwich correction; report delay undercoverage honestly
7. Validate fit against unfitted low-frequency moments before any structural attribution

## Related
- [[market-informedness-rl-market-making]] — Hawkes market-taker modeling (application side)
- [[collusion-basin-audit-qlearning]] — auditing RL pricing agents (same rigor tradition)
