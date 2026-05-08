---
name: brain-dnn-transformation-alignment
description: >
  Category-theoretic framework for brain-DNN alignment via approximate naturality.
  Tests whether brains and DNNs preserve the same stimulus transformations, not just
  per-stimulus correspondence. Introduces Naturality Violation Score (NVS) for
  axis-resolved alignment analysis. Use when: (1) comparing brain and DNN representations,
  (2) going beyond RSA/CKA/Brain-Score for alignment, (3) studying transformation
  preservation across systems, (4) category theory in neuroscience.
  Trigger: brain-DNN alignment, naturality violation, NVS, transformation preservation,
  category theory neuroscience, representational alignment, cospan alignment.
---

# Brain-DNN Alignment via Approximate Naturality

Based on Kamitani (2026), arXiv:2605.06420.

## Core Insight

Existing alignment metrics (RSA, CKA, encoding/decoding accuracy) test whether brain
and DNN assign similar codes to the same stimuli. This framework asks a deeper question:
**do they preserve the same transformations** among stimuli?

## Naturality Square

For brain space B, model space M, and proxy space W:

```
η ◦ F_B(r) = F_M(r) ◦ η
```

Where:
- `r : s → s'` = candidate stimulus transformation
- `F_B(r) : B → B`, `F_M(r) : M → M` = linear operators realizing r on each side
- `η : B → M` = translator (linear decoder), `η' : M → B` = translator (linear encoder)

The two paths should approximately commute: propagate-then-translate ≈ translate-then-propagate.

## Operational Implementation via Cospan

The naturality square is realized through three learned linear maps:

1. **Φ_B : W → B** — world-to-brain map (Ridge regression)
2. **Φ_M : W → M** — world-to-model map (Ridge regression)
3. **η : B → M**, **η' : M → B** — translators between systems

Each candidate morphism is parameterized by ΔW = F_W(s') - F_W(s) ∈ W.

The operational identity becomes:
```
Φ_M(ΔW) = η(Φ_B(ΔW))
```

## Naturality Violation Score (NVS)

```
NVS_η  = ||η(Φ_B(ΔW)) - Φ_M(ΔW)|| / E_π[||η(Φ_B(ΔW)) - Φ_M(ΔW)||]
NVS_η' = ||η'(Φ_M(ΔW)) - Φ_B(ΔW)|| / E_π[||η'(Φ_M(ΔW)) - Φ_B(ΔW)||]
NVS    = ½(NVS_η + NVS_η')
```

- **NVS = 0**: perfect commutativity (transformation preserved)
- **NVS = 1**: permutation null baseline (chance level)
- **NVS < 1**: evidence for structure relative to null

## World Model Proxy Space (W)

The choice of W determines which transformations can be tested:

| Proxy | Captures | Example |
|-------|----------|---------|
| CLIP-text | Language-grounded semantics | image captions → text embeddings |
| DINOv2 | Self-supervised visual structure | image → visual features |
| DreamSim | Human perceptual similarity | image → perceptual embedding |

## Axis-Resolved Analysis (CAV-based)

Decompose ΔW along Concept Activation Vector (CAV) directions:
```
ΔW_a = ⟨ΔW, v_a⟩ · v_a
```

This yields NVS_a (e.g., NVS_animacy) — testing whether a specific semantic axis
is preserved across brain and model.

## Key Empirical Findings (GOD Dataset)

**Hierarchy Crossover**: Different transformation axes align at different brain regions
and DNN layers:

| Axis Level | Brain Region | DNN Layers | Best NVS |
|-----------|-------------|------------|----------|
| Low-level (luminance, spatial freq) | V1 | Shallow (L1-L4) | ~0.37 |
| Mid-level (curvilinearity, texture) | V2-V4 | Middle (L3-L6) | ~0.40-0.58 |
| Semantic (animacy, real size) | HVC | Deep (L6-L8) | 0.19-0.45 |

**Animacy** is the strongest axis: NVS_animacy = 0.39 (vs. 1.0 null baseline),
consistent with ventral stream organization.

## Why NVS > Traditional Metrics

| Metric | Tests | Limitation |
|--------|-------|------------|
| Encoding/Decoding r | Per-stimulus correspondence | Misses transformation structure |
| RSA | Pairwise similarity | Single scalar, no axis resolution |
| CKA | Global geometry alignment | Collapses factor-level differences |
| Procrustes | Optimal rotation alignment | Cannot localize which factors align |
| **NVS** | **Per-transformation preservation** | **Axis-resolved, null-normalized** |

In synthetic PoC: CCA returns ≈0.99 for models preserving disjoint factor subsets,
while NVS cleanly separates them per axis (0.02 vs 0.57).

## Implementation Pipeline

### Step 1: Define Spaces
- B: brain activity (fMRI voxels, neural recordings)
- M: DNN layer activations
- W: proxy embedding space (CLIP, DINOv2, DreamSim)

### Step 2: Fit Linear Maps
- Φ_B, Φ_M: Ridge regression from W to B/M
- η, η': Ridge regression between B and M
- Fit on training stimulus pairs

### Step 3: Compute NVS
- For each test pair (s, s'), compute ΔW
- Evaluate both paths around the naturality square
- Compute permutation-normalized residuals

### Step 4: Axis Decomposition
- Project ΔW onto CAV directions v_a
- Compute NVS_a for each concept axis
- Identify hierarchy crossover patterns

## Code Skeleton

```python
import numpy as np
from sklearn.linear_model import Ridge

# Fit translators
eta = Ridge(alpha=1.0).fit(B_train, M_train)
eta_inv = Ridge(alpha=1.0).fit(M_train, B_train)

# Fit world-to-space maps
phi_B = Ridge(alpha=1.0).fit(W_train, B_train)
phi_M = Ridge(alpha=1.0).fit(W_train, M_train)

# Compute NVS for a set of transformations
def compute_nvs(delta_W, eta, eta_inv, phi_B, phi_M, n_perm=1000):
    # Direct paths
    direct_M = phi_M.predict(delta_W)
    via_B = eta.predict(phi_B.predict(delta_W))
    
    # Residual
    residual = np.linalg.norm(via_B - direct_M, axis=1).mean()
    
    # Permutation null
    perm_residuals = []
    for _ in range(n_perm):
        idx = np.random.permutation(len(delta_W))
        perm_residuals.append(
            np.linalg.norm(via_B - phi_M.predict(delta_W[idx]), axis=1).mean()
        )
    
    return residual / np.mean(perm_residuals)
```

## Limitations

- n=5 subjects on single dataset (GOD)
- Proxy space W is a limited approximation of true world model
- Linear maps may not capture nonlinear structure
- Not enforcing strict functorial properties (composition, identity)
- CAV-based axes depend on proxy viability

## Related Concepts

- Category theory (natural transformations, functors)
- Cospan diagram (W → B, W → M)
- Linear representation hypothesis
- Concept Activation Vectors (CAVs)
- Brain-Score, RSA, CKA (existing metrics)
- Equivariant neural networks
