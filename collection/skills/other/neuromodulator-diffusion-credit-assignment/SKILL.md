---
name: neuromodulator-diffusion-credit-assignment
version: 1.0.0
category: ai_collection
tags: [neuromodulator, credit-assignment, spiking-neural-network, reinforcement-learning, diffusion, plasticity]
activation_keywords: [neuromodulator, credit assignment, diffusion, temporal credit, spiking network learning, volume transmission]
created: 2026-04-24
source: arXiv:2603.08949
description: Skill for neuromodulator diffusion credit assignment
---


# Neuromodulator Diffusion for Temporal Credit Assignment

## Overview
Learning mechanism inspired by volume transmission of neuromodulators in biological neural networks. Error information diffuses locally through the network, enabling neurons to learn even without direct feedback by using local concentration of a diffusing credit signal.

## Core Mechanism
- **Diffusive Credit Signaling**: Error signals propagate via local diffusion (mimicking volume transmission), not point-to-point synapses
- **Sparse Feedback Connectivity**: Works in recurrent spiking neural networks where only a subset of neurons receive direct error feedback
- **Local Concentration Learning**: Neurons use local neuromodulator concentration to modulate synaptic plasticity

## Key Results
- Improves learning accuracy in recurrent SNNs with sparse feedback
- Biological plausibility: mirrors real neuromodulatory systems (dopamine, serotonin, acetylcholine)
- Enables temporal credit assignment over longer timescales than direct feedback alone

## Implementation Guidelines

### Diffusion Model
1. Define a diffusion kernel for credit signal propagation across network topology
2. Credit signal concentration C(x,t) follows: dC/dt = D * nabla^2(C) - gamma*C + S(x,t)
   - D: diffusion coefficient (spatial spread rate)
   - gamma: decay rate (temporal extent)
   - S(x,t): source term (neurons receiving direct feedback)
3. Each neuron reads local C to modulate its weight updates

### Integration with SNN Training
1. Combine diffusive credit with STDP or surrogate gradient methods
2. Weight update: delta_w = eta * C_local * eligibility_trace
3. Tune D and gamma for task-specific temporal credit requirements

## Applications
- Recurrent SNN training with sparse feedback
- Biologically plausible deep learning in spiking networks
- Temporal credit assignment in reinforcement learning scenarios
- Neuromorphic computing with on-chip learning

## Authors
Joao Barretto-Bittar, Anna Levina, Emmanouil Giannakakis, Roxana Zeraati

## References
- arXiv:2603.08949 (2026-03-09)


## Activation Keywords

- neuromodulator-diffusion-credit-assignment
- neuromodulator diffusion credit
- neuromodulator diffusion credit assignment


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Neuromodulator Diffusion Credit Assignment

**Agent:** Neuromodulator Diffusion Credit Assignment 是关于...
