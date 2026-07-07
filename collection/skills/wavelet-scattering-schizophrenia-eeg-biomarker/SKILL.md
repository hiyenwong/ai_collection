---
name: wavelet-scattering-schizophrenia-eeg-biomarker
description: Wavelet Scattering Transform (WST) framework for interpretable schizophrenia biomarker discovery and classification from resting-state EEG. Multi-order scattering coefficients capture cross-frequency coupling and amplitude modulation dynamics, achieving 90.48% accuracy under strict subject-independent evaluation.
tags: [eeg, schizophrenia, biomarker, wavelet-scattering-transform, cross-frequency-coupling, interpretable-ml, clinical-neuroscience]
arxiv_id: "2607.05282"
date: 2026-07-06
authors: ["Unknown"]
---

# Wavelet Scattering Transform for Schizophrenia EEG Biomarker Discovery

## Core Innovation

**Problem**: Existing EEG-based schizophrenia classifiers rely on static power spectral density (PSD) features that are blind to amplitude modulation dynamics and cross-frequency coupling—phenomena central to schizophrenia pathophysiology. They also suffer from temporal data leakage through epoch-level cross-validation.

**Solution**: Multi-order Wavelet Scattering Transform (WST) with strict Leave-One-Subject-Out (LOSO) cross-validation and SHAP explainability.

## Key Findings

1. **Second-order scattering coefficients** (encoding cross-frequency coupling) dominate discriminative biomarkers
2. **Gamma-band features** most prevalent in the biomarker set
3. **Electrode P3** identified as single most discriminative site
4. **90.48% accuracy** (AUC = 0.9339, sensitivity = 95.56%) under rigorous subject-independent evaluation

## Methodology

### 1. Wavelet Scattering Transform (WST)

The WST is a mathematically principled feature extraction method that captures multi-scale amplitude modulation structure:

**Zeroth-order**: Local average (low-pass)
```
S[0]x(t) = x * φ_J(t)
```

**First-order**: Modulus of wavelet coefficients
```
S[1]x(t) = |x * ψ_j| * φ_J(t)
```

**Second-order**: Modulus of first-order coefficients
```
S[2]x(t) = ||x * ψ_j| * ψ_k| * φ_J(t)
```

**Key Properties**:
- **Translation invariance**: Stable to time shifts
- **Deformation stability**: Robust to small temporal warping
- **Low variance**: Statistical stability for classification
- **Interpretability**: Each order captures specific temporal scales

### 2. Feature Extraction Pipeline

```python
import numpy as np
from kymatio import Scattering1D

# Initialize WST
J = 6  # Number of scales
Q = 8  # Wavelets per octave
scattering = Scattering1D(J=J, shape=signal_length, Q=Q)

# Extract scattering coefficients
# Input: (batch, channels, time)
Sx = scattering(eeg_data)

# Sx contains:
# - S[0]: 1 coefficient per channel (local average)
# - S[1]: J*Q coefficients per channel (first-order moduli)
# - S[2]: J*(J-1)/2*Q^2 coefficients per channel (second-order)
```

### 3. Biomarker Discovery

**Statistical Testing**:
```python
from scipy import stats
from statsmodels.stats.multitest import multipletests

# Subject-level ANOVA for each feature
f_stats, p_values = stats.f_oneway(
    patients_features, controls_features, axis=0
)

# FDR correction
reject, pvals_corrected, _, _ = multipletests(
    p_values, alpha=0.05, method='fdr_bh'
)

significant_biomarkers = np.where(reject)[0]
```

### 4. Classification with Strict LOSO

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut

logo = LeaveOneGroupOut()
classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Subject-level majority voting
for train_idx, test_idx in logo.split(X, y, groups=subject_ids):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    
    classifier.fit(X_train, y_train)
    
    # Epoch-level predictions
    epoch_preds = classifier.predict_proba(X_test)
    
    # Subject-level majority vote
    subject_pred = np.argmax(np.mean(epoch_preds, axis=0))
```

### 5. SHAP Explainability

```python
import shap

# Create explainer
explainer = shap.TreeExplainer(classifier)
shap_values = explainer.shap_values(X_test)

# Identify top biomarkers
top_features = np.argsort(np.abs(shap_values).mean(axis=0))[-10:]
```

## Critical Methodological Points

### 1. Avoid Temporal Data Leakage

**WRONG**: Epoch-level cross-validation
```python
# ❌ This leaks information
for train_idx, test_idx in KFold().split(X_epochs, y_epochs):
    ...
```

**CORRECT**: Subject-level cross-validation
```python
# ✓ No leakage
for train_idx, test_idx in LeaveOneGroupOut().split(X, y, groups=subjects):
    ...
```

### 2. Subject-Level Majority Voting

When classifying multiple epochs per subject, aggregate predictions:
```python
# Get epoch-level probabilities
epoch_probs = classifier.predict_proba(X_subject)

# Majority vote
subject_prediction = np.argmax(np.mean(epoch_probs, axis=0))
```

### 3. Interpretation of Scattering Orders

- **S[0]**: Slow trends, DC offset
- **S[1]**: Amplitude modulations at scale j
- **S[2]**: Cross-frequency coupling between scales j and k

**Schizophrenia-specific**: Second-order coefficients capture disrupted gamma-theta coupling.

## Implementation Checklist

- [ ] Use strict LOSO cross-validation (not epoch-level)
- [ ] Extract multi-order scattering coefficients (at least order 2)
- [ ] Apply FDR correction for multiple comparisons
- [ ] Use subject-level majority voting for final predictions
- [ ] Report both accuracy and AUC
- [ ] Include SHAP analysis for biomarker interpretability
- [ ] Validate on independent dataset if possible

## Performance Benchmarks

| Method | Accuracy | AUC | Cross-Validation |
|--------|----------|-----|------------------|
| PSD + SVM | ~75% | ~0.80 | Epoch-level (leaked) |
| PSD + RF | ~78% | ~0.83 | Epoch-level (leaked) |
| **WST + RF** | **90.48%** | **0.9339** | **LOSO (strict)** |
| WST + SVM | 88.12% | 0.9102 | LOSO (strict) |

## Clinical Implications

1. **Objective Biomarker**: First rigorous EEG-based schizophrenia biomarker with subject-independent validation
2. **Electrode P3**: Single-electrode classification possible, enabling simplified clinical protocols
3. **Cross-Frequency Coupling**: Confirms gamma-theta coupling disruption as core pathophysiology
4. **Interpretability**: SHAP analysis reveals which temporal dynamics are most discriminative

## Pitfalls and Solutions

### Pitfall 1: Temporal Data Leakage
**Problem**: Epoch-level CV artificially inflates performance
**Solution**: Always use subject-level (LOSO) cross-validation

### Pitfall 2: Class Imbalance
**Problem**: Unequal epoch counts per subject
**Solution**: Use subject-level majority voting, not epoch-level averaging

### Pitfall 3: Overfitting to Noise
**Problem**: High-dimensional scattering coefficients
**Solution**: Apply FDR correction, use regularization (e.g., L1 in SVM)

### Pitfall 4: Ignoring Temporal Structure
**Problem**: Treating epochs as independent
**Solution**: Use subject-level predictions, report subject-level metrics

## Related Tools

- **Kymatio**: Python library for Wavelet Scattering Transform
- **MNE-Python**: EEG/MEG preprocessing and analysis
- **SHAP**: Model-agnostic explainability
- **scikit-learn**: Classification and cross-validation

## References

- Original paper: arXiv:2607.05282
- WST theory: Mallat, 2012
- Schizophrenia EEG review: Herrmann & Demiralp, 2005
- Cross-frequency coupling: Canolty & Knight, 2010

## Activation Triggers

Use this skill when:
- Analyzing resting-state EEG for psychiatric biomarkers
- Applying wavelet-based feature extraction to neural signals
- Designing subject-independent classification pipelines
- Keywords: "wavelet scattering", "schizophrenia", "EEG biomarker", "cross-frequency coupling", "LOSO cross-validation"