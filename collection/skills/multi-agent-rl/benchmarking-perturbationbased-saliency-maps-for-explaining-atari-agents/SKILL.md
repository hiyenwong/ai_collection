# Benchmarking Perturbation-based Saliency Maps for Explaining Atari Agents

**arXiv ID:** 2101.07312
**Authors:** Tobias Huber, Benedikt Limmer, Elisabeth André
**Published:** 2021-01-18T19:57:52Z
**Abstract:**
One of the most prominent methods for explaining the behavior of Deep Reinforcement Learning (DRL) agents is the generation of saliency maps that show how much each pixel attributed to the agents' decision. However, there is no work that computationally evaluates and compares the fidelity of different saliency map approaches specifically for DRL agents. It is particularly challenging to computationally evaluate saliency maps for DRL agents since their decisions are part of an overarching policy. For instance, the output neurons of value-based DRL algorithms encode both the value of the current state as well as the value of doing each action in this state. This ambiguity should be considered when evaluating saliency maps for such agents. In this paper, we compare five popular perturbation-based approaches to create saliency maps for DRL agents trained on four different Atari 2600 games. The approaches are compared using two computational metrics: dependence on the learned parameters of the agent (sanity checks) and fidelity to the agent's reasoning (input degradation). During the sanity checks, we encounter issues with one approach and propose a solution to fix these issues. For fidelity, we identify two main factors that influence which saliency approach should be chosen in which situation.

## Skill Description

This skill is generated from the arXiv paper: Benchmarking Perturbation-based Saliency Maps for Explaining Atari Agents (2101.07312).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2101.07312](http://arxiv.org/abs/2101.07312v3)
