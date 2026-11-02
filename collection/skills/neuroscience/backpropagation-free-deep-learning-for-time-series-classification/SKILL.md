---
name: backpropagation-free-deep-learning-for-time-series-classification
description: "Backpropagation-free Deep Learning for Time-Series..."
tags: [cs.LG, cs.AI]
source: arxiv
arxiv_id: 2610.41805v1
utility: 0.97
published: 2026-10-30
---

# Backpropagation-free Deep Learning for Time-Series Classification

**Authors:** Miha Kapš, Blaž Bertalanič, Carolina Fortuna
**Published:** 2026-10-30
**arXiv:** [2610.41805v1](https://arxiv.org/abs/2610.41805v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.97

## Abstract

Deep neural networks for time series classification (TSC) are trained almost exclusively by error backpropagation, which imposes update locking and the weight-transport problem. Backpropagation-free learning rules such as Direct Feedback Alignment (DFA), Direct Random Target Projection (DRTP), and the diffusion-inspired NoProp relax these constraints but have been evaluated almost exclusively on 2D image benchmarks. We adapt these three learners to univariate TSC with 1D convolutional architectures and present the first systematic study of them across 112 datasets from the UCR time series archive, with one hyperparameter-optimized configuration per method. The optimized learners reach mean F1 scores of 0.76 to 0.79, below ROCKET (0.83) and InceptionTime (0.84). We propose an analysis framework that relates the per-dataset gap to InceptionTime to dataset properties and tests convolutional feature learning by replacing the flatten readout with global average pooling, measured as a difference-in-differences (DD) against a backpropagation control on the identical architecture. Intra-class temporal variability is the dataset property most consistently associated with the gap for all three learners (partial Spearman $ρ$ from $0.28$ to $0.40$). Pooling harms DFA and DRTP more than backpropagation (DD $-0.025$ and $-0.055$), consistent with near-random convolutional features, whereas NoProp tolerates pooling as backpropagation does (DD $+0.013$). Relative to backpropagation on the sa

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-30

## Activation

backpropagationfree, deep, learning, timeseries, classification
