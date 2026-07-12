---
name: multi-modal-multi-environment-machine-teaching-robust-reward
description: "Hierarchical machine teaching algorithm for robust reward learning across multiple MDPs. Demonstrates comparisons impose stronger constraints than demonstrations in unlimited-data regime. Greedily selects informative environments then queries low-cost feedback. Activation: machine teaching, reward learning, inverse reinforcement learning, multi-environment, robust reward, feedback modalities."
metadata:
  arxiv_id: "2607.08647"
  published: "2026-07-09"
  authors: "Ali Larian, Qian Lin, Chang Zong Wu, Daniel S. Brown"
  tags: [machine-teaching, reward-learning, inverse-reinforcement-learning, multi-environment, robust-reward]
---

# Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning

## Overview

As autonomous agents are increasingly deployed across diverse operational contexts, aligning their behavior with human intent demands reward functions that remain robust to environmental changes. This paper introduces a hierarchical machine teaching algorithm for reward learning that operates across multiple MDPs, addressing the limitation that demonstrations in one MDP entangle reward information with environment-specific structure.

## Key Innovations

### Theoretical Analysis of Feedback Modalities
- Shows that in the unlimited-data regime, comparisons impose strictly stronger global constraints than other modalities
- Different feedback modalities constrain rewards differently
- Demonstrations in one MDP entangle reward with environment structure, causing generalization failure

### Hierarchical Machine Teaching
- First selects informative environments that expose complementary reward constraints
- Then strategically queries low-cost feedback within those environments
- Greedy environment selection based on complementary information

### Multi-Environment Robustness
- Rewards learned across multiple environments generalize better than single-environment rewards
- Substantially lower regret on held-out environments under identical feedback budgets
- Demonstrates importance of multi-environment teaching for dynamics-robust reward functions

## Methodology

1. **Environment Selection**: Greedily select MDPs exposing complementary reward constraints
2. **Feedback Querying**: Strategically query low-cost feedback within selected environments
3. **Reward Learning**: Learn reward functions that generalize across environments
4. **Evaluation**: Compare against uniform teaching baselines on held-out environments

## Implications

- Multi-environment teaching is essential for robust reward learning
- Feedback modality choice significantly impacts reward constraint quality
- Hierarchical approach enables efficient use of feedback budgets
- Applicable to autonomous agent deployment across diverse contexts

## Pitfalls

- Requires access to multiple environments during training
- Greedy environment selection may miss globally optimal combinations
- Low-cost feedback may not always be informative
- Theoretical results assume unlimited-data regime which may not hold in practice

## Activation Keywords

machine teaching, reward learning, inverse reinforcement learning, multi-environment, robust reward functions, feedback modalities, hierarchical teaching, MDP generalization

## Paper Reference

arXiv:2607.08647 - "Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning" (Jul 2026)
