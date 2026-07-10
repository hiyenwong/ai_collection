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

## Pattern 12: qLDPC Breakeven on Trapped-Ion Platforms

**Core idea:** High-rate qLDPC codes demonstrated on trapped-ion hardware with breakeven performance, leveraging all-to-all connectivity and OMG architecture for efficient mid-circuit measurement.

### Key Techniques
1. **OMG architecture** — Optical-Metastable-Ground state enables addressable mid-circuit measurement and reset without ion transport
2. **All-to-all connectivity** — Trapped-ion naturally supports dense parity checks required by qLDPC codes
3. **No coolant ions** — OMG eliminates need for dedicated coolant ions, saving ion count

### Key Result
4 logical qubits encoded into 18 physical qubits with qLDPC code. Logical error rate 9x better than previous superconducting demonstration. Breakeven achieved (logical lifetime ≥ physical lifetime).

### When to Use
- Fault-tolerant quantum computing architecture design
- qLDPC vs surface code comparison
- Mid-circuit measurement optimization
- Trapped-ion QEC implementation

## Pattern 13: Multiple Quantum Hypothesis Testing with Dimension-Free Bounds

**Core idea:** Dimension-free one-shot bounds for Bayesian discrimination among multiple quantum states, resolving long-standing conjectures about the multiple quantum Chernoff distance.

### Key Techniques
1. **Pairwise error summation** — Upper bound expressed as sum of pairwise errors, independent of Hilbert space dimension
2. **Trace harmonic-mean characterization** — Binary minimum error probability within factor 2 of optimal classical error
3. **Infinite-dimensional extension** — Proves achievability for separable Hilbert spaces

### Key Result
Resolves Audenaert-Mosonyi conjecture (J. Math. Phys. 55, 2014). Removes dimension-dependent prefactor from multiple quantum Chernoff bound. Binary error characterized up to universal constants.

### When to Use
- Quantum state discrimination with M>2 hypotheses
- Quantum communication protocol design
- Quantum channel discrimination
- Quantum metrology and sensing analysis

## Pattern 14: Exponential Entanglement-Assisted Capacity Gains

**Core idea:** Quantum entanglement assistance provides exponential multiplicative capacity advantage in classical multiple access channels with causal CSIT, robust to significant entanglement noise.

### Key Techniques
1. **Causal CSIT + entanglement** — Transmitters adapt encoding using both channel state and shared entanglement
2. **Multiplicative advantage** — Gain factor grows exponentially with number of users K
3. **Noise robustness** — Advantage persists with 30% depolarization per entangled qubit

### Key Result
21x capacity gain for K=5, 88x for K=7 (binary alphabet). Unbounded advantage as state alphabet size grows. Entanglement only needed at transmitters, not receivers.

### When to Use
- Quantum-enhanced communication protocol design
- Multi-user channel capacity analysis
- Quantum network coding
- Evaluating quantum advantage in classical communication

## Pattern 15: Lattice Surgery for Fault-Tolerant Logical Operations

**Core idea:** Merge-and-split surface code patches enable logical two-qubit operations with lower spacetime overhead than CNOT-based approaches, demonstrated experimentally on planar superconducting hardware.

### Key Results (arXiv:2606.06598)
- **Distance-3 surface code** logical qubits on planar superconducting processor
- **Per-cycle error rates**: 0.0365(2) and 0.0282(1) after leakage rejection
- **Logical Bell state**: Deterministic preparation via joint initialization + lattice splitting
- **Logical Deutsch-Jozsa algorithm**: Two-qubit algorithm at logical level
- **Magic-state injection**: Continuous non-Clifford RX(π/4) with fidelity 0.943 (conditioned on no detected errors)

### Lattice Surgery vs CNOT
| Aspect | CNOT-based | Lattice Surgery |
|--------|-----------|-----------------|
| Connectivity | Requires direct coupling | Neighboring patches sufficient |
| Overhead | Higher gate count | Lower spacetime cost |
| Fault tolerance | Code distance maintained | Merge-split operations |

### Logical Gate Set via Lattice Surgery
- **Clifford gates**: Via merge/split lattice surgery operations
- **Non-Clifford gates**: Via magic-state injection + gate teleportation
- **Universal computation**: Clifford + T-gate achieves universality

### Pitfalls
- **Leakage events**: Must be detected and rejected; reduces effective throughput
- **Distance-3 limitation**: Small code distance; larger distances needed for practical advantage
- **Conditional fidelity**: 0.943 fidelity conditioned on no detected errors; unconditioned fidelity lower
- **Planar constraint**: 2D nearest-neighbor connectivity limits parallelism
- **Magic-state overhead**: Non-Clifford gates require expensive magic-state preparation

### When to Use
- Near-term FTQC architecture design
- Logical algorithm execution on surface-code hardware
- Lower-overhead alternative to CNOT-based logical gates

## Pattern 16: Quantum Triangle Cut Sparsification

**Core idea:** Quantum algorithms for triangle listing via heavy-light vertex partition + quantum walks + Grover search achieve sublinear time, enabling efficient construction of ε-triangle cut sparsifiers (ICML 2026, arXiv:2606.06287).

### Triangle Listing Complexity
T_q-list = Õ(min(n^(5/4)·t^(7/12) + n^(7/6)·t^(7/9), m + m^(3/4)·t^(1/2), n^(3/2)·t^(1/2)))

### Key Algorithmic Components
1. **Heavy-Light Partition**: Split vertices by degree (threshold ~ √m)
   - Heavy-heavy triangles: quantum walk on dense induced subgraph
   - Heavy-light triangles: Grover search over edge pairs
   - Light-light triangles: classical enumeration (sparse enough)
2. **Quantum Walk Detection**: Extend Ambainis-style walk on Johnson graph of vertex subsets
3. **Sparsifier Construction**: Õ(n/ε²) edges, matching Ω(n/ε²) lower bound

### Complexity Comparison
| Regime | Classical | Quantum | Speedup |
|--------|-----------|---------|---------|
| Dense (t ~ n³) | O(n³) | O~(n^(23/12)) | ~n^(13/12) |
| Sparse (m ~ n) | O(n^(3/2)) | O~(n^(5/4)) | ~n^(1/4) |
| t ~ n^(3/2) | O(n^(9/4)) | O~(n^(7/4)) | ~n^(1/2) |

### Applications
- Triangle-based spectral clustering and higher-order modularity
- Community detection via triangle density measures
- Triangle-aware GNN pre-processing for large graphs
- PPI network analysis and motif discovery in bioinformatics

### Pitfalls
- **QRAM assumption**: Algorithm assumes efficient quantum RAM access to graph data
- **Cut preservation only**: Preserves triangle counts across cuts, not individual triangles
- **Small ε cost**: Ω(n/ε²) lower bound is tight — small ε requires large sparsifier

### When to Use
- Large-scale graph analysis where triangle structure is important
- Network clustering and community detection
- Graph compression retaining higher-order structural properties

## Pattern 17: Blind Quantum Rare Event Discovery and Sampling

**Core idea:** Quantum algorithm for discovering and sampling events with probability < ε without first learning which events are rare. Achieves O(1/√ε) optimal quantum scaling — quadratic improvement over O(1/ε) classical (arXiv:2606.06316).

### Key Results
- **Blind discovery**: No pre-flagging of rare events needed
- **Optimal scaling**: O(1/√ε) vs O(1/ε) classical
- **Heavy-tailed systems**: Quadratic speedup when tail has nonvanishing total mass
- **Stationary processes**: Polynomial speedup with exponent from entropy-rate structure

### Algorithm Structure
1. Uniform superposition over sample space
2. Amplitude encoding of probability distribution
3. Threshold comparison via quantum phase estimation
4. Grover-like amplification for below-threshold events
5. Measurement to sample rare events

### Applications
- **Financial risk**: Crash scenario discovery without knowing specific triggers
- **AI safety**: Critical error mode identification in complex systems
- **Infrastructure**: Cascading failure prediction in power grids, network outages
- **Scientific discovery**: Rare particle detection, extreme value statistics

### Pitfalls
- **Distribution encoding overhead**: May negate quantum advantage if state prep is expensive
- **Threshold sensitivity**: Performance degrades near threshold boundary
- **Heavy-tail assumption**: Quadratic speedup requires specific tail properties
- **Finite sampling**: Statistical fluctuations may misidentify rare events

### When to Use
- Any scenario requiring rare event identification without prior knowledge
- Heavy-tailed distributions where classical importance sampling is inefficient
- AI safety critical error detection and anomaly discovery

## Pattern 18: Projector Variational Ansatz (PVA)

**Core idea:** VQE ansatz structured like FTQC projector algorithms rather than direct state transitions. Bridges NISQ variational and fault-tolerant paradigms. Converges with shallower circuit depth than ADAPT-VQE (arXiv:2606.07084).

### Key Techniques
1. **Projector-based ansatz** — Instead of unitary evolution U(θ)|ψ₀⟩, constructs operator P(θ) that projects onto target subspace using ancillary qubits to flag good solutions
2. **Parametric flexibility** — One parametrization → equivalent to ISQ-QSP; another → equivalent to ADAPT-VQE circuit structure
3. **Amplitude amplification** — Uses amplitude amplification instead of post-selection for better convergence efficiency

### VQE vs PVA Comparison
| Aspect | Standard VQE | PVA |
|--------|-------------|-----|
| Ansatz | Unitary U(θ) | Projector P(θ) |
| Paradigm | NISQ variational | FTQC-like projector |
| State identification | Energy minimization | Ancilla flagging |
| Circuit depth | Deeper (ADAPT-VQE) | Shallower |

### Key Result
PVA converges with shallower ansatz depth than ADAPT-VQE for equivalent ground state accuracy. First proposal of projector-style variational ansatz.

### When to Use
- VQE problems where ADAPT-VQE circuit depth is a bottleneck
- Ground state search where ancilla-based verification is feasible
- Bridging NISQ and early FTQC algorithm regimes

### Pitfalls
- **Noise sensitivity** — Projector structure may be more noise-sensitive than unitary VQE
- **Parametrization mapping** — Must correctly map to ISQ-QSP or ADAPT-VQE form
- **Ancilla overhead** — Additional qubits required for flagging mechanism

## Pattern 19: Compressed Minimum-Purity Time Evolution (CoMPuTE)

**Core idea:** Simulate late-time quantum many-body dynamics by closing the hierarchy of equations of motion using a minimum-purity principle on reduced local density matrices — avoiding exponential entanglement growth (arXiv:2606.11392).

### Key Techniques
1. **Minimum-purity closure** — Select least biased (max entropy) extension consistent with local reduced density matrices {ρᵢ}: min Tr(ρ²) s.t. Tr_{j≠i}(ρ) = ρᵢ ∀i
2. **Local patch evolution** — Apply local Hamiltonian terms to reduced states, then re-extend
3. **Iterative time stepping** — Repeat for desired simulation duration

### Key Results
- Accurate energy diffusion in 1D mixed-field Ising model
- Works for out-of-equilibrium Floquet dynamics from pure states
- More efficient than local-information time evolution (LITE)

### Pitfalls
- **Integrable systems fail** — XXZ chain at Δ=1 governed by non-local integrals of motion; local reduced density matrix approximation breaks down
- **Initial state sensitivity** — Requires simple initial state for hierarchy closure
- **Higher dimensions** — Extension to 2D+ remains open

### When to Use
- Long-time quantum dynamics simulation where entanglement growth limits MPS/TEBD
- Energy transport studies in 1D quantum spin chains
- Floquet dynamics and prethermalization analysis

## Pattern 20: Ribbon ZX Calculus for Gauge Theory

**Core idea:** Extend ZX calculus (graphical quantum process formalism) to 2D Yang-Mills theory with compact gauge groups via Hopf Frobenius algebraic structure (arXiv:2606.13551).

### Key Techniques
1. **Hopf Frobenius mapping** — Map ZX spiders to Hopf Frobenius algebra of group algebra K[G]
2. **2D TQFT diagrammatics** — Describe gauge theory amplitudes using ZX-style ribbon diagrams
3. **Group algebra structure** — Both Frobenius (multiplication/comultiplication) and Hopf (antipode/inversion) properties

### Applications
- 2D Yang-Mills partition functions and correlation functions
- Topological quantum field theory invariants
- Low-dimensional gravity connections (2D/3D gauge-gravity correspondence)

### Pitfalls
- **Dimensional limitation** — Currently 2D only; 4D extension open
- **Compact group requirement** — Framework assumes compact gauge groups
- **Diagram complexity** — Large diagrams need systematic simplification

### When to Use
- Graphical reasoning about gauge theory amplitudes
- TQFT computation via diagrammatic methods
- Quantum information theory meets quantum field theory

## Session Research Logs
- See [references/session-2026-05-05.md](references/session-2026-05-05.md) for 2026-05-05 research findings, KG PageRank results, and emerging trend analysis.
- See [references/session-2026-06-07.md](references/session-2026-06-07.md) for 2026-06-07 research on qLDPC breakeven, quantum hypothesis testing, and entanglement-assisted capacity.
- See [references/session-2026-06-09.md](references/session-2026-06-09.md) for 2026-06-09 research on lattice surgery, triangle sparsification, rare event sampling, and coherent vs stochastic noise.
- See [references/session-2026-06-14.md](references/session-2026-06-14.md) for 2026-06-14 research on CoMPuTE time evolution, ribbon ZX calculus for gauge theory, and fermion-boson nonlocality comparison.

## Tools Integration
- **kg_tool**: Import quantum papers, search knowledge graph
- **arxiv-search**: Search for latest quantum computing papers
- **web_search**: Find news and breakthrough announcements

## Verification Steps
1. Check arXiv for latest papers in quant-ph, cs.LG, cs.DC
2. Search knowledge graph for related papers
3. Verify claimed quantum advantage against classical baselines
4. Check if NISQ constraints are realistically addressed
