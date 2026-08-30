# Improving Expert Specialization in Mixture of Experts

**arXiv ID:** 2302.14703
**Authors:** Yamuna Krishnamurthy, Chris Watkins, Thomas Gaertner
**Published:** 2023-02-28T16:16:45Z
**Abstract:**
Mixture of experts (MoE), introduced over 20 years ago, is the simplest gated modular neural network architecture. There is renewed interest in MoE because the conditional computation allows only parts of the network to be used during each inference, as was recently demonstrated in large scale natural language processing models. MoE is also of potential interest for continual learning, as experts may be reused for new tasks, and new experts introduced. The gate in the MoE architecture learns task decompositions and individual experts learn simpler functions appropriate to the gate's decomposition. In this paper: (1) we show that the original MoE architecture and its training method do not guarantee intuitive task decompositions and good expert utilization, indeed they can fail spectacularly even for simple data such as MNIST and FashionMNIST; (2) we introduce a novel gating architecture, similar to attention, that improves performance and results in a lower entropy task decomposition; and (3) we introduce a novel data-driven regularization that improves expert specialization. We empirically validate our methods on MNIST, FashionMNIST and CIFAR-100 datasets.

## Skill Description

This skill is generated from the arXiv paper: Improving Expert Specialization in Mixture of Experts (2302.14703).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2302.14703](http://arxiv.org/abs/2302.14703v1)
