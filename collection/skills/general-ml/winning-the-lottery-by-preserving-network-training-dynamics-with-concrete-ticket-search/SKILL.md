# Winning the Lottery by Preserving Network Training Dynamics with Concrete Ticket Search

**arXiv ID:** 2512.07142
**Authors:** Tanay Arora, Christof Teuscher
**Published:** 2025-12-08T03:48:51Z
**Abstract:**
The Lottery Ticket Hypothesis asserts the existence of highly sparse, trainable subnetworks ('winning tickets') within dense, randomly initialized neural networks. However, state-of-the-art methods of drawing these tickets, like Lottery Ticket Rewinding (LTR), are computationally prohibitive, while more efficient saliency-based Pruning-at-Initialization (PaI) techniques suffer from a significant accuracy-sparsity trade-off and fail basic sanity checks. In this work, we argue that PaI's reliance on first-order saliency metrics, which ignore inter-weight dependencies, contributes substantially to this performance gap, especially in the sparse regime. To address this, we introduce Concrete Ticket Search (CTS), an algorithm that frames subnetwork discovery as a holistic combinatorial optimization problem. By leveraging a Concrete relaxation of the discrete search space and a novel gradient balancing scheme (GRADBALANCE) to control sparsity, CTS efficiently identifies high-performing subnetworks near initialization without requiring sensitive hyperparameter tuning. Motivated by recent works on lottery ticket training dynamics, we further propose a knowledge distillation-inspired family of pruning objectives, finding that minimizing the reverse Kullback-Leibler divergence between sparse and dense network outputs (CTS-KL) is particularly effective. Experiments on varying image classification tasks show that CTS produces subnetworks that robustly pass sanity checks and achieve accuracy comparable to or exceeding LTR, while requiring only a small fraction of the computation. For example, on ResNet-20 on CIFAR10, it reaches 99.3% sparsity with 74.0% accuracy in 7.9 minutes, while LTR attains the same sparsity with 68.3% accuracy in 95.2 minutes. CTS's subnetworks outperform saliency-based methods across all sparsities, but its advantage over LTR is most pronounced in the highly sparse regime.

## Skill Description

This skill is generated from the arXiv paper: Winning the Lottery by Preserving Network Training Dynamics with Concrete Ticket Search (2512.07142).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2512.07142](http://arxiv.org/abs/2512.07142v1)
