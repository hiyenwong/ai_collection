---
name: vector-policy-optimization
description: "Vector Policy Optimization (VPO) methodology for training LLMs to maintain response diversity during inference-time search. Use when: (1) Training models for test-time compute scaling, (2) Improving AlphaEvolve/AlphaCode-style search procedures, (3) Addressing low-entropy response distributions in RL fine-tuning, (4) Designing multi-objective reward training pipelines, (5) Balancing per-reward performance with cross-reward diversity in agentic systems."
arxiv_id: "2605.22817"
date: "2026-05-21"
authors: "Unknown"
tags: ["information-science", "llm-training", "reinforcement-learning", "diversity", "test-time-compute"]
---

# Vector Policy Optimization (VPO)

## Description

Vector Policy Optimization (VPO) trains language models to maintain response diversity, enabling better performance in inference-time search procedures (AlphaEvolve, AlphaCode) that select rollouts with varied task-specific reward functions. Standard LLM post-training optimizes a pre-specified scalar reward, leading to low-entropy response distributions that struggle at inference-time search.

## Core Insight

**Problem**: Scalar reward optimization → low-entropy responses → poor inference-time search diversity.

**Solution**: Train with a vector of rewards simultaneously, optimizing both per-reward performance AND cross-reward diversity.

## Mathematical Framework

VPO optimizes:

```
max_θ Σ_k E_{x~D, y~π_θ(·|x)}[r_k(x,y)] + λ · Diversity(π_θ)
```

Where:
- `r_k` = k different reward functions
- `Diversity` measures response variety across reward dimensions
- `λ` controls diversity-performance tradeoff

## Key Mechanism

VPO derives from the REINFORCE gradient with a diversity bonus term:

1. **Vector Return**: Compute returns for each reward dimension separately
2. **Diversity Bonus**: Add bonus for responses that differ across reward dimensions
3. **Gradient update**: Standard PPO/GRPO-style update with vector-valued advantages

## Usage Patterns

### Pattern 1: Multi-Objective RL Fine-Tuning

When fine-tuning an LLM where different use cases require different quality metrics (correctness, helpfulness, creativity, safety):

1. Define K reward functions for each quality dimension
2. Use VPO to train on the joint reward vector
3. At inference, select outputs via search over the diverse response set

### Pattern 2: Test-Time Compute Scaling

For systems using inference-time search (best-of-N, tree search, evolutionary search):

1. Pre-train with VPO to build diverse response distributions
2. At test time, generate N diverse candidates
3. Score candidates with task-specific reward
4. Select best candidate — diversity ensures coverage of solution space

### Pattern 3: Agent Reasoning Diversity

For agentic systems where different reasoning paths lead to different solutions:

1. Define reward functions for different reasoning styles (step-by-step, analogy-based, verification-first)
2. Train with VPO to maintain diversity across reasoning strategies
3. At inference, deploy diverse reasoning paths in parallel
4. Aggregate or select best result

## Implementation Guidance

### GRPO Integration

VPO integrates with Group Relative Policy Optimization (GRPO):

```python
# Standard GRPO: scalar reward
advantages = (rewards - mean(rewards)) / std(rewards)

# VPO: vector rewards with diversity
vector_advantages = compute_vector_advantages(reward_matrix)
diversity_bonus = compute_diversity_bonus(responses)
final_advantages = vector_advantages + lambda * diversity_bonus
```

### Key Hyperparameters

- `K` (number of reward dimensions): Start with 3-5
- `λ` (diversity weight): Tune based on search procedure needs
- `N` (group size for GRPO): Same as standard GRPO
- Temperature: Keep higher than scalar-trained models to preserve diversity

## When to Use

- **Use VPO when**: Training models for inference-time search, multi-objective optimization, or diverse reasoning
- **Avoid VPO when**: Single well-defined reward function suffices, or deployment doesn't use test-time search
- **Best with**: AlphaEvolve-style systems, code generation, mathematical reasoning, creative tasks

## Error Handling

### Low Diversity Despite VPO
- Increase λ (diversity weight)
- Check reward functions aren't too correlated
- Verify temperature isn't being annealed too aggressively

### Performance Degradation on Single Metric
- Expected tradeoff: VPO sacrifices peak single-metric performance for diversity
- If unacceptable: reduce λ or add per-metric floor constraints

## Resources

- **arXiv**: [2605.22817](https://arxiv.org/abs/2605.22817)
- **Related**: GRPO training, inference-time compute scaling, AlphaEvolve
