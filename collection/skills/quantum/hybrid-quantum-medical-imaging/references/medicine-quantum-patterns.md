# Medicine + Quantum ML Research Patterns

## Key Papers and Skills (2026-05-13)

### Hybrid Quantum-Classical Medical Imaging
- **arXiv: 2604.16953** - HQNN for breast cancer thermographic classification
- Combines classical CNN backbone (ResNet/EfficientNet) with parameterized quantum circuits
- Two-phase training: freeze quantum during classical training, then joint fine-tuning
- NISQ-era design: ≤4 circuit depth, RY/RZ encoding

### Quanvolutional Neural Networks
- **arXiv: 2510.23660** - Quanvolutional layers for pneumonia detection from chest X-rays
- Replaces classical conv with quantum feature maps (2x2 patches → 4-8 qubit circuits)
- Hybrid training: classical gradients + parameter-shift for quantum
- Energy-efficient alternative to large CNNs for small medical datasets

### Quantum IoMT Systems
- **arXiv: 2507.04326** - QNN/QSVM for 5G-enabled IoMT healthcare
- Quantum kernel methods (QSVM) for high-dimensional medical sensor classification
- QKD + federated learning for privacy-preserving distributed healthcare AI
- Edge-to-cloud architecture: local inference → 5G transport → quantum cloud processing

## Common Architecture Pattern

```
Input Data -> Classical Preprocessing -> Quantum Encoding
                                            |
                                  Parameterized Quantum Circuit
                                            |
                               Measurement -> Classical Post-processing -> Output
```

## NISQ-Era Constraints

- Circuit depth ≤ 4 for practical deployment
- Qubit count: 4-20 for near-term hardware
- Shot noise requires 1024+ measurements for stable gradients
- Always benchmark against classical baselines first
- Quantum advantage is theoretical for most medical tasks today

## Implementation Libraries

- **PennyLane**: Most accessible for quantum-classical hybrid models
- **Qiskit Machine Learning**: Good for QSVM and quantum kernels
- **TorchQuantum**: PyTorch integration for quantum neural networks

## Pitfalls

- Quantum layers add significant computational overhead
- Shot noise can destabilize training
- NISQ hardware limits practical deployment
- Data encoding overhead can negate quantum advantage for simple tasks
- Quantum advantage is dataset-dependent
