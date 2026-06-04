---
name: nerve-fc-bilinear-tokenization
description: "NERVE: Network-Aware Bilinear Tokenization for Brain Functional Connectivity representation learning. Self-supervised learning framework that redefines FC tokenization via structured bilinear factorization, aligning with large-scale brain network organization. Activation: NERVE, brain FC tokenization, functional connectivity representation, bilinear tokenization, network-aware MAE, brain network MAE."
category: neuroscience
---

# NERVE: Network-Aware Bilinear Tokenization for Brain FC

**arXiv**: 2605.14048v2 (2026-05-15)
**Authors**: Leo Milecki, Qingyu Hu, Bahram Jafrasteh, Mert R. Sabuncu, Qingyu Zhao
**Affiliation**: Weill Cornell Medicine, Cornell University
**Code**: https://github.com/leomlck/NERVE
**Keywords**: rs-fMRI, Brain Functional Connectivity, Deep Learning, Masked Autoencoder, Self-Supervised Learning

## Overview

NERVE (Network-Aware Representations of Brain Functional Connectivity via Bilinear Tokenization) is a self-supervised learning framework that addresses the fundamental question of how to tokenize brain functional connectivity (FC) matrices in a way that aligns with the intrinsic modular organization of large-scale brain networks.

### Core Innovation

The key insight is that **FC matrices should be tokenized based on brain network organization**, not treated as structurally homogeneous elements. NERVE partitions FC matrices into patches of intra- and inter-network connectivity blocks, then embeds these heterogeneous patches through a novel **structured bilinear factorization**.

## Technical Details

### Problem Statement

Existing approaches for FC representation learning (e.g., Masked Autoencoders adapted from computer vision) use heuristic tokenization schemes that:
- Treat FC matrices as structurally homogeneous
- Ignore large-scale brain network organization
- Use region-centric or graph-based schemes that don't reflect functional modularity

### NERVE Architecture

1. **Network-Aware Patch Definition**: FC matrices are partitioned into patches based on brain network pairs (e.g., Default Mode Network × Salience Network), creating heterogeneous-sized blocks that correspond to distinct functional roles.

2. **Structured Bilinear Factorization**: Each FC patch is embedded via a bilinear decomposition:
   - Preserves network identity
   - Reduces parameter complexity from quadratic O(N²) to linear O(N) scaling in the number of networks
   - Captures both within-network and between-network connectivity patterns

3. **Masked Autoencoder Training**: Patches are masked and reconstructed from visible tokens, learning robust representations without labeled data.

4. **Downstream Prediction**: Learned representations are used for behavioral and psychopathology prediction tasks.

### Key Design Choices

| Component | NERVE Approach | Baseline Approach |
|-----------|---------------|-------------------|
| Tokenization | Network-pair blocks | Fixed-size patches / regions |
| Embedding | Bilinear factorization | Linear projection |
| Parameter Scaling | Linear in # networks | Quadratic in # regions |
| Domain Prior | Brain network organization | Structurally agnostic |

## Evaluation Results

### Datasets
- **ABCD** (Adolescent Brain Cognitive Development)
- **PNC** (Philadelphia Neurodevelopmental Cohort)
- **CCNP** (Columbia Center for Computational Neuroimaging Pediatric)

### Performance
- **Outperforms** structurally agnostic MAE variants and graph-based self-supervised baselines
- **More stable and transferable** representations, particularly in cross-cohort evaluation
- **Ablation studies** confirm bilinear network embedding and anatomically grounded parcellation are critical for performance

## Practical Applications

### 1. Brain-Behavior Prediction
Use NERVE representations to predict:
- Cognitive abilities
- Behavioral outcomes
- Psychopathology risk

### 2. Cross-Cohort Generalization
NERVE's network-aware design enables better transfer learning across different neuroimaging datasets and populations.

### 3. Developmental Neuroscience
Particularly effective for studying brain development across age groups due to robust representation learning.

## Implementation Guide

### Setup
```bash
git clone https://github.com/leomlck/NERVE
cd NERVE
# Follow repository setup instructions
```

### Typical Workflow
1. **Data Preparation**: Prepare FC matrices from rs-fMRI data using a standardized parcellation
2. **Network Assignment**: Assign regions to canonical brain networks (e.g., Yeo 7-network or 17-network parcellation)
3. **Bilinear Tokenization**: Partition FC matrices into network-pair blocks
4. **MAE Pre-training**: Train masked autoencoder on unlabeled FC data
5. **Fine-tuning**: Use learned representations for downstream prediction tasks

## Key Concepts

### Functional Connectivity (FC)
Temporal correlation between spatially distributed brain regions measured via rs-fMRI. Used to study individual differences in brain organization.

### Masked Autoencoder (MAE)
Self-supervised learning framework that:
- Partitions input into tokens
- Masks a subset of tokens
- Reconstructs masked content from visible tokens
- Learns robust representations without labels

### Bilinear Factorization
Decomposition that captures interactions between two sets of factors while reducing parameter complexity. In NERVE, it preserves network identity while enabling efficient embedding of heterogeneous FC patches.

## Research Implications

1. **Domain-Specific Inductive Biases Matter**: Simply applying computer vision techniques to neuroimaging data is suboptimal. Incorporating brain network organization significantly improves performance.

2. **Self-Supervised Learning for Connectomics**: MAE-based approaches hold promise for learning from the vast amounts of unlabeled rs-fMRI data.

3. **Cross-Cohort Transfer**: Network-aware representations generalize better across different populations and scanning protocols.

## Related Concepts
- Resting-state fMRI analysis
- Brain network parcellation (Yeo networks, Schaefer atlas)
- Self-supervised learning for neuroimaging
- Graph neural networks for brain connectivity
- Developmental neuroscience
- Psychopathology prediction

## Activation Triggers
- NERVE tokenization
- brain FC representation
- functional connectivity MAE
- bilinear factorization brain
- network-aware brain ML
- rs-fMRI deep learning
- cross-cohort brain prediction
- brain behavior prediction
- psychopathology ML
- connectomics representation learning

## References
- Milecki, L., Hu, Q., Jafrasteh, B., Sabuncu, M.R., Zhao, Q. (2026). "Network-Aware Bilinear Tokenization for Brain Functional Connectivity Representation Learning." arXiv:2605.14048v2
