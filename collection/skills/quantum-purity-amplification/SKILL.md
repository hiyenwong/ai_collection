---
name: quantum-purity-amplification
description: Quantum Purity Amplification (QPA) methodology — coherently transforming n copies of a mixed state into high-fidelity copies of a chosen eigenstate. Solves QPA in the general setting with arbitrary target eigenstates, local dimension d, and generic input states. Use when: quantum error mitigation, state purification, quantum state preparation, mixed-to-pure state transformation, quantum information processing with noisy states.
---

# Quantum Purity Amplification (QPA)

## Core Concept

Quantum Purity Amplification is the task of coherently transforming n copies of a mixed state into high-fidelity copies of a chosen eigenstate. The general solution handles:
- n input copies → m output copies
- Arbitrary target eigenstates
- Arbitrary local dimension d
- Generic input states

## Key Insights

1. **Eigenstate Selection**: QPA can target any chosen eigenstate of the input mixed state, not just the dominant one
2. **Coherent Transformation**: The process preserves quantum coherence throughout the purification
3. **Scalability**: The framework handles arbitrary local dimensions d (qubits, qudits, continuous-variable systems)
4. **Fidelity Trade-off**: Higher output fidelity requires more input copies, with quantifiable bounds

## Implementation Patterns

### Basic QPA Protocol
1. Prepare n copies of the mixed state ρ
2. Apply coherent transformation unitary U
3. Measure ancilla to verify purification
4. Obtain m high-fidelity copies of target eigenstate |ψ⟩

### Eigenstate Targeting
- For dominant eigenstate: standard purification suffices
- For arbitrary eigenstate: apply spectral filtering before amplification
- For degenerate eigenvalues: use symmetry-adapted protocols

## Applications

- **Quantum Error Mitigation**: Purify states before computation
- **Quantum State Preparation**: Generate high-purity resource states
- **Quantum Communication**: Improve channel state quality
- **Quantum Sensing**: Enhance probe state purity

## Activation Keywords
- quantum purity amplification
- QPA
- state purification
- mixed to pure state
- quantum state amplification
- eigenstate purification
- 量子纯度放大
- 量子态纯化

## Related Skills
- quantum-error-correction-methods
- distributed-quantum-error-correction
- quantum-state-preparation-medical
