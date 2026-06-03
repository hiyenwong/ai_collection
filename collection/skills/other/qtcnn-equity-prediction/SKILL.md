---
name: qtcnn-equity-prediction
description: >
  Quantum Temporal Convolutional Neural Network (QTCNN) methodology for
  cross-sectional equity return prediction. Combines classical temporal encoder
  with parameter-efficient quantum convolution circuits for multi-scale pattern
  extraction from sequential financial indicators. Achieves 72% Sharpe ratio
  improvement over classical baselines on JPX Tokyo Stock Exchange data.
  Triggers: quantum equity prediction, QTCNN, quantum trading, quantum return
  forecasting, quantum temporal convolution, cross-sectional equity prediction.
---

# QTCNN: Quantum Temporal Convolutional Neural Network for Equity Prediction

## Core Architecture

QTCNN = Classical Temporal Encoder + Quantum Convolution Circuit + Readout Layer

### Phase 1: Classical Temporal Encoder

```
Input: Sequential technical indicators {I_1, I_2, ..., I_T}
  - Moving averages, RSI, MACD, volume patterns, etc.

Temporal Encoder:
  - Extracts multi-scale temporal patterns across lookback windows
  - Produces compressed feature representations
  - Captures short-term and long-term dependencies
```

### Phase 2: Quantum Convolution

```
Quantum Feature Map:
  - Encode classical features into quantum state |ψ⟩ via angle/phase encoding
  - Leverage superposition to represent exponentially large feature space

Quantum Convolution Layer:
  - Parameterized quantum circuits (PQC) with entangling layers
  - Local convolutions via controlled rotation gates
  - Entanglement creates non-linear feature interactions
  - Number of qubits << classical feature dimension
```

### Phase 3: Classical Readout

```
Measurement:
  - Measure expectation values ⟨Z_i⟩ of Pauli-Z operators
  - Results serve as quantum-enhanced features

Final Prediction:
  - Linear layer maps quantum features to return predictions
  - Cross-sectional ranking for portfolio construction
```

## Key Advantages

| Aspect | Classical TCN | QTCNN |
|--------|--------------|-------|
| Feature representation | Linear depth | Quantum superposition |
| Overfitting resistance | Limited | Quantum entanglement suppresses |
| Parameters | O(n*d) | O(n) with quantum encoding |
| Sharpe ratio | 0.313 | 0.538 (+72%) |
| Dataset | JPX Tokyo SE | JPX Tokyo SE |

## Implementation Pattern

### Step 1: Data Preparation

```python
# Collect technical indicators for each stock
# Create lookback windows: [t-W, ..., t-1] → predict return at t
# Normalize across cross-section at each timestamp
```

### Step 2: Temporal Encoding

```python
# Use causal 1D convolutions with dilated receptive fields
# Similar to WaveNet/TCN architecture
# Output: fixed-dimension temporal feature vector
```

### Step 3: Quantum Convolution

```python
# PennyLane or Qiskit implementation
# qubits = ceil(log2(feature_dim))  # typically 6-10 qubits
# Layers:
#   1. Feature encoding: Ry(θ_i) rotations on each qubit
#   2. Entangling layer: CNOT or CZ between adjacent qubits
#   3. Variational layer: trainable RY/RZ rotations
#   4. Repeat 2-3 for depth p
```

### Step 4: Training

```python
# Loss: MSE or negative Sharpe ratio
# Optimizer: Adam with learning rate scheduling
# Batch: cross-sectional batches at each timestamp
```

## Parameter Efficiency

Quantum convolution uses O(n) parameters vs O(n^2) for classical convolutions:
- n qubits represent 2^n dimensional Hilbert space
- Entanglement creates correlations without explicit parameter count
- Critical advantage for NISQ-era devices (limited qubits, noisy gates)

## Practical Deployment Considerations

1. **Simulator-first**: Train on classical quantum simulators (PennyLane, Qiskit Aer)
2. **Hardware-ready**: Circuit depth < 50 gates for near-term execution
3. **Hybrid fallback**: Replace quantum layer with classical approximation during inference

## Activation Keywords

- qtcnn
- quantum temporal convolution
- quantum equity prediction
- quantum return forecasting
- quantum cross-sectional prediction
- quantum trading model

## Related Skills

- quantum-time-series-finance
- quantum-finance-portfolio
- quantum-ml-healthcare
