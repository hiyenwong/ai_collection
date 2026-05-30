---
name: cgpo-critic-guided-diffusion-policy
description: Critic-Guided diffusion Policy Optimization - balances exploration and exploitation using training-free guidance in diffusion policy denoising
version: 1.0.0
author: Hermes Agent (from arXiv 2605.30056)
tags: [RL, diffusion-policy, robotics, optimization, exploration-exploitation]
activation_keywords: [diffusion policy, critic guidance, MuJoCo, robotics, exploration exploitation, policy optimization]
---

# CGPO: Critic-Guided Diffusion Policy Optimization

## Overview

CGPO addresses the exploration-exploitation tradeoff in diffusion-based reinforcement learning. It integrates training-free guidance into the denoising process, steering action generation toward high-value regions defined by the critic network.

## Problem Context

### Two Branches of Diffusion RL
1. **Sampling-Based Policy Optimization**: Good exploration, slow convergence
2. **Gradient-Based Policy Optimization**: Good exploitation, collapses to unimodal

### CGPO Solution
Balances both using training-free guidance in denoising process.

## Core Methodology

### Training-Free Guidance Integration
```python
def guided_denoising_step(diffusion_model, critic, noisy_action, t):
    # Standard denoising
    denoised = diffusion_model.denoise(noisy_action, t)
    
    # Compute critic value for action
    action_value = critic.evaluate(denoised)
    
    # Guide toward high-value regions
    guidance_scale = compute_guidance_scale(t)
    guided_action = denoised + guidance_scale * critic_gradient(denoised)
    
    return guided_action
```

### Action Generation Process
```python
def cgpo_generate_action(diffusion_model, critic, num_steps):
    # Start from noise
    action = sample_noise()
    
    # Guided denoising trajectory
    for t in reversed(range(num_steps)):
        action = guided_denoising_step(diffusion_model, critic, action, t)
    
    return action
```

### Policy Update
```python
def cgpo_policy_update(policy, critic, experience_buffer):
    # Use guided actions as regression objectives
    guided_actions = []
    for state in experience_buffer.states:
        action = cgpo_generate_action(policy.diffusion, critic, num_steps)
        guided_actions.append(action)
    
    # Regression loss on guided actions
    loss = policy_regression_loss(policy, guided_actions)
    policy.update(loss)
```

## Implementation Steps

### Step 1: Setup Components
- Diffusion policy model (conditional denoising)
- Critic network (Q-value estimator)
- Guidance scale scheduler

### Step 2: Configure Guidance
```python
# Guidance scale increases as denoising progresses
def compute_guidance_scale(t, total_steps):
    # Higher guidance for later steps (more refined actions)
    return base_scale * (t / total_steps)
```

### Step 3: Training Loop
```python
def cgpo_training(env, policy, critic, episodes):
    for episode in range(episodes):
        state = env.reset()
        action = cgpo_generate_action(policy.diffusion, critic)
        next_state, reward, done = env.step(action)
        
        # Update critic
        critic.update(state, action, reward, next_state)
        
        # Update policy with guided regression
        policy.update_with_guided_targets(critic)
```

## Key Results
- State-of-the-art on 5 MuJoCo locomotion tasks
- First successful diffusion policy on real-world RL (Franka robot arm)
- Superior exploration-exploitation balance

## When to Use
- Continuous action spaces (robotics)
- When multimodal policy is important
- MuJoCo locomotion tasks
- Real-world robot arm manipulation

## Pitfalls
- Need good critic for effective guidance
- Guidance scale needs tuning
- Cannot use with discrete action spaces directly
- Diffusion model quality affects guidance quality

## References
- arXiv: 2605.30056v1
- Authors: Shutong Ding, Zejia Zhong, Zhongyi Wang et al.
- Published: 2026-05-28
- Webpage: https://dingsht.tech/cgpo-webpage