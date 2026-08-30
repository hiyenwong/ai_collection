# Meta Continual Learning

**arXiv ID:** 1806.06928
**Authors:** Risto Vuorio, Dong-Yeon Cho, Daejoong Kim, Jiwon Kim
**Published:** 2018-06-11T06:49:54Z
**Abstract:**
Using neural networks in practical settings would benefit from the ability of the networks to learn new tasks throughout their lifetimes without forgetting the previous tasks. This ability is limited in the current deep neural networks by a problem called catastrophic forgetting, where training on new tasks tends to severely degrade performance on previous tasks. One way to lessen the impact of the forgetting problem is to constrain parameters that are important to previous tasks to stay close to the optimal parameters. Recently, multiple competitive approaches for computing the importance of the parameters with respect to the previous tasks have been presented. In this paper, we propose a learning to optimize algorithm for mitigating catastrophic forgetting. Instead of trying to formulate a new constraint function ourselves, we propose to train another neural network to predict parameter update steps that respect the importance of parameters to the previous tasks. In the proposed meta-training scheme, the update predictor is trained to minimize loss on a combination of current and past tasks. We show experimentally that the proposed approach works in the continual learning setting.

## Skill Description

This skill is generated from the arXiv paper: Meta Continual Learning (1806.06928).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1806.06928](http://arxiv.org/abs/1806.06928v1)
