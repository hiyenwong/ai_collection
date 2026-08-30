# Breaking the Conventional Forward-Backward Tie in Neural Networks: Activation Functions

**arXiv ID:** 2509.07236
**Authors:** Luigi Troiano, Francesco Gissi, Vincenzo Benedetto, Genny Tortora
**Published:** 2025-09-08T21:30:00Z
**Abstract:**
Gradient-based neural network training traditionally enforces symmetry between forward and backward propagation, requiring activation functions to be differentiable (or sub-differentiable) and strictly monotonic in certain regions to prevent flat gradient areas. This symmetry, linking forward activations closely to backward gradients, significantly restricts the selection of activation functions, particularly excluding those with substantial flat or non-differentiable regions. In this paper, we challenge this assumption through mathematical analysis, demonstrating that precise gradient magnitudes derived from activation functions are largely redundant, provided the gradient direction is preserved. Empirical experiments conducted on foundational architectures - such as Multi-Layer Perceptrons (MLPs), Convolutional Neural Networks (CNNs), and Binary Neural Networks (BNNs) - confirm that relaxing forward-backward symmetry and substituting traditional gradients with simpler or stochastic alternatives does not impair learning and may even enhance training stability and efficiency. We explicitly demonstrate that neural networks with flat or non-differentiable activation functions, such as the Heaviside step function, can be effectively trained, thereby expanding design flexibility and computational efficiency. Further empirical validation with more complex architectures remains a valuable direction for future research.

## Skill Description

This skill is generated from the arXiv paper: Breaking the Conventional Forward-Backward Tie in Neural Networks: Activation Functions (2509.07236).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2509.07236](http://arxiv.org/abs/2509.07236v1)
