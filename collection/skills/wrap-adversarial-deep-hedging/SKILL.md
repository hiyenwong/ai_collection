---
name: wrap-adversarial-deep-hedging
description: Two-budget DRO robust deep hedging under market drift.
category: ai_collection
trigger: deep hedging, nonstationary market, distributionally robust optimization, adversarial reweighting, Wasserstein transport, drift-aware weights, phi-divergence, path perturbation robustness
---

# WRAP: Wasserstein-Reweighting Adversarial Perturbation for Deep Hedging

**Paper**: "Adversarial Training for Deep Hedging in Nonstationary Markets" — Schneider, Looser, Garin, Liu, Kuhn (EPFL / Waterloo, arXiv:2610.07162, Oct 2026)

## Problem

Deep hedging (Buehler et al. 2019) learns a sequence of state-dependent trading decisions from historical/simulated market trajectories. Under **nonstationarity**, the training distribution fails to represent the next hedging period through three channels:
1. Old trajectories are less temporally relevant
2. Reference distribution assigns wrong probability mass to scenarios
3. Future trajectories differ from observed ones

The robust-hedging problem therefore splits into: (a) how to build the reference distribution from temporally heterogeneous data, (b) how to protect the hedge against residual misspecification around it.

## Core Method

### 1. Drift-aware reference distribution (channel 1)
- Weighted empirical law `mu_w = Σ w_n δ_{X_n}` with weights `w_n` FIXED during training, chosen independently of hedging losses
- Trade-off formalized by two quantities:
  - **Effective sample size** `N_eff(w) = 1/Σ w_n²` — governs sampling uncertainty (more spread weight → larger N_eff → tighter concentration bound)
  - **Drift index** `D_p(w) = (Σ w_n (N−n+1)^p)^{1/p}` — governs cumulative drift exposure (each step adds one distribution shift toward P_{N+1})
- Drift model: `W∞(P_n, P_{n+1}) ≤ ϱ` (uniform bound on one-step law changes)
- Calibrated radius (Theorem 2.3): `ε_ϱ(w,β) = D_p(w)·ϱ + [c₂N_eff(w)^(−ν) + log(1/β)/(c₁N_eff(w))]^(1/p)` — covers P_{N+1} w.p. ≥ 1−β
- Optimal weights maximize `N_eff(w)(ε_ϱ − D_p(w)ϱ)^{2p+}` → closed form `w_n = a₁ − a₂(N−n+1)^{p+}` (truncated polynomial): as drift bound ϱ grows, mass shifts to recent observations; small ϱ favors broad allocation

### 2. Two-budget OT–φ ambiguity set (channels 2+3)

`B_{ε,τ}(μ_w) = { η : ∃π,π' couplings, π₁=μ_w, π₂'=η, D_φ(π'∥π) ≤ τ, ∫d_{κ,λ}^p dπ ≤ ε^p }`

- **τ (φ-divergence budget)**: adversary reweights observed trajectories (scenario-probability misspecification). KL or Pearson χ²
- **ε (transport budget)**: adversary perturbs paths in trajectory space under anisotropic metric
  - `d_{κ,λ}(X,X̃) = (Σᵢ (λᵢ max_t κ_t |X_t^i − X̃_t^i|)^p)^{1/p}` — ℓ∞ over time within each component, ℓp across components → **separate scaling per trading date (κ_t) and market variable (λ_i)**

### 3. Joint first-order expansion (Theorem 3.6) — the key theoretical insight

`V_ϑ(ε,τ) = L̄_w(ϑ) + Υ_w(ϑ)·ε + √(2/φ''(1))·σ_w(ϑ)·√τ + o(√ε + √τ)`

The two adversarial mechanisms have **clean orthogonal leading-order roles**:
- **Transport coefficient** `Υ_w = (Σ w_n ‖g_n‖*^q)^{1/q}` with `g_n = ∇_X ℓ(ϑ; X_n)` → penalizes **sensitivity of loss to path perturbations** (within-scenario sensitivity)
- **Reweighting coefficient** `σ_w = (Σ w_n (L_n − L̄_w)²)^{1/2}` → penalizes **dispersion of losses across trajectories** (cross-scenario heterogeneity)
- Cross-effects only at higher order (though coupled in the exact problem)
- Special cases recover known limits: τ=0 → Wasserstein DRO (Bartl et al.); ε=0 → φ-divergence DRO (Duchi et al.)

### 4. Explicit first-order adversary (Algorithm 1, WRAP)

Per batch I, with current policy ϑ:
1. **Reweight step** (if τ>0): centered losses `Y_n = L_n − L̄_I`; find largest `α_τ ≥ 0` s.t. `1 + α_τ Y_n ≥ 0 ∀n` and `Σ w̄_n φ(1+α_τ Y_n) ≤ τ`; set `w̃_n = w̄_n(1+α_τ Y_n)` → **mass flows to above-average-loss trajectories**
2. **Transport step** (if ε>0): reweighted sensitivity `Υ̃_w = (Σ w̃_n‖g_n‖*^q)^{1/q}`; perturb `X̃_n = X_n + ε·h(g_n)·‖g_n‖*^{(q−1)}·Υ̃_w^{1−q}` where `h(g_n)` is the dual-norm maximizer → **larger perturbations for higher-sensitivity trajectories**, budget-normalized
3. **Outer step**: minimize `J_adv^I(ϑ) = Σ w̃_n ℓ(ϑ; X̃_n)` holding adversary fixed; recompute adversary after each update (Danskin argument gives gradient of robust value to leading order)

Multistep variant: iterate adversary refinement (Appendix D.3); one-step WPGD of He et al. (2025) is the τ=0, uniform-weights special case.

## Why It Works (intuition)

- φ-divergence reweighting = **vertical** robustness: re-prices the SAME scenarios (crashes underweighted by sampling)
- OT transport = **horizontal** robustness: moves trajectories to locally adverse regions (increases realized variation without needing terminal-moneyness change)
- For a European call, transport stresses the sequence of trading gains while barely moving the terminal payoff — precisely the failure mode ERM hedges miss
- Drift-aware weights anchor the ambiguity ball where the data says the market is going, not where it has been

## Empirical Results (Table 1, nonstationary Heston; CVaR objective)

| Method | Far-future CVaR | Δ vs ERM-U |
|--------|----------------|------------|
| ERM-U | 8.992 | — |
| φ-U (reweight only) | 8.128 | −9.6% |
| OT-U (transport only) | 7.811 | −13.1% |
| WRAP-U (joint) | 7.268 | **−19.2%** |
| ERM-W | 8.707 | −3.2% (weights alone) |
| **WRAP-W** | **7.221** | **−19.7%** (best overall) |

- Drift-aware weighting improves EVERY method in every evaluation period (weights and adversary are complementary, not substitutes)
- GAD market-data experiments (Asian calls on AAPL/AMZN/BRK-B/GOOGL/MSFT, entropic risk, fitted regime windows 2008–19/2020–23/2024–25): WRAP-U beats both single-budget methods in all 10 stock×scheme combos; lowers test entropic risk vs ERM-U in 6/10, ties 3 (gains stock-dependent, not a free lunch)
- Transaction-cost and Mean-CVaR extensions also favor joint training
- Loss-landscape visualization (Fig 1): reweighting concentrates probability on high-loss scenarios; transport increases realized variation with small moneyness change; WRAP does both

## Reusable Patterns

### Pattern A: Two-budget robustness decomposition
Any path-dependent sequential decision problem (hedging, inventory, energy trading, robotics under regime drift) can use: separate budgets for (i) scenario-probability misspecification (φ-divergence on empirical weights) and (ii) state-trajectory misspecification (OT in an anisotropic path metric). The first-order expansion tells you the attack is: **tilt weights toward high-loss scenarios ∝ loss dispersion, perturb states along loss-gradient ∝ path sensitivity**. No inner supremum solve needed — one probability multiplier + one perturbed trajectory per sample.

### Pattern B: Recency-vs-sample-size trade-off made rigorous
`N_eff(w) = 1/Σw_n²` vs `D_p(w) = (Σ w_n (N−n+1)^p)^{1/p}` with closed-form truncated-polynomial optimal weights. Generalizes to any learning under distribution drift where "use more old data" vs "trust recency" is a knob — the radius calibration `ε_ϱ = D_p(w)ϱ + O(N_eff^{-ν})` prices both terms.

### Pattern C: Anisotropic path metrics for trajectory perturbations
The `d_{κ,λ}` construction (ℓ∞ in time per component, ℓp across components, per-date weights κ_t, per-variable scales λ_i) lets the adversary spend budget where it matters: e.g., perturb volatility features more than prices, early dates more than expiry. Reusable for any OT-based augmentation of time series.

### Pattern D: Adversarial training as robustness pricing
The expansion `L̄ + Υε + √(2/φ''(1))σ√τ` is a **robustness price formula**: linear in transport radius, sqrt in divergence radius. Use it to (i) sanity-check adversarial-training configs (if your robust gain ≫ first-order prediction, you are overfitting the adversary), (ii) transfer budgets across problem scales.

## Implementation Notes

- Loss: OCE risk measure (CVaR or entropic) with trainable offset m; pathwise loss `ℓ_DH = m + ℓ(−PnL − m)`
- Perturbations applied to input trajectories X (prices + features), gradients `g_n = ∇_X ℓ` w.r.t. INPUT (not parameters) — differentiable simulator required
- Budgets (ε, τ) selected on validation split per setting; drift ratio (ρ/ε_ϱ)* also validated
- Baselines to compare: ERM, φ-only, OT-only, WRAP; weights: uniform (-U) vs drift-aware (-W) — 2×4 grid isolates each factor
- Code: authors state implementation matching paper (AI-verified notation consistency)

## Relation to Existing Skills

- `mean-expectile-wasserstein-dro-portfolio` (2610.11917) — same Wasserstein-DRO family, single-budget, portfolio selection not sequential hedging
- `distributionally-robust-control`, `dr-data-driven-predictive-control` — DRO for control; WRAP adds the drift-aware weighting + two-budget decomposition
- `risk-averse-ensemble-control` — ensemble robustness, complementary approach
- Quantum link (daily topic): robustness budgets ε,τ as conjugate "uncertainty resources" mirrors entanglement-budget analyses in quantum algorithm resource estimates

## Limitations (from authors)

- Weights depend only on temporal ordering, not market state — richer: condition on observable states / latent regimes (HMM), weight by economic similarity
- Budgets via validation, not principled calibration (ε could come from coverage guarantee; τ from finite-sample weight uncertainty)
- Parametric generator (GAD) still needed for market-data experiments; direct training on realized trajectory panels is open
- Gains stock-dependent (6/10 improvements) — not guaranteed to help when test window is milder than training
