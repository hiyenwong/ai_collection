---
name: rl-nqs-optimization
description: Frame neural quantum state optimization as reinforcement learning for scalable wavefunction approximation.
trigger_keywords: ["rl-nqs", "neural quantum states optimization", "reinforcement learning quantum", "NQS RL", "autoregressive quantum", "wavefunction RL"]
---

# RL-NQS Optimization

## Description

Methodology from arXiv:2607.02292 that frames Neural Quantum States (NQS) optimization as a reinforcement learning problem. Autoregressive NQS models enable exact, independent sampling from the Born distribution, avoiding MCMC autocorrelation issues. The key insight: treat each local spin update as an RL action and use energy reduction as the reward signal, bridging the gap between scalable Adam (which ignores function space geometry) and stochastic reconfiguration (geometry-aware but doesn't scale).

## Core Methodology

1. **Autoregressive NQS as Policy Network**: Use autoregressive neural network as the policy for spin configuration sampling
2. **Energy as Reward**: Define reward as negative energy difference (ΔE) between successive configurations
3. **Local Spin Actions**: Each spin flip/rotation is an atomic action in the RL environment
4. **Geometry-Aware Updates**: Implicitly capture the Fubini-Study metric through RL reward shaping, without explicit SR matrix inversion

## Key Patterns

- **Autoregressive Sampling**: Replace MCMC with direct autoregressive generation for independent samples from Born distribution
- **RL Formulation**: State = spin configuration, Action = local spin update, Reward = -ΔE
- **Scalability**: O(N) per update vs O(N²) for stochastic reconfiguration
- **Exploration Strategy**: ε-greedy or softmax over spin flip actions with temperature scheduling

## Applications

- Quantum many-body ground state preparation
- Quantum phase transition characterization
- Molecular electronic structure problems
- Spin glass optimization

## Activation

Use when: optimizing variational quantum states, improving NQS training scalability, replacing SR with more scalable methods, applying RL to quantum many-body problems.

**Keywords**: neural quantum states, reinforcement learning optimization, autoregressive sampling, Born distribution, stochastic reconfiguration, Fubini-Study metric, variational Monte Carlo
