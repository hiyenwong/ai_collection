---
name: selective-timestep-weighting-and-advantage-based-replay-for-sample-efficient
description: 'Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly fe. Based on arXiv:2607.07693.'
---

# Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF

**arXiv**: 2607.07693 | **Authors**: Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay | **Utility**: 0.85

## Overview

Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that substantially improve the feedback efficiency of diffusion RLHF while preserving generalization to unseen prompts. Our key observation is that reward information in diffusion trajectories is unevenly distributed: not all denoising timesteps or trajectories contribute equally to learning from a reward signal. By emphasizing informative timesteps and trajectories during optimization, we obtain more effective gradient updates. First, we introduce a per-timestep weighting scheme that reweights denoising steps during policy optimization. We theoretically connect this weighting to the optimal convergence properties of proximal policy optimization (PPO) and approximate the resulting weighting trend empirically. Second, we introduce a replay mechanism that prioritizes informative trajectories, enabling the model to reuse past samples instead of repeatedly querying new rewards. Together, these strategies significantly improve the feedback efficiency of diffusion RLHF. Under identical hyperparameter settings, our approach achieves up to a 6$\times$ improvement in sample efficiency compared to widely used diffusion RLHF baselines.

## Key Contributions

1. Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences.
2. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations.
3. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck.
4. In this paper, we propose two complementary strategies that substantially improve the feedback efficiency of diffusion RLHF while preserving generalization to unseen prompts.

## Implementation Notes

- **Keywords**: reinforcement-learning, diffusion-model, rlhf
- **Categories**: cs.LG, cs.AI, cs.CV
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: reinforcement-learning, diffusion-model, rlhf.
