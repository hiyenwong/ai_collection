---
name: geometric-stability-neural-population-codes
description: "Geometric Stability of Neural Population Codes methodology - Shesha metric quantifying pairwise distance structure reproducibility across split-half RDMs, dissociable from temporal stability and decoding accuracy. Use when analyzing representational reliability beyond centroid drift, comparing brain regions, or modeling attractor-network mechanisms for RDM consistency. Activation: geometric stability, Shesha, split-half RDM, representational dissimilarity, neural population code, striatum hippocampus, attractor network, recurrent excitation, neural-behavioral coupling."
license: MIT
metadata:
  arxiv_id: "2606.29655"
  published: "2026-06-28"
  authors: "Prashant C. Raju"
  categories: ["q-bio.NC", "cs.NE", "q-bio.QM"]
  tags: [neuroscience, neural-population, geometric-stability, representational-similarity, RDM, attractor-network, striatum, hippocampus, brain-regions, behavioral-relevance]
---

# Geometric Stability of Neural Population Codes

## Paper
**arXiv: 2606.29655** — "Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence" (Prashant C. Raju, 2026-06-28)

## Core Contribution

Introduces **geometric stability** as a new axis of representational analysis, formally distinct from temporal stability (centroid drift) and decoding accuracy. Quantified via **Shesha** (Spearman rank correlation between split-half representational dissimilarity matrices, RDMs), it measures whether the *pairwise distance structure among stimuli* reproduces across independent observations within a single session.

### Why It Matters

Existing representational reliability frameworks focus on temporal stability: do population centroids persist across sessions/days? This leaves a fundamental question unanswered: how reliably does the **pairwise geometry** (distance structure) among stimuli reproduce across independent observations within a session? Geometric stability answers this and turns out to be:

1. **Empirically dissociable** from both temporal stability and decoding accuracy
2. **Behaviorally predictive** where temporal stability is not
3. **Regionally heterogeneous** in a hierarchy opposite to temporal stability
4. **Circuit-dependent** — explainable by recurrent attractor dynamics

## Methodology: Shesha Metric

### Definition

For a session with N stimuli and trial-level population activity vectors:

1. Split trials for each stimulus into two halves (odd/even, or random partition)
2. Compute RDM₁ and RDM₂ (pairwise dissimilarity matrices, e.g., 1 − Pearson correlation of mean activity vectors)
3. **Shesha S = ρ_spearman(vech(RDM₁), vech(RDM₂))** — Spearman rank correlation between upper triangles of the two RDMs

### Interpretation
- **S → 1**: Pairwise geometry reproduces perfectly across observations
- **S → 0**: Distance structure is unreliable; only marginal statistics are stable
- **S < 0**: Anti-correlated geometry (rare, indicates non-stationary coding)

### Why Not Just Decoding or Centroid Drift?

| Property | Centroid Drift | Decoding Accuracy | **Shesha (Geometric Stability)** |
|----------|---------------|-------------------|----------------------------------|
| Captures mean activity shifts | ✓ | indirect | independent |
| Captures pairwise distance reliability | ✗ | indirect | ✓ (direct) |
| Predicts trial-by-trial behavior | ✗ (ρ=0.002) | partial | ✓ (ρ=0.18, p=0.005) |
| Sensitive to recurrent circuit structure | weak | weak | strong |

## Key Empirical Findings

### 1. Behavioral Relevance (Steinmetz et al. 2019 dataset)

Across **229 area-session observations spanning 68 brain regions** in a visual discrimination task:
- **Geometric stability predicts trial-by-trial neural-behavioral coupling**: ρ = 0.18, p = 0.005
- **Centroid drift does NOT predict behavior**: ρ = 0.002, p = 0.976

This dissociation is the central empirical claim: geometric stability captures a behaviorally relevant property that temporal-stability analyses miss entirely.

### 2. Regional Hierarchy (opposite to temporal stability)

| Region | Geometric Stability (S̄) | Temporal Stability |
|--------|--------------------------|--------------------|
| **Striatum** | 0.44 (most stable) | lower |
| **Hippocampus** | 0.19 (least stable) | higher |

The regional hierarchy of geometric stability runs **roughly opposite** to the temporal stability hierarchy. This implies the two axes measure fundamentally different organizational properties — brain regions optimized for temporal persistence are not necessarily optimized for geometric consistency.

### 3. Circuit-Level Account (Attractor Network Model)

Motivated by directionally consistent olfactory data (Bolding & Franks 2018), an **attractor network model** with recurrent excitatory coupling explains geometric stability emergence:

- Recurrent excitation **amplifies split-half RDM consistency** by completing stimulus patterns from sparse feedforward input
- Model prediction: ρ = +0.64, p = 0.010
- Mechanism: recurrent attractor dynamics denoise the representational geometry, pulling noisy observations toward stable fixed points

This provides a circuit-level explanation: regions with stronger recurrent excitation (e.g., striatum) exhibit higher geometric stability because attractor dynamics regularize the geometry.

## Implementation Guide

### Computing Shesha in Python

```python
import numpy as np
from scipy.stats import spearmanr

def compute_shesha(activity, stim_labels, n_splits=100):
    """
    activity: (n_trials, n_neurons) population activity matrix
    stim_labels: (n_trials,) stimulus identity for each trial
    Returns mean Shesha across random split halves.
    """
    unique_stims = np.unique(stim_labels)
    shesha_values = []
    
    for _ in range(n_splits):
        # Split trials for each stimulus into two halves
        mean_vectors_1, mean_vectors_2 = [], []
        for stim in unique_stims:
            idx = np.where(stim_labels == stim)[0]
            if len(idx) < 4:
                continue
            np.random.shuffle(idx)
            half = len(idx) // 2
            mean_vectors_1.append(np.mean(activity[idx[:half]], axis=0))
            mean_vectors_2.append(np.mean(activity[idx[half:]], axis=0))
        
        if len(mean_vectors_1) < 3:
            continue
        
        M1 = np.array(mean_vectors_1)
        M2 = np.array(mean_vectors_2)
        
        # Compute RDMs (1 - Pearson correlation)
        def rdm(M):
            # Pairwise correlation-based RDM
            corr = np.corrcoef(M)
            return 1 - corr
        
        rdm1 = rdm(M1)
        rdm2 = rdm(M2)
        
        # Spearman correlation between upper triangles
        iu = np.triu_indices(len(unique_stims), k=1)
        rho, _ = spearmanr(rdm1[iu], rdm2[iu])
        shesha_values.append(rho)
    
    return np.mean(shesha_values), np.std(shesha_values)
```

### Workflow

1. **Data preparation**: Trial-level neural activity (n_trials × n_neurons) with stimulus labels
2. **Minimum trial count**: ≥4 trials per stimulus for stable split-half estimates
3. **Split strategy**: Random partitioning (n_splits=100 for bootstrap CI)
4. **RDM metric**: 1 − Pearson correlation of mean population vectors (flexible — can use Euclidean, Mahalanobis, or cross-validated distances)
5. **Interpretation**: Compare Shesha across brain regions, sessions, or task conditions; correlate with behavioral metrics

## When to Use

- **Representational reliability analysis** beyond centroid drift and decoding accuracy
- **Cross-region comparison** of representational geometry stability
- **Circuit modeling** linking recurrent dynamics to representational structure
- **Behavioral prediction** from neural population geometry
- **BCI/neurofeedback** applications where geometric consistency of neural codes matters

## Relation to Existing Frameworks

- **Complementary to RSA (Representational Similarity Analysis)**: RSA compares RDMs across regions/models/subjects; Shesha measures within-session split-half RDM consistency — an internal reliability metric
- **Complementary to temporal stability (drift)**: Orthogonal axes — a region can have high temporal stability but low geometric stability (hippocampus) or vice versa (striatum)
- **Attractor network theory**: Shesha provides an empirical signature to test predictions of attractor models — regions with stronger attractor dynamics should show higher Shesha

## Pitfalls

- **Trial count sensitivity**: Shesha is unreliable with <4 trials per stimulus. Always report trial counts.
- **RDM metric choice**: Pearson-based RDMs are standard, but Euclidean or Mahalanobis distances may reveal different geometric properties. Pre-register or systematically compare metrics.
- **Stimulus set size**: Small stimulus sets (<5 stimuli) produce unreliable RDMs. Aim for ≥8 stimuli for stable Shesha estimates.
- **Confound with firing rate**: Regions with higher baseline firing may show higher Shesha due to better SNR, not necessarily stronger attractor dynamics. Control for mean firing rate in cross-region comparisons.

## References

- Raju, P. C. (2026). Geometric Stability of Neural Population Codes. arXiv:2606.29655
- Steinmetz, N. A., et al. (2019). Distributed coding of choice, action and engagement across the mouse brain. Nature 576, 266–273.
- Bolding, K. A. & Franks, K. M. (2018). Recurrent cortical circuits implement concentration-invariant odor coding. Science 361, eaat6904.
- See also: [[representational-similarity-analysis]], [[neural-population-dynamics]], [[attractor-models-language-reasoning]]
