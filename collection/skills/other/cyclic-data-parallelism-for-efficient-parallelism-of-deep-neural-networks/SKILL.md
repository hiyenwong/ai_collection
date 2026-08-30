# Cyclic Data Parallelism for Efficient Parallelism of Deep Neural Networks

**arXiv ID:** 2403.08837
**Authors:** Louis Fournier, Edouard Oyallon
**Published:** 2024-03-13T08:39:21Z
**Abstract:**
Training large deep learning models requires parallelization techniques to scale. In existing methods such as Data Parallelism or ZeRO-DP, micro-batches of data are processed in parallel, which creates two drawbacks: the total memory required to store the model's activations peaks at the end of the forward pass, and gradients must be simultaneously averaged at the end of the backpropagation step. We propose Cyclic Data Parallelism, a novel paradigm shifting the execution of the micro-batches from simultaneous to sequential, with a uniform delay. At the cost of a slight gradient delay, the total memory taken by activations is constant, and the gradient communications are balanced during the training step. With Model Parallelism, our technique reduces the number of GPUs needed, by sharing GPUs across micro-batches. Within the ZeRO-DP framework, our technique allows communication of the model states with point-to-point operations rather than a collective broadcast operation. We illustrate the strength of our approach on the CIFAR-10 and ImageNet datasets.

## Skill Description

This skill is generated from the arXiv paper: Cyclic Data Parallelism for Efficient Parallelism of Deep Neural Networks (2403.08837).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2403.08837](http://arxiv.org/abs/2403.08837v1)
