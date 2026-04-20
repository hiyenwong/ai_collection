---
name: snn-learning-survey
description: Comprehensive survey of Spiking Neural Network learning algorithms. Classification of Hebbian, gradient-based, reward-based, and bio-inspired learning methods with computational efficiency vs. biological plausibility analysis.
category: neuroscience
tags: [spiking neural network, SNN, learning algorithms, survey, Hebbian, gradient-based, surrogate gradient, bio-inspired]
created: 2026-04-18
source: "A Survey on Spiking Neural Network: Learning Algorithms"
arxiv: https://arxiv.org/abs/2504.13817
---

# SNN Learning Algorithms Survey

## Overview
Comprehensive taxonomy and analysis of learning algorithms for Spiking Neural Networks (SNNs), covering bio-inspired, gradient-based, and hybrid approaches.

## Learning Algorithm Classification

### 1. Bio-Inspired Learning
- **Hebbian Learning**: Correlation-based weight updates (Δw = η·x_pre·x_post)
- **STDP**: Spike-Timing Dependent Plasticity with temporal windows
- **Homeostatic Plasticity**: Maintains network stability through activity regulation
- **Synaptic Scaling**: Global weight adjustment for homeostasis

### 2. Gradient-Based Learning
- **BPTT**: Backpropagation Through Time for temporal sequences
- **Surrogate Gradients**: Smooth approximations for non-differentiable spikes
- **e-prop**: Eligibility propagation for online learning
- **DECOLLE**: Deep Continuous Local Learning with local gradients

### 3. Reward-Based Learning
- **Three-factor rules**: Pre × Post × Reward modulation
- **Actor-Critic**: Value-based reinforcement learning in SNNs
- **Policy Gradient**: Direct policy optimization with spiking neurons

### 4. Hybrid Approaches
- **ANN-to-SNN conversion**: Train ANN, convert to SNN for inference
- **Direct training**: Train SNN directly with surrogate gradients
- **Neuromodulated learning**: Combine bio-inspired and gradient methods

## Comparison Framework

| Criterion | Bio-Inspired | Gradient-Based | Reward-Based |
|-----------|-------------|----------------|--------------|
| Biological plausibility | High | Low | Medium |
| Computational efficiency | High | Medium | Medium |
| Task performance | Medium | High | High |
| Temporal credit assignment | Limited | Excellent | Good |
| Online learning capability | Excellent | Limited | Good |

## Practical Guidelines
- Use bio-inspired for unsupervised feature learning
- Use gradient-based for supervised tasks requiring high accuracy
- Use reward-based for reinforcement learning scenarios
- Consider hybrid approaches for best of both worlds

## Key Challenges
- Temporal credit assignment in spiking networks
- Balancing biological plausibility with computational efficiency
- Handling vanishing gradients in deep SNNs
- Designing effective surrogate gradient functions

## Verification Steps
1. Benchmark learning algorithm on standard temporal tasks
2. Compare computational efficiency across methods
3. Validate biological plausibility against neuroscientific data
4. Test scalability to deeper architectures
5. Evaluate robustness to noise and parameter variations

## Activation Keywords

- "snn-learning-survey"
- "snn learning survey"
- "use snn learning survey"
- "snn learning survey help"
- "snn learning survey tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Snn Learning Survey usage
```
User: "Help me with snn learning survey"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed snn learning survey assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
