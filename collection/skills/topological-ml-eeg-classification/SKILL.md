---
name: topological-ml-eeg-classification
description: "Topological Machine Learning for epileptic iEEG seizure detection using persistent homology and persistence diagrams. Features multiple TDA representations and cross-patient generalization. Activation: topological data analysis, TDA, EEG classification, seizure detection, persistent homology."
---

# Topological Machine Learning for Epileptic iEEG Classification

> Framework using topological data analysis (TDA) features from persistence diagrams for classifying preictal, ictal, and interictal brain states in epilepsy patients.

## Metadata
- **Source**: arXiv:2604.11971
- **Published**: 2026-04-13
- **Categories**: cs.LG, stat.AP

## Core Methodology

### Key Innovation
EEG/iEEG signals have high dimensionality and nonlinear/stochastic dynamics that challenge traditional feature extraction. This work uses **topological data analysis (TDA)** to extract robust structural features from neural time series, particularly effective for seizure detection across multiple patients.

### Technical Framework

1. **Persistent Homology**
   - Track topological features (connected components, holes, voids) across scales
   - Encode as persistence diagrams: D = {{(b_i, d_i)}}
   - Persistence = d_i - b_i (feature lifetime)

2. **TDA Representations**
   
   **Carlsson Coordinates**: Vectorization via algebraic functions
   ```
   f(b, d) = (d - b)^α * b^β
   ```
   
   **Persistence Images**: Kernel density estimation on persistence diagram
   ```
   ρ(x, y) = Σ w(b_i, d_i) * K((x, y) - (b_i, d_i))
   ```
   
   **Template Functions**: Projection onto learned basis functions

3. **Multichannel Analysis**
   - Construct time-series from iEEG electrode arrays
   - Embed in point cloud via sliding window
   - Compute persistence for each channel
   - Aggregate features across channels

4. **Classification Pipeline**
   - TDA feature extraction → ML classifier
   - Evaluated on 55 patients
   - Cross-patient generalization

## Implementation Guide

### Prerequisites
- Python with scikit-learn, PyTorch/TensorFlow
- TDA libraries: GUDHI, Ripser, or Persim
- Understanding of algebraic topology basics

### Step-by-Step

1. **Preprocess iEEG Data**

```python
from scipy.signal import butter, filtfilt

def preprocess_eeg(signal, fs=256, low_freq=0.5, high_freq=80):
    """
    Bandpass filter and normalize iEEG signal
    """
    nyquist = fs / 2
    low = low_freq / nyquist
    high = high_freq / nyquist
    b, a = butter(5, [low, high], btype='band')
    filtered = filtfilt(b, a, signal)
    normalized = (filtered - filtered.mean()) / filtered.std()
    return normalized
```

2. **Create Point Cloud Embedding**

```python
from sklearn.decomposition import PCA

def sliding_window_embedding(signal, window_size, delay):
    """
    Takens' embedding: time series → point cloud
    """
    n_points = len(signal) - (window_size - 1) * delay
    embedded = np.zeros((n_points, window_size))
    
    for i in range(n_points):
        embedded[i, :] = signal[i:i + window_size * delay:delay]
    
    # Optional: PCA to reduce dimensions
    if window_size > 3:
        pca = PCA(n_components=3)
        embedded = pca.fit_transform(embedded)
    
    return embedded
```

3. **Compute Persistent Homology**

```python
import gudhi

def compute_persistence_diagram(point_cloud, max_dim=2):
    """
    Compute persistence diagram from point cloud
    """
    rips_complex = gudhi.RipsComplex(
        points=point_cloud, 
        max_edge_length=2.0
    )
    simplex_tree = rips_complex.create_simplex_tree(max_dimension=max_dim)
    persistence = simplex_tree.persistence()
    
    diagrams = {d: [] for d in range(max_dim + 1)}
    for dim, (birth, death) in persistence:
        if death != float('inf'):
            diagrams[dim].append([birth, death])
    
    return diagrams
```

4. **Vectorize Persistence Diagrams**

```python
from scipy.stats import multivariate_normal

def persistence_image(diagram, resolution=(20, 20), sigma=0.1):
    """
    Convert persistence diagram to image representation
    """
    x = np.linspace(0, 1, resolution[0])
    y = np.linspace(0, 1, resolution[1])
    X, Y = np.meshgrid(x, y)
    
    image = np.zeros(resolution)
    for birth, death in diagram:
        if death != float('inf'):
            weight = death - birth
            rv = multivariate_normal(
                mean=[birth, death], 
                cov=[[sigma**2, 0], [0, sigma**2]]
            )
            image += weight * rv.pdf(np.dstack([X, Y]))
    
    return image.flatten()

def carlsson_coordinates(diagram):
    """
    Carlsson coordinate vectorization
    """
    coords = []
    for birth, death in diagram:
        if death != float('inf'):
            persistence = death - birth
            coords.append(persistence)
            coords.append(persistence ** 2)
            coords.append(birth * persistence)
            coords.append(death * persistence)
    
    return np.array(coords) if coords else np.zeros(10)
```

5. **Multi-Channel Feature Extraction**

```python
def extract_tda_features(eeg_data, channels, window_duration=1.0, fs=256):
    """
    Extract TDA features from multi-channel iEEG
    """
    window_size = int(window_duration * fs)
    all_features = []
    
    for ch in channels:
        signal = eeg_data[ch, :]
        signal = preprocess_eeg(signal, fs)
        point_cloud = sliding_window_embedding(signal, window_size=20, delay=1)
        diagrams = compute_persistence_diagram(point_cloud, max_dim=1)
        
        for dim in [0, 1]:
            pi = persistence_image(diagrams[dim], resolution=(10, 10))
            cc = carlsson_coordinates(diagrams[dim])
            all_features.extend(pi)
            all_features.extend(cc[:10])
    
    return np.array(all_features)
```

6. **Train Classifier**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_seizure_classifier(features, labels):
    """
    Train classifier for preictal/ictal/interictal states
    """
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, stratify=labels
    )
    
    clf = RandomForestClassifier(n_estimators=100, max_depth=10)
    clf.fit(X_train, y_train)
    
    return clf
```

### Code Example: Full Pipeline

```python
class TopologicalEEGClassifier:
    """
    Complete TDA-based iEEG seizure detection pipeline
    """
    def __init__(self, fs=256, window_duration=1.0):
        self.fs = fs
        self.window_size = int(window_duration * fs)
        self.classifier = None
        self.feature_scaler = StandardScaler()
    
    def extract_features_multichannel(self, eeg_data):
        """Extract features from all channels"""
        features = []
        for ch in range(eeg_data.shape[0]):
            ch_features = self.extract_features_single_channel(
                eeg_data[ch, :]
            )
            features.append(ch_features)
        return np.concatenate(features)
    
    def fit(self, eeg_recordings, labels):
        """Train classifier on multiple recordings"""
        X = [self.extract_features_multichannel(rec) 
             for rec in eeg_recordings]
        X = np.array(X)
        X = self.feature_scaler.fit_transform(X)
        
        self.classifier = RandomForestClassifier(
            n_estimators=200, 
            max_depth=15,
            class_weight='balanced'
        )
        self.classifier.fit(X, labels)
        return self
    
    def predict(self, eeg_recording):
        """Predict seizure state"""
        features = self.extract_features_multichannel(eeg_recording)
        features = self.feature_scaler.transform(features.reshape(1, -1))
        return self.classifier.predict(features)[0]
```

## Applications
- **Real-Time Seizure Detection**: Continuous monitoring with early warning systems
- **Seizure Onset Zone Localization**: Identifying epileptic brain regions
- **Pharmacological Research**: Evaluating drug efficacy on seizure patterns
- **Surgical Planning**: Pre-surgical evaluation of iEEG data

## Pitfalls
- **Computational Cost**: Persistent homology computation is O(n²) to O(n³), limiting real-time use
- **Parameter Sensitivity**: Window size, delay, and filtration parameters affect results
- **Small Sample Sizes**: Rare seizure events limit training data
- **Class Imbalance**: Interictal states vastly outnumber ictal states
- **Interpretability**: Topological features lack direct neurobiological interpretation

## Related Skills
- eeg-structure-guided-diffusion
- eeg-foundation-model-adapters
- explainable-gnn-eeg-neurological
