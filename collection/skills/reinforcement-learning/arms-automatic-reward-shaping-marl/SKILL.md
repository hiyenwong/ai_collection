---
name: arms-automatic-reward-shaping-marl
description: ARMS (Automatic Reward-shaping in Multi-agent Systems) — self-supervised reward shaping for sparse-reward MARL with Nash equilibrium preservation guarantees.
---

# ARMS: Automatic Reward Shaping for Multi-Agent RL

## Overview

Self-supervised reward shaping framework for Multi-Agent Reinforcement Learning (MARL) that learns dense shaping signals from sparse environmental rewards through trajectory ranking. Preserves Nash equilibria under conditional best-response reasoning.

## Core Methodology

### Problem
- Sparse rewards in MARL induce non-stationarity and make reward design delicate
- Single-agent trajectory-ranking guarantees don't transfer to MARL
- Need to preserve strategic structure, not just improve short-term optimization

### Solution: ARMS Framework
1. **Trajectory Ranking**: Rank trajectories by sparse environmental reward
2. **Shaping Reward Learning**: Learn dense shaping signal from rankings (self-supervised)
3. **Conditional Best-Response Reasoning**: Reformulate policy invariance for MARL
4. **Alternating Training**: Policy learning ↔ Reward learning with shared parameters

### Key Theorem
If shaping rewards satisfy conditional best-response conditions, they preserve each agent's best-response set under fixed opponent policies → preserve Nash equilibrium set.

## Implementation Steps

1. Collect trajectories under sparse environmental rewards
2. Rank trajectories by final reward
3. Learn shaping reward function via trajectory ranking loss
4. Alternate between policy update (with shaping) and shaping reward update
5. Monitor for oscillation failure mode; increase exploration if detected

## Applications

- Sparse-reward multi-agent coordination tasks
- Dec-POMDPs with delayed rewards
- Cooperative multi-agent navigation
- Team-based RL tasks

## Pitfalls

- **Oscillation Failure Mode**: Coupled policy-reward dynamics can oscillate
- **Mitigation**: Increase exploration to stabilize dynamics
- **Don't**: Apply single-agent reward shaping guarantees directly to MARL

## Related Skills

- [[gcpo-cooperative-policy-optimization]] — cooperative policy optimization replaces winner-takes-all
- [[distributed-zeroth-order-marlh]] — distributed zeroth-order MARL

## Activation Keywords

ARMS, automatic reward shaping, MARL, multi-agent reward design, sparse reward MARL, trajectory ranking, Nash equilibrium preservation, conditional best-response

## Source

arXiv:2605.23562 — ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning