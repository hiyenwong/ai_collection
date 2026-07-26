---
name: zeta-law-biomedical-scaling
description: "Zeta Law framework for predicting data scaling in biomedical discovery. Uses spectral covariance structure and Riemann zeta function to model cross-modal discoverability, predicting when models transition from underparameterized to overparameterized regimes. Activation: zeta law, biomedical data scaling, cross-modal discoverability, Riemann zeta function, scaling laws, data efficiency."
---

# Zeta Law: Data Scaling in Biomedical Discovery

> Framework for predicting when additional data will improve performance in biomedical AI, using spectral covariance analysis and the Riemann zeta function.

## Metadata
- **Source**: arXiv:2604.17581
- **Authors**: Paul M. Thompson
- **Published**: 2026-04-19
- **Categories**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Neurons and Cognition (q-bio.NC)

## Core Methodology

### Problem Statement
As biomedical datasets scale to millions of samples and AI models grow, progress depends on predicting when additional data will substantially improve performance. Current approaches rely on empirical scaling curves with limited theoretical guidance.

### The Zeta Law
A scaling-law framework for cross-modal discoverability based on three key components:

1. **Spectral Structure of Data Covariance Operators**
2. **Task-Aligned Signal Projections**
3. **Learned Representations**

### Mathematical Foundation

#### Performance Metrics as Spectral Accumulation
Many performance metrics (including AUC) can be expressed as cumulative signal-to-noise energy across identifiable spectral modes:

```
Performance = Σᵢ (Signalᵢ² / Noiseᵢ²) = Σᵢ (aligned_signal_energyᵢ / covariance_modeᵢ)
```

#### Zeta-Like Scaling Law
Under mild assumptions, this accumulation follows a power-law governed by covariance spectra decay:

```
Performance(n) ∝ ζ(s) = Σᵢ₌₁ⁿ i⁻ˢ
```

Where the Riemann zeta function naturally emerges from power-law decay of covariance spectra.

## Key Insights

### Representation Learning Effects
Sparse models, low-rank embeddings, and multimodal contrastive objectives improve sample efficiency by:
- Concentrating useful signal into earlier stable modes
- Steepening spectral decay
- Shifting scaling curves upward

### Cross-Over Regimes
The framework predicts regimes where:
- **Small samples**: Simpler models perform best
- **Large samples**: Higher-capacity or multimodal encoders outperform
- **Transition point**: Predictable from spectral properties

### Applications Covered
- Multimodal disease classification
- Imaging genetics
- Functional MRI
- Topological data analysis

## Implementation Guide

### Prerequisites
- Understanding of spectral decomposition
- Access to covariance structure of data
- Familiarity with representation learning methods

### Computing the Zeta Law

#### Step 1: Spectral Decomposition
```python
import numpy as np
from scipy.linalg import eigh

def compute_zeta_law(X, y, n_modes=100):
    """
    Compute Zeta Law scaling from data covariance
    
    Args:
        X: Data matrix (n_samples × n_features)
        y: Target labels
        n_modes: Number of spectral modes to analyze
    
    Returns:
        zeta_curve: Predicted performance scaling
        spectral_decay: Power-law exponent
    """
    # Compute data covariance
    cov = np.cov(X.T)
    
    # Eigenvalue decomposition
    eigenvalues, eigenvectors = eigh(cov)
    eigenvalues = eigenvalues[::-1]  # Sort descending
    
    # Task-aligned signal projection
    signal_projection = np.abs(eigenvectors.T @ y_mean_signal) ** 2
    
    # Cumulative SNR
    snr_accumulation = np.cumsum(signal_projection[:n_modes] / eigenvalues[:n_modes])
    
    # Fit power-law decay
    spectral_decay = fit_power_law(eigenvalues[:n_modes])
    
    # Zeta-like prediction
    zeta_curve = compute_riemann_zeta_approx(spectral_decay, n_modes)
    
    return zeta_curve, spectral_decay
```

#### Step 2: Cross-Modal Scaling Prediction
```python
def predict_crossover_point(modality1_spectrum, modality2_spectrum, 
                           modality1_signal, modality2_signal):
    """
    Predict when multimodal models outperform unimodal
    """
    # Compute zeta curves for each modality
    zeta1 = compute_zeta_curve(modality1_spectrum, modality1_signal)
    zeta2 = compute_zeta_curve(modality2_spectrum, modality2_signal)
    
    # Multimodal (assume signal concentration)
    combined_spectrum = combine_spectra(modality1_spectrum, modality2_spectrum)
    combined_signal = concentrate_signal(modality1_signal, modality2_signal)
    zeta_multi = compute_zeta_curve(combined_spectrum, combined_signal)
    
    # Find crossover
    crossover_sample_size = find_intersection(zeta1, zeta_multi)
    
    return crossover_sample_size
```

### Practical Considerations

#### When Zeta Law Applies
- **Power-law spectral decay**: Most natural signals
- **Linear signal accumulation**: Additive contribution of modes
- **Mild distributional assumptions**: Beyond Gaussian

#### When It May Not Apply
- Exponential (not power-law) spectral decay
- Strong non-linear interactions between modes
- Discrete spectral gaps

## Applications

### Biomedical Data Scaling
#### Use Case: Disease Classification
```python
# Example: Multimodal Alzheimer's prediction
fmri_spectrum = compute_data_spectrum(fmri_data)
pet_spectrum = compute_data_spectrum(pet_data)
cognitive_spectrum = compute_data_spectrum(cognitive_scores)

# Predict when 3-modal > 2-modal > 1-modal
threshold_1_to_2 = predict_crossover(fmri_spectrum, pet_spectrum, ...)
threshold_2_to_3 = predict_crossover(combined_2mod, cognitive_spectrum, ...)

print(f"Add PET data when N > {threshold_1_to_2}")
print(f"Add cognitive data when N > {threshold_2_to_3}")
```

### Experimental Design
- **Sample size planning**: Predict performance before data collection
- **Cost-benefit analysis**: Is more data worth the cost?
- **Multi-site pooling**: When to combine datasets vs. keep separate

### Model Selection
- **Underparameterized regime**: Prefer simpler models
- **Overparameterized regime**: Complex models with proper regularization
- **Optimal architecture**: Match capacity to predicted scaling

## Pitfalls

### Common Misconceptions
1. **Universal power-law**: Not all data has power-law spectra
2. **Linear accumulation**: Mode interactions can be non-additive
3. **Static spectra**: Real data may have sample-dependent structure

### Validation Requirements
- Check spectral decay empirically
- Validate predictions on hold-out data
- Account for finite-sample effects

### Best Practices
- Always verify power-law assumption
- Use robust estimators for covariance
- Bootstrap confidence intervals for predictions

## Related Skills
- brain-dit-fmri-foundation-model
- multi-view-o-information-brain-dynamics
- functional-connectivity-graph-neural-networks

## Mathematical Background

### Riemann Zeta Function
```
ζ(s) = Σₙ₌₁^∞ n^(-s)  for Re(s) > 1
```

The zeta function emerges naturally from power-law decay: if covariance eigenvalues decay as λᵢ ∝ i^(-α), then cumulative SNR follows a zeta-like form.

### Spectral Analysis
- **Karhunen-Loève Transform**: Optimal linear decomposition
- **Mercer's Theorem**: Spectral decomposition of covariance operators
- **Power-Law Universality**: Common in natural signals (1/f noise, etc.)

## References
- Thompson, P. M. (2026). How Much Data is Enough? The Zeta Law of Discoverability in Biomedical Data, featuring the enigmatic Riemann zeta function. arXiv:2604.17581.
- Riemann, B. (1859). Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse.
- Donoho, D. L. (2006). Compressed sensing. IEEE Transactions on Information Theory.

## Activation Keywords
- zeta law biomedical scaling
- cross-modal discoverability
- Riemann zeta function data
- spectral covariance analysis
- data efficiency prediction
- scaling law transition
