---
name: csows-cost-sensitive-window-expert-aggregation
description: "Use for online window-size expert aggregation with regret bounds."
activation: window size selection, sliding window portfolio, Fixed Share, Hedge algorithm, tracking regret, transaction cost aware online learning, expert aggregation finance, rolling estimation window
category: ai_collection
---

# Cost-Sensitive Online Window Size Selection via Expert Aggregation

**Source**: arXiv:2609.29887 (Liu & Hsieh, NTHU, Sep 2026, math.OC/q-fin)

## Problem This Solves
Rolling-window models (mean-variance portfolios, forecasts) need a window size j. Long windows smooth noise; short windows adapt fast. Classic fixes (Pesaran & Timmermann window averaging, Rossi–Inoue robust selection, Inoue MSFE-equivalence) are batch/statistical — none gives a **sequential learning rule with performance guarantees** that adapts to regime shifts while **accounting for the transaction costs induced by re-weighting itself**.

Key insight the paper formalizes: even if each window-expert's portfolio is unchanged, **changing aggregation weights creates turnover in the deployed aggregate portfolio**. Expert-level costs don't capture this — the regret must.

## Framework (Two-Level)

```
Level 1 (experts): each candidate window j ∈ N solves cost-sensitive Markowitz on last j days:
  w_j(t) = argmax_w  μ̂_j(t)ᵀw − wᵀΣ̂_j(t)w − c(t)·‖w − w_j(t−1)‖₁
  (rolling mean/cov estimators over window j; convex → CVXPY)

Level 2 (aggregation): aggregate portfolio ŵ(t) = Σ_j q_j(t)·w_j(t)
  q(t) updated online from TURNOVER-INCLUSIVE expert losses
  ℓ̃_j(t) = ℓ(w_j(t), y(t)) + c(t)‖w_j(t) − w_j(t−1)‖₁
```

## The Aggregators

**Fixed Share** (tracks the best switching expert sequence):
```
Step 1 exponentiate:  q_j^exp(t) = q_j(t)e^{−ηℓ̃_j(t)} / Σ_k q_k(t)e^{−ηℓ̃_k(t)}
Step 2 share:        q_j(t+1) = (1−α)·q_j^exp(t) + α/n
```
- Hedge = Fixed Share with α=0 (static regret vs best FIXED window)
- α>0 guarantees floor weight α/n → recoverability after regime shifts
- Higher η → faster adaptation; lower η → stable weights

## Regret Decomposition (Theorem 3.1 — the core result)

For ANY aggregation rule, cost-sensitive tracking regret against best expert sequence with ≤K switches:

```
R^c_track(T,K) ≤ Σ_t [Σ_j q_j(t)ℓ̃_j(t) − ℓ̃_{j_t}(t)]   (expert-loss regret)
               + Σ_t c(t)‖q(t) − q(t−1)‖₁                (weight-shift turnover term)
```

**The coefficient 1 on the second term is SHARP** (cannot be reduced): proven by a 2-asset/2-expert construction where ℓ≡0, c(1)=0<c(2), experts hold e₁,e₂, weights flip (1,0)→(0,1) → regret = 2c(2) = bound exactly.

Derivation steps (reusable):
1. Jensen (ℓ convex): ℓ(ŵ,y) ≤ Σ_j q_j ℓ(w_j,y)
2. Add-subtract Σ_j q_j(t)w_j(t−1) in the aggregate turnover, then triangle inequality:
   c‖ŵ(t)−ŵ(t−1)‖₁ ≤ c Σ_j q_j(t)‖w_j(t)−w_j(t−1)‖₁ + c‖q(t)−q(t−1)‖₁
   (uses ‖w_j‖₁=1 on the simplex)

## Fixed Share Bound (Corollary 3.4)

```
R^c_track(T,K) ≤ C(K,α,n,T)/η + (η/8)Σ_t(b−a+2c(t))²
               + η Σ_{t≥2} c(t)[(b−a+2c(t−1)) + 2α(1−1/n)]

C(K,α,n,T) = log n                                if α=0, K=0 (Hedge static)
           = ∞                                     if α=0, K>0  (Hedge can't track)
           = (K+1)log n + K log(1/α) + (T−K−1)log(1/(1−α))   otherwise
```

Bounded losses a ≤ ℓ ≤ b give expert losses ℓ̃_j ∈ [a, b+2c(t)] (max ℓ₁ distance on simplex = 2).

**Weight-variation lemma**: ‖q(t)−q(t−1)‖₁ ≤ η·(max_j ℓ̃_j(t−1) − min_j ℓ̃_j(t−1)) + 2α(1−1/n) — mixing α has its own turnover price.

## Optimal Tuning (Proposition 3.5)

- **c=0, K≥0**: α* = K/(T−1), η* = √(8C/(b−a)T) → bound (b−a)√(T·2[(K+1)log n + (T−1)H(K/(T−1))]/2) with binary entropy H
- **c>0, K=0** (static): α*=0, η*=√(log n/A_T) → R ≤ 2√(A_T log n), where A_T = Σ(b−a+2c)²/8 + Σ c(t)(b−a+2c(t−1))
- **c>0, K≥1**: α* solves √(C(K,α,n,T)/α(1−α)) = 2(1−1/n)C_T/√(A_T) implicitly; η* = √(C/A_T)
- **Hannan consistency**: with K(T)=o(T) and per-horizon tuning, lim R^c/T ≤ 0 — asymptotic no-regret even with costs

## Empirical Protocol

- Synthetic: 32 stocks, 2000 days, windows N={5,10,21,63}, c=10bps, controlled regime shift at day 1000 (window 63 → 5). Fixed Share reallocates faster than Hedge; regret tracks theoretical bound; the optimal-switch oracle regret flattens.
- Real: DJIA (2021–2024) and S&P 500 (2020–2026) with N={5,10,21,30,41,50,63,126}: Hedge/Fixed Share beat UP/EG/PAMR/CWMR/OLMAR on S&P cumulative return (578%/471% vs ~205%), smaller DJIA drawdowns (−12.6% vs −20%); mean-reversion baselines collapse (−88%).
- Loss used: negative PnL ℓ = −fᵀy + c‖f−f_{t−1}‖₁ (not just tracking error).

## Reusable Patterns

1. **Parameter-as-expert**: any hyperparameter whose best value drifts (window size, lookback, regularization strength, model order) → spawn one expert per value, aggregate online with Fixed Share, get tracking-regret guarantees instead of grid-search-and-freeze.
2. **Cost-aware expert loss**: fold each expert's OWN switching/actuation cost into the loss fed to the aggregator (ℓ̃ = ℓ + cost), so the weight update itself prices the cost of following that expert.
3. **Aggregate-turnover accounting**: when aggregating controllers/portfolios, the meta-level weight change is itself a cost source — decompose with add-subtract + triangle inequality; the extra ‖q(t)−q(t−1)‖₁ term is tight and must appear in any honest bound.
4. **Hedge vs Fixed Share decision**: static environment or unknown shift count → Hedge (α=0); nonstationary with switching budget K(T)=o(T) → Fixed Share with α≈K/(T−1); α>0 needed for recoverability but pays 2α(1−1/n) in extra drift.
5. **Sharpness certificates**: prove bound-tightness with minimal 2-expert constructions (ℓ≡0, one nonzero cost step, weight flip) — cheap way to certify coefficients are not loose.

## Pitfalls

- Switching budget K restricts the COMPARATOR, not the market — it's an analysis device, not an assumption on data.
- Jensen step requires ℓ convex in first argument (negative PnL qualifies; some utility functions may not).
- Fixed Share with α=0 CANNOT track switching comparators (C=∞ case) — don't use Hedge in regimes you expect to shift.
- c(t) sequence must be known/estimated for optimal tuning; with unknown costs use Corollary 3.4 form with conservative η.
- Bound terms grow with (b−a) — normalize/clip losses to keep the range tight, or η tuning degrades.

## Related Skills / KG

- `a-share-trading-simulator` — rolling window trading (apply expert aggregation to its window choice)
- `recap-regime-adaptive-portfolio` — regime-aware portfolio management (Fixed Share is a lighter-weight online alternative)
- `deep-timeseries-equity-portfolio-benchmark` — benchmarking methodology for deep TS portfolio models
- KG: arXiv:2609.29887, q-fin/math.OC
