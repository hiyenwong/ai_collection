---
name: evolutionary-search-drl-orchestration
description: "DRL-DCO: Deep RL-governed dynamic DE-CMA-ES orchestration for high-dimensional optimization. DDPG actor-critic fluidly reallocates resources between exploration (DE) and exploitation (CMA-ES) with progression-aware rewards."
tags: [evolutionary-algorithms, deep-rl, optimization, cma-es, differential-evolution, model-updating]
source: "arXiv:2610.11546"
utility_score: 0.85
---

# Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination

## Paper Metadata

- **arXiv ID**: 2610.11546
- **Title**: Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating
- **Authors**: Lechen Li, Rongye Shi, Wanhuan Zhou
- **Published**: 2026-10-08
- **Categories**: cs.NE, cs.AI
- **Link**: https://arxiv.org/abs/2610.11546

## Abstract Summary

Solving high-dimensional structural model updating problems requires an algorithm capable of navigating complex, non-convex landscapes with correlated parameters. Existing hybrid evolutionary algorithms typically rely on static architecture or fixed switching rules, resulting in disjointed search phases. This work proposes a Deep Reinforcement Learning-governed dynamic DE-CMAES Orchestration (DRL-DCO) algorithm, in which a Deep Deterministic Policy Gradient (DDPG)-based actor-critic agent continuously governs the evolutionary process as a single, unified system. Guided by a progression-aware state representation and a diversity-informed reward, the agent fluidly reallocates computational resources between the difference-vector-based exploration of Differential Evolution (DE) and the covariance-guided exploitation of CMA-ES, while jointly regulating population size, elite preservation, and a restart mechanism. Beyond the training phase, the trained actor can operate in a supervision-free inference mode, where the internalized policy autonomously orchestrates DE and CMA-ES control from observed search states through forward inference alone. Validated on high-dimensional single-objective optimization benchmarks and the IASC-ASCE structural health monitoring benchmark, DRL-DCO achieves superior convergence accuracy and robustness.

## Key Contributions

1. **DRL-governed orchestration**: DDPG actor-critic continuously governs evolutionary process as unified system
2. **Dynamic resource allocation**: Fluidly reallocates between DE exploration and CMA-ES exploitation
3. **Progression-aware state**: State representation tracks search progress for informed decisions
4. **Diversity-informed reward**: Reward function balances exploration-exploitation based on population diversity
5. **Supervision-free inference**: Trained actor operates via forward inference alone after training

## Research Implications

- **Adaptive algorithms**: Moves beyond static hybrid algorithms to learned orchestration
- **Unified search**: Treats DE and CMA-ES as complementary tools in unified framework
- **Autonomous optimization**: Eliminates need for manual algorithm selection and switching rules
- **Transfer learning**: Trained policy can orchestrate search on new problems without retraining
- **Structural health monitoring**: Demonstrated on real-world engineering benchmark

## Practical Applications

- High-dimensional optimization in engineering design
- Structural model updating for health monitoring
- Black-box optimization with correlated parameters
- Autonomous optimization without manual algorithm tuning
- Complex non-convex landscape navigation

## Related Work

- Evolutionary algorithms
- CMA-ES and differential evolution
- Deep reinforcement learning for optimization
- Hybrid metaheuristics
- Structural health monitoring
