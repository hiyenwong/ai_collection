---
name: decoupling-time-and-space-a-temporally
description: "Decoupling Time and Space: A Temporally Conditione..."
tags: [cs.LG]
source: arxiv
arxiv_id: 2610.06726v1
utility: 0.87
published: 2026-10-05
---

# Decoupling Time and Space: A Temporally Conditioned Refinement for EEG Source Imaging

**Authors:** Marco Morik, Jesse Palarus, Carmen Vidaurre, Klaus-Robert Müller, Shinichi Nakajima
**Published:** 2026-10-05
**arXiv:** [2610.06726v1](https://arxiv.org/abs/2610.06726v1)
**Categories:** cs.LG
**Utility Score:** 0.87

## Abstract

Electroencephalography (EEG) offers millisecond temporal resolution, but inferring underlying neural sources is a severely ill-posed spatial inverse problem. While deep learning has advanced spatial reconstruction, current architectures face a critical dilemma: frame-by-frame models discard vital temporal context, whereas full 4D spatiotemporal networks introduce an architectural trade-off between reconstruction accuracy and inference cost. We propose a novel two-stream framework that explicitly decouples global temporal representation learning from per-time-point spatial refinement. A Transformer-based Temporal Condition Encoder processes the entire EEG sequence via factorized spatiotemporal attention, retaining sensor-resolved features. A fixed inverse then maps these features into source-indexed conditioning for a per-timestep Source-Space Transformer or volumetric convolutional refiner. Extensive evaluations on realistic synthetic data demonstrate that this temporal prior dramatically improves spatial localization, outperforming classical and spatiotemporal baselines, particularly in high-noise and multi-source regimes. Training across diverse leadfields and explicit operator mismatches improves transfer to unseen head geometries and brings template-based reconstruction closer to subject-specific inversion. Furthermore, we apply the model trained only on synthetic EEG data to real-world EEG. A logistic regressor fit on source power differences in eyes-open, eyes-closed co

## Key Contributions

- Novel research in cs.LG
- Published 2026-10-05

## Activation

decoupling, time, space, temporally, conditioned, refinement, source, imaging
