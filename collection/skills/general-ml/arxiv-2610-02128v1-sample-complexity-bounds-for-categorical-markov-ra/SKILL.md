---
name: arxiv-2610-02128v1-sample-complexity-bounds-for-categorical-markov-ra
description: "arXiv paper: Sample complexity bounds for categorical Markov random fields via Discrete Diffusions"
tags: [arxiv, math.ST, research]
created: 2026-10-04
utility: 0.87
---

# Sample complexity bounds for categorical Markov random fields via Discrete Diffusions

**arXiv ID:** 2610.02128v1
**Authors:** Shivam Kumar, Nabarun Deb
**Published:** 2026-10-01
**Category:** math.ST
**Utility Score:** 0.87
**URL:** https://arxiv.org/abs/2610.02128v1

## Abstract

Many applications in statistics, economics, and physics require sampling from high-dimensional categorical distributions with local dependence structures. Examples include finite memory language models, Ising and Potts systems in statistical physics and protein folding, etc. In modern machine learning, discrete diffusions have emerged as a flexible approach for sampling such data, with strong empirical performance. Motivated by this, we develop learning methods with end-to-end sample complexity bounds for discrete diffusion with uniform noising under local dependence, which we model through low order Markov random fields (MRFs). Our main technical insight is a new \emph{pinning decomposition} of the discrete score. It shows that unlike in continuous diffusions, the score decomposes into components where the dependence on time separates multiplicatively from the dependence on the target. Building on this decomposition, we propose a \emph{weight-sharing neural score learner} and combine it with $τ$-leaping to obtain an end-to-end sampling procedure. Rather than treating score-learning error as a black-box input, as is common in existing sampling analyses, we study the score learning error from finite data and derive optimal sampling guarantees with explicit dependence on the vocabulary size, the interaction order of the MRF, and the sample size. Moreover, our strategy trains a single score network across uniform noise levels while leaving the sampling discretization to be chosen at inference-time. This allows the same trained model to trade accuracy for computational cost as inference-time budgets vary. Numerical experiments on Potts, Ising, and tree-structured models show that weight-sharing score networks outperform fully connected ones for sampling long sequences.

## Key Contributions

- Novel research in math.ST
- Published on arXiv: 2026-10-01

## Related Work

See arXiv for citations and references.
