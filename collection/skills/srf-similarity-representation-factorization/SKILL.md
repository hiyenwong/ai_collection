---
name: srf-similarity-representation-factorization
description: Similarity-Based Representation Factorization (SRF) methodology for recovering low-dimensional, interpretable embeddings from similarity matrices. Use when analyzing neural, behavioral, or AI representations; extracting core dimensions from representational similarity analysis (RSA); comparing representations across brains, behavior, and models; or performing factorization on sparse/incomplete similarity data. Applicable to neuroscience, psychology, cognitive science, and AI representation studies.
license: Complete terms in LICENSE.txt
---

# Similarity-Based Representation Factorization (SRF)

## Overview

SRF is a computational method for recovering low-dimensional, non-negative, interpretable embeddings from similarity matrices derived from measured data. It addresses key limitations in current representation analysis methods by providing:

- **Dimension recovery**: Extract interpretable latent dimensions shaping representations
- **Sparse data handling**: Works with incomplete similarity matrices
- **Cross-domain applicability**: Neural data, behavioral measures, AI model outputs
- **Interpretability**: Non-negative factors with clear semantic meaning

## Core Methodology

### The Mathematical Framework

SRF factorizes similarity matrices S into:
```
S ≈ W × W^T
```

Where:
- **S**: Similarity matrix (n×n) from stimuli comparisons
- **W**: Non-negative embedding matrix (n×k), k = number of dimensions
- **k**: Low-dimensional latent factors (typically 5-20)

### Key Properties

1. **Non-negativity**: All entries in W ≥ 0, enabling interpretability
2. **Low-rank**: k << n, capturing essential structure
3. **Interpretability**: Each column of W represents a semantic dimension
4. **Robustness**: Handles missing entries via optimization constraints

### Algorithm Components

1. **Initialization**: 
   - Choose number of dimensions k
   - Initialize W randomly or via PCA/SVD projection

2. **Optimization**:
   - Minimize reconstruction error: ||S - W×W^T||_F
   - Enforce non-negativity constraints
   - Handle missing entries with weighted loss

3. **Interpretation**:
   - Examine W columns as dimension vectors
   - Map dimensions to semantic labels via stimuli properties
   - Validate with independent behavioral/neural measures

## Application Workflow

### 1. Data Collection Phase

**Input Types**:
- Neural similarity matrices: fMRI RDMs, EEG patterns, spike correlations
- Behavioral similarity matrices: confusion matrices, subjective ratings
- AI model similarity matrices: feature space distances, output correlations

**Quality Requirements**:
- Minimum coverage: 30-50% of similarity matrix entries
- Reliable similarity estimates (multiple measurements or validated metrics)
- Standardized stimulus set across all domains

### 2. Dimensionality Selection

**Methods to determine k**:
- **Cross-validation**: Split data, reconstruct, measure error
- **Stability analysis**: Bootstrap similarity matrix, check factor consistency
- **Interpretability threshold**: Minimum k that yields coherent factors
- **Prior knowledge**: Use domain expertise (e.g., known cognitive dimensions)

**Typical ranges**:
- Simple perception tasks: k = 3-5
- Complex cognitive tasks: k = 10-15
- Multi-domain comparisons: k = 15-20

### 3. Factorization Execution

**Step-by-step**:

1. Prepare similarity matrix S:
   ```python
   # Normalize similarity scores
   S_normalized = (S - S.min()) / (S.max() - S.min())
   
   # Handle missing entries (mark as NaN)
   S_with_missing = np.where(mask == 0, np.nan, S_normalized)
   ```

2. Apply SRF optimization:
   ```python
   # Initialize with random non-negative matrix
   W_init = np.random.rand(n_stimuli, k_dimensions)
   
   # Optimize with missing entry handling
   W_optimal = optimize_srf(S_with_missing, W_init, 
                             max_iter=1000, 
                             tolerance=1e-6)
   ```

3. Extract dimension scores:
   ```python
   # Each stimulus's score on each dimension
   dimension_scores = W_optimal  # n × k matrix
   
   # Identify dimension loadings
   for i in range(k_dimensions):
       high_loading_stimuli = stimuli[dimension_scores[:, i] > threshold]
       interpret_dimension(i, high_loading_stimuli)
   ```

### 4. Interpretation and Validation

**Dimension interpretation strategies**:

1. **Stimulus inspection**:
   - Identify stimuli with high scores on each dimension
   - Find common properties among high-loading stimuli
   - Assign semantic labels (e.g., "animacy", "size", "complexity")

2. **Correlation analysis**:
   ```python
   # Correlate dimensions with known stimulus properties
   for property in stimulus_metadata:
       r = correlate(dimension_scores[:, dim_idx], property_values)
       if r > 0.7:
           label_dimension(dim_idx, property)
   ```

3. **Cross-domain validation**:
   - Compare neural dimensions with behavioral ratings
   - Validate AI model dimensions against human judgments
   - Check dimension consistency across datasets

**Quality metrics**:
- Reconstruction accuracy: Correlation between S and W×W^T
- Factor stability: Bootstrap consistency > 0.8
- Behavioral prediction: Dimensions correlate with independent measures
- Interpretability: Clear semantic labels for all factors

## Key Applications

### Neuroscience

**Use cases**:
- Extract cognitive dimensions from fMRI RDMs
- Identify perceptual axes in neural encoding spaces
- Compare neural representations across brain regions
- Link neural dimensions to behavioral performance

**Example workflow**:
```
1. Collect fMRI RDM for stimulus set (n stimuli)
2. Apply SRF to extract k dimensions
3. Interpret dimensions via stimulus properties
4. Validate with behavioral ratings on same stimuli
5. Map dimensions to brain regions via voxel correlations
```

### Cognitive Psychology

**Use cases**:
- Discover latent dimensions in subjective similarity judgments
- Factorize confusion matrices to identify error patterns
- Extract cognitive axes from categorization behavior
- Compare mental representations across tasks

### AI and Machine Learning

**Use cases**:
- Analyze DNN representation spaces
- Extract interpretable dimensions from model embeddings
- Compare AI representations to human neural/behavioral data
- Identify conceptual axes in language model outputs

**Example**: Analyzing vision model representations
```python
# Extract features from CNN for stimulus set
features = model.extract_features(stimuli)

# Compute similarity matrix
S_model = compute_cosine_similarity(features)

# Apply SRF
W_model = optimize_srf(S_model)

# Compare with human dimensions
correlation = correlate(W_model, W_human_neural)
print(f"Brain-model alignment: {correlation:.3f}")
```

## Advantages over Traditional RSA

### Compared to Raw Similarity Analysis

| Metric | Traditional RSA | SRF |
|--------|-----------------|-----|
| Dimension access | No (only pairwise) | Yes (k interpretable factors) |
| Missing data | Requires complete matrix | Handles sparsity |
| Interpretability | Limited | High (non-negative, semantic) |
| Statistical power | Lower (matrix comparison) | Higher (factor tests) |
| Exploratory analysis | Difficult | Easy (visualize dimensions) |

### Compared to PCA/SVD

| Aspect | PCA/SVD | SRF |
|--------|---------|-----|
| Non-negativity | No | Yes |
| Interpretability | Mixed signs | Clear positive factors |
| Missing data | Requires imputation | Direct optimization |
| Semantic clarity | Abstract components | Labelable dimensions |

## Implementation Considerations

### Computational Requirements

- **Time complexity**: O(n²k) per iteration, typically < 1 min for n < 100
- **Memory**: O(n²) for similarity matrix storage
- **Optimization**: Gradient descent or alternating least squares

### Data Requirements

- **Minimum stimuli**: 20-30 (for stable factorization)
- **Similarity coverage**: > 30% of matrix entries
- **Reliability**: Similarity estimates with known variance

### Pitfalls to Avoid

1. **Overfitting**: Choose k via cross-validation, not arbitrary values
2. **Missing data bias**: Account for systematic missingness patterns
3. **Interpretation overreach**: Validate dimensions with independent data
4. **Dimension collapse**: Ensure factors are distinct (correlation < 0.5)

## Integration with Existing Workflows

### NEST Simulator Integration

For neural network simulations:
```python
# Generate spike trains from NEST model
spike_data = nest_simulation(stimuli)

# Compute spike pattern similarity
S_spikes = spike_pattern_similarity(spike_data)

# Apply SRF to neural dynamics
W_neural = optimize_srf(S_spikes)

# Compare with experimental neural dimensions
alignment = correlate(W_neural, W_fMRI)
```

### Brain Imaging Analysis

For fMRI/EEG data:
```python
# Standard preprocessing
neural_data = preprocess_fmri(raw_data)

# Compute RDM per ROI
for roi in brain_regions:
    S_roi = compute_RDM(neural_data[roi])
    W_roi = optimize_srf(S_roi)
    dimension_profiles[roi] = W_roi

# Visualize dimension maps
plot_dimension_brain_maps(dimension_profiles)
```

## Advanced Techniques

### Multi-Dataset Fusion

Factorize similarity matrices from multiple sources simultaneously:
```python
# Joint factorization across domains
W_shared = optimize_joint_srf([S_neural, S_behavioral, S_model],
                               shared_dimensions=True)

# Domain-specific factors
W_neural_specific = optimize_srf(S_neural - W_shared @ W_shared.T)
```

### Hierarchical Factorization

Extract dimensions at multiple abstraction levels:
```python
# Level 1: Broad categories
W_high = optimize_srf(S, k=5)

# Level 2: Fine distinctions
residual_S = S - W_high @ W_high.T
W_low = optimize_srf(residual_S, k=10)
```

## References and Further Reading

### Original Paper

**arXiv:2605.26921** - "Revealing the core dimensions underlying representations in brains, behavior and AI"
- Authors: Florian P. Mahner, Ka Chun Lam, Francisco Pereira, Martin N. Hebart
- Submitted: May 26, 2026
- DOI: https://doi.org/10.48550/arXiv.2605.26921

### Related Methods

- Representational Similarity Analysis (RSA) - Kriegeskorte et al., 2008
- Non-negative Matrix Factorization (NMF) - Lee & Seung, 1999
- Multi-dimensional scaling (MDS) - classical similarity visualization

### Validation Studies

See paper for:
- Simulation studies on sparse data performance
- Neural dataset analyses (fMRI, EEG)
- Behavioral validation experiments
- AI model representation comparisons

## Activation Keywords

- similarity-based representation factorization
- SRF
- representation factorization
- similarity matrix factorization
- neural dimension extraction
- behavioral dimension recovery
- AI representation analysis
- representational similarity analysis enhancement
- interpretability of representations
- sparse similarity matrix analysis

## Example Use Cases

### Use Case 1: Neural Representation Analysis

**Scenario**: You have fMRI RDMs for 50 visual stimuli across multiple brain regions.

**Workflow**:
1. Compute similarity matrices per ROI
2. Apply SRF with k=10 dimensions
3. Interpret dimensions via stimulus properties
4. Validate with behavioral animacy/size ratings
5. Compare dimension profiles across regions

**Expected outcome**: 10 interpretable dimensions (animacy, size, shape, color, texture, complexity, etc.) that predict behavior and differ across visual processing stages.

### Use Case 2: Brain-Model Alignment

**Scenario**: Compare CNN representations to human fMRI patterns.

**Workflow**:
1. Extract features from CNN layer
2. Compute model similarity matrix
3. Apply SRF to both neural and model data
4. Correlate dimension scores across domains
5. Identify shared vs. unique dimensions

**Expected outcome**: Quantified alignment scores per dimension, revealing which conceptual axes are shared between brains and models.

## Summary

SRF provides a principled approach to extracting interpretable dimensions from similarity data. Key strengths:

- **Reveals hidden structure**: Go beyond pairwise similarities to latent factors
- **Handles real-world data**: Works with sparse, incomplete matrices
- **Cross-domain applicable**: Neuroscience, psychology, AI
- **Interpretability**: Non-negative, labelable dimensions
- **Validation-ready**: Test dimensions against independent measures

Use SRF when you need to understand **what dimensions** shape representations, not just **how similar** stimuli are.