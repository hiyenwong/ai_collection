---
title: "SABLE: Scalable Affine Bayesian Latent-space Exploration"
authors: "Erik Bodin, Lisa Maria Kreusser, Donney Fan, Henry Moss, Geoff Pleiss..."
published: "2026-10-22"
arxiv_id: "2610.31495v1"
url: "https://arxiv.org/abs/2610.31495v1"
categories: ["cs.LG", "cs.AI", "stat.ML"]
utility_score: 0.89
tags: [arxiv, paper, ai-safety-eval]
---

# SABLE: Scalable Affine Bayesian Latent-space Exploration

**Authors:** Erik Bodin, Lisa Maria Kreusser, Donney Fan, Henry Moss, Geoff Pleiss...
**Published:** 2026-10-22
**arXiv:** [2610.31495v1](https://arxiv.org/abs/2610.31495v1)
**Categories:** cs.LG, cs.AI, stat.ML
**Utility Score:** 0.89

## Abstract

Complex objects such as engineering designs and proteins are often difficult to optimise because their design spaces exhibit high-dimensional structure and objective evaluations are expensive. Generative models provide continuous latent representations, but their latent spaces can have thousands to tens of thousands of dimensions, creating a regime where the latent dimension $D$ greatly exceeds the evaluation budget. We introduce SABLE, a Bayesian optimisation method for high-dimensional latent spaces with an isotropic distribution and limited budget. SABLE uses a Bayesian affine surrogate for prediction and acquisition, treating higher-order structure as surrogate discrepancy. After $N$ observations, the slope update has dimension at most $N-1$, yielding a decomposition of each query into an in-span component optimised by expected improvement (EI) in at most $N$ dimensions and an off-span component governed by a scalar norm. We show that the off-span norm implicitly selected by affine EI can lead to underexploration, and SABLE instead prescribes it using a finite-horizon schedule, without restricting search to a learned subspace. A recompression scheme reduces information to $\mathcal O(M)$ pseudo-observations, bounding refitting cost by $\mathcal O(M^2D+M^3)$ while keeping parameter inference, prediction, and acquisition decisions to tens of milliseconds. Across synthetic benchmarks and latent-space optimisation tasks, SABLE achieves high sample efficiency and reduces decision time by several orders of magnitude at large budgets.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: ai-safety-eval

## Related Skills

Check the `ai-safety-eval` directory for related papers and tools.
