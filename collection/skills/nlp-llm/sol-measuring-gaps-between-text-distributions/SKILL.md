---
name: sol-measuring-gaps-between-text-distributions
description: "SOL: Measuring Gaps between Text Distributions by ..."
tags: [cs.CL, cs.LG, stat.ML]
source: arxiv
arxiv_id: 2610.06513v1
utility: 0.89
published: 2026-10-05
---

# SOL: Measuring Gaps between Text Distributions by Double Sliced Wasserstein Metrics

**Authors:** Gregor Kornhardt, Moritz Piening, Jannis Chemseddine, Gabriele Steidl
**Published:** 2026-10-05
**arXiv:** [2610.06513v1](https://arxiv.org/abs/2610.06513v1)
**Categories:** cs.CL, cs.LG, stat.ML
**Utility Score:** 0.89

## Abstract

Evaluating text generation requires measuring how well the generated distribution matches the data distribution. For autoregressive models, this is done by the perplexity. Diffusion and flow-based language models can only provide a likelihood bound, whose tightness differs between model families. Sample-based substitutes such as generative perplexity with entropy do not consider the distribution fit. We propose SOL, a distance between text distributions. Each sequence is represented by the empirical measure of its hidden states under a fixed transformer and the distributions of these measures are compared by the double sliced Wasserstein distance. We prove that SOL is a metric if the transformer is injective. Experiments show that SOL detects distributional failures, recovers expected model trends, and provides stable sample-based estimates. We put forward SOL to fill the gap in the current evaluation protocol used for non auto-regressive models. As a first step we use SOL to re-evaluate a variety of models trained on OpenWebText.

## Key Contributions

- Novel research in cs.CL, cs.LG
- Published 2026-10-05

## Activation

measuring, gaps, between, text, distributions, double, sliced, wasserstein, metrics
