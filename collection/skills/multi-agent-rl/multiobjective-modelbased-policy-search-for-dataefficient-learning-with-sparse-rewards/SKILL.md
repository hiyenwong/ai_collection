# Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards

**arXiv ID:** 1806.09351
**Authors:** Rituraj Kaushik, Konstantinos Chatzilygeroudis, Jean-Baptiste Mouret
**Published:** 2018-06-25T09:46:47Z
**Abstract:**
The most data-efficient algorithms for reinforcement learning in robotics are model-based policy search algorithms, which alternate between learning a dynamical model of the robot and optimizing a policy to maximize the expected return given the model and its uncertainties. However, the current algorithms lack an effective exploration strategy to deal with sparse or misleading reward scenarios: if they do not experience any state with a positive reward during the initial random exploration, it is very unlikely to solve the problem. Here, we propose a novel model-based policy search algorithm, Multi-DEX, that leverages a learned dynamical model to efficiently explore the task space and solve tasks with sparse rewards in a few episodes. To achieve this, we frame the policy search problem as a multi-objective, model-based policy optimization problem with three objectives: (1) generate maximally novel state trajectories, (2) maximize the expected return and (3) keep the system in state-space regions for which the model is as accurate as possible. We then optimize these objectives using a Pareto-based multi-objective optimization algorithm. The experiments show that Multi-DEX is able to solve sparse reward scenarios (with a simulated robotic arm) in much lower interaction time than VIME, TRPO, GEP-PG, CMA-ES and Black-DROPS.

## Skill Description

This skill is generated from the arXiv paper: Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards (1806.09351).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1806.09351](http://arxiv.org/abs/1806.09351v3)
