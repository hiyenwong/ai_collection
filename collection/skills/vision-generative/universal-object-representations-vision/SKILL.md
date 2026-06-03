---
name: universal-object-representations-vision
description: >
  Decomposition methodology for identifying universal vs model-specific dimensions in
  vision model representations across 162 diverse models. Universal dimensions are more
  interpretable, driven by conceptual image properties, and better predict macaque IT
  activity and human similarity judgments. arXiv:2605.13675.
category: neuroscience
tags: [universal-representations, vision-models, non-negative-decomposition,
       macaque-IT, representational-similarity, model-convergence, semantic-vision]
related_skills:
  - face-perception-inverse-generative
  - neuroscience-of-transformers
  - cross-modal-convergence-dispersion
  - neural-encoding-evaluation-ground-truth
activation_keywords:
  - universal object representations vision
  - vision model convergence dimensions
  - non-negative dimension decomposition vision
  - macaque IT prediction vision models
  - model similarity structure vision
  - conceptual image properties universality
---

# Universal Object Representations Across Vision Models

**Paper**: *Characterizing Universal Object Representations Across Vision Models*
**Authors**: Florian P. Mahner, Johannes Roth, Ka Chun Lam, Michael F. Bonner, Francisco Pereira, Martin N. Hebart
**arXiv**: 2605.13675 (May 13, 2026)
**Category**: cs.CV, cs.LG, q-bio.NC

## Overview

Decomposes object similarity structure of 162 diverse vision models into non-negative
dimensions, identifying which dimensions are **universal** (reappear across many models)
vs **model-specific**. Universal dimensions are more interpretable and better predict
biological vision.

## Core Problem

DNNs trained with different architectures, objectives, and datasets converge on similar
visual representations. What properties do they converge on? What drives convergence?

## Key Innovation: Non-Negative Dimension Decomposition

1. Decompose each model's object similarity structure into non-negative dimensions
2. Count how often each dimension reappears across the 162 models
3. **Universal dimensions** = high cross-model frequency
4. **Model-specific dimensions** = low frequency, unique to particular setups

## Scale

- **162 diverse vision models** across architectures, objectives, datasets
- Non-negative matrix factorization of similarity structures
- Frequency analysis of dimension recurrence

## Key Findings

1. **Universal dimensions are more interpretable** - driven by conceptual image properties
2. **Semantic content drives universality** - interpretability is an implicit factor
3. **Not explained by training variables** - architecture, objective, data, size, performance
   do NOT explain universal dimension emergence
4. **Biological relevance**: Models with more universal dimensions better predict:
   - Macaque IT neural activity
   - Human similarity judgments
5. **Universality = biological alignment**

## Core Principle

Convergent representations reflect fundamental computational constraints of vision,
not shared training procedures. **More universal = more brain-like**.

## Implementation Pattern

```python
# Conceptual pipeline
# 1. Collect representations from diverse models on same stimulus set
# 2. Compute pairwise similarity (RSA) for each model
# 3. Apply NMF to find non-negative dimensions
# 4. Count dimension frequency across models
# 5. Identify universal (high-freq) vs specific (low-freq)
# 6. Validate against biological neural data
```

## Workflow for Agents

### When to apply
1. Analyzing convergence across multiple AI model architectures
2. Evaluating how brain-like a vision model is
3. Understanding universal vs idiosyncratic representations
4. Designing model ensembles capturing diverse dimensions

### Steps
1. Collect diverse model representations on shared stimuli
2. Compute RSA matrices per model
3. Decompose into non-negative dimensions (NMF)
4. Cross-model frequency analysis
5. Validate universal dimensions against neural recordings

## Pitfalls

1. **Dimension matching is non-trivial** - may be permuted or rotated across models
2. **Non-negative constraint matters** - standard PCA/SVD miss parts-based structure
3. **Stimulus set bias** - must be diverse and representative
4. **Correlation not causation** - universality correlates with but doesn't prove alignment

## Applications

1. Model selection - choose universal models for brain prediction
2. Representation analysis - understand what makes representations good
3. Neuroscience hypothesis generation - fundamental computational constraints
4. AI interpretability - universal dimensions are more interpretable

## References

- arXiv:2605.13675 (Mahner et al., 2026)
- Kriegeskorte et al. (2008): Representational Similarity Analysis
- Yamins & DiCarlo (2016): Goal-driven deep learning for sensory cortex
