---
name: contextual-quantum-neural-stock-prediction
description: "Contextual quantum neural network methodology for multi-asset stock price prediction using quantum batch gradient update (QBGU) and quantum multi-task learning (QMTL) with share-and-specify ansatz."
---

# Contextual Quantum Neural Stock Prediction

## Description
Methodology for stock price prediction using contextual quantum neural networks that capture recent market trends via quantum superposition. Introduces quantum batch gradient update (QBGU) for accelerated convergence and quantum multi-task learning (QMTL) with share-and-specify ansatz for simultaneous multi-asset training with logarithmic qubit overhead.

## Activation Keywords
- quantum stock prediction
- 量子股票预测
- contextual quantum neural network
- QBGU quantum gradient
- quantum multi-task learning
- share-and-specify ansatz
- QMTL finance
- quantum portfolio prediction
- 量子多任务学习股票

## Tools Used
- terminal: Run quantum circuit simulations (Qiskit, PennyLane)
- write_file: Create quantum circuit definitions
- read_file: Read market data, model configurations
- search_files: Locate financial datasets and quantum ML codebases

## Usage Patterns

### Pattern 1: Multi-Asset Stock Price Prediction
When predicting prices for multiple correlated assets:
1. Encode recent price trends as quantum states
2. Build share-and-specify ansatz circuit
3. Train with QBGU for faster convergence
4. Extract price distribution predictions from measurement

### Pattern 2: Quantum Portfolio Representation
When encoding entire portfolios in quantum states:
1. Use logarithmic qubit overhead for N assets
2. Apply task-specific operators controlled by quantum labels
3. Simultaneously train all assets on same circuit
4. Capture inter-asset correlations through entanglement

### Pattern 3: Contextual Market Adaptation
When market regimes change:
1. Update quantum state encoding with recent data window
2. Re-train only task-specific operators (not shared layers)
3. Maintain shared quantum features across regimes
4. Achieve faster adaptation than full retraining

## Instructions for Agents

### Step 1: Data Preparation
1. Collect OHLCV data for target assets
2. Compute features: returns, volatility, volume ratios
3. Normalize to [0, 1] for amplitude encoding
4. Split into training/validation/test sets with temporal ordering

### Step 2: Quantum State Encoding
```
|ψ⟩ = Σ_i sqrt(p_i) |i⟩
```
where p_i represents normalized price/trend features.
Use angle encoding or amplitude encoding based on data dimensionality.

### Step 3: Build Share-and-Specify Ansatz
1. **Shared layers**: Common quantum feature extraction
   - Parameterized rotation gates: RY(θ), RZ(φ)
   - Entangling gates: CNOT, CZ for inter-asset correlations
2. **Task-specific layers**: Asset-specific operators
   - Controlled by quantum labels identifying each asset
   - Separate parameters per asset for specialization
3. **Measurement**: Expectation values → price predictions

### Step 4: Quantum Batch Gradient Update (QBGU)
1. Replace standard SGD with QBGU:
   - Compute gradients via parameter-shift rule
   - Batch multiple gradient evaluations in quantum superposition
   - Update parameters with momentum term
2. QBGU converges faster than classical SGD on quantum circuits
3. Monitor loss: MSE between predicted and actual prices

### Step 5: Evaluation and Validation
1. Compare against classical baselines (LSTM, GRU, ARIMA)
2. Evaluate multi-asset prediction accuracy
3. Assess inter-asset correlation capture
4. Test out-of-sample generalization across market regimes

## Error Handling

### Barren Plateaus
If gradients vanish during training:
- Reduce circuit depth
- Use layerwise training (train one layer at a time)
- Apply correlated parameter initialization
- Increase QBGU batch size

### Overfitting
If model memorizes training data:
- Add quantum regularization (measure intermediate observables)
- Reduce ansatz expressivity
- Apply cross-validation across time periods
- Use dropout-equivalent quantum noise

### Hardware Noise (Real QPU)
If running on actual quantum hardware:
- Apply error mitigation (zero-noise extrapolation)
- Use readout error calibration
- Reduce circuit depth for NISQ devices
- Consider classical simulation for development

## Examples

### Example 1: S&P 500 Multi-Asset Prediction
```python
import pennylane as qml
import numpy as np

# Configuration
n_assets = 4  # AAPL, GOOGL, MSFT, AMZN
n_qubits = int(np.ceil(np.log2(n_assets))) + 2  # logarithmic overhead
n_layers = 3

# Share-and-specify ansatz
def ansatz(params, asset_label):
    # Shared feature extraction
    for i in range(n_qubits):
        qml.RY(params[0, i], wires=i)
    
    # Entangling layer for correlations
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
    
    # Task-specific (asset-controlled) operations
    for j in range(n_layers):
        qml.RY(params[j + 1, asset_label], wires=asset_label % n_qubits)
        qml.CNOT(wires=[asset_label % n_qubits, (asset_label + 1) % n_qubits])

# Quantum node
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def circuit(params, asset_label, features):
    # Encode features
    for i in range(min(len(features), n_qubits)):
        qml.RY(features[i], wires=i)
    
    # Apply ansatz
    ansatz(params, asset_label)
    
    # Measure expectation value
    return qml.expval(qml.PauliZ(0))

# QBGU training loop
def qbgu_train(params, data, labels, lr=0.01, batch_size=4):
    for epoch in range(100):
        # Batch gradient computation via quantum superposition
        grads = np.zeros_like(params)
        for asset_idx in range(n_assets):
            asset_data = data[asset_idx]
            asset_labels = labels[asset_idx]
            
            # Parameter-shift rule for gradients
            for i in range(params.shape[0]):
                for j in range(params.shape[1]):
                    params_plus = params.copy()
                    params_plus[i, j] += np.pi / 2
                    params_minus = params.copy()
                    params_minus[i, j] -= np.pi / 2
                    
                    grad_plus = circuit(params_plus, asset_idx, asset_data)
                    grad_minus = circuit(params_minus, asset_idx, asset_data)
                    grads[i, j] += (grad_plus - grad_minus) / 2
        
        # Update parameters
        params -= lr * grads
    return params
```

## Resources
- arXiv: 2503.01884 - Contextual Quantum Neural Networks for Stock Price Prediction
- Scientific Reports 16, Article 34413 (2026)
- arXiv: 2510.11153 - Hot-Starting Quantum Portfolio Optimization

## Related Skills
- quantum-ml-patterns
- quantum-portfolio-optimizer
- quantum-neural-architecture
- quantum-finance-analysis
