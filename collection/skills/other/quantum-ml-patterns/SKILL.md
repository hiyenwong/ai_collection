---
name: quantum-ml-patterns
description: >
  Reusable patterns for Quantum Machine Learning (QML) research and implementation.
  Covers Variational Quantum Circuits (VQC), Quantum Neural Networks (QNN),
  Quantum Approximate Optimization Algorithm (QAOA), quantum kernels, QUBO-encoded
  RL policy search, and hybrid quantum-classical training. Use when analyzing QML
  papers, designing variational quantum algorithms, implementing quantum-classical
  hybrid systems, or selecting quantum data encoding strategies. Trigger: quantum ML,
  QML, variational quantum, QNN, QAOA, quantum kernel, quantum neural network, VQC,
  quantum-classical hybrid, quantum advantage, QUBO policy search, quantum process
  synthesis, data encoding selection, NISQ encoding, amplitude encoding, angle encoding,
  quantum state preparation, barren plateaus, encoding taxonomy.
---

# Quantum Machine Learning Patterns

## Reference Files
- `references/quantum-hilbert-ml.md` — Quantum Hilbert space prototype learning with MPS, Born rule classification, quantum probability geometry
- `references/quantum-rl-process-synthesis.md` — QUBO-encoded RL policy search for process synthesis (arXiv: 2605.21213)
- `references/fourier-amplitude-embedding-vqc.md` — Fourier analysis of amplitude-embedded VQCs (arXiv:2606.14206): Weingarten calculus, domain sensitivity, noise suppression
- `references/quantum-encoding-selection.md` — QML encoding selection three-axis taxonomy, five-regime framework, NN state preparation (arXiv: 2606.05387, 2605.31006)
- `references/quantum-control-qec-networks.md` — Intervention-aware quantum predictive control (IA-VQC-DPC), SCOPE syndrome-driven routing, GNN-VQE operator selection, neural decoder confidence as logical gap proxy (2026-06-09)

Reusable patterns extracted from recent QML research papers.

## Pattern 1: Variational Quantum Circuit (VQC) Design

VQCs are parameterized quantum circuits optimized by classical algorithms.

### Core Components
1. **Data encoding layer**: Map classical data to quantum states (angle, amplitude, or basis encoding)
2. **Variational ansatz**: Parameterized gates (RY, RZ, CNOT entangling layers)
3. **Measurement layer**: Extract expectation values as output features
4. **Classical optimizer**: Gradient-based (parameter-shift) or gradient-free (COBYLA, SPSA)

### Common Pitfalls (Updated 2026-06-23)
- **Barren plateaus**: Gradient vanishes exponentially with qubit count; use shallow circuits, local cost functions, or structured initializations
- **Expressivity-trainability tradeoff**: More expressive circuits are harder to train (Anschuetz & Gao, 2026)
- **Noise sensitivity**: NISQ devices introduce gate errors; consider error mitigation (ZNE, PEC, DDD)
- **Encoding metric fallacy**: Entanglement capability and Fourier decomposition provide minimal insight into actual encoding performance. Use **effective rank of feature maps** instead — it correlates with QML model performance and can serve as a threshold criterion to prune poor encodings before expensive training (arXiv:2605.18540)
- **⚠️ Measurement-induced logit contraction (arXiv: 2606.22551)**: Pauli measurement outputs are bounded to [-1,1]. When used with cross-entropy loss + softmax for multi-class classification, the loss operates in weak sensitivity regime → gradients suppressed → training instability. **Fix: Quantum Measurement Temperature (QMT)** — add a learnable scaling parameter τ that rescales logits before loss: `rescaled = quantum_logits / τ`. Architecture-agnostic, validated on protein classification and Fashion MNIST. See [references/qmt-measurement-temperature.md](references/qmt-measurement-temperature.md).
- **⚠️ Reference-frame generalization impossibility (arXiv: 2606.22331)**: QML CANNOT generalize to unseen quantum directions without a reference frame. If training states span subspace S ⊂ H, all states orthogonal to S receive the SAME prediction — even when mutually orthogonal. Learning generic unstructured concepts requires exponentially many independently oriented training directions. Feature maps, measurement bases, Hamiltonians, symmetry priors are MANDATORY operational resources, not optional. See [references/qml-generalization-impossibility.md](references/qml-generalization-impossibility.md).

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

- **Importance-Aware QCNN with Ring-Topology**: IA-QCNN for MGMT methylation prediction in glioblastoma — feature importance weighting + ring qubit topology reduces SWAP overhead (arXiv:2604.22877)

- **Importance-Aware QCNN with Ring-Topology**: IA-QCNN for MGMT methylation prediction in glioblastoma — feature importance weighting + ring qubit topology reduces SWAP overhead (arXiv:2604.22877)

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

## Pattern 15: QML Encoding Selection on NISQ Hardware (Updated 2026-06-09)

Comprehensive methodology from arXiv:2606.05387 for selecting optimal quantum data encoding strategies. Survey of 66 primary works (2017-2026).

### Three-Axis Taxonomy
All encoding families classified along: **Cost** (gate depth, qubit count), **Expressivity** (Fourier, feature rank, kernel richness), **Robustness** (noise resilience, barren plateau resistance, kernel concentration).

### Encoding Families Quick Reference
| Encoding | Qubits | Depth | Expressivity | NISQ Viable |
|----------|--------|-------|-------------|-------------|
| Basis | D | O(1) | Low | Yes |
| Angle | n | O(n) | Medium | Yes |
| Dense-Angle | n | O(n) | Medium-High | Yes |
| Amplitude | log₂(D) | O(D) | High | Only if p < 10⁻³ |
| Data Re-uploading | n | O(n×L) | Very High | Limited |
| IQP | n | O(n²) | High | Limited |

### Critical Threshold: p* ~ 10⁻³
**At current NISQ error rates (p ≥ 10⁻³), shallow angle-based encodings consistently outperform amplitude encoding despite the latter's exponential qubit advantage.** This is the single most actionable finding.

### Five-Regime Decision Framework
Map (D, n, p, τ) → encoding:
1. Low-D, High-p → Basis encoding
2. Medium-D, Medium-p → Angle/dense-angle encoding
3. High-D, Low-p (< 10⁻³) → Amplitude encoding
4. Complex features, Any-p → Data re-uploading
5. Hardware-aware → IQP when connectivity permits

### Neural Network State Preparation (arXiv:2605.31006)
Alternative to variational encoding: train classical NN to map input data → quantum circuit parameters directly.
- 0.992 fidelity on unseen MNIST/Fashion-MNIST images
- 5000x runtime reduction per data instance
- All optimization performed once during training phase
- **When to use**: When per-instance state preparation bottleneck dominates QML pipeline

### ⚠️ Updated Pitfalls
- **Amplitude encoding's exponential advantage is nullified** by decoherence at current NISQ error rates — default to angle-based unless p < 10⁻³
- **Fixed embedding ansatz selection** without data geometry analysis leads to suboptimal performance
- **Ignoring the cost-expressivity-robustness triad** results in untrainable circuits
- **Wasserstein distance in input space** provides a priori diagnostic for encoding optimization saturation

See [references/quantum-encoding-selection.md](references/quantum-encoding-selection.md) for complete taxonomy, decision framework, and NN state preparation details (2026-06-09).

## Pattern 16: Forward Gradient Estimation for PQC Training (QUIVER)

Training parameterised quantum circuits is bottlenecked by gradient estimation cost. The parameter-shift rule scales O(P) with parameter count P, dominating shot budgets at scale.

**Forward gradient estimators** (arXiv:2606.09734) use forward-mode automatic differentiation to yield unbiased gradient estimates by averaging random directional derivatives — with **no ancilla qubits or controlled-gate overhead**.

### Unified Framework

The estimator interpolates between established methods:
- K=1, single random direction → **SPSA** (Simultaneous Perturbation)
- K=P, canonical basis directions → **random coordinate descent**
- K=P², full basis coverage → **parameter-shift rule** exactly

### QUIVER Optimiser

Derives **closed-form minimum measurement-cost allocation**:
```
shots_i ∝ |g_i| / σ_i  (more shots to high-signal, low-noise parameters)
```

Computed iteratively — parameters with larger estimated gradients get more measurement budget.

### Implementation

```python
def quantum_forward_gradient(cost_fn, theta, k_samples=10):
    """Forward gradient via random directional derivatives."""
    p = len(theta)
    grad_est = np.zeros(p)
    for _ in range(k_samples):
        v = np.random.choice([-1, 1], size=p)  # Rademacher
        eps = 1e-4
        directional = (cost_fn(theta + eps*v) - cost_fn(theta - eps*v)) / (2*eps)
        grad_est += directional * v
    return grad_est / k_samples
```

### Key Results
- Trains QNNs with **60 qubits and 1770 parameters** on ECG5000/MNIST
- Orders of magnitude more efficient than parameter-shift
- Proven convergence with explicit second-moment expansion

### When to Use
- PQC training with P > 100 parameters where parameter-shift is prohibitive
- NISQ-era QML with limited shot budgets
- QAOA and VQE optimisation where gradient accuracy vs. cost matters
- Start with K ≈ √P as default direction sample count

### Pitfalls
- **Rademacher directions** (±1) give lower variance than Gaussian for most QML objectives
- **ε step size**: Must balance linear approximation vs. shot noise (10⁻⁴ to 10⁻³)
- **Variance estimation**: QUIVER needs running variance estimates; use exponential moving average

### Activation
- forward gradient, directional derivative, PQC training, QUIVER optimiser
- parameter-shift alternative, measurement-frugal quantum, quantum automatic differentiation
- shot budget optimization, SPSA quantum

## Pattern 17: Scalable On-Hardware QNN Training via Butterfly Circuits (2026-06-11)

Training QNNs on real quantum hardware is bottlenecked by gradient estimation: standard parameter-shift requires O(n²) circuit evaluations with trainable parameters.

### Butterfly Circuit Architecture
- Structured, subspace-preserving ansatz with O(n log n) parameters
- Logarithmic circuit depth with commuting structure within each layer
- Enables parallel gradient extraction within layers

### Layer-Wise Training Strategy
- Confine on-hardware optimization to one small layer at a time
- Freeze trained layers before adding next layer
- Add optional fine-tuning phase after full network assembled

### Parallelized Parameter-Shift Rule
- Exploit commuting structure within each Butterfly layer
- Extract all gradients in constant number of circuit executions per layer
- Reduces evaluations from O(n²) to O(log n) per optimization step

### Validation on Real Hardware
- IonQ Forte Enterprise trapped-ion hardware at 16 qubits (training)
- Tensor-network simulation at 32 qubits
- 32-qubit inference executed directly on hardware
- MIMIC-III EHR benchmark: matches/exceeds classical neural baselines

### When to Use
- QNN training on NISQ hardware with 16+ qubits
- Clinical/medical data with optimization instability sensitivity
- Any scenario where standard parameter-shift gradient estimation is the bottleneck

### Pitfalls
- Butterfly architecture restricts expressivity — verify task compatibility
- Layer-wise training may get stuck in local optima — add fine-tuning phase
- Hardware noise still affects results — combine with error mitigation techniques

### Relationship to Pattern 16 (Forward Gradient / QUIVER)
Pattern 17 reduces the number of circuit evaluations architecturally (O(n²) → O(log n)); Pattern 16 reduces the measurement cost per evaluation. They are **complementary**: use Butterfly circuits to reduce circuit count AND QUIVER to optimize shot allocation within each circuit.

See [references/quantum-on-hardware-qnn-training.md](references/quantum-on-hardware-qnn-training.md) for full paper analysis.

## Pattern 18: Non-Unitary QML via Trainable Quantum Channels (2026-06-23)

Traditional QML is constrained to unitary dynamics. This methodology (arXiv:2606.15808, Wen et al.) **reformulates quantum channels as trainable computational primitives** rather than detrimental noise.

### Core Framework
```
ρ_out = Σ_k K_k(θ) U(φ) ρ_in U†(φ) K_k†(θ)
```
where K_k(θ) are trainable Kraus operators and U(φ) are standard unitary variational gates.

### Three Key Innovations
1. **Structured superposition**: Channel-enhanced outputs form superpositions of multiple functional components, each with effective observables whose spectra adaptively modulate during training
2. **Spectral modulation**: Unlike unitary transformations (spectral invariance), channel parameters enable spectral changes — the eigenvalues of effective observables change as channel parameters are optimized
3. **Enriched optimization geometry**: Ensemble-averaged gradients across Kraus branches + additional optimization directions from non-unitary Kraus parameters

### Implementation
- Use trainable amplitude-damping or phase-damping channels as non-unitary layers
- CPTP constraint enforcement: Stinespring dilation, projection after gradient steps, or penalty terms
- Hybrid architecture: [Encoding] → [Unitary Layer] → [Trainable Channel] → [Unitary Layer] → [Measurement]

### When to Use
- Tasks where unitary-only QML shows poor convergence or barren plateaus
- Noisy or energy-dissipative data structures
- NISQ hardware where channels are unavoidable — make them trainable rather than treating as fixed noise

### Empirical Results
- Amplitude-damping and phase-damping channels improve classification accuracy over purely unitary baselines
- Non-unitary degrees of freedom provide escape routes from barren plateaus

See [references/non-unitary-quantum-channels.md](references/non-unitary-quantum-channels.md) for full methodology and PennyLane implementation.

## Pattern 19: Anyonic Quantum Kernels via Fractional Exchange Statistics (2026-06-23)

Methodology from arXiv:2606.16090 (Zhang et al.) that **unifies bosonic, fermionic, and anyonic exchange statistics** within a single quantum kernel learning paradigm. Fractional exchange phases (θ ∈ (0, π)) access feature-space directions inaccessible to purely symmetric or antisymmetric limits.

### Three-Level Analysis Framework
1. **Representation level**: Haar-averaged effective dimension shows D_eff(θ) > max(D_eff^bosonic, D_eff^fermionic) for optimal anyonic θ
2. **Kernel geometry level**: Anyonic Gram matrices show greater separation from distinguishable-particle baseline and reduced label-dependent model complexity
3. **Learning performance level**: Anyonic kernels consistently outperform bosonic/fermionic counterparts with stronger target alignment and more favorable class geometry

### Implementation Pattern
- Design quantum feature maps with tunable exchange statistics parameter θ ∈ [0, π]
- Optimize θ jointly with model parameters or via grid search
- Combine bosonic, fermionic, and anyonic kernels in ensemble for complementary feature-space coverage

### When to Use
- Data with mixed/asymmetric structure where bosonic or fermionic kernels alone are insufficient
- Classification tasks with complex decision boundaries
- Any scenario where feature-space geometry limits classical or standard quantum kernel performance

### Caveat
Current quantum hardware doesn't natively support anyonic statistics — simulate using controlled phase gates or anyon braiding via unitary circuits.

## Pattern 20: Partially-Blind Single-Qubit Classification (PB-SQC) (2026-07-07)

Privacy-preserving delegated quantum ML on untrusted quantum networks. Combines single-qubit classifiers with blind quantum computation.

### Core Concept
- Server **knows**: a classification task is being performed
- Server **does NOT know**: the specific input data or classification outcome
- Data encoded to hide individual samples while preserving classification utility

### Architecture
```
Client data → BQC encoding → SQC circuit (server executes) → Client measures → Result
```

### Key Results (arXiv: 2607.01998)
- Tested on real-world credit card fraud database
- Approaches classical deep-belief network accuracy
- Two-qubit classifier (TQC) enables verification of delegated computation
- Integratable into heterogeneous quantum networks via entanglement swapping

### Scaling Path
SQC proof-of-principle → TQC with verification → multi-qubit quantum classifiers → quantum network service

### Pitfalls
- **Partial vs Full Blindness**: PB-SQC hides data+outcome but not task identity. Full BQC hides everything at higher cost.
- **NISQ fragility**: Single-qubit coherence limits; TQC requires entanglement maintenance.
- **Network latency**: Entanglement swapping adds latency/error to remote classification.

### When to Use
- Quantum-secured ML as network service, privacy-preserving delegated computation, NISQ proof-of-principle experiments

## Pattern 21: Health-Aware HPO for Neural-Network Quantum States (2026-06-30)

Neural-network quantum states (NQS) variational accuracy depends sensitively on architecture-level hyperparameters and optimization schedules. Standard HPO (select lowest-energy run) is unreliable because destructive optimization events can mask good architectures.

**NQS-Agent** (arXiv:2606.30464, Wang et al.) introduces **health-aware HPO** that goes beyond final energy.

### Core Pipeline
```
while not converged:
    energy = compute_energy(params)
    monitor(energy_trajectory)
    if detect_instability(trajectory):
        checkpoint = rollback_to_stable()
        modify_lr_schedule(checkpoint)
        resume_optimization(checkpoint, new_lr)
    if detect_divergence(trajectory):
        abort_candidate()
        record("unstable")
```

### Four-Phase Methodology
1. **Energy Trajectory Monitoring**: Continuously track energy curves, derivatives, variance
2. **Destructive Event Detection**: Identify gradient explosion, oscillation divergence, NaN/Inf
3. **Safe Checkpoint Recovery**: Roll back to stable checkpoints, modify learning-rate schedule, resume
4. **Anomaly-Aware Scoring**: Rank by composite score = α×energy + β×stability − γ×recovery_count

### Key Insight
> The stability and recovery history of an optimization trajectory should be considered when assessing an NQS result. Health-aware HPO provides a reproducible tuning protocol that goes beyond selecting a single lowest-energy calculation.

### When to Use
- NQS architecture search (residual CNN vs aCNN, wide-vs-deep)
- Quantum many-body model tuning (Heisenberg, J1-J2, frustrated systems)
- Any variational quantum calculation where gradient instability masks genuine convergence

### Pitfalls
- **Single-run selection trap**: Lowest-energy run may be a lucky convergence, not genuine. Always use multiple runs per configuration.
- **Checkpoint granularity**: Too-frequent checkpoints waste memory; too-sparse lose too much progress. Checkpoint every 10-50 steps for NQS.
- **Instability threshold calibration**: Energy derivative threshold for "instability" is physics-model-dependent. Calibrate on a known-good configuration first.
- **Parameter count matching**: When comparing architectures, ensure fair comparison by matching parameter counts (wide-and-shallow vs deep-and-narrow).

### Activation
- nqs hyperparameter optimization, health-aware HPO quantum
- neural-network quantum states tuning, quantum many-body variational optimization
- NQS-Agent, energy trajectory monitoring, quantum state optimization agent

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
- See [references/quantum-encoding-selection.md](references/quantum-encoding-selection.md) for encoding selection taxonomy, five-regime framework, and NN state prep (2026-06-09)

- See [references/quantum-on-hardware-qnn-training.md](references/quantum-on-hardware-qnn-training.md) for on-hardware QNN training via Butterfly circuits (arXiv:2606.03517, 2026-06-11)
- See [references/ia-qcn-ring-gliobastoma.md](references/ia-qcn-ring-gliobastoma.md) for IA-QCNN ring-topology architecture for MGMT methylation prediction (arXiv:2604.22877, 2026-06-11)
- See [references/non-unitary-quantum-channels.md](references/non-unitary-quantum-channels.md) for trainable quantum channel QML methodology (arXiv:2606.15808, 2026-06-23)
- See [references/anyon-quantum-kernels.md](references/anyon-quantum-kernels.md) for anyonic quantum kernel methodology via fractional exchange statistics (arXiv:2606.16090, 2026-06-23)
- See [references/quantum-network-authentication.md](references/quantum-network-authentication.md) for quantum network authentication taxonomy (arXiv:2606.30636, 2026-06-30)
- See [references/partially-blind-sqc-quantum-ml.md](references/partially-blind-sqc-quantum-ml.md) for PB-SQC privacy-preserving quantum classification methodology (arXiv:2607.01998, 2026-07-07)

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
