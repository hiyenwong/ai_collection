---
name: quantum-adversarial-defense
description: "Quantum adversarial defense methodology using quantum autoencoders for protecting quantum classifiers against adversarial perturbations. Covers quantum autoencoder purification, adversarial training-free defense frameworks, confidence metrics for adversarial sample detection, and evaluation of variational quantum classifiers under attack. Use when defending QML models, analyzing quantum adversarial robustness, implementing purification-based defenses, or studying adversarial attacks on variational quantum circuits."
---

# Quantum Adversarial Defense via Quantum Autoencoders

Defense framework for protecting quantum machine learning classifiers against adversarial perturbations using quantum autoencoder-based purification.

## Background

Quantum machine learning models, particularly variational quantum classifiers (VQCs), are vulnerable to adversarial attacks — carefully crafted noise inserted into input data that causes misclassification. While adversarial training (training on adversarial examples) is a common defense, it has practical limitations: it may not be feasible when adversarial samples cannot be generated during training, and models can overfit to specific attack types.

## Core Methodology

### Quantum Autoencoder Purification Framework

The defense uses a quantum autoencoder (QAE) to purify adversarial samples through reconstruction:

```
Adversarial Input → Quantum Encoder → Compressed Latent → Quantum Decoder → Purified Output → Quantum Classifier → Prediction
```

**Key insight**: The quantum autoencoder learns to compress and reconstruct legitimate data manifold. Adversarial perturbations, being off-manifold, are attenuated during the compression-decompression cycle.

### Confidence Metric

The framework provides a confidence metric to identify adversarial samples that cannot be effectively purified:

```python
def purification_confidence(input_state, purified_state):
    """
    Compute fidelity between input and reconstructed state.
    Low fidelity indicates the input may be adversarial
    and cannot be reliably purified.
    """
    fidelity = |<input|purified>|^2
    return fidelity
```

### Two-Stage Defense Pipeline

1. **Purification Stage**: Pass input through quantum autoencoder
2. **Detection Stage**: If reconstruction fidelity is below threshold, flag as potentially adversarial

## Implementation

### Quantum Autoencoder Circuit

```python
import pennylane as qml
import numpy as np

class QuantumAutoencoderDefense:
    def __init__(self, n_qubits, n_latent, n_layers=2):
        self.n_qubits = n_qubits
        self.n_latent = n_latent  # Compressed dimension
        self.n_layers = n_layers
        self.n_trash = n_qubits - n_latent
        
    def encoder(self, params, wires):
        """Encode input into latent space, discarding trash qubits."""
        for layer in range(self.n_layers):
            # Entangling layers
            for i in range(self.n_qubits - 1):
                qml.CNOT(wires=[wires[i], wires[i+1]])
            # Parameterized rotations
            for i in range(self.n_qubits):
                qml.Rot(*params[layer * self.n_qubits + i], wires=wires[i])
    
    def purification_cost(self, input_circuit, params):
        """
        Cost function: maximize fidelity between
        original clean states and purified outputs.
        Trash qubits should be in |0> state after encoding.
        """
        # Apply input state preparation
        input_circuit()
        
        # Encode
        self.encoder(params, wires=range(self.n_qubits))
        
        # Cost: trash qubits should be |0>
        trash_expectation = sum(
            qml.expval(qml.PauliZ(i)) for i in range(self.n_latent, self.n_qubits)
        )
        return trash_expectation
    
    def purify(self, adversarial_state, encoder_params):
        """
        Purify an adversarial input by encoding-decoding.
        """
        # Encode: compress to latent space
        # Decode: reconstruct from latent space
        # The adversarial noise is reduced in the process
        pass
    
    def detect_adversarial(self, input_state, purified_state, threshold=0.9):
        """
        Detect if input is adversarial based on purification quality.
        Returns: (is_adversarial, confidence_score)
        """
        fidelity = self.compute_fidelity(input_state, purified_state)
        is_suspicious = fidelity < threshold
        return is_suspicious, fidelity
```

### Variational Quantum Classifier (Target Model)

```python
class VariationalQuantumClassifier:
    def __init__(self, n_qubits, n_layers=2):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        
    def circuit(self, features, weights):
        """VQC circuit for classification."""
        # Data encoding
        for i in range(self.n_qubits):
            qml.RY(features[i], wires=i)
        
        # Variational layers
        for layer in range(self.n_layers):
            for i in range(self.n_qubits):
                qml.Rot(*weights[layer][i], wires=i)
            for i in range(self.n_qubits - 1):
                qml.CNOT(wires=[i, i+1])
        
        # Measurement
        return qml.expval(qml.PauliZ(0))
```

### Defense Integration

```python
class AdversarialDefensePipeline:
    def __init__(self, autoencoder, classifier):
        self.qae = autoencoder
        self.classifier = classifier
    
    def predict(self, input_state, qae_params, vqc_weights):
        """
        Full defense pipeline:
        1. Purify input through QAE
        2. Classify purified state
        3. Return prediction + confidence
        """
        purified = self.qae.purify(input_state, qae_params)
        confidence = self.qae.detect_adversarial(input_state, purified)
        prediction = self.classifier.circuit(purified, vqc_weights)
        return prediction, confidence
    
    def evaluate_under_attack(self, test_data, attack_fn, qae_params, vqc_weights):
        """
        Evaluate defense effectiveness under adversarial attack.
        Compare: accuracy without defense vs with QAE defense.
        """
        results = {
            'clean_accuracy': self.evaluate(test_data, vqc_weights),
            'attacked_accuracy': self.evaluate(test_data, attack_fn, vqc_weights),
            'defended_accuracy': self.evaluate_with_defense(
                test_data, attack_fn, qae_params, vqc_weights
            )
        }
        return results
```

## Training Procedure

### Phase 1: Train Quantum Autoencoder

Train on clean (non-adversarial) data only:

```python
def train_autoencoder(qae, clean_data, n_epochs=100):
    """
    Train QAE to compress and reconstruct clean data.
    No adversarial samples needed during training.
    """
    optimizer = qml.AdamOptimizer(learning_rate=0.01)
    params = qae.init_params()
    
    for epoch in range(n_epochs):
        for sample in clean_data:
            cost = qae.purification_cost(sample, params)
            params = optimizer.step(
                lambda p: qae.purification_cost(sample, p), params
            )
    
    return params
```

### Phase 2: Train Quantum Classifier

Train classifier on purified data:

```python
def train_classifier_with_defense(vqc, qae, qae_params, clean_data, labels):
    """Train VQC using QAE-purified inputs."""
    optimizer = qml.GradientDescentOptimizer(learning_rate=0.1)
    weights = vqc.init_weights()
    
    for epoch in range(n_epochs):
        for x, y in zip(clean_data, labels):
            purified = qae.purify(x, qae_params)
            loss = vqc.loss(purified, y, weights)
            weights = optimizer.step(
                lambda w: vqc.loss(purified, y, w), weights
            )
    
    return weights
```

## Evaluation Metrics

| Metric | Description |
|--------|-------------|
| Clean Accuracy | Accuracy on unperturbed test data |
| Attacked Accuracy | Accuracy under adversarial attack (no defense) |
| Defended Accuracy | Accuracy under attack with QAE defense |
| Improvement | Defended - Attacked accuracy (up to 68% reported) |
| Detection Rate | % of adversarial samples correctly flagged |
| False Positive Rate | % of clean samples incorrectly flagged |

## Key Advantages

1. **Training-Free Defense**: No adversarial training required
2. **Attack-Agnostic**: Works against various attack types, not overfit to one
3. **Confidence Scoring**: Provides detectability metric for uncertain samples
4. **NISQ Compatible**: Uses shallow quantum circuits
5. **Dual Protection**: Both purifies attack samples AND detects un-purifiable ones

## Activation Keywords

- quantum adversarial defense
- quantum autoencoder defense
- adversarial quantum classifier
- quantum adversarial robustness
- QAE purification
- variational quantum classifier defense
- quantum ML security
- adversarial perturbation quantum

## Tools Used

- exec: Run quantum simulations with PennyLane or Qiskit
- python: Implement quantum autoencoder circuits and defense evaluation

## Best Practices

1. Train QAE on diverse clean data for better purification
2. Tune reconstruction fidelity threshold per dataset
3. Evaluate against multiple attack types (FGSM, PGD, etc.)
4. Use the confidence metric to reject suspicious inputs
5. Report improvement over undefended baseline

## Limitations

- Requires additional quantum circuit depth for QAE
- Purification quality depends on autoencoder capacity
- Some sophisticated attacks may bypass purification
- Threshold tuning is dataset-dependent
- Evaluated primarily on image classification tasks

## Related Skills

- quantum-reservoir-computing
- quantum-neural-architecture
- hybrid-quantum-classical-architecture

## References

- Paper: "Defending Quantum Classifiers against Adversarial Perturbations through Quantum Autoencoders" (arXiv:2604.28176v1)
- Authors: Emma Andrews, Sahan Sanjaya, Prabhat Mishra
- Published: 2026-04-30
- Categories: quant-ph, cs.LG
