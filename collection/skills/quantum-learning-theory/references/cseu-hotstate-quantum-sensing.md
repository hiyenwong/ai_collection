# Session Knowledge Bank: CSEU and Hot-State Quantum Sensing

Source: arXiv papers from 2026-06-14 research session (Information Science + Quantum)

---

## Classical Shadow Estimation of Unitary Channels (CSEU)
**Source**: arXiv:2606.13638

### Protocol
- Query unknown d-dimensional unitary U
- Store classical data for post-hoc prediction of tr[O·UρU†]
- Parallel non-adaptive protocol achieves O(d/ε) queries
- Heisenberg scaling in ε (vs standard shot-noise ε⁻²)
- Query-optimal: matching Ω(d/ε⁻¹) lower bound proven

### Key Applications
1. **Unitary channel tomography** - optimal with parallel queries only
2. **Hamiltonian learning** - learn H from e^{-iHt}
3. **Pauli transfer matrix learning** - efficient for sparse channels
4. **Shallow circuit learning** - NISQ device characterization

### Protocol Steps
1. Prepare random input states (Haar/Clifford)
2. Apply unknown unitary U
3. Measure in random bases
4. Store classical snapshots
5. Post-process to predict any observable

### Implementation Notes
- Clifford measurements for efficiency
- Classical post-processing scales polynomially
- Memory: O(d²) for storing shadows
- Verified on IBM quantum processors (up to 156 qubits)

---

## Hot-State Quantum Displacement Sensing
**Source**: arXiv:2606.13650

### Key Insight
Complete cooling to ground state is NOT universally optimal for quantum-enhanced displacement sensing.

### Two Mechanisms
1. **Parity Selection**: Projecting mixed probe onto definite parity sector removes thermal suppression of displacement quantum Fisher information, which can then increase with initial thermal occupation
2. **Coherence Between Displaced Components**: Coherent superpositions of opposite displacements retain sensitivity even when underlying state is mixed

### Protocol Classification
- Parity-selection only
- Coherence-only
- Both mechanisms combined

### Optimization Framework
Compare initial cooling vs direct hot-state preparation under realistic decoherence → complete cooling is not universally optimal.

---

## Bounded-Degree max-LINSAT Complexity
**Source**: arXiv:2606.13570

### Results
- NP-hard to exceed r/q + O(1/√D) for max-Ek-LINSAT(q,r) with bounded degree D
- DQI with classical decoders: information-theoretic 1/√(D log D) barrier
- DQI with quantum decoders: compatible with 1/√D scaling (optimal)
- Quantum decoding is key ingredient for matching complexity-theoretic scaling
