---
name: rft-visual-continual-learning
description: "Using Reinforcement Fine-Tuning (RFT/GRPO) to overcome catastrophic forgetting in visual continual learning. Activation triggers: reinforcement fine-tuning continual learning, GRPO visual CL, RL visual continual learning, catastrophic forgetting visual, class-incremental visual learning"
---

# Overcoming Catastrophic Forgetting in Visual Continual Learning with Reinforcement Fine-Tuning

> Demonstrates that Reinforcement Fine-Tuning (RFT), specifically GRPO, is inherently more resilient to catastrophic forgetting than Supervised Fine-Tuning (SFT) in challenging visual continual learning settings like class-incremental learning.

## Metadata
- **Source**: arXiv:2605.09640
- **Authors**: Meng Lou, Hanzhong Guo, Linwei Chen, Yizhou Yu
- **Published**: 2026-05-10

## Core Problem

**Visual Continual Learning**: Models must learn to recognize new visual classes incrementally without forgetting previously learned classes. Class-incremental learning is particularly challenging as the model must distinguish between all seen classes, old and new.

**Catastrophic Forgetting**: Standard fine-tuning on new class data causes significant performance degradation on old classes.

## Key Finding

**RFT > SFT for Continual Learning**: Reinforcement Fine-Tuning (RFT), exemplified by GRPO, shows significantly better retention of old task performance compared to Supervised Fine-Tuning (SFT).

### Why RFT Forgets Less

1. **Reward-based learning**: RFT optimizes for task completion rewards rather than exact label matching, learning more generalizable representations.

2. **Implicit regularization**: The RL objective naturally regularizes updates, preventing overfitting to new class features.

3. **Policy gradient stability**: Unlike supervised loss gradients which can be sharp and task-specific, RL gradients tend to be smoother and more stable.

4. **Exploration bonus**: RL's inherent exploration encourages finding solutions that work across tasks rather than memorizing new ones.

## Methodology

### GRPO for Visual CL
- Uses Group Relative Policy Optimization for visual classification tasks
- Compares performance within groups of samples to compute advantage estimates
- No value function needed, reducing training complexity

### Training Setup
- Class-incremental protocol: sequentially introduce new classes
- No replay buffer (or minimal buffer)
- Evaluate on all classes seen so far after each increment

### Comparison Baselines
- Standard SFT with cross-entropy loss
- EWC (Elastic Weight Consolidation)
- Replay-based methods
- Other CL baselines

## Results

**Key Finding**: RFT (GRPO) maintains higher accuracy on old classes while achieving comparable performance on new classes, resulting in better overall continual learning performance.

## Implementation Guide

### Prerequisites
- Vision model (ViT, ResNet, etc.)
- GRPO implementation (TRL or similar)
- Class-incremental dataset setup

### Step-by-Step
1. **Define reward function**: Classification accuracy or confidence-based rewards
2. **Group formation**: Group samples for relative policy optimization
3. **Policy optimization**: Apply GRPO updates without explicit value function
4. **Sequential training**: Incrementally add new classes and continue training

### Code Sketch
```python
# Reward for classification
def compute_rewards(predictions, targets):
    # Positive reward for correct classification
    # Scaled by confidence
    correct = (predictions == targets).float()
    return correct * confidence_scale

# GRPO-style update
advantages = (rewards - rewards.mean()) / (rewards.std() + 1e-8)
policy_loss = -(advantages * log_prob_ratio).mean()
```

## Applications
- Visual class-incremental learning without replay
- Medical image classification with new disease classes
- Autonomous vehicle perception with new object types
- Industrial defect detection with new defect categories

## Pitfalls
- **Reward design**: Poor reward functions can lead to suboptimal policies
- **Sample efficiency**: RFT typically requires more samples than SFT
- **Training stability**: RL training can be less stable than supervised training
- **Scalability**: May not scale as well as SFT for very large class sets

## Related Skills
- zeroth-order-adaptation-forgetting-theory
- catastrophic-forgetting-mitigation
- reinforcement-learning-fine-tuning
