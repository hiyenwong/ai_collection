# Learning Synthetic Environments for Reinforcement Learning with Evolution Strategies

**arXiv ID:** 2101.09721
**Authors:** Fabio Ferreira, Thomas Nierhoff, Frank Hutter
**Published:** 2021-01-24T14:16:13Z
**Abstract:**
This work explores learning agent-agnostic synthetic environments (SEs) for Reinforcement Learning. SEs act as a proxy for target environments and allow agents to be trained more efficiently than when directly trained on the target environment. We formulate this as a bi-level optimization problem and represent an SE as a neural network. By using Natural Evolution Strategies and a population of SE parameter vectors, we train agents in the inner loop on evolving SEs while in the outer loop we use the performance on the target task as a score for meta-updating the SE population. We show empirically that our method is capable of learning SEs for two discrete-action-space tasks (CartPole-v0 and Acrobot-v1) that allow us to train agents more robustly and with up to 60% fewer steps. Not only do we show in experiments with 4000 evaluations that the SEs are robust against hyperparameter changes such as the learning rate, batch sizes and network sizes, we also show that SEs trained with DDQN agents transfer in limited ways to a discrete-action-space version of TD3 and very well to Dueling DDQN.

## Skill Description

This skill is generated from the arXiv paper: Learning Synthetic Environments for Reinforcement Learning with Evolution Strategies (2101.09721).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2101.09721](http://arxiv.org/abs/2101.09721v3)
