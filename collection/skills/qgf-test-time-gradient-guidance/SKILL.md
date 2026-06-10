---
name: qgf-test-time-gradient-guidance
description: QGF (Q-Guided Flow) - test-time RL algorithm that performs policy optimization entirely at test time using value gradient guidance without additional policy learning
version: 1.0.0
author: extracted from arXiv:2606.11087v1
date: 2026-06-11
activation_keywords: [test-time RL, flow policy, gradient guidance, offline RL, goal-conditioned, expressive policy, value gradient]
---

# QGF: Q-Guided Flow - Test-Time Gradient Guidance for Flow Policies

## Overview

QGF (Q-Guided Flow) is a reinforcement learning algorithm that performs policy optimization entirely at test time. It uses the value gradient to guide a reference flow policy to generate higher-value actions without any additional policy learning, avoiding actor-critic training instability.

## Core Innovation

**Test-Time Policy Improvement Pattern:**
- **No policy learning**: Optimization happens only at test/inference time
- **Stable training intact**: Reference policy trained via supervised behavioral cloning
- **Value gradient guidance**: Uses gradient to guide flow policy generation
- **Scalable with model size**: Avoids actor-critic instability, favorable scaling

## Problem Addressed

**Expressive Policy RL Challenges:**
1. **Training instability**: Actor-critic training with expressive policies causes issues
2. **Denoising backpropagation**: Specialized objectives or backprop through denoising
3. **Scalability concerns**: Instability affects policy scaling

## Methodology

### Architecture Components

1. **Reference Flow Policy**
   - Pre-trained via standard behavioral cloning (BC)
   - Stable supervised training objective
   - Expressive policy representation (diffusion/flow model)

2. **Value Function Critic**
   - Pre-trained alongside reference policy
   - Estimates state/action values
   - Provides gradient for test-time guidance

3. **Test-Time Guidance**
   - Uses value gradient to guide flow policy
   - Generates higher-value actions
   - No additional policy learning required

### Training Protocol

1. **Pre-training Phase**
   - Train reference flow policy: Behavioral cloning objective
   - Train value function critic: Standard RL critic training
   
2. **Test-Time Phase**
   - Use value gradient to guide reference policy
   - Generate higher-value actions at inference
   - Policy optimization without learning

3. **Deployment**
   - Deploy guided flow policy
   - Test-time optimization preserves stability

## Performance Metrics

- **Single-task offline RL**: Outperforms prior test-time RL methods
- **Goal-conditioned offline RL**: Competitive with state-of-the-art training-time algorithms
- **High-dimensional action spaces**: Effective for complex control
- **Cost efficiency**: Much cheaper than training-time algorithms
- **Model scaling**: Favorable scaling with model size

## Use Cases

- High-dimensional action space control
- Single-task offline RL benchmarks
- Goal-conditioned tasks
- Robot control with expressive policies
- Stable policy deployment without actor-critic instability

## Implementation Guidelines

1. **Flow Policy Training**: Use standard behavioral cloning for reference policy
2. **Critic Training**: Pre-train value function with standard methods
3. **Test-Time Guidance**: Apply value gradient during inference
4. **Action Generation**: Flow policy guided toward higher-value actions
5. **Scaling**: Leverage model size scaling without training instability

## Key Parameters

- Flow policy: Reference expressive policy (diffusion/flow model)
- Value critic: Pre-trained value function
- Gradient guidance: Test-time value gradient application
- Action space: High-dimensional continuous control

## Advantages Over Previous Methods

- **Actor-critic training**: Avoids instability issues
- **Training-time algorithms**: Much cheaper to run
- **Backprop through denoising**: Eliminates specialized objectives
- **Model scaling**: Favorable scaling without training instability
- **Test-time only**: No additional policy learning

## Technical Details

### Test-Time Guidance Process

```
Pre-training:
  Offline Data → Behavioral Cloning → Reference Flow Policy
  Offline Data → RL Training → Value Function Critic
  
Test-Time:
  Reference Policy + Value Gradient → Guided Action Generation
  (No policy learning, only guidance)
  
Deployment:
  Guided Flow Policy → Robot control (high-value actions)
```

### Expressive Policy Benefits

- Diffusion models: Multi-step denoising for action generation
- Flow models: Continuous action representation
- High-dimensional: Effective for complex action spaces

## References

- arXiv:2606.11087v1 - Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning
- Offline RL benchmarks
- Goal-conditioned RL tasks
- Expressive policy representations (diffusion, flow)

## Related Skills

- `diffusion-policy-robot-control` - Diffusion policy implementations
- `flow-policy-rl` - Flow policy RL methods
- `offline-rl` - Offline RL methodologies
- `test-time-optimization` - Test-time optimization patterns
- `actor-critic-rl` - Actor-critic alternatives