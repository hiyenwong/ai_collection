---
name: auto-dsm-evaluation-framework
description: >
  Black-box evaluation framework for assessing LLM-generated Design Structure
  Matrices (DSMs) from structured technical documentation. Integrates structural
  metrics (Completeness, Correctness, Coupling Density), classification metrics
  (Selective Accuracy, Abstention Coverage), and stability measures (Entropy,
  Fleiss' κ) into a Composite Quality Score (Q). Provides transparent benchmarking
  methodology for auditing Auto-DSM pipelines in MBSE workflows.
category: systems-engineering
tags: [mbse, dsm, llm-evaluation, design-structure-matrix, systems-engineering, model-based]
source: arxiv:2607.05985
date: 2026-07-07
---

# Auto-DSM Evaluation Framework: Black-Box Assessment of LLM-Based DSM Generation

## Paper

- **Title**: Auto-DSM Under the Lens: A Black-Box Evaluation Framework for LLM-Based DSM Generation
- **Authors**: Niels Potters, Theo Hofman
- **arXiv**: [2607.05985](https://arxiv.org/abs/2607.05985)
- **Date**: 2026-07-07
- **Categories**: cs.AI, cs.AR, cs.CE, eess.SY

## Problem

LLMs are increasingly used to auto-generate Design Structure Matrices (DSMs) from technical documentation, but:
- Auto-DSM pipelines are closed-source and opaque
- No standardized methodology exists for evaluating LLM-generated DSMs
- LLMs are sensitive to ambiguity, inconsistent dependency definitions, and prompt formulation
- Hallucination and abstention failures need systematic characterization

## Evaluation Framework

### Three-Perspective Approach

| Perspective | Metrics | Purpose |
|-------------|---------|---------|
| **Single-Run** | Completeness, Correctness, Coupling Density | Structural quality of one DSM |
| **Multi-Run** | Selective Accuracy, Abstention Coverage | Consistency across runs |
| **Stability** | Entropy, Fleiss' κ | Reproducibility and agreement |

### 1. Structural Metrics (Single-Run)

**Completeness**: Fraction of GT-DSM dependencies recovered by GEN-DSM
```
Completeness = |GEN-DSM ∩ GT-DSM| / |GT-DSM|
```

**Correctness**: Fraction of GEN-DSM dependencies that match GT-DSM
```
Correctness = |GEN-DSM ∩ GT-DSM| / |GEN-DSM|
```

**Coupling Density**: Ratio of actual dependencies to possible dependencies
```
Density = |DSM| / (n × (n-1))
```
where n = number of system elements.

### 2. Classification Metrics (Multi-Run)

**Selective Accuracy**: Accuracy when the LLM does NOT abstain
```
SA = Correct Predictions / (Total Predictions - Abstentions)
```

**Abstention Coverage**: Fraction of cases where the LLM correctly abstains
```
AC = Correct Abstentions / Total Abstentions
```

### 3. Stability Measures

**Entropy**: Measures variability across multiple runs
```
H = -Σ p_ij × log(p_ij)
```
where p_ij is the empirical probability of a dependency between elements i and j.

**Fleiss' κ**: Inter-rater agreement across multiple LLM runs
```
κ = (P̄ - P̄e) / (1 - P̄e)
```
where P̄ is observed agreement and P̄e is expected agreement by chance.

### Composite Quality Score (Q)

Synthesizes all metrics into a single score:
```
Q = w1·Completeness + w2·Correctness + w3·Selective Accuracy
  + w4·(1 - Entropy/Entropy_max) + w5·Fleiss_κ
```

Weights can be tuned based on application priorities (e.g., safety-critical vs. exploratory).

## Experimental Design

### Controlled Variables

1. **Phrasing variations**: Same system described with different terminology
2. **Parameter-dataset alignment**: Matching LLM temperature/top_p to task difficulty
3. **System complexity**: Abstract vs. real-world (refrigerator) decompositions

### Key Findings

- LLMs produce structurally plausible DSMs under well-structured inputs
- High reproducibility achievable with clear dependency definitions
- **Systematic failure modes**:
  - Ambiguous dependency definitions → hallucination
  - Inconsistent terminology → missed dependencies
  - Poor prompt formulation → excessive abstention or over-confident errors
- Performance degrades significantly with system complexity increase

## Implementation Pattern

```python
import numpy as np
from collections import Counter

class DSMEvaluator:
    """Black-box evaluation framework for LLM-generated DSMs."""
    
    def __init__(self, weights=None):
        self.weights = weights or {
            'completeness': 0.25,
            'correctness': 0.25,
            'selective_accuracy': 0.20,
            'stability': 0.15,
            'agreement': 0.15
        }
    
    def _to_binary_matrix(self, dsm, elements):
        """Convert DSM dict to binary adjacency matrix."""
        n = len(elements)
        idx = {e: i for i, e in enumerate(elements)}
        mat = np.zeros((n, n))
        for (src, tgt), val in dsm.items():
            if src in idx and tgt in idx:
                mat[idx[src], idx[tgt]] = 1
        return mat
    
    def completeness(self, gen_dsm, gt_dsm):
        """Fraction of GT dependencies recovered."""
        gen_set = set(gen_dsm.keys())
        gt_set = set(gt_dsm.keys())
        intersection = gen_set & gt_set
        return len(intersection) / max(len(gt_set), 1)
    
    def correctness(self, gen_dsm, gt_dsm):
        """Fraction of GEN dependencies that are correct."""
        gen_set = set(gen_dsm.keys())
        gt_set = set(gt_dsm.keys())
        intersection = gen_set & gt_set
        return len(intersection) / max(len(gen_set), 1)
    
    def coupling_density(self, dsm, n_elements):
        """Ratio of actual to possible dependencies."""
        n_possible = n_elements * (n_elements - 1)
        return len(dsm) / max(n_possible, 1)
    
    def selective_accuracy(self, predictions, ground_truth, abstentions):
        """Accuracy excluding abstained predictions."""
        non_abstained = [(p, g) for p, g, a in zip(predictions, ground_truth, abstentions) if not a]
        if not non_abstained:
            return 0.0
        correct = sum(1 for p, g in non_abstained if p == g)
        return correct / len(non_abstained)
    
    def abstention_coverage(self, abstentions, ground_truth):
        """Fraction of cases where abstention was correct."""
        # Abstention is "correct" when the dependency is genuinely ambiguous
        # or the information is missing from documentation
        if not any(abstentions):
            return 1.0  # No abstentions = nothing to cover
        return sum(abstentions) / len(abstentions)  # Placeholder; refine per domain
    
    def stability_entropy(self, dsm_runs, elements):
        """Entropy across multiple DSM generation runs."""
        n = len(elements)
        prob_matrix = np.zeros((n, n))
        for dsm in dsm_runs:
            prob_matrix += self._to_binary_matrix(dsm, elements)
        prob_matrix /= max(len(dsm_runs), 1)
        
        # Flatten and compute entropy
        probs = prob_matrix.flatten()
        probs = probs[probs > 0]  # Ignore zero-probability entries
        entropy = -np.sum(probs * np.log2(probs + 1e-10))
        max_entropy = np.log2(n * n)
        return entropy / max(max_entropy, 1)  # Normalized
    
    def fleiss_kappa(self, dsm_runs, elements):
        """Fleiss' kappa for inter-rater agreement across runs."""
        n_elements = len(elements)
        n_raters = len(dsm_runs)
        
        # Build rating matrix
        ratings = np.zeros((n_elements * (n_elements - 1), n_raters))
        for r, dsm in enumerate(dsm_runs):
            mat = self._to_binary_matrix(dsm, elements)
            idx = 0
            for i in range(n_elements):
                for j in range(n_elements):
                    if i != j:
                        ratings[idx, r] = mat[i, j]
                        idx += 1
        
        # Compute Fleiss' kappa
        n_items, n_raters = ratings.shape
        p_j = np.sum(ratings, axis=0) / (n_items * n_raters)
        p_bar_e = np.sum(p_j * (1 - p_j))
        
        p_i = np.sum(ratings * (1 - ratings), axis=1) / (n_raters * (n_raters - 1))
        p_bar = 1 - np.mean(p_i)
        
        if p_bar_e == 1:
            return 1.0
        return (p_bar - p_bar_e) / (1 - p_bar_e)
    
    def composite_quality(self, gen_dsm, gt_dsm, dsm_runs, elements,
                         predictions=None, ground_truth=None, abstentions=None):
        """Compute Composite Quality Score Q."""
        metrics = {
            'completeness': self.completeness(gen_dsm, gt_dsm),
            'correctness': self.correctness(gen_dsm, gt_dsm),
        }
        
        if predictions is not None and abstentions is not None:
            metrics['selective_accuracy'] = self.selective_accuracy(
                predictions, ground_truth, abstentions)
        
        metrics['stability'] = 1 - self.stability_entropy(dsm_runs, elements)
        metrics['agreement'] = max(0, self.fleiss_kappa(dsm_runs, elements))
        
        q = sum(self.weights.get(k, 0) * metrics.get(k, 0) for k in self.weights)
        return q, metrics
```

## Key Insights for Systems Engineering

1. **Structured inputs are critical**: LLMs perform well on DSM generation only when documentation is clear and dependency definitions are consistent
2. **Multi-run evaluation is essential**: Single-run metrics hide hallucination patterns; stability measures reveal systematic failure modes
3. **Abstention is a feature, not a bug**: Proper abstention when information is ambiguous is preferable to confident hallucination
4. **Composite scoring enables trade-offs**: Different MBSE contexts prioritize different aspects (safety → correctness, exploration → completeness)
5. **Black-box auditing bridges the gap**: This framework enables systematic evaluation without requiring access to Auto-DSM internals

## Activation Keywords

DSM generation, design structure matrix, auto-dsm, MBSE evaluation, LLM systems engineering, model-based decomposition, system architecture evaluation, dependency matrix, systems engineering LLM
