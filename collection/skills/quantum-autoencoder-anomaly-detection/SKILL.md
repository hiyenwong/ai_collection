---
name: quantum-autoencoder-anomaly-detection
description: "Compression-driven anomaly detection methodology using quantum autoencoders (QAE) for brain MRI and medical imaging. Maps data to quantum states via angle encoding, trains variational encoder-decoder to compress normal data while discarding to trash qubits. Anomaly scores = compression resistance. Use when building quantum ML pipelines for medical anomaly detection."
---

## Quantum Autoencoder Anomaly Detection

### Description

Anomaly detection methodology using quantum autoencoders (QAE) for brain MRI and medical imaging data. Leverages angle encoding to map image patches into quantum states, trains variational encoder-decoder architecture to discard information via auxiliary trash qubits. Anomaly scores reflect compression resistance — abnormal inputs resist compression more than normal data.

### Activation Keywords
- quantum autoencoder
- QAE anomaly detection
- 量子自编码器
- compression anomaly detection
- 压缩异常检测
- quantum medical imaging
- brain MRI anomaly
- trash qubit compression
- quantum compression detection
- variational encoder decoder quantum

### Core Methodology

#### 1. Angle Encoding for Image Data
Map image patches to quantum states:
```
|ψ(x)⟩ = ⊗_i RY(x_i)|0⟩
```
- Normalize pixel values to [0, π]
- Each pixel → single qubit rotation
- N pixels → N qubits (or patch-based encoding for larger images)

#### 2. QAE Architecture
```
Input qubits (n) → Encoder U(θ) → [Kept qubits (k) | Trash qubits (t)]
                         ↓
                   Decoder U†(θ)
                         ↓
                  Reconstructed input
```
- **n**: Total input qubits
- **k**: Kept qubits (compressed representation, k < n)
- **t**: Trash qubits (t = n - k, discarded information)
- **U(θ)**: Parameterized unitary (variational circuit)

#### 3. Training Objective
Minimize fidelity between trash qubits and |0⟩^⊗t:
```
L(θ) = 1 - ⟨0|^⊗t ρ_trash(θ) |0⟩^⊗t
```
- Normal data → low loss (compresses well, trash ≈ |0⟩)
- Anomalous data → high loss (resists compression, trash ≠ |0⟩)

#### 4. Anomaly Scoring
After training on normal data:
```
anomaly_score(x) = 1 - fidelity(trash_qubits, |0⟩^⊗t)
```
- Score ≈ 0: Normal data (well compressed)
- Score > threshold: Anomaly detected

### Implementation Patterns

#### Pattern 1: Basic QAE with PennyLane

```python
import pennylane as qml
import numpy as np

def qae_circuit(params, n_qubits, n_trash):
    """Quantum autoencoder circuit."""
    n_kept = n_qubits - n_trash
    
    # Encoder
    for i in range(n_qubits):
        qml.RY(params[i], wires=i)
    
    # Variational layers
    for layer in range(n_layers):
        for i in range(n_qubits):
            qml.Rot(*params[layer*3:(layer+1)*3], wires=i)
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i+1])
    
    # Measure trash qubits
    return [qml.expval(qml.PauliZ(i)) for i in range(n_kept, n_qubits)]

def compute_anomaly_score(model, data_point):
    """Score a data point after training."""
    trash_expectations = model(data_point)
    # Fidelity with |0⟩ state: average of ⟨Z⟩ measurements
    fidelity = np.mean([(1 + exp) / 2 for exp in trash_expectations])
    return 1 - fidelity  # Anomaly score
```

#### Pattern 2: Patch-Based Encoding for MRI

```python
def encode_mri_patches(mri_volume, patch_size=8, n_qubits=6):
    """Encode 3D MRI volume into quantum-compatible patches."""
    patches = extract_patches(mri_volume, patch_size)
    encoded = []
    for patch in patches:
        # Flatten and normalize patch
        flat = patch.flatten()
        # Dimensionality reduction to match qubit count
        reduced = pca_transform(flat, n_components=n_qubits)
        # Normalize to [0, π] for angle encoding
        normalized = (reduced - reduced.min()) / (reduced.max() - reduced.min()) * np.pi
        encoded.append(normalized)
    return np.array(encoded)
```

#### Pattern 3: Threshold Calibration

```python
def calibrate_threshold(scores, percentile=95):
    """Set anomaly detection threshold from training scores."""
    return np.percentile(scores, percentile)

def detect_anomalies(model, test_data, threshold):
    """Run anomaly detection on test data."""
    anomalies = []
    for i, data_point in enumerate(test_data):
        score = compute_anomaly_score(model, data_point)
        if score > threshold:
            anomalies.append({
                'index': i,
                'score': score,
                'is_anomaly': True
            })
    return anomalies
```

### Step-by-Step Workflow

1. **Preprocess data**: Normalize MRI/medical images, extract patches
2. **Encode to quantum states**: Angle encoding with normalization
3. **Design QAE circuit**: Choose n_kept, n_trash, variational ansatz
4. **Train on normal data**: Minimize trash qubit excitation
5. **Calibrate threshold**: Use validation set of known normal data
6. **Detect anomalies**: Score test data, flag high-compression-resistance inputs
7. **Interpret results**: Map anomaly scores back to spatial locations in original image

### Error Handling

#### Barren Plateaus
If training fails to converge:
- Reduce circuit depth
- Use layer-wise training (train one layer at a time)
- Initialize parameters near identity (small angles)

#### Insufficient Qubits
For large images:
- Use patch-based encoding (process sub-regions independently)
- Apply PCA/dimensionality reduction before encoding
- Consider amplitude encoding for very large inputs (log(N) qubits)

#### Noise Sensitivity
On noisy quantum hardware:
- Use error mitigation (zero-noise extrapolation)
- Reduce circuit depth to minimize decoherence
- Consider simulation-based training, hardware-based inference

### Pitfalls

1. **Patch boundary artifacts**: Anomalies at patch boundaries may be missed. Use overlapping patches with stride < patch_size.
2. **Normalization sensitivity**: Angle encoding is sensitive to input scaling. Always normalize per-patch, not globally.
3. **Threshold selection**: Too conservative → missed anomalies; too aggressive → false positives. Use ROC analysis on validation set.
4. **Class imbalance**: Anomalies are rare. Train only on normal data; don't mix anomalies into training set.
5. **Interpretability**: QAE detects "unusual" patterns but doesn't classify anomaly type. Combine with classical classifier for diagnosis.

### Resources
- arXiv:2606.27411 — Compression-Driven Anomaly Detection with QAE
- PennyLane: Quantum ML framework
- Qiskit: IBM's quantum computing SDK
