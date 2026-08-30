# Option Discovery in Hierarchical Reinforcement Learning using Spatio-Temporal Clustering

**arXiv ID:** 1605.05359
**Authors:** Aravind Srinivas, Ramnandan Krishnamurthy, Peeyush Kumar, Balaraman Ravindran
**Published:** 2016-05-17T20:44:19Z
**Abstract:**
This paper introduces an automated skill acquisition framework in reinforcement learning which involves identifying a hierarchical description of the given task in terms of abstract states and extended actions between abstract states. Identifying such structures present in the task provides ways to simplify and speed up reinforcement learning algorithms. These structures also help to generalize such algorithms over multiple tasks without relearning policies from scratch. We use ideas from dynamical systems to find metastable regions in the state space and associate them with abstract states. The spectral clustering algorithm PCCA+ is used to identify suitable abstractions aligned to the underlying structure. Skills are defined in terms of the sequence of actions that lead to transitions between such abstract states. The connectivity information from PCCA+ is used to generate these skills or options. These skills are independent of the learning task and can be efficiently reused across a variety of tasks defined over the same model. This approach works well even without the exact model of the environment by using sample trajectories to construct an approximate estimate. We also present our approach to scaling the skill acquisition framework to complex tasks with large state spaces for which we perform state aggregation using the representation learned from an action conditional video prediction network and use the skill acquisition framework on the aggregated state space.

## Skill Description

This skill is generated from the arXiv paper: Option Discovery in Hierarchical Reinforcement Learning using Spatio-Temporal Clustering (1605.05359).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1605.05359](http://arxiv.org/abs/1605.05359v3)
