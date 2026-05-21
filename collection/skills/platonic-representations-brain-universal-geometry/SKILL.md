---
name: platonic-representations-brain-universal-geometry
description: "Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry — evidence for a shared neural geometry in human visual cortex where subject-specific fMRI representations are approximately isometric across individuals. (arXiv:2605.20496)"
tags: [brain, representation-learning, fmri, visual-cortex, neural-geometry, plato-hypothesis, isometric-embedding, unsupervised-learning]
---

# Platonic Representations in the Human Brain

**Paper**: [arXiv:2605.20496](https://arxiv.org/abs/2605.20496) — Submitted 19 May 2026
**Authors**: Pablo Marcos-Manchón, Rishi Jha, Lluís Fuentemilla
**Categories**: q-bio.NC, cs.CV

## Summary

The **Strong Platonic Representation Hypothesis** suggests that representational convergence in artificial neural networks can be harnessed constructively — embeddings can be translated across models through a universal latent space without paired data. This paper asks whether an **analogous geometry can be recovered across human brains**.

Using **fMRI data from the Natural Scenes Dataset**, the authors propose a self-supervised encoder that learns subject-specific embeddings from brain data alone by exploiting repeated stimulus presentations.

## Key Findings

1. **Cross-subject geometric translation**: Independently learned subject-specific brain spaces can be translated across subjects using **unsupervised orthogonal rotations**, without paired cross-subject samples or intermediate model representations.

2. **Shared latent space**: Synchronizing pairwise rotations into a single shared latent space further improves cross-subject retrieval, indicating that subject-specific spaces are mutually compatible with a common coordinate system.

3. **Evidence for universal neural geometry**: The results provide evidence for a **shared neural geometry in the human visual cortex** — subject-specific fMRI representations are approximately isometric across individuals and can be translated through purely geometric transformations.

## Methodology

- **Data**: Natural Scenes Dataset (fMRI, 8 subjects viewing natural images)
- **Approach**: Self-supervised encoder → subject-specific embeddings → unsupervised orthogonal rotation alignment → shared latent space
- **Key technique**: Unsupervised Procrustes/orthogonal rotation to align independently learned embedding spaces
- **Evaluation**: Cross-subject retrieval performance before and after alignment

## Implications

- Supports the **Strong Platonic Representation Hypothesis** in biological neural systems
- Provides a **geometric foundation** for cross-subject brain decoding without paired data
- Enables **zero-shot transfer** of brain representations across individuals
- Bridges **artificial neural network representation learning** and **neuroscience**

## Activation

**Keywords**: platonic representation, universal geometry, brain representation, cross-subject alignment, fMRI, visual cortex, isometric embedding, unsupervised alignment, neural geometry, Natural Scenes Dataset

## Related Skills

- `meta-learning-in-context-brain-decoding` — Training-free cross-subject brain decoding
- `neuroscience-of-transformers` — Transformer architectures for brain data modeling
- `geometric-brain-dynamics-mapping` — Geometry-aware brain dynamics mapping
