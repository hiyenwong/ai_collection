---
name: quantum-dynamic-time-warping
description: "Quantum Dynamic Time Warping (qDTW) for multivariate time series classification — hybrid quantum-classical architecture replacing classical distance metrics with parameterized Hilbert space geometry. Use when implementing quantum-enhanced time series analysis, multivariate sequence alignment, or hybrid quantum-classical distance metrics for ML pipelines."
metadata:
  arxiv_id: "2606.27815"
  published: "2026-06-26"
  authors: "Diego Alvarez-Estevez, Alejandro Mayorga-Redondo, Eduardo Mosqueira-Rey"
  tags: [quantum, machine-learning, time-series, dynamic-time-warping, classification]
license: Complete terms in LICENSE.txt
---

# Quantum Dynamic Time Warping (qDTW)

Replace classical Dynamic Time Warping distance metrics with parameterized quantum Hilbert space geometry for multivariate time series classification.

## Core Architecture

qDTW is a hybrid quantum-classical architecture that:

1. **Replaces Euclidean distance** in classical DTW with a **parameterized quantum kernel** computed via quantum circuit measurement
2. **Encodes multivariate time series** into quantum states using amplitude or angle encoding
3. **Learns optimal distance geometry** through variational quantum circuit parameters trained on classification loss
4. **Handles cross-channel correlations** naturally via quantum entanglement between qubits representing different time series channels

## Implementation Pattern

### Step 1: Time Series Encoding

```python
# Encode multivariate time point x ∈ R^d into quantum state
# Angle encoding: θ_i = π * (x_i - min) / (max - min) for each channel
def encode_to_quantum_state(x, n_qubits, encoding='angle'):
    """Map multivariate time point to quantum circuit rotations."""
    # For d channels, use min(d, n_qubits) qubits
    # Apply RY(θ_i) for each channel i
    pass
```

### Step 2: Quantum Distance Kernel

```python
# Compute distance between two time points via quantum circuit
def quantum_distance(state1, state2, params):
    """
    Use SWAP test or fidelity-based measurement to compute
    quantum-enhanced distance between encoded states.
    Returns: scalar distance in learned metric space
    """
    # Variational circuit U(θ) transforms states
    # Measure overlap |⟨ψ1|U†U|ψ2⟩|²
    # Distance = 1 - fidelity
    pass
```

### Step 3: qDTW Alignment

```python
def qdtw_alignment(series1, series2, quantum_params):
    """
    Standard DTW algorithm but using quantum_distance
    instead of Euclidean distance for the cost matrix.
    """
    # Build cost matrix with quantum kernel
    # Find optimal warping path
    # Return qDTW distance
    pass
```

### Step 4: Classification

```python
# Use qDTW distance as feature for kNN or as loss in training loop
def qdtw_classifier(train_data, train_labels, test_point, k=3):
    """kNN using qDTW distance metric."""
    distances = [qdtw_alignment(test_point, t, params) for t in train_data]
    # Return majority vote of k nearest neighbors
    pass
```

## Key Advantages

- **Latent correlation capture**: Quantum entanglement captures cross-channel dependencies that Euclidean distance misses
- **Parameterized geometry**: Variational parameters adapt the distance metric to the specific classification task
- **Structural ablation**: qDTW components can be ablated to study contribution of quantum vs classical parts
- **Hybrid deployment**: Quantum kernel can run on simulator or NISQ hardware; classical DTW wrapping handles scalability

## Pitfalls

- **NISQ hardware limits**: Current quantum hardware limits circuit depth and qubit count; use simulators for development
- **Encoding bottleneck**: Mapping high-dimensional time series to limited qubits requires dimensionality reduction or block encoding
- **Training cost**: Variational parameter optimization requires many circuit evaluations; use gradient-free optimizers (SPSA, CMA-ES)
- **Classical baseline**: Always compare against classical DTW + standard features — quantum advantage must be demonstrated empirically

## Activation

`qdtw`, `quantum dynamic time warping`, `quantum time series`, `quantum distance metric`, `quantum kernel DTW`, `hybrid quantum classification`, `multivariate time series quantum`

## References

- Paper: https://arxiv.org/abs/2606.27815
