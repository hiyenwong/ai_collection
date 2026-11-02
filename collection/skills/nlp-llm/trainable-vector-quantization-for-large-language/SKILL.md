---
name: trainable-vector-quantization-for-large-language
description: "Trainable Vector Quantization for Large Language M..."
tags: [cs.LG]
source: arxiv
arxiv_id: 2610.41822v1
utility: 0.95
published: 2026-10-30
---

# Trainable Vector Quantization for Large Language Models

**Authors:** Anastasiia Prutianova, Alina Bogdanova, Mikhail Shutov, Dmitrii Poimanov, Anatoly Gorkov...
**Published:** 2026-10-30
**arXiv:** [2610.41822v1](https://arxiv.org/abs/2610.41822v1)
**Categories:** cs.LG
**Utility Score:** 0.95

## Abstract

Vector Quantization (VQ) is a rapidly evolving technique for compressing Large Language Model (LLM) weights, reducing memory usage, and speeding up inference. However, extreme compression deteriorates model performance, which is challenging to recover due to the discrete nature of VQ parameters. Existing methods employ training-free approaches that are limited to layer-wise reconstruction loss minimization. To address this limitation, we propose TVQ, a novel method that leverages straight-through estimation to enable gradient descent-based optimization of vector-quantized LLMs. By reformulating VQ LLM optimization with trainable latent weights, TVQ enables arbitrary objective minimization. We constitute our approach by applying TVQ in a block-wise knowledge distillation paradigm, which balances quality and training efficiency, and propose several practical solutions to accelerate training. In experiments on modern LLMs, we demonstrate that TVQ is compatible with modern VQ schemes. As a result, TVQ achieves state-of-the-art quality in low-bit post-training quantization settings with a modest training budget and straightforward PyTorch implementation. For instance, TVQ achieves near-lossless 2-bit quantization for LLaMA2-70B with only 1% accuracy drop on popular Question-Answering benchmarks.

## Key Contributions

- Novel research in cs.LG
- Published 2026-10-30

## Activation

trainable, vector, quantization, large, language, models
