# TreeQN and ATreeC: Differentiable Tree-Structured Models for Deep Reinforcement Learning

**arXiv ID:** 1710.11417
**Authors:** Gregory Farquhar, Tim Rocktäschel, Maximilian Igl, Shimon Whiteson
**Published:** 2017-10-31T11:54:35Z
**Abstract:**
Combining deep model-free reinforcement learning with on-line planning is a promising approach to building on the successes of deep RL. On-line planning with look-ahead trees has proven successful in environments where transition models are known a priori. However, in complex environments where transition models need to be learned from data, the deficiencies of learned models have limited their utility for planning. To address these challenges, we propose TreeQN, a differentiable, recursive, tree-structured model that serves as a drop-in replacement for any value function network in deep RL with discrete actions. TreeQN dynamically constructs a tree by recursively applying a transition model in a learned abstract state space and then aggregating predicted rewards and state-values using a tree backup to estimate Q-values. We also propose ATreeC, an actor-critic variant that augments TreeQN with a softmax layer to form a stochastic policy network. Both approaches are trained end-to-end, such that the learned model is optimised for its actual use in the tree. We show that TreeQN and ATreeC outperform n-step DQN and A2C on a box-pushing task, as well as n-step DQN and value prediction networks (Oh et al. 2017) on multiple Atari games. Furthermore, we present ablation studies that demonstrate the effect of different auxiliary losses on learning transition models.

## Skill Description

This skill is generated from the arXiv paper: TreeQN and ATreeC: Differentiable Tree-Structured Models for Deep Reinforcement Learning (1710.11417).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1710.11417](http://arxiv.org/abs/1710.11417v2)
