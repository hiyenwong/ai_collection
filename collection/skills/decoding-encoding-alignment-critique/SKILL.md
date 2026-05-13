---
name: decoding-encoding-alignment-critique
description: >
  Critical analysis framework for brain-model alignment methods demonstrating
  that decoding-based similarity metrics (RSA, CKA, Procrustes) are insensitive
  to internal functional organization. Based on arXiv:2605.05907 (Bertram et al.,
  2026). Use when: (1) evaluating representational similarity analysis validity,
  (2) comparing neural systems across species or models, (3) designing encoding
  manifold analyses, (4) applying Gromov-Wasserstein distance for neural
  population comparison, (5) questioning whether high RSA/CKA implies functional
  similarity, (6) analyzing neural population topology. Activation: decoding
  alignment, encoding manifold, RSA critique, CKA limitations, representational
  similarity analysis, neural manifold, Gromov-Wasserstein neural alignment,
  brain-model comparison, neural population topology, 解码对齐, 编码流形,
  表征相似性分析批判.
---

# Decoding-Alignment Critique

Based on: *"Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience"* (Bertram et al., arXiv:2605.05907, May 2026).

## Core Argument

Decoding-based similarity metrics (RSA, CKA, Procrustes, classification accuracy) can be **saturated by a small subset of neurons** and are **insensitive to internal functional organization**. Two systems can achieve identical alignment scores while having qualitatively different internal architectures.

## Key Insight: Two Manifolds

### Decoding Manifold (stimulus-centric)
- Points = stimuli, coordinates = population responses
- Nearby points = stimuli evoking similar activity
- What decoding metrics (RSA, CKA) measure

### Encoding Manifold (neuron-centric)
- Points = neurons, coordinates = stimulus-response profiles
- Nearby points = neurons with similar tuning
- Captures functional architecture independently of readout

## Critical Findings

### 1. Decoding Metrics Saturate with Small Subpopulations

Across mouse retina, V1, and VISp:
- All 8 decoding metrics plateau at **5% of neurons** or below under best selection
- RSA and CKA remain near ceiling even under random selection at moderate fractions
- Same scalar summary can be produced by functionally heterogeneous populations

### 2. Encoding Manifold Position Determines Decoding Fidelity

- High-PC1 subpopulations recover full-population decoding profile
- Low-PC1 subpopulations yield substantially lower scores
- **BUT**: both occupy only a small, localized region of encoding manifold
- Decoding metrics capture local vs. global encoding differences but miss the topology

### 3. Causal Manipulation Evidence (MNIST Experiment)

- Decoding metrics unchanged when encoding topology is causally manipulated via training loss
- Discrete vs. continuous encoding manifolds produce identical RSA/CKA scores
- Provides causal (not just correlational) evidence of decoding metric blindness

### 4. Biological Validation

- Retina: encoding manifold clusters by known retinal ganglion cell types
- V1: no known functional groups, shows continuous encoding topology
- Allen Brain Observatory (5 cortical areas): decoding metrics saturate, encoding reveals structural differences

## Methodology

### Encoding Manifold Construction (3 stages)

1. **Nonnegative Tensor Factorization (NTF)**
   - Decompose response tensor (neurons x stimuli x trials x time)
   - Yields neural factors embedding each neuron in stimulus-response space
   - Only hyperparameter: number of factors

2. **Iterated Adaptive Neighborhoods (IAN)**
   - Build weighted data graph over neural encoding space
   - Locally adaptive similarity kernel (no fixed neighborhood size)

3. **Diffusion Maps**
   - Low-dimensional embedding preserving intrinsic geometry
   - Produces the encoding manifold in diffusion coordinates

### Gromov-Wasserstein (GW) Distance

Applied as intrinsic measure of encoding manifold coverage:
- Finds optimal transport between two metric spaces (no point correspondence needed)
- Two manifolds with same shape = zero distance
- Structurally incompatible = high distance
- Normalized GW similarity = 1 - GW/max_baseline

```
GW(E_sub, E_full) = min_T sum_{ij} T_ij * |d_E_sub(i,j) - d_E_full(i,j)|^2
GW_similarity = 1 - GW / GW_baseline
```

### Eight Complementary Metrics

**Static**: k-NN accuracy, RSA, CKA, Procrustes R²
**Trajectory**: time-resolved RSA, Speed Profile Correlation, Trajectory Procrustes R², Dynamical Similarity Analysis (DSA)

## Practical Implications

1. **Model validation is incomplete**: A model declared "brain-aligned" by RSA/CKA may have structurally distinct internal organization
2. **Neuroscience comparisons need both manifolds**: Always complement decoding analysis with encoding manifold analysis
3. **GW for population comparison**: Use Gromov-Wasserstein distance as complementary diagnostic
4. **Subpopulation analysis matters**: Test whether results hold across subpopulations, not just full population

## When to Apply

- Validating brain-model alignment claims (RSA/CKA alone is insufficient)
- Comparing neural populations across brain regions, species, or models
- Designing experiments to characterize neural population functional architecture
- Questioning whether high representational similarity implies functional similarity
- Building interpretable neural decoding systems

## Code Reference

Neural Manifold Explorer tool provided in paper.
NTF: https://github.com/ahwillia/tensorly
IAN: iterative adaptive neighborhoods algorithm
Diffusion maps: https://diffusion-maps.readthedocs.io/

## Related

- brain-dnn-transformation-alignment: category-theoretic alignment framework
- naturality-violation-score: brain-DNN alignment methodology
- neural-manifold-learning-dynamics: neural manifold analysis methods
