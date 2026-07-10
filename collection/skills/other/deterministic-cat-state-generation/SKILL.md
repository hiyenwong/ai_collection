---
name: deterministic-cat-state-generation
description: "Deterministic generation of large cat states (100+ photons) using dynamical invariants of hybrid qubit-bosonic systems under time-dependent Hamiltonians. Universal quantum control theory for quantum metrology and fault-tolerant computation. arXiv:2606.03293."
metadata:
  arxiv_id: "2606.03293"
  category: "quant-ph"
  published: "2026-06-02"
---

## Deterministic Generation of Cat States with More Than 100 Photons Under Dissipation

**arXiv: 2606.03293** (June 2026)

### Problem

Large-size cat states are fundamental for exploring quantum-to-classical transitions and are promising resources for quantum metrology and fault-tolerant quantum computation. However, amplifying cat state magnitude is challenging due to growing fragility under decoherence.

### Solution

**Dynamical Invariant-Based Control**:
- Uses dynamical invariants of hybrid qubit-bosonic systems
- Works under both Hermitian and non-Hermitian time-dependent Hamiltonians
- Applies Universal Quantum Control (UQC) theory for system dynamics analysis
- Deterministic generation (not probabilistic or post-selected)

### Key Results

- **Scale**: Cat states with 100+ photons
- **Method**: Dynamical invariant engineering under time-dependent control
- **Robustness**: Operates under dissipation (decoherence present)
- **Framework**: Universal Quantum Control theory applies to broad class of systems

### Reusable Patterns

#### Pattern 1: Dynamical Invariant Engineering
Use dynamical invariants to steer quantum systems to desired states:
1. Identify target state (e.g., cat state of size α)
2. Construct dynamical invariant that has target state as eigenstate
3. Design time-dependent Hamiltonian that preserves the invariant
4. System evolves deterministically to target regardless of initial state

#### Pattern 2: Hybrid Qubit-Bosonic Control
Leverage hybrid systems combining discrete (qubit) and continuous (bosonic) variables:
- Qubit provides discrete control degrees of freedom
- Bosonic mode provides large Hilbert space for encoding
- Coupling enables deterministic state preparation in bosonic subspace

#### Pattern 3: Non-Hermitian Quantum Control
Exploit non-Hermitian Hamiltonians for enhanced control:
- Dissipation can be engineered as a resource, not just a nuisance
- Non-Hermitian dynamics enable faster state preparation
- Effective for large-state generation where Hermitian-only approaches are too slow

### Applications

- **Quantum metrology**: Large cat states for Heisenberg-limited sensing
- **Fault-tolerant QC**: Cat states as logical qubits in bosonic QEC codes
- **Quantum-to-classical transition**: Study decoherence at macroscopic scales
- **Universal QC**: Cat states as resources for universal gate sets

### Activation
cat states, bosonic codes, dynamical invariants, universal quantum control, quantum metrology, fault-tolerant quantum computation, hybrid qubit-bosonic, non-Hermitian Hamiltonian, deterministic state preparation

### Related Skills
- `quantum-control-engineering` - Quantum control patterns
- `bosonic-grid-states-qec` - Bosonic QEC codes
- `universal-robust-quantum-control` - Noise-agnostic quantum control
