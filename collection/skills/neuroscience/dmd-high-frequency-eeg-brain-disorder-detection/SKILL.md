---
name: dmd-high-frequency-eeg-brain-disorder-detection
version: 1.0.0
description: Detecting high-frequency brain disorder signals using Dynamic Mode Decomposition (DMD) from EEG data. Extracts consistent dynamical changes in high-frequency bands to identify neurological patterns distinguishing clinical groups like alcohol-dependent patients from controls.
tags:
  - neuroscience
  - eeg
  - dynamic-mode-decomposition
  - brain-disorders
  - signal-processing
  - machine-learning
author: Jacob Kang, Jong-Hyeon Seo
license: arXiv license
arxiv_id: 2608.02804
date: 2026-08-03
---

# DMD High-Frequency EEG Brain Disorder Detection

## Overview
This methodology applies **Dynamic Mode Decomposition (DMD)** to extract consistent and persistent dynamical changes in the high-frequency band from neurologically relevant EEG channels. The approach identifies high-frequency DMD modes as features that can distinguish between different clinical populations, such as alcohol-dependent groups versus control groups.

## Core Contributions

### 1. High-Frequency DMD Feature Extraction
- Utilizes DMD to decompose EEG signals into dynamic modes
- Focuses specifically on high-frequency bands where brain disorder signals manifest
- Extracts consistent dynamical patterns that persist across time

### 2. Statistical Validation Framework
- Implements random distribution tests to validate feature consistency
- Approximately 70% of samples show consistent high-frequency dynamics within specific channels
- Provides statistical confidence in detected patterns

### 3. Clinical Classification Capability
- PCA components of validated DMD features form consistent patterns distinguishing clinical groups
- Successfully differentiates alcohol-dependent patients from control groups
- Demonstrates practical utility for neurological diagnosis

## Implementation Steps

### Step 1: Data Preprocessing
```python
import numpy as np
from pydmd import DMD

def preprocess_eeg_high_freq(eeg_data, fs=256, high_freq_range=(30, 100)):
    """
    Extract high-frequency components from EEG data
    
    Args:
        eeg_data: Raw EEG data [channels, time_points]
        fs: Sampling frequency
        high_freq_range: High-frequency band range (default: 30-100 Hz)
    
    Returns:
        filtered_data: High-frequency filtered EEG data
    """
    from scipy import signal
    
    # Design bandpass filter for high-frequency range
    nyquist = fs / 2
    low = high_freq_range[0] / nyquist
    high = high_freq_range[1] / nyquist
    b, a = signal.butter(4, [low, high], btype='band')
    
    # Apply filter to each channel
    filtered_data = np.zeros_like(eeg_data)
    for ch in range(eeg_data.shape[0]):
        filtered_data[ch] = signal.filtfilt(b, a, eeg_data[ch])
    
    return filtered_data
```

### Step 2: Dynamic Mode Decomposition
```python
def extract_dmd_modes(eeg_high_freq, svd_rank=None, exact=True):
    """
    Apply DMD to high-frequency EEG data
    
    Args:
        eeg_high_freq: High-frequency filtered EEG data [channels, time_points]
        svd_rank: Rank for SVD truncation (None for optimal rank selection)
        exact: Use exact DMD or projected DMD
    
    Returns:
        dmd_result: DMD object with modes, eigenvalues, and amplitudes
    """
    dmd = DMD(svd_rank=svd_rank, exact=exact)
    dmd.fit(eeg_high_freq)
    return dmd
```

### Step 3: Feature Table Construction
```python
def build_feature_table(dmd_results_list, channels_of_interest):
    """
    Construct feature table from DMD results across multiple subjects
    
    Args:
        dmd_results_list: List of DMD objects from multiple subjects
        channels_of_interest: Neurologically relevant EEG channels
    
    Returns:
        feature_table: Matrix of DMD mode features [subjects, features]
    """
    features = []
    for dmd in dmd_results_list:
        # Extract high-frequency DMD modes
        high_freq_modes = []
        for i, eig in enumerate(dmd.eigs):
            freq = np.abs(np.log(eig) / (2 * np.pi))
            if freq > 30:  # High-frequency threshold
                high_freq_modes.extend(dmd.modes[:, i][channels_of_interest].flatten())
        features.append(high_freq_modes)
    
    return np.array(features)
```

### Step 4: Statistical Validation
```python
def random_distribution_test(feature_table, alpha=0.05):
    """
    Perform random distribution test to validate feature consistency
    
    Args:
        feature_table: Feature matrix [subjects, features]
        alpha: Significance level
    
    Returns:
        valid_features: Boolean mask indicating consistent features
        p_values: P-values for each feature
    """
    from scipy import stats
    
    p_values = []
    for feature_idx in range(feature_table.shape[1]):
        feature_values = feature_table[:, feature_idx]
        # Test against random distribution
        _, p_val = stats.normaltest(feature_values)
        p_values.append(p_val)
    
    valid_features = np.array(p_values) < alpha
    return valid_features, np.array(p_values)
```

### Step 5: Classification Pipeline
```python
def classify_brain_disorders(feature_table, labels, valid_mask):
    """
    Classify brain disorders using validated DMD features
    
    Args:
        feature_table: Feature matrix [subjects, features]
        labels: Clinical labels (e.g., 0=control, 1=alcohol-dependent)
        valid_mask: Boolean mask for validated features
    
    Returns:
        classification_results: Dictionary with performance metrics
    """
    from sklearn.decomposition import PCA
    from sklearn.model_selection import cross_val_score
    from sklearn.svm import SVC
    
    # Select validated features
    X_valid = feature_table[:, valid_mask]
    
    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=min(10, X_valid.shape[1]))
    X_pca = pca.fit_transform(X_pca)
    
    # Train classifier
    clf = SVC(kernel='rbf', random_state=42)
    scores = cross_val_score(clf, X_pca, labels, cv=5)
    
    return {
        'accuracy': scores.mean(),
        'std': scores.std(),
        'pca_explained_variance': pca.explained_variance_ratio_,
        'feature_consistency_rate': valid_mask.sum() / len(valid_mask)
    }
```

## Usage Guidelines

### When to Use
- **EEG analysis for neurological disorders**: When analyzing EEG data to detect brain disorder signatures
- **High-frequency signal detection**: When interested in gamma-band and higher frequency neural oscillations
- **Clinical group differentiation**: When needing to distinguish between patient groups and controls
- **Dynamical systems approach**: When traditional spectral analysis is insufficient for capturing temporal dynamics

### Key Parameters
- **High-frequency range**: Typically 30-100 Hz for gamma oscillations
- **SVD rank**: Controls dimensionality; use optimal rank selection for best results
- **Channels of interest**: Focus on neurologically relevant electrodes based on clinical hypothesis
- **Statistical threshold**: Alpha level for validation (typically 0.05)

### Validation Metrics
- **Feature consistency rate**: Percentage of features passing random distribution test (~70% reported)
- **Classification accuracy**: Performance in distinguishing clinical groups
- **PCA explained variance**: Amount of variance captured by principal components

## Pitfalls and Considerations

### Common Issues
1. **Noise sensitivity**: High-frequency bands are more susceptible to artifacts
   - **Solution**: Apply rigorous artifact rejection before DMD analysis
   
2. **Channel selection bias**: Results depend heavily on channel selection
   - **Solution**: Use anatomically/clinically justified channel selection or systematic exploration

3. **Overfitting risk**: High-dimensional feature space with limited samples
   - **Solution**: Apply proper cross-validation and regularization

### Best Practices
1. **Preprocessing**: Apply appropriate filtering and artifact removal
2. **Validation**: Always perform statistical validation of extracted features
3. **Replication**: Validate findings across independent datasets when possible
4. **Interpretability**: Combine with traditional EEG analysis for comprehensive understanding

## Applications

### Primary Applications
- **Alcohol dependence detection**: Differentiating alcohol-dependent patients from controls
- **Epilepsy monitoring**: Detecting pre-seizure high-frequency patterns
- **Cognitive impairment assessment**: Identifying neural signatures of cognitive decline
- **Psychiatric disorder diagnosis**: Characterizing neural dynamics in psychiatric conditions

### Extended Applications
- **Brain-computer interfaces**: Using high-frequency dynamics for BCI control signals
- **Neurofeedback**: Providing real-time feedback based on high-frequency patterns
- **Drug response monitoring**: Tracking changes in neural dynamics during treatment

## References
- Kang, J., & Seo, J. (2026). Detecting high-frequency brain disorder signals using dynamic mode decomposition from EEG. arXiv:2608.02804 [q-bio.NC].
- Tu, J. H., Rowley, C. W., Luchtenburg, D. M., Brunton, S. L., & Kutz, J. N. (2014). On dynamic mode decomposition: Theory and applications. Journal of Computational Dynamics, 1(2), 391-421.
- Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing equations from data by sparse identification of nonlinear dynamical systems. Proceedings of the National Academy of Sciences, 113(15), 3932-3937.

## Activation Keywords
- DMD EEG analysis
- high-frequency brain signals
- dynamic mode decomposition neuroscience
- EEG brain disorder detection
- gamma oscillation analysis
- neurological classification EEG
- DMD feature extraction
- brain dynamics decomposition