---
name: quantum-tcnn-equity-prediction
description: "Quantum Temporal Convolutional Neural Network (QTCNN) methodology for cross-sectional equity return prediction. Combines quantum circuit layers with temporal convolution networks to capture both temporal patterns and quantum feature space interactions in financial time-series. Use when building quantum-enhanced stock prediction models, designing quantum neural networks for financial forecasting, or implementing temporal quantum machine learning for equity markets."
---

# Quantum TCNN for Equity Return Prediction

Methodology for using Quantum Temporal Convolutional Neural Networks to predict cross-sectional equity returns, based on arXiv:2512.06630.

## Architecture

```
Input (Financial Time-Series) → Temporal Convolution → Quantum Circuit Layer → Prediction
```

### Temporal Convolution Block

- Causal convolutions to preserve temporal ordering
- Dilated convolutions for capturing long-range dependencies
- Residual connections for gradient flow
- Output: temporal feature representations

### Quantum Circuit Layer

- Encode temporal features into quantum states via amplitude or angle encoding
- Apply parameterized quantum gates (rotation + entangling layers)
- Measure observables to extract quantum-enhanced features
- Output: quantum feature vectors

### Key Design Decisions

1. **Encoding**: Angle encoding for sequential data (preserves temporal structure)
2. **Ansatz**: Hardware-efficient with alternating rotation/entangling layers
3. **Measurement**: Pauli-Z expectation values for real-valued output
4. **Training**: Hybrid quantum-classical backpropagation

## Application to Equity Returns

- **Input features**: Price history, volume, technical indicators, market factors
- **Target**: Cross-sectional return ranking (not absolute price prediction)
- **Advantage**: Quantum layers may capture non-linear interactions that classical TCNNs miss
- **Evaluation**: Compare against pure classical TCNN baseline

## Training Pipeline

1. Prepare cross-sectional dataset (stocks × time × features)
2. Normalize features per stock to remove scale effects
3. Split into train/validation/test by time period
4. Train TCNN backbone on classical data
5. Fine-tune with quantum layer inserted
6. Evaluate on out-of-sample period using rank IC (Information Coefficient)

## Validation Metrics

- Rank Information Coefficient (IC): Correlation between predicted and actual return ranks
- IC decay: How predictive power degrades over time horizon
- Turnover-adjusted returns: Practical trading simulation
- Quantum vs. classical performance gap

## Limitations

- Requires careful data encoding to preserve temporal structure
- Quantum circuit depth limited by noise on NISQ devices
- Need sufficient qubits for meaningful feature dimension
- Classical TCNN baseline is very strong - quantum advantage not guaranteed

## Resources

- Primary paper: arXiv:2512.06630
