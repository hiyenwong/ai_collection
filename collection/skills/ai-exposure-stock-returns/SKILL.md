---
name: ai-exposure-stock-returns
description: "AI consumption factor and firm AI-beta long-short premium."
trigger: AI exposure stock returns, AI factor construction, AI beta estimation, LLM token consumption factor, AI premium quintile portfolios, market-implied AI exposure occupations, OpenRouter token data asset pricing, agentic token share, AI consumption growth PCA
---

# The Cross-Section of Stock Returns and AI Exposure (AI-FACTOR-BETA)

**Source**: arXiv:2606.30583 (Borri/LUISS, Liu/Rochester, Tsyvinski/Yale-NBER, Sep 2026 v3; data: OpenRouter, Inc.)

## Problem Class
Measure the economy-wide exposure of public firms to AI consumption growth using **realized** (paid-request) token data — not surveys, patents, or AI-labeled task taxonomies — and price that exposure in the cross-section of equity returns. 380.8 trillion cumulative tokens, 400+ LLMs, Jan 2024–Apr 2026, ~2% of global monthly token consumption.

## Core Pipeline (5 stages)

### Stage 1 — AI Factor construction (PCA)
Build three weekly aggregate series from user–model–day panel:
- **Total tokens** (quantity of LLM work demanded)
- **Dollar usage** (expenditure = quantity × realized price)
- **Distinct active users** (extensive margin of adoption)

AI Factor = **first principal component of standardized weekly LOG GROWTH** of the three series. Use growth (not levels) because asset returns respond to the *unexpected* component of AI consumption, not the mechanical diffusion trend. Baseline loadings: 0.665/0.559/0.496; PC1 explains 56.5% of joint variance.

Sub-factors (same PCA recipe on filtered subsets): closed-source vs open-weight models; paid/core vs new users; seasoned vs casual; long (>75th pct of prior-13-week prompt length) vs short prompts; content category (programming/science/roleplay); agentic (finish_reason=tool_calls) vs ordinary.

### Stage 2 — Firm AI-beta (rolling regression)
```
r_i,τ = α_i,t + β_AI_i,t · AI_τ + β_m_i,t · r_m,τ + ε_i,τ,  τ ∈ W_t
```
- W_t = **13-week rolling window** ending at formation week t; re-estimate weekly
- Controls: log-excess market return (and for robustness: high-tech portfolio, semiconductor portfolio, AI/robotics ETF basket [BOTZ/AIQ/IRBO/ROBO/ARTY/WTAI/CHAT], FF30 industry component, Google Trends AI attention)
- β_AI is *market-implied*: inferred from realized price comovement, time-varying, revised as investors update valuations

### Stage 3 — Quintile portfolios + AI premium
- Sort ALL firms weekly into quintiles by current β_AI (all-stock breakpoints; NYSE-breakpoint robustness), **rebalance weekly**, value-weight (each quintile ≈680 stocks)
- **H−L spread: 60.4 bp/week (t-signif 1%)**; ~53 bp after FF5+momentum (5%)
- Excluding frontier-release weeks: still **34.3 bp/week** — premium NOT confined to release news
- Around frontier releases (Anthropic/DeepSeek/Google/Meta/OpenAI): H−L earns **1.7% over 5-day window**
- Cross-check with **Fama-MacBeth** weekly cross-sectional regressions controlling size, value, profitability, investment, momentum, reversal, leverage, accruals

### Stage 4 — Heterogeneity (which consumption carries the premium)
Closed-source 51.6 bp vs open-weight 23.0 bp · paid/core 44.5 vs new 18.5 · seasoned 54.0 vs non-seasoned 31.6 · long prompts 47.7 vs short 29.6 (all bp/week). Premium concentrated in **intensive, frontier-oriented, sophisticated** consumption. Developed markets ≈10 bp/week; emerging (incl. China) insignificant.

### Stage 5 — Occupation/skill exposure mapping
Firm β_AI → aggregate to industry (value-weight) → map to occupations via **BLS employment weights** → map to skills via **O*NET ratings**.
- +1σ **nonroutine interactive** content → **+0.16σ** exposure; +1σ **nonroutine analytic** → **−0.17σ**
- Interaction/communication skill: coefficient **0.26** (1% signif); information use: negative
- Market-implied exposure diverges from task-based measures (ESZ/Felten/Eloundou/Webb explain <2% of its variation) — market prices rent reallocation, not automatability

## Key Empirical Signatures
| Finding | Value |
|---|---|
| Cumulative tokens (Jan24–Apr26) | 380.8T (11.4B → 15.6T weekly, ×1362) |
| Baseline H−L (value-weighted) | 60.4 bp/week; 53 bp FF5+mom-adjusted |
| Ex-release-weeks spread | 34.3 bp/week |
| Controlling semiconductors / AI-ETF / hi-tech | 48.7 / 35.0 / 53.1 bp |
| FF30-industry removed / Trends-controlled | 54.1 / 69.1 bp |
| Agentic token share | ~0% (2024) → ~½ of all tokens (2026) |
| Agentic price per token | declining (caching + cheap-model routing) |
| Highest / lowest S&P500 exposure | AppLovin / Moderna |
| Most +/- industries | Retail (+) / Health, non-durables (−) |

## Reusable Design Patterns
1. **Consumption→factor→beta→premium chain**: any novel consumption/usage stream (tokens, API calls, cloud spend) can be turned into a priced factor: PCA on growth rates of quantity/spend/breadth, then rolling beta, then quintile spreads — the generic recipe for pricing a technology shock.
2. **Growth-not-levels rule**: factor from log growth of adoption series; levels trend mechanically with diffusion.
3. **Market-implied exposure beats declared exposure**: β from realized price comovement captures belief revisions; supplement (don't replace) with attention (Trends) and industry controls to isolate the shock from hype.
4. **Release-week event studies**: identify frontier-release calendar, compare H−L around releases vs non-release weeks to separate news-revision from persistent premium.
5. **Sub-factor attribution**: decompose the aggregate into usage-quality margins (tier/user-intensity/tenure/prompt-length/agentic) — premium localization identifies WHOSE adoption is priced.
6. **Occupation bridging**: firm β → industry (value-weight) → occupation (BLS weights) → skill (O*NET) generalizes any firm-level factor into labor-market exposure measures.
7. **Agentic detection**: finish_reason == tool_calls tags agentic requests; track tool-call / reasoning-token / cache-read shares separately — each has different cost dynamics.

## Caveats
- Sample = early fast-moving AI diffusion phase; realized premium may decay as adoption matures
- OpenRouter overrepresents sophisticated/developer users → premium tied to pricing of *observed sophisticated* consumption
- Agentic premium estimates positive but statistically insignificant (too recent)
- Data licensed/aggregated — original user–model–day rows not redistributable

## Implementation Notes
- Panel: user–model–day level; model = specific version (Opus 4.7 ≠ Opus 4.6)
- Portfolio math: weekly OLS on log-excess returns; Newey–West (5 lags) t-stats for spreads
- Equal-weight (Panel A) and WLS by market cap (Panel B) variants; both significant
- Related: Anthropic Economic Index (single-provider conversation taxonomy, ~1M convs); Eisfeldt-Schubert-Zhang (task-based firm exposure); Aubakirova et al. 2025 (OpenRouter/a16z 100T stylized facts, arXiv:2601.10088)
