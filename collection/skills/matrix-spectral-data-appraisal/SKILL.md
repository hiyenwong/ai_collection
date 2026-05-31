---
name: matrix-spectral-data-appraisal
description: "Matrix spectral functions methodology for data appraisal, unifying neural scaling laws and Vendi Score. Shows both are submodular, with Vendi Score as a special case. Introduces secular-equation-based updates achieving 35,000x speedup for Vendi optimization. Reveals facility location outperforms Vendi Score for subset selection. Use when: data selection, dataset valuation, Vendi Score optimization, submodular data appraisal, neural scaling laws, matrix spectral functions, training subset selection."
metadata:
  arxiv_id: "2605.29448"
  published: "2026-05-28"
  authors: "Jeff A. Bilmes, Gantavya Bhatt, Arnav M. Das"
  tags: [data-appraisal, vendi-score, submodular, matrix-spectral-functions, neural-scaling-laws, dataset-value, facility-location]
---

# Matrix Spectral Data Appraisal

## Paper Reference

**arXiv: 2605.29448** — "How Much Is a Dataset Worth? Scaling Laws, the Vendi Score, and Matrix Spectral Functions"
- Authors: Jeff A. Bilmes, Gantavya Bhatt, Arnav M. Das
- Published: May 28, 2026
- 75 pages

## Core Methodology

This paper unifies **neural scaling laws** and the **Vendi Score** (which uses quantum entropy to measure dataset value) under a broader framework of **matrix spectral functions** — all of which are submodular objectives for data appraisal.

### Key Results

1. **Submodularity**: Both neural scaling law objectives and the Vendi Score are submodular
2. **Vendi Score as Special Case**: Vendi Score is a special case of matrix spectral functions, which also include DPP (Determinantal Point Process) objectives and many others
3. **Weakly Matrix Monotone Functions**: New class of functions yielding weakly submodular matrix spectral functions
4. **35,000x Speedup**: Secular-equation-based updates avoid repeated eigendecompositions, reducing marginal-gain evaluation by O(m) factor
5. **Facility Location Wins**: Across multiple datasets, facility location outperforms Vendi Score, DPPs, and new variants for predicting held-out test performance
6. **Vendi Score Limitation**: While predictive over moderate score ranges, pushing to higher values makes it a poor downstream performance proxy
7. **Random Subsets Concentration**: Uniformly random fixed-size subsets are remarkably concentrated in both appraisal scores and held-out performance

## Framework

### Matrix Spectral Functions

For m-dimensional embeddings, a matrix spectral function is:
```
f(S) = g(λ₁(K_S), λ₂(K_S), ..., λ_m(K_S))
```
where K_S is the kernel matrix of subset S and g is a symmetric function.

### Submodularity Hierarchy

```
Strongly Submodular
  ├── Facility Location (best performer)
  ├── Determinantal Point Processes (DPPs)
  └── Vendi Score (special case of matrix spectral functions)
       └── Weakly Submodular variants (weakly matrix monotone)
```

## Reusable Patterns

### Pattern 1: Fast Vendi Score Optimization

The key optimization uses secular equations instead of repeated eigendecompositions:

```python
def fast_vendi_update(embeddings, current_subset, new_element):
    """Secular-equation-based update avoiding O(m³) eigendecomposition."""
    # Instead of recomputing eigenvalues from scratch:
    # old_eigvals = eig(K_current)  # O(m³) — SLOW
    
    # Use secular equation to update eigenvalues in O(m²):
    # Δeigvals from rank-1 update
    # Total speedup: ~35,000x on ImageNet-1K scale
    pass
```

### Pattern 2: Submodular Greedy Selection

```python
def submodular_greedy(data, objective_fn, k):
    """Greedy subset selection using submodular objective."""
    selected = []
    for _ in range(k):
        best_gain = -inf
        best_elem = None
        for elem in remaining:
            gain = objective_fn(selected ∪ {elem}) - objective_fn(selected)
            if gain > best_gain:
                best_gain = gain
                best_elem = elem
        selected.append(best_elem)
    return selected
```

### Pattern 3: Multi-Objective Comparison

When evaluating data appraisal objectives:

1. Test across multiple datasets
2. Compare under fixed-size, class-balanced, and fixed training-budget regimes
3. Measure correlation with held-out test performance
4. Check concentration behavior of random subsets

## Key Findings for Practice

### What Works Best
- **Facility location** consistently outperforms Vendi Score and DPPs
- Use facility location for practical subset selection tasks

### Vendi Score Caveats
- Predictive over moderate score ranges
- **Degrades at high values** — optimizing Vendi to extreme values gives poor downstream performance
- Use with score range awareness

### Random Subsets Are Surprisingly Good
- Uniform random fixed-size subsets are concentrated in both scores and performance
- Even when controlling for size, class balance, and budget, performance ranges smoothly from good to bad

## When to Use

- **Training data selection**: Selecting optimal subsets for model training
- **Dataset valuation**: Quantifying the value of datasets
- **Active learning**: Choosing which data points to label next
- **Data pruning**: Removing low-value data points
- **Scaling law analysis**: Understanding how data size affects model performance
- **Diversity-based selection**: When dataset diversity matters more than size

## Activation Keywords

- data appraisal
- Vendi Score optimization
- matrix spectral functions
- submodular data selection
- dataset value estimation
- neural scaling laws
- facility location data selection
- secular equation update
- 数据集价值评估
- 数据选择
- 次模函数

## Related Skills

- **structure-aware-coreset-fc-benchmarking** — coreset-based benchmarking acceleration
- **quantum-ml-data-loading** — data loading for quantum ML
- **quantum-feature-map-benchmarking** — matched spectral benchmarking for quantum feature maps

## Pitfalls

- Vendi Score optimization to extreme values → poor downstream performance
- Random subsets may be sufficient — don't over-optimize
- Facility location outperforms Vendi Score in practice
- Secular-equation updates save 35,000x but still require m-dimensional embeddings
- Size, class balance, and training budget alone don't determine data value