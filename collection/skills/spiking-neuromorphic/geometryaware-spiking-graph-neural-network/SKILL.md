# Geometry-Aware Spiking Graph Neural Network

**arXiv ID:** 2508.06793
**Authors:** Bowen Zhang, Genan Dai, Hu Huang, Long Lan
**Published:** 2025-08-09T02:52:38Z
**Abstract:**
Graph Neural Networks (GNNs) have demonstrated impressive capabilities in modeling graph-structured data, while Spiking Neural Networks (SNNs) offer high energy efficiency through sparse, event-driven computation. However, existing spiking GNNs predominantly operate in Euclidean space and rely on fixed geometric assumptions, limiting their capacity to model complex graph structures such as hierarchies and cycles. To overcome these limitations, we propose \method{}, a novel Geometry-Aware Spiking Graph Neural Network that unifies spike-based neural dynamics with adaptive representation learning on Riemannian manifolds. \method{} features three key components: a Riemannian Embedding Layer that projects node features into a pool of constant-curvature manifolds, capturing non-Euclidean structures; a Manifold Spiking Layer that models membrane potential evolution and spiking behavior in curved spaces via geometry-consistent neighbor aggregation and curvature-based attention; and a Manifold Learning Objective that enables instance-wise geometry adaptation through jointly optimized classification and link prediction losses defined over geodesic distances. All modules are trained using Riemannian SGD, eliminating the need for backpropagation through time. Extensive experiments on multiple benchmarks show that GSG achieves superior accuracy, robustness, and energy efficiency compared to both Euclidean SNNs and manifold-based GNNs, establishing a new paradigm for curvature-aware, energy-efficient graph learning.

## Skill Description

This skill is generated from the arXiv paper: Geometry-Aware Spiking Graph Neural Network (2508.06793).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2508.06793](http://arxiv.org/abs/2508.06793v2)
