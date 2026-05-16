---
name: quantum-tcnn-equity-prediction
description: "Quantum Temporal Convolutional Neural Network (QTCNN) methodology for cross-sectional equity return prediction. Combines classical temporal encoder with parameter-efficient quantum convolution circuits for stock market forecasting. Use when: building quantum-enhanced financial prediction models, combining quantum circuits with time-series analysis, equity return forecasting, portfolio construction from quantum ML predictions, or benchmarking quantum vs classical financial models. Activation: quantum tcnn, quantum temporal convolution, equity return prediction quantum, quantum stock forecasting, QTCNN, quantum time-series finance."
---

# Quantum Temporal Convolutional Neural Networks for Equity Prediction

Design and evaluate Quantum Temporal Convolutional Neural Networks (QTCNN) for cross-sectional equity return prediction. Combines classical temporal encoding with quantum convolution circuits to leverage superposition and entanglement for enhanced feature representation.

## Architecture

### Two-Stage Pipeline

```
Market Data → Temporal Encoder → Quantum Convolution → Prediction
```

### Stage 1: Classical Temporal Encoder
- Extract multi-scale patterns from sequential technical indicators
- Use dilated causal convolutions (TCN-style) to capture varying time horizons
- Handle noisy input and regime shifts via robust feature extraction
- Output: compressed temporal feature vectors

### Stage 2: Quantum Convolution Circuit
- Encode classical features into quantum state via amplitude/angle encoding
- Apply parameterized quantum gates (entangling layers) for feature transformation
- Leverage superposition for parallel feature processing
- Use entanglement for capturing non-linear cross-feature dependencies
- Measurement yields enhanced feature representation
- Fewer parameters than classical equivalents → suppresses overfitting

## Key Design Decisions

### Encoding Strategy
- **Amplitude encoding**: O(log N) qubits for N features; requires state preparation
- **Angle encoding**: One rotation per feature; more NISQ-friendly
- Choose based on qubit count and feature dimensionality

### Quantum Circuit Depth
- Shallow circuits (2-4 entangling layers) for NISQ compatibility
- Use hardware-efficient ansatz matching device connectivity
- Balance expressivity against noise accumulation

### Training Approach
- Classical encoder: standard backpropagation
- Quantum circuit: parameter-shift rule for gradient computation
- Joint optimization with shared loss (e.g., portfolio Sharpe ratio)

## Evaluation Protocol

1. **Dataset**: Use large-scale exchange data (e.g., JPX Tokyo Stock Exchange)
2. **Metric**: Out-of-sample Sharpe ratio as primary performance metric
3. **Baseline**: Compare against classical TCN, LSTM, and linear models
4. **Portfolio**: Construct long-short portfolios from model predictions
5. **Result benchmark**: QTCNN achieved Sharpe ratio of 0.538, outperforming classical baseline by ~72%

## When to Use

- Financial prediction with noisy, regime-shifting data
- Need for parameter-efficient models (limited training data)
- Quantum advantage hypothesis testing in finance
- Cross-sectional prediction across many assets simultaneously

## Implementation Notes

- Use PennyLane, Qiskit, or similar quantum ML frameworks
- Simulate on classical hardware first, then deploy to real quantum devices
- Key parameter: number of qubits vs feature dimension tradeoff
- Consider variational quantum circuits with trainable gates
- Monitor for barren plateaus in gradient-based optimization

## Resources

- arXiv: 2512.06630 - "Quantum Temporal Convolutional Neural Networks for Cross-Sectional Equity Return Prediction"
- Authors: Chi-Sheng Chen, Xinyu Zhang, En-Jui Kuo, Rong Fu, Qiuzhe Xie, Fan Zhang
