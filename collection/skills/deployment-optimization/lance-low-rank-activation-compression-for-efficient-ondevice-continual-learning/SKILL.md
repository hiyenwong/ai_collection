# LANCE: Low Rank Activation Compression for Efficient On-Device Continual Learning

**arXiv ID:** 2509.21617
**Authors:** Marco Paul E. Apolinario, Kaushik Roy
**Published:** 2025-09-25T21:33:40Z
**Abstract:**
On-device learning is essential for personalization, privacy, and long-term adaptation in resource-constrained environments. Achieving this requires efficient learning, both fine-tuning existing models and continually acquiring new tasks without catastrophic forgetting. Yet both settings are constrained by high memory cost of storing activations during backpropagation. Existing activation compression methods reduce this cost but rely on repeated low-rank decompositions, introducing computational overhead. Also, such methods have not been explored for continual learning. We propose LANCE (Low-rank Activation Compression), a framework that performs one-shot higher-order Singular Value Decomposition (SVD) to obtain a reusable low-rank subspace for activation projection. This eliminates repeated decompositions, reducing both memory and computation. Moreover, fixed low-rank subspaces further enable on-device continual learning by allocating tasks to orthogonal subspaces without storing large task-specific matrices. Experiments show that LANCE reduces activation storage up to 250$\times$ while maintaining accuracy comparable to full backpropagation on CIFAR-10/100, Oxford-IIIT Pets, Flowers102, and CUB-200 datasets. On continual learning benchmarks (Split CIFAR-100, Split MiniImageNet, 5-Datasets), it performs competitively with orthogonal gradient projection methods at a fraction of the memory cost. These results position LANCE as a practical and scalable solution for efficient fine-tuning and continual learning on edge devices.

## Skill Description

This skill is generated from the arXiv paper: LANCE: Low Rank Activation Compression for Efficient On-Device Continual Learning (2509.21617).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2509.21617](http://arxiv.org/abs/2509.21617v2)
