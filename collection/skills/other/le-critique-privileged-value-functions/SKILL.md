---
name: le-critique-privileged-value-functions
description: "Privileged Value Functions for LLM reinforcement learning."
---

# Le Critique: Privileged Value Functions for LLM Reinforcement Learning

## Overview
Le Critique proposes two complementary strategies to improve the performance of value function reinforcement learning for Large Language Models (LLMs): Privileged Value Functions (PVF) and TETHER baseline. These address the infrastructure engineering challenges that have made value functions difficult to justify in RL pipelines compared to critic-free methods like GRPO.

## Key Strategies

### 1. Privileged Value Functions (PVF)
- Provides an elegant mechanism to inject additional task-relevant token-level signal
- Does not bias the policy objective
- Addresses the practical limitations of standard value functions

### 2. TETHER Baseline
- Adaptively interpolates between group-relative and value baselines
- Depends on the value function accuracy
- Provides robust performance across different scenarios

## Performance Benefits
- Both strategies consistently improve over the standard value function baseline
- Competitive with or outperform mean-baseline GRPO across several reasoning tasks
- Addresses both gradient variance reduction and throughput issues

## Implementation Guidelines

### When to Use
- LLM reinforcement learning tasks requiring token-level credit assignment
- Need to reduce gradient variance without large group sampling
- Want to avoid straggler rollouts that block training throughput
- Seeking alternatives to critic-free methods like GRPO

### Integration Steps
1. Implement Privileged Value Functions with task-relevant signals
2. Add TETHER adaptive baseline interpolation
3. Monitor value function accuracy for optimal baseline selection
4. Compare against mean-baseline GRPO for performance validation

## Applications
- Reasoning task optimization
- Agent policy improvement
- Token-level advantage estimation
- Efficient LLM reinforcement learning pipelines

## References
- arXiv:2608.16739
- GRPO comparison results
- Reasoning task benchmarks