---
name: temperature-scaled-hybrid-fusion
description: "Temperature-Scaled Hybrid Fusion (TSHF) methodology for balancing quantum-classical gradient dynamics in hybrid ML pipelines. Introduces a learnable scalar τ inspired by multimodal learning to resolve optimization asymmetries between quantum and classical branches."
---

# Temperature-Scaled Hybrid Fusion (TSHF)

## Description

TSHF is a methodology for balancing gradient dynamics in hybrid quantum-classical machine learning pipelines. It introduces a learnable temperature scalar τ that dynamically balances the contributions from quantum circuit outputs and classical neural network features during training, resolving optimization bottlenecks that arise from the fundamentally different optimization landscapes of quantum and classical components.

Core insight: quantum and classical branches operate on different gradient scales and convergence rates. A static fusion (averaging) fails because one branch dominates. TSHF learns a scalar that adapts during training to balance both.

**arXiv Source**: 2604.22903 - "On the Complementarity of Quantum and Classical Features"

## Activation Keywords
- temperature-scaled fusion
- TSHF
- hybrid quantum-classical fusion
- quantum-classical gradient balancing
- 温度缩放混合融合
- 量子经典梯度平衡
- hybrid feature fusion medical
- quantum medical diagnosis fusion
- adaptive hybrid fusion

## Core Methodology

### Problem Statement

Hybrid quantum-classical architectures suffer from **optimization asymmetries**:
- Classical CNNs (e.g., ResNet) converge with stable gradients
- Quantum circuits have barren plateaus and noisy gradients
- Naive fusion (concatenation/averaging) causes one branch to dominate
- Result: suboptimal performance that doesn't exceed the best single branch

### TSHF Solution

Introduce a learnable scalar τ (temperature) that dynamically scales the quantum branch contribution:

```
fused_output = classical_features + τ * quantum_features
```

where τ is learned during backpropagation, initialized to balance the magnitudes of both branches.

### Three Fusion Strategies (Progressive)

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **SHF** (Static Hybrid Fusion) | Offline feature extraction, no co-training | Quick prototyping, limited compute |
| **DHF** (Dynamic Hybrid Fusion) | End-to-end co-adaptation, no temperature scaling | When both branches are well-calibrated |
| **TSHF** (Temperature-Scaled Hybrid Fusion) | Learnable τ scalar for dynamic balance | **Recommended** - resolves optimization asymmetries |

### Mathematical Formulation

```python
# TSHF Layer
class TemperatureScaledFusion(nn.Module):
    def __init__(self, classical_dim, quantum_dim, init_tau=1.0):
        super().__init__()
        self.classical_proj = nn.Linear(classical_dim, shared_dim)
        self.quantum_proj = nn.Linear(quantum_dim, shared_dim)
        self.tau = nn.Parameter(torch.tensor(init_tau))  # Learnable
    
    def forward(self, classical_features, quantum_features):
        c = self.classical_proj(classical_features)
        q = self.quantum_proj(quantum_features)
        return c + self.tau * q  # Temperature-scaled fusion
```

## Usage Patterns

### Pattern 1: Medical Image Classification Pipeline

```
Input → [Classical Branch: ResNet] → classical_features
      → [Quantum Branch: Variational Circuit] → quantum_features
      → [TSHF Layer] → fused_features → Classifier → Output
```

**Validated on**: BreastMNIST dataset (breast cancer classification)
**Results**: 87.82% accuracy, 91.77% F1, 89.08% AUC-ROC (vs classical baseline ~85%)

### Pattern 2: Diffusion-Augmented Quantum Classification

Combine with SDA-QEC pattern (from paper 2601.18556):
1. Use diffusion model to augment minority class samples
2. Apply TSHF for quantum-classical feature fusion
3. Deploy for imbalanced medical datasets

### Pattern 3: Multi-Modal Quantum-Classical Fusion

Extend TSHF to multi-modal settings where each modality uses different τ:
```python
tau_visual = nn.Parameter(torch.tensor(1.0))
tau_quantum = nn.Parameter(torch.tensor(1.0))
fused = visual_features * tau_visual + quantum_features * tau_quantum
```

## Implementation Instructions

### Step 1: Set Up Dual-Branch Architecture

```python
# Classical branch
classical_backbone = models.resnet18(pretrained=True)
classical_backbone.fc = nn.Identity()  # Remove final layer

# Quantum branch
import pennylane as qml
n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    qml.AngleEmbedding(inputs, wires=range(n_qubits))
    qml.StronglyEntanglingLayers(weights, wires=range(n_qubits))
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### Step 2: Implement TSHF Layer

```python
class TSHF(nn.Module):
    def __init__(self, c_dim, q_dim, init_tau=0.5):
        super().__init__()
        self.c_proj = nn.Sequential(
            nn.Linear(c_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 128)
        )
        self.q_proj = nn.Sequential(
            nn.Linear(q_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 128)
        )
        self.tau = nn.Parameter(torch.tensor(init_tau))
        self.classifier = nn.Linear(128, num_classes)
    
    def forward(self, c_feat, q_feat):
        c = self.c_proj(c_feat)
        q = self.q_proj(q_feat)
        fused = c + self.tau * q  # Core TSHF operation
        return self.classifier(fused), self.tau
```

### Step 3: Training with Gradient Monitoring

```python
# Monitor τ during training to ensure balanced contributions
for epoch in range(num_epochs):
    output, tau = model(classical_input, quantum_input)
    loss = criterion(output, targets)
    loss.backward()
    optimizer.step()
    
    # Log tau to verify it's learning meaningful values
    if tau < 0.1: print("WARNING: Quantum branch being suppressed")
    if tau > 10: print("WARNING: Classical branch being suppressed")
```

### Step 4: Validation Strategy

- Compare against pure classical baseline (ResNet only)
- Compare against pure quantum baseline (Quantum circuit only)
- Compare against SHF (no learnable τ) and DHF (no scaling)
- Report accuracy, F1, AUC-ROC, and final learned τ value

## Error Handling

### τ Collapses to Zero

**Symptom**: `tau → 0` during training, quantum branch suppressed
**Fix**: 
- Increase init_tau (try 1.0 → 2.0)
- Add gradient clipping to quantum branch
- Use deterministic quantum features (IQP kernel) for stable initialization

### τ Diverges

**Symptom**: `tau → ∞`, classical branch suppressed
**Fix**:
- Add τ regularization: `loss += λ * |τ - 1.0|²`
- Use softplus activation: `tau = softplus(raw_tau)` to constrain τ > 0
- Reduce quantum branch learning rate

### Barren Plateau in Quantum Branch

**Symptom**: Quantum gradient magnitudes → 0
**Fix**:
- Reduce number of qubits (4 → 2)
- Use shallow circuit depth (1-2 entangling layers)
- Switch to IQP (Informationally Complete Quantum) encoding

## Best Practices

1. **Start with 4 qubits**: Proven effective for medical image features
2. **Initialize τ = 0.5**: Gives classical branch slight priority initially
3. **Use ResNet backbone**: Validated on BreastMNIST, good feature extractor
4. **Monitor τ trajectory**: Should converge to a stable non-zero value
5. **Use trainable quantum circuits**: Outperforms deterministic (IQP) in final accuracy
6. **Apply to class-imbalanced data**: Combine with diffusion augmentation (SDA-QEC)

## Related Papers

- **2604.22903**: TSHF original paper (BreastMNIST validation)
- **2604.16953**: HQNN with multi-head attention (thermographic classification)
- **2601.18556**: SDA-QEC (diffusion augmentation + quantum discrimination)

## Related Skills

- `hybrid-quantum-medical-classification` - HQNN for breast cancer thermographic
- `quantum-medical-feature-fusion` - Adaptive hybrid feature fusion
- `quantum-eeg-encoding` - Quantum EEG encoding patterns
- `quantum-medical-imaging` - Quantum medical image analysis