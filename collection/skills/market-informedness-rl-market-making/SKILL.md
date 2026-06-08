---
name: market-informedness-rl-market-making
description: "Market making with heterogeneous agents using reinforcement learning. MAPPO algorithm in CTDE setting with finite-horizon stability guarantees for Hawkes market-taker process. Analyzes how market maker profitability increases with market informedness (adverse selection risk). Use when: market making, RL trading, MAPPO, CTDE, Hawkes processes, adverse selection, order flow, bid-ask spread, profitability analysis."
metadata:
  arxiv_id: "2606.05882"
  published: "2026-06-04"
  authors: "Konrad Ochedzan, Nino Antulov-Fantulin"
  tags: [market-making, reinforcement-learning, MAPPO, Hawkes-process, adverse-selection]
---

## Context

Market makers compete in environments with heterogeneous agents (informed traders, noise traders). Traditional models assume homogeneous agents, but real markets have information asymmetry. This paper studies how market maker profitability depends on the degree of market informedness.

## Core Methodology

1. **MAPPO in CTDE**: Multi-Agent Proximal Policy Optimization in Centralized Training with Decentralized Execution
2. **Hawkes Process Modeling**: Market-taker arrival modeled as Hawkes process with finite-horizon stability guarantees
3. **Adverse Selection Analysis**: Quantifies how informed trader presence affects market maker profitability through adverse selection risk
4. **Heterogeneous Agent Simulation**: Multiple agent types with different information sets and trading objectives

## Key Results

- Market maker profitability INCREASES with market informedness (counterintuitive)
- Adverse selection risk is bounded under Hawkes process stability conditions
- CTDE setting enables coordination between market makers while maintaining decentralized execution
- Hawkes process captures bursty order flow patterns better than Poisson baseline

## Implementation Steps

1. Define agent types: market makers (provide liquidity), informed traders (exploit information), noise traders (random)
2. Model order flow as Hawkes process with self-excitation parameter
3. Verify Hawkes process stability (spectral radius of excitation kernel < 1)
4. Train MAPPO with centralized critic (observes all agent states) and decentralized actors (each agent observes local state)
5. Evaluate profitability as function of informed trader fraction
6. Analyze adverse selection: decompose P&L into spread revenue vs adverse selection losses

## Pitfalls

- **Counterintuitive result**: Higher informedness can increase MM profitability — informed traders generate more volume, increasing spread capture
- **Hawkes stability**: Must verify excitation kernel spectral radius < 1, otherwise process explodes
- **CTDE communication**: Centralized critic must observe all states — simulation environment needs full observability during training
- **Adverse selection decomposition**: Separating spread revenue from adverse selection losses requires careful attribution methodology

## Verification

- Verify Hawkes process stability (spectral radius condition)
- Confirm MAPPO convergence with centralized critic
- Check profitability curve is monotonically increasing in informedness fraction
- Validate adverse selection decomposition sums to total P&L

## Activation Keywords

market making, RL trading, MAPPO, CTDE, Hawkes process, adverse selection, order flow, bid-ask spread, profitability, informed traders, heterogeneous agents, liquidity provision
