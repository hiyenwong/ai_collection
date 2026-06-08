---
name: market-informedness-rl-market-making
description: "Market making with heterogeneous agents and reinforcement learning — MAPPO algorithm with finite-horizon stability guarantees for Hawkes market-taker processes. Shows profitability increases with market informedness."
category: economics
tags: [market-making, reinforcement-learning, multi-agent, hawkes-process, informedness, adverse-selection, MAPPO, CTDE]
---

# Market Informedness & RL Market Making

## Context

Market makers face adverse selection risk from informed traders while providing liquidity. Traditional models assume homogeneous agents and static equilibrium, missing the dynamic interplay between market maker strategies and trader behavior. Multi-agent reinforcement learning (MARL) with proper stability guarantees enables study of how market informedness affects profitability.

Source: arXiv:2606.05882 — "The Impact of Market Informedness on Market Makers' Profitability"

## Core Methodology

1. **Heterogeneous Agent Modeling**: Model market with multiple agent types — informed traders (with private information), noise traders (random), and market makers (liquidity providers). Each has distinct objectives and information sets.

2. **MAPPO in CTDE Setting**: Use Multi-Agent Proximal Policy Optimization (MAPPO) in Centralized Training, Decentralized Execution (CTDE) paradigm. Centralized critic sees full state during training; each agent acts on local observations during execution.

3. **Hawkes Process for Order Flow**: Model market-taker arrivals as a Hawkes process (self-exciting point process). This captures the clustering of trades and the feedback between order flow and future arrivals.

4. **Finite-Horizon Stability Guarantees**: Derive theoretical bounds on policy stability over finite horizons — crucial for market making where strategies must be reliable within trading sessions.

5. **Informedness-Profiteability Analysis**: Systematically vary the fraction of informed traders and measure impact on market maker profitability, inventory risk, and spread dynamics.

## Implementation Steps

1. **Define the Market Environment**:
   - Order book dynamics (limit order book with bid/ask queues)
   - Agent types: informed (signal-driven), noise (random), market maker
   - Hawkes process parameters for order arrival intensity

2. **State Representation**:
   - Market maker: current inventory, bid-ask spread, recent trade flow
   - Informed trader: private signal about true value
   - Global: order book state, recent price history

3. **Action Space**:
   - Market maker: set bid and ask prices (continuous or discrete)
   - Include inventory skewing to manage risk

4. **Reward Design**:
   - Market maker: P&L from spreads minus inventory holding cost
   - Include penalty for large inventory positions
   - Terminal penalty for inventory at horizon end

5. **Training Protocol**:
   - Centralized critic observes all agent states
   - Each agent optimizes its own policy
   - Use Hawkes-driven order arrival for realistic dynamics

6. **Analysis**:
   - Vary informed trader fraction from 0% to 50%
   - Measure market maker profitability, spread, inventory
   - Test stability under different Hawkes parameter regimes

## Key Results

- Market maker profitability **increases** with market informedness (counterintuitive — informed flow provides more predictable adverse selection patterns)
- Hawkes process captures realistic order flow clustering
- MAPPO converges to equilibrium strategies that adapt to informedness level
- Finite-horizon stability guarantees ensure deployable strategies

## Pitfalls

- **Hawkes Parameter Calibration**: Self-excitation parameter must be < 1 for stability; calibrate on real order flow data
- **CTDE Scalability**: Centralized critic may not scale to many agent types — consider parameter sharing or graph-based approaches
- **Reward Shaping**: Poor reward design can lead to pathological strategies (e.g., never quoting). Include minimum spread constraints.
- **Market Regime Changes**: Model trained on one volatility regime may fail in another — include regime-switching in environment

## Verification

1. Check that MAPPO policies converge to known analytical solutions in simple cases (e.g., Avellaneda-Stoikov)
2. Verify Hawkes process produces realistic order flow statistics (clustering, heavy tails)
3. Test policy robustness: perturb Hawkes parameters and measure performance degradation
4. Compare informedness-profitability curve against theoretical predictions

## Activation Keywords

market making, informedness, adverse selection, reinforcement learning, multi-agent, MAPPO, CTDE, Hawkes process, order flow, liquidity provision, spread dynamics, inventory risk
