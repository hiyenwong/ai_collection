---
name: surrogate-gradient-quantum-reservoir-medical
description: >
  Surrogate-driven training methodology for quantum reservoir computing in medical image classification.
  Overcomes the non-differentiable quantum measurement barrier using differentiable surrogate models
  that emulate the quantum layer, enabling end-to-end backpropagation. Use when training quantum
  reservoir systems, hybrid quantum-classical medical AI pipelines, or Rydberg Hamiltonian-based
  image classification. Triggers: surrogate quantum training, quantum reservoir medical imaging,
  gradient barrier quantum, Rydberg Hamiltonian encoding, differentiable quantum surrogate,
  quantum auto-encoder medical.
---

# Surrogate-Gradient Quantum Reservoir for Medical Imaging

## Core Methodology

Hybrid quantum-classical pipeline for medical image classification using neutral-atom reservoir computing:

1. **Guided auto-encoder**: Learn compact representations of high-dimensional medical images
2. **Surrogate model**: Train differentiable surrogate that emulates the quantum layer
3. **End-to-end backprop**: Jointly optimize classification accuracy + auto-encoder reconstruction
4. **Quantum encoding**: Map latent representations to Rydberg Hamiltonian pulse detuning parameters
5. **Quantum embeddings**: Obtain embeddings via expectation values, pass to linear classifier

## Architecture

```
[Medical Image] -> [Guided Auto-Encoder] -> [Latent z]
    -> [Rydberg Hamiltonian Encoding (pulse detuning)]
    -> [Quantum Reservoir Evolution]
    -> [Expectation Values]
    -> [Linear Classifier]
    
Training: Surrogate model provides gradients through quantum layer
Loss = Classification Loss + Reconstruction Loss (auto-encoder)
```

## Key Design Principles

- **Surrogate emulates quantum**: Differentiable approximation enables gradient flow
- **Joint optimization**: Auto-encoder and classifier trained simultaneously
- **Guided representations**: Auto-encoder produces representations optimized for quantum reservoir
- **Outperforms PCA**: Guided auto-encoder > unguided auto-encoder > PCA for quantum encoding

## Rydberg Hamiltonian Encoding

```
H = sum_i (Omega_i * sigma_x_i - Delta_i * n_i) + sum_{i<j} V_{ij} * n_i * n_j
```

- Latent vector components mapped to detuning parameters Delta_i
- Interaction strength V_{ij} determined by atom distances
- Quantum embeddings from measurement expectation values

## Implementation Pattern

```python
# Surrogate model replaces quantum layer during training
class QuantumReservoirSurrogate(nn.Module):
    def __init__(self, input_dim, reservoir_size):
        super().__init__()
        self.encoder = nn.Sequential(...)  # Maps input to reservoir state
        self.reservoir = nn.Linear(reservoir_size, reservoir_size)  # Emulates quantum evolution
        self.readout = nn.Linear(reservoir_size, num_classes)
    
    def forward(self, x):
        # During training: use surrogate
        h = self.encoder(x)
        h = torch.tanh(self.reservoir(h))  # Nonlinearity emulates quantum measurement
        return self.readout(h)

# During inference: replace surrogate with actual quantum reservoir
def inference_quantum(x, hamiltonian_params):
    # Encode into Rydberg Hamiltonian
    evolve_quantum_state(hamiltonian_params)
    # Measure expectation values
    embeddings = measure_observables()
    return linear_classifier(embeddings)
```

## Application: Polyp Detection

- Binary classification task for medical imaging
- Handles high dimensionality via auto-encoder compression
- NISQ-era compatible with limited qubits

## Activation Keywords
- surrogate quantum training
- quantum reservoir medical imaging
- gradient barrier quantum
- Rydberg Hamiltonian encoding
- differentiable quantum surrogate
- quantum auto-encoder medical
- cold-atom reservoir computing
- neutral-atom quantum classification
- end-to-end quantum backprop
