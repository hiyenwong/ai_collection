# Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

## Paper Reference
**arXiv**: [2606.29655v1](https://arxiv.org/abs/2606.29655v1)  
**Author**: Prashant C. Raju  
**Date**: June 28, 2026  
**Keywords**: geometric stability, Shesha, representational dissimilarity matrix, neural population codes, recurrent circuits, representational drift

## Core Contribution

Introduces **geometric stability** as a new, independent axis of representational analysis orthogonal to both temporal stability (centroid drift) and decoding accuracy. Formalized via the Shesha metric — the Spearman rank correlation between split-half representational dissimilarity matrices (RDMs). Demonstrates that geometric stability predicts trial-by-trial neural-behavioral coupling while centroid drift does not.

## Conceptual Framework

### The Missing Dimension
Current representational reliability models focus on:
- **Temporal stability**: Do population centroids survive across sessions/days?
- **Decoding accuracy**: Can task variables be read out?

**Missing**: How reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session?

### Geometric Stability vs. Alternatives
| Property | What It Measures | What It Misses |
|---|---|---|
| Centroid drift | Mean population state preservation | Internal relational structure |
| Decoding accuracy | Information content in low-dim subspace | Full geometry reproducibility |
| **Geometric stability (Shesha)** | Pairwise distance structure consistency | Temporal dynamics |

**Critical finding**: Shesha and decoding accuracy are empirically orthogonal (ρ = 0.09, p = 0.19). A population can be highly decodable yet geometrically brittle.

## Shesha Metric — Formal Definition

### Computation
```python
# For each stimulus condition, compute population vectors on odd/even trial splits
x_bar_i_odd = mean(population_vectors[condition_i, odd_trials])
x_bar_i_even = mean(population_vectors[condition_i, even_trials])

# Build RDMs (pairwise cosine distances)
D_odd[i,j] = 1 - cos(x_bar_i_odd, x_bar_j_odd)
D_even[i,j] = 1 - cos(x_bar_i_even, x_bar_j_even)

# Geometric stability = Spearman rank correlation
S = spearmanr(vec(D_odd), vec(D_even))
```

### Properties
- **Range**: -1 to 1 (higher = more stable geometry)
- **Scale-invariant**: Rank correlation makes it robust to overall distance scaling
- **Sensitive to compression artifacts**: Detects failures from aggressive dimensionality reduction that CK A misses
- **Orthogonal to similarity metrics**: Shares < 0.1% variance with centered kernel alignment

## Key Empirical Results

### 1. Regional Hierarchy (Steinmetz et al., 2019 — 229 area-sessions, 68 regions)

**Geometric Stability** (most → least stable):
- Striatum: S̄ = 0.44 [0.34, 0.56]
- Motor cortex: 0.38 [0.25, 0.50]
- Visual cortex: 0.36 [0.27, 0.46]
- Hippocampus: 0.19 [0.13, 0.25] ← lowest

**Temporal Stability (centroid similarity)** — inverted hierarchy:
- Thalamus: 0.95 [0.92, 0.97] ← most stable
- Hippocampus: 0.94 (second-least stable for geometry, but high temporal stability)
- Striatum: 0.83 ← least stable temporally

**Interpretation**:
- Striatum: Encodes action-reward with reliable relational structure but shifting baseline → continuous value updating with consistent readout
- Hippocampus: Preserves mean state while internal structure reorganizes → rapid memory formation rather than fixed codes

### 2. Behavioral Prediction

- Geometric stability → neural-behavioral coupling: **ρ = 0.18, p = 0.005** ✓
- Centroid drift → neural-behavioral coupling: **ρ = 0.002, p = 0.976** ✗
- At session level: Shesha does NOT predict mean task accuracy (ρ = 0.087, p = 0.191)
- **Behavioral relevance is trial-to-trial, not session-to-session**

### 3. Circuit Dependence (Olfactory System — Bolding & Franks, 2018)

**Predicted ordering** (attractor network hypothesis):
- OB (no recurrence): S = 0.47
- TeLC PCx (recurrence silenced): S = 0.53
- Control PCx (intact recurrence): S = 0.60

**Result**: Ordering confirmed (OB < TeLC PCx < Control PCx), though small samples (n = 5-11) prevent statistical significance.

## Circuit Mechanism — Attractor Network Model

### Architecture
- N = 200 rate units, 20% sparse random recurrent connectivity
- E/I balance maintained via fixed global inhibitory leak (−γr̄)
- Feedforward input with 70% channel dropout per trial (simulating incomplete OB→PCx projection)
- Dynamics: τẋ = −x + J·Wexc·f(x) + Winh·f(x) − γr̄ + Wff·u + η

### Mechanism
1. Trial-to-trial dropout → each split receives different random input subset → RDMs differ → low S
2. Recurrent dynamics counteract by attracting responses to stimulus-specific fixed points
3. Pattern completion from partial input regardless of which channels survive

### Results
- J = 0 (TeLC analog): Shesha = 0.27
- J = 1.4: Shesha = 0.51
- Monotonic increase: **ρ = +0.64, p = 0.010** ✓
- Shesha more sensitive to J than within-session consistency (|ρ| = 0.64 vs 0.55)

## Theoretical Implications

### Orthogonality Results
1. Geometric stability ⊥ Temporal stability (empirically dissociable)
2. Geometric stability ⊥ Decoding accuracy (different computational properties)
3. Geometric stability ⊥ CKA / similarity metrics (< 0.1% shared variance)

### Functional Role
- **Striatum**: High geometric stability + low temporal stability → reliable relational readout of shifting value representations
- **Hippocampus**: Low geometric stability + high temporal stability → stable mean state supports rapid memory encoding with flexible internal codes
- **Motor/Visual**: Intermediate on both dimensions → balanced stability-flexibility tradeoff

### Why Centroid Drift Fails
Centroid preservation only asks "does the average state survive?" It cannot detect whether the internal geometry (distances between all pairs of conditions) is reproducible. Shesha captures the full relational structure.

## Implementation Guide

### Computing Shesha
```python
import numpy as np
from scipy.stats import spearmanr

def compute_shesha(data, conditions, n_splits=2):
    """
    data: (n_trials, n_neurons) array
    conditions: (n_trials,) array of condition labels
    Returns: Shesha score (Spearman ρ between split-half RDMs)
    """
    # Split trials
    odd_idx = np.arange(len(data))[::2]
    even_idx = np.arange(len(data))[1::2]
    
    # Compute condition-averaged population vectors per split
    unique_conds = np.unique(conditions)
    RDM_odd = np.zeros((len(unique_conds), len(unique_conds)))
    RDM_even = np.zeros((len(unique_conds), len(unique_conds)))
    
    for i, ci in enumerate(unique_conds):
        for j, cj in enumerate(unique_conds):
            # Odd split
            vi = np.mean(data[odd_idx][conditions[odd_idx] == ci], axis=0)
            vj = np.mean(data[odd_idx][conditions[odd_idx] == cj], axis=0)
            RDM_odd[i, j] = 1 - np.dot(vi, vj) / (np.linalg.norm(vi) * np.linalg.norm(vj))
            
            # Even split
            vi = np.mean(data[even_idx][conditions[even_idx] == ci], axis=0)
            vj = np.mean(data[even_idx][conditions[even_idx] == cj], axis=0)
            RDM_even[i, j] = 1 - np.dot(vi, vj) / (np.linalg.norm(vi) * np.linalg.norm(vj))
    
    # Extract upper triangular vectors
    triu_idx = np.triu_indices(len(unique_conds), k=1)
    S, p = spearmanr(RDM_odd[triu_idx], RDM_even[triu_idx])
    return S, p
```

### Bootstrap Confidence Intervals
```python
def bootstrap_shesha_ci(data, conditions, n_bootstrap=10000):
    """Compute 95% CI for Shesha via trial resampling."""
    S_values = []
    for _ in range(n_bootstrap):
        idx = np.random.choice(len(data), size=len(data), replace=True)
        S, _ = compute_shesha(data[idx], conditions[idx])
        S_values.append(S)
    return np.percentile(S_values, [2.5, 97.5])
```

## Methodological Patterns

### When to Use Shesha
- Evaluating representational reliability within sessions
- Comparing stability across brain regions
- Testing circuit mechanisms for representational geometry
- Detecting compression artifacts from dimensionality reduction
- Any context where pairwise relational structure matters more than centroids

### When NOT to Use
- Cross-session/cross-day stability (use temporal metrics)
- Decoding performance evaluation (use classification metrics)
- Single-condition analysis (needs ≥3 conditions for meaningful RDM)

## Connections to Existing Work
- **RSA** (Kriegeskorte et al., 2008): Shesha compares data-to-data; RSA compares data-to-model
- **Representational drift** (Driscoll et al., 2017; Rule et al., 2019): Orthogonal property
- **Low-dimensional latent dynamics** (Gallego et al., 2020): Shesha captures what low-dim preservation misses
- **Attractor networks** (Hopfield, 1982): Pattern completion mechanism for geometric stability

## Activation Triggers
**Keywords**: geometric stability, Shesha, representational dissimilarity matrix, split-half reliability, neural population codes, representational drift, attractor networks, pattern completion, regional hierarchy, neural-behavioral coupling

**Use Cases**:
- Analyzing neural population geometry reliability
- Comparing representational properties across brain regions
- Testing circuit mechanisms for stability
- Evaluating dimensionality reduction quality
- Brain-computer interface design (stable geometry → better decoders)
