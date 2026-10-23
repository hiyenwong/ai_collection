---
name: maker-spread-screening-vs-cadence-threshold
description: Break-even spread model trading quote cadence against informed-flow screening.
category: ai_collection
---

# Maker's Spread: Screening Threshold vs Repricing Cadence

**Source**: Adadurov et al., "How Much Screening Buys a Second? Speed, Selection, and the Maker's Spread" (arXiv:2610.21510, q-fin.TR, 2026-10-15).

## Core Idea

A liquidity provider facing stale-quote adverse selection has exactly two defenses: reprice sooner (shorter exposure horizon h) or screen informed flow (reject fraction eta). A single break-even condition prices both on one scale, yielding the **exact screening threshold** eta_crit — the screening rate at which a slower screened maker matches a faster unscreened venue's spread.

## Model

- Innovation Z_h = p_{t+h} - p_t, only requires integrable mean-zero increments (jumps, atoms, infinite variance all admissible).
- Truncated informed loss: A_h(s) = E[(|Z_h| - s)+], s = half-spread.
- Break-even (Glosten-Milgrom competitive condition): s* = r(theta, eta) * A_h(s*), with r = theta(1-eta)/(1-theta).
- **Theorem 1 (exact threshold)**: eta_crit(h_P, theta) = 1 - A_{h0}(s0)/A_{hP}(s0), where s0 is the fast venue's spread. Ranking: s*(h_P, eta) <=> s0 iff eta <=> eta_crit.
- Scale-free: multiplying innovations by c multiplies spreads by c, leaves eta_crit unchanged.
- Gaussian benchmark: s* ~ sqrt(h) (Brownian scaling); eta_crit -> 1 - sqrt(h0/h_P) as theta -> 0; strictly increasing in theta.
- **Drift is a centering problem**: known drift widens a spot-centered quote (quadratically near zero, linearly as residual noise vanishes), but a quote recentered on the expected reference p_t + mu*h recovers the driftless spread exactly (Prop 16). Drift premium = cost of a centering restriction, not of risk.

## Empirical Results (USDC-WETH pools vs Binance ETH-USDT, Jun-Aug 2026, 1.73M swaps)

- One-second innovation is sharply non-Gaussian: 73.4% of seconds show NO mid change (zero atom), excess kurtosis 154 at 1s. kappa(1s) = 0.29 bps vs Gaussian-implied 0.68 (ratio 0.43), converging as h grows.
- Cutting cadence 12s -> 1s sheds 84.5% of the expected shock on the empirical law (vs 71.1% Gaussian = 1 - 1/sqrt(12)).
- **A 12-second maker must screen >= 84.5% of informed flow to match a 1-second venue** (Gaussian would imply only 71.1%); stays 84.5-85.2% up to the tightest netting toxicity bound theta <= 0.257; ~87.8% at theta = 0.71.
- Staleness elasticity: IV (missed-proposer-slot instrument, F=3046) gives 0.45 for log benchmark move on log staleness — near the diffusion rate 1/2; OLS is biased DOWN (0.22) by endogenous arbitrage timing.
- Directional confirmation: with-trend fills execute at effective spread 11.1 bps LOWER than against-trend (same sign in all 4 pools; shift-test p < 0.002) — the stale quote is picked off at execution, and the 5s markout gap is ~0 (loss already realized in the fill price, no continuation).
- Volatility-anchored rule of thumb theta*sigma*sqrt(h)/(1-theta) overstates the true break-even spread by 1.7x-7x because it ignores participation truncation (informed orders only execute when |Z| > s).

## Identification Discipline (reusable)

- Exogenous reference: Binance leads price discovery (same-slot coef 0.60, 96% absorbed within a minute; pool does not lead: 0.007).
- Exogenous timing variation: missed proposer slots stretch block gaps 12 -> 24/36 s for non-market reasons (IV).
- Toxicity is an upper bound, not a point estimate: batch-netting residual nu(h) vs run-preserving (cyclic rotation) null — rotation explains almost all imbalance, so report objects across theta grid.
- Markout-sign shares are a toxicity proxy trap: against a martingale reference the favorable-markout share is set by the symmetric innovation, not the informed share — measure the loss in the execution price (effective spread), not in post-trade impact.
- Placebos: circular drift-sign shift (>= 1 hour, 500 draws), calm-window restriction, mid vs last-trade reference cross-check.

## Pitfalls

- Screening assumed costless, uninformed-preserving, and independent of opportunity size — loss-weighted screening needs a different formalism.
- Threshold monotonicity in toxicity requires tail ordering (Gaussian); general integrable innovations can reverse it.
- Symmetry of residual innovations is substantive for drift results — counterexample exists without it.
- Pool fixed effects + hour clustering essential: fills in the same hour share one benchmark path.

## Reuse

- Any venue comparison trading latency vs flow selection: CEX/DEX, dark pools, RFQ vs AMM, solver-auction makers.
- The truncated-excess-loss function A_h(s) = E[(|Z|-s)+] is the universal pricing object — works for any integrable innovation, no variance needed.

## Metadata

- arxiv_id: 2610.21510
- published: 2026-10-15
- authors: Aleksei Adadurov, Eduard Airapetian, Anton Chtepine, Antero Eloranta, Boris Pletenev, Andrei Sebyakin, Arsenii Valitov
- tags: [market-microstructure, adverse-selection, amm, screening, cadence, market-making, crypto]
