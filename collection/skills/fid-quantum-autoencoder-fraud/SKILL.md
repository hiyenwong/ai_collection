---
name: fid-quantum-autoencoder-fraud
category: quantum-finance
description: Fidelity-driven Quantum Autoencoder (FiD-QAE) methodology for credit card fraud detection using quantum state compression and SWAP test fidelity estimation as anomaly detection criterion. Robust under quantum noise and validated on real IBM Quantum hardware.
tags: [quantum-anomaly-detection, fraud-detection, quantum-autoencoder, quantum-fidelity, financial-security]
---

# FiD-QAE: Fidelity-Driven Quantum Autoencoder for Fraud Detection

## Overview

The Fidelity-based Quantum Autoencoder (FiD-QAE) employs quantum state compression and fidelity estimation as the decision criterion for anomaly detection in credit card fraud. Transactions are encoded into quantum states, compressed through a variational quantum circuit, and evaluated using the SWAP test to distinguish legitimate from fraudulent transactions.

**Source Paper**: "FiD-QAE: A Fidelity-Driven Quantum Autoencoder for Credit Card Fraud Detection" (arXiv: 2512.12689)

## Core Principles

### 1. Quantum State Encoding
- Financial transactions → quantum states via amplitude/angle encoding
- Feature vectors mapped to qubit rotation parameters
- High-dimensional transaction data compressed into compact quantum representations

### 2. Variational Quantum Compression
- Encoder circuit: maps input states to compressed latent quantum states
- Decoder circuit: attempts to reconstruct original states from compressed representation
- Training objective: maximize reconstruction fidelity for legitimate transactions
- Fraudulent transactions (anomalies) → poor reconstruction → low fidelity

### 3. SWAP Test Fidelity Estimation
- **SWAP test**: quantum circuit that estimates fidelity between two quantum states
- Compares original transaction state |ψ⟩ with reconstructed state |ψ'⟩
- Fidelity F = |⟨ψ|ψ'⟩|² serves as anomaly score
- **Decision rule**: F < threshold → fraud, F ≥ threshold → legitimate
- Threshold determined from validation set of known transactions

### 4. Noise Robustness
- Maintains consistent performance under multiple quantum noise models
- Validated on IBM Quantum hardware backends
- Results consistent between simulation and real devices

## Implementation Steps

### Step 1: Transaction Encoding
```python
import numpy as np
import pennylane as qml

def encode_transaction(features, n_qubits):
    """
    Encode financial transaction features into quantum state.
    
    Args:
        features: Normalized transaction feature vector
        n_qubits: Number of qubits for encoding
    """
    # Amplitude encoding for dense representation
    # Normalize to unit vector
    features = features / np.linalg.norm(features)
    
    # Pad to 2^n_qubits dimension
    padded = np.zeros(2**n_qubits)
    padded[:len(features)] = features
    padded = padded / np.linalg.norm(padded)
    
    return padded

def angle_encoding(features, wires):
    """Alternative: angle encoding via rotation gates."""
    for i, feat in enumerate(features):
        qml.RY(feat, wires=wires[i % len(wires)])
        qml.RZ(feat * np.pi, wires=wires[i % len(wires)])
```

### Step 2: Quantum Autoencoder Circuit
```python
def quantum_autoencoder(n_qubits, n_latent, n_layers=3):
    """
    Variational quantum autoencoder circuit.
    
    Args:
        n_qubits: Total input qubits
        n_latent: Compressed latent qubits
        n_layers: Number of variational layers
    """
    n_trash = n_qubits - n_latent  # Trash qubits to discard
    
    def encoder_circuit(features, weights):
        # Input encoding
        angle_encoding(features, range(n_qubits))
        
        # Variational compression layers
        for layer in range(n_layers):
            # Entangling layer
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i+1])
            # Parametrized rotations
            for i in range(n_qubits):
                qml.RY(weights[layer, i], wires=i)
                qml.RZ(weights[layer, n_qubits + i], wires=i)
        
        return # Latent state on first n_latent qubits
    
    def decoder_circuit(latent_weights):
        # Inverse of encoding to reconstruct
        for layer in reversed(range(n_layers)):
            for i in range(n_qubits):
                qml.RZ(-latent_weights[layer, n_qubits + i], wires=i)
                qml.RY(-latent_weights[layer, i], wires=i)
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i+1])
    
    return encoder_circuit, decoder_circuit
```

### Step 3: SWAP Test Fidelity
```python
def swap_test_circuit(state1_wires, state2_wires, ancilla_wire):
    """
    SWAP test to estimate fidelity between two quantum states.
    
    Returns expectation value related to fidelity:
    P(ancilla=0) = (1 + |⟨ψ1|ψ2⟩|²) / 2
    """
    # Hadamard on ancilla
    qml.Hadamard(wires=ancilla_wire)
    
    # Controlled SWAP
    for w1, w2 in zip(state1_wires, state2_wires):
        qml.Toffoli(wires=[ancilla_wire, w1, w2])
    
    # Hadamard on ancilla
    qml.Hadamard(wires=ancilla_wire)
    
    return qml.expval(qml.PauliZ(ancilla_wire))

def compute_fidelity(circuit, original_state, reconstructed_state):
    """Compute fidelity using SWAP test."""
    # Fidelity = 2 * P(0) - 1 = |⟨ψ|ψ'⟩|²
    expectation = circuit(original_state, reconstructed_state)
    fidelity = (expectation + 1) / 2
    return fidelity
```

### Step 4: Training Loop
```python
def train_autoencoder(normal_transactions, n_qubits, n_latent, 
                       n_epochs=50, learning_rate=0.01):
    """
    Train quantum autoencoder on legitimate transactions.
    
    Objective: maximize reconstruction fidelity for normal data.
    """
    # Initialize variational parameters
    weights = np.random.randn(n_layers, 2 * n_qubits) * 0.1
    
    for epoch in range(n_epochs):
        total_loss = 0
        for txn in normal_transactions:
            # Encode
            encoded_state = encode_transaction(txn, n_qubits)
            
            # Forward pass: encode then decode
            reconstructed = autoencoder_forward(encoded_state, weights)
            
            # Fidelity loss
            fidelity = compute_fidelity(encoded_state, reconstructed)
            loss = 1 - fidelity  # Minimize reconstruction error
            
            total_loss += loss
        
        # Gradient update (parameter-shift rule)
        grads = compute_gradients(weights, normal_transactions)
        weights -= learning_rate * grads
        
        avg_loss = total_loss / len(normal_transactions)
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: avg loss = {avg_loss:.4f}")
    
    return weights

def detect_fraud(transaction, trained_weights, threshold=0.85):
    """
    Detect fraud using trained autoencoder.
    
    Returns: (is_fraud, fidelity_score)
    """
    state = encode_transaction(transaction, n_qubits)
    reconstructed = autoencoder_forward(state, trained_weights)
    fidelity = compute_fidelity(state, reconstructed)
    
    is_fraud = fidelity < threshold
    return is_fraud, fidelity
```

## Key Advantages

| Aspect | Classical Autoencoder | FiD-QAE |
|--------|----------------------|---------|
| Feature compression | Linear/nonlinear layers | Quantum variational circuit |
| Anomaly criterion | Reconstruction error (MSE) | Quantum fidelity (SWAP test) |
| High-dimensional data | Curse of dimensionality | Quantum exponential encoding |
| Noise robustness | Depends on architecture | Built-in quantum noise tolerance |
| Hardware validation | N/A | Validated on IBM Quantum |
| Imbalance handling | Requires special techniques | Naturally handles via fidelity threshold |

## Pitfalls

1. **Feature normalization is critical**: Non-normalized financial data causes encoding failures
2. **SWAP test requires two copies**: Need both original and reconstructed states simultaneously
3. **Threshold selection**: Must be calibrated on validation set; domain-specific
4. **Qubit count limits**: Current NISQ devices limit encoding dimensionality
5. **Noise sensitivity**: While robust, deep autoencoder circuits accumulate noise
6. **Training data purity**: Contaminated training set (fraud in "normal" data) degrades performance

## Verification Steps

1. Validate on benchmark fraud datasets (e.g., Kaggle credit card fraud)
2. Test under multiple quantum noise models (depolarizing, amplitude damping, phase damping)
3. Run on real IBM Quantum hardware and compare with simulation
4. Evaluate across different class imbalance ratios
5. Compare F1-score, precision, recall against classical baselines
6. Statistical validation (ANOVA) of performance differences across configurations

## Activation Keywords

quantum autoencoder, fraud detection, fidelity estimation, SWAP test, anomaly detection, quantum machine learning, credit card fraud, financial security, quantum noise robustness, variational quantum circuit, IBM Quantum

## Related Skills

- `qml-fraud-detection-comparison` - Comparative QML architecture analysis for fraud
- `quantum-credit-scoring-interpretable` - Interpretable quantum neural network for credit scoring
- `contextual-qnn-stock-prediction` - Contextual QNN for stock price prediction
- `quantum-anomaly-detection` - General quantum anomaly detection patterns
