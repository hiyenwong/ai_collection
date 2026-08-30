# Proximal Policy Optimization with Evolutionary Mutations

**arXiv ID:** 2601.14705
**Authors:** Casimir Czworkowski, Stephen Hornish, Alhassan S. Yasin
**Published:** 2026-01-21T06:34:53Z
**Abstract:**
Proximal Policy Optimization (PPO) is a widely used reinforcement learning algorithm known for its stability and sample efficiency, but it often suffers from premature convergence due to limited exploration. In this paper, we propose POEM (Proximal Policy Optimization with Evolutionary Mutations), a novel modification to PPO that introduces an adaptive exploration mechanism inspired by evolutionary algorithms. POEM enhances policy diversity by monitoring the Kullback-Leibler (KL) divergence between the current policy and a moving average of previous policies. When policy changes become minimal, indicating stagnation, POEM triggers an adaptive mutation of policy parameters to promote exploration. We evaluate POEM on four OpenAI Gym environments: CarRacing, MountainCar, BipedalWalker, and LunarLander. Through extensive fine-tuning using Bayesian optimization techniques and statistical testing using Welch's t-test, we find that POEM significantly outperforms PPO on three of the four tasks (BipedalWalker: t=-2.0642, p=0.0495; CarRacing: t=-6.3987, p=0.0002; MountainCar: t=-6.2431, p<0.0001), while performance on LunarLander is not statistically significant (t=-1.8707, p=0.0778). Our results highlight the potential of integrating evolutionary principles into policy gradient methods to overcome exploration-exploitation tradeoffs.

## Skill Description

This skill is generated from the arXiv paper: Proximal Policy Optimization with Evolutionary Mutations (2601.14705).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2601.14705](http://arxiv.org/abs/2601.14705v1)
