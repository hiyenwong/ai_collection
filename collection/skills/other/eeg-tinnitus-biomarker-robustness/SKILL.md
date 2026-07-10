---
name: eeg-tinnitus-biomarker-robustness
description: "EEG-based tinnitus biomarker identification methodology with cross-dataset generalization. Uses microstate analysis and Koopman operator analysis via DMD to extract robust neural signatures. Focuses on Koopman eigenvalue magnitude for oscillation stability. Applications: clinical diagnostics, cross-platform tinnitus detection. Triggers: tinnitus biomarker, EEG microstate, Koopman EEG, cross-dataset generalization"
---

# EEG-Based Tinnitus Biomarker Robust to Cross-Subject and Cross-Platform Variation

> A methodology for identifying robust EEG-based tinnitus biomarkers using microstate analysis and Koopman operator dynamics, with emphasis on cross-dataset generalization through Koopman eigenvalue magnitude features.

## Metadata
- **Source**: arXiv:2604.22116
- **Authors**: Adyant Balaji, Abhinav Uppal, Min Suk Lee, Yuchen Xu, et al.
- **Published**: 2026-04-23
- **Category**: Neuroscience, Clinical Neurophysiology

## Core Methodology

### Key Innovation
This work addresses the critical challenge of cross-dataset generalization for EEG-based tinnitus biomarkers. The methodology combines **microstate analysis** (quasi-stable topographic configurations) with **Koopman operator analysis** (Dynamic Mode Decomposition) to identify robust neural signatures that generalize across different EEG platforms and populations.

### Technical Framework

#### 1. Microstate Analysis
- **Purpose**: Characterize quasi-stable topographic configurations in EEG
- **Features Extracted**:
  - Transition probability matrices
  - State duration statistics
- **Significance**: Captures large-scale brain network dynamics associated with tinnitus

#### 2. Koopman Operator Analysis via DMD
- **Approach**: Apply Dynamic Mode Decomposition (DMD) to dimensionality-reduced EEG data
- **Key Features**:
  - **Koopman eigenvalue magnitude**: Encodes oscillation stability (ρ̄ = 0.685, generalizes well)
  - **Koopman eigenvalue phase**: Encodes oscillation frequency (ρ̄ = 1.583, does not generalize)
- **Insight**: Altered oscillatory decay rates constitute more robust tinnitus biomarkers than frequency shifts

#### 3. Cross-Dataset Generalization Framework
- **Validation**: Linear SVM trained on one dataset, tested on another
- **Robustness Metric**: Wasserstein-distance consistency analysis
- **Result**: PCA-based Koopman features outperform microstate-derived features for cross-dataset discrimination

## Implementation Guide

### Prerequisites
- Python 3.8+
- Libraries: MNE-Python, PyDMD, scikit-learn, scipy, numpy

### Step-by-Step Implementation

#### Step 1: Preprocess EEG Data
```python
import mne
import numpy as np

# Load resting-state EEG
def preprocess_eeg(eeg_file, sfreq=500, l_freq=1, h_freq=40):
    """Preprocess resting-state EEG for biomarker extraction."""
    raw = mne.io.read_raw_fif(eeg_file, preload=True)
    raw.filter(l_freq=l_freq, h_freq=h_freq)
    raw.set_eeg_reference('average')
    return raw.get_data()
```

#### Step 2: Microstate Analysis
```python
from sklearn.cluster import KMeans

def extract_microstates(eeg_data, n_states=4, n_runs=10):
    """
    Extract microstates using modified K-means clustering.
    
    Args:
        eeg_data: Channels x Time array
        n_states: Number of microstates (typically 4)
        n_runs: Number of random initializations
    
    Returns:
        microstate_maps: Prototype topographies
        labels: Time-series microstate labels
        features: Transition probabilities and durations
    """
    # Global field power for segmentation
    gfp = np.std(eeg_data, axis=0)
    
    # Modified K-means clustering
    best_maps = None
    best_score = -np.inf
    
    for _ in range(n_runs):
        kmeans = KMeans(n_clusters=n_states, random_state=42)
        labels = kmeans.fit_predict(eeg_data.T)
        
        # Calculate features
        transitions = np.zeros((n_states, n_states))
        for i in range(len(labels)-1):
            transitions[labels[i], labels[i+1]] += 1
        transitions = transitions / transitions.sum(axis=1, keepdims=True)
        
        # State durations
        durations = []
        current_state = labels[0]
        duration = 1
        for label in labels[1:]:
            if label == current_state:
                duration += 1
            else:
                durations.append(duration)
                current_state = label
                duration = 1
        
        # Store best solution
        if np.sum(kmeans.inertia_) > best_score:
            best_score = np.sum(kmeans.inertia_)
            best_maps = kmeans.cluster_centers_
    
    return best_maps, labels, {'transitions': transitions, 'durations': durations}
```

#### Step 3: Koopman Operator Analysis (DMD)
```python
from pydmd import DMD
from sklearn.decomposition import PCA

def extract_koopman_features(eeg_data, n_components=20, dmd_rank=10):
    """
    Extract Koopman operator features using DMD on PCA-reduced data.
    
    Args:
        eeg_data: Channels x Time array
        n_components: Number of PCA components
        dmd_rank: Rank for DMD truncation
    
    Returns:
        eigenvalue_magnitudes: |λ| (stability indicator)
        eigenvalue_phases: arg(λ) (frequency indicator)
        modes: Koopman modes
    """
    # PCA dimensionality reduction
    pca = PCA(n_components=n_components)
    data_reduced = pca.fit_transform(eeg_data.T).T  # Components x Time
    
    # DMD on PCA-reduced data
    dmd = DMD(svd_rank=dmd_rank)
    dmd.fit(data_reduced[:, :-1], data_reduced[:, 1:])
    
    # Extract eigenvalues
    eigenvalues = dmd.eigs
    magnitudes = np.abs(eigenvalues)
    phases = np.angle(eigenvalues)
    
    return {
        'magnitudes': magnitudes,
        'phases': phases,
        'modes': dmd.modes,
        'explained_variance': pca.explained_variance_ratio_
    }
```

#### Step 4: Cross-Dataset Classification
```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from scipy.stats import wasserstein_distance

def evaluate_cross_dataset_generalization(
    features_dataset1, labels_dataset1,
    features_dataset2, labels_dataset2
):
    """
    Evaluate cross-dataset generalization using Wasserstein distance.
    
    Returns:
        accuracy: Classification accuracy
        wasserstein_rho: Wasserstein distance consistency metric
    """
    # Standardize features
    scaler = StandardScaler()
    X1 = scaler.fit_transform(features_dataset1)
    X2 = scaler.transform(features_dataset2)
    
    # Train SVM on dataset 1
    svm = SVC(kernel='linear', C=1.0)
    svm.fit(X1, labels_dataset1)
    
    # Test on dataset 2
    accuracy = svm.score(X2, labels_dataset2)
    
    # Calculate Wasserstein distance consistency
    w_distances = []
    for feature_idx in range(X1.shape[1]):
        w_distances.append(wasserstein_distance(X1[:, feature_idx], X2[:, feature_idx]))
    wasserstein_rho = np.mean(w_distances)
    
    return {
        'accuracy': accuracy,
        'wasserstein_rho': wasserstein_rho,
        'w_distances': w_distances
    }
```

## Applications
- **Clinical Diagnostics**: Objective tinnitus assessment in clinical settings
- **Cross-Platform Biomarkers**: EEG biomarkers that generalize across different EEG systems
- **Neuroplasticity Research**: Understanding altered oscillatory dynamics in tinnitus
- **Treatment Monitoring**: Tracking changes in neural signatures post-intervention

## Pitfalls
- **Dataset Alignment**: Ensure consistent preprocessing across datasets (sampling rate, montage)
- **Subject Variability**: Age and hearing loss covariates may affect generalization
- **PCA Component Selection**: Optimal n_components varies with dataset characteristics
- **DMD Rank Selection**: Too low rank loses dynamics; too high introduces noise
- **Microstate Number**: Standard 4 microstates may need adjustment for specific populations

## Related Skills
- eeg-biomarker-robustness-cross-population
- geometric-brain-dynamics-mapping
- brain-dit-fmri-foundation-model

## Key Insights
1. **Koopman eigenvalue magnitudes (decay rates)** generalize better than phases (frequencies)
2. **PCA-based Koopman features** outperform microstate features for cross-dataset discrimination
3. **Wasserstein distance** provides interpretable robustness quantification
4. The methodology suggests altered **oscillatory stability** rather than frequency shifts are the robust neural signature of tinnitus
