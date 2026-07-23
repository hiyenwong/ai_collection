---
name: rank-order-n-of-m-codes-for-sparse-distributed-mem
description: Skill derived from arXiv paper 2607.02967: Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures
category: other
created: 2026-07-23
arxiv_id: 2607.02967
utility: 1.0
---
# rank-order-n-of-m-codes-for-sparse-distributed-mem

Derived from arXiv paper [2607.02967]: Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures

## Abstract
Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory. CALM (Nechesov and Ruponen, 2025) identifies its threshold-binary encoder as an open design question. This paper evaluates rank-order N-of-M encoding (Furber et al., 2007) as an alternative. We make three contributions. First, a faithful reimplementation validates the published architecture by confirming exact equivalence between WheelSDM and RankOrderSDM (cosine similarity 1.0000 across 10 seeds) and reproducing the documented divergence of RDLIF neurons under interference. Second, multi-seed capacity experiments show RankOrderSDM outperforming StandardSDM by 13.4 percentage points at saturation in the scaled configuration and by 0.8 percentage points at the published architecture scale. Third, BER robustness experiments disentangle representation and learning effects, showing that the large robustness gain arises primarily from the interaction of rank-order encoding with MAX-Hebbian learning, while the encoder alone provides only a small advantage under matched learning conditions. Experiments on GloVe-100 embeddings confirm this small but consistent encoding benefit on real structured data, whereas sentence embeddings exhibit a ceiling effect at low memory load. A secondary analysis shows that idealized rank-order encoding requires half the component-level encoding energy of SpikingMamba's SI-LIF neurons at four-bit precision, although decoder costs dominate overall system energy. These results identify which components of the original rank-order SDM architecture provide measurable benefits for contemporary memory-augmented AI systems, offering practical guidance for architectures such as CALM.

## Authors
Joy Bose

## Published
2026-07-03

## Categories
cs.LG, cs.NE

## Utility
1.0

## Note
This skill was automatically generated from the arXiv paper as part of the daily cron job.
