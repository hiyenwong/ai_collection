---
name: quantum-feature-surrogate
description: >
  Quantum Feature Surrogate methodology for scalable quantum advantage in
  production ML systems. Instead of processing every data sample on quantum
  hardware (prohibitively expensive at scale), use a small representative
  subsample to train quantum feature extraction, then transfer learned patterns
  to a classical surrogate model that applies them to the full dataset at
  near-zero cost. The quantum processor becomes a teacher of representations
  while production inference runs entirely on classical hardware. Developed
  by Kipu Quantum for industrial-scale applications including healthcare,
  molecular analysis, and sensor data. Use when: (1) quantum ML with large
  datasets where per-sample quantum inference is infeasible, (2) medical
  image classification with quantum-enhanced features, (3) molecular property
  prediction at production scale, (4) cost-effective quantum advantage
  deployment.
---

# Quantum Feature Surrogate Framework

## Core Idea

Quantum computing can extract information from data in ways classical algorithms
struggle to match, but processing millions of samples on quantum hardware is
prohibitively expensive. The quantum feature surrogate framework breaks this
bottleneck:

1. **Subsample selection** - Carefully choose a small subset whose distribution
   faithfully represents the full dataset
2. **Quantum feature extraction** - Process only the subsample on quantum hardware
   to extract rich quantum-enhanced features
3. **Surrogate training** - Train a simple classical model to learn the mapping
   from raw inputs to quantum-extracted features
4. **Classical production inference** - Apply the surrogate to the full dataset
   at near-zero cost

The quantum processor stops being a per-sample engine and becomes a **teacher of
representations**, while production inference runs entirely on classical hardware.

## Framework Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Training Phase                        │
│                                                         │
│  Full Dataset ──→ Subsample Selection ──→ N samples     │
│                        │                                 │
│                        ▼                                 │
│               Quantum Feature Extractor                  │
│               (QPU - expensive but powerful)             │
│                        │                                 │
│                        ▼                                 │
│              Quantum-Enhanced Features                   │
│                        │                                 │
│                        ▼                                 │
│              Classical Surrogate Model                   │
│              (learn the Q→C mapping)                     │
│                        │                                 │
│                        ▼                                 │
│         [Raw Input → Quantum Feature Predictor]          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                 Production Phase                        │
│                                                         │
│  Full Dataset ──→ Classical Surrogate ──→ Predicted     │
│                        │              Quantum Features   │
│                        ▼                                 │
│               Downstream ML Model                        │
│               (classification, regression)               │
│                        │                                 │
│                        ▼                                 │
│                   Predictions                            │
└─────────────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Representative Subsample Selection

```python
import numpy as np
from sklearn.cluster import KMeans

def select_representative_subsample(X, n_samples, method='kmeans'):
    """
    Select a small subsample that faithfully represents the full dataset.

    Methods:
    - kmeans: Cluster centroids as representative samples
    - kcenter: Maximize coverage of feature space
    - stratified: Maintain class/strata proportions
    """
    if method == 'kmeans':
        kmeans = KMeans(n_clusters=n_samples, random_state=42)
        kmeans.fit(X)
        # Find nearest actual samples to centroids
        indices = []
        for center in kmeans.cluster_centers_:
            dists = np.linalg.norm(X - center, axis=1)
            indices.append(np.argmin(dists))
        return np.array(indices)

    elif method == 'kcenter':
        # Greedy max-min distance selection
        indices = [np.random.randint(len(X))]
        for _ in range(n_samples - 1):
            dists = np.min([np.linalg.norm(X - X[i], axis=1)
                          for i in indices], axis=0)
            indices.append(np.argmax(dists))
        return np.array(indices)
```

### Step 2: Quantum Feature Extraction

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.kernels import QuantumKernel

def quantum_feature_extraction(X_subsample, n_qubits, feature_dim=64):
    """
    Extract quantum-enhanced features from subsample.

    Uses quantum kernel methods to map classical data into
    high-dimensional quantum feature space.
    """
    # Feature map: encode classical data into quantum states
    feature_map = ZZFeatureMap(feature_dimension=n_qubits, reps=2)

    # Quantum kernel computation
    qkernel = QuantumKernel(feature_map=feature_map)
    kernel_matrix = qkernel.evaluate(X_subsample)

    # Extract features via kernel PCA or spectral decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(kernel_matrix)

    # Select top-k features
    top_k = min(feature_dim, len(eigenvalues))
    indices = np.argsort(eigenvalues)[::-1][:top_k]
    features = eigenvectors[:, indices] * np.sqrt(eigenvalues[indices])

    return features
```

### Step 3: Surrogate Model Training

```python
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

def train_surrogate(X_raw, quantum_features, model_type='mlp'):
    """
    Train classical model to predict quantum features from raw inputs.

    The surrogate learns the mapping: raw_input → quantum_features
    """
    if model_type == 'mlp':
        surrogate = MLPRegressor(
            hidden_layer_sizes=(128, 64, 32),
            max_iter=1000,
            random_state=42
        )
    elif model_type == 'random_forest':
        surrogate = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )

    surrogate.fit(X_raw, quantum_features)
    return surrogate
```

### Step 4: Production Inference Pipeline

```python
def predict_with_surrogate(surrogate, downstream_model, X_full):
    """
    Full production pipeline:
    1. Use surrogate to predict quantum features for all samples
    2. Apply downstream ML model for final prediction
    """
    # Step 1: Predict quantum features (classical, fast)
    predicted_quantum_features = surrogate.predict(X_full)

    # Step 2: Use predicted quantum features for downstream task
    predictions = downstream_model.predict(predicted_quantum_features)

    return predictions
```

### Step 5: Quality Validation

```python
def validate_surrogate_quality(X_test, surrogate, quantum_feature_fn):
    """
    Validate that surrogate predictions match true quantum features.
    """
    # Get true quantum features for test set
    true_features = quantum_feature_fn(X_test)

    # Get surrogate predictions
    predicted_features = surrogate.predict(X_test)

    # Compute fidelity metrics
    from sklearn.metrics import r2_score, mean_squared_error

    r2 = r2_score(true_features, predicted_features)
    mse = mean_squared_error(true_features, predicted_features)

    # Feature correlation
    correlations = np.corrcoef(true_features.T, predicted_features.T)
    feature_correlations = np.diag(correlations[:len(true_features), len(true_features):])

    return {
        'r2_score': r2,
        'mse': mse,
        'mean_feature_correlation': np.mean(feature_correlations),
        'min_feature_correlation': np.min(feature_correlation)
    }
```

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| subsample_size | 100-500 | Number of samples for quantum processing |
| n_qubits | 10-20 | Qubit count for feature extraction |
| feature_dim | 64-128 | Dimensionality of quantum feature space |
| surrogate_model | MLP | Classical surrogate type |
| validation_split | 0.2 | Fraction for surrogate quality check |

## Cost-Benefit Analysis

| Metric | Direct Quantum | Surrogate Approach |
|--------|---------------|-------------------|
| QPU calls (1M samples) | 1,000,000 | 100-500 |
| Inference cost | ~$100K+ | ~$1-5K |
| Inference latency | Hours-Days | Seconds |
| Feature quality | Exact | ~95-99% fidelity |
| Scalability | Limited | Linear |

## When to Use Quantum Feature Surrogates

Use this approach when:
- Dataset size > 10,000 samples (quantum inference too expensive per sample)
- Quantum advantage demonstrated on subsample but not cost-effective at scale
- Medical imaging, molecular screening, or sensor data with large volumes
- Need production-ready ML with quantum-enhanced features
- Budget constraints on quantum hardware access

## Activation Keywords

- quantum feature surrogate, quantum surrogate model, offline quantum
  advantage, quantum production ML, quantum teacher model, quantum
  feature extraction scalable, kipu quantum methodology, cost-effective
  quantum ml, quantum classical surrogate, quantum representation learning

## Related Skills

- `quantum-feature-amplification-network`: QFAN for medical imaging
- `quantum-kernel-medical-embeddings`: Quantum kernel methods for medical AI
- `quantum-ml-healthcare`: Quantum ML patterns for healthcare
- `hybrid-quantum-classical-architecture`: Hybrid quantum-classical computing patterns

## References

- Flores-Garrigos, Alvarado Barrios, Zhang, Simen, Solano. "Off-line quantum-advantage
  feature extraction for industrial production" arXiv:2605.19801 (2026)

## Notes

- Developed by Kipu Quantum for industrial-scale applications
- The subsample distribution must faithfully represent the full dataset
- Surrogate quality should be validated against true quantum features
- This approach enables quantum advantage TODAY, not waiting for fault tolerance
