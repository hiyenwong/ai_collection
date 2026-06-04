---
name: quantum-computing-patterns
description: >
  Reusable patterns from quantum computing and quantum machine learning research.
  Covers distributed quantum computing, variational quantum algorithms, QML architectures,
  and quantum advantage verification. Use when analyzing quantum computing papers,
  designing quantum-classical hybrid systems, or researching quantum advantage in ML.
  Triggers: quantum computing, QML, variational quantum algorithm, distributed quantum,
  quantum advantage, quantum circuit routing, NISQ.
---

# Quantum Computing Patterns

## Reference Files
- `references/quantum-number-theory.md` — Number-theoretic quantum algorithms: isogeny graph QUE, golden gates, post-quantum cryptography security bounds

Reusable patterns extracted from arXiv/Nature/Science quantum computing research.

## Pattern 1: Distributed Quantum Computing (DQC)

**Core idea:** Partition quantum computation across multiple NISQ devices.

### Key Techniques
1. **Matrix partitioning** - Split large linear systems Ax=b across quantum nodes
2. **Variational distributed algorithms** - Each node optimizes local parameters
3. **Low-loss interconnects** - Microwave/photonic links between quantum modules

### When to Use
- Problem size exceeds single NISQ device capacity
- Need modular scalability for fault-tolerant QC
- Multi-parameter quantum metrology tasks

## Pattern 2: Quantum Circuit Routing via RL

**Core idea:** Frame qubit routing as reinforcement learning problem.

### Key Techniques
1. **State-dependent networking** - Qubit placement depends on current circuit state
2. **Action-space engineering** - Design RL actions for qubit swap/placement
3. **Cross-module coordination** - Route qubits between DQC modules

### When to Use
- Distributed quantum circuit compilation
- NISQ device with limited qubit connectivity
- Dynamic qubit allocation across modules

## Pattern 3: Quantum-Classical Hybrid Neural Networks

**Core idea:** Combine quantum circuits with classical neural network layers.

### Key Techniques
1. **Quantum feature extraction** - Use quantum circuits as trainable feature maps
2. **Hybrid loss landscapes** - Joint optimization of quantum and classical parameters
3. **Quantum kernel methods** - Train quantum kernels with quantum neural networks

### When to Use
- Small quantum advantage on classical ML tasks
- Quantum-enhanced feature spaces
- Quantum reservoir computing

## Pattern 4: Variational Quantum Algorithms (VQA)

**Core idea:** Parameterized quantum circuits optimized via classical feedback loop.

### Key Techniques
1. **Parameterized ansatz** - Design circuit templates with tunable parameters
2. **Classical optimizer loop** - Use gradient-free optimizers (COBYLA, SPSA)
3. **Error mitigation** - Zero-noise extrapolation, probabilistic error cancellation

### When to Use
- NISQ-era quantum applications
- Quantum chemistry/optimization problems
- Quantum machine learning model training

## Pattern 5: Quantum Advantage Verification

**Core idea:** Demonstrate and verify quantum advantage over classical methods.

### Key Techniques
1. **Verifiable protocols** - Interactive proofs for quantum computations
2. **Blind quantum computing** - Client verifies without revealing computation
3. **Benchmark comparisons** - Compare with best classical algorithms

### When to Use
- Quantum supremacy/advantage claims
- Algorithm comparison studies
- Quantum computing capability assessment

## Pattern 6: Phononic Holonomic Gates with Biased Erasure

**Core idea:** Crystallographic symmetry in mechanical metamaterials generates topological holonomic gates with naturally erasure-biased error channels.

### Key Techniques
1. **Holonomic gate construction** — Berry connection over adiabatic parameter cycles for geometric phase gates
2. **Crystallographic symmetry** — Point group constraints restrict allowed holonomies to discrete gate sets
3. **Erasure-biased QEC** — Phononic qubits exhibit η = p_erasure / p_pauli >> 1, enabling more efficient correction

### When to Use
- Fault-tolerant quantum gate design
- Holonomic quantum computing
- Erasure-biased error correction codes

## Pattern 7: Photonic QNN Algorithmic Advantage

**Core idea:** Gate-based variational QNNs on photonic hardware achieve superior performance with fewer parameters than classical ANNs.

### Key Techniques
1. **Effective dimension analysis** — QNNs have higher capacity per trainable parameter
2. **Gradient-free optimization** — Robust to photon loss and phase-shifter noise
3. **Single-photon encoding** — Probabilistic gates emulate standard circuit model

### Key Result
2-parameter QNN solved XOR task requiring 8+ parameter classical ANN. Validated on 6-qubit photonic processor.

### When to Use
- Photonic quantum machine learning
- Quantum advantage benchmarks
- QNN capacity analysis

## Pattern 8: Hamiltonian Sparsification

**Core idea:** Many quantum Hamiltonians can be reduced to significantly fewer terms while preserving system behavior for all states.

### Key Techniques
1. **Matrix Chernoff bounds** — Operator-valued concentration for Hamiltonian term sampling
2. **Pauli sparsification** — r-local Pauli strings reducible to O(r log n / ε²) terms
3. **Quantum SAT sparsification** — Arbitrary r-local operators of rank ≥ 2^r - 1 sparsifiable

### Key Insight
Quantum systems are often easier to sparsify than their classical counterparts (counterintuitive result from arXiv:2605.02211).

### When to Use
- Quantum simulation circuit depth reduction
- Trotter term optimization
- Streaming algorithms for quantum Max-Cut

## Pattern 9: Equivariant RL for Quantum Circuit Synthesis

**Core idea:** Exploit Clifford group symmetry to design equivariant RL policies for circuit synthesis.

### Key Techniques
1. **Equivariant policy** — π(g·s) = g·π(s) respects group symmetries
2. **Stabilizer tableau states** — Efficient state representation for Clifford circuits
3. **Reduced search space** — Symmetry reduces effective state space by |C_n| factor

### When to Use
- Clifford circuit compilation
- Quantum circuit optimization
- Group-equivariant quantum ML

## Pattern 10: Partial QEC for Quantum Metrology

**Core idea:** Selectively correct dominant noise channels while preserving signal sensitivity, improving sensing beyond standard quantum limit.

### Key Techniques
1. **pQEC condition** — Correct noise L_k while ensuring [C, G] ≠ 0 (signal not corrected away)
2. **Entanglement-enhanced sensing** — GHZ/spin-squeezed probes with periodic pQEC cycles
3. **Precision scaling** — Δω ~ 1/(√N · T · √η) where η is QEC efficiency

### When to Use
- Quantum sensor design
- Noise-resilient metrology
- Heisenberg-limited sensing

## Pattern 11: Distributed Inverse QFT

**Core idea:** Prune remote controlled-phase gates beyond "communication horizon" threshold, reducing distributed iQFT communication from O(P²) to O(P).

### Key Techniques
1. **Communication horizon** — Exploit exponentially decaying controlled-phase significance
2. **Threshold-driven pruning** — Skip inter-node gates below accuracy threshold
3. **Linear entanglement scaling** — Per-node entanglement consumption saturates to constant

### When to Use
- Distributed quantum algorithm compilation
- Multi-QPU quantum network protocols
- Shor's algorithm distribution across nodes

## Key References
- arXiv:2604.01426 - Distributed Variational Quantum Linear Solver
- arXiv:2605.02389 - Action-Space Engineering for Quantum Circuit Routing
- arXiv:2602.00048 - Quantum Circuit-Based Learning Models
- Nature s41467-026-68535-9 - Distributed Multi-Parameter Quantum Metrology
- Science adu6894 - Universal Distributed Blind Quantum Computing
- arXiv:2505.23860 - Quantum Computing and AI: Status and Perspectives
- arXiv:2605.10932 - Phononic Holonomic Gates with Biased Erasure
- arXiv:2605.10801 - Algorithmic Advantage on Gate-Based Photonic QNN
- arXiv:2605.02211 - Many Hamiltonians Are Sparsifiable
- arXiv:2605.10910 - Equivariant RL for Clifford Quantum Circuit Synthesis
- arXiv:2605.08341 - Quantum Metrology via Partial QEC
- arXiv:2605.10710 - Communication-Efficient Distributed Inverse QFT

## Session Research Logs
- See [references/session-2026-05-05.md](references/session-2026-05-05.md) for 2026-05-05 research findings, KG PageRank results, and emerging trend analysis.

## Tools Integration
- **kg_tool**: Import quantum papers, search knowledge graph
- **arxiv-search**: Search for latest quantum computing papers
- **web_search**: Find news and breakthrough announcements

## Verification Steps
1. Check arXiv for latest papers in quant-ph, cs.LG, cs.DC
2. Search knowledge graph for related papers
3. Verify claimed quantum advantage against classical baselines
4. Check if NISQ constraints are realistically addressed
