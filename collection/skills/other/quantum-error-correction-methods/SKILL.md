---
name: quantum-error-correction-methods
description: "Reusable patterns from quantum error correction research. Covers RL-controlled QEC, fault-tolerant architectures, neutral-atom systems, Bacon-Shor codes, and loss-biased codes. Use when analyzing QEC papers, designing fault-tolerant quantum systems, selecting error correction codes, or comparing QEC approaches."
---

# Quantum Error Correction Methods

## Related Skills
- [[permutation-invariant-qec-recovery]] — QER for permutation-invariant codes under correlated amplitude-damping noise; CAD code family (arXiv: 2607.02346)
- [[spatially-coupled-quantum-codes]] — Spatially coupled CSS codes achieving quantum erasure hashing bound via seeded BP (arXiv: 2606.32001)
- [[real-time-qec-system-stack]] — Six-layer real-time QEC system architecture, decoder benchmarking, and latency budgets (arXiv: 2605.30765)
- [[symmetry-protected-quantum-metamaterials]] — Symmetry-protected qubit architecture (arXiv: 2606.00254)
- `tensor-network-readout-error-mitigation` — MPO-based correlated readout error characterization and mitigation (arXiv: 2606.25974)
- `pauli-propagation-error-mitigation` — Hybrid Pauli propagation + quantum noise cancellation for observable estimation (arXiv: 2606.20441)
- `adaptive-syndrome-skipping-surface-gkp` — Syndrome adaptive gain control for surface and GKP codes (arXiv: 2606.24469)
- `monitored-clifford-purification` — Universal purification dynamics of monitored Clifford circuits reducing to exactly solvable Markovian death process, bypassing replica trick (arXiv: 2607.06683)

## Core Patterns

## Pattern 1: RL-Controlled Quantum Error Correction

**Core idea**: Use reinforcement learning to adaptively control QEC instead of halting computation for recalibration.

**Problem**: Environmental drift degrades quantum operations over time. Traditional approach: stop computation, recalibrate, resume — unsustainable for long algorithms.

**RL solution**:
- State: Syndrome measurements, drift indicators
- Action: Adjust error correction parameters
- Reward: Logical error rate reduction
- Continuous online adaptation without interrupting computation

**Key paper**: "Reinforcement Learning Control of Quantum Error Correction" (arxiv:2511.08493)

## Pattern 2: Neutral-Atom Fault-Tolerant Architecture

**Core idea**: Reconfigurable neutral-atom arrays for scalable fault-tolerant quantum computing.

**Key results (Harvard, 2025)**:
- 448 neutral atoms in reconfigurable array
- Integrated all core elements of scalable error-corrected computation
- Repeatable error correction with present-day technology
- Roadmap: high-fidelity gates + scalable atom control + robust decoding

**Architecture pattern**:
1. Physical qubits in 2D atom array
2. Logical qubits via surface code or similar
3. Reconfigurable connectivity for gate operations
4. Real-time syndrome extraction

## Pattern 3: Measurement-Free Fault-Tolerant Computation

**Core idea**: Fault-tolerant quantum computation without mid-circuit measurements.

**Method**: Bacon-Shor code + code deformation
- All logical operations via unitary gates + resets only
- No mid-circuit measurements needed
- No classical decoding during computation
- Reduces hardware requirements significantly

## Pattern 4: Loss-Biased Quantum Error Correction

**Core idea**: Exploit biased noise channels (loss dominates over other errors) for more efficient QEC.

**Key insight**: Physical error channels are often biased (e.g., photon loss >> dephasing). Design codes that protect against dominant error type more efficiently.

**Applications**: Superconducting qubits, photonic quantum computing, bosonic codes (GKP).

## Pattern 5: Concatenated Code Decoding

**Core idea**: Bidirectional decoding for concatenated quantum Hamming codes.

**Results** (SpinQ + HKUST, QEC 2026):
- Near-optimal effective distance
- More efficient fault-tolerant threshold
- Suitable for near-term quantum processors

## Pattern 6: Adaptive Window Decoding (ADaPT)

**Core idea**: Use decoder confidence to dynamically adjust window size in real-time QEC decoding, reducing reaction time without compromising logical error rates.

**Problem**: Fixed window size `d` in window decoding pays unnecessary overhead per window due to sparsity of average-case errors in QEC.

**Solution** (arxiv:2605.01149, 2026-05-05):
- Monitor decoder confidence during window processing
- Shrink window when confidence is high (sparse errors)
- Expand window only when needed (dense error clusters)
- Achieves target error rate with lower decoding time overhead
- Benchmarked across different codes and hardware-inspired noise models
- Maintains low reaction time while preserving logical error rate performance

**Key insight**: Average-case QEC errors are sparse — most windows don't need full-size processing.

## Pattern 7: FPGA-Based QLDPC Decoding with GARI

**Core idea**: Hardware architecture for correlated error decoding in quantum LDPC codes using Graph Augmentation and Rewiring for Inference (GARI) method.

**Architecture** (arxiv:2605.01035, 2026-05-05):
- Message-passing decoder exploiting detector error model structure from GARI
- Resource reuse with modest parallelism for reduced power/area
- Case study: VCU19P FPGA, 3 decoder cores for [[144,12,12]] bivariate bicycle code
- Average latency: 596 ns per decoding round
- 6x fewer resources than previous GARI-based proposal
- First multi-core decoder implementation for correlated errors on single FPGA

**Design principles**:
- Flexible scaling to any QLDPC code using GARI framework
- Energy-conscious scaling for QEC classical layer
- Real-time decoding constraints met without accuracy compromise

## Pattern 8: Quasi-Dyadic CSS LDPC Code Construction

**Core idea**: Build dual-containing CSS LDPC codes using quasi-dyadic (circulant block) matrices for efficient encoding/decoding and fault tolerance.

**Construction** (arxiv:2605.03631, 2026-05-05):
- Use quasi-dyadic matrices: sparse circulant blocks that commute
- Dual-containing property: H_x · H_z^T = 0 (needed for CSS codes)
- Enables compact representation and efficient algebraic decoding
- Applicable to scalable fault-tolerant quantum computation

**Key advantage**: Circulant structure enables hardware-friendly implementation with reduced memory and computation overhead.

## Pattern 9: Fault-Tolerant Cut-Cat Syndrome Extraction

**Core idea**: Novel syndrome extraction protocol using cut-cat states that prevents error propagation during QEC measurement cycles.

**Method** (arxiv:2604.17339, 2026-04-19):
- Prepare ancillary "cut-cat" states (truncated cat states)
- Use transversal CNOT gates between data qubits and ancilla
- Verify syndrome measurement before applying corrections
- Prevents single physical error from cascading into logical failure

**Benefit**: Reduces syndrome extraction circuit depth and connectivity requirements compared to standard Steane/Shor extraction.

## Pattern 10: Compass Code Dynamic Low-Valency QEC

**Core idea**: Dynamic compass codes with low valency (few connections per qubit) enable scalable QEC on hardware with limited connectivity.

**Method** (arxiv:2604.14299, 2026-04-15):
- Low-valency code structure: each qubit connects to few neighbors
- Dynamic code deformation for adaptivity
- Rapid logical error rate reduction with code scaling
- Practical for near-term hardware with connectivity constraints

## Pattern 11: QEC Decoder Analysis Framework

**Core idea**: Systematic analysis framework for comparing QEC decoders across multiple dimensions.

**Analysis dimensions** (arxiv:2603.20127, 2026-03-20):
- **Belief propagation convergence**: Speed and stability of iterative message passing
- **Trapping set analysis**: Short cycles in Tanner graph that cause decoder failure
- **OSD post-processing**: Ordered statistics decoding to escape local minima
- **Computational complexity**: Classical processing overhead per syndrome round

## Pattern 12: Maximum Likelihood Decoding (MLD) via Three Complementary Lenses

**Core idea**: MLD is provably optimal for QEC but #P-hard in general. Three approaches approximate or solve it:

1. **Statistical Mechanics** (arxiv:2605.17230): Maps MLD to partition functions of disordered spin models. For CSS codes: MLD ↔ partition function of classical spin model with quenched disorder. Each qubit → spin variable; syndrome → random magnetic field; error probability → Boltzmann weight. Decoding threshold = thermodynamic phase transition on Nishimori line: exp(-2βJ) = p/(1-p). Exact MLD via tensor network contraction of the spin model; approximate MLD via belief propagation with guaranteed convergence for tree-like factor graphs. Code geometry determines: computational complexity (low treewidth → exact TN tractable), BP convergence (locally tree-like → converges), optimal contraction order. Below threshold = ordered phase (successful decoding); at threshold = critical point; above threshold = disordered phase (decoding failure). See `references/statistical-physics-qec-decoding.md` for detailed spin model construction and implementation patterns.

2. **Tensor Networks**: Build factor graph from parity check matrix H, contract tensor network to compute marginals. Complexity O(χ^d) where χ is bond dimension. Near-MLD accuracy with polynomial cost.
3. **AI/Neural Decoders**: Autoregressive generative models and recurrent transformers learn P(error|syndrome) from data. Fast real-time decoding on GPU/TPU, accuracy depends on training data quality.

**Integration pattern**: Statistical mechanics for exact threshold estimation (small codes), tensor networks for near-optimal accuracy (moderate distances), neural decoders for real-time throughput (large codes).

**Key paper**: "Maximum Likelihood Decoding of Quantum Error Correction Codes" (arxiv:2605.17230, 2026-05)

## Pattern 13: VarEFTQC — Learning-Based Logical Operation Discovery for Arbitrary QEC Codes

**Core idea**: Given only an encoding circuit (no stabilizer description required), use learning-based optimization to discover physical implementations of logical operations while enforcing structural constraints (transversality, shallow depth). Extended to **VarEFTQC** co-design: jointly optimizes non-additive encodings with noise-adapted logical gate sets.

**Problem**: Discovering logical operations for quantum error-correcting codes is challenging, especially for non-additive codes that lack a stabilizer description. Analytical methods only work for well-studied codes.

**Solution** (arxiv:2605.28162, 2026-05):
1. **Input**: Only the encoding circuit is needed — no stabilizer tableau
2. **Ansatz construction**: Parameterized gate sequences for candidate logical operations
3. **Loss function**: Combines fidelity (correct logical action) with structural constraints (transversality, depth)
4. **Optimization**: Gradient-based or gradient-free methods for non-convex landscapes
5. **VarEFTQC co-design**: Jointly optimizes encoding + logical ops for specific noise models
   - Tailors non-additive encodings to noise characteristics
   - Enforces desired logical gate sets (transversal IQP families, low-depth universal sets)

**Validation**: Rediscover known logical operations on standard stabilizer codes, then extend to non-additive codes.

**When to use**:
- Non-additive codes where analytical methods fail
- Hardware-adapted logical gadget discovery
- Code-device co-optimization for specific noise models
- Exploring codes beyond the stabilizer formalism

**Pitfalls**:
- Non-convex optimization landscape with many local minima — requires careful initialization
- Circuit size scales with code size — may need hierarchical approaches
- Results depend on accurate noise model characterization
- Full simulation verification required

**Key paper**: "Learning Logical Operations for Arbitrary Quantum Error Correction Codes" (arxiv:2605.28162, 2026-05)

## Pattern 15: qLDPC Breakeven on Trapped-Ion with OMG Architecture

**Core idea**: High-rate qLDPC codes achieve breakeven on trapped-ion hardware using optical-metastable-ground (OMG) architecture for addressable mid-circuit measurement and reset.

**Problem**: qLDPC codes require non-local connectivity — surface codes dominate planar architectures. Trapped-ion all-to-all connectivity makes them ideal for qLDPC but mid-circuit measurement traditionally requires ion transport or coolant ions, consuming significant runtime/ion count.

**OMG Architecture** (arxiv:2606.06455, 2026-06):
1. Prepare data + ancilla qubits in ion chain
2. Apply syndrome extraction gates (entangling)
3. Pump ancilla to metastable state (optical transition)
4. Read metastable state via fluorescence detection
5. Reset ancilla via optical pumping to ground state
6. **No ion transport or coolant ions needed**

**Results**:
- [[18,4]] qLDPC code: 9× better logical error rate than previous superconducting demonstration
- **Breakeven achieved**: logical qubit lifetime ≥ physical qubit lifetime
- Tested **9 QECC families** (qLDPC, topological, concatenated) on single device without reconfiguration
- Demonstrates trapped-ion flexibility advantage for QEC code comparison

**When to use**:
- qLDPC code design on flexible-connectivity platforms
- Mid-circuit measurement without hardware overhead
- Multi-code QEC family benchmarking
- Logical qubit breakeven evaluation

**Key metrics**:
- Logical error rate vs physical error rate (breakeven = logical ≤ physical)
- Syndrome extraction cycle time vs coherence time
- Error suppression factor (target: >10× improvement per code generation)

**Pitfalls**:
- **Connectivity mismatch**: qLDPC requires non-local stabilizers; superconducting platforms need SWAP overhead
- **OMG readout fidelity**: Directly impacts syndrome extraction quality
- **Decoding latency**: Must complete within coherence time
- **Code distance trade-off**: Higher-rate qLDPC has lower distance than surface codes of similar size

## Pattern 14: Hybrid Stabilizer-Tensor Network for Non-Clifford Crosstalk

**Core idea**: Simulate surface code QEC under **coherent crosstalk noise** by decomposing noise into Clifford + non-Clifford components, using stabilizer formalism for the Clifford part and matrix product states (MPS) for the non-Clifford corrections.

**Problem**: Surface code QEC simulation assumes Pauli/incoherent noise. Real devices have **coherent crosstalk** (ZZ, XZ, YZ couplings between neighbors) that breaks Gottesman-Knill stabilizer simulation.

**Method** (arxiv:2605.29514, 2026-05):
1. **Decompose** crosstalk noise into Clifford + non-Clifford components
2. **Stabilizer layer**: efficient tableau simulation of Clifford operations
3. **Tensor network layer**: MPS representation of non-Clifford noise as low-rank corrections
4. **Iterate**: alternate stabilizer evolution and TN corrections per QEC round

**Crosstalk Hamiltonian**: H = J_zz Z_iZ_j + J_xz X_iZ_j + J_yz Y_iZ_j (depends on qubit layout and pulse shapes)

**TN compression**:
- Adaptive bond dimension based on entanglement entropy
- Exploit locality: crosstalk limited to nearest-neighbor qubits
- Truncate small Schmidt values (tolerance ~1e-8)

**When to use**:
- Surface code threshold estimation under realistic coherent noise
- Hardware-aware QEC design (pulse sequence optimization)
- Benchmarking beyond Pauli noise assumptions

**Pitfalls**:
- **Bond dimension explosion**: non-Clifford noise creates entanglement → bond dim grows exponentially with rounds. Mitigation: truncate aggressively, use local MPS patches.
- **Clifford approximation error**: ignoring small non-Clifford components underestimates logical error rate.
- **Measurement noise**: framework assumes noise-free syndrome measurements; needs separate treatment for measurement errors.

## Pattern 16: Iterative Low-Order Decoding (ILOD) via Ising Hamiltonian

**Core idea**: Map QEC decoding to classical Ising Hamiltonian ground-state optimization, then decompose the joint Hamiltonian into alternating X-type and Z-type sub-Hamiltonians with Bayesian priors to approximate cross-correlations. This halves the maximum interaction order per sub-problem.

**Problem**: Under phenomenological depolarizing noise, exact joint QEC decoding contains:
- **Toric code**: up to 8-body interaction terms
- **6.6.6 color code**: up to 10-body interaction terms
- X-Z error correlations appear as cross terms in the Hamiltonian

High-order terms cause: solver convergence degradation at larger code distances, inflated runtime, large auxiliary spin overhead when embedding into native 2-body Ising hardware.

**ILOD Algorithm** (arxiv:2606.12301, 2026-06-10):
1. **Decompose** joint Hamiltonian into X-type and Z-type sub-Hamiltonians
2. **Initialize** uniform priors P_X = P_Z
3. **Alternate optimization**:
   - Solve argmin H_X(error_X | P_Z) — X-errors conditioned on Z-prior
   - Update P_X via Bayesian inference from inferred error_X
   - Solve argmin H_Z(error_Z | P_X) — Z-errors conditioned on X-prior
   - Update P_Z via Bayesian inference from inferred error_Z
4. **Converge** when |error - prev_error| < threshold

**Performance**:
- Toric code threshold: 4.73% (vs 4.83% joint formulation — minimal loss)
- Runtime scaling: (0.81)^d empirical ratio vs joint formulation
- Spin reduction: 2.5x fewer spins for 2-body hardware embedding
- **Color code advantage**: ILOD remains convergent at larger code distances where joint formulation fails entirely

**When to use**:
- Hardware embedding on 2-body Ising solvers (D-Wave, simulated annealing)
- Color code decoding at large distances (joint formulation infeasible)
- Any QEC decoder where X-Z cross-correlations dominate Hamiltonian complexity

**Pitfalls**:
- **Near-threshold degradation**: Performance drops ~0.1% below joint at threshold — increase code distance rather than decoder complexity
- **Convergence failure**: Increase iterations, check syndrome consistency, fall back to MWPM for toric codes
- **Bayesian coupling strength (λ)**: Controls influence of cross-priors; too high causes oscillation, too low loses correlation benefit

## Pattern 17: GSC-QEMit — Adaptive Telemetry-Driven Quantum Error Mitigation

**Core idea**: Use a context-forecast-bandit framework to dynamically switch between QEM strategies (lightweight → heavy) as hardware noise drifts, optimizing the mitigation-quality vs runtime-overhead tradeoff.

**Problem**: QEM deployments must balance mitigation strength against computational cost under time-varying noise. Static QEM pipelines either over-mitigate (wasting runtime) or under-mitigate (poor results).

**Solution** (arxiv:2604.24551, 2026-04):

GSC-QEMit composes three coupled modules:

1. **(G) Growing Hierarchical Context**: Builds multi-scale noise telemetry representations
   - Organizes device calibration data (T1, T2, gate fidelities, readout errors) into hierarchical time windows
   - Shorter windows for fast-changing parameters, longer for slow drift
   - Cross-correlates noise across qubits to identify shared noise sources

2. **(S) State Forecast**: Time-series prediction of future noise states
   - Anticipates noise regime transitions (calibration changes, drift events)
   - Provides lookahead for proactive (not reactive) mitigation selection
   - Generates confidence intervals for forecast uncertainty

3. **(C) Contextual Bandit Controller**: Multi-armed bandit for mitigation strategy selection
   - Maps forecast noise state + context to bandit context vector
   - Balances exploration vs exploitation in strategy selection
   - Selects from spectrum: ZNE (light) → PEC (medium) → full QEM suite (heavy)
   - Approaches oracle performance that knows noise in advance

**When to use**:
- VQA and other iterative quantum algorithms (per-iteration mitigation adjustment)
- Long-running quantum workloads where noise drifts significantly
- NISQ devices with available telemetry data
- Scenarios where QEM overhead is a significant fraction of total runtime

**Implementation pattern**:
1. Collect telemetry → build hierarchical context
2. Forecast noise state with confidence bounds
3. Select mitigation strategy via contextual bandit (Thompson sampling or UCB)
4. Execute circuit, record outcome, update bandit rewards
5. Iterate: continuously update context and refine forecasts

**Pitfalls**:
- **No telemetry available**: Fall back to static mitigation or worst-case assumptions
- **Bandit not converging**: Increase exploration rate, reset if noise regime fundamentally changed
- **Forecast inaccurate**: Reduce forecast horizon, increase context uncertainty, bias toward heavier mitigation
- **Overhead exceeds benefit**: For very short circuits, static QEM may be more efficient

**Key paper**: "GSC-QEMit: A Telemetry-Driven Hierarchical Forecast-and-Bandit Framework for Adaptive Quantum Error Mitigation" (arxiv:2604.24551, 2026-04)

## Pattern 19: Quantum Error Recovery (QER) for Permutation-Invariant Codes

**Core idea**: Use channel-aware quantum error recovery maps on permutation-invariant (PI) codes to achieve fidelity beyond noise-parameter-independent QEC.

**Problem**: Stabilizer codes apply fixed correction regardless of noise strength. For correlated non-Pauli noise (e.g., amplitude damping), this wastes resources. PI codes are symmetric under qubit permutations, have tunable parameters, and require simpler recovery circuits.

**QER vs QEC**:
- **QEC**: Fixed correction, noise-parameter independent
- **QER**: Optimal recovery map computed from channel knowledge, exceeds QEC fidelity

**CAD Codes** (arxiv:2607.02346, 2026-07):
- New PI code family for global symmetric amplitude-damping errors
- **CAD4**: 4-qubit code, perfectly corrects 1 global symmetric AD error, recovery circuit = 10 system/ancilla gates (realizable from linear geometric phase gates)
- **CAD9**: 9-qubit code, outperforms many existing codes by >1 order of magnitude
- Direct path from optimized recovery maps → low-overhead implementable protocols

**When to use**:
- Correlated amplitude-damping noise dominant
- Hardware with limited addressability (PI codes need fewer targeted operations)
- Non-Pauli noise where stabilizer overhead is prohibitive

**Pitfalls**:
- QER requires accurate noise channel estimation — performance degrades with poor channel knowledge
- Recovery map computation scales with code size — use approximate recovery for large codes
- PI codes may have lower code distance than optimal stabilizer codes for the same qubit count

## Pattern 20: Spatially Coupled CSS Codes with Seeded BP Decoding

**Core idea**: Spatial coupling of CSS codes enables belief-propagation (BP) decoding to achieve the quantum erasure hashing bound — a threshold normally only reachable with optimal (MAP) decoding.

**Problem**: BP is a suboptimal decoder compared to MAP. For quantum erasure channels, achieving the hashing bound (R = 1 - 2p) typically requires MAP decoding.

**Solution** (arxiv:2606.32001, 2026-06):
1. **CSS ensemble**: MN/HA-type punctured sparse matrices for X and Z checks
2. **Spatial coupling**: Couple multiple code instances along a chain
3. **Seeded BP**: Initialize with known qubits at chain boundaries
4. **DE analysis**: Five-message density evolution recursion decomposed into Z-side and X-side constituents
5. **Coupled-vector potential method**: Proves BP threshold = MAP threshold = hashing bound for equal-rate case

**Key mathematical result**: For X/Z equal-rate family, BP threshold = hashing-bound channel parameter determined by design rate. For unequal rates: BP threshold = min(Z-side degree ratio, X-side complementary degree ratio).

**When to use**:
- Quantum erasure channel QEC design
- Need low-complexity BP decoder with near-optimal performance
- CSS code construction with spatial coupling

**Pitfalls**:
- **Finite-length effects**: DE assumes infinite block length; finite codes need BP concentration analysis and block-error convergence study
- **Unequal X/Z rates**: Hashing bound not achieved; threshold limited by min of constituent ratios
- **Seed realization**: Finite-code realization of ideal DE seed is a separate engineering challenge

## Pattern 18: Quantum Group Codes from Class Field Theory for Non-Clifford Logic

**Core idea**: Construct quantum CSS codes from classical quasi group codes lifted via class field theory, supporting transversal multi-control-Z gates that are both addressable and parallelizable — enabling efficient non-Clifford gate implementation with quasi-quadratic decoding.

**Problem**: Non-Clifford gates require magic-state distillation, which dominates resource overhead in fault-tolerant quantum computing. Existing quantum AG codes support transversal gates but have cubic-time decoding.

**Solution** (arxiv:2606.27211, 2026-06):

1. **Classical quasi group codes**: Codes over F_q where product is associative up to invertible normalized cocycle
2. **Lifting via class field theory**: Apply ray class field construction to underlying classical AG code
3. **Result**: Quantum group code over F_{q^2} supporting transversal C^mZ and parallelizable C^{m-1}Z gates
4. **Decoding**: Quasi-quadratic time decoder with linear decoding radius (vs O(n^3) for previous quantum AG codes)

**Mathematical bridge**: Class field theory (deep algebraic number theory) → quantum CSS code construction
- Ray class fields provide the lifting structure
- Stark units may enter SIC overlaps (related to arxiv:2606.23535)
- Maximal rings of integers attached to ray class fields determine code parameters

**When to use**:
- Non-Clifford gate implementation without costly magic-state distillation per gate
- Parallelizable multi-control-Z gates in quantum circuit design
- Reducing magic-state distillation protocol overhead (almost linear speedup)
- Connecting number-theoretic code construction to fault-tolerant quantum computing

**Key advantage**: Quasi-quadratic decoding complexity O(n^2 log^c n) vs O(n^3) for previous quantum AG codes, plus parallelizable C^{m-1}Z gates reduce circuit depth.

**Pitfalls**:
- Requires understanding of class field theory and algebraic geometry codes
- Code parameters depend on ray class field properties — not all base codes admit good liftings
- Verification of transversality requires checking class field theory lifting conditions

## Code Selection Guide

| Platform | Recommended Code | Key Advantage |
|---|---|---|
| Neutral atoms | Surface code variants | Reconfigurable connectivity |
| Superconducting | Bacon-Shor, loss-biased | Measurement-free ops possible |
| Photonic | GKP, loss-biased | Natural loss bias exploitation |
| Trapped ions | qLDPC (OMG architecture) | Breakeven achieved, 9× better than superconducting qLDPC |
| NISQ general | RL-controlled adaptive | No recalibration needed |
| QLDPC (real-time) | GARI message-passing | FPGA-decodable, correlated errors |
| Non-Clifford logic | Quantum group codes (class field theory) | Quasi-quadratic decoding, parallelizable C^mZ gates |
| Correlated amplitude damping | Permutation-invariant QER (CAD codes) | Channel-aware recovery, 10-gate CAD4, >10x CAD9 improvement |
| Erasure channel (CSS) | Spatially coupled MN/HA CSS codes | Seeded BP achieves hashing bound, coupled-vector potential proof |
| Surface code (FTQC) | ADaPT adaptive window | Low latency, confidence-based |
| Toric/Color code (Ising hardware) | ILOD iterative low-order | 2.5x spin reduction, (0.81)^d scaling |
| Threshold estimation | Statistical mechanics mapping | Exact via phase transition, Nishimori line |
| Moderate-distance codes | Tensor network contraction | Near-MLD, O(χ^d) complexity |
| Large-scale real-time | Neural network decoders | GPU/TPU parallel, fast inference |

## Key Metrics to Track

- **Logical error rate**: Target < 10^-6 for practical computation
- **Code distance**: d = 3, 5, 7... (higher = more protection, more overhead)
- **Syndrome extraction cycle time**: Must be << qubit coherence time
- **Qubit overhead**: Physical/logical qubit ratio
- **Threshold**: Physical error rate below which logical error decreases with code size
- **Decoding latency**: Target < 1 μs per round for real-time FTQC (ADaPT: adaptive; GARI: 596 ns on FPGA)
- **Decoder resource usage**: FPGA LUT/DSP count, power consumption for hardware decoders

## References

Key papers in knowledge graph (kg.db):
- Entity 177: Google Quantum Echoes (verifiable Q advantage)
- Entity 179: Quantum Computing 2025 Milestones (1000+ qubit)
- New: RL Control of QEC (arxiv:2511.08493)
- New: Harvard 448-Atom FT Milestone (2025-11)
- New: Universal QC via Measurement-Free QEC (APS, 2026)
- New: Loss-biased FT QEC
- New: MLD Three-Lens Framework (arxiv:2605.17230, 2026-05) — spin models + tensor networks + neural decoders
- New: ADaPT Adaptive Window Decoding (arxiv:2605.01149, 2026-05)
- New: FPGA QLDPC GARI Decoder (arxiv:2605.01035, 2026-05)
- New: Trapped-Ion Multiqubit Gates Compatible with Scalable QEC (arxiv:2605.28536, 2026-05)
- New: VarEFTQC Learning-Based Logical Operation Discovery (arxiv:2605.28162, 2026-05) — Pattern 13 above
- New: Non-Clifford Crosstalk via Hybrid Stabilizer-TN (arxiv:2605.29514, 2026-05) — Pattern 14 above
- New: qLDPC Breakeven on Trapped-Ion with OMG Architecture (arxiv:2606.06455, 2026-06) — Pattern 15 above
- New: Iterative Low-Order Decoding (ILOD) via Ising Hamiltonian (arxiv:2606.12301, 2026-06) — Pattern 16 above
- New: GSC-QEMit Adaptive Telemetry-Driven QEM (arxiv:2604.24551, 2026-04) — Pattern 17 above
- New: Quantum Group Codes from Class Field Theory (arxiv:2606.27211, 2026-06) — Pattern 18 above
- New: QER for Permutation-Invariant Codes (arxiv:2607.02346, 2026-07) — Pattern 19 above
- New: Spatially Coupled CSS Codes with Seeded BP (arxiv:2606.32001, 2026-06) — Pattern 20 above
- New: Spacetime Lifting for Low-Overhead QEC (arxiv:2606.06365, 2026-06)

**Support files**:
- `references/gsc-qemit-adaptive-qem.md` — GSC-QEMit architecture details, module breakdown, mitigation strategy spectrum
- `references/statistical-physics-qec-decoding.md` — Statistical mechanics QEC decoding details
- `references/ilod-ising-qec-decoder.md` — ILOD algorithm implementation details

## Pattern 22: Confidence-Gated Two-Stage QEC Decoding

**Core idea**: Treat QEC syndrome decoding as a confidence-gated inference problem — lightweight neural fast-path handles the majority, expensive MWPM refinement only for low-confidence cases.

**Problem**: Real-time decoding is the major bottleneck in scaling QEC. MWPM has O(n³) complexity; pure neural decoders sacrifice accuracy for speed.

**Solution** (arxiv:2607.05814, 2026-07):
1. **Stage 1 (Fast-Path)**: Feed-forward neural network produces correction + confidence score
2. **Stage 2 (Refinement)**: MWPM triggered only when confidence < threshold τ
3. **Results**: At τ=0.95, accuracy 99.21% → 99.81% with only 3.3–6.2% escalation rate
4. **Throughput**: ~4.6×10⁵ samples/s on commodity CPU (batch size 512)
5. **Key insight**: Beyond code distance d=7, neural inference is NOT the throughput bottleneck — the MWPM refinement stage dominates

**Accuracy-Latency Trade-off**:
| τ (threshold) | Accuracy | Escalation Rate | Latency |
|---------------|----------|-----------------|---------|
| 0.00 (neural-only) | 99.21% | 0% | Minimal |
| 0.95 | 99.81% | 3.3-6.2% | Medium |
| 1.00 (MWPM-only) | ~99.9%+ | 100% | High |

**When to use**:
- Latency-constrained real-time QEC decoder design
- Hardware-aware QEC co-design for fault-tolerant systems
- Benchmarking decoder performance across code distances
- Systems engineering for quantum computing reliability

**Pitfalls**:
- Confidence threshold must be calibrated per noise model and code distance
- Neural training data must cover the full syndrome distribution
- Beyond d=7, optimize the MWPM graph stage, not the neural inference

**Key paper**: "Latency-Constrained Hardware-Aware Quantum Error Correction Co-Design with Adaptive Confidence-Gated Neural Decoding" (arxiv:2607.05814, 2026-07)

## Pattern 23: Bosonic QEC with Finite Stellar Rank

**Core idea**: Use stellar rank as an operational resource measure for bosonic QEC under practical state-preparation constraints.

**Problem**: Bosonic QEC relies on non-Gaussian encodings whose preparation cost is a central constraint. Prior work assumed ideal (infinite stellar rank) codewords.

**Solution** (arxiv:2607.06404, 2026-07):
1. **Stellar rank k**: Number of zeros of the stellar function f_ψ(z) = ⟨z*|ψ⟩
2. **Trade-off**: State approximability × energy × logical protection under finite rank
3. **Key finding**: k=2 suffices for break-even under ALL dephasing strengths
4. **Direct optimization**: At fixed stellar rank, discovers noise-adapted code structures
   - Photon loss → grid-like encodings emerge
   - Dephasing → rotation-symmetric encodings emerge
5. **Photon loss**: Required rank increases with loss rate γ

**Stellar rank meaning**:
- k = 0: Gaussian states (free, easy to prepare)
- k ≥ 1: Non-Gaussian states (resource-intensive)

**When to use**:
- Designing bosonic QEC codes for circuit QED or optical systems
- Analyzing non-Gaussian resource requirements for fault tolerance
- Optimizing GKP or cat state preparation under hardware constraints
- Determining minimum stellar rank for break-even

**Pitfalls**:
- Codewords with better ideal properties need NOT be optimal under finite-rank constraints
- Required rank for photon loss protection scales with loss rate — budget accordingly
- Direct optimization at fixed rank > approximating ideal codewords

**Key paper**: "Bosonic quantum error-correcting codes with finite stellar rank" (arxiv:2607.06404, 2026-07)

**Related Skills**:
- `bosonic-gkp-parity-encoding` — GKP code design
- `bosonic-grid-states-qec` — Bosonic grid states for QEC

## Practical Notes

**Quantum Group Codes Reference**: See `references/quantum-group-codes-class-field.md` for class field theory lifting procedure details and SIC overlap connections (arxiv:2606.27211, 2606.23535).

## Session Notes

- See `references/session-2026-05-07-qec.md` for 2026-05-07 paper analysis including CSS LDPC construction, cut-cat syndrome extraction, compass codes, bosonic QEC memory, and decoder analysis framework.
- See `references/session-2026-07-09-qec-decoders.md` for confidence-gated decoding, geometric obstruction metrology, and stellar rank bosonic QEC patterns (2607.05814, 2607.06410, 2607.06404).

**Core idea**: Extend pipe diagram lattice surgery compilation from surface codes to **triangular color codes** on the 6.6.6 lattice, enabling distance-independent spacetime optimization and automated compilation to syndrome extraction circuits.

**Problem**: Pipe diagrams are established for **surface code** lattice surgery compilation, but analogous techniques for **color codes** were unexplored — despite color code advantages: reduced qubit overhead and transversal single-qubit Clifford gates.

**Solution** (arxiv:2607.05501, 2026-07-06):

1. **Pipe diagram representation** for triangular color code on 6.6.6 lattice
2. **ZX-diagram correspondence**: Mapping between color code pipes and ZX-diagrammatic computation
3. **Distance-independent constructions**: Correlation surfaces, stabilizers, syndrome extraction circuits
4. **Compact spacetime embeddings**: Leverage color code geometry for efficient logical computation layouts

**Color Code vs Surface Code Trade-off**:
| Property | Surface Code | Color Code (6.6.6) |
|----------|-------------|-------------------|
| Qubit overhead | Higher | Lower |
| Transversal Cliffords | Limited | Full single-qubit set |
| Lattice surgery framework | Established (pipe diagrams) | **This paper** |

**When to use**:
- FTQC architecture using color codes (lower overhead than surface code)
- Need lattice surgery compilation with transversal Clifford advantage
- Spacetime optimization for logical color code computations

**Pitfalls**:
- **Surface code pipe diagrams ≠ color code pipe diagrams**: Different lattice geometry (triangular 6.6.6 vs square) requires different constructions
- **Related skill**: `color-code-pipe-diagrams` (2607.05501) covers the methodology in detail

## Practical Notes

**Quantum Group Codes Reference**: See `references/quantum-group-codes-class-field.md` for class field theory lifting procedure details and SIC overlap connections (arxiv:2606.27211, 2606.23535).

**arXiv API rate limiting**: arXiv returns HTTP 429 (Too Many Requests) when sending queries too quickly. Mitigation: add 3.5s delay between queries (time.sleep(3.5)). Also handle HTTP 421 (Misdirected Request) — may indicate proxy misconfiguration. Use `scripts/arxiv_sunday_search.py` pattern with httpx and proxy support.

## Session Notes

- See `references/session-2026-05-07-qec.md` for 2026-05-07 paper analysis including CSS LDPC construction, cut-cat syndrome extraction, compass codes, bosonic QEC memory, and decoder analysis framework.
