---
name: arxiv-2610-17998-saliency-guided-replay-for-continual-learning-in-deep-spikin
description: 'Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks (arXiv: 2610.17998)'
metadata:
  {
    "arxiv_id": "2610.17998",
    "utility": 1.0,
    "title": "Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.17998"
  }
---

# Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks

**arXiv ID:** 2610.17998
**URL:** https://arxiv.org/abs/2610.17998
**Utility Score:** 1.00

## Abstract

Spiking Neural Networks (SNNs) are promising for energy-efficient neuromorphic computing, but they still suffer from catastrophic forgetting when learning tasks sequentially. This work investigates the integration of Experience Packing and Replay (EPR) as a memory-efficient continual learning strategy for deep SNNs under low-latency constraints. The proposed framework combines Batch Normalization Through Time stabilized VGG9 SNNs with Spike Activation Maps (SAM), which provide forward-only explanations based on spike activity. These explanations are temporally aggregated into spatial attention maps and used to select the most informative image patches for replay, instead of storing full images. Experiments on Split CIFAR10 and Split CIFAR100 show that SAM-guided EPR improves the accuracy-memory trade-off under tight memory budgets, and remains competitive while requiring substantially less storage.

## Key Topics

neural, spiking, neuromorphic, memory, efficient, continual learning

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.17998
