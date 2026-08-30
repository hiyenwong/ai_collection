# CosineGate: Semantic Dynamic Routing via Cosine Incompatibility in Residual Networks

**arXiv ID:** 2512.22206
**Authors:** Yogeswar Reddy Thota
**Published:** 2025-12-21T18:26:18Z
**Abstract:**
Modern deep residual networks perform substantial redundant computation by evaluating all residual blocks for every input, even when identity mappings suffice. We introduce CosineGate, an end-to-end differentiable architecture for dynamic routing in residual networks that uses cosine incompatibility between identity and residual feature representations as a self-supervised skip signal. CosineGate measures semantic redundancy through the Cosine Incompatibility Ratio (CIR), defined as 1 - cos(x, F(x)), and uses Gumbel-Softmax relaxation to enable per-sample, per-block gating during training. A progressive FLOPs regularization term controls average compute usage without destabilizing optimization. On CIFAR-10, CosineGate spans the accuracy-efficiency Pareto frontier: an aggressive configuration achieves 89.9 percent accuracy with 24.1 percent FLOPs savings, a balanced configuration achieves 91.3 percent accuracy with 28.5 percent savings at epoch 160, and a conservative configuration reaches a peak of 93.2 percent accuracy with minimal compute reduction. These results match or exceed ResNet-20 (91.3 percent) while reducing computation, without auxiliary supervision, distillation, or task-specific heuristics. Our results demonstrate that simple geometric measures of feature incompatibility provide a principled and effective signal for dynamic residual routing.

## Skill Description

This skill is generated from the arXiv paper: CosineGate: Semantic Dynamic Routing via Cosine Incompatibility in Residual Networks (2512.22206).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2512.22206](http://arxiv.org/abs/2512.22206v1)
