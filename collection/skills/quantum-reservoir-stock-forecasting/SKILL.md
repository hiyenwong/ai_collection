---
name: quantum-reservoir-stock-forecasting
description: >
  Quantum Reservoir Computing (QRC) framework for nonlinear financial time-series
  forecasting using small-scale quantum systems (≤6 qubits). Predicts trading volumes,
  stock movements, and market patterns for quantum-sector and traditional stocks.
  Use when: (1) quantum machine learning for financial time series, (2) stock movement
  forecasting with reservoir computing, (3) small-scale quantum advantage demonstration,
  (4) nonlinear pattern detection in trading data, (5) quantum-invested market analysis.
---

# Quantum Reservoir Computing for Stock Forecasting

## Core Idea

Quantum Reservoir Computing (QRC) leverages the rich dynamics of small quantum
systems (as few as 3-6 qubits) as computational reservoirs for time-series
prediction. Unlike full quantum neural networks, QRC only trains the readout
layer, making it feasible on near-term hardware.

## Architecture

```
Input (financial features) → Quantum Reservoir (evolving quantum state) →
Classical Readout (trained linear layer) → Output (prediction)
```

### Key Components

1. **Input encoding**: Map financial time series to quantum states
2. **Quantum reservoir**: Fixed Hamiltonian evolution provides nonlinear expansion
3. **Classical readout**: Ridge regression on measurement outcomes

## Implementation

### Step 1: Data Preparation

```python
import numpy as np
import pandas as pd

def prepare_financial_data(prices, volumes, window=20):
    """Prepare features for QRC forecasting."""
    returns = np.diff(np.log(prices))
    volume_changes = np.diff(np.log(volumes))

    # Create sliding window features
    features = []
    targets = []
    for i in range(len(returns) - window):
        feat = np.concatenate([
            returns[i:i+window],
            volume_changes[i:i+window],
        ])
        features.append(feat)
        targets.append(returns[i+window])  # Predict next return

    return np.array(features), np.array(targets)
```

### Step 2: Quantum Reservoir Construction

```python
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.primitives import StatevectorSimulator

def build_qrc_circuit(n_qubits=4, n_layers=2):
    """Build fixed quantum reservoir circuit."""
    qc = QuantumCircuit(n_qubits)

    # Fixed random input rotation (reservoir property)
    np.random.seed(42)
    for layer in range(n_layers):
        for q in range(n_qubits):
            theta = np.random.uniform(0, 2*np.pi)
            qc.ry(theta, q)
            qc.rz(theta, q)
        # Entangling layer
        for q in range(n_qubits - 1):
            qc.cz(q, q + 1)

    return qc

def encode_input(qc, input_vector, n_qubits):
    """Encode financial features into quantum state via angle encoding."""
    encoded = qc.copy()
    for i, val in enumerate(input_vector[:n_qubits]):
        # Scale to [0, pi]
        angle = (val + 1) * np.pi / 2  # assuming normalized input
        encoded.rx(angle, i % n_qubits)
    return encoded
```

### Step 3: Reservoir States Collection

```python
def collect_reservoir_states(circuit, features, n_qubits, n_shots=1024):
    """Collect measurement statistics as reservoir states."""
    reservoir_states = []

    for feat in features:
        encoded = encode_input(circuit, feat, n_qubits)

        # Measure in computational basis
        encoded.measure_all()
        # In practice, run on simulator or hardware
        # counts = execute(encoded, backend, shots=n_shots).result().get_counts()

        # Extract expectation values as features
        for q in range(n_qubits):
            # ⟨Z_q⟩ expectation value
            z_exp = compute_z_expectation(encoded, q, n_shots)
            reservoir_states.append(z_exp)

        # Add Pauli correlations ⟨Z_i Z_j⟩
        for i in range(n_qubits):
            for j in range(i+1, n_qubits):
                zz_exp = compute_zz_expectation(encoded, i, j, n_shots)
                reservoir_states.append(zz_exp)

    return np.array(reservoir_states).reshape(len(features), -1)
```

### Step 4: Train Readout Layer

```python
from sklearn.linear_model import Ridge

def train_readout(reservoir_states, targets, alpha=1.0):
    """Train classical readout with ridge regression."""
    model = Ridge(alpha=alpha)
    model.fit(reservoir_states, targets)
    return model

def predict(model, new_reservoir_states):
    """Make predictions using trained readout."""
    return model.predict(new_reservoir_states)
```

### Step 5: Evaluation Metrics

```python
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_forecast(predictions, actuals):
    """Evaluate forecasting performance."""
    mse = mean_squared_error(actuals, predictions)
    r2 = r2_score(actuals, predictions)

    # Directional accuracy (can we predict up vs down?)
    direction_correct = np.sum(np.sign(predictions) == np.sign(actuals))
    direction_accuracy = direction_correct / len(actuals)

    return {
        'mse': mse,
        'rmse': np.sqrt(mse),
        'r2': r2,
        'direction_accuracy': direction_accuracy
    }
```

## Key Advantages

- **Small qubit requirement**: Works with 3-6 qubits
- **No training on quantum hardware**: Only classical readout is trained
- **Rich dynamics**: Quantum entanglement provides nonlinear feature expansion
- **NISQ-compatible**: Short circuits, minimal gate depth

## Typical Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| n_qubits | 4-6 | Reservoir size |
| n_layers | 2-3 | Circuit depth |
| n_shots | 1024 | Measurements per input |
| window | 20-60 | Time series lookback |
| ridge_alpha | 0.1-10 | Regularization strength |

## Application: Quantum-Sector Stocks

For predicting quantum-sector stock movements:
- Input: daily returns, volumes, VIX, sector ETF prices
- Target: next-day trading volume or return direction
- Universe: IBM, GOOG, IONQ, RGTI, QBTS, etc.

## Activation Keywords

- quantum reservoir computing, QRC stock forecasting, quantum time series,
  quantum stock prediction, reservoir computing finance, small-scale quantum ML,
  quantum trading volume prediction, quantum-invested stocks

## References

- "A Quantum Reservoir Computing Approach to Quantum Stock Movement Forecasting
  in Quantum-Invested Markets", arXiv:2602.13094 (2026)
