---
name: platonic-representations-brain
description: "Platonic Representations in the Human Brain methodology — unsupervised recovery of universal neural geometry across subjects from fMRI data. Use when: (1) studying cross-subject brain alignment without shared stimuli, (2) applying unsupervised orthogonal rotation / Procrustes to neural embeddings, (3) working with the Strong Platonic Representation Hypothesis in biological neural systems, (4) analyzing shared geometry in human visual cortex from fMRI (NSD dataset), (5) implementing self-supervised fMRI encoders with repeated stimulus presentations. Keywords: platonic representation, universal geometry, cross-subject alignment, fMRI, orthogonal Procrustes, representational similarity, visual cortex, NSD."
---
# Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry

Methodology from arXiv:2605.20496 (May 2026). Authors: Pablo Marcos-Manchón, Rishi Jha, Lluís Fuentemilla.

## Core Idea

The Strong Platonic Representation Hypothesis states that independently trained neural networks converge to geometrically similar representations. This paper extends that hypothesis to **biological neural systems** — specifically, the human visual cortex — showing that subject-specific fMRI embedding spaces can be translated across subjects using **only the intrinsic geometry of neural responses**, without shared stimuli or paired supervision.

## Key Results

1. **Self-supervised fMRI encoder**: Learns subject-specific embeddings from fMRI data alone by exploiting repeated stimulus presentations (Natural Scenes Dataset).

2. **Approximately isometric spaces**: Independently learned subject embeddings can be translated via simple unsupervised orthogonal rotations (Procrustes), recovering accurate instance-level cross-subject correspondences.

3. **Common coordinate system**: Synchronizing pairwise rotations into a single shared latent space improves cross-subject retrieval, demonstrating mutual compatibility of subject-specific spaces.

## Method Details

### Self-Supervised Encoder
- Uses repeated stimulus presentations in NSD (each image seen 3 times by each subject)
- Learns embeddings from brain activity voxels without any image/modal supervision
- Exploits the fact that repeated presentations of the same stimulus should produce similar neural embeddings

### Unsupervised Orthogonal Rotation
- Given two subject-specific embedding spaces S₁, S₂, finds orthogonal matrix R minimizing ||S₁R - S₂||²
- No paired cross-subject samples needed — relies on shared stimulus identity across subjects
- Proves that independently learned spaces are approximately isometric

### Shared Latent Space Synchronization
- Extends pairwise alignment to multi-subject setting
- Synchronizes all pairwise rotations into one consensus coordinate system
- Further improves cross-subject retrieval performance

## Dataset

**Natural Scenes Dataset (NSD)**: Large-scale 7T fMRI dataset of subjects viewing complex natural images. Each image is viewed 3 times per subject, enabling self-supervised learning from repetition structure.

## Implications

- Provides evidence for shared neural geometry in human visual cortex
- Suggests that biological brains converge toward similar geometric representations of visual experience
- Practical applications: cross-subject neural decoding, brain-computer interfaces without subject-specific calibration
- Bridging the gap between AI representational convergence and neuroscience

## Activation
- platonic representation, universal geometry, cross-subject alignment, fMRI alignment, neural geometry, Procrustes alignment, shared latent space, brain representation convergence
