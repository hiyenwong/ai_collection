---
name: factorbench-portfolio-aware-factor-mining
description: Use when benchmarking automated factor mining or evaluating discovered alpha signals. Portfolio-aware three-level protocol.
category: economics
---

# FactorBench: Portfolio-Aware Benchmark for Automated Factor Mining

**Source**: arXiv:2610.06947 (Wang & Ventre, King's College London, q-fin.PM/cs.LG, 2026-10-03) — benchmark comparing ~5,000 factors from 9 automated mining methods (GP, AlphaGen, AlphaCFG, AlphaQCM, AlphaForge, AlphaSAGE, R&D-Agent, AlphaAgent, QuantaAlpha) across 5 equity markets (S&P 100, HSI, CSI 300, FTSE 100, Nikkei 225). Repo: github.com/ZhuoHan1998/FactorBench-Release

## Core Finding

**No mining paradigm consistently dominates.** Relative advantages change at every stage of the discovery→evaluation→portfolio chain. GP/RL/generative methods show high training IC that collapses out-of-sample; LLM agents have lower train IC but their held-out IC is NOT consistently higher; LLM-generated pools are closer to published classical factors (Alpha101) than non-LLM search. Alpha101 itself remains competitive with all mined pools after costs.

## The Three-Level Evaluation Protocol (the reusable part)

### Level 1 — Factor validity & temporal generalization
- **Execution contract**: both symbolic expressions and executable Python code map to a standardized date-by-asset signal matrix. A factor-market instance is *executable* if it runs under the contract; *scorable* if ≥100 scorable dates per split (≥2 stocks with finite values + nonzero cross-sectional variance).
- **IC**: daily cross-sectional Pearson correlation between signal and 20-day forward return, reported separately for train (2017–21) / validation (2022–23) / test (2024–25).
- **Orientation freeze**: factor sign is fixed from TRAINING IC only — negative validation/test IC then means genuine out-of-sample sign reversal (adaptive overfitting signal).
- **Residual IC (style neutralization)**: regress the signed factor cross-sectionally on market beta, volatility, momentum, short-term reversal, liquidity; adjusted R² quantifies exposure overlap, residual IC measures predictiveness beyond style. **High raw IC with near-zero residual IC = performance is repackaged style exposure, not alpha.**

### Level 2 — Pool distinctness (three forms)
Similarity = time-averaged |daily cross-sectional Spearman correlation| on matched dates.
1. Within-method redundancy (does one run duplicate itself?)
2. Across-method distinctness (do systems converge on the same signal space? — non-LLM cluster together; LLM agents cluster together via shared foundation model priors)
3. Similarity to Alpha101 (are mined "novel" factors just published formulas?)

Nominal pool size ≠ effective signal breadth. AlphaGen/AlphaQCM most internally redundant (related expression spaces + IC objectives); AlphaSAGE highly redundant in CSI 300 but diverse elsewhere (market-dependent).

### Level 3 — Composite & after-cost portfolio
- Unified selection: pre-test-period predictive evidence + redundancy limit.
- Combination: equal weight / validation-IC weight / ridge regression (weights learned on train, regularization on validation).
- Portfolio test: long-only (active return vs equal-weight benchmark) AND dollar-neutral long-short (isolates cross-sectional value from market direction). 20-day rebalance, 10 bps per dollar traded, short-borrow costs included.
- **Diagnostics that explain returns**: positive raw composite IC with small/negative RankIC = weak monotonic ordering; raw→residual IC collapse identifies style-lease performance (R&D-Agent: 0.0253→0.0011; AlphaQCM retains most; Alpha101 nearly unchanged).

## Key Empirical Numbers

| Method | Raw IC | Residual IC | L/S Sharpe | Turnover |
|---|---|---|---|---|
| R&D-Agent | 0.0253 (highest) | 0.0011 (collapses) | 0.679 | 7.8× |
| AlphaQCM | 0.0191 | 0.0175 (retains) | 0.668 | 4.6× (lowest) |
| Alpha101 | 0.0238 | 0.0237 (unchanged) | 0.340 | 6.4× |
| GP | 0.0165 | −0.0067 | 0.340 | 6.3× |

- GP/R&D-Agent highest exposure overlap (adj. R²): GP rediscovers styles because it searches transformations of the same price-volume variables the controls are built from; R&D-Agent's pretrained financial knowledge favors established concepts.
- Runtime 0.14h (GP) → 27.9h (QuantaAlpha); validity 80.5–100%. LLM wall-clock includes API latency.
- Long-only CAGR 22–31%, Sharpe 1.03–1.31 across ALL methods — weakly discriminating; long-short (Sharpe −0.087 to 0.679) is the discriminating test.

## Reusable Design Rules

1. **Never judge a mining system by its search objective or in-sample score** — trace outputs through validity → temporal generalization → exposure neutralization → pool distinctness → after-cost portfolio.
2. **Freeze factor orientation on training data** so held-out sign reversals are interpretable as decay, not luck.
3. **Always report residual IC after style neutralization** alongside raw IC; the raw-vs-residual gap is the style-lease diagnostic.
4. **Pool size is not breadth** — measure within-method correlation before celebrating factor count.
5. **Long-short after-cost results discriminate; long-only CAGR flatters everything** in a rising test window.
6. Compare g-like quantities only at matched sample size n (conditioning sensitivity — see photonic-reservoir-kernel-geometry for the parallel lesson).

## Limitations

Five large-cap markets, one daily 20-day target, one chronological split, 3 seeds/method; residual IC controls only 5 exposures (not pure alpha — no industry classifications); static universes, simplified cost/borrow models; native discovery processes preserved (runtime differences are NOT controlled efficiency comparisons).

## Related Skills

- `governed-self-evolution-anytime-referee` — anytime-valid governance of agent-proposed factors (CSI 500 application)
- `mean-expectile-wasserstein-dro-portfolio` — robust portfolio optimization (downstream consumer of factors)
- `economics/stock-analysis` — technical analysis pipeline
