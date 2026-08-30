# Maximum Mutation Reinforcement Learning for Scalable Control

**arXiv ID:** 2007.13690
**Authors:** Karush Suri, Xiao Qi Shi, Konstantinos N. Plataniotis, Yuri A. Lawryshyn
**Published:** 2020-07-24T16:29:19Z
**Abstract:**
Advances in Reinforcement Learning (RL) have demonstrated data efficiency and optimal control over large state spaces at the cost of scalable performance. Genetic methods, on the other hand, provide scalability but depict hyperparameter sensitivity towards evolutionary operations. However, a combination of the two methods has recently demonstrated success in scaling RL agents to high-dimensional action spaces. Parallel to recent developments, we present the Evolution-based Soft Actor-Critic (ESAC), a scalable RL algorithm. We abstract exploration from exploitation by combining Evolution Strategies (ES) with Soft Actor-Critic (SAC). Through this lens, we enable dominant skill transfer between offsprings by making use of soft winner selections and genetic crossovers in hindsight and simultaneously improve hyperparameter sensitivity in evolutions using the novel Automatic Mutation Tuning (AMT). AMT gradually replaces the entropy framework of SAC allowing the population to succeed at the task while acting as randomly as possible, without making use of backpropagation updates. In a study of challenging locomotion tasks consisting of high-dimensional action spaces and sparse rewards, ESAC demonstrates improved performance and sample efficiency in comparison to the Maximum Entropy framework. Additionally, ESAC presents efficacious use of hardware resources and algorithm overhead. A complete implementation of ESAC can be found at karush17.github.io/esac-web/.

## Skill Description

This skill is generated from the arXiv paper: Maximum Mutation Reinforcement Learning for Scalable Control (2007.13690).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2007.13690](http://arxiv.org/abs/2007.13690v7)
