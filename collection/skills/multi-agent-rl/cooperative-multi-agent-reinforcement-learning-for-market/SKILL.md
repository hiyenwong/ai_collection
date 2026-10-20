---
name: cooperative-multi-agent-reinforcement-learning-for-market
description: "Cooperative Multi-Agent Reinforcement Learning for..."
tags: [stat.ML, cs.LG, cs.MA]
source: arxiv
arxiv_id: 2610.26789v1
utility: 1.0
published: 2026-10-19
---

# Cooperative Multi-Agent Reinforcement Learning for Market Making on Prediction-Market Order Books

**Authors:** Skander Lejmi
**Published:** 2026-10-19
**arXiv:** [2610.26789v1](https://arxiv.org/abs/2610.26789v1)
**Categories:** stat.ML, cs.LG, cs.MA, q-fin.TR
**Utility Score:** 1.0

## Abstract

A market maker provides liquidity by quoting prices to buy and sell an asset, earning the spread while managing inventory risk. We study market makers trained with multi-agent reinforcement learning on prediction markets, specifically Polymarket, whose thin order books pose distinct challenges. Three challenges underpin this research: adverse selection may cause a policy trained on real data to stop quoting; the consequences of a quote can arrive many steps after the action; and prediction-market L2 data does not identify individual orders needed for simulation. We address these challenges by reconstructing order-level LOBSTER-format data from Polymarket and training agents in JaxMARL-HFT on 417 real markets. We enrich the baseline market maker's observation space with the book and recent flow, redesign its actions and inventory controls, and propose a cooperative multi-agent decomposition into a quoter and a risk manager trained using recurrent Independent Proximal Policy Optimisation (IPPO) with RNN policies. We investigate reward shaping, particularly reward blending and post-fill markout, to mitigate credit-assignment difficulties between the agents. Our redesigned single-agent market maker quotes more frequently and incurs smaller held-out losses than the retrained JaxMARL-HFT baseline, although the contributions of jointly changed observations, actions and risk constraints are not separately identified. Decomposition alone performs poorly; careful reward design substant

## Key Contributions

- Novel research in stat.ML, cs.LG
- Published 2026-10-19

## Activation

cooperative, multiagent, reinforcement, learning, market, making, predictionmarket, order, books
