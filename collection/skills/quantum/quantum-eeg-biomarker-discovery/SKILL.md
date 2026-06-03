---
name: quantum-eeg-biomarker-discovery
description: >
  Quantum-enhanced EEG biomarker discovery methodology. Uses quantum machine
  learning to discover robust EEG biomarkers for neurological conditions
  (tinnitus, epilepsy, depression, anxiety). Combines quantum kernel methods
  with EEG signal processing for improved cross-subject and cross-platform
  generalization. Use when: (1) discovering EEG biomarkers with quantum ML,
  (2) quantum classification of EEG signals, (3) quantum feature selection
  for neurological diagnosis, (4) cross-subject EEG generalization with
  quantum models, (5) quantum robustness analysis of EEG biomarkers.
---

# Quantum EEG Biomarker Discovery

## Description

Quantum-enhanced EEG biomarker discovery uses quantum machine learning to
identify robust, generalizable EEG biomarkers for neurological conditions.
Quantum models capture non-linear EEG dynamics and inter-channel correlations
that classical methods miss, especially in cross-subject and cross-platform
scenarios. Based on recent work on tinnitus biomarkers (arXiv:2604.22116)
and quantum EEG analysis.

## Activation Keywords

- quantum EEG biomarker
- quantum brain signal
- quantum EEG classification
- quantum EEG diagnosis
- quantum neurological biomarker

## Core Methodology

### Step 1: EEG Preprocessing

```python
# Band-pass filter, artifact removal, epoching
from mne import Epochs, filter
data = filter.notch_filter(raw, Fs=256, freqs=[50, 100])
epochs = Epochs(data, events, tmin=-0.2, tmax=0.8)
```

### Step 2: Quantum Feature Extraction

Extract features from EEG and encode into quantum states:

```python
def eeg_to_quantum(epochs, n_qubits=6):
    """Encode EEG spectral features into quantum circuit."""
    # Compute PSD for each epoch
    psd = compute_psd(epochs, fmin=1, fmax=50)

    # Normalize and encode as rotation angles
    angles = normalize(psd)

    # Ry encoding for spectral features
    for i in range(min(n_qubits, len(angles))):
        qml.RY(angles[i], wires=i)

    # Entangling layer for cross-channel correlations
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
```

### Step 3: Quantum Kernel Biomarker Selection

```python
def quantum_biomarker_kernel(eeg_a, eeg_b):
    """Quantum kernel for EEG biomarker similarity."""
    # Maps EEG patterns to quantum feature space
    # Computes kernel matrix for biomarker selection
    return qml.kernels.feature_kernel(eeg_a, eeg_b,
        feature_map=eeg_to_quantum)

# Use kernel matrix for:
# 1. Feature selection (identifying most discriminative channels)
# 2. Classification (condition vs control)
# 3. Cross-subject transfer (domain adaptation)
```

### Step 4: Cross-Subject Validation

```python
# Leave-one-subject-out cross-validation with quantum SVM
from sklearn.svm import SVC
from sklearn.model_selection import LeaveOneGroupOut

logo = LeaveOneGroupOut()
scores = []
for train_idx, test_idx in logo.split(X, y, subjects):
    # Compute quantum kernel on train
    K_train = quantum_biomarker_kernel(X[train_idx], X[train_idx])
    K_test = quantum_biomarker_kernel(X[test_idx], X[train_idx])

    clf = SVC(kernel='precomputed')
    clf.fit(K_train, y[train_idx])
    scores.append(clf.score(K_test, y[test_idx]))
```

## Application Areas

1. **Tinnitus biomarkers**: Cross-subject robust EEG patterns (arXiv:2604.22116)
2. **Epilepsy detection**: Seizure prediction from interictal EEG
3. **Depression markers**: Resting-state EEG biomarkers for MDD
4. **Anxiety networks**: Brain network patterns for subclinical anxiety
5. **BCI optimization**: EEG feature selection for brain-computer interfaces

## Key Advantages

- **Cross-subject generalization**: Quantum kernels capture universal patterns
- **Cross-platform robustness**: Insensitive to hardware-specific artifacts
- **Non-linear dynamics**: Captures complex EEG interactions
- **Few-shot learning**: Quantum models generalize from fewer subjects

## Pitfalls

- **Signal-to-noise**: EEG noise may overwhelm quantum signal encoding
- **Qubit limitation**: Limited qubits restrict channel count
- **Classical baseline**: ICA + SVM already strong for EEG classification
- **Interpretability**: Quantum features harder to interpret clinically
- **Validation**: Requires large multi-site datasets for robust evaluation

## Resources

- Tinnitus biomarkers paper (arXiv:2604.22116)
- Quantum kernel medical embeddings skill
- EEG foundation model adapters skill
