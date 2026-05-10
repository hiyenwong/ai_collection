---
name: naturality-violation-score
description: "Naturality Violation Score (NVS) methodology for brain-DNN alignment assessment using category theory. Introduces approximate naturality as a new framing: whether brains and deep neural networks preserve the same stimulus transformations, not just per-stimulus sameness. Use when: (1) evaluating brain-DNN alignment beyond RSA/CKA/encoding accuracy, (2) analyzing which stimulus transformations are jointly preserved across neural and artificial systems, (3) comparing representational geometries along specific semantic or visual axes (animacy, luminance, etc.), (4) implementing the cospan framework with World Model proxies (CLIP-text, DINOv2, DreamSim), (5) studying hierarchical crossover patterns in visual cortex alignment. Trigger words: NVS, naturality violation, brain-DNN alignment, category theory alignment, approximate naturality, cospan framework, transformation preservation, axis-resolved alignment."
---

# Naturality Violation Score (NVS)

Category-theoretic framework for assessing brain-DNN alignment through **approximate naturality** — whether two systems preserve the same candidate transformations among stimuli, not just per-stimulus sameness.

Source: Kamitani (2026), *Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?* (arXiv:2605.06420)

## Core Idea

Traditional alignment metrics (RSA, CKA, encoding/decoding accuracy) test whether brain and model assign similar codes to the same stimuli individually. NVS instead asks: **when stimuli change in a particular way, do both systems change their representations compatibly?**

Formalized via the naturality square:

```
η ∘ F_B(r) = F_M(r) ∘ η
```

Where:
- **B** = brain space (fMRI voxel patterns, neural recordings)
- **M** = model space (DNN layer activations)
- **r: s → s'** = candidate stimulus change (morphism)
- **F_B(r), F_M(r)** = how the change manifests in each system
- **η: B → M, η': M → B** = linear translators (decoders/encoders)

## The Cospan Framework

Three spaces connected via a proxy embedding **FW: Stim → W**:

```
    W (proxy space)
   / \
 ΦB   ΦM
 /     \
B ----- M
   η, η'
```

- **W** = World Model proxy embedding space (CLIP-text, DINOv2, DreamSim)
- **ΦB: W → B**, **ΦM: W → M** = world-to-brain/model maps (Ridge regression)
- Candidate morphisms parameterized by **∆W = FW(s') − FW(s) ∈ W**

## NVS Computation

### Step 1: Fit linear maps

```python
# World-to-brain and world-to-model (Ridge regression)
ΦB = fit_ridge(FW(stimuli), B_responses)
ΦM = fit_ridge(FW(stimuli), M_activations)

# Cross-system translators
η = fit_ridge(B_responses, M_activations)
η_prime = fit_ridge(M_activations, B_responses)
```

### Step 2: Compute per-direction residuals

For each test pair (s, s') with ∆W = FW(s') − FW(s):

```
NVS_η = E[||η(ΦB(∆W)) − ΦM(∆W)||₂] / E_π[||η(ΦB(∆W)) − ΦM(∆W)||₂]
NVS_η' = E[||η'(ΦM(∆W)) − ΦB(∆W)||₂] / E_π[||η'(ΦM(∆W)) − ΦB(∆W)||₂]
NVS = (NVS_η + NVS_η') / 2
```

Where **E_π** is expectation over permutations that destroy cross-space pairing while preserving marginal geometry.

### Interpretation

| NVS Value | Meaning |
|-----------|---------|
| 0.0 | Perfect commutativity (full naturality) |
| < 1.0 | Better than chance (structure preserved) |
| 1.0 | Permutation null baseline (no structure) |
| > 1.0 | Worse than chance |

## Two Regimes

### Full-Vector Regime (NVS_full)
Uses complete ∆W vectors → single global score over all directions in W.

### Axis-Resolved Regime (NVS_a)
Projects ∆W onto concept-axis directions (CAVs):

```
∆W_a = ⟨∆W, v_a⟩ · v_a  (v_a = unit CAV direction for axis a)
```

Yields **NVS_animacy**, **NVS_luminance**, etc. — localizes *which* transformations are preserved.

## Key Empirical Findings (GOD Dataset)

### Hierarchy Crossover
Different transformation axes align at different levels of the visual hierarchy:

| Axis Type | Best ROI | Best Layer | NVS |
|-----------|----------|------------|-----|
| Luminance (low-level) | V1 | L4 (ResNet) | 0.37 |
| Spatial frequency | V1 | L4 (ResNet) | 0.32 |
| Texture energy (mid) | V1 | L2 (AlexNet) | 0.28 |
| Curvilinearity (mid) | V2 | L4 (AlexNet) | 0.52 |
| Real size (semantic) | HVC | L7 (ResNet) | 0.45 |
| **Animacy** (semantic) | **HVC** | **L6 (ResNet)** | **0.19** |

Animacy is the strongest-aligned axis (NVS = 0.39 pooled across all cells vs 0.52–0.72 for other axes), consistent with ventral stream organization.

### Proxy Comparison
- **DreamSim** (human perceptual similarity): best overall NVS (~0.58)
- **CLIP-text** (language-grounded semantics): moderate (~0.70)
- **DINOv2** (self-supervised visual): weakest (~0.85)

## Advantages Over Traditional Metrics

| Metric | What It Tests | What It Misses |
|--------|---------------|----------------|
| Encoding accuracy | Per-stimulus prediction | Transformation structure |
| RSA | Pairwise similarity geometry | Which specific transforms preserved |
| CKA | Global subspace alignment | Axis-selective correspondence |
| **NVS** | **Transformation preservation per axis** | — |

### Synthetic Proof-of-Concept
In a 5-factor toy world (position, scale, rotation, color):
- **M_pos** (keeps position only) and **M_obj** (keeps object features only) both score ~0.99 on CCA — indistinguishable
- Per-axis NVS cleanly separates them: M_pos has NVS≈0.02 on {x,y} but ≈0.57 on {scale,θ,color}; M_obj shows the inverse

## Implementation Workflow

```python
import numpy as np
from sklearn.linear_model import Ridge

def compute_nvs(FW_stim, B_data, M_data, n_permutations=1000):
    """
    Compute NVS for brain-DNN alignment.
    
    Args:
        FW_stim: (N, d_W) proxy embeddings for N stimuli
        B_data: (N, d_B) brain responses
        M_data: (N, d_M) model activations
        n_permutations: number of permutation null samples
    
    Returns:
        NVS: symmetry-averaged naturality violation score
    """
    # Fit maps
    phi_B = Ridge().fit(FW_stim, B_data)
    phi_M = Ridge().fit(FW_stim, M_data)
    eta = Ridge().fit(B_data, M_data)
    eta_prime = Ridge().fit(M_data, B_data)
    
    # Compute deltas for all ordered pairs
    N = len(FW_stim)
    pairs = [(i, j) for i in range(N) for j in range(N) if i != j]
    
    actual_residuals_eta = []
    actual_residuals_eta_prime = []
    
    for i, j in pairs:
        dW = FW_stim[j] - FW_stim[i]
        
        # Direct vs. brain-mediated paths
        direct_M = phi_M.predict(dW.reshape(1, -1))
        via_B = eta.predict(phi_B.predict(dW.reshape(1, -1)))
        actual_residuals_eta.append(np.linalg.norm(direct_M - via_B))
        
        # Reverse direction
        direct_B = phi_B.predict(dW.reshape(1, -1)))
        via_M = eta_prime.predict(phi_M.predict(dW.reshape(1, -1)))
        actual_residuals_eta_prime.append(np.linalg.norm(direct_B - via_M))
    
    # Permutation null
    perm_residuals_eta = []
    perm_residuals_eta_prime = []
    
    for _ in range(n_permutations):
        perm = np.random.permutation(len(pairs))
        # Shuffle pair indices to destroy cross-space correspondence
        # ... (compute permuted residuals)
        pass
    
    NVS_eta = np.mean(actual_residuals_eta) / np.mean(perm_residuals_eta)
    NVS_eta_prime = np.mean(actual_residuals_eta_prime) / np.mean(perm_residuals_eta_prime)
    
    return (NVS_eta + NVS_eta_prime) / 2
```

## Axis-Resolved Analysis

For concept-axis decomposition using CAVs:

```python
def compute_nvs_axis(FW_stim, B_data, M_data, v_axis):
    """Compute NVS for a specific concept axis."""
    # Project deltas onto axis direction
    deltas = FW_stim[1:] - FW_stim[:-1]
    projected = (deltas @ v_axis)[:, None] * v_axis[None, :]
    
    # Compute NVS using projected deltas instead of full deltas
    return compute_nvs(projected, B_data, M_data)
```

### Common Concept Axes (from GOD study)
- **Low-level**: luminance, spatial frequency
- **Mid-level**: curvilinearity, texture energy
- **Semantic**: animacy, real size
- **Extended atlas** (15 axes): affordance (hold/ride), material (metal/natural), etc.

## Pitfalls

1. **Proxy viability matters**: NVS results depend on the chosen proxy space W. Always check held-out CAV readout quality (R² > 0) before interpreting axis-specific results.
2. **Not strict functors**: The operational maps are empirical linear approximations fitted per-edge — not enforced to satisfy composition or identity laws.
3. **Small N limitation**: Empirical results from n=5 subjects on a single dataset; cross-dataset validation needed.
4. **Per-axis vs. full-FW answer different questions**: Full-∆ NVS is a global score; per-axis NVS localizes which transformations are preserved. Report both.
5. **Cross-axis comparison requires care**: Each axis is normalized to its own permutation null, so cross-axis comparisons reflect relative preservation against axis-specific shuffled baselines.
6. **Additive bias robustness**: NVS in ∆-space largely cancels additive bias (unlike RSA which drops from 1.0 to 0.29 under session-specific bias), making it more robust to systematic offsets.

## Related Work

- **RSA** (Kriegeskorte et al., 2008): Representational Similarity Analysis
- **CKA** (Kornblith et al., 2019): Centered Kernel Alignment
- **Brain-Score** (Schrimpf et al., 2018): Integrative benchmarking framework
- **BH Score** (Nonaka et al., 2021): Brain Hierarchy score
- **Categorical Deep Learning** (Gavranović et al., 2024): Category theory in DL
- **Linear Representation Hypothesis** (Mikolov et al., 2013; Park et al., 2024)

## When to Use

- Brain-DNN alignment studies where you need **axis-specific** rather than aggregate scores
- Diagnosing *which* transformations a model captures vs. misses (beyond overall similarity)
- Comparing different proxy spaces (CLIP vs. DINO vs. perceptual embeddings) for neuro-AI alignment
- Studies of hierarchical organization in sensory cortex (V1 → HVC mapping to shallow → deep layers)
- Evaluating world models as comparison spaces for neural representation
