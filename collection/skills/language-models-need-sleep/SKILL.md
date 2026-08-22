---
name: language-models-need-sleep
description: >-
  Sleep paradigm for LLMs that enables continual learning through memory consolidation and dreaming phases.
  Use when: (1) implementing continual learning for LLMs; (2) designing memory consolidation mechanisms;
  (3) creating autonomous self-improvement systems; (4) addressing catastrophic forgetting in sequential tasks;
  (5) developing RL-based curriculum generation for synthetic data.
  Trigger words: sleep paradigm, memory consolidation, dreaming process, knowledge seeding, LLM sleep.
---
# Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories

This skill implements the "Sleep" paradigm from the paper [arXiv:2606.03979](https://arxiv.org/abs/2606.03979) by Behrouz et al. (2026), updated with v2 details from July 10, 2026.
This methodology introduces a "Sleep" paradigm for Large Language Models (LLMs) that enables continual learning by distilling short-term fragile memories into stable long-term knowledge through replay, and recursively improving themselves with a "Dreaming" process.

## Core Components

### 1. Memory Consolidation (Knowledge Seeding)
- **Upward distillation process**: Memories of a smaller-self are distilled into a larger network to provide more capacity while preserving knowledge
- **Generalized Distillation**: Combines on-policy distillation with Reinforcement Learning (RL)-based imitation learning

### 2. Dreaming (Self-Improvement Phase)
- **RL-based curriculum generation**: Model uses RL to generate synthetic data to rehearse new knowledge and refine existing capabilities without human supervision
- **Autonomous self-improvement**: No external supervision required during the dreaming phase

## Applications
- Long-horizon tasks
- Continual learning scenarios
- Knowledge incorporation
- Few-shot generalization tasks

## Implementation Guidelines
1. **Two-stage sleep process**: Implement both memory consolidation and dreaming phases sequentially
2. **Knowledge seeding**: Use generalized distillation combining on-policy distillation with RL-based imitation learning
3. **Dreaming curriculum**: Generate synthetic data through RL that challenges the model's current capabilities
4. **Evaluation metrics**: Test on long-horizon, continual learning, knowledge incorporation, and few-shot generalization tasks

## Key Insights
- Existing LLMs lack the ability to continually learn and effectively transfer temporal in-context knowledge to long-term parameters
- The sleep paradigm addresses this gap by providing mechanisms for both consolidation and self-improvement
- Experiments demonstrate the importance of both stages working together for optimal performance

## References
- Original paper: [arXiv:2606.03979](https://arxiv.org/abs/2606.03979)
- Published: June 2, 2026
- License: CC BY 4.0