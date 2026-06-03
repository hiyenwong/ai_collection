---
name: qml-fraud-detection-comparison
category: quantum-finance
description: Comparative performance analysis methodology for Quantum Machine Learning architectures in financial fraud detection. Systematically evaluates VQC, SQNN, and EQNN classifiers across different quantum feature maps and ansatz configurations with statistical validation.
tags: [quantum-machine-learning, fraud-detection, model-comparison, vqc, sqnn, eqnn, financial-analytics]
---

# QML Fraud Detection Comparison Methodology

## Overview

Systematic comparative analysis of Quantum Machine Learning (QML) architectures for financial fraud detection. Evaluates three QML classifiers — **VQC** (Variational Quantum Classifier), **SQNN** (Sampler Quantum Neural Network), and **EQNN** (Estimator Quantum Neural Network) — across different quantum feature maps and ansatz configurations, with statistical validation (ANOVA) and noise robustness testing.

**Source Paper**: "Comparative Performance Analysis of Quantum Machine Learning Architectures for Credit Card Fraud Detection" (arXiv: 2412.19441)

## Core Principles

### 1. Architecture Comparison Framework
- **VQC (Variational Quantum Classifier)**: Parameterized quantum circuit with classical optimization
- **SQNN (Sampler Quantum Neural Network)**: Sampling-based quantum neural network
- **EQNN (Estimator Quantum Neural Network)**: Estimator-based quantum neural network
- Each architecture has distinct performance characteristics on financial data

### 2. Feature Map and Ansatz Configuration
- Quantum feature maps: encode classical financial data into quantum states
- Ansatz configurations: variational circuit structures for learning
- Performance varies significantly with configuration choices
- Must evaluate multiple combinations systematically

### 3. Statistical Validation
- ANOVA tests confirm significance of observed performance differences
- Multiple performance metrics: F1-score, precision, recall, accuracy
- Results validated across different imbalance levels

### 4. Noise Robustness Testing
- Best-performing models tested under 5 quantum noise types
- Maintains competitive performance under realistic noise conditions
- Validates practical applicability on NISQ devices

## Implementation Steps

### Step 1: QML Architecture Setup
```python
import pennylane as qml
from pennylane import numpy as np

def vqc_circuit(n_qubits, n_layers, feature_map='angle'):
    """
    Variational Quantum Classifier circuit.
    
    Consistently demonstrates strong classification results
    (F1-score of 0.88 in benchmark studies).
    """
    def circuit(inputs, weights):
        # Feature encoding
        if feature_map == 'angle':
            for i in range(n_qubits):
                qml.RY(inputs[i % len(inputs)], wires=i)
        elif feature_map == 'amplitude':
            qml.AmplitudeEmbedding(inputs, wires=range(n_qubits), normalize=True)
        
        # Variational layers
        for layer in range(n_layers):
            # Entangling
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i+1])
            # Parametrized
            for i in range(n_qubits):
                qml.Rot(*weights[layer, i], wires=i)
        
        return qml.expval(qml.PauliZ(0))
    
    return circuit

def sqnn_circuit(n_qubits, n_layers):
    """
    Sampler Quantum Neural Network circuit.
    Uses sampling-based measurement.
    Delivers promising outcomes for fraud detection.
    """
    def circuit(inputs, weights):
        # Encoding
        for i in range(n_qubits):
            qml.RY(inputs[i % len(inputs)], wires=i)
            qml.RZ(inputs[i % len(inputs)] * np.pi, wires=i)
        
        # Variational
        for layer in range(n_layers):
            for i in range(n_qubits):
                qml.CRY(weights[layer, i], wires=[i, (i+1) % n_qubits])
            for i in range(n_qubits):
                qml.RX(weights[layer, n_qubits + i], wires=i)
        
        return [qml.sample(qml.PauliZ(i)) for i in range(n_qubits)]
    
    return circuit

def eqnn_circuit(n_qubits, n_layers):
    """
    Estimator Quantum Neural Network circuit.
    Uses estimator-based measurement.
    Struggles with non-standardized data.
    """
    def circuit(inputs, weights):
        # Encoding
        qml.AngleEmbedding(inputs, wires=range(n_qubits))
        
        # Variational
        for layer in range(n_layers):
            qml.BasicEntanglerLayers(weights[layer], wires=range(n_qubits))
        
        return qml.expval(qml.PauliZ(0))
    
    return circuit
```

### Step 2: Systematic Configuration Evaluation
```python
from itertools import product
import numpy as np

def systematic_evaluation(train_data, train_labels, test_data, test_labels):
    """
    Evaluate all QML architecture configurations systematically.
    """
    architectures = {
        'VQC': vqc_circuit,
        'SQNN': sqnn_circuit,
        'EQNN': eqnn_circuit,
    }
    
    feature_maps = ['angle', 'amplitude', 'iqp', 'zz']
    n_layer_options = [2, 3, 4]
    
    results = {}
    
    for arch_name, arch_fn in architectures.items():
        for fm in feature_maps:
            for n_layers in n_layer_options:
                config_key = f"{arch_name}_{fm}_L{n_layers}"
                
                try:
                    circuit = arch_fn(n_qubits=len(train_data[0]), 
                                     n_layers=n_layers, 
                                     feature_map=fm)
                    
                    # Train and evaluate
                    model = train_qml_model(circuit, train_data, train_labels)
                    metrics = evaluate_model(model, test_data, test_labels)
                    
                    results[config_key] = {
                        'f1': metrics['f1'],
                        'precision': metrics['precision'],
                        'recall': metrics['recall'],
                        'accuracy': metrics['accuracy'],
                        'config': {'arch': arch_name, 'fm': fm, 'layers': n_layers}
                    }
                except Exception as e:
                    results[config_key] = {'error': str(e)}
    
    return results
```

### Step 3: Statistical Validation (ANOVA)
```python
from scipy import stats

def statistical_validation(results):
    """
    ANOVA test to confirm significance of performance differences.
    """
    # Group results by architecture
    vqc_f1 = [r['f1'] for r in results.values() if 'VQC' in r.get('config', {}).get('arch', '') and 'f1' in r]
    sqnn_f1 = [r['f1'] for r in results.values() if 'SQNN' in r.get('config', {}).get('arch', '') and 'f1' in r]
    eqnn_f1 = [r['f1'] for r in results.values() if 'EQNN' in r.get('config', {}).get('arch', '') and 'f1' in r]
    
    # One-way ANOVA
    f_stat, p_value = stats.f_oneway(vqc_f1, sqnn_f1, eqnn_f1)
    
    return {
        'f_statistic': f_stat,
        'p_value': p_value,
        'significant': p_value < 0.05,
        'means': {
            'VQC': np.mean(vqc_f1) if vqc_f1 else 0,
            'SQNN': np.mean(sqnn_f1) if sqnn_f1 else 0,
            'EQNN': np.mean(eqnn_f1) if eqnn_f1 else 0,
        }
    }
```

### Step 4: Noise Robustness Testing
```python
def noise_robustness_test(best_model, noise_types=5):
    """
    Test model robustness under quantum noise models.
    """
    noise_models = [
        qml.AmplitudeDamping,
        qml.PhaseDamping, 
        qml.DepolarizingChannel,
        qml.BitFlip,
        qml.PhaseFlip,
    ]
    
    results = {}
    for noise in noise_models[:noise_types]:
        # Apply noise to circuit
        noisy_model = apply_noise(best_model, noise, probability=0.01)
        metrics = evaluate_model(noisy_model, test_data, test_labels)
        results[noise.__name__] = metrics
    
    return results
```

## Key Findings from Research

| Architecture | F1-Score | Data Sensitivity | Noise Robustness |
|-------------|----------|-----------------|------------------|
| **VQC** | 0.88 | Low (robust) | High |
| **SQNN** | ~0.80-0.85 | Moderate | Moderate |
| **EQNN** | < 0.70 | High (struggles with non-standardized data) | Low |

**Key insight**: VQC consistently demonstrates strong classification results across configurations. EQNN struggles significantly with non-standardized financial data, emphasizing the importance of data preprocessing.

## Pitfalls

1. **Data standardization is critical**: EQNN fails on non-normalized data; always preprocess
2. **Configuration matters more than architecture**: Feature map and ansatz choices dominate performance
3. **Small dataset quantum advantage**: QML may not show advantage on small classical datasets
4. **Noise threshold**: Performance degrades rapidly above certain noise levels
5. **ANSOVA assumptions**: Ensure normality and homogeneity of variance before ANOVA
6. **Reproducibility**: Quantum circuit initialization affects results; use fixed seeds

## Verification Steps

1. Reproduce VQC F1-score of 0.88 on benchmark fraud dataset
2. Run ANOVA to confirm significance of architecture differences
3. Test all 5 noise types on best model
4. Validate on two different non-normalized financial fraud datasets
5. Compare against classical baseline (e.g., Random Forest, XGBoost)
6. Statistical validation with multiple random seeds

## Activation Keywords

quantum machine learning comparison, VQC, SQNN, EQNN, fraud detection architecture, quantum feature map, ansatz configuration, ANOVA validation, quantum noise robustness, financial fraud classification, QML benchmark

## Related Skills

- `fid-quantum-autoencoder-fraud` - Quantum autoencoder for fraud detection
- `contextual-qnn-stock-prediction` - Contextual QNN for stock prediction
- `qml-model-testing` - QML model testing and robustness analysis
- `quantum-credit-scoring-interpretable` - Interpretable quantum neural network for credit scoring
