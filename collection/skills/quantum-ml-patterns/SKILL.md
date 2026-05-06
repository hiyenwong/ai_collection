---
name: quantum-ml-patterns
description: >
  Reusable patterns for Quantum Machine Learning (QML) research and implementation.
  Covers Variational Quantum Circuits (VQC), Quantum Neural Networks (QNN),
  Quantum Approximate Optimization Algorithm (QAOA), quantum kernels, and
  hybrid quantum-classical training. Use when analyzing QML papers, designing
  variational quantum algorithms, or implementing quantum-classical hybrid systems.
  Trigger: quantum ML, QML, variational quantum, QNN, QAOA, quantum kernel,
  quantum neural network, VQC, quantum-classical hybrid, quantum advantage.
---

# Quantum Machine Learning Patterns

Reusable patterns extracted from recent QML research papers.

## Pattern 1: Variational Quantum Circuit (VQC) Design

VQCs are parameterized quantum circuits optimized by classical algorithms.

### Core Components
1. **Data encoding layer**: Map classical data to quantum states (angle, amplitude, or basis encoding)
2. **Variational ansatz**: Parameterized gates (RY, RZ, CNOT entangling layers)
3. **Measurement layer**: Extract expectation values as output features
4. **Classical optimizer**: Gradient-based (parameter-shift) or gradient-free (COBYLA, SPSA)

### Common Pitfalls
- **Barren plateaus**: Gradient vanishes exponentially with qubit count; use shallow circuits, local cost functions, or structured initializations
- **Expressivity-trainability tradeoff**: More expressive circuits are harder to train ( Anschuetz & Gao, 2026)
- **Noise sensitivity**: NISQ devices introduce gate errors; consider error mitigation (ZNE, PEC, DDD)

### Implementation Checklist
- [ ] Choose encoding matching data structure
- [ ] Ansatz depth balances expressivity and trainability
- [ ] Use parameter-shift rule for gradient computation
- [ ] Validate with noise simulation before hardware execution

## Pattern 2: QAOA Parameter Scheduling

QAOA solves combinatorial optimization via alternating problem/ mixer Hamiltonians.

### Key Insight
Instead of variational optimization, use **spectral gap informed parameter schedules** (de-variationalization):
- Linear Ramp QAOA: parameters follow adiabatic evolution schedule
- Spectral gap determines optimal transition rate between problem and mixer terms
- Eliminates NP-hard parameter search in many cases

### Application Domains
- MaxCut, graph partitioning, portfolio optimization
- Works best when problem Hamiltonian spectral gap is estimable

## Pattern 3: Quantum Kernel Methods

Quantum embeddings encode classical data into quantum feature states.

### Two Types
1. **Embedding Quantum Kernels (EQK)**: Measure vector similarities in quantum feature space
2. **Projected Quantum Kernels (PQK)**: Project quantum states before similarity measurement

### Design Guidelines
- EQK: High expressivity but sensitive to noise; best for low-dimensional data
- PQK: More robust to noise; better scalability
- Train quantum kernels with QNNs for adaptive feature extraction

## Pattern 4: Distributed Quantum Computing

For problems exceeding single-device capacity:

### Architecture
- Variational quantum linear solver at each node
- Distributed classical optimization coordinates quantum subproblems
- Quantum cost function design enables distributed convergence

### When to Use
- Large linear systems, distributed optimization
- Multi-device quantum networks with classical coordination

## Pattern 5: Geometric/Symmetry-Aware QML

Embed symmetries into quantum circuits via equivariant gates.

### Approach
- Identify symmetry group (finite or compact Lie group)
- Construct equivariant quantum circuit ansatz
- Reduces parameter count and improves generalization
- Particularly effective for PDE solving with geometric structure (GQPINN)

## Pattern 6: Hybrid Tensor Networks with Trainable Post-Selection

Tensor networks as ML models can be hybridized with quantum execution.

### Core Idea
Post-selection is the key property interpolating between classical and quantum tensor networks. Introduce a **trainable hyperparameter** controlling the post-selection budget allocation:
- 0 post-selection → pure classical tensor network
- Full post-selection → pure quantum tensor network
- Partial → hybrid (practical NISQ regime)

### Design Workflow
1. Start with classical tensor network backbone (MPS, PEPS, TTN)
2. Select edges for quantum replacement
3. Define post-selection budget
4. Jointly optimize model parameters + post-selection allocation
5. Let the model learn where quantum matters most

### Key Insight
Post-selection budget complements bond dimension as a second capacity control axis. Trainable allocation beats fixed allocation on NISQ devices.

## Pattern 7: GST-Based Quantum Circuit Synthesis

Generate hardware-native quantum circuits directly from Gate Set Tomography data.

### Architecture Pipeline
Raw GST data → Tokenization → Curriculum Learning → Set-ViT → Concept Space → Diffusion Model → Circuit Synthesis

### Key Advantages
- **End-to-end**: Bypasses traditional GST+unitary-decomposition two-step pipeline
- **Context-aware**: Set-ViT captures shared physical noise (crosstalk, drift) across circuits
- **Generative**: Diffusion model samples circuits conditioned on target measurement distribution

### When to Use
- NISQ devices with complex calibration procedures
- Hardware-native compilation respecting device topology
- Automated calibration reduction

## Pattern 8: Quantum-Enhanced Medical Diagnostics

### Core Architectures
1. **Hybrid QNN-Classical**: Quantum layers on classical backbones for medical imaging
2. **Tensor-Network Quantum Frontends**: Privacy-aware federated learning
3. **Parameter-Efficient Multi-Task**: Shared quantum circuit parameters across diagnostic tasks

### Medical Imaging Workflow
- Preprocessing → Classical feature extraction → Quantum encoding (amplitude/angle) → PQC classifier → Post-processing
- SSL pretraining (SimCLR, BYOL, DINO) before quantum fine-tuning when labels are limited

### Evaluation
- MedMNIST benchmark on 127-qubit IBM hardware
- Fair active learning with weighted entropy for reducing performance disparity across groups

## Verification Steps

When implementing any QML pattern:
1. Verify ansatz expressivity with unitary t-design or entanglement entropy
2. Check gradient magnitude to detect barren plateaus
3. Simulate with noise model matching target hardware
4. Compare against classical baselines (same computational budget)
5. Validate quantum advantage claim: must outperform best classical alternative

## Resources

- Parameter-shift rule: `d⟨O⟩/dθ = (⟨O⟩(θ+π/2) - ⟨O⟩(θ-π/2)) / 2`
- PennyLane, Qiskit, Cirq for VQC implementation
- IBM Quantum, Rigetti, IonQ for hardware access
