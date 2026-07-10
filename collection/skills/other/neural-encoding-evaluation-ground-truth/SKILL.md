---
name: neural-encoding-evaluation-ground-truth
description: "Systematic audit methodology for EEG foundation model interpretability. Decomposes what models learn, what they use, and how much can be explained using layer-wise ridge probing, LEACE cross-covariance erasure, and transparent classifiers. Use when: EEG foundation model analysis, neural encoding evaluation, interpretability audit, feature causality analysis, brain signal representation analysis, EEG feature lexicon, LEACE analysis."
---

# Neural Encoding Evaluation: Ground-Truth Approximation

Systematic methodology for auditing what EEG foundation models capture from human brain signals.

## Paper

- **Title**: What Do EEG Foundation Models Capture from Human Brain Signals?
- **arXiv**: 2605.11410
- **Authors**: Ling Tang, Qian Chen, Jilin Mei, Houshi Xu, Quanshi Zhang et al.
- **Date**: 2026-05-12
- **Categories**: cs.AI

## Overview

Clinical EEG analysis uses hand-crafted features (band power, connectivity, complexity). Modern EEG foundation models learn directly from raw signals via self-supervised pretraining, matching or outperforming feature-engineered baselines. This paper systematically audits **what** these models learn, **what** they use, and **how much** can be explained.

## Key Research Questions

The audit decomposes into three sub-questions:

| Question | Method |
|----------|--------|
| **What does the model learn?** | Layer-wise ridge probing |
| **What does the model use?** | LEACE-style cross-covariance subspace erasure |
| **How much can be explained?** | Transparent classifier vs. random-feature baseline |

## Methodology

### 1. Layer-Wise Ridge Probing

- Train linear probes on each layer's representations
- Measure how well each known EEG feature can be decoded
- Identifies which features are encoded at which depth

### 2. LEACE-Style Cross-Covariance Erasure

- Linear Erasure of All Covariance Evidences
- Removes feature-related information from representations
- Tests whether the feature is **causal** to model predictions

### 3. Feature Classification

Features are classified as:
- **Representation-Causal (RC)**: Feature is both encoded AND used for predictions
- **Encoded-Only**: Feature is encoded but not causally used

## Audit Scope

| Dimension | Details |
|-----------|---------|
| Models | CSBrain, CBraMod, LaBraM (3 foundation models) |
| Tasks | MDD, Stress, ISRUC-Sleep, TUSL, Siena (5 clinical tasks) |
| Feature Lexicon | 6 families, 63 features |

**Total units audited**: 945 (model × task × feature)

## Key Results

### Causality Breakdown

- **648/945 (68.6%)**: Representation-causal features
- **199/945 (21.1%)**: Encoded-only features

### Universal Features

- **50 features** qualify as universal candidates (strong RC support across all 3 architectures in 2+ tasks)
- Frequency-domain features dominate
- Other 5 feature families each contribute substantial causal mass

### Recovery Analysis

- Confirmed features recover **79.3%** of foundation model's advantage over random baseline
- **Task gradient** of recovery:
  - MDD ≈ 99% (near ceiling — almost fully explained by lexicon)
  - Stress ≈ 56% (harder task — significant residual for future concept discovery)

## Implementation Pattern

```
[EEG Foundation Model] → [Layer Representations]
                              ↓
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
    [Ridge Probing]    [LEACE Erasure]   [Classification]
              ↓               ↓               ↓
    [Encoded Features] [Causal Features] [Recovery Score]
              ↓               ↓               ↓
              └───────────────┼───────────────┘
                              ↓
                    [Unified Audit Report]
```

## Applications

- Interpretable EEG foundation model development
- Clinical validation of brain signal AI models
- Feature engineering for brain-computer interfaces
- Understanding representational alignment in neural AI
- Identifying gaps in current EEG feature lexicons

## Key Insights

1. **Majority Causal**: Most learned features are causally used (68.6% RC)
2. **Task Difficulty Gradient**: Easy tasks are well-explained; hard tasks reveal unknown representations
3. **Frequency Dominance**: Frequency features dominate but other families matter significantly
4. **Residual Discovery**: The unexplained portion of hard tasks (e.g., Stress at 44%) is a concrete target for future concept discovery
5. **Architecture Convergence**: 50 universal features show convergence across different architectures

## Related Concepts

- EEG foundation models (CSBrain, CBraMod, LaBraM)
- LEACE (Linear Erasure of All Covariance Evidences)
- Ridge regression probing
- Neural encoding models
- Clinical EEG features (band power, connectivity, complexity)
- Representational alignment

## Pitfalls

- Hand-crafted features may not capture all model-learned representations
- LEACE only removes linear relationships — nonlinear encodings may persist
- Recovery analysis depends on classifier choice and baseline
- Task-dependent: what's explained varies significantly by clinical domain

## References

- arXiv: 2605.11410
- Related: neural encoding evaluation, EEG interpretability, foundation model audit

## Notes for Agents

When using this methodology:
1. Always run all three methods (probing, erasure, classification) together
2. The task gradient is important — don't generalize from one task to all
3. The 50 universal features are a validated starting point for new EEG analysis
4. The residual (unexplained portion) of hard tasks is where new discoveries live
5. Compare against random-feature baseline to avoid overclaiming
