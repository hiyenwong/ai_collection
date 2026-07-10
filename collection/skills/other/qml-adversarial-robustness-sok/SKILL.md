---
name: qml-adversarial-robustness-sok
description: "SoK: Critical Evaluation of Quantum Machine Learning for Adversarial Robustness. Comprehensive systematization of adversarial attacks on QML systems across black-box, gray-box, and white-box threat models with empirical evaluation of poisoning, backdoor, and evasion attacks. Reveals accuracy-robustness trade-offs between encoding schemes and proposes threat-aware, noise-resilient framework for secure QML deployment. Trigger: QML security, quantum adversarial robustness, quantum classifier attack, SoK quantum machine learning, quantum backdoor, QMLP evaluation."
---

# QML Adversarial Robustness SoK

Comprehensive systematization of adversarial robustness in Quantum Machine Learning (QML) systems.
Based on arXiv:2511.14989 by Nowmi, Lopez, Imon, Pouryousef, Rahman (2026).

## Core Findings

### Accuracy-Robustness Trade-off

1. **Amplitude encoding**: Highest clean accuracy (92.6% MNIST, 67% AZ-Class) but collapses under adversarial perturbations + depolarizing noise
2. **Angle encoding**: Shallower models more stable under attack
3. **Circuit depth impact**: Models evaluated at depths 2, 5, 10, and 50 layers
4. **QMLP vs CMLP**: QMLP more robust to label-flipping poisoning but substantially more vulnerable to gradient-based evasion (FGSM, PGD)

### Attack Taxonomy

| Threat Model | Attack | Description |
|---|---|---|
| Black-box | Label-flipping poisoning | Flips training labels without model access |
| Gray-box | Encoder-level indiscriminate poisoning | Poisons at quantum encoder level |
| Gray-box | Proxy-model clean-label backdoor | Backdoor via surrogate model |
| White-box | Circuit-level backdoor (QTrojan) | Hardware-level trojan insertion |
| White-box | Gradient-based evasion (FGSM, PGD) | Adversarial example generation |

### Key Results

- **QUID defense**: Effective noiseless, weakened under noise
- **Proxy-model backdoor**: Persists unless circuit overwhelmed
- **Circuit-level backdoor**: Fails in multi-class setting (scalability limitation)
- **Depth vs robustness**: Deeper circuits not necessarily more robust

## Implementation Guide

### QMLP Architecture for Security Testing

```python
import pennylane as qml
import numpy as np

def create_qmlp(n_qubits, n_layers, encoding='angle'):
    """Create Quantum MLP for adversarial robustness testing."""
    dev = qml.device('default.qubit', wires=n_qubits)

    @qml.qnode(dev)
    def circuit(inputs, weights):
        # Encoding
        if encoding == 'angle':
            for i in range(n_qubits):
                qml.RY(inputs[i], wires=i)
        elif encoding == 'amplitude':
            qml.AmplitudeEmbedding(inputs, wires=range(n_qubits), normalize=True)

        # Variational layers
        for layer in range(n_layers):
            for i in range(n_qubits):
                qml.Rot(weights[layer, i, 0], weights[layer, i, 1], weights[layer, i, 2], wires=i)
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i + 1])

        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

    return circuit
```

### Adversarial Attack Implementation

```python
def fgsm_attack(model, inputs, labels, epsilon=0.1):
    """FGSM attack on QML model."""
    inputs_grad = inputs.copy()
    # Compute gradient of loss w.r.t. input
    with qml.que.AnnotatedQueue() as q:
        loss = model(inputs_grad, labels)
    # Gradient ascent on loss
    grad = qml.grad(lambda x: model(x, labels))(inputs_grad)
    adversarial = inputs_grad + epsilon * np.sign(grad)
    return adversarial

def label_flipping_poison(train_data, flip_rate=0.1):
    """Black-box label flipping poisoning."""
    n_poison = int(len(train_data) * flip_rate)
    indices = np.random.choice(len(train_data), n_poison, replace=False)
    poisoned = train_data.copy()
    for idx in indices:
        poisoned[idx]['label'] = 1 - poisoned[idx]['label']
    return poisoned
```

### Threat-Aware Evaluation Protocol

1. **Phase 1**: Clean accuracy baseline (no attack, no noise)
2. **Phase 2**: Noise-only evaluation (depolarizing channel at varying rates)
3. **Phase 3**: Attack-only evaluation (each attack type independently)
4. **Phase 4**: Combined attack + noise (realistic threat model)
5. **Phase 5**: Defense evaluation (QUID, adversarial training)

### Recommended Depth-encoding Combinations

| Use Case | Encoding | Depth | Reason |
|---|---|---|---|
| High accuracy (noisy env) | Angle | 2-5 | Stable under noise |
| Max accuracy (clean env) | Amplitude | 10-50 | Best clean performance |
| Security-critical | Angle | 2-5 | Most robust to attacks |
| Backdoor detection | Angle | 5 | Balance detectability + stability |

## Pitfalls

- **Amplitude encoding + noise = collapse**: Do NOT use amplitude encoding in noisy/deployed environments
- **Circuit-level backdoors don't scale**: Multi-class QML inherently resistant to QTrojan
- **QMLP != more robust overall**: Better against poisoning, worse against evasion
- **Depth does not equal security**: Deeper circuits ≠ more robust to adversarial attacks
- **QUID needs calibration**: Defense effectiveness degrades with realistic noise levels
- **Gray-box proxy backdoors persistent**: These attacks survive most defenses unless circuit capacity is overwhelmed

## Activation

qml adversarial robustness, quantum machine learning security, QML attack evaluation, quantum classifier adversarial, SoK quantum security, QMLP robustness, quantum backdoor detection, QUID defense, quantum adversarial training, quantum poisoning attack, FGSM PGD quantum, amplitude encoding vulnerability, angle encoding robustness