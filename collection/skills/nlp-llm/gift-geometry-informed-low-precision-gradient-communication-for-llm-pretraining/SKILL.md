---
name: gift-geometry-informed-low-precision-gradient-communication-for-llm-pretraining
description: 'Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining. Communicating gradients in low-precision formats, such as FP8 and NVFP4, can significantly reduce the. Based on arXiv:2607.07494.'
---

# GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining

**arXiv**: 2607.07494 | **Authors**: Jieying Wang, Shuyuan Fan, Mingkai Zheng, Zhao Zhang | **Utility**: 0.85

## Overview

Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining. Communicating gradients in low-precision formats, such as FP8 and NVFP4, can significantly reduce the communication volume. Existing methods quantize gradients via linear or nonlinear mappings in Euclidean space, often degrading model performance because highly anisotropic gradients incur direction-dependent distortion. We present GIFT, a geometry-informed gradient scaling method that performs low-precision communication in geometry-aware coordinates. By transforming gradients into a near-isotropic space before quantization, GIFT makes low-precision representations substantially more faithful to their high-precision counterparts. GIFT only changes the coordinate system used for low-precision gradient communication and does not change the optimizer, training recipe, communication collective, or low-precision format. We also develop a simplified geometry-aware transformation algorithm with low-rank approximation and selective application to balance the computation overhead and communication reduction. We examine the empirical convergence of GIFT using Llama-300M and Llama-600M models. Our results show that GIFT reduces the end-to-end pretraining time of Llama-600M by 7.6% on 64 NVIDIA GH200 Superchips, while improving the downstream task preservation profile over direct Euclidean FP8 communication under the same optimizer and communication path.

## Key Contributions

1. Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining.
2. Communicating gradients in low-precision formats, such as FP8 and NVFP4, can significantly reduce the communication volume.
3. Existing methods quantize gradients via linear or nonlinear mappings in Euclidean space, often degrading model performance because highly anisotropic gradients incur direction-dependent distortion.
4. We present GIFT, a geometry-informed gradient scaling method that performs low-precision communication in geometry-aware coordinates.

## Implementation Notes

- **Keywords**: llm
- **Categories**: cs.DC, cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm.
