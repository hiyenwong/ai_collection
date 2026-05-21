---
name: platonic-representations-brain-universal-geometry
description: Platonic Representations in the Human Brain — self-supervised recovery of universal neural geometry across subjects using fMRI. Tests whether human visual cortex representations are approximately isometric and translatable via purely geometric transformations. Based on arXiv:2605.20496.
---

# Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry

**arXiv**: 2605.20496 | **Authors**: Pablo Marcos-Manchón, Rishi Jha, Lluís Fuentemilla

Tests the Strong Platonic Representation Hypothesis in biological brains: whether subject-specific fMRI representations can be aligned via purely geometric (orthogonal) transformations without paired cross-subject samples.

## Key Contributions

1. **Self-supervised fMRI encoder** learns subject-specific embeddings from repeated stimulus presentations (Natural Scenes Dataset)
2. **Unsupervised orthogonal rotation alignment** translates independently learned brain spaces across subjects
3. **Shared latent space** via synchronized pairwise rotations improves cross-subject retrieval
4. Evidence that **human visual cortex representations are approximately isometric** across individuals

## Method

- Self-supervised encoder trained on fMRI data alone (no labels, no model representations)
- Repeated stimulus trials provide the supervisory signal for representation learning
- Cross-subject alignment: find optimal orthogonal rotation between independently learned spaces
- Pairwise rotation synchronization extends to shared latent space across >2 subjects

## When to Use

- Analyzing cross-subject variability in brain representations
- Building zero-shot cross-subject decoding pipelines
- Investigating geometric properties of neural representations
- Studying convergence between ANN representations and biological brain geometry
- Working with Natural Scenes Dataset or similar fMRI datasets

## Activation Keywords

platonic representation, universal geometry, brain representation, cross-subject alignment, fMRI visual cortex, isometric embedding, Natural Scenes Dataset, representation alignment, self-supervised brain encoding, unsupervised brain translation
