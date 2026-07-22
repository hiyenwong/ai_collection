---
name: h2sd-hybrid-hindsight-self-distillation
version: 1.0.0
description: Hybrid Hindsight Self-Distillation for Reinforcement Learning with Verifiable Rewards
trigger_words:
  - h2sd
  - hybrid hindsight self-distillation
  - rlvr
  - on-policy self-distillation
arxiv_id: 2607.18955
---

# H²SD: Hybrid Hindsight Self-Distillation

## Overview
H²SD (Hybrid Hindsight Self-Distillation) is a framework that improves reinforcement learning with verifiable rewards (RLVR) by providing better token-level credit assignment through a hybrid approach to self-distillation.

## Key Innovation
H²SD uses the teacher signal differently based on trajectory correctness:
- **For successful trajectories**: Uses teacher probabilities to modulate update magnitudes without changing direction
- **For failed trajectories**: Minimizes reverse KL divergence from student to teacher conditioned on reference hints

## Implementation Steps

1. **Setup Base Model**: Start with a language model suitable for your reasoning task
2. **Implement Trajectory Evaluation**: Create a mechanism to verify if a reasoning trajectory is correct
3. **Create Teacher Conditioning**:
   - For successful trajectories: Condition teacher on student response + rephrasing instruction
   - For failed trajectories: Condition teacher on reference hint + verified answer
4. **Apply Hybrid Distillation**:
   - Successful: Use teacher probabilities as magnitude weights for gradient updates
   - Failed: Minimize reverse KL divergence to teacher distribution
5. **Train with RLVR**: Combine with standard RLVR reward signals

## Benefits
- Consistently outperforms RLVR, OPSD, and RLSD baselines
- Maintains stable optimization during training
- Provides explicit correction direction for failed reasoning
- Preserves generation efficiency

## Use Cases
- Mathematical reasoning with LLMs
- Code generation with verification
- Complex multi-step reasoning tasks
- Any domain where verifiable rewards are available

## References
- Paper: [H²SD: Hybrid Hindsight Self-Distillation](https://arxiv.org/abs/2607.18955)
- Related work: RLVR, on-policy distillation, self-distillation, reinforcement learning