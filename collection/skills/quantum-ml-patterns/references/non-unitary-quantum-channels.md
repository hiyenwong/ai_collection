# Non-Unitary Quantum Learning via Trainable Channels (arXiv:2606.15808)

Methodology from Wen et al. (Jun 2026) reformulating quantum channels as **trainable computational primitives** rather than detrimental noise.

## Core Framework

Traditional QML is constrained to unitary dynamics:
ρ_out = U(θ) ρ_in U†(θ)

Trainable channel framework uses CPTP maps:
ρ_out = Σ_k K_k(θ) U(φ) ρ_in U†(φ) K_k†(θ)

## Key Innovations

1. **Structured superposition**: Channel-enhanced outputs form superpositions of functional components, each governed by effective observables
2. **Spectral modulation**: Unlike unitary transformations (spectral invariance), channel parameters enable adaptive spectral modulation during training
3. **Enriched optimization geometry**: Ensemble-averaged gradients + additional directions from Kraus operators

## Empirical Results
- Trainable amplitude-damping and phase-damping channels improve classification accuracy
- Outperforms purely unitary baselines of equivalent depth
- Non-unitary degrees of freedom provide escape routes from barren plateaus

## Implementation Pattern (PennyLane)
def trainable_damping_circuit(params, n_qubits, n_layers):
    for layer in range(n_layers):
        for i in range(n_qubits):
            qml.Rot(params[layer, i, 0], params[layer, i, 1], params[layer, i, 2], wires=i)
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i + 1])
        for i in range(n_qubits):
            qml.AmplitudeDamping(sigmoid(params[layer + n_layers, i]), wires=i)

## CPTP Constraint Enforcement
- Reparametrize via Stinespring dilation (unitary on system + ancilla)
- Projection after each gradient step: Σ_k K_k† K_k = I
- Penalty term: λ ||Σ_k K_k† K_k - I||²

## When to Use
- Tasks where unitary-only QML shows poor convergence
- Classification problems with noisy or energy-dissipative data structure
- Near-term hardware where channels are unavoidable — make them trainable rather than treating them as fixed noise
