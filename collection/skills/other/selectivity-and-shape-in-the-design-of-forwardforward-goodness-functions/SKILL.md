# Selectivity and Shape in the Design of Forward-Forward Goodness Functions

**arXiv ID:** 2604.13081
**Authors:** Talha Ruzgar Akkus, Suayp Talha Kocabay, Kamer Ali Yuksel, Hassan Sawaf
**Published:** 2026-03-28T23:11:21Z
**Abstract:**
The Forward-Forward (FF) algorithm trains networks layer-by-layer using a local "goodness function," yet sum-of-squares (SoS) has remained the only choice studied. We systematically explore the goodness-function design space and identify a unifying principle: the goodness function must be sensitive to the shape of neural activity, not its total energy. This principle is motivated by the observation that deep network activations follow heavy-tailed distributions and that discriminative information is often concentrated in peak activities. We propose two complementary families: selective functions (top-k, entmax-weighted energy) that measure only peak activity, and shape-sensitive functions (excess kurtosis / "burstiness" and higher-order moments) that reward heavy-tailed distributions via scale-invariant statistics. Combined with separate label-feature forwarding (FFCL), controlled experiments across 13 goodness functions, 5 activations, 6 datasets, and three continuous sweeps, each tracing a characteristic inverted-U, yield 89.0% on Fashion-MNIST and 98.2+-0.1% on MNIST (4x2000), a +32.6pp gain over SoS, with consistent improvements across all benchmarks (+72pp USPS, +52pp SVHN). The scale-invariant nature of burstiness makes it particularly robust to magnitude shifts across layers and datasets.

## Skill Description

This skill is generated from the arXiv paper: Selectivity and Shape in the Design of Forward-Forward Goodness Functions (2604.13081).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.13081](http://arxiv.org/abs/2604.13081v2)
