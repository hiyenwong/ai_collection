---
name: brain-dnn-transformation-alignment
description: >
  Naturality Violation Score (NVS) for brain-DNN alignment beyond object-level
  comparison. Uses category theory to test whether brains and DNNs preserve the
  same transformations among stimuli. Covers approximate naturality, axis-resolved
  alignment analysis, and hierarchy crossover detection. Use when: (1) evaluating
  brain-DNN alignment at the transformation level, (2) comparing neural representations
  across model architectures, (3) analyzing semantic vs low-level visual alignment,
  or (4) designing neuroscience-inspired model evaluation.
  Activation: naturality violation score, NVS, brain-DNN alignment, transformation
  alignment, category theory neuroscience, axis-resolved alignment, hierarchy
  crossover, approximate naturality, brain model comparison.
---

# Brain-DNN Transformation Alignment (NVS)

Based on Kamitani (2026) — arXiv:2605.06420.

## Core Concept

Traditional brain-DNN alignment measures per-stimulus correspondence (encoding
accuracy, RSA, CKA). This paper introduces a **transformation-level** alignment
test: do the brain and model preserve the *same* transformations among stimuli?

## Mathematical Framework

### Approximate Naturality

Inspired by category theory, alignment is formalized as naturality:

```
Brain side:    x ──f──► x'
                  │         │
              φ_brain    φ_model
                  ↓         ↓
Model side:   φ(x)─f'──► φ(x')
```

If the brain and model preserve the same transformation f, the naturality
square approximately commutes:

```
φ_model(f(x)) ≈ f'(φ_brain(x))
```

### Naturality Violation Score (NVS)

NVS quantifies deviation from commutativity, normalized to a permutation null:

```
NVS(f) = ||φ_model(f(x)) - f'(φ_brain(x))|| / E_perm[||...||]
```

- **NVS ≈ 0**: perfect transformation preservation
- **NVS ≈ 1**: no better than random permutation
- **Lower NVS = better alignment** for that transformation axis

## Key Findings

### Hierarchy Crossover

Applied to fMRI (GOD dataset, 5 subjects) + 3 vision DNNs + 3 world-model
proxies:

| Alignment Axis | Best Aligned To | NVS |
|---------------|-----------------|-----|
| **Semantic** (animacy) | High-level visual cortex + deep DNN layers | 0.39 |
| **Mid-level visual** | Mid visual cortex + mid DNN layers | < next-best |
| **Low-level visual** | Early visual cortex + shallow layers | < next-best |

This reveals that alignment is **axis-selective** rather than uniform —
different transformation families align at different depths.

### Dissociation from Traditional Metrics

- NVS captures alignment failures that RSA/CKA cannot resolve
- Encoding/decoding accuracy does not predict NVS
- Alignment is selective over candidate morphism families

## Implementation Workflow

### Step 1: Define Proxy Space

Choose a proxy space W and comparison maps:
- **Proxy**: semantic embeddings (e.g., CLIP, Word2Vec)
- **Maps**: morphisms between stimuli (e.g., animacy gradient, pose rotation)

### Step 2: Compute NVS Per Axis

For each transformation axis f:
1. Apply f to stimuli on brain side → get brain responses
2. Apply f to stimuli on model side → get model activations
3. Measure commutativity deviation
4. Normalize against permutation null distribution

### Step 3: Axis-Resolved Analysis

- Compare NVS across multiple axes (semantic, spatial, temporal)
- Identify which brain regions align with which model layers per axis
- Detect hierarchy crossovers (different axes peak at different depths)

## Practical Applications

### Model Selection
Use NVS to choose DNN architectures that best preserve brain-relevant
transformations for a specific task domain.

### Layer-wise Alignment
Map which DNN layers correspond to which brain areas for different
transformation types — useful for neuroscientific interpretability.

### Proxy Space Design
The method generalizes to any proxy space (world models, symbolic
representations, etc.), enabling richer brain-model comparisons.

## Comparison with Existing Methods

| Method | Granularity | Transformation-aware? | Null model |
|--------|------------|----------------------|------------|
| Encoding accuracy | Per-stimulus | No | None |
| RSA | Geometry | Partial | None |
| CKA | Global similarity | No | None |
| **NVS (this work)** | **Per-axis** | **Yes** | **Permutation null** |

## Common Pitfalls

- **Proxy space quality**: NVS results depend on proxy choice; poor proxies
  yield misleading NVS values
- **Transformation definition**: candidate morphisms must be well-defined
  and meaningful for both brain and model domains
- **Permutation null**: ensure sufficient permutations (≥1000) for stable
  normalization
- **W-less control**: always run anchor-ablation to verify alignment isn't
  driven by trivial correlations

## Activation Keywords

- naturality violation score, NVS, brain-DNN transformation alignment,
  approximate naturality, axis-resolved alignment, hierarchy crossover,
  category theory neuroscience, brain model comparison, transformation
  preservation, semantic alignment
