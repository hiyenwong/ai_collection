---
name: lob-path-irreversibility-simulator-benchmark
description: Measure time-irreversibility of LOB paths as a simulator benchmark.
category: ai_collection
---

# LOB Path Irreversibility: Ordering Increment as Simulator Benchmark

**Source**: Yeo, Cha & Hwang, "Neural Estimation of Irreversibility in Real and Simulated Limit Order Book Paths" (arXiv:2610.16151, q-fin.TR, v2 2026-10-15; ICAIF '26).

## Core Idea

A path indistinguishable from its own reverse carries no arrow of time. Define the **irreversibility rate** of a coarse-grained limit-order-book path as the forward-to-reverse log-density ratio per event, estimated with an antisymmetric neural score (density-ratio estimation by classification, from stochastic thermodynamics). The **ordering increment** — the gap between an order-sensitive network (temporal CNN) and an order-invariant network (pooled MLP) — isolates the part of the asymmetry that lives in the *order* of events rather than their *composition*. This becomes a within-path benchmark that generated-vs-real distributional comparisons miss entirely.

## Method Pipeline

1. **Event-clock coarse-graining**: block = B source events (completed book updates, not raw messages); realized count N_t = B + overshoot. Block z_t = [S_{t-1}, U_t, S_t] — boundary state + interval features. 37 features in 4 groups (book state, mechanical flow, liquidity events, price) + activity clock. Exclude order IDs, raw timestamps, message labels (order age alone separates forward from reverse).
2. **Physical reversal R**: state levels keep values but swap position; odd features (signed mid change, net depth change, quote changes) flip sign; paired event roles (depletion/appearance) exchange. R^2 = identity.
3. **Antisymmetric score**: s0(W) = g(W) - g(RW) for any network g — cancels all even-in-time components automatically. Balanced logistic loss gives the log-density ratio at optimum. Temperature-scale alpha on calibration days; clip logits to +/- log 99.
4. **Two networks, same blocks/encoder/budget**: pooled (mean+max of block embeddings — permutation invariant) vs ordered (3 residual dilated TCNs, dilations 1,2,4, receptive field 15). Delta_order = I_ordered - I_pooled, in nats per event (normalize by realized event count, weight dates equally).
5. **Splits**: 15 days -> 9 development / 3 calibration / 3 held-out; overlapping paths stay within split; 3 seeds; report per-date signs.

## Key Results (NVDA, B=10, K=6, daytime)

- Pooled 0.036 vs ordered 0.054 nats/event; increment 0.018, positive for all 12 symbols on every held-out date (SOFI 0.004 to AAPL 0.018).
- Linear baselines: ~0.0004 nats — two orders of magnitude below; asymmetry is nonlinear composition.
- Shuffle blocks -> increment collapses 0.0071 -> 0.00055; K=1 gives increment -0.0013 (negative); circular padding barely moves it (0.0179 -> 0.0160). Increment is tied to real block order, not capacity or boundary cues.
- One-step references: K=1 score summed along path falls short by 0.016-0.032 nats; Eulerian surrogate preserving the coarse transition table recovers 30% LESS irreversibility than observed paths. Both point to higher-order path dependence.
- Rate is representation- and scale-bound: at fixed horizon 60 updates, increment 0.0216 (B=5,K=12) / 0.0179 (10,6) / 0.0020 (30,2). Always report (B, K).
- **Simulator verdict**: calibrated queue-reactive simulator matches the ordered rate (0.051-0.052 vs 0.054) but its increment is 0.0006 vs 0.018 — it builds temporal asymmetry out of block composition, not block order. Swapping in real durations (QR-B) moves it by only 0.0001.
- Scores add no forecasting power over standard book/flow inputs (delta MSE < 0.12% in 22/24 combos) — this is a diagnostic, not an alpha.

## Pitfalls

- Reversal must be physical (per-feature even/odd/role-exchange), not naive sequence flip — message labels are not one-to-one reversible (cancel vs execution ambiguity).
- Overlapping paths violate row-level independence — aggregate per date.
- Logit clipping bounds per-path score; at long K the bound saturates (84% of ordered paths at K=12) — report unclipped alongside.
- Threshold/comparison across books must fix (B, K): "the rate belongs to a representation and scale, not a market".

## Reuse

- Simulator evaluation beyond marginals: any generative market simulator (queue-reactive, GAN, learned) can be scored on (ordering increment, scale profile) — does it reproduce WHERE the asymmetry lives?
- Same antisymmetric paired-score machinery transfers to any trajectory data with a definable physical reversal: molecular dynamics, agent-based simulations, neural SDE samplers.

## Metadata

- arxiv_id: 2610.16151
- published: 2026-10-12 (v2 2026-10-15)
- authors: Hyeonjun Yeo, Doohwi Cha, Yoontae Hwang
- code: https://github.com/hjyeo30/lob-irreversibility
- tags: [limit-order-book, time-irreversibility, density-ratio, market-simulation, benchmark, econophysics]
