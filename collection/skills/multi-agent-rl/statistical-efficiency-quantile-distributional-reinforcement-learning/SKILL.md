---
name: statistical-efficiency-quantile-distributional-reinforcement-learning
description: "Studies quantile-based distributional RL from statistical efficiency perspective. Non-asymptotic error bound O(√(m/n)) under W∞ metric. Achieves optimal √n convergence rate. Asymptotic distribution and semiparametric efficiency bound. Berry-Esseen theorem. Activation: distributional RL, quantile regression, statistical efficiency, policy evaluation, return distribution."
metadata:
  arxiv_id: "2607.08444"
  published: "2026-07-09"
  authors: "Zijie Cheng, Yang Peng, Zhihua Zhang"
  tags: [distributional-reinforcement-learning, quantile-regression, statistical-efficiency, policy-evaluation, return-distribution]
---

# Statistical Efficiency and Inference of Quantile Distributional Reinforcement Learning

## Overview

This paper studies quantile-based distributional reinforcement learning from the perspective of statistical efficiency, focusing on distributional policy evaluation. It establishes non-asymptotic error bounds, asymptotic distributions, and semiparametric efficiency bounds for quantile-based distributional RL estimators.

## Key Innovations

### Non-Asymptotic Error Bounds
- Constructs estimator based on empirical MDP
- Error bound scales as Õ(√(m/n)) under supremum W∞ metric
- m = number of quantiles, n = sample size
- Implies optimal parametric √n convergence rate for fixed m

### Asymptotic Distribution
- Derives asymptotic distribution of quantile parameters √n(θ_m^(n) - θ_m)
- Characterizes semiparametric efficiency bound
- Estimator attains the efficiency bound

### Infinite-Dimensional Limit
- Investigates regime where number of quantiles diverges
- Limit covariance structure matches semiparametric efficiency bound
- Shows quantile-based estimators remain asymptotically efficient

### Berry-Esseen Theorem
- Establishes Berry-Esseen theorem for smooth functionals
- Provides foundation for statistically valid inference
- Enables confidence intervals on functionals of return distribution

## Methodology

1. **Quantile Fixed Point**: Define η_m via quantile-projected distributional Bellman equation
2. **Estimator Construction**: Empirical MDP-based estimator η_m^(n)
3. **Error Analysis**: Non-asymptotic bounds under W∞ metric
4. **Asymptotic Analysis**: Distribution theory and efficiency bounds
5. **Infinite-Dimensional Regime**: Diverging quantile analysis

## Implications

- Quantile-based distributional RL is statistically efficient
- Provides theoretical foundation for inference on return distributions
- Semiparametric efficiency in infinite-dimensional limit is a strong result
- Enables principled uncertainty quantification in distributional RL

## Pitfalls

- Assumes access to a generative model which may not be available in practice
- Fixed-m analysis may not capture the full complexity of adaptive quantile selection
- W∞ metric may be conservative compared to other distributional metrics
- Smooth functionals assumption may not hold for all applications

## Activation Keywords

distributional reinforcement learning, quantile regression, statistical efficiency, policy evaluation, return distribution, semiparametric efficiency, Berry-Esseen, W∞ metric, non-asymptotic bounds

## Paper Reference

arXiv:2607.08444 - "Statistical Efficiency and Inference of Quantile Distributional Reinforcement Learning" (Jul 2026)
