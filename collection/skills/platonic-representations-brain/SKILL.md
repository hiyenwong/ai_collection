---
name: platonic-representations-brain
description: "Demonstrates that subject-specific fMRI representations from visual cortex are approximately isometric across individuals and can be translated through purely geometric transformations. Uses self-supervised learning and unsupervised orthogonal rotations to recover a shared neural geometry."
---

# Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry

Extends the Strong Platonic Representation Hypothesis from artificial neural networks to the human brain: fMRI representations from different subjects' visual cortex are approximately isometric and can be aligned through purely geometric transformations without paired data.

Based on: *Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry* (arXiv:2605.20496) — Marcos-Manchón, Jha & Fuentemilla (2026).

## Activation Keywords

- platonic representation human brain
- cross-subject brain alignment unsupervised
- fMRI representation geometry translation
- shared neural geometry visual cortex
- self-supervised brain encoder orthogonal rotation
- universal latent space brain decoding
- neural isometry cross-subject
- 柏拉图表示人脑通用几何

## Core Innovation

### Translating the Platonic Hypothesis to Brains

The Strong Platonic Representation Hypothesis says neural network embeddings can be translated through a universal latent space. This work asks: **Can the same be done across human brains?**

### Key Method

Using fMRI data from the **Natural Scenes Dataset**:

1. **Self-supervised encoder**: Learns subject-specific embeddings from brain data alone by exploiting repeated stimulus presentations (no labels)
2. **Unsupervised alignment**: Translates embeddings across subjects using orthogonal rotations — no paired cross-subject samples needed
3. **Joint synchronization**: Aligning all pairwise rotations into a shared latent space further improves retrieval

## Key Findings

### Evidence for Shared Neural Geometry

- **Subject-specific fMRI representations** in visual cortex are approximately isometric across individuals
- **Geometric transformations alone** (orthogonal rotations) suffice for cross-subject translation
- **Common coordinate system** exists: pairwise synchronizations are mutually compatible

### No Intermediate Models Needed

Unlike prior work that uses intermediate DNN representations to bridge subjects, this approach works with:
- No intermediate model representations
- No paired cross-subject training samples
- No stimulus labels during encoding

## Methodology

### Encoder Architecture

- Self-supervised learning via repeated stimulus presentations
- Subject-specific embedding spaces
- fMRI voxel → latent space mapping

### Alignment Procedure

1. Learn independent subject-specific embeddings
2. Compute pairwise orthogonal rotations between subject spaces
3. Synchronize rotations into a single shared latent space
4. Evaluate via cross-subject retrieval performance

## Implications

### For Neuroscience

- Provides evidence that **neural representations share a universal geometry** across individuals
- Suggests the visual cortex develops functionally equivalent representations through shared developmental and evolutionary constraints
- Opens the door to pooling fMRI data across subjects without explicit normalization

### For Brain-Computer Interfaces

- Enables cross-subject zero-shot decoding
- Reduces need for subject-specific calibration
- Could generalize to other brain regions and modalities

### For AI

- Biological validation of the Platonic Representation Hypothesis
- Suggests alignment methods from AI transfer to neural data
- Potential for brain-to-brain communication frameworks

## Related Work

- [[grid-place-cell-co-emergence]] - Unified model of spatial cell co-emergence
- [[meta-learning-in-context-brain-decoding]] - Training-free cross-subject brain decoding
- [[fc-guided-band-selection-bci]] - Subject-adaptive BCI via functional connectivity
