# PredProp: Bidirectional Stochastic Optimization with Precision Weighted Predictive Coding

**arXiv ID:** 2111.08792
**Authors:** André Ofner, Sebastian Stober
**Published:** 2021-11-16T21:43:15Z
**Abstract:**
We present PredProp, a method for optimization of weights and states in predictive coding networks (PCNs) based on the precision of propagated errors and neural activity. PredProp jointly addresses inference and learning via stochastic gradient descent and adaptively weights parameter updates by approximate curvature. Due to the relation between propagated error covariance and the Fisher information matrix, PredProp implements approximate Natural Gradient Descent. We demonstrate PredProp's effectiveness in the context of dense decoder networks and simple image benchmark datasets. We found that PredProp performs favorably over Adam, a widely used adaptive learning rate optimizer in the tested configurations. Furthermore, available optimization methods for weight parameters benefit from using PredProp's error precision during inference. Since hierarchical predictive coding layers are optimised individually using local errors, the required precisions factorize over hierarchical layers. Extending beyond classical PCNs with a single set of decoder layers per hierarchical layer, we also generalize PredProp to deep neural networks in each PCN layer by additionally factorizing over the weights in each PCN layer.

## Skill Description

This skill is generated from the arXiv paper: PredProp: Bidirectional Stochastic Optimization with Precision Weighted Predictive Coding (2111.08792).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2111.08792](http://arxiv.org/abs/2111.08792v2)
