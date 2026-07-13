---
name: nerve-brain-fc-tokenization
description: >
  NERVE (Network-Aware Representations of Brain Functional Connectivity via Bilinear Tokenization) -
  self-supervised learning framework for brain functional connectivity (FC) representation learning.
  Redefines FC matrix tokenization by partitioning into intra/inter-network connectivity blocks,
  using structured bilinear factorization for heterogeneous patch sizes.
  Use when: building brain network ML models, self-supervised fMRI/FC representation learning,
  masked autoencoder for brain data, brain-behavior prediction, or developmental neuroimaging analysis.
  Keywords: NERVE, brain functional connectivity, bilinear tokenization, masked autoencoder,
  self-supervised learning, brain network, FC representation, MAE brain, connectome tokenization.
---

# NERVE: Network-Aware Brain FC Tokenization

arXiv: 2605.14048 | Milecki et al. (May 2026)

## Core Problem

Standard masked autoencoders (MAEs) for brain functional connectivity (FC) treat FC matrices as
structurally homogeneous elements, ignoring the large-scale modular organization of brain networks.
Fixed-size patch tokenization (from vision MAEs) is fundamentally misaligned with brain network structure.

## NERVE Solution

### Bilinear Tokenization
- Partition FC matrices into patches defined by **network pairs** (intra-network and inter-network blocks)
- Each patch corresponds to a distinct functional role (e.g., DMN-visual, fronto-parietal)
- Patches are heterogeneous in size (unlike image patches)

### Structured Bilinear Factorization
- Embed FC patches through low-rank bilinear decomposition
- Preserves network identity information
- Reduces parameter complexity from **quadratic to linear** in number of networks
- Key insight: W = A ⊗ B where A captures source-network factors, B captures target-network factors

## Architecture

```
FC Matrix (N×N)
    ↓ Network-aware partitioning
Patches (heterogeneous sizes, network-pair defined)
    ↓ Bilinear factorization
Low-dim embeddings preserving network identity
    ↓ Masked Autoencoder
Self-supervised representation
    ↓ Downstream: behavior/psychopathology prediction
```

## Key Advantages

1. **Network-aware**: Respects known brain network organization (DMN, FPN, visual, etc.)
2. **Parameter efficient**: Linear scaling vs. quadratic in number of networks
3. **Transferable**: Stable representations across developmental cohorts
4. **Interpretable**: Patches map to known functional circuits

## Evaluated On

- ABCD (Adolescent Brain Cognitive Development)
- PNC (Philadelphia Neurodevelopmental Cohort)
- CCNP (Connectomes Related to Human Brain Development)

## Applications

- Behavior prediction from resting-state fMRI
- Psychopathology screening
- Developmental trajectory analysis
- Transfer learning across cohorts

## When to Use NERVE Approach

- Self-supervised pre-training on FC matrices
- Brain-behavior prediction tasks
- Multi-cohort transfer learning
- When interpretability of FC representations matters

## Activation

- NERVE, bilinear tokenization, brain FC
- 脑功能连接, 脑网络表示学习
- Masked autoencoder for brain data
- FC matrix tokenization, self-supervised fMRI
