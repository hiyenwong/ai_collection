---
name: brain-dnn-transformation-alignment
description: >
  Category-theoretic framework for brain-DNN alignment via Naturality Violation Score (NVS).
  Evaluates whether brains and DNNs preserve the same representational transformations across
  stimulus conditions, going beyond static representational similarity.
  Use when: (1) analyzing brain-DNN alignment beyond RSA/CCA, (2) evaluating transformation
  preservation in neural networks, (3) category theory approaches to neuroscience,
  (4) naturality scores for model-brain comparison, (5) representational dynamics analysis.
  Trigger words: NVS, naturality violation, brain-DNN transformation, representational dynamics,
  category theory neuroscience, transformation alignment, Kamitani lab, brain model alignment.
---

# Brain-DNN Transformation Alignment (NVS)

Category-theoretic methodology for evaluating whether brains and DNNs preserve the same
representational transformations, not just static alignment.

## Core Concept

Traditional RSA measures static representational similarity at each layer. NVS asks:
**do brains and DNNs transform representations in the same way** when stimulus conditions change?

A low NVS means the DNN's transformation structure is "natural" (commutes) with the brain's.

## Mathematical Framework

### Naturality Square

Given two conditions A → B (e.g., original vs. augmented images):

```
    R_brain(A) ──T_brain──► R_brain(B)
        │                       │
     φ_A│                    φ_B│
        ▼                       ▼
    R_model(A) ──T_model──► R_model(B)
```

The square commutes (naturality) when: φ_B ∘ T_brain = T_model ∘ φ_A

### Naturality Violation Score (NVS)

NVS = ||φ_B(T_brain(R_brain(A))) - T_model(φ_A(R_brain(A)))||

- NVS ≈ 0: DNN transformations mirror brain transformations
- NVS >> 0: DNN and brain transform differently despite similar representations

## Computation Pipeline

1. **Extract representations**: Get R_brain(condition) and R_model(condition) for multiple conditions
2. **Define transformations**: T_brain and T_model map between condition representations
3. **Learn alignment maps**: φ_A, φ_B via linear regression between brain/model representations
4. **Compute NVS**: Measure how far the naturality square deviates from commuting
5. **Statistical testing**: Compare against null distributions (permuted labels, shuffled features)

## Interpretation

| NVS Level | Meaning |
|-----------|---------|
| Low (~0.01) | DNN transformations faithfully mirror brain dynamics |
| Medium (~0.1) | Partial alignment; some transformations diverge |
| High (>0.5) | Representations may align statically but transform differently |

## Key Insight from Paper

Models can achieve high RSA while having high NVS — they match representations statically
but use fundamentally different transformation dynamics. This reveals misalignment invisible
to standard RSA analysis.

## Practical Applications

- **Model selection**: Choose architectures that minimize NVS for brain-like AI
- **Architecture analysis**: Compare CNNs, ViTs, and SNNs on transformation alignment
- **Training intervention**: Regularize NVS during training for brain-aligned models
- **Causal probing**: Test which architectural components reduce transformation violations

## arXiv Reference

- Paper: "Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?"
- Authors: Yukiyasu Kamitani
- ID: arXiv:2605.06420v1
- Category: q-bio.NC
