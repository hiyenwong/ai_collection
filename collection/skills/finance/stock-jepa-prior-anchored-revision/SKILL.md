---
name: stock-jepa-prior-anchored-revision
description: Use when combining financial priors with deep representation learning for equity return forecasting.
category: ai_collection
---

# STOCK-JEPA: Prior-Anchored Latent Revision Representation Learning in Equity Markets

**Paper**: STOCK-JEPA: Prior-Anchored Latent Revision Representation Learning in Equity Markets (arXiv:2610.07006, Oct 2026)
**Authors**: Yizhi Luo, Jiahe Yi, Jianhui Zhang, Shuo Sun (HKUST-GZ, SJTU, BZA)
**Activation**: stock representation learning, equity forecasting, financial prior, JEPA finance, residual learning asset pricing, latent revision, cross-sectional ranking

## Core Methodology

STOCK-JEPA reframes financial representation learning as **learning predictable incremental revisions relative to a point-in-time financial prior** — instead of end-to-end prediction of noisy realized returns.

### 1. Information-Structure Decomposition (the theory)

Nested σ-algebras G ⊆ H:
- **G** = σ(P): prior statistics only (what a low-complexity financial model knows)
- **H** = σ(P, X_ctx): prior + historical context

Key objects:
```
Z_anc := E[Z_tgt | G]          # anchor: what the prior predicts
Δ     := E[Z_tgt | H] − Z_anc  # revision: what history adds
D     := Z_tgt − Z_anc = Δ + ε_lat   # observed displacement (noisy target)
```

**Proposition 1 (exact risk reduction)**: With squared loss, the optimal revision reduces prediction risk by exactly **R_H = R_G − E‖Δ‖²₂**, with equality iff Δ=0 a.s. This is the tower-property/conditional-expectation guarantee (Banerjee et al. 2005 optimality of conditional expectation as Bregman predictor) — adding history can only maintain or reduce minimum MSE, and the gain is the predictable displacement magnitude. Note E[Δ|G]=0: this is a conditional-mean restriction, NOT an independence assumption, and does NOT require the prior to span the true factor space.

### 2. Three-Stage Pipeline

**S1 — Point-in-time financial prior**: multi-output Ridge regression maps stock/market descriptors to 8 forecasts (return, volatility, drawdown, market-relative return × 5/21-day horizons), combined with coordinate-wise historical log-residual scales → P_t ∈ R¹⁶. Block-wise point-in-time fitting (no lookahead); fixed during representation learning.

**S2 — Prior-anchored representation learning** (the JEPA core):
- Target encoder T_θ̄: encodes standardized future window X_tgt (21×40) → Z_tgt (stop-gradient)
- Prior projector A_φ: maps P_t into the same d_z-dim latent space → anchor Ẑ_anc (G-measurable by construction)
- Context encoder E_θ: summarizes 126-day history (126×40; 28 asset + 12 market variables)
- Revision predictor Q_ψ: predicts Δ̂ = Q_ψ(H, Ẑ_anc)
- **EMA targets**: T_θ̄, A_φ̄ updated as exponential moving averages, receive NO gradients
- Masking operator M on context during training only; identity at inference

**Separate losses (critical design)**:
```
L_anc = E‖Ẑ_anc − Z_tgt‖²₂     # updates ONLY A_φ (prior branch)
L_rev = E‖Δ̂ − D_trn‖²₂        # updates ONLY E_θ, Q_ψ (context branch)
```
The anchor is **detached** in both the predictor input and the displacement target. A joint loss on the SUM would leave the anchor/revision allocation unspecified (branch compensation ambiguity).

**S3 — Frozen readout**: single MLP f_ω on [s_t; P_t; Ẑ_anc; Δ̂] → return forecast; ALL representation modules frozen; readout trained on 21-day log-return labels. Separates representation learning from return supervision.

### 3. Empirical Results

- CN ALL (5,669 securities) & US ALL (10,152): best on 4/5 metrics each market vs 13 baselines (FMB, IPCA, LSTM, Transformer, iTransformer, TimeMixer, FactorVAE, StockMixer, MASTER, PRISM-VQ, T-JEPA, TS-JEPA, Fin-JEPA)
- RankIC 11.22% (CN) / 12.96% (US), +14.0%/+15.9% over second-best (MASTER/FactorVAE); strongest vanilla-JEPA baseline only 4.09%/0.69%
- Net Sharpe 1.50 (CN top-30 long-only) / 1.24 (US long-short), net AR 45.66%/68.20%, mildest MDD −40.12% in US long-short
- Test period Jan 2024–Jun 2026, 5 bps transaction costs both sides
- Ablations: Separate-EMA > Separate-online > Joint-online > Ordinary-JEPA on portfolio metrics — the prior anchoring AND the separate objectives both matter
- Simulation: anchor recovers slow signal (R² 66.14%), revision recovers fast signal (R² 49.25%) without component supervision; Ordinary-JEPA fails slow-signal recovery
- Revision structure: effective rank 21.1 (128-dim), broad market-average revision shifts around monetary-policy repricing / trade-tension events

## Reusable Patterns

1. **Prior-relative residual learning in latent space**: replace raw-residual prediction with `predict E[Z_future | full info] − E[Z_future | prior]` — the noise ε_lat averages out because it's H-measurable mean-zero. Generalizes to any domain with a structured low-complexity prior (physics simulators, factor models, epidemic baselines).

2. **Separate objectives to prevent branch compensation**: when a pipeline output is a SUM of two branches, train each branch against its own well-defined target with the other branch detached; otherwise gradient paths let branches trade off against each other.

3. **Noisy-target regression via conditional mean**: regress on the observed noisy displacement D (not on the clean decomposition) — the optimal squared-loss predictor of D given H is exactly Δ. You never need clean labels.

4. **EMA-anchored JEPA for low-SNR regimes**: EMA target + anchor encoders stabilize the moving target; when combined with prior anchoring, EMA anchor beats online anchor on downstream portfolio metrics.

5. **Frozen-representation evaluation protocol**: freeze all representation modules, train only a lightweight readout on the downstream task — clean separation of representation quality from task overfitting.

## Pitfalls / Notes

- The future window X_tgt is used ONLY as a representation-learning target (stop-gradient); at inference only history + prior are needed — no lookahead.
- Prior statistics include residual scales shared within block — these are historical fitting errors, not sample-specific predictive uncertainty.
- US long-short MDD is still −40%: top-30/bottom-30 batches on small caps are exposed to short-side upward jumps.
- Vanilla JEPA baselines perform poorly on equities (RankIC ≤4.09%) — the prior anchor is what makes JEPA viable in low-SNR financial data.

## Relation to Existing Skills

- Extends `markets-hard-to-predict-framework` (epistemic vs aleatoric decomposition → here operationalized as anchor vs revision)
- Financial-prior counterpart of `neurolens-jepa-chronic-recordings` (JEPA for electrode drift) and `ai-collection/meta-learning-in-context-brain-decoding`
- Complements `residual-learning-empirical-asset-pricing` (2610.09613, same-day listing) — that is return-space residual learning; STOCK-JEPA is representation-space
