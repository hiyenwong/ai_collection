---
name: online-neuroevolution-island-ensemble-edge
description: "Island-champion rank ensembles for online NAS on streams."
category: ai_collection
trigger: online neuroevolution, ONE-NAS, neural architecture search time series, island model ensemble, evolved population reading, rank-mean ensemble, edge forecasting deployment, Raspberry Pi inference, non-stationary stream forecasting, data drift adaptation, population-based search ensemble, low-parameter alternatives to transformers
---

# Online Neuroevolution Island-Ensemble + Host/Edge Deployment

**Source**: Chang & Lyu, "Evolve on the Host, Predict on the Edge: Deploying Online Neuroevolutionary Architecture Search for Cross-sectional Stock Return Prediction" (arXiv:2610.10038, cs.NE/cs.CE, Oct 2026)
Code: https://github.com/zimenglyu/ONENAS

## Core Thesis

When an evolving population of small RNNs tracks a non-stationary stream (ONE-NAS online neuroevolution), **how you READ the population at scoring time matters more than the search itself**: the single global-best genome (all prior work) trails every neural baseline (+4.5%), while the same runs read as a **rank-mean ensemble of island champions** return +27.5% net of costs (paired gain +23.0pp, t=18.2) — because individual champions are weak (rank IC ~0.0065-0.0068) and weakly correlated (mean pairwise Spearman ρ 0.150-0.166), so averaging N of them multiplies signal by the equicorrelated factor N/(1+(N-1)ρ), matching measured ensemble IC within 3%. **The search does not pay by finding one good architecture; it pays by producing a diverse population.**

## Key Results

| Arm | Net return 2022-24 | Sharpe | Break-even cost multiple |
|---|---|---|---|
| Island-ensemble N=40 (rank-mean) | **+27.5%** | 0.87 | 10.6× |
| Single champion (prior ONE-NAS reading) | +4.5% | 0.21 | — |
| Online LSTM / GRU (1 step/day) | +11.3 / +11.7% | — | 4.5× |
| Periodic LSTM (monthly retrain) | +14.8% | — | 5.4× |
| Online AR(1) | -3.3% | — | — |

- Ensemble beats every baseline in 2022 and 2023; paired t>6.5 over 40 (panel, seed) cells. Fama-French+momentum alpha +10.0 to +11.2%/yr (t≈2.56-2.77, Newey-West lag 10) at market β≈0.11 — near market-neutral, not factor exposure.
- Gain is **positive in 16/16 configurations** of the tuning screen (mean +8.3pp at 8-island width) — not a tuned artifact.
- Cost robustness: at 5× realistic transaction costs the ensemble still returns +15.6-18.8% while online LSTM/GRU go negative; partly from lower turnover (0.12 vs 0.13-0.14 of gross book/day).
- Island count: return/Sharpe rise steeply 10→~20 islands then flatten (20-60 indistinguishable at 10 seeds); width mainly buys **consistency** (per-seed Sharpe SD 0.227→0.11-0.13; worst seed 0.53→0.91). Inference cost on endpoint scales with N.
- Warm-start matters: population evolving since 2020-01 returns +26.5% vs +12.3% cold-started 2022-01 — more than half the return comes from pre-evaluation evolution. **Start the population well before the period it must serve, never reset.**

## Method Mechanics

### ONE-NAS online protocol (prequential, leakage-free by construction)
1. Stream partitioned into windows of W=5 trading days; **one generation per window**.
2. At generation t, revealed history Ht splits into: **validation block = V=5 most recent windows** (fitness=MSE there) and **training pool = everything older** (offspring train 10 epochs on subsequences L=40 days).
3. Predict window t+1 day-by-day as features arrive; when it closes, labels append, validation block slides forward.
4. No genome is ever trained on data it is scored on, or selected on data it later predicts.

### Genome = directed graph (EXAMM-style)
- Hidden nodes drawn from a cell-type library (simple, UGRNN, MGU, GRU, Δ-RNN, LSTM); edges feedforward or recurrent.
- Grows from a **minimal seed genome** (input→output only) — depth, recurrence, cell composition are all search outcomes.
- Offspring inherit parent weights for retained components (brief training only); mutations = node/edge insertion-deletion, recurrent-edge insertion, cell-type change; plus crossover.
- **N=40 islands** evolve independently with rare inter-island crossover → increasing structural diversity over time. Async worker pool; wall-clock scales with workers, not population size.

### The two population readings (scoring-time decision, same runs)
- **Single-champion rule** (prior work): global best genome predicts alone.
- **Island-champion ensemble rule**: best elite of EACH island predicts; each predicted cross-section converted to **ranks**, ranks averaged across N members. Ranks (not raw outputs) because members have non-comparable output scales and downstream consumers read only the ordering.
- Ensemble MSE 0.975 < single champion 1.031 < average member — the combination beats what the search would ship.

### Ensembling math (why it works)
- Weakly correlated weak learners: ensemble IC ≈ m·N/(1+(N-1)ρ) for equicorrelated averaging — with m≈0.0066, ρ≈0.16, N=40 this predicts measured ensemble IC within 3%.
- Implication: **island diversity is the product**. Anything that collapses islands into one lineage destroys the ensemble gain (cf. PBT-PPO diversity collapse).

## Host/Edge Deployment Pattern (generalizable)
- **Split workloads by cost asymmetry**: parallel expensive search on host (cloud/workstation); cheap inference on endpoint (Raspberry Pi 4B, $50).
- Each generation, host **serialises champion genomes** (graph structure + cell types + weights, binary) and ships over TCP/IP; endpoint deserialises and predicts online; **prediction and search overlap in time but are decoupled across hardware**.
- Endpoint is **stateless w.r.t. search**: if host unavailable, it keeps predicting from last received genomes and resynchronises at next hand-off. Inference cost scales only with N and #securities, not with search size.
- Measured on Pi 4B: single champion 24.6 ms per 50-stock window; 40-member ensemble 556 ms (39× weights at 23× time) — both far inside daily cadence. 88% of single-champion energy is board idle → **uptime dominates compute at this scale**; evolved-network size governs energy (size control = energy control). INA219 whole-board metering with idle subtraction.

## When to Apply / Integration Patterns

- **Non-stationary streams where refit schedules go stale between refits**: online NAS adapts architecture AND weights continuously; no offline phase to rot.
- **Reading ANY evolved/population-based search result**: default to the diverse-ensemble reading (per-island or per-niche champions + rank aggregation) instead of the single best individual. Check member correlation first — the gain formula tells you what to expect; if ρ→1 the ensemble gain vanishes.
- **Rank-normalise outputs before ensembling** whenever scales are incomparable and consumers only need orderings (cross-sectional ranking, retrieval, recommendation).
- **Edge deployment of continuous learning**: ship generations, not weight deltas — endpoint never needs the search infrastructure; graceful degradation via last-received genomes.
- **Low-SNR prediction problems** (finance, sensor streams): prefer many small diverse models over one large one; ensemble gain (+23pp) dwarfs architecture-search gain (+4.5pp single).
- **Honest evaluation on drifting data**: prequential windows + sliding validation block + burn-in/tuning/evaluation span split + paired (panel, seed) t-tests. All configuration decisions on tuning span only; report on a disjoint evaluation span.

## Limitations (honest)
- Search is compute-heavy at the host (128-core cluster node used); the ensemble reading costs nothing extra but requires having run islands.
- Ensemble endpoint cost scales linearly with N (23× single time at 40 members) — fine for daily cadence, not for high-frequency.
- Finance results are daily cross-sectional rank prediction with realistic CRSP bid-ask costs; authors note live execution layer is future work.
- Single-champion rule can win where island diversity collapses (small N, heavy inter-island crossover) — the equicorrelated formula is the check.

## Related Skills

- `neuroevolution-continual-rl-stability-plasticity` — parameter-space NE for continual RL; complementary evidence that population-based search handles non-stationarity better than gradient methods
- `a-share-trading-simulator` — trading-simulation context
- `early-reservoir-evolutionary-learning` — evolutionary reservoir learning (single-model reading)
