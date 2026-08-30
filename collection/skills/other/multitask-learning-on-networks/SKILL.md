# Multi-Task Learning on Networks

**arXiv ID:** 2112.04891
**Authors:** Andrea Ponti
**Published:** 2021-12-07T09:13:10Z
**Abstract:**
The multi-task learning (MTL) paradigm can be traced back to an early paper of Caruana (1997) in which it was argued that data from multiple tasks can be used with the aim to obtain a better performance over learning each task independently. A solution of MTL with conflicting objectives requires modelling the trade-off among them which is generally beyond what a straight linear combination can achieve. A theoretically principled and computationally effective strategy is finding solutions which are not dominated by others as it is addressed in the Pareto analysis. Multi-objective optimization problems arising in the multi-task learning context have specific features and require adhoc methods. The analysis of these features and the proposal of a new computational approach represent the focus of this work. Multi-objective evolutionary algorithms (MOEAs) can easily include the concept of dominance and therefore the Pareto analysis. The major drawback of MOEAs is a low sample efficiency with respect to function evaluations. The key reason for this drawback is that most of the evolutionary approaches do not use models for approximating the objective function. Bayesian Optimization takes a radically different approach based on a surrogate model, such as a Gaussian Process. In this thesis the solutions in the Input Space are represented as probability distributions encapsulating the knowledge contained in the function evaluations. In this space of probability distributions, endowed with the metric given by the Wasserstein distance, a new algorithm MOEA/WST can be designed in which the model is not directly on the objective function but in an intermediate Information Space where the objects from the input space are mapped into histograms. Computational results show that the sample efficiency and the quality of the Pareto set provided by MOEA/WST are significantly better than in the standard MOEA.

## Skill Description

This skill is generated from the arXiv paper: Multi-Task Learning on Networks (2112.04891).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2112.04891](http://arxiv.org/abs/2112.04891v1)
