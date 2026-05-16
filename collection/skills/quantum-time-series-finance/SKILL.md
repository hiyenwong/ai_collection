---
name: quantum-time-series-finance
description: >
  Quantum time series forecasting methodology for financial data using QLSTM and QRC.
  Compares Quantum Long Short-Term Memory (QLSTM) and Quantum Reservoir Computing (QRC)
  architectures for financial time-series prediction. Uses amplitude encoding for efficient
  representation of lagged observations under realistic qubit constraints.
  Use when: financial time series forecasting, quantum LSTM, quantum reservoir computing,
  quantum machine learning for finance, stock prediction, temporal pattern recognition,
  quantum-enhanced forecasting, amplitude encoding financial data.
---

# Quantum Time Series Financial Forecasting

QLSTM and QRC architectures for financial time series prediction with amplitude encoding.

## Core Architectures

### Quantum LSTM (QLSTM)

Quantum-enhanced LSTM using parameterized quantum circuits for recurrent dynamics:

Input: Amplitude-encoded lagged observations |x(t-lag), ..., x(t-1)>
Recurrent: Parameterized quantum circuit U(theta) for cell state update
Output: Measured quantum state to classical readout layer

### Quantum Reservoir Computing (QRC)

Quantum reservoir with fixed random circuit and trainable readout:

Input: Amplitude-encoded lagged window |x(t-w), ..., x(t-1)>
Reservoir: Fixed random parameterized quantum circuit (no training)
Readout: Classical linear regression on measurement outcomes

## Amplitude Encoding

Efficient state preparation for normalized lagged observations:

```python
import numpy as np

def amplitude_encode_lags(data, lag_window):
    n_qubits = int(np.ceil(np.log2(lag_window)))
    window = np.array(data[-lag_window:])
    window = window / np.linalg.norm(window)
    padded = np.zeros(2**n_qubits)
    padded[:lag_window] = window
    return padded, n_qubits
```

## Lag Structure Selection

| Setting | Univariate | Multivariate |
|---------|-----------|-------------|
| Lag Window | 5-20 | 3-10 per feature |
| Encoding | Single amplitude vector | Concatenated amplitudes |
| Qubits Needed | ceil(log2(lag)) | ceil(log2(lag * features)) |

### Lag Selection Strategy

1. Autocorrelation analysis: Identify significant lags via ACF/PACF
2. Mutual information: Select lags with highest MI to target
3. Cross-validation: Test multiple lag windows on validation set
4. Quantum constraint: Max lag limited by available qubits (2^n states)

## Implementation Workflow

### Step 1: Data Preparation

```python
def prepare_financial_data(prices, lag=10, split=0.8):
    returns = np.diff(np.log(prices))
    X, y = [], []
    for i in range(lag, len(returns)):
        X.append(returns[i-lag:i])
        y.append(returns[i])
    X, y = np.array(X), np.array(y)
    split_idx = int(len(X) * split)
    return X[:split_idx], y[:split_idx], X[split_idx:], y[split_idx:]
```

### Step 2: QLSTM Circuit

QLSTM cell with parameterized quantum circuit:
- Encode input and hidden state as quantum amplitudes
- Apply parameterized quantum layers for gate computation
- Measure output gates (input, forget, cell, output)
- Update cell and hidden states classically

### Step 3: QRC Training

Train readout layer for quantum reservoir computing:
- Run fixed random quantum circuit on input states
- Collect measurement outcomes as reservoir states
- Train classical Ridge regression on reservoir states

## Benchmarking

Compare against classical baselines:
- Classical LSTM
- Classical Reservoir Computing (ESN)
- ARIMA / Prophet

Metrics: MSE, MAE, MAPE, directional accuracy

## Key Findings

1. Univariate: Quantum models match classical baselines with proper lag selection
2. Multivariate: Quantum models can modestly outperform classical with suitable encoding
3. Qubit efficiency: Amplitude encoding enables large lag windows with few qubits
4. Training cost: QRC requires minimal quantum circuit training (only readout)

## When to Use

- Financial time series with limited training data
- Need for quantum advantage demonstration in forecasting
- Amplitude-encoded data with moderate feature dimensionality
- Comparison studies of quantum vs classical architectures

## References

- arXiv: 2605.02656 - Learning Temporal Patterns in Financial Time Series: QLSTM vs QRC
- Maheshwari, Hellstern, Zaefferer et al., 2026
