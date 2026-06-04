---
name: quantum-ml-patterns
description: >
  Reusable patterns for Quantum Machine Learning (QML) research and implementation.
  Covers Variational Quantum Circuits (VQC), Quantum Neural Networks (QNN),
  Quantum Approximate Optimization Algorithm (QAOA), quantum kernels, QUBO-encoded
  RL policy search, and hybrid quantum-classical training. Use when analyzing QML
  papers, designing variational quantum algorithms, or implementing quantum-classical
  hybrid systems. Trigger: quantum ML, QML, variational quantum, QNN, QAOA, quantum
  kernel, quantum neural network, VQC, quantum-classical hybrid, quantum advantage,
  QUBO policy search, quantum process synthesis.
---

# Quantum Machine Learning Patterns

## Reference Files
- `references/quantum-hilbert-ml.md` — Quantum Hilbert space prototype learning with MPS, Born rule classification, quantum probability geometry
- `references/quantum-rl-process-synthesis.md` — QUBO-encoded RL policy search for process synthesis (arXiv: 2605.21213)

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
- **Expressivity-trainability tradeoff**: More expressive circuits are harder to train (Anschuetz & Gao, 2026)
- **Noise sensitivity**: NISQ devices introduce gate errors; consider error mitigation (ZNE, PEC, DDD)
- **Encoding metric fallacy**: Entanglement capability and Fourier decomposition provide minimal insight into actual encoding performance. Use **effective rank of feature maps** instead — it correlates with QML model performance and can serve as a threshold criterion to prune poor encodings before expensive training (arXiv:2605.18540)

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

### ⚠️ Exponential Concentration Problem (Updated 2026-06-02)
The fidelity quantum kernel $K(x,x') = |\langle\psi(x)|\psi(x')\rangle|^2$ suffers from **exponential concentration** as qubit count increases — kernel values collapse to a constant, rendering SVM useless beyond few-qubit systems.

**Solution: Hamming Quantum Kernel** (arXiv:2605.31449)
- Uses **full measurement statistics** instead of single fidelity value
- Classical post-processing only — zero additional quantum resources
- Outperforms fidelity kernel at ≥15 qubits, classical Gaussian on synthetic quantum data
- Scales to 27 qubits in simulation
- **When to use**: Any quantum SVM with ≥15 qubits where fidelity kernel shows concentration

### Spectral Entropy Diagnostic for Kernel Selection (Updated 2026-06-02)
Normalized spectral entropy $S(K)/\log n$ of the kernel Gram matrix governs both QGP dequantization and posterior pathology (arXiv:2605.30952):
- **High entropy** → optimal for smooth targets
- **Low entropy** → optimal for band-limited quantum data
- Kernel-agnostic: hardware-efficient, matchgate, IQP, RBF/Matern all collapse onto identical diagnostic curves
- Verified on IBM Heron hardware (median error 3.2%)
- **Diagnostic use**: Compute $S(K)/\log n$ before expensive quantum circuit execution to select kernel family

## Pattern 4: Distributed Quantum Computing

For problems exceeding single-device capacity:

### Architecture
- Variational quantum linear solver at each node
- Distributed classical optimization coordinates quantum subproblems
- Quantum cost function design enables distributed convergence
- **Q-ANCHOR** (arXiv:2605.30075): Quantum Federated Learning with ZNE-guided server anchoring + stateful client correction to address double-drift (client drift from non-IID data + hardware bias from noisy quantum gradients)

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

### Detailed Medical Sub-Patterns

See [references/quantum-medical.md](references/quantum-medical.md) for full details on:
- **Hybrid Quantum-Classical Medical Modeling** — Classical preprocessing + quantum feature map + VQC (EEG, MRI, clinical data)
- **Quantum Generative Models for Medical Imaging** — QGANs/QCBMs for image enhancement (knee X-rays, medical MNIST)
- **Quantum Kernel Methods for Medical Foundation Models** — Quantum kernels overcome classical "kernel collapse" in high-dim embeddings
- **Quantum Optimization for Clinical Trials & Drug Discovery** — QUBO/QAOA/VQE for patient stratification and molecular simulation
- **Continuous-Variable QNNs for Biomedical Imaging** — Photonic quantum systems for continuous medical data
- **Tensor Network Feature Engineering** — Tucker/CP decomposition from sparse MRI for multi-class neurological disorder prediction; factor matrices reveal important brain regions (arXiv:2605.17771)
- **Adaptive Feature Fusion** — Gate-based module learns per-sample quantum/classical feature weighting; reveals when quantum complements classical (arXiv:2604.22903)
- Implementation checklist (encoding, circuit depth, metrics, NISQ constraints)
- Common pitfalls (data encoding bottleneck, barren plateaus, class imbalance, reproducibility)

## Pattern 9: QUACOD — Coordinate Descent for NISQ Optimization

Decompose large-scale optimization problems into quantum-solvable subproblems via classical coordinate descent, enabling NISQ devices to handle problems far exceeding their qubit count.

### Core Algorithm
1. **Formulate as QUBO/Ising**: Express objective as `min x^T Q x + c^T x` with constraints
2. **Block partitioning**: Divide n-bit variables into blocks of size k ≤ available qubits
3. **Iterative solve**: Fix variables outside block, solve subproblem quantumly, update block
4. **Block selection**: Greedy (max |Q_ij|) for strong coupling; random for weak coupling; graph-based for sparse Q

### Key Results
- 5x problem size scaling vs direct quantum approach (arXiv:2605.14001)
- Hardware-efficient circuits outperform deep theoretical circuits on real NISQ devices
- Monotone descent guarantee — each subproblem solve improves or maintains objective

### Application Domains
- **Portfolio optimization**: Mean-variance with cardinality constraints, decompose N assets into k-asset subproblems
- **Scheduling/routing**: Job-shop, vehicle routing, drone delivery
- **Feature selection**: L0-regularized regression with sparse variable selection

### Implementation Template
```python
def quacod_solve(Q, c, n, k_qubits, max_iter=100):
    x = np.random.randint(0, 2, n)
    for _ in range(max_iter):
        block = select_block(x, Q, k_qubits)  # greedy/random/graph
        sub_Q = Q[np.ix_(block, block)]
        sub_c = c[block] + 2 * Q[np.ix_(block, ~block)] @ x[~block]
        x[block] = quantum_optimize(sub_Q, sub_c)  # VQE/QAOA on subproblem
        if converged(x): break
    return x
```

### Critical Pitfall
**Block size ≠ qubit count**: k should account for ancilla qubits needed by the ansatz. If you need 2 ancillas per logical qubit, set `k = available_qubits / 2`.

## Pattern 10: Quantum-Inspired Dequantization

Classical polynomial-time algorithms that match purported quantum advantages, using the right mathematical tools.

### Core Technique: Ridgelet Transform Sampling
For neural network lottery ticket (sparse subnetwork) selection:
- Compute ridgelet transform of output weights → optimized probability distribution
- Sample hidden nodes from this distribution in O(poly(D)) time
- Matches quantum O(D) sampling quality classically (arXiv:2605.13979)

### When to Suspect Dequantization
- Quantum algorithm relies on state preparation + sampling from structured distribution
- The distribution can be classically approximated via Monte Carlo or transform methods
- Claims of exponential quantum speedup on classical ML tasks

### Design Implication
Before investing in quantum hardware for ML tasks, verify the quantum speedup is not eliminable via classical polynomial-time approximation. Many "quantum ML advantages" are dequantizable.

## Pattern 11: Quantum End-to-End Learning for Contextual Combinatorial Optimization

QEL (Lee & Kwon, arXiv:2605.20222) — the first quantum end-to-end learning framework for contextual combinatorial optimization (CCO).

### Architecture
```
Context → Re-uploading Phase-Separator → Quantum Surrogate Policy (QAOA) → Task Loss → Backprop
```

### Key Innovation: Context Re-uploading Phase-Separator
- Encodes contextual features directly into the quantum circuit via repeated data re-uploading layers
- Analogous to state preparation in QAOA, but jointly captures relations among contexts, uncertain coefficients, and optimal solutions
- Contextual encoder integrates seamlessly within the quantum policy

### Advantages Over Classical Methods
- **Fewer parameters** than classical benchmarks
- **No NP-hard solver calls** — direct task-loss training despite discreteness and nonconvexity
- **Stationarity guarantee** — gradient-based training converges despite nonconvexity
- Exploits optimization-aware structure grounded in quantum physical principles

### When to Use
- Resource allocation under uncertainty with contextual features
- Routing with time-varying demands
- Portfolio optimization with market context
- Any CCO problem where context-to-solution mapping is complex

## Pattern 12: Bowtie VarQTE — Resource-Efficient Quantum State Preparation

Bowtie VarQTE (Drudis et al., arXiv:2605.20331) — hybrid classical-quantum variational time evolution using causal light-cone optimization.

### Core Mechanism
For local Hamiltonians, the **causal light-cone** of an operator determines which qubits influence the measurement. Terms within the light-cone can be simulated classically; only genuinely quantum terms require quantum evaluation.

### Algorithm
1. Compute light-cones for each gradient and QGT term
2. Classical simulation for causally relevant subcircuits
3. Quantum evaluation only for non-causal terms
4. Exact parameter updates via **McLachlan's variational principle** (A θ̇ = C)

### Comparison with AQC
| Aspect | AQC | Bowtie VarQTE |
|--------|-----|---------------|
| Target state representation | Required classically | Not needed |
| Fidelity | High | Comparable |
| Quantum cost | Higher | Reduced via light-cone |
| Numerical stability | May degrade | Improved |

### When to Use
- Ground state preparation for quantum algorithms
- Sample-based quantum algorithms (Krylov diagonalization)
- Imaginary + real time evolution pipelines
- NISQ-era state preparation where qubit budget is tight

## Pattern 13: QUBO-Encoded RL Policy Search for Process Synthesis

Quantum-enhanced reinforcement learning for sequential decision problems with large discrete action spaces (arXiv: 2605.21213).

### Core Idea
Encode RL policy decisions as binary variables and map policy optimization to QUBO, solved by quantum annealer or quantum-inspired solver.

### Workflow
```
Process Problem → RL State/Action Design → QUBO Formulation → 
Quantum Annealer Solver → Decode Solution → Validate Process Design
```

### QUBO Formulation
`min x^T Q x + c^T x` where x ∈ {0,1}^n, Q encodes process constraints + economic objectives + safety bounds + RL reward

### Key Advantages
- Exponential reduction in search space exploration
- Better global optima vs classical RL alone
- Handles combinatorial complexity of process flowsheet design

### When to Use
- Chemical process design and optimization
- Plant flowsheet synthesis
- Industrial process optimization with large discrete decision spaces
- Any sequential decision problem with combinatorial action space

### Relationship to QUACOD (Pattern 9)
This paper encodes RL policy directly as QUBO for quantum annealing; QUACOD decomposes large QUBOs into quantum-solvable subproblems. For problems exceeding qubit count, combine both approaches.

### Activation
- quantum process synthesis, QUBO RL, quantum annealing optimization
- quantum reinforcement learning, chemical process optimization
- sequential decision quantum, RL combinatorial optimization

See [references/quantum-rl-process-synthesis.md](references/quantum-rl-process-synthesis.md) for full paper analysis.

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
- See [references/effective-rank-encoding.md](references/effective-rank-encoding.md) for effective rank encoding predictor implementation
- See [references/quantum-kernel-diagnostics.md](references/quantum-kernel-diagnostics.md) for Hamming kernel + spectral entropy diagnostic details (2026-06-02)
- See [references/session-2026-05-16.md](references/session-2026-05-16.md) for QUACOD details and arXiv API access patterns
- See [references/quantum-rl-process-synthesis.md](references/quantum-rl-process-synthesis.md) for QUBO-encoded RL policy search (arXiv: 2605.21213)
- See [references/quantum-simulation-vs-learning.md](references/quantum-simulation-vs-learning.md) for empirical comparison framework: simulability ≠ learnability (arXiv: 2605.28986)

## Pattern 14: Quantum Simulation vs Sample-Based Learning Comparison

Empirical framework comparing two classical approaches to reproducing Born-rule statistics for quantum systems (arXiv:2605.28986).

### Core Insight
**Simulability ≠ Learnability**: Systems that are hard to simulate from classical descriptions may still be efficiently learnable from measurement samples, and vice versa.

### Complexity Classes
| Class | Simulation | Learning | Example |
|-------|-----------|----------|---------|
| Easy-Easy | Efficient | Efficient | Clifford circuits |
| Hard-Easy | Intractable | Efficient | Some random circuits |
| Easy-Hard | Efficient | Intractable | Structured systems |
| Hard-Hard | Intractable | Intractable | Generic quantum systems |

### When to Use This Framework
- Verifying quantum advantage claims (simulation hardness alone is insufficient)
- Choosing between simulation-based training vs sample-based training for quantum ML
- Characterizing unknown quantum systems

### Methodology
1. Define system class and complexity parameters (circuit depth, qubit count, noise)
2. Run classical simulation (exact or approximate) — record time/memory scaling
3. Run sample-based learning from measurement data — record sample complexity
4. Compare: accuracy, computational cost, scaling behavior

### Key Finding
For some random circuit ensembles, learning from O(poly(n)) samples succeeds where classical simulation requires exponential resources. This means quantum advantage claims based solely on simulation hardness need additional evidence.

### Activation
- quantum simulation vs learning comparison
- simulability learnability gap
- Born-rule statistics benchmark
- quantum advantage verification methodology

See [references/quantum-simulation-vs-learning.md](references/quantum-simulation-vs-learning.md) for detailed experimental setup, metrics, and related work.
