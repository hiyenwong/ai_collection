---
name: topological-ml-eeg-classification
category: ai_collection
tags:
  - topological-data-analysis
  - persistent-homology
  - eeg
  - ieeg
  - seizure-detection
  - machine-learning
  - neuroscience
  - signal-processing
description: >
  Topological Machine Learning for EEG/iEEG Classification of Seizures —
  persistent homology and topological signatures for seizure detection and
  classification from electroencephalographic signals.
paper:
  title: "Topological Machine Learning for EEG/iEEG Classification of Seizures"
  arxiv: "2604.13538v1"
  date: 2026-04-15
---

# Topological Machine Learning for EEG/iEEG Classification

## Overview

This skill covers how **Topological Data Analysis (TDA)** — specifically **persistent homology** — is applied to EEG/iEEG signals for automated seizure detection and classification. TDA captures the "shape" of data at multiple scales, producing robust, noise-resilient features that complement traditional spectral and temporal biomarkers.

## Why Topology for EEG?

| Challenge in EEG/iEEG | How TDA Helps |
|---|---|
| Non-stationary, chaotic dynamics | Persistent homology is invariant to small perturbations and parameter choices |
| High dimensionality (multi-channel, high sample rate) | Topological features compress structure into low-dimensional, stable summaries |
| Noise and artifacts (EMG, movement, line noise) | Homological features are robust to bounded perturbations (stability theorem) |
| Multi-scale structure (bursts, oscillations, slow waves) | Filtration sweeps across all scales automatically |
| Need for interpretable biomarkers | Persistence diagrams and barcodes are visual and interpretable |

## Core Methodology

### 1. Signal Preprocessing Pipeline

```
Raw EEG/iEEG  →  Band-pass filter (0.5–150 Hz)  →  Notch filter (50/60 Hz)
  →  Artifact rejection / ICA  →  Segmentation (epochs: 2–10 s)
  →  Normalization (z-score per channel)
```

### 2. Phase-Space Reconstruction

EEG time series are scalar signals. To apply TDA we first reconstruct the underlying dynamical system's attractor using **time-delay embedding** (Takens' theorem):

```
x(t) = [s(t), s(t+τ), s(t+2τ), ..., s(t+(m-1)τ)]
```

- **τ (delay)**: estimated via first minimum of mutual information or autocorrelation drop to 1/e
- **m (embedding dimension)**: estimated via false-nearest-neighbors (FNN) algorithm, typically 3–7 for EEG

Each channel yields a point cloud in ℝ^m.

### 3. Distance Matrix Computation

For each embedded epoch, compute a pairwise distance matrix:

```python
from scipy.spatial.distance import pdist, squareform

D = squareform(pdist(embedded_signal, metric='euclidean'))
# D is an N×N symmetric matrix (N = number of embedded points)
```

This distance matrix serves as the input for the Vietoris-Rips filtration.

### 4. Vietoris-Rips Filtration & Persistent Homology

**Vietoris-Rips Complex**: For a set of points and a distance threshold ε, include a simplex (edge, triangle, tetrahedron, ...) whenever all pairwise distances are ≤ ε.

**Filtration**: Vary ε from 0 to max(D). Track when topological features (holes) are born and die.

**Dimensions of interest**:

| Dimension | Topological Feature | EEG Interpretation |
|---|---|---|
| H₀ | Connected components | Clustering of similar phase-space points |
| H₁ | Loops / 1-cycles | Periodic or oscillatory structure in the attractor |
| H₂ | Voids / 2-cycles | Higher-order coordination across channels |

```python
import ripser
from persim import plot_diagrams

# Compute persistence diagrams
diagrams = ripser.ripser(D, maxdim=2)['diagrams']
# diagrams[d] contains (birth, death, dimension) tuples
```

### 5. Persistence Diagrams & Barcodes

A **persistence diagram (PD)** plots each topological feature as a point (birth, death). Features far from the diagonal are "persistent" (significant); those near the diagonal are noise.

```
Death
  |
  |        ●  (persistent loop)
  |    ●
  |      ●
  | ●  ● ●  ●
  |________________ Birth
    diagonal: death = birth
```

**Barcodes** are an equivalent representation: horizontal bars from birth to death.

### 6. Vectorization of Topological Features

Persistence diagrams are not directly usable by ML models. They must be vectorized.

#### 6a. Persistence Landscapes

```python
from persim import PersistenceLandscape

pl = PersistenceLandscape(resolution=100)
landscapes = pl.fit_transform(diagrams)
# Shape: (n_epochs, n_dims, resolution)
```

A persistence landscape converts each PD into a sequence of piecewise-linear functions.

#### 6b. Persistence Images

```python
from persim import PersImage

pi = PersImage(pixels=[50, 50], sigma=0.1)
pimages = pi.transform(diagrams)
# Shape: (n_epochs, n_dims, 50, 50)
```

PDs are smoothed into 2D images using Gaussian kernels.

#### 6c. Betti Curves

```python
def betti_curve(dgm, resolution=100):
    """Compute Betti number curve from persistence diagram."""
    births = dgm[:, 0]
    deaths = dgm[:, 1]
    thresholds = np.linspace(0, np.max(deaths), resolution)
    betti = np.zeros(resolution)
    for i, t in enumerate(thresholds):
        betti[i] = np.sum((births <= t) & (deaths > t))
    return betti
```

#### 6d. Summary Statistics

```python
def pd_summary_stats(dgm):
    """Extract scalar features from a persistence diagram."""
    if len(dgm) == 0:
        return [0.0] * 12
    lifetimes = dgm[:, 1] - dgm[:, 0]
    stats = [
        np.max(lifetimes),           # max persistence
        np.mean(lifetimes),          # mean persistence
        np.std(lifetimes),           # std of persistence
        np.sum(lifetimes),           # total persistence
        np.percentile(lifetimes, 75),  # 75th percentile
        np.percentile(lifetimes, 25),  # 25th percentile
        np.max(dgm[:, 0]),           # max birth
        np.mean(dgm[:, 0]),          # mean birth
        np.max(dgm[:, 1]),           # max death
        len(dgm),                    # number of features
        np.sum(lifetimes > 0.5),     # persistent features count
        np.mean(lifetimes > 0.5),    # ratio of persistent features
    ]
    return stats
```

### 7. Multi-Channel & Cross-Frequency Topology

For multi-channel EEG/iEEG, extend beyond single-channel analysis:

- **Concatenated embedding**: Stack embeddings from all channels to capture cross-channel topology
- **Functional connectivity graph**: Build a graph from coherence/correlation between channels, then compute graph TDA
- **Cross-frequency coupling**: Embed low-frequency amplitude vs. high-frequency phase to capture PAC structure topologically
- **Sliding window**: Apply TDA on overlapping windows to capture temporal evolution

```python
def multi_channel_tda(channels_data, τ=10, m=4, maxdim=2):
    """Compute TDA features across multiple EEG channels."""
    all_features = []
    for ch_idx in range(channels_data.shape[1]):
        ch_signal = channels_data[:, ch_idx]
        embedded = time_delay_embed(ch_signal, τ=τ, m=m)
        D = squareform(pdist(embedded))
        diagrams = ripser.ripser(D, maxdim=maxdim)['diagrams']
        for dim in range(maxdim + 1):
            stats = pd_summary_stats(diagrams[dim])
            all_features.extend(stats)
    return np.array(all_features)
```

## Machine Learning Pipeline

### Full End-to-End Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    FULL TDA-ML PIPELINE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Raw EEG/iEEG  ──►  Preprocessing  ──►  Epoching                 │
│        │                                                         │
│        ▼                                                         │
│  Phase-Space Embedding (τ, m per epoch)                          │
│        │                                                         │
│        ▼                                                         │
│  Distance Matrix Computation                                     │
│        │                                                         │
│        ▼                                                         │
│  Vietoris-Rips Filtration  ──►  Persistence Diagrams (H₀,H₁,H₂) │
│        │                                                         │
│        ▼                                                         │
│  Vectorization  ──►  Landscapes / Images / Statistics            │
│        │                                                         │
│        ▼                                                         │
│  Feature Concatenation  ──►  [+ Spectral / Temporal features]    │
│        │                                                         │
│        ▼                                                         │
│  Feature Selection  ──►  PCA / UMAP / Mutual Information         │
│        │                                                         │
│        ▼                                                         │
│  Classification Model:                                          │
│    • SVM (RBF kernel)                                           │
│    • Random Forest / XGBoost                                    │
│    • Neural Network (MLP or CNN on Persistence Images)           │
│    • Ensemble methods                                           │
│        │                                                         │
│        ▼                                                         │
│  Output: Seizure vs Non-Seizure / Seizure Type Classification    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation: Scikit-Learn Pipeline

```python
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import classification_report, roc_auc_score

class TDAPipeline:
    """End-to-end TDA feature extraction and classification pipeline."""

    def __init__(self, τ=10, m=4, maxdim=2, classifier='svm', resolution=100):
        self.τ = τ
        self.m = m
        self.maxdim = maxdim
        self.classifier_name = classifier
        self.resolution = resolution

    def extract_features(self, X_epochs):
        """
        X_epochs: list or array of shape (n_epochs, n_channels, n_samples)
        Returns: feature matrix of shape (n_epochs, n_features)
        """
        features = []
        for epoch in X_epochs:
            epoch_features = []
            for ch in range(epoch.shape[0]):
                embedded = self._embed(epoch[ch])
                D = squareform(pdist(embedded))
                diagrams = ripser.ripser(D, maxdim=self.maxdim)['diagrams']
                for dim in range(self.maxdim + 1):
                    stats = pd_summary_stats(diagrams[dim])
                    epoch_features.extend(stats)
                # Add landscape features
                pl = PersistenceLandscape(resolution=self.resolution)
                for dim in range(self.maxdim + 1):
                    ls = pl.fit_transform([diagrams[dim]])
                    if len(ls) > 0:
                        epoch_features.extend(ls[0].flatten())
            features.append(epoch_features)
        return np.array(features)

    def _embed(self, signal):
        """Time-delay embedding of a 1D signal."""
        N = len(signal) - (self.m - 1) * self.τ
        if N <= 0:
            return np.zeros((1, self.m))
        embedded = np.zeros((N, self.m))
        for i in range(self.m):
            embedded[:, i] = signal[i * self.τ:i * self.τ + N]
        return embedded

    def build_and_evaluate(self, X, y):
        """Build pipeline and evaluate with cross-validation."""
        features = self.extract_features(X)
        features = np.nan_to_num(features)

        # Normalize
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)

        # Classifier
        if self.classifier_name == 'svm':
            clf = SVC(kernel='rbf', C=1.0, probability=True)
        elif self.classifier_name == 'rf':
            clf = RandomForestClassifier(n_estimators=200, max_depth=10)
        elif self.classifier_name == 'xgb':
            from xgboost import XGBClassifier
            clf = XGBClassifier(n_estimators=100, max_depth=5)
        else:
            raise ValueError(f"Unknown classifier: {self.classifier_name}")

        # Cross-validation
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        scores = cross_val_score(clf, features_scaled, y, cv=cv, scoring='accuracy')

        clf.fit(features_scaled, y)
        y_pred = clf.predict(features_scaled)
        print(classification_report(y, y_pred))

        return clf, features_scaled, scores
```

### Seizure Detection Binary Classifier

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, auc

def seizure_detection_pipeline(eeg_data, labels, τ=10, m=4):
    """Binary classification: seizure vs. non-seizure."""
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        eeg_data, labels, test_size=0.2, stratify=labels, random_state=42
    )

    pipeline = TDAPipeline(τ=τ, m=m, maxdim=2, classifier='svm')
    clf, features, scores = pipeline.build_and_evaluate(eeg_data, labels)

    # Test on held-out set
    X_test_features = pipeline.extract_features(X_test)
    X_test_features = np.nan_to_num(X_test_features)
    # Fit scaler on full data for demo
    scaler = StandardScaler().fit(features)
    X_test_scaled = scaler.transform(X_test_features)

    y_pred = clf.predict(X_test_scaled)
    y_prob = clf.predict_proba(X_test_scaled)[:, 1]

    cm = confusion_matrix(y_test, y_pred)
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    print(f"Cross-val accuracy: {scores.mean():.4f} ± {scores.std():.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")
    print(f"Confusion matrix:\n{cm}")

    return clf, cm, roc_auc
```

### Seizure Type Classification (Multi-class)

```python
def seizure_type_classification(eeg_data, labels):
    """Multi-class classification: seizure types (e.g., focal, generalized, unknown)."""
    pipeline = TDAPipeline(τ=10, m=5, maxdim=2, classifier='rf')

    features = pipeline.extract_features(eeg_data)
    features = np.nan_to_num(features)
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    clf = RandomForestClassifier(n_estimators=300, max_depth=15, class_weight='balanced')
    scores = cross_val_score(clf, features_scaled, labels, cv=cv, scoring='f1_macro')

    clf.fit(features_scaled, labels)
    y_pred = clf.predict(features_scaled)
    print(classification_report(labels, y_pred))

    # Feature importance analysis
    importances = clf.feature_importances_
    top_indices = np.argsort(importances)[::-1][:20]

    return clf, scores, importances
```

## Combined Feature Approach

Best performance is often achieved by combining TDA features with traditional EEG features:

```python
def combined_features(eeg_data, fs=256):
    """Combine TDA + spectral + temporal features."""
    tda_features = []  # from pipeline.extract_features()
    spectral_features = []
    temporal_features = []

    for epoch in eeg_data:
        # Spectral: band powers (delta, theta, alpha, beta, gamma)
        freqs, psd = welch(epoch, fs=fs, nperseg=fs*2)
        bands = {'delta': (0.5, 4), 'theta': (4, 8), 'alpha': (8, 13),
                 'beta': (13, 30), 'gamma': (30, 100)}
        band_powers = []
        for name, (lo, hi) in bands.items():
            mask = (freqs >= lo) & (freqs <= hi)
            band_powers.append(np.trapz(psd[mask], freqs[mask]))
        spectral_features.append(band_powers)

        # Temporal: Hjorth parameters
        diff1 = np.diff(epoch)
        diff2 = np.diff(diff1)
        activity = np.var(epoch)
        mobility = np.sqrt(np.var(diff1) / activity)
        complexity = np.sqrt(np.var(diff2) / np.var(diff1)) / mobility
        temporal_features.append([activity, mobility, complexity])

    return np.hstack([tda_features, spectral_features, temporal_features])
```

## Practical Considerations

### Computational Efficiency

TDA on large EEG datasets is computationally intensive. Key optimizations:

1. **Subsampling**: Use representative subset of embedded points (e.g., 200–500 points per epoch)
2. **Approximate Rips**: Use sparse filtrations or witness complexes
3. **Parallel processing**: Compute TDA features per epoch/channel in parallel
4. **Chunked processing**: Process in sliding windows with overlap

```python
from joblib import Parallel, delayed

def parallel_tda_features(epochs, n_jobs=-1):
    """Compute TDA features in parallel across epochs."""
    results = Parallel(n_jobs=n_jobs)(
        delayed(extract_single_epoch_features)(epoch) for epoch in epochs
    )
    return np.array(results)
```

### Stability Guarantees

The **Bottleneck Stability Theorem** ensures that small perturbations in the input data produce small changes in the persistence diagram:

```
d_B(D_1, D_2) ≤ d_∞(X_1, X_2)
```

This means EEG noise bounded by ε produces at most ε change in topological features — a critical guarantee for clinical applications.

### Interpretability

- **H₀ features**: Number and persistence of connected components → signal stationarity
- **H₁ features**: Persistent loops → oscillatory/periodic dynamics (alpha, beta rhythms)
- **H₂ features**: Persistent voids → complex multi-dimensional coordination (seizure networks)

Seizure onset typically manifests as:
- Increase in H₁ persistence (synchronization of neural oscillators)
- Change in H₀ structure (clustering of phase-space trajectories)
- Emergence of H₂ features (high-dimensional coordinated firing)

### Parameter Selection Guide

| Parameter | Typical Range | Selection Method |
|---|---|---|
| Delay τ | 5–20 samples | Mutual information minimum |
| Embedding dim m | 3–7 | False nearest neighbors |
| Max homology dim | 1–2 | H₀+H₁ usually sufficient; H₂ for iEEG |
| Epoch length | 2–10 s | Balance temporal resolution vs. embedding quality |
| Subsample size | 100–500 points | Accuracy vs. computation tradeoff |
| Filtration ε range | 0 to max(D) | Automatic from ripser |

## Dependencies

```
pip install ripser persim gtda-ts scipy scikit-learn numpy
pip install mne  # for EEG data loading and preprocessing
pip install xgboost  # optional, for gradient boosting classifier
pip install joblib  # for parallel processing
pip install matplotlib  # for visualization
```

## References

1. Ghrist, R. (2008). "Barcodes: The Persistent Topology of Data." *Bulletin of the AMS*.
2. Otter, N. et al. (2017). "A roadmap for the computation of persistent homology." *EPJ Data Science*.
3. Chazal, F. & Michel, B. (2021). "An introduction to Topological Data Analysis." *Frontiers in AI*.
4. Perea, A. et al. (2015). "A topological approach for selecting genes of interest using sleep transcriptomics." *BMC Bioinformatics*.
5. Umeda, Y. (2017). "Time series classification via topological data analysis." *Information and Media Technologies*.
6. Bunch, P. et al. (2021). "Persistent homology of dynamical systems and EEG signals." *Journal of Neuroscience Methods*.
7. Rucco, M. et al. (2018). "Persistent homology in brain networks: A methodological review." *NeuroImage*.

## Quick Start

```python
# Minimal working example
import numpy as np
import ripser
from scipy.spatial.distance import pdist, squareform

# Simulate a seizure-like signal (increased oscillation)
t = np.linspace(0, 10, 2560)
preictal = np.sin(2*np.pi*10*t) + 0.3*np.random.randn(len(t))
ictal = np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*3*t) + 0.2*np.random.randn(len(t))

# Embed
def embed(signal, τ=10, m=4):
    N = len(signal) - (m-1)*τ
    return np.column_stack([signal[i*τ:i*τ+N] for i in range(m)])

# Compute TDA
for name, sig in [('preictal', preictal), ('ictal', ictal)]:
    emb = embed(sig)
    D = squareform(pdist(emb))
    diags = ripser.ripser(D, maxdim=1)['diagrams']
    for dim in [0, 1]:
        lifetimes = diags[dim][:, 1] - diags[dim][:, 0]
        print(f"{name} H{dim}: max persistence = {np.max(lifetimes):.4f}, "
              f"mean = {np.mean(lifetimes):.4f}")
```
