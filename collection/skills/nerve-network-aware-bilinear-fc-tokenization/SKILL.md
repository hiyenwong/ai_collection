---
name: nerve-network-aware-bilinear-fc-tokenization
description: "NERVE: Network-Aware Representations of Brain Functional Connectivity via Bilinear Tokenization. Self-supervised learning framework for FC representation using network-aware bilinear tokenization in MAE. Partitions FC matrices into intra/inter-network connectivity blocks. Uses structured bilinear factorization to preserve network identity with linear parameter scaling. Evaluated on ABCD, PNC, CCNP cohorts for behavior prediction. Activation: nerve, network-aware fc tokenization, bilinear tokenization brain, brain functional connectivity representation learning, mae functional connectomics, self-supervised brain network, fc matrix tokenization, brain network mae. arXiv: 2605.14048 (May 2026)"
---

# NERVE: Network-Aware Bilinear Tokenization for Brain FC Representation Learning

**arXiv:** 2605.14048 [cs.AI] | **Date:** 2026-05-13
**Authors:** Leo Milecki, Bahram Jafrasteh, Mert R. Sabuncu, Qingyu Zhao (Weill Cornell Medicine, Cornell University)

## Overview

NERVE introduces a domain-informed tokenization strategy for applying Masked Autoencoders (MAEs) to brain functional connectivity (FC) matrices. The key insight: the conceptual analog of spatially neighboring pixels in images is groups of brain regions organized into large-scale functional networks. NERVE partitions FC matrices into patches defined by intra- and inter-network connectivity blocks, then embeds them via structured bilinear factorization.

## Core Problem

FC matrices lack a canonical "patch" definition for MAE tokenization:
- **Region-centric approaches** (BrainMass): treat individual regions as units, mask random rows — ignores network organization
- **Graph-based methods**: operate on node-level embeddings — lose network-level structure
- **Both** treat FC as structurally homogeneous, overlooking the modular organization of brain networks

## NERVE Architecture

### 1. Network-Based Patching

FC matrix X ∈ R^{R×R} is reorganized by grouping R regions into N established functional networks:
- Each patch corresponds to a connectivity block between network pair (N_i, N_j)
- Patches capture both **intra-network** (within-network) and **inter-network** (between-network) connectivity
- This is the functional analog of image patches — groups sharing similar functional dynamics

### 2. Structured Bilinear Tokenization

Key innovation: instead of learning independent embeddings for each network-pair patch:
- Learn **network-specific region embeddings** for each functional network
- Compute patch tokens through **bilinear interactions** between network weights
- Formula: patch_token(i,j) = W_i^T · X_{ij} · W_j (bilinear factorization)

**Advantages:**
- **Parameter efficiency:** Linear O(N) scaling in number of networks instead of O(N²)
- **Network identity preservation:** Each network carries distinct functional role
- **Heterogeneous patch handling:** Works with varying patch dimensions (different network sizes)

### 3. MAE Framework Integration

- Standard transformer-based MAE applied to network-aware tokens
- Random masking of subset of tokens
- Reconstruction of masked content from visible tokens
- Network-aware inductive bias guides what structure the model learns

## Key Findings

### Evaluation Setup
- **Datasets:** Three large-scale developmental cohorts
  - ABCD (Adolescent Brain Cognitive Development)
  - PNC (Philadelphia Neurodevelopmental Cohort)
  - CCNP (Connectomes Related to Human Development)
- **Task:** Behavior and psychopathology prediction from FC representations

### Results
1. **Outperforms structurally agnostic MAE variants** across all cohorts
2. **More stable and transferable representations**, particularly in cross-cohort evaluation
3. **Superior to graph-based self-supervised baselines**
4. **Ablation studies confirm:**
   - Bilinear network embedding is critical for performance
   - Anatomically grounded parcellation is essential
   - Network-aware tokenization > random/region-based tokenization

## Technical Details

### Mathematical Formulation

Given FC matrix X^{(i)} for subject i:
1. **Partition:** Group regions into functional networks {N_1, ..., N_{N_n}}
2. **Patch extraction:** Each patch X_{jk} corresponds to connectivity between networks j and k
3. **Bilinear tokenization:** t_{jk} = W_j^T · X_{jk} · W_k
   - W_j: learnable network-specific weight matrix for network j
   - Preserves network identity in token computation
4. **MAE:** Standard transformer encoder-decoder with random masking
5. **Reconstruction:** Reconstruct masked FC patches from visible tokens

### Parameter Scaling

| Approach | Parameters | Scaling |
|----------|-----------|---------|
| Independent patch embeddings | O(N² × d²) | Quadratic in networks |
| NERVE bilinear factorization | O(N × d × r) | Linear in networks |

Where N = number of networks, d = embedding dimension, r = region count per network.

## When to Use NERVE

### Best Fit Scenarios
- **Self-supervised learning on resting-state fMRI FC matrices**
- **Cross-cohort transfer learning** (representations that generalize across datasets)
- **Behavioral/clinical prediction** from functional connectivity
- **When domain structure matters** — leveraging known brain network organization

### vs. Alternatives

| Method | Uses Network Structure | Parameter Efficiency | Cross-Cohort Transfer |
|--------|----------------------|---------------------|----------------------|
| BrainMass (region-centric) | No | Medium | Limited |
| Graph-based SSL | Partial | Medium | Moderate |
| **NERVE** | **Yes** | **High (linear)** | **Strong** |

## Implementation Guidelines

### Key Design Choices
1. **Functional network parcellation:** Use established atlases (Yeo 7/17 networks, etc.)
2. **Bilinear factorization:** Learn network-specific weights, not patch-specific
3. **MAE masking ratio:** Standard MAE settings (75% masking typically works)
4. **Transformer architecture:** Standard encoder-decoder, tokens are network-pair based

### Integration with Existing Pipelines
- Works with any FC matrix preprocessing pipeline
- Compatible with standard neuroimaging tools (fMRIPrep, CONN, etc.)
- Can replace the tokenization step in existing MAE frameworks

## Related Skills

- **brain-dit-fmri-foundation-model**: fMRI foundation model for multi-state prediction
- **multimodal-brain-connectivity-gnn**: Multi-modal brain connectivity with GNNs
- **functional-connectivity-graph-neural-networks**: FC analysis with GNNs
- **meta-learning-in-context-brain-decoding**: Training-free cross-subject brain decoding
- **brain-graph-neural**: GNN methods for brain connectivity analysis
- **tablet-fmri-tokenization-transformer**: fMRI volume tokenization with pre-trained transformers

## Dependencies

```bash
pip install torch transformers nibabel numpy scikit-learn
```

## Notes

- Published under arXiv.org perpetual non-exclusive license
- The bilinear tokenization is the core innovation — replaces quadratic parameter growth with linear scaling
- Cross-cohort evaluation is the most compelling evidence of representation quality
- Anatomically grounded parcellation is essential — arbitrary region ordering doesn't work
- This work highlights the broader principle: incorporating domain-specific structural priors into self-supervised learning significantly improves representation quality for neuroimaging data
