# Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets

**arXiv ID:** 2605.17307
**Authors:** Kamil Kashif, Robert Ślepaczuk
**Published:** 2026-05-17T07:50:37Z
**Abstract:**
This study develops and evaluates a deep reinforcement learning framework for dynamic portfolio allocation across global equity markets. The Soft Actor-Critic algorithm is used to learn continuous portfolio weights within a Markov Decision Process, incorporating transaction costs, turnover penalties, and diversification constraints into the reward function. Five model configurations are compared, varying in reward formulation, policy structure (flat versus hierarchical Dirichlet), portfolio constraints, and temporal encoder (LSTM versus Transformer), and evaluated via walk-forward optimization across sixteen out-of-sample folds spanning 2003-2026 on the Nasdaq-100, Nikkei 225, and Euro Stoxx 50. Results show that RL strategies achieve competitive risk-adjusted performance primarily in the Euro Stoxx 50, where statistically significant abnormal returns are observed, but the central hypothesis is only partially confirmed: no strategy achieves statistically significant excess returns relative to Buy and Hold under HAC-robust inference across all markets. Regime analysis reveals that RL adds the most value during periods of elevated uncertainty, while ensemble aggregation across markets improves risk-adjusted performance and confirms the benefits of geographic diversification.

## Skill Description

This skill is generated from the arXiv paper: Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets (2605.17307).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.17307](http://arxiv.org/abs/2605.17307v1)
