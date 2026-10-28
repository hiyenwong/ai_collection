---
name: spide-liquidity-profile-clmm
description: Use when modeling concentrated liquidity in AMMs (SPIDE).
category: economics
trigger: Uniswap V3 liquidity dynamics, concentrated liquidity AMM, stochastic PIDE, Sturm-Liouville Gegenbauer modes, liquidity profile forecasting, loss-versus-rebalancing, tick-level liquidity calibration
arxiv_id: "2610.30539"
---

# Dynamics of the Liquidity Profile in Concentrated Liquidity Provision (SPIDE)

Methodology from "Dynamics of the Liquidity Profile in Concentrated Liquidity Provision: An SPIDE Approach" (arXiv:2610.30539, Lee, Risk, Tung, Wang, Oct 2026). Models the FULL aggregated liquidity profile of Uniswap-V3-style concentrated-liquidity AMMs as an infinite-dimensional stochastic process — replacing per-tick point processes or averaged-profile regressions with a SPIDE whose spectral reduction is a small coupled linear SDE system.

## When to Use
- Forecasting or calibrating the whole liquidity profile of a concentrated-liquidity AMM (not just price or TVL).
- Deriving pool reserves / pool value / LVR expressions under a stochastic liquidity profile.
- Any spatial density dynamics with (i) mean-reverting concentration toward a center, (ii) nonlocal redistribution, and (iii) a fixed interval with degenerate endpoints.

## The SPIDE

On a fixed interval [−L, L] (tick-rank coordinates), the profile u_t(x) evolves as

```
du_t(x) = {L u_t − V_t[u_t] + h(t, x)} dt + Σ_m {σ_m(t, x) + σ̃_m(t, x)[u_t]} dW_t^m
```

with the **degenerate Sturm–Liouville operator**

```
L u = a(L²−x²) ∂²_x u − b x ∂_x u,   a, b > 0
```

- −b·x drift: liquidity at tick x repositions toward the center (spot price) — mean-reverting concentration.
- a(L²−x²) diffusion: infinitesimal splitting of a position into neighboring ticks.
- **V_t[u](x) = ∫ V_t(x, y) u(y) w(y) dy** — Hilbert–Schmidt integral operator: nonlocal cross-tick redistribution driven by LP repositioning (the empirically observed cross-mode dependence).
- h(t, x): arrival rate of new liquidity.
- Boundary behavior: degenerate at ±L (not uniformly elliptic); if b/2a ∈ (0, 1) impose lim_{x→±L}(L²−x²)^{b/2a} u′(x)=0, else no boundary condition needed. A = L − V generates a C₀-semigroup ⇒ existence/uniqueness of the mild solution in weighted L²_w.

## Spectral reduction — the workhorse

The eigensystem is **Gegenbauer (ultraspherical)** with order

```
α = b/(2a) − 1/2,  w(x) = (L²−x²)^{(α−1)/2},  p(x) = a(L²−x²)^{α+1/2}
λ_n = a·n·(n + 2α)
```

- a=1, b=2, L=1 ⇒ α=1/2: the **Legendre operator**, λ_n = n(n+1). λ_0 = 0 always — the level mode is a unit root absent relocation (V) or source (h).
- Expanding in eigenfunctions e_n converts the SPIDE into a **coupled infinite system of linear SDEs** for the modes u^n_t, coupling only through the V_nk matrix elements:

```
du^n_t = [−Σ_k (λ_k δ_nk + V_nk) u^k_t + h^n_t] dt + Σ_m [σ^n_m + Σ_k σ̃^nk_m u^k_t] dW^m_t
```

- **Low-order modes = level, slope, curvature** of the profile — the same interpretation as empirical Legendre/PCA diagnostics, so the model nests prior functional-PCA analysis as its K-truncation.
- Verified numerically: eigenrelation residuals ~1e-10 for α ∈ {0.5, 1, 1.5, 2.5}; finite-rank system with dense V is stationary (ρ(exp(−A_K∆))<1) while V=0 leaves ρ=1 from λ_0=0.

## Market model: pairing with a log-price process

Couple the profile SPIDE with `dr_t = (μ_t − σ_t²/2)dt + σ_t dZ_t` (Z ⊥ W):
- **OU-type**: σ̃_m ≡ 0 ⇒ additive noise ⇒ Gaussian; natural in (r, u) **log-liquidity** coordinates (u = ln ℓ ⇒ positivity automatic).
- **BS-type**: σ_m ≡ 0 ⇒ multiplicative noise linear in profile; natural in (r, U) raw-liquidity coordinates (pool quantities linear in U); nonlocal σ̃ does NOT preserve positivity in general.
The two are distinct specifications — exponentiating one does not solve the other.

Pool quantities in price-liquidity coordinates: `x(p, ℓ)=∫_p^∞ ℓ(q)dq`, `y(p, ℓ)=∫_0^p q ℓ(q)dq`; in log coordinates `x = ∫_r^∞ e^{u(ξ−r)+ξ}dξ`, `y = ∫_{−∞}^r e^{u(ξ−r)+2ξ}dξ`. LVR and its moments evaluate the profile at the spot tick ξ=0 through the eigen-series u_t(0)=Σ u^n_t e_n(0) (mild-solution version, Hölder-½ in time).

## Finite-rank calibration (what the data identify)

Truncate at rank K with V_nk = 0 for n, k ≥ K ⇒ the retained block closes **exactly** as a finite-dim OU process:

```
dc_t = (−A_K c_t + h_K)dt + noise,  A_K = Λ_K + V_K,  Λ_K = diag(λ_0..λ_{K−1})
Time-∆ transition: c̃_{j+1} = Φ_K c̃_j + ε,  Φ_K = exp(−A_K ∆),  ε ~ N(0, Σ_∆)
Σ_∆ = ∫₀^∆ e^{−sA_K} C e^{−sA_K^T} ds,   stationarity ⇔ ρ(Φ_K) < 1
```

Practical recipe (paper's deployment on 3 Uniswap V3 WETH–USDC pools):
1. Tick-level snapshots on a uniform N=201 grid over [−1, 1] in **normalized tick-RANK** coordinates (rank 0 = tick nearest spot; NOT log-moneyness — fitted rates/densities live in rank space).
2. Subsample at fixed block stride (8h); partition into contiguous windows.
3. Center by the temporal mean ū (stationary-branch surrogate; absorbs h); fit the OU transition by Gaussian likelihood; profile over α (concentration order) which shows a flat band.
4. Configurations to isolate what data pin down: Dense-3 (full nonsymmetric V on modes {0,1,2}), Dense-3 + **Frobenius penalty on V** (Hilbert–Schmidt-motivated), Sparse (V diagonal only), Legendre-OU (V=0, level held at unit root).
5. Baselines: martingale null û_{j+1}=u_j (denominator of all ratios) + Factor VAR on mass-weighted PCA coefficients (generic low-rank, no operator structure).
6. Metrics: R_A = active-band mass-weighted RMSE ratio (|x|≤0.5), R_V = value-weighted profile ratio, Hosking whiteness severity S_H ≈ 1 under white residuals.

## Empirical findings (W1 + Full windows, ARB5/ETH5/ETH30)
- **Branch-compatible pools (ARB5, ETH5)**: active-band forecast ratios R_A ≈ 0.93–0.99 / 0.84–0.87 < 1 for every SPIDE configuration — out-of-sample mean reversion carried by the shared low modes.
- **Regularization matters at the broad pool**: unpenalized Dense-3 over-parameterizes on ARB5 Full (R_V = 1.150); the finite-rank Frobenius penalty restores it (R_V = 0.807) while shrinking off-diagonal relocations.
- **Nonstationarity is detectable and honest**: ETH30 (shifting mean profile, stale boundary mass) posts R_A > 1 in all configs — the stationary branch fails there exactly as its failure mode predicts (ū stops approximating the conditional mean), motivating price-aware/time-varying extensions. Report this diagnostic rather than forcing a stationary fit.

## Pitfalls
- The level mode λ_0=0: without relocation or source terms the K-truncated system is a unit root — never fit a stationary OU to the level without V_00 or explicit trending assumptions.
- Rank-grid calibration does not transfer to log-price distance coordinates without a separate coordinate-map calibration.
- R_V value-weights apply in rank coordinates — it diagnoses profile forecast quality, not pool-value forecast.
- A Gaussian OU branch is one branch: additive noise on log-liquidity. Multiplicative (BS) noise needs the (r, U) specification and a fresh calibration.

## Related topics
- lvr-transaction-cost-amm (LVR under transaction costs)
- dealer-market-competition-nash-equilibrium · maker-spread-screening-vs-cadence-threshold (microstructure companions)
- Spectral-operator skills — the Gegenbauer reduction mirrors spectral methods in quantum simulation (orthogonal-polynomial eigensystems)
