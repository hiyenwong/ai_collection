---
name: naturality-violation-score
description: "Category-theory-based brain-DNN alignment methodology using Naturality Violation Score (NVS). Shifts alignment assessment from per-stimulus correspondence to preservation of candidate transformations. Activation: brain-DNN alignment, naturality violation, RSA critique, representational alignment, transformation alignment, brain model comparison, fMRI alignment"
---

# Naturality Violation Score (NVS) for Brain-DNN Alignment

## Overview

The Naturality Violation Score (NVS) is a methodology for assessing brain-deep neural network (DNN) alignment inspired by category theory. Instead of measuring per-stimulus correspondence or stimulus-set geometry (like RSA/CKA), it tests whether brain and model **preserve the same candidate transformations** among stimuli.

## Activation Keywords

- brain-DNN alignment
- naturality violation
- NVS alignment
- transformation alignment
- representational similarity critique
- brain model comparison
- fMRI-DNN alignment
- category theory neuroscience

## Key Problem

Standard alignment metrics (RSA, CKA, encoding/decoding accuracy) collapse multi-dimensional alignment into aggregate scalars, missing complementary alignment failures. They test whether the brain and model represent the same stimuli similarly, but not whether they transform stimuli in the same way.

## Core Methodology

### 1. Naturality Square

The fundamental question is formalized as a naturality square:

```
Brain(X) ──Brain(f)──> Brain(Y)
  │                       │
  T                       T
  ↓                       ↓
Model(X) ──Model(f)──> Model(Y)
```

If this square approximately commutes, the brain and model preserve the same transformations under the comparison map T.

### 2. NVS Computation Steps

1. **Define proxy space W**: An intermediate embedding space (e.g., world-model embeddings, semantic attributes)
2. **Select morphism family F**: Candidate transformations between stimuli (e.g., animacy, scene complexity)
3. **Compute deviation from commutativity**: For each morphism f in F, measure:
   - Path A: Brain -> Transform -> Translate to model
   - Path B: Translate to model -> Transform in model
4. **Normalize against permutation null**: Score is normalized relative to random permutation baseline (1.0 = random, 0.0 = perfect alignment)

### 3. Axis-Resolved Analysis

Rather than a single aggregate score, NVS decomposes alignment per semantic axis:
- Animacy, scene type, color, orientation, etc.
- Each axis gets its own NVS score
- Reveals **hierarchy crossover**: semantic axes align deeper in both brain and DNNs, while low-level axes align earlier

### 4. Comparison to Existing Methods

| Method | What it measures | Limitation |
|--------|-----------------|------------|
| RSA | Representational similarity | Insensitive to transformation preservation |
| CKA | Kernel-based alignment | Aggregate scalar, axis-agnostic |
| Encoding/Decoding | Predictive accuracy | Doesn't test structural preservation |
| **NVS** | **Transformation preservation** | **Axis-resolved, proxy-explicit** |

### 5. Validation Controls

- **W-less anchor-ablation**: Remove proxy space to test if alignment is proxy-dependent
- **Permutation null**: Random shuffle to calibrate score range
- **Dissociation tests**: Show NVS captures failures RSA/CKA miss

## Application Pipeline

```
1. Collect neural data (fMRI, EEG, single-unit)
2. Extract DNN activations at multiple layers
3. Define proxy space W (e.g., CLIP embeddings, world-model states)
4. Define morphism family F (semantic axes, transformations)
5. Compute NVS per axis per layer
6. Compare axis-resolved alignment profiles
7. Validate with controls (permutation, ablation)
```

## Key Findings from the Paper

- **Hierarchy crossover**: Semantic axes (animacy) align most strongly toward higher visual cortex (HVC) and deeper DNN layers
- **Complementary failures**: NVS detects alignment failures that RSA/CKA miss
- **Selective alignment**: Alignment is selective over morphism families, not uniform
- **Normalized scoring**: NVS = 0.39 for animacy vs 1.0 permutation null shows meaningful alignment

## Python Implementation Sketch

```python
import numpy as np

def compute_nvs(brain_reps, model_reps, proxy_reps, morphisms, n_permutations=1000):
    """Compute Naturality Violation Score for each morphism."""
    # Translate brain -> model space via linear mapping
    T = np.linalg.lstsq(brain_reps, model_reps, rcond=None)[0]
    
    nvs_scores = {}
    for name, (idx_a, idx_b) in morphisms.items():
        # Path A: brain -> transform -> translate
        path_a = T @ brain_reps[idx_b]
        
        # Path B: translate -> transform in model
        translated_a = T @ brain_reps[idx_a]
        path_b = model_reps[idx_b]
        
        # Commutativity violation
        violation = np.linalg.norm(path_a - path_b)
        
        # Permutation null distribution
        null_violations = []
        for _ in range(n_permutations):
            perm_idx = np.random.permutation(len(brain_reps))
            null_violations.append(
                np.linalg.norm(T @ brain_reps[perm_idx[idx_b]] - model_reps[idx_b])
            )
        
        # Normalize
        nvs = violation / np.mean(null_violations)
        nvs_scores[name] = nvs
    
    return nvs_scores
```

## When to Use

- Comparing brain representations to DNN layers
- Evaluating whether a model preserves brain-like transformations
- Testing alignment beyond stimulus-level similarity
- Diagnosing where in the processing hierarchy alignment breaks down

## Source

arXiv: 2605.06420 - "Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?" by Yukiyasu Kamitani (2026-05-07)

## Related Skills

- decoding-encoding-alignment-critique
- brain-dnn-transformation-alignment
- untrained-cnns-backprop-v1-rsa
