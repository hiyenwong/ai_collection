# SKILL.md - Alpha-Z Divergence Brain Connectivity Fingerprint

## Activation Keywords

- Alpha-Z divergence, Bures-Wasserstein divergence
- brain connectivity fingerprint, functional connectome
- phenotypic traits, cognitive behavioral patterns
- FC analysis, divergence-based distance metric

## What It Does

Provides a novel divergence-based distance metric (Alpha-Z Bures-Wasserstein) for functional connectivity analysis, enabling enhanced sensitivity in linking FC patterns to cognitive and behavioral outcomes with better individual identification.

## When To Use

**Use this skill when:**
- Analyzing functional connectivity (FC) patterns
- Identifying individuals from functional connectomes
- Linking FC to cognitive/behavioral phenotypes
- Need geometry-aware FC distance metrics
- Comparing resting-state vs task-based fMRI

**Do NOT use for:**
- Structural connectivity analysis (different metrics)
- Simple correlation-based FC (use traditional methods)
- Non-fMRI connectivity data (method optimized for fMRI)

## How To Use

### Step-by-Step Workflow

1. **Functional Connectome Construction**
   - Extract fMRI time series using parcellation scheme
   - Compute functional connectivity matrix (correlation or partial correlation)
   - Normalize FC matrices to positive definite covariance matrices

2. **Alpha-Z Bures-Wasserstein Divergence Setup**
   - Choose alpha parameter (α ∈ (0, 2)) for divergence sensitivity
   - Set Z parameter for regularization
   - Configure geometry-aware weighting

3. **Divergence Computation**
   - Compute Alpha-Z divergence: D_α,Z(FC₁, FC₂) = α Bures-Wasserstein distance + Z regularization
   - Bures-Wasserstein formula: BW(A, B) = √(trace(A + B - 2√(A√B√A)))
   - Apply geometry-aware weighting for Riemannian manifold structure

4. **Phenotypic Trait Extraction**
   - Use divergence-based distances for clustering
   - Link FC patterns to cognitive scores
   - Extract behavioral correlates via regression
   - Validate individual identification accuracy

5. **Cross-Validation**
   - Test on resting-state vs task-based fMRI
   - Compare across parcellation schemes (e.g., Schaefer, AAL)
   - Measure generalization performance

### Key Parameters

| Parameter | Range | Purpose |
|-----------|-------|---------|
| Alpha (α) | 0-2 | Divergence sensitivity |
| Z | >0 | Regularization strength |
| Parcellation | Any | Brain region definition |

### Performance Metrics

- **Fingerprint accuracy:** Individual identification rate
- **Phenotypic correlation:** FC-behavior linkage strength
- **Cross-task generalization:** Rest vs task consistency

## Example Usage

### Individual Identification Pipeline

**Input:**
```
FC matrices from n subjects (resting-state fMRI)
Target: identify individuals across sessions
```

**Steps:**
1. Construct FC matrices for each session
2. Compute Alpha-Z divergence matrix D_ij = D_α,Z(FC_i, FC_j)
3. Use nearest-neighbor matching for identification
4. Validate accuracy across sessions

**Output:** Identification accuracy ~95%+ (reported in paper)

### Cognitive-Behavioral Linkage

**Input:**
```
FC matrices + cognitive scores (e.g., fluid intelligence)
```

**Steps:**
1. Compute Alpha-Z divergence from group template
2. Regress divergence features on cognitive scores
3. Identify significant FC-behavior relationships

**Output:** Enhanced sensitivity vs traditional correlation methods

## Related Skills

- **functional-connectome-fingerprint** - Traditional fingerprinting methods
- **brain-connectivity-distance-metrics** - Other FC distance metrics
- **riemannian-geometry-fc** - Riemannian manifold approaches

## Source

- arXiv:2507.23116v2
- Title: Alpha-Z divergence unveils further distinct phenotypic traits of human brain connectivity fingerprint
- Utility: 0.88
- Authors: Md Kaosar Uddin, Nghi Nguyen, Huajun Huang, Duy Duong-Tran, Jingyi Zheng

## Notes

- Alpha-Z provides geometry-aware FC distance metric
- Better sensitivity for cognitive/behavioral patterns
- Works across resting-state and task-based fMRI
- Scalable for large datasets
- Applications: clinical neuroscience, individualized diagnosis

---

_Created: 2026-04-01_