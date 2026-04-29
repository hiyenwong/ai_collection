---
name: poisson-gradient-estimation-guide
version: 1.0.0
category: ai_collection
tags: [poisson, gradient-estimation, latent-variable, computational-neuroscience, Gumbel-SoftMax, exponential-arrival]
activation_keywords: [Poisson, gradient estimation, latent variable, firing rate, spike train, Gumbel-SoftMax, EAT]
created: 2026-04-24
source: arXiv:2602.03896
description: Skill for poisson gradient estimation guide
---


# Hitchhiker's Guide to Poisson Gradient Estimation

## Overview
Systematic comparison and practical guide for gradient estimation through Poisson-distributed latent variable models, widely used in computational neuroscience. Compares Exponential Arrival Time (EAT) simulation and Gumbel-SoftMax (GSM) relaxation approaches.

## Key Contributions
- **First systematic comparison** of EAT and GSM for Poisson gradient estimation
- **Modified EAT method**: guarantees unbiased first moment (exactly matching firing rate) and reduces second-moment bias
- Practical guidance for practitioners on when to use each method

## Methods Compared

### Exponential Arrival Time (EAT) Simulation
- Simulates spike trains as events in time using exponential inter-arrival times
- Naturally differentiable through continuous time variables
- Modified version ensures exact firing rate matching

### Gumbel-SoftMax (GSM) Relaxation
- Relaxes discrete Poisson samples to continuous distributions
- Temperature parameter controls relaxation tightness
- Standard approach in deep learning but may introduce bias

## Implementation Guidelines

### Choosing Between Methods
1. **Use modified EAT when**: exact first-moment matching is critical (e.g., firing rate models)
2. **Use GSM when**: computational efficiency is prioritized over exact matching
3. **Both methods**: applicable to variational inference in neural data models

### Modified EAT Algorithm
1. Generate exponential arrival times: t_k ~ Exp(lambda)
2. Count events in observation window [0, T]
3. Apply modified reparameterization for unbiased gradient estimation
4. Validate: E[count] = lambda * T (exact match)

## Applications
- Neural data analysis with Poisson observation models
- Variational autoencoders for neural spike trains
- Fitting GLMs to neural recording data
- Bayesian inference in computational neuroscience

## Authors
Michael Ibrahim, Hanqi Zhao, Eli Sennesh, Zhi Li, Anqi Wu

## References
- arXiv:2602.03896 (2026-02-03)


## Tools Used

- `read` - 读取相关文件和资料
- `write` - 创建实现代码
- `exec` - 运行实验和验证


## Instructions for Agents

1. 阅读技能内容，理解核心方法论
2. 根据用户需求提供相应的技术指导
3. 结合实际应用场景给出建议
4. 如需代码实现，参考核心贡献部分的方法


## Examples

### Example 1: 基本概念理解

**User:** 什么是 Poisson Gradient Estimation Guide?

**Agent:** Poisson Gradient Estimation Guide 是一种计算方法...

### Example 2: 实际应用

**User:** 如何在项目中使用这个方法?

**Agent:** 你可以按照以下步骤应用...


## Activation Keywords

- poisson-gradient-estimation-guide
- poisson gradient estimation
- poisson gradient estimation guide
