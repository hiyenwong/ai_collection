---
name: quantum-fmri-foundation-models
description: >
  Quantum-enhanced fMRI foundation model methodology. Integrates quantum machine
  learning with brain foundation models (Brain-DiT, fMRI transformers) for
  improved neuroimaging analysis. Use when: (1) applying quantum computing to
  fMRI data analysis, (2) building quantum-classical hybrid models for brain
  imaging, (3) enhancing foundation model embeddings with quantum kernels,
  (4) quantum feature extraction from neuroimaging data, (5) quantum advantage
  in brain decoding or encoding tasks.
---

# Quantum fMRI Foundation Models

## Description

Quantum-enhanced fMRI foundation models combine pre-trained brain foundation
models (Brain-DiT, NeuroSTORM, TABLeT) with quantum machine learning for
improved neuroimaging analysis. Quantum feature maps capture non-linear brain
dynamics that classical models may miss, while quantum kernels provide
exponential feature space expansion for classification tasks.

Based on Brain-DiT (arXiv:2604.12683) + quantum computing research.

## Activation Keywords

- quantum fMRI
- quantum brain imaging
- quantum foundation model brain
- quantum neuroimaging
- quantum brain decoding
- quantum fMRI analysis

## Tools Used

- qiskit/pennylane: Quantum circuit construction
- pytorch: Classical neural network backbone
- nibabel: fMRI data loading (NIfTI format)

## Core Methodology

### Step 1: Classical Feature Extraction

Extract embeddings from pre-trained fMRI foundation models:

```python
# Brain-DiT or similar foundation model
brain_embeddings = foundation_model.encode(fmri_volumes)
# Shape: (n_subjects, n_volumes, embedding_dim)
```

### Step 2: Quantum Feature Mapping

Map classical embeddings to quantum Hilbert space:

```python
def quantum_feature_map(classical_features, n_qubits=8, depth=3):
    """Encode fMRI embeddings into quantum state."""
    from pennylane import numpy as qnp

    # Amplitude encoding for dense representations
    # Or angle encoding for sparse activation patterns
    circuit = qml.AmplitudeEmbedding(
        features=classical_features,
        wires=range(n_qubits),
        normalize=True
    )

    # Variational layers for trainable transformations
    for d in range(depth):
        qml.BasicEntanglerLayers(
            weights=layer_weights[d],
            wires=range(n_qubits)
        )

    return circuit
```

### Step 3: Quantum Kernel Computation

Compute quantum kernel matrix for downstream tasks:

```python
def quantum_kernel(x1, x2, feature_map):
    """Compute overlap between quantum states."""
    # |<φ(x1)|φ(x2)>|² via SWAP test or direct computation
    return fidelity(feature_map(x1), feature_map(x2))
```

### Step 4: Hybrid Training

Train quantum-classical hybrid for classification/regression:

```python
@qml.qnode(dev)
def hybrid_circuit(features, weights):
    quantum_feature_map(features, n_qubits, depth)
    qml.BasicEntanglerLayers(weights=weights, wires=range(n_qubits))
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# Classical layer consumes quantum outputs
hybrid_model = nn.Sequential(
    QuantumLayer(hybrid_circuit),
    nn.Linear(n_qubits, num_classes)
)
```

## Application Areas

1. **Brain disorder classification**: Alzheimer's, schizophrenia, depression
2. **Cognitive state decoding**: Task vs rest, attention states
3. **Longitudinal analysis**: Disease progression tracking
4. **Cross-subject generalization**: Transfer learning across populations
5. **Multimodal fusion**: fMRI + EEG + structural MRI

## Key Advantages

- **Exponential feature space**: 2^n dimensional Hilbert space for n qubits
- **Non-linear capture**: Quantum entanglement captures complex brain dynamics
- **Foundation model synergy**: Leverages pre-trained representations
- **Cross-domain transfer**: Quantum features transfer across imaging modalities

## Pitfalls

- **Noise sensitivity**: NISQ-era quantum computers add noise to fMRI analysis
- **Dimension mismatch**: fMRI data (10⁵ voxels) must be compressed before quantum encoding
- **Barren plateaus**: Deep quantum circuits suffer from vanishing gradients
- **Classical baseline**: Strong classical models (transformers) set high bar
- **Data requirements**: Quantum models need sufficient training data despite advantage

## Resources

- Brain-DiT: Universal multi-state fMRI foundation model (arXiv:2604.12683)
- Quantum kernel methods for medical AI (quantum-kernel-medical-embeddings skill)
- Hybrid quantum-classical medical diagnosis (hybrid-quantum-medical-diagnosis skill)
