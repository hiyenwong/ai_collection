# Proposal and Verification of Novel Machine Learning on Classification Problems

**arXiv ID:** 2207.04884
**Authors:** Chikako Dozono, Mina Aragaki, Hana Hebishima, Shin-ichi Inage
**Published:** 2022-06-23T06:47:32Z
**Abstract:**
This paper aims at proposing a new machine learning for classification problems. The classification problem has a wide range of applications, and there are many approaches such as decision trees, neural networks, and Bayesian nets. In this paper, we focus on the action of neurons in the brain, especially the EPSP/IPSP cancellation between excitatory and inhibitory synapses, and propose a Machine Learning that does not belong to any conventional method. The feature is to consider one neuron and give it a multivariable Xj (j = 1, 2,.) and its function value F(Xj) as data to the input layer. The multivariable input layer and processing neuron are linked by two lines to each variable node. One line is called an EPSP edge, and the other is called an IPSP edge, and a parameter Δj common to each edge is introduced. The processing neuron is divided back and forth into two parts, and at the front side, a pulse having a width 2Δj and a height 1 is defined around an input X . The latter half of the processing neuron defines a pulse having a width 2Δj centered on the input Xj and a height F(Xj) based on a value obtained from the input layer of F(Xj). This information is defined as belonging to group i. In other words, the group i has a width of 2Δj centered on the input Xj, is defined in a region of height F(Xj), and all outputs of xi within the variable range are F(Xi). This group is learned and stored by a few minutes of the Teaching signals, and the output of the TEST signals is predicted by which group the TEST signals belongs to. The parameter Δj is optimized so that the accuracy of the prediction is maximized. The proposed method was applied to the flower species classification problem of Iris, the rank classification problem of used cars, and the ring classification problem of abalone, and the calculation was compared with the neural networks.

## Skill Description

This skill is generated from the arXiv paper: Proposal and Verification of Novel Machine Learning on Classification Problems (2207.04884).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2207.04884](http://arxiv.org/abs/2207.04884v1)
