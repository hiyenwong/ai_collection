---
name: a-unified-hessian-guided-framework-for-post-training
description: "A Unified Hessian-Guided Framework for Post-Traini..."
tags: [cs.LG, cs.AI]
source: arxiv
arxiv_id: 2610.40345v1
utility: 0.94
published: 2026-10-29
---

# A Unified Hessian-Guided Framework for Post-Training Quantization

**Authors:** Mads Toftrup, Marco Federici, Boris van Breugel, Paul Whatmough, Markus Nagel
**Published:** 2026-10-29
**arXiv:** [2610.40345v1](https://arxiv.org/abs/2610.40345v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.94

## Abstract

Low-bit quantization enables efficient deployment of large language models by reducing memory footprint and computational cost. Achieving high accuracy at low precision requires selecting quantization ranges, linear transformations, and weight rounding decisions. Existing approaches typically optimize these components independently using local reconstruction objectives, which fail to account for the varying impact of quantization errors on downstream predictions. Direct optimization of task-level metrics would provide a more faithful objective, but is challenging due to the discontinuous nature of quantization operations and the high computational cost of evaluating their downstream effects. In this work, we derive a Hessian-guided approximation of the output change induced by joint weight and activation quantization. Based on a tractable Fisher approximation, we formulate a unified post-training quantization framework that enables the joint optimization of quantization ranges, linear transformations, and weight rounding under a common output-sensitivity objective. The resulting method remains practical for modern large language models and consistently outperforms state-of-the-art transformation and rounding methods across both channel-wise and block-wise quantization settings.

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-29

## Activation

unified, hessianguided, framework, posttraining, quantization
