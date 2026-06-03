---
name: qpinn-trainable-embeddings
description: "QPINN Framework with Quantum Trainable Embeddings for PDE solving. Use when building quantum physics-informed neural networks, variational quantum circuits for PDEs, quantum feature maps for scientific computing, or quantum-assisted fluid dynamics simulations. Triggered by: QPINN, quantum PINN, quantum physics-informed neural network, quantum trainable embeddings, quantum PDE solver, quantum neural network for fluid dynamics."
---

# QPINN with Quantum Trainable Embeddings

Quantum Physics-Informed Neural Network (QPINN) framework using QNN-based trainable embeddings for solving nonlinear PDEs. Based on arXiv:2605.13892 (May 2026).

## Core Methodology

### Architecture

```
Spatial Coordinates → QNN Trainable Embedding → Variational Quantum Circuit → Physics-Informed Loss
```

The key innovation: instead of classical data encoding (fixed feature maps), a QNN learns data-adaptive quantum feature maps that encode spatial coordinates before processing by a variational quantum circuit within a physics-informed loss formulation.

### Key Findings

1. **Stable Training**: QNN-TE-QPINN exhibits stable training behavior compared to classical PINNs and hybrid quantum models with classical embeddings
2. **Competitive Accuracy**: Matches solution accuracy of classical PINNs on nonlinear flow regimes (lid-driven cavity)
3. **Parameter Efficiency**: Requires significantly fewer trainable parameters than classical baselines
4. **Embedding Design Matters**: Embedding design plays a critical role in quantum-assisted PDE solvers

### QPINN Workflow

1. **Problem Setup**: Define PDE (Navier-Stokes, etc.), domain, boundary/initial conditions
2. **Quantum Embedding Layer**: Train a QNN to learn optimal encoding of input coordinates into quantum state space
3. **Variational Quantum Circuit**: Process embedded states through parameterized quantum gates
4. **Physics-Informed Loss**: Compute loss from PDE residuals, boundary conditions, initial conditions
5. **Hybrid Optimization**: Use classical optimizer (Adam, L-BFGS) to update both QNN and VQC parameters

### Implementation Pattern

```python
import pennylane as qml
import torch

# Quantum embedding layer (trainable)
n_qubits = 4
n_layers = 2

dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev, interface="torch")
def quantum_embedding(x, embed_params):
    # Trainable encoding (learned feature map)
    for i in range(n_qubits):
        qml.RY(embed_params[0, i] * x[i % len(x)], wires=i)
    
    # Entangling layer
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
    
    # Additional trainable rotations
    for l in range(1, n_layers + 1):
        for i in range(n_qubits):
            qml.RY(embed_params[l, i], wires=i)
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i + 1])
    
    return qml.expval(qml.PauliZ(0))

# VQC processing
@qml.qnode(dev, interface="torch")
def vqc(encoding, vqc_params):
    # Receive encoded state, apply variational circuit
    qml.Rot(vqc_params[0], vqc_params[1], vqc_params[2], wires=0)
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
    qml.Rot(vqc_params[3], vqc_params[4], vqc_params[5], wires=0)
    return qml.expval(qml.PauliZ(0))

# Physics-informed loss
def qpinn_loss(x_collocation, u_pred, pde_residual):
    # PDE residual loss (Navier-Stokes)
    loss_pde = torch.mean(pde_residual ** 2)
    # Boundary condition loss
    loss_bc = torch.mean((u_pred - u_bc) ** 2)
    return loss_pde + loss_bc
```

### Comparison with Classical PINNs

| Aspect | Classical PINN | QPINN (Classical Encoding) | QPINN (Trainable Embedding) |
|--------|---------------|---------------------------|---------------------------|
| Parameters | High | Medium | **Low** |
| Training Stability | Variable | Often unstable | **Stable** |
| Accuracy | Baseline | Competitive | **Competitive** |
| Expressivity | Standard | Limited by encoding | **Adaptive** |

## Activation Keywords

- QPINN
- quantum PINN
- quantum physics-informed neural network
- quantum trainable embeddings
- quantum PDE solver
- quantum neural network fluid dynamics
- variational quantum PDE
- 量子物理信息神经网络

## Resources

- **Paper**: https://arxiv.org/abs/2605.13892
- **PDF**: https://arxiv.org/pdf/2605.13892
- **Primary Category**: quant-ph
- **Secondary**: physics.flu-dyn

## Notes

- Does NOT claim computational speedup over classical methods
- Focus is on parameter efficiency and training stability
- Embedding design is the key differentiator
- Lid-driven cavity problem used as benchmark (nonlinear flow regime)
- Framework generalizes to other PDE benchmarks
