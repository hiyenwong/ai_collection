---
name: reliable-mechanistic-operator-recovery-with-biologically-informed-neural
description: 'Many biological processes are governed by complex dynamical mechanisms that remain incompletely understood despite increasing volumes of experimental data. Biologically-informed neural networks (BINNs. Based on arXiv:2607.07425.'
---

# Reliable mechanistic operator recovery with biologically-informed neural networks: principles for architecture and optimisation design

**arXiv**: 2607.07425 | **Authors**: Rebecca M. Crossley, Yuan Yin, Sarah L. Waters, Ruth E. Baker | **Utility**: 0.85

## Overview

Many biological processes are governed by complex dynamical mechanisms that remain incompletely understood despite increasing volumes of experimental data. Biologically-informed neural networks (BINNs) seek to address this challenge by embedding mechanistic differential equations into neural network training, enabling interpretable constitutive operators to be recovered directly from sparse and noisy observations. However, reliable operator recovery depends sensitively on network architecture, optimisation strategy, and data informativeness. Here, we present a systematic empirical study of how these factors influence mechanistic inference using BINNs applied to canonical one-dimensional advection-diffusion-reaction partial differential equation models. Across a suite of benchmark problems, we investigate how network expressivity, learning rate, loss weighting, and batch size influence optimisation behaviour and operator recovery. We show that successful mechanistic inference depends on balancing competing objectives rather than maximising any single aspect of the model or optimisation. Moderately expressive architectures outperform overly complex networks, intermediate learning rates improve optimisation stability, balanced data and PDE losses are essential for accurate operator recovery, and intermediate batch sizes provide the best compromise between computational efficiency and reproducibility. We further identify practical diagnostics for recognising common failure modes, including over-fitting, unstable optimisation, and poor mechanistic recovery when the ground truth is unavailable. Together, these findings provide evidence-based guidelines for deploying BINNs as credible tools for biological model discovery.

## Key Contributions

1. Many biological processes are governed by complex dynamical mechanisms that remain incompletely understood despite increasing volumes of experimental data.
2. Biologically-informed neural networks (BINNs) seek to address this challenge by embedding mechanistic differential equations into neural network training, enabling interpretable constitutive operators to be recovered directly from sparse and noisy observations.
3. However, reliable operator recovery depends sensitively on network architecture, optimisation strategy, and data informativeness.
4. Here, we present a systematic empirical study of how these factors influence mechanistic inference using BINNs applied to canonical one-dimensional advection-diffusion-reaction partial differential equation models.

## Implementation Notes

- **Keywords**: neural-network
- **Categories**: q-bio.QM, cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: neural-network.
