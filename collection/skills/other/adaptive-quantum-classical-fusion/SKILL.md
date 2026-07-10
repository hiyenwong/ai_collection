---
name: adaptive-quantum-classical-fusion
description: "Adaptive quantum-classical feature fusion methodologies for medical AI diagnosis. Covers Temperature-Scaled Hybrid Fusion (TSHF), tensor-network compression with quantum refinement, and multi-head quantum-aware encoding. Use when building hybrid quantum-classical models for medical image classification, federated healthcare diagnosis, or quantum-enhanced diagnostic pipelines. Activation: quantum medical, hybrid quantum classical, quantum diagnosis, quantum feature fusion, breast cancer quantum, federated quantum medical, TSHF, tensor network quantum"
---

# Adaptive Quantum-Classical Fusion for Medical AI

Methodologies for combining quantum computing with classical deep learning in medical diagnosis contexts, extracted from arXiv papers (2026-04).

## Core Patterns

### 1. Temperature-Scaled Hybrid Fusion (TSHF)
**Paper**: arXiv:2604.22903 (Sobrinho et al.)

Three progressive fusion strategies for hybrid quantum-classical architectures:

| Strategy | Use Case | Mechanism |
|----------|----------|-----------|
| **SHF** (Static) | Offline extraction | Fixed concatenation of classical + quantum embeddings |
| **DHF** (Dynamic) | End-to-end training | Co-adaptive gradient flow between branches |
| **TSHF** (Temperature-Scaled) | Production | Learnable scalar τ balances gradient dynamics: `output = softmax(classical/τ, quantum/τ)` |

**Key insight**: TSHF resolves optimization asymmetries between classical and quantum branches. With ResNet + trainable quantum circuit on BreastMNIST: 87.82% accuracy, 91.77% F1, 89.08% AUC-ROC.

**Implementation guide**:
- Dual-branch: classical backbone (ResNet/CNN) + parameterized quantum circuit
- Quantum circuit: trainable gates, strongly entangling layers
- TSHF scalar: init τ=1.0, learnable via backprop
- Prefer TSHF when gradient magnitudes differ between branches

### 2. Tensor-Network + QEP Co-Design
**Paper**: arXiv:2604.01616 (Yamauchi et al.)

Tensor-network frontends compress high-dimensional medical images before quantum processing:

```
Raw Image → [MPS/TTN/MERA] → Compressed Latent → [QEP] → Classification
                    ↑                          ↑
              Compression               Quantum refinement
              (client-side)             (post-aggregation)
```

**Frontend comparison**:
- **TTN + QEP**: Most balanced — best accuracy/latency/communication trade-off
- **MPS + QEP**: Fastest compression, lower expressivity
- **MERA + QEP**: Highest expressivity, most compute

**Dual role of tensor-network compression**:
1. Enables small-qubit quantum processing on compressed features
2. Reduces MPC communication overhead in federated settings

**Design rule**: Match qubit count to latent dimension. TTN output dimension should equal 2^n_qubits.

### 3. Multi-Head Quantum-Aware Encoding
**Paper**: arXiv:2604.16953 (Syah et al.)

Quantum circuits with multi-head attention for feature encoding:

- 4-qubit variational circuit with strongly entangling layers
- Multi-head attention captures cross-feature quantum correlations
- Classical CNN layers handle spatial pattern recognition
- Quantum branch handles global feature relationships

**Performance**: Superior convergence dynamics vs. purely classical CNNs on thermographic breast cancer data.

## Decision Table

```
Task                              → Recommended Pattern
Breast cancer classification      → TSHF (SHF if offline)
Federated medical diagnosis       → TTN + QEP (privacy-aware)
Thermographic analysis            → Multi-head quantum encoding
Low-qubit constraint (< 10)       → Tensor-network compression first
High-dimensional input            → MERA frontend + QEP
End-to-end trainable pipeline     → DHF or TSHF
Production deployment             → TSHF (adaptive balancing)
```

## Implementation Considerations

### Quantum Circuit Design
- Use **strongly entangling layers** for expressivity
- **4-qubit circuits** sufficient for compressed latent features
- Prefer **trainable** over **deterministic** (data re-uploading) circuits

### Data Preparation
- Normalize inputs to unit sphere before quantum encoding
- For medical images: consider dimensionality reduction (PCA/tensor-network) before angle encoding
- BreastMNIST/PneumoniaMNIST are good benchmark datasets

### Classical Backbone
- ResNet-family backbones work well with quantum circuits
- CNN + quantum circuit: quantum branch should handle global features
- Avoid placing quantum circuit too early in pipeline (information bottleneck)

## Related Existing Skills
- `hybrid-quantum-medical-diagnosis` — broader QML medical diagnosis patterns
- `quantum-medical-feature-fusion` — general feature fusion approaches
- `federated-quantum-medical-diagnosis` — federated learning with quantum
- `tensor-network-quantum-federated` — tensor network methods for quantum FL

## References
- arXiv:2604.22903 — Adaptive Hybrid Quantum-Classical Feature Fusion (kg_entity: check by URL)
- arXiv:2604.01616 — Tensor-Network Frontends for Federated Medical Diagnosis
- arXiv:2604.16953 — Hybrid QNN for Breast Cancer Thermographic Classification
