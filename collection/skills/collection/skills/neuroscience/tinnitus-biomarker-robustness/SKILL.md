---
name: tinnitus-biomarker-robustness
title: "Resting-State EEG Biomarkers of Tinnitus Robust to Cross-Subject and Cross-Platform Variation"
category: neuroscience
source: arXiv:2604.22116
paper_title: "Resting-State EEG Biomarkers of Tinnitus Robust to Cross-Subject and Cross-Platform Variation"
authors:
  - Adyant Balaji
  - Abhinav Uppal
  - Min Suk Lee
  - Yuchen Xu
  - Akihiro Matsuoka
  - Gert Cauwenberghs
date: 2026-04-23
subjects:
  - q-bio.NC (Quantitative Biology - Neurons and Cognition)
  - eess.SP (Electrical Engineering and Systems Science - Signal Processing)
description: >
  Cross-dataset generalizable EEG biomarkers for tinnitus using Koopman operator
  analysis and microstate theory. PCA-based Koopman features outperform microstate
  features in cross-dataset transfer. Koopman eigenvalue magnitude (oscillation
  stability) generalizes across datasets, while eigenvalue phase (frequency) does not.
keywords:
  - tinnitus biomarker
  - EEG biomarker
  - cross-dataset generalization
  - Koopman operator
  - dynamic mode decomposition
  - DMD
  - EEG microstate analysis
  - Wasserstein distance consistency
  - oscillation stability
  - resting-state EEG
  - auditory condition
  - clinical biomarker
  - robust biomarker discovery
  - 耳鸣生物标志物
  - 脑电图生物标志物
  - 跨数据集泛化
  - 库普曼算子
  - 动态模态分解
  - 脑电微状态分析
  - 振荡稳定性
activation_keywords:
  - tinnitus EEG biomarker
  - tinnitus biomarker
  - Koopman EEG
  - EEG microstate tinnitus
  - cross-dataset EEG biomarker
  - dynamic mode decomposition EEG
  - DMD biomarker
  - Wasserstein EEG consistency
  - oscillation stability biomarker
  - 耳鸣脑电标志物
  - 库普曼脑电分析
---

# Tinnitus EEG Biomarker Discovery via Koopman Operator Analysis

## Overview

A systematic approach to discovering **robust, cross-dataset generalizable EEG biomarkers** for tinnitus using **Koopman operator analysis** (via Dynamic Mode Decomposition) and **EEG microstate theory**. The key finding: **Koopman eigenvalue magnitude** (encoding oscillation stability) generalizes across datasets, while eigenvalue phase (encoding oscillation frequency) does not — suggesting that **altered oscillatory decay rates**, rather than frequency shifts, constitute the more robust tinnitus biomarker.

- **arXiv**: [2604.22116](https://arxiv.org/abs/2604.22116)
- **Authors**: Adyant Balaji, Abhinav Uppal, Min Suk Lee, Yuchen Xu, Akihiro Matsuoka, Gert Cauwenberghs
- **Published**: 2026-04-23

---

## Key Contributions

1. **Cross-Dataset Generalization Paradigm** — Biomarker robustness quantified as classification performance across independent datasets (critical for clinical translation).
2. **Koopman Operator Analysis via DMD** — Applied Dynamic Mode Decomposition to dimensionality-reduced EEG to extract single-window dynamical features.
3. **Microstate Analysis** — Identified topographic states, derived transition probability and state duration features.
4. **Wasserstein-Distance Consistency Analysis** — Quantified feature distribution consistency across datasets.
5. **Key Finding**: PCA-based Koopman features yield strongest discrimination metrics across both transfer directions, outperforming microstate-derived features.

---

## Methodology

### 2.1 Data Pipeline

```
Resting-State EEG (2 datasets)
    ↓
Preprocessing (filtering, artifact removal)
    ↓
Dimensionality Reduction (PCA)
    ↓
┌────────────────────┬────────────────────┐
│  Microstate        │  Koopman/DMD       │
│  Analysis          │  Analysis          │
│  - State ID        │  - Eigenvalues     │
│  - Transition prob │  - Eigenvectors    │
│  - State duration  │  - Mode amplitudes │
└────────────────────┴────────────────────┘
    ↓                       ↓
Feature Extraction      Feature Extraction
    ↓                       ↓
┌──────────────────────────────────────────┐
│  Linear SVM Classification               │
│  - Cross-dataset transfer (A→B, B→A)    │
│  - Within-dataset baseline               │
└──────────────────────────────────────────┘
```

### 2.2 Microstate Analysis

EEG microstates are quasi-stable topographic configurations:

```python
def eeg_microstate_analysis(eeg_data, n_states=4):
    """
    Extract EEG microstate features.
    
    Parameters
    ----------
    eeg_data : (n_channels, n_timepoints) preprocessed EEG
    n_states : number of microstate classes (typically 4: A, B, C, D)
    
    Returns
    -------
    features : dict with transition probs, durations, coverage
    """
    from sklearn.cluster import KMeans
    
    # 1. GFP (Global Field Power) peak selection
    gfp = np.std(eeg_data, axis=0)
    peak_idx = find_local_maxima(gfp)
    
    # 2. Clustering to find microstate templates
    topographies = eeg_data[:, peak_idx].T  # (n_peaks, n_channels)
    kmeans = KMeans(n_clusters=n_states, n_init=10)
    kmeans.fit(topographies)
    templates = kmeans.cluster_centers_  # (n_states, n_channels)
    
    # 3. Backfit: assign each timepoint to nearest template
    labels = np.zeros(eeg_data.shape[1], dtype=int)
    for t in range(eeg_data.shape[1]):
        dists = [np.linalg.norm(eeg_data[:, t] - templates[s]) 
                 for s in range(n_states)]
        labels[t] = np.argmin(dists)
    
    # 4. Extract features
    features = {
        'transition_matrix': compute_transition_matrix(labels, n_states),
        'state_durations': compute_state_durations(labels),
        'state_coverage': compute_state_coverage(labels),
        'templates': templates,
    }
    return features
```

### 2.3 Koopman Operator Analysis via DMD

The Koopman operator provides a linear representation of nonlinear dynamics:

```python
def koopman_dmd_features(eeg_data, n_modes=10):
    """
    Extract Koopman operator features via Dynamic Mode Decomposition.
    
    Parameters
    ----------
    eeg_data : (n_channels, n_timepoints) preprocessed EEG
    n_modes : number of DMD modes to retain
    
    Returns
    -------
    features : dict with eigenvalues, modes, amplitudes
    """
    # Step 1: PCA dimensionality reduction
    from sklearn.decomposition import PCA
    pca = PCA(n_components=min(20, eeg_data.shape[0]))
    X = pca.fit_transform(eeg_data.T).T  # (n_components, n_timepoints)
    
    # Step 2: Build data matrices
    X1 = X[:, :-1]  # t=0,...,T-1
    X2 = X[:, 1:]   # t=1,...,T
    
    # Step 3: SVD-based DMD
    U, S, Vt = np.linalg.svd(X1, full_matrices=False)
    
    # Truncate to r modes
    r = min(n_modes, len(S))
    Ur = U[:, :r]
    Sr = np.diag(S[:r])
    Vr = Vt[:r, :]
    
    # Compute Koopman operator approximation
    A_tilde = Ur.T @ X2 @ Vr @ np.linalg.inv(Sr)
    
    # Eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eig(A_tilde)
    
    # DMD modes
    modes = X2 @ Vr @ np.linalg.inv(Sr) @ eigenvectors
    
    # Compute amplitudes (projection onto initial condition)
    b = np.linalg.pinv(modes) @ X[:, 0]
    
    features = {
        'eigenvalues': eigenvalues[:r],      # Complex: encodes frequency + decay
        'eigenvalue_magnitude': np.abs(eigenvalues[:r]),  # Oscillation stability
        'eigenvalue_phase': np.angle(eigenvalues[:r]),     # Oscillation frequency
        'modes': modes[:, :r],
        'amplitudes': b[:r],
    }
    return features
```

### 2.4 Key Insight: Magnitude vs. Phase

```python
def wasserstein_consistency_analysis(features_dataset1, features_dataset2):
    """
    Compute Wasserstein distance for feature consistency across datasets.
    
    Lower distance = more consistent (robust) across datasets.
    
    Parameters
    ----------
    features_dataset1, features_dataset2 : Koopman feature dicts
    
    Returns
    -------
    consistency : dict with Wasserstein distances per feature type
    """
    from scipy.stats import wasserstein_distance
    
    consistency = {}
    
    # Eigenvalue magnitude consistency (oscillation stability)
    mag_dist = wasserstein_distance(
        features_dataset1['eigenvalue_magnitude'],
        features_dataset2['eigenvalue_magnitude']
    )
    consistency['magnitude_wasserstein'] = mag_dist
    
    # Eigenvalue phase consistency (oscillation frequency)
    phase_dist = wasserstein_distance(
        features_dataset1['eigenvalue_phase'],
        features_dataset2['eigenvalue_phase']
    )
    consistency['phase_wasserstein'] = phase_dist
    
    # Interpretation
    consistency['robust_biomarker'] = 'magnitude' if mag_dist < phase_dist else 'phase'
    
    return consistency
```

---

## Results Summary

| Feature Type | Cross-Dataset A→B | Cross-Dataset B→A | Wasserstein Consistency |
|-------------|-------------------|-------------------|------------------------|
| **PCA-Koopman** | **Best** | **Best** | Magnitude: ρ̄ = 0.685 ✓ |
| Microstate (transition) | Moderate | Moderate | Higher variability |
| Microstate (duration) | Lower | Lower | Higher variability |
| Koopman phase | Poor | Poor | ρ̄ = 1.583 ✗ |

### Key Finding

- **Koopman eigenvalue magnitude** (encoding **oscillation stability/decay rate**) → ρ̄ = 0.685 (consistent across datasets)
- **Koopman eigenvalue phase** (encoding **oscillation frequency**) → ρ̄ = 1.583 (inconsistent across datasets)

**Conclusion**: Altered oscillatory decay rates, not frequency shifts, constitute the more robust tinnitus biomarker.

---

## Clinical Implications

1. **Objective Tinnitus Diagnosis** — Koopman-based EEG biomarkers enable non-invasive, objective tinnitus assessment.
2. **Cross-Platform Robustness** — Features generalize across different EEG acquisition systems, essential for clinical deployment.
3. **Mechanistic Insight** — Tinnitus is associated with altered oscillatory stability (decay rates) rather than frequency shifts, informing targeted interventions.
4. **Biomarker Selection** — When developing clinical biomarkers, prioritize Koopman eigenvalue magnitude over phase or microstate features for cross-dataset generalization.

---

## Implementation Pipeline

```python
def tinnitus_biomarker_pipeline(eeg_data_tinnitus, eeg_data_control, 
                                 target_eeg_data, target_labels):
    """
    Full pipeline: train on dataset A, test on dataset B.
    """
    from sklearn.svm import LinearSVC
    from sklearn.preprocessing import StandardScaler
    
    # Extract Koopman features
    features_tinnitus = []
    for eeg in eeg_data_tinnitus:
        f = koopman_dmd_features(eeg, n_modes=10)
        features_tinnitus.append(np.concatenate([
            f['eigenvalue_magnitude'],
            f['amplitudes'].real,
            f['amplitudes'].imag,
        ]))
    
    features_control = []
    for eeg in eeg_data_control:
        f = koopman_dmd_features(eeg, n_modes=10)
        features_control.append(np.concatenate([
            f['eigenvalue_magnitude'],
            f['amplitudes'].real,
            f['amplitudes'].imag,
        ]))
    
    # Build training set
    X_train = np.array(features_tinnitus + features_control)
    y_train = np.array([1]*len(features_tinnitus) + [0]*len(features_control))
    
    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    # Train SVM
    svm = LinearSVC(C=1.0)
    svm.fit(X_train_scaled, y_train)
    
    # Test on target dataset
    features_target = []
    for eeg in target_eeg_data:
        f = koopman_dmd_features(eeg, n_modes=10)
        features_target.append(np.concatenate([
            f['eigenvalue_magnitude'],
            f['amplitudes'].real,
            f['amplitudes'].imag,
        ]))
    
    X_test = scaler.transform(np.array(features_target))
    predictions = svm.predict(X_test)
    accuracy = np.mean(predictions == target_labels)
    
    return accuracy, svm, scaler
```

---

## References

```
@article{balaji2026tinnitus,
  title = {Resting-State EEG Biomarkers of Tinnitus Robust to Cross-Subject and Cross-Platform Variation},
  author = {Balaji, Adyant and Uppal, Abhinav and Lee, Min Suk and Xu, Yuchen and Matsuoka, Akihiro and Cauwenberghs, Gert},
  journal = {arXiv preprint},
  year = {2026},
  eprint = {2604.22116},
  primaryClass = {q-bio.NC},
  secondaryClass = {eess.SP},
  url = {https://arxiv.org/abs/2604.22116},
  date = {2026-04-23}
}
```

---

## Related Skills

- `eeg-foundation-model-adapters`
- `eeg-hopfield-emotion-energy`
- `hermes-brain-connectivity`
- `eeg-brain-connectivity-bci`
- `interpretable-eeg-biomarkers-parkinsons`
