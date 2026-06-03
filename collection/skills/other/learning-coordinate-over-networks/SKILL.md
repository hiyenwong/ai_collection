---
name: learning-coordinate-over-networks
description: "Network coordination games are widely used to model collaboration among interconnected agents, with applications across diverse domains including economics, robotics, and cyber-sec... Activation: distributed"
---

# Learning to Coordinate over Networks with Bounded Rationality

## Overview

Network coordination games are widely used to model collaboration among interconnected agents, with applications across diverse domains including economics, robotics, and cyber-security. We consider networks of bounded-rational agents who interact through binary stag hunt games, a canonical game theoretic model for distributed collaborative tasks. Herein, the agents update their actions using logit response functions, yielding the Log-Linear Learning (LLL) algorithm. While convergence of LLL to a risk-dominant Nash equilibrium requires unbounded rationality, we consider regimes in which rationality is strictly bounded. We first show that the stationary probability of states corresponding to perfect coordination is monotone increasing in the rationality parameter $\beta$. For $K$-regular networks, we prove that the stationary probability of a perfectly coordinated action profile is monotone in the connectivity degree $K$, and we provide an upper bound on the minimum rationality required to achieve a desired level of coordination. For irregular networks, we show that the stationary probability of perfectly coordinated action profiles increases with the number of edges in the graph. We show that, for a large class of networks, the partition function of the Gibbs measure is well approximated by the moment generating function of Gaussian random variable. This approximation allows us to optimize degree distributions and establishes that the optimal network - i.e., the one that maximizes the stationary probability of coordinated action profiles - is $K$-regular. Consequently, our results indicate that networks of uniformly bounded-rational agents achieve the most reliable coordination when connectivity is evenly distributed among agents.

## Source Paper

- **Title**: Learning to Coordinate over Networks with Bounded Rationality
- **Authors**: Zhewei Wang, Emrah Akyol, Marcos M. Vasconcelos
- **arXiv**: 2604.07751v1
- **Published**: 2026-04-09
- **Categories**: eess.SY, cs.MA
- **Primary Category**: eess.SY

## Core Concepts

This paper presents research on systems engineering with focus areas including:
- Novel methodological frameworks
- Theoretical foundations and analysis
- Practical implementation strategies
- Experimental validation

## Technical Contributions

1. **Novel Approach**: Advanced methodology for complex systems problems
2. **Theoretical Foundation**: Rigorous mathematical analysis
3. **Practical Implementation**: Real-world application and validation

## Applications

- Systems engineering research and development
- Distributed systems design and optimization
- Control system implementation
- Multi-agent coordination

## Implementation Guidelines

1. Review the source paper for detailed methodology
2. Understand the theoretical framework
3. Implement the proposed approach
4. Validate with appropriate experiments

## References

- Zhewei Wang et al. (2026). "Learning to Coordinate over Networks with Bounded Rationality." arXiv:2604.07751v1.
- arXiv URL: https://arxiv.org/abs/2604.07751v1

## Activation Keywords

distributed
