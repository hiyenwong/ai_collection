---
name: cross-species-neural-dynamics
description: Cross-species representation learning aligns mouse and human neural dynamics to track clinical drug efficacy, revealing that preclinical models poorly predict human drug efficacy.
tags: [cross-species-analysis, neural-dynamics, drug-efficacy, representation-learning, translational-neuroscience]
---

# Cross-species Neural Dynamics

## Paper Metadata

- **arXiv ID**: 2610.11222
- **Title**: Cross-species Neural Dynamics
- **Categories**: q-bio.NC, cs.AI, cs.LG
- **Utility Score**: 0.86
- **Date**: 2026-10-10
- **Link**: https://arxiv.org/abs/2610.11222

## Key Contributions

- Develops cross-species representation learning that aligns mouse and human neural dynamics into a shared embedding space.
- Demonstrates that aligned representations can track clinical drug efficacy across species.
- Reveals that preclinical (mouse) models poorly predict human drug efficacy when using neural dynamics as the outcome measure.
- Provides a framework for improving translational validity of preclinical neuroscience research.

## Core Methodology

The framework addresses a fundamental challenge in translational neuroscience: how to relate neural measurements from animal models to human brain function. Traditional approaches compare summary statistics (e.g., firing rates, power spectra) across species, but these may miss dynamically relevant features.

The method learns a shared representation space where mouse and human neural recordings are aligned based on their dynamical properties rather than their raw features. Using contrastive learning or optimal transport, the model maps neural activity patterns from both species into a common embedding where similar dynamics occupy nearby regions regardless of species.

When applied to drug efficacy studies, the aligned representations reveal that drugs that produce similar neural dynamics in mice do not necessarily produce similar dynamics in humans. This finding challenges the assumption that preclinical models are predictive of human outcomes and suggests that cross-species alignment could improve drug development by identifying which animal models are truly translational for specific neural circuits or conditions.

## Relevance to neuroscience

Directly addresses the translational gap between preclinical and clinical neuroscience. Relevant to drug development, biomarker discovery, and understanding which aspects of neural function are conserved across species versus which are species-specific.

## Reference

- Paper: https://arxiv.org/abs/2610.11222
