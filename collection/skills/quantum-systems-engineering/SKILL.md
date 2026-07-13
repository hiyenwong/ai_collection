---
name: quantum-systems-engineering
description: "Systems engineering patterns for quantum computing systems. Covers hybrid quantum-classical architecture, distributed quantum computing, robust quantum control, QEC network architectures (SCOPE Pattern 20), network constraint modeling (Pattern 21), QLDPC logical processing (Pattern 14), ML-based QEM (Pattern 15), deterministic cat state generation (Pattern 16), software-based coherent error compensation (Pattern 17), hardware-tailored QEC resource estimation (Pattern 18), QND measurement primitives for biased noise (Pattern 19), thermal state prep, molecular qubit control, bistable qubits, and unauthenticated BFT consensus. Keywords: quantum systems, distributed quantum, quantum control, QLDPC, error mitigation, cat states, NISQ, QEC, coherent error compensation, resource estimation, biased noise, network control, SCOPE"
---

# Quantum Systems Engineering

Systems engineering patterns applied to quantum computing systems, combining distributed computing principles with quantum hardware constraints.

## Key References

See `references/papers-2026-05-21.md` for session-specific research on quantum RL process synthesis (state encoding decoupling qubit count from problem size) and pulse-level QML software frameworks (composable ansatz, JAX optimization, Fourier diagnostics). See `references/papers-2026-06-05.md` for dual-keyword arXiv discovery results and 3 new patterns (software AC-line compensation, hardware-tailored QEC resource estimation, QND measurement primitives for biased noise).

## Activation Keywords
- quantum systems engineering
- distributed quantum computing
- quantum control systems
- hybrid quantum-classical
- quantum architecture design
- robust quantum control
- quantum system design
- quantum error correction architecture

## Core Patterns

### Pattern 1: Hybrid Quantum-Classical Dataflow Architecture

Based on Tierkreis framework principles:

**Key Design Principles:**
1. Higher-order dataflow graph representation
2. Automatic parallelism and asynchronicity
3. Compositional algorithm design
4. Remote quantum computer integration (cloud/distributed)
5. Long-running algorithm management

**Implementation Steps:**
```
1. Identify quantum and classical computation boundaries
2. Design dataflow graph with nodes representing operations
3. Specify data types flowing between quantum/classical nodes
4. Implement runtime for distributed execution
5. Handle communication latency and asynchronicity
```

**Key Considerations:**
- Remote nature of quantum computers requires cloud integration
- Hybrid algorithms need distributed computing frameworks
- Graph-based representation mirrors algorithm visualization
- Automatic parallelization reduces manual optimization

### Pattern 20: SCOPE — Syndrome-Driven Control Plane for QEC-Enabled Quantum Networks (arXiv:2606.08873)

Network-layer architecture enabling joint routing and coding optimization using purely passive telemetry from QEC decoders:

- Problem: Quantum networks suffer from time-varying channel noise that topology-aware routing cannot adapt to. QEC error correction and network routing decisions are separated, leading to logical error rates exceeding thresholds.
- Solution: Three-component architecture — (1) Passive Telemetry Engine: harvests error syndromes from QEC decoders during user service with zero additional overhead; (2) Error Map Reconstruction: converts raw syndrome streams into spatial-temporal error models, tracking correlation patterns and noise hotspots; (3) Decision Engine: pushes optimal route-and-code configurations, jointly optimizing routing paths and QEC code selection in real-time.
- Results: 30-35% logical error rate reduction (up to 65% in extreme noise scenarios) vs topology-aware baselines. Zero measurement overhead — uses existing QEC syndrome data.
- Reusable pattern: WHEN system generates error/telemetry data as byproduct THEN (1) harvest passively without extra measurement, (2) reconstruct real-time error landscape, (3) jointly optimize across system layers (routing + coding), (4) push adaptive configurations.
- Pitfall: Syndrome collection latency must be faster than coherence times; noisy syndrome data may lead to suboptimal decisions; decision engine complexity grows with network size.

### Pattern 21: Network Constraints in Fault-Tolerant Distributed Quantum Computing (arXiv:2606.17495)

End-to-end simulation framework for modeling the interplay between error correction operations and communication resources in modular quantum computing:

- Problem: Existing analyses treat network constraints in isolation or through simplified models, leaving the interplay between QEC operations and communication resources underexplored.
- Solution: Joint simulation framework modeling surface-code operations, internal QPU connectivity, and realistic network constraints including finite entanglement generation rates, heralding latency, and memory coherence times.
- Key insight: Error correction overhead and communication resource constraints must be co-optimized — treating them independently leads to suboptimal system design.
- Reusable pattern: WHEN designing distributed quantum systems THEN (1) model QEC and communication jointly, (2) account for finite entanglement rates and heralding latency, (3) include memory coherence time constraints, (4) validate end-to-end rather than component-by-component.
- Pitfall: Simplified network models (e.g., assuming instantaneous entanglement) overestimate system performance; surface-code cycle time must be compatible with network latency.

### Pattern 22: Q-READY — Predictive Feasibility Assessment for Hybrid Quantum-Classical Applications

Before deploying quantum computation, systematically assess whether a problem can benefit from quantum acceleration and how to optimally partition workloads:

- Problem: Teams waste resources trying quantum approaches on problems where classical methods dominate, or miss quantum opportunities due to lack of structured assessment.
- Solution: 5-dimension quantum readiness scoring:
  1. **Algorithm Mapping** (1-5): Does the problem map to known quantum algorithms (QAOA, VQE, HHL, quantum simulation)?
  2. **Noise Resilience** (1-5): Can the application tolerate NISQ-level errors?
  3. **Encoding Efficiency** (1-5): Is there an efficient classical-to-quantum data loading strategy?
  4. **Classical Competition** (1-5): What's the gap between classical baseline and potential quantum advantage?
  5. **Infrastructure Access** (1-5): Availability of quantum hardware/simulators
- Threshold: Total ≥ 15 = quantum-feasible; 10-14 = monitor (reassess as hardware improves); < 10 = not feasible

**Hybrid Partitioning Strategy:**
1. Identify quantum-suitable subproblems (superposition, entanglement, interference benefit)
2. Design classical pre-processing (data encoding, feature engineering) and post-processing (result interpretation, error mitigation)
3. Define interface: data exchange formats, synchronization points
4. Build iterative feedback: classical optimization adjusts quantum circuit parameters

**Software Engineering Applications (from Q-READY paper):**
- Test optimization: quantum-enhanced test case prioritization
- Project scheduling: QAOA-based resource allocation
- Code analysis: quantum graph algorithms for static analysis
- CI/CD pipeline: quantum scheduling for parallel test execution

**Pitfall:** Feasibility thresholds are moving targets — classical algorithms (tensor networks, approximation algorithms) continue improving. Reassess quarterly.

- Reference: arXiv:2606.16201 — "Q-READY: Predictive Feasibility Assessment for Hybrid Quantum-Classical Applications"

### Pattern 2: Sampling-based Learning Control (SLC) for Quantum Systems

Robust control design for quantum systems with uncertainties.

**Two-Phase Workflow:**
```
Phase 1: Training
1. Construct augmented system with artificial samples
2. Sample uncertainty parameters from distribution
3. Optimize control for sample set
4. Validate across sampled scenarios

Phase 2: Testing
1. Apply learned control to real system
2. Measure performance across uncertainty range
3. Refine if performance degrades
4. Iterate until robustness criteria met
```

**Key Parameters:**
- Sample distribution selection (uniform, Gaussian, etc.)
- Training sample size (balance coverage vs computational cost)
- Robustness metric (probability of success, average fidelity)
- Iteration convergence criteria

### Pattern 3: Distributed Quantum Computing Architecture

Understanding computational limits in distributed quantum settings.

**Architecture Levels:**
```
Level 1: Bandwidth-limited networks
- Quantum communication constrained by channel capacity
- Entanglement distribution protocols
- Local quantum operations with remote coordination

Level 2: Distance-constrained networks
- Large geographic separation
- Latency-aware quantum gate scheduling
- Distributed quantum error correction

Level 3: Full quantum network
- Quantum internet protocols
- Distributed quantum algorithms
- Quantum repeater architectures
```

**Key Metrics:**
- Quantum communication bandwidth
- Entanglement fidelity across distance
- Gate latency compensation
- Distributed algorithm complexity

### Pattern 4: RL-based Robust Quantum Control (2025-2026 research)

Three complementary approaches for robust quantum control under noise and model uncertainty:

**RLfD (Reinforcement Learning from Demonstration)**:
- Problem: Model-free RL needs excessive quantum system interaction; model-based RL suffers from model bias.
- Solution: Use model-generated control sequences as demonstrations to warm-start RL training.
- Benefit: Faster convergence, stable training, avoids model bias in final policy.
- Reference: Li & Fan et al., npj Quantum Information (2025).

**Adaptive Feedback Control (RL + Kalman Filter)**:
- Problem: NISQ device parameters drift; static QAOA parameters perform poorly.
- Solution: Combine RL for adaptive parameter tuning with Kalman filters for noise estimation.
- Benefit: Dynamic adjustment to time-varying noise without recalibration pauses.
- Reference: "Adaptive and Robust Feedback-Based Quantum Optimization" (Springer, 2025).

**Polynomial Global Optimization**:
- Problem: Quantum control problems are nonconvex with dense local extrema.
- Solution: Formulate as polynomial optimization for certified global optimality.
- Reference: "Globally Optimal Control of Quantum Dynamics" (Phys. Rev. Research, 2025).

### Pattern 5: Hardware Co-Design for Quantum Control

- Problem: Classical control hardware imperfections (crosstalk, beam leakage) degrade quantum operations.
- Solution: Design control software aware of and compensating for hardware-specific imperfections.
- Key insight: Joint optimization of control algorithms and hardware calibration parameters.
- Reference: "Hardware Co-Designed Intelligent Quantum Control Framework" (arXiv:2504.11737).

### Pattern 6: Formal Verification for QEC Fault-Tolerance

- Problem: QECC implementations may have subtle fault-tolerance violations not caught by simulation.
- Solution: Use quantum symbolic execution to formally verify fault-tolerance properties.
- Key insight: Encode fault-tolerance within the language of quantum programs for automatic verification.
- Reference: "Verifying Fault-Tolerance of Quantum Error Correction Codes" (arXiv:2501.14380).

### Pattern 7: Ultra-High-Rate QEC Architectures

- Problem: QEC decoding throughput is a bottleneck for practical fault-tolerant quantum computing.
- Solution: Reconfigurable architectures for ultra-high-rate quantum error correction.
- Reference: "Towards Ultra-High-Rate Quantum Error Correction" (arXiv:2604.16209).

### Pattern 8: Dissipative Thermal State Preparation with Rigorous Error Bounds

Recent advances in analog quantum simulation provide rigorous error-bounded thermal state preparation:

- Problem: Digital Lindbladian simulation for thermal states remains out of reach for NISQ hardware.
- Solution: Collision model approximations using resettable ancilla qubit baths with tunable time-dependent couplings.
- Key insight: System-bath coupling generates both desired Lindblad dynamics AND a unitary Lamb shift that tightens the fixed-point error bound, scaling as J^2 where J is the coupling strength.
- Randomized drive implementation suppresses spectral resonances with the many-body spectrum.
- Practical trade-off: Stronger J speeds convergence but increases Lamb shift error.
- Reference: arXiv:2605.03011.

### Pattern 9: Analytical Two-Pulse Control for High-Fidelity Molecular Qubits

Closed-form unitary evolution for universal single-qubit gates:

- Problem: Complex control protocols and sensitivity to experimental imperfections limit practical quantum gate operations.
- Solution: First-order Magnus expansion to derive closed-form unitary evolution from optimized two-pulse sequences in rotational states of ultracold molecules (e.g., NaCs).
- Results: Gate fidelities >0.9999 with minimal population leakage to auxiliary states.
- Key benefit: Complex multi-gate sequences executable with phase-locked operations; time-dependent molecular orientation encodes gate truth table enabling practical gate tomography.
- Platform-independent: Applicable to other molecular species and physical platforms.
- Reference: arXiv:2605.03461.

### Pattern 10: Adaptive Feedback Control for Bistable Qubits

Bistable quantum systems require adaptive rather than static control:

- Problem: Bistable qubits exhibit two stable operating regimes requiring dynamic parameter adjustment.
- Solution: Adaptive feedback control that monitors system response in real-time, identifies current operating regime, and adjusts control parameters accordingly.
- Key considerations: Hysteresis in bistable systems means transition paths matter; noise in feedback loop must be accounted for; adaptive adjustments must be faster than decoherence timescale.
- Reference: arXiv:2605.03187.

### Pattern 11: Unauthenticated Byzantine Consensus for Post-Quantum Distributed Systems

Fast TetraBFT methodology for post-quantum distributed consensus:

- Problem: Post-quantum signatures (lattice-based, hash-based) are significantly larger and slower, creating throughput bottlenecks in Byzantine consensus protocols.
- Solution: Unauthenticated BFT protocols that rely only on authenticated point-to-point channels (e.g., TLS) rather than message-level signatures, achieving optimal f < n/3 Byzantine fault tolerance.
- Key insight: Latency optimization focuses on the critical path — pre-prepare (optimized proposal), prepare (parallel validation), commit (batched messages), decision (fast path).
- Benefits: Reduced cryptographic overhead, post-quantum ready by design, optimal fault tolerance preserved.
- Pitfall: Requires trusted point-to-point channels; partial synchrony assumption (liveness not guaranteed in fully asynchronous networks).
- Reference: arXiv:2606.03754 — "Fast TetraBFT: Optimizing Latency Where It Matters"

### Pattern 12: Topological Quantum Gates via Majorana Fermion Braiding

Planar Pauli stabilizer code framework for fault-tolerant logical gate design:

- Problem: Logical information in topological QEC is stored non-locally, making efficient gate design challenging.
- Solution: Encode logical qubits in pairwise Majorana fermion parity. Physical braiding operations implement logical Clifford gates with full topological protection.
- Key insight: Braiding alone provides Clifford gates; T-gates require supplementary protocols (magic state distillation). Planar 2D layout enables practical hardware implementation.
- Benefits: Local errors cannot affect non-local parity encoding (topological protection), scalable distance (scales with √N).
- Pitfall: Braiding completeness limited to Clifford group; measurement-based gates introduce additional error channels; physical Majorana realization has decoherence beyond ideal model.
- Reference: arXiv:2606.03916 — "Practical gates by Majorana fermion motion"

### Pattern 13: Optimal Control for Trapped-Ion Piston Operations

GRAPE/CRAB-based optimal control methodology for two-ion quantum device manipulation:

- Problem: Precise ion positioning in trapped-ion quantum devices requires sub-nanometer accuracy while maintaining high gate fidelity.
- Solution: GRAPE (Gradient Ascent Pulse Engineering) and CRAB (Chopped Random Basis) algorithms for optimal control pulse design, combined with closed-loop experimental calibration.
- Key insight: Two-ion system has collective modes (center-of-mass, stretch) that enable controlled coupling between motional and internal states for entangling gates.
- Benefits: Gate fidelity >99.9%, microsecond-scale pulses, extensible to N-ion chains via mode decomposition.
- Pitfall: Ion trap heating degrades control fidelity (requires cryogenic operation for best results); real trap potentials deviate from ideal harmonic; crosstalk in multi-ion systems.
- Reference: arXiv:2606.03488 — "Piston control in a two-ion quantum device"

### Pattern 14: Full Extractor Architecture for QLDPC Logical Processing

Full extractor construction for fault-tolerant logical processing in Hypergraph Product (HGP) QLDPC codes:

- Problem: QLDPC codes offer low-overhead quantum memories but lack practical logical processing methods. Prior approaches introduce compilation overhead vs surface code PBC.
- Solution: Construct full extractors (surgery systems) that measure arbitrary logical Pauli operators on a code block, enabling Pauli-based computation without compilation overhead.
- Key insight: Assemble many partial extractors with verifiable fault-tolerance into a single full extractor. Extractor size 50-80% of base HGP code, max qubit degree 10.
- Benefits: Combines QLDPC space efficiency with surface-code-PBC convenience. Distance-10 code achieves ~10^-6 logical error at 0.1% physical error rate.
- Pitfall: Requires fixed-connectivity hardware design (max degree 10); partial extractors must be independently verified for fault-tolerance before assembly.
- Reference: arXiv:2606.03507 — "Full Extractors for Logical Processing in Hypergraph Product Codes" (Chuang et al.)

### Pattern 15: ML-Based Quantum Error Mitigation via Clifford Surrogate Training

Practical ML-QEM protocol for variational quantum algorithms on NISQ processors:

- Problem: Existing ML-QEM methods rely on inaccessible noiseless training data, limiting practical use on real quantum hardware.
- Solution: Generate training data by simulating (near-)Clifford circuits (classically simulable), use for model selection and training, then apply to arbitrary variational circuits.
- Key insight: Error structure learned from Clifford circuits generalizes to non-Clifford variational circuits of similar structure. Model transfers across different target Hamiltonians.
- Benefits: Several-fold error suppression, superior to ZNE in high-noise regime. No need for noiseless reference data. Cross-Hamiltonian transfer reduces per-experiment overhead.
- Pitfall: Requires structurally similar Clifford circuits for training; transfer quality depends on Hamiltonian similarity; benchmarked primarily on Sherrington-Kirkpatrick model.
- Reference: arXiv:2606.02697 — "Machine Learning-based Quantum Error Mitigation for Variational Algorithms" (Korolev et al.)

### Pattern 16: Deterministic Large Cat State Generation via Dynamical Invariants

Deterministic generation of 100+ photon cat states for quantum metrology and fault-tolerant computation:

- Problem: Large cat states are fragile under decoherence; probabilistic generation methods have low success rates that scale poorly with size.
- Solution: Use dynamical invariants of hybrid qubit-bosonic systems under time-dependent Hamiltonians (Hermitian and non-Hermitian) for deterministic state preparation.
- Key insight: Universal Quantum Control (UQC) theory enables system dynamics analysis that preserves target state as invariant eigenstate throughout evolution. Non-Hermitian dynamics can accelerate preparation.
- Benefits: Deterministic (not probabilistic) generation; operates under dissipation; applicable to quantum metrology and bosonic QEC resource preparation.
- Pitfall: Requires precise time-dependent Hamiltonian control; dissipation engineering must be carefully calibrated; non-Hermitian control introduces additional design complexity.
- Reference: arXiv:2606.03293 — "Deterministic Generation of Cat States with More Than 100 Photons Under Dissipation"

### Pattern 17: Software-Based Compensation for Reproducible Coherent Errors

When quantum control errors are reproducible with respect to an external reference signal (AC power line phase, temperature cycle, etc.), software compensation achieves dramatic error reduction without hardware modifications:

- Problem: AC mains power line-synchronous disturbances cause coherent, time-dependent errors in precision quantum control (trapped-ion detunings, accumulated phases on superpositions).
- Solution: Line-triggered calibration frame measures reproducible disturbances; software corrections applied to control sequences at two levels — instantaneous detuning compensation during pulses + phase accumulation compensation between pulses.
- Key results: 21(9)× reduction in AC detuning contribution, recovery of 99.93(1)% gate fidelity via RB, 10(7)% → 70(9)% success on 16-level qudit Bernstein-Vazirani.
- Reusable pattern: IF noise is reproducible w.r.t. external reference THEN (1) trigger measurement on reference, (2) build deterministic disturbance model, (3) apply software correction, (4) no hardware needed.
- Qudit generalization: Extend qubit compensation to multilevel systems by characterizing all relevant energy structure shifts and computing phase accumulation across all transitions.
- Pitfall: Compensation only works for reproducible (not stochastic) noise sources. Randomized benchmarking is essential to verify that standard decay model is recovered after compensation.
- Reference: arXiv:2606.00358 — "Software-based compensation of AC-line-induced control errors in qubits and qudits"

### Pattern 18: Hardware-Tailored QEC Resource Estimation (Bottom-Up + Top-Down)

Quantum error correction resource estimation must account for hardware-specific noise characteristics rather than using architecture-agnostic models:

- Problem: Architecture-agnostic QEC resource estimation leads to over/under-estimation of physical qubit requirements across different hardware platforms (silicon spin, superconducting, trapped-ion).
- Solution: Dual-directional analysis — (a) bottom-up: hardware noise model (Hamiltonian + 1/f non-Markovian noise) → logical error rate → application capability; (b) top-down: application requirements → logical error rate → hardware performance constraints. Intersection identifies gap.
- Key results on silicon spin qubits: optimized control pulses reduce magic-state distillation overhead by 42%; biased error-correcting codes achieve ~3× physical footprint reduction vs. surface code, even without physical-bias-preserving operations.
- Architecture comparison: evaluate shuttling-based, dense nearest-neighbor, and hybrid designs under realistic noise; compare surface/color/biased codes; analyze 5→1 vs 15→1 magic-state distillation protocols.
- Highest-ROI lever: control pulse optimization (30-50% overhead reduction) before considering hardware redesign.
- Reference: arXiv:2605.28936 — "Hardware-Tailored Resource Estimation for Magic-State Distillation on Silicon Spin Qubits"

### Pattern 19: QND Measurements as Fault-Tolerance Primitive for Biased Noise

Quantum non-demolition (QND) multi-qubit Pauli measurements can replace bias-preserving CNOT gates for all bias-tailored error correction operations:

- Problem: Leveraging noise bias (phase-flip >> bit-flip) reduces FTQC overhead, but existing approaches require bias-preserving CNOT gates that are experimentally challenging and provably impossible for strictly 2D systems.
- Solution: QND ZZ measurements as universal primitive — compile all bias-tailored EC operations (repetition code stabilizers, XZZX surface code stabilizers, LDPC code stabilizers) using measurement-only approach. No bias-preserving CNOT required.
- Key results: asymmetric XZZX surface code achieves ~1.25% phase-flip threshold with 6× qubit overhead reduction at η=10⁴; repetition code achieves ~2.3% threshold in large bias regime.
- Physical platforms: solid-state nuclear spins coupled to electron spin ancillas; dissipatively stabilized superconducting cat qubits.
- Reusable pattern: WHEN hardware lacks required gate BUT supports measurement primitive THEN (1) express gate operations in measurement basis, (2) compile stabilizer circuits measurement-only, (3) verify threshold/overhead match or exceed gate-based approach.
- Reference: arXiv:2605.24262 — "Quantum non-demolition measurements as a practical primitive for fault-tolerant computation against biased noise"

### Pattern 24: Safe Quantum Control Deployment — Q-DASC & Simplex Architecture (2026-07)

When deploying quantum control policies in safety-critical cyber-physical systems, classical safety wrapping is mandatory — raw quantum policies show unacceptable violation rates even under nominal conditions.

**Q-DASC Framework** (arXiv:2606.28834):
- Problem: Variational quantum circuit (VQC) policies inherit deployment weakness — when model is locally wrong, apparently-safe policy violates real-world constraints. NISQ read-out noise adds uncertainty.
- Solution: Four-component safety wrapper around VQC: (1) Discrepancy detection via false-discovery-rate control identifies misspecified operating regimes; (2) Shrinkage repair fixes local model gains; (3) Classical projection onto repaired feasible set ensures constraint satisfaction; (4) Attribution engine classifies residual violations into policy error, model error, or physical limits.
- Results: 26.0% → 0.02% comfort violation on BOPTEST building emulators; 0.24% under NISQ noise; 0.00% with repair-aware VQC variant.
- Key insight: Classical projection layer is noise-invariant — finite-shot and depolarizing read-out noise cannot break safety certificate because final projection is deterministic classical computation.

**Simplex Architecture** (arXiv:2606.31056):
- Pattern: High-performance quantum module (QA-HSGPR) + high-assurance classical module (GPR) + runtime safety monitor that dynamically switches between them.
- Demonstrated on CSTR benchmark with controllable performance-safety trade-off.
- Reusable pattern: WHEN quantum module is high-performance but untrusted THEN (1) build classical high-assurance fallback, (2) runtime monitor evaluates safety continuously, (3) automatic failover on safety violation, (4) dynamic switching based on conditions.

**Reusable pattern**: WHEN deploying quantum RL/VQC in CPS THEN (1) wrap with classical safety layer, (2) detect model misspecification with statistical control (FDR), (3) repair local models via shrinkage, (4) project onto feasible set, (5) attribute violations for diagnosis, (6) design Simplex fallback for critical systems.

**Pitfall**: Never deploy raw VQC policies without safety wrapping — 26% violation rate is unacceptable. Excessive shrinkage can over-smooth legitimate dynamics. Safety projection may increase energy consumption — optimize repair-aware variants to minimize interventions.

### Pattern 23: Quantum Compilation Systems — Three Axes of Optimization (arXiv:2606.31833, 2606.31791, 2606.31837)

Beyond qubit routing, quantum compilation has three orthogonal optimization axes discovered in 2026-07-02 research:

**Axis A: Movement Elimination (buffer-relay fabric)**
- Replace dynamic qubit shuttling with static buffer atoms mediating long-range interactions
- BRIDGE pattern: ~10× fidelity, ~540× faster than shuttle-based baselines
- Key: dual-species 2D interleaved array + lazy-move compiler
- See skill: `bridge-buffer-relay-compilation`

**Axis B: Error-Budget-Aware Decomposition**
- Minimize two-qubit infidelity (not gate count) per gate decomposition choice
- **Safety finding**: pattern-matched relative-phase Toffoli substitution is silently incorrect — requires instance-specific equivalence verification
- Up to 39.5% two-qubit gate reduction, 36-43% circuit infidelity reduction
- See skill: `context-verified-toffoli-decomposition`

**Axis C: Program Representation for Parallelization**
- Permeability DAG data structure captures commutation across abstraction levels
- Automatic parallelization + memory management + uncomputation synthesis
- Retargetable across NISQ/FTQC and per-device speeds
- See skill: `permeability-dag-quantum-parallelization`

**Reusable pattern**: WHEN designing a quantum compiler THEN (1) analyze interaction graph for hotspot qubits, (2) apply movement elimination first (static routing > dynamic), (3) select gate decompositions by error budget not gate count, (4) verify equivalence per-substitution, (5) use permeability analysis for parallelism extraction.

## Implementation Checklist

When designing a robust quantum control system:

1. **Noise characterization**: Identify dominant noise sources (dephasing, amplitude damping, crosstalk)
2. **Control strategy selection**:
   - Model available? → Model-based RL with RLfD warm-start
   - No model? → Model-free RL with demonstration data
   - Real-time drift? → Adaptive feedback (RL + Kalman filter)
3. **Verification strategy**:
   - Gate-level: Symbolic execution for fault-tolerance verification
   - System-level: Hardware co-design with calibration-aware control
4. **Optimization method**:
   - Small scale: Gradient-based (GRAPE, CRAB)
   - Nonconvex landscape: Polynomial optimization for global solutions
   - NISQ devices: Adaptive feedback with noise mitigation
5. **Architecture design**:
   - Characterize classical-quantum boundary for each subtask
   - Design hybrid interface with minimal overhead
6. **Compilation optimization** (2026-07-02):
   - Routing: position graph + SABRE → see `quantum-compiler-routing`
   - Decomposition: error-budget-aware selection with equivalence verification → see `context-verified-toffoli-decomposition`
   - Movement elimination: static buffer-relay fabric → see `bridge-buffer-relay-compilation`
   - Parallelization: permeability DAG analysis → see `permeability-dag-quantum-parallelization`

## Error Handling

| Error Type | Detection | Recovery |
|-----------|-----------|----------|
| Model bias | Compare model-based vs model-free RL performance | Switch to RLfD or model-free approach |
| Hardware crosstalk | Fidelity drop on multi-qubit gates | Apply co-designed compensation pulses |
| Noise drift | Calibration metrics deviate from baseline | Trigger adaptive recalibration |
| Local optima trap | Multiple runs converge to different fidelities | Use polynomial optimization or global search |
| QEC failure | Logical error rate exceeds threshold | Verify fault-tolerance via symbolic execution |

## Tools Used

- exec: Run quantum simulation tools (Qiskit, Cirq, QuTiP)
- read: Load quantum circuit specifications, control parameters
- write: Save control sequences, architecture diagrams
- image: Visualize quantum circuits, dataflow graphs

## References

### Quantum Control System Libraries
- QuTiP: Quantum Toolbox in Python for dynamics simulation
- Qiskit Pulse: Low-level quantum control
- Cirq: Google's quantum computing framework

### Distributed Computing Patterns
- MapReduce for quantum-classical hybrid algorithms
- Actor model for asynchronous quantum operations
- Dataflow graphs for compositional algorithms

## Instructions for Agents

### Step 1: Identify System Type

Determine the quantum system category:
- **Hardware control**: Focus on control pulses, calibration
- **Algorithm design**: Focus on dataflow, composition
- **Distributed architecture**: Focus on communication, latency

### Step 2: Apply Pattern

For **hybrid quantum-classical**:
1. Map classical and quantum operations
2. Design dataflow representation
3. Specify communication protocols
4. Handle latency and asynchronicity

For **robust quantum control**:
1. Identify uncertainty sources (hardware noise, parameter drift)
2. Define uncertainty distribution
3. Apply SLC two-phase workflow
4. Validate robustness criteria

For **distributed quantum**:
1. Analyze network constraints (bandwidth, distance)
2. Design entanglement distribution protocol
3. Schedule quantum gates accounting for latency
4. Implement distributed error correction

### Step 3: Validate Design

Check:
- Physical constraints satisfied (decoherence time, gate fidelity)
- Communication latency within bounds
- Error correction overhead acceptable
- Classical-quantum interface functional

## Example Workflow

**Designing a Hybrid Quantum-Classical Algorithm:**

```
1. Problem: Variational Quantum Eigensolver (VQE) for molecular simulation
2. Analysis:
   - Quantum part: Parameterized quantum circuit
   - Classical part: Optimization loop, Hamiltonian construction
   - Distributed: Quantum computer remote, classical local
   
3. Architecture:
   - Dataflow graph: 
     - Classical node: Parameter optimization
     - Quantum node: Circuit execution
     - Data flow: Parameters → Quantum → Measurements → Classical
   
4. Implementation:
   - Use Tierkreis-like dataflow framework
   - Handle remote quantum API calls
   - Asynchronous parameter updates
   
5. Validation:
   - Test with molecular Hamiltonians
   - Measure convergence rate
   - Verify distributed latency handling
```

## Related Skills

- quantum-control-optimization
- distributed-systems-design
- hybrid-computing-architecture
- robust-control-systems

## Limitations

- Requires quantum computing domain knowledge
- Hardware-specific constraints vary by platform
- Distributed quantum computing is evolving rapidly
- Real quantum hardware access needed for validation