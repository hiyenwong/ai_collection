---
name: hybrid-quantum-gan
description: Hybrid quantum-classical GAN architecture for adversarial generation tasks. Use when generating adversarial network traffic, quantum-enhanced generative modeling, or hybrid quantum-classical neural network design.
---

# Hybrid Quantum-Classical GANs

## Description
Generative Adversarial Networks combining quantum variational circuits with classical neural layers. Quantum generator leverages high-dimensional Hilbert space for enhanced expressivity.

## Architecture

### Quantum Generator
```
Classical noise z → Classical encoder → Quantum embedding → 
Variational Quantum Circuit (VQC) → Measurement → Classical decoder → Generated sample
```

### Classical Discriminator
```
Real/Fake sample → Classical neural network → Discrimination output
```

### Training Loop
```python
for epoch in range(epochs):
    # Train Discriminator
    real_loss = D(real_data)
    fake_data = G(z)
    fake_loss = D(fake_data.detach())
    d_loss = real_loss + fake_loss
    d_loss.backward()
    
    # Train Generator (with quantum circuit)
    fake_data = G(z)
    g_loss = D(fake_data)
    g_loss.backward()
    # Parameter-shift rule for quantum gradients
```

## Key Components
1. **Quantum Embedding**: Angle embedding or amplitude encoding
2. **Variational Circuit**: Strong entangling layers or hardware-efficient ansatz
3. **Measurement**: Pauli-Z expectation values on all qubits
4. **Classical Decoder**: Linear layer mapping measurements to output space

## NISQ Considerations
- Qubit count: 4-16 qubits typical
- Circuit depth: < 10 layers for current hardware
- Gradient estimation: parameter-shift rule (2 evaluations per parameter)
- Shot noise: use analytical simulator for training, add shot noise for deployment

## Applications
- Adversarial network traffic generation
- Quantum-enhanced data augmentation
- Anomaly detection in cybersecurity
- Financial time series generation
