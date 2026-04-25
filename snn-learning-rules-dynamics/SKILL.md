---
name: snn-learning-rules-dynamics
description: SNN learning rules, dynamics, and learning ability analysis methodology. Covers Hebbian/anti-Hebbian learning, reward-based learning, backpropagation, surrogate gradients, and their relationships to network dynamics.
category: neuroscience
tags: [spiking neural network, SNN, learning rules, Hebbian learning, surrogate gradient, neural dynamics, computational neuroscience]
created: 2026-04-18
source: "Learning Rules, Dynamics and Learning Ability in Spiking Neural Networks"
arxiv: https://arxiv.org/abs/2504.13718
---

# SNN Learning Rules and Dynamics Analysis

## Overview
Comprehensive methodology for analyzing learning rules in Spiking Neural Networks (SNNs) and their relationships to network dynamics and learning ability.

## Key Learning Rules

### 1. Hebbian Learning
- **Core principle**: "Neurons that fire together, wire together"
- **Mathematical form**: Δw = η·x_pre·x_post (correlation-based weight update)
- **Anti-Hebbian**: Δw = -η·x_pre·x_post (decorrelation for competition)
- **Applications**: Unsupervised learning, feature extraction, STDP

### 2. Spike-Timing Dependent Plasticity (STDP)
- **Temporal Hebbian learning**: Weight changes depend on precise spike timing
- **Causal STDP**: Pre before post → LTP (long-term potentiation)
- **Anti-causal STDP**: Post before pre → LTD (long-term depression)
- **Window function**: Δw = f(Δt) where Δt = t_post - t_pre

### 3. Reward-Modulated Learning
- **Three-factor rule**: Δw = η·pre·post·R (R = reward signal)
- **Eligibility traces**: e(t) = ∫exp(-(t-t')/τ)·pre(t')·post(t') dt'
- **Weight update**: Δw = η·e(t)·R(t)
- **Applications**: Reinforcement learning in SNNs

### 4. Backpropagation Through Time (BPTT)
- **Unroll recurrent network**: Treat as feedforward over time steps
- **Gradient computation**: Backpropagate error through time
- **Challenges**: Vanishing/exploding gradients, non-differentiable spikes

### 5. Surrogate Gradient Methods
- **Replace Heaviside with smooth approximation**: σ'(u) ≈ sigmoid'(u), fast_sigmoid'(u)
- **Common functions**: sigmoid, arctan, piecewise linear, exponential
- **Trade-offs**: Accuracy vs. computational efficiency

## Dynamics-Learning Relationships

### Network Dynamics States
1. **Asynchronous irregular (AI)**: Desynchronized, irregular firing (optimal for learning)
2. **Synchronous regular (SR)**: Synchronized oscillations (can impair learning)
3. **Critical dynamics**: Balance between order and chaos (maximal information processing)

### Learning Impact on Dynamics
- Hebbian learning → can drive network toward synchronization
- Anti-Hebbian learning → promotes asynchronous activity
- Homeostatic plasticity → maintains activity in AI regime
- Reward learning → shapes dynamics toward task-relevant patterns

## Practical Guidelines

### Choosing Learning Rules
| Task Type | Recommended Rule | Rationale |
|-----------|------------------|-----------|
| Unsupervised feature learning | STDP, Hebbian | Local, biologically plausible |
| Reinforcement learning | Reward-modulated STDP | Handles delayed feedback |
| Supervised classification | Surrogate gradient BPTT | Precise error gradients |
| Temporal pattern learning | BPTT or e-prop | Handles temporal dependencies |

### Stability Considerations
1. **Weight normalization**: Prevent runaway excitation/inhibition
2. **Homeostatic plasticity**: Maintain target firing rates
3. **Synaptic scaling**: Global weight adjustment for stability
4. **Metaplasticity**: Plasticity depends on history (prevent saturation)

## Common Pitfalls
- Ignoring the relationship between learning rules and emergent dynamics
- Using BPTT without surrogate gradients (non-differentiable spikes)
- Applying rate-based learning rules to spike-based networks
- Not considering temporal credit assignment in spiking networks
- Overlooking the role of neuromodulators in biological learning

## Verification Steps
1. Verify learning rule is compatible with network dynamics
2. Check weight distributions remain bounded
3. Monitor firing rate stability during training
4. Validate surrogate gradient choice against task requirements
5. Test learning rule on benchmark temporal tasks (e.g., XOR, pattern recognition)

## References
- Learning Rules, Dynamics and Learning Ability in Spiking Neural Networks (arXiv:2504.13718)
- A Survey on Spiking Neural Network: Learning Algorithms (arXiv:2504.13817)
- Three-factor learning rules for SNNs
- DECOLLE: Deep Continuous Local Learning
