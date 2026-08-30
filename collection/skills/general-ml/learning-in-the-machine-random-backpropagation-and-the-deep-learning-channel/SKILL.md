# Learning in the Machine: Random Backpropagation and the Deep Learning Channel

**arXiv ID:** 1612.02734
**Authors:** Pierre Baldi, Peter Sadowski, Zhiqin Lu
**Published:** 2016-12-08T17:15:45Z
**Abstract:**
Random backpropagation (RBP) is a variant of the backpropagation algorithm for training neural networks, where the transpose of the forward matrices are replaced by fixed random matrices in the calculation of the weight updates. It is remarkable both because of its effectiveness, in spite of using random matrices to communicate error information, and because it completely removes the taxing requirement of maintaining symmetric weights in a physical neural system. To better understand random backpropagation, we first connect it to the notions of local learning and learning channels. Through this connection, we derive several alternatives to RBP, including skipped RBP (SRPB), adaptive RBP (ARBP), sparse RBP, and their combinations (e.g. ASRBP) and analyze their computational complexity. We then study their behavior through simulations using the MNIST and CIFAR-10 bechnmark datasets. These simulations show that most of these variants work robustly, almost as well as backpropagation, and that multiplication by the derivatives of the activation functions is important. As a follow-up, we study also the low-end of the number of bits required to communicate error information over the learning channel. We then provide partial intuitive explanations for some of the remarkable properties of RBP and its variations. Finally, we prove several mathematical results, including the convergence to fixed points of linear chains of arbitrary length, the convergence to fixed points of linear autoencoders with decorrelated data, the long-term existence of solutions for linear systems with a single hidden layer and convergence in special cases, and the convergence to fixed points of non-linear chains, when the derivative of the activation functions is included.

## Skill Description

This skill is generated from the arXiv paper: Learning in the Machine: Random Backpropagation and the Deep Learning Channel (1612.02734).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1612.02734](http://arxiv.org/abs/1612.02734v2)
