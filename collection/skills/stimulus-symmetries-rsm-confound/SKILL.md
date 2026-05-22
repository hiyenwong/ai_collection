---
name: stimulus-symmetries-rsm-confound
description: "Systematic analysis of how stimulus symmetries (spatial, temporal, categorical) can create misleadingly high Representational Similarity Analysis (RSA) scores between brain and model representations. Provides diagnostic tools to detect symmetry artifacts in brain-DNN alignment studies. Activation: RSA confounds, stimulus symmetries, representational similarity, brain-DNN alignment artifacts."
---

# Stimulus Symmetries Confound RSA: A Systematic Analysis

**arXiv:** [2605.21324](https://arxiv.org/abs/2605.21324) (Submitted May 21, 2026)
**Categories:** q-bio.NC, cs.LG, cs.NE, stat.ML

## Core Problem

Representational Similarity Analysis (RSA) is widely used to compare brain and model representations, but it can be systematically **inflated** by unaccounted stimulus symmetries.

## Key Findings

### 1. Three Types of Symmetries that Inflate RSA

- **Spatial symmetries**: Mirror images, rotations, or translations that create spurious similarity between dissimilar representations
- **Temporal symmetries**: Repeated patterns or periodic structures in stimulus sequences that inflate correlation
- **Categorical symmetries**: Shared category-level structure that masks fine-grained representational differences

### 2. Systematic Inflation Mechanism

Stimulus symmetries create **shared structure** in representational dissimilarity matrices (RDMs) that is not driven by genuine neural coding similarity, leading to inflated RSA scores.

### 3. Diagnostic Tools

The paper provides diagnostic methods to detect when stimulus symmetries are artifactually inflating RSA:
- Permutation tests controlling for symmetry structure
- Partial correlation approaches to factor out symmetry-driven similarity
- Visualization methods for identifying symmetry artifacts in RDMs

## Implications

- Many reported high brain-model RSA scores may be partially or fully driven by stimulus symmetries
- Re-evaluation of published RSA results may be needed
- Best practices for stimulus set design to minimize symmetry confounds

## Activation Keywords

- RSA confounds
- stimulus symmetries
- representational similarity analysis
- brain-DNN alignment artifacts
- RDM inflation
- permutation test RSA
- partial correlation RSA
- neural representational geometry

## Related Skills

- cross-species-rsa-brain-alignment
- untrained-cnns-match-backpropagation-v1-rsa
- target-space-recovery-profiles-brain-alignment
