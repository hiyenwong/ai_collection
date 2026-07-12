## Non-Markovian Kerr Feedback Superiority (arXiv:2606.06689)

**Core finding**: A single Kerr (nonlinear) element with time-delayed feedback achieves unbounded cross-time nonlinear rank, replacing up to ~100 linear optical modes in CV-QRC.

**Theorem (Resource Separation)**:
- N-mode Gaussian reservoir: max cross-time nonlinear rank = 2N (hardware ceiling)
- Single Kerr + feedback depth D: rank = D (no ceiling, D = 30–230 on integrated platforms)

**Key mechanism**: 
- Kerr effect: phase depends on intensity → true multiplication inside medium
- Feedback: light revisits Kerr element repeatedly → one mode mixes its own history
- "Feedback turns time into space": D passes through one nonlinear mode replace D parallel linear modes

**Counterintuitive role of loss**:
- Loss is the enabler — each round-trip dims light → different nonlinear phase per pass
- Without loss, passes would be redundant
- Practical loss: η ≈ 0.9–0.99 per round-trip

**Implementation**:
```python
# Kerr Hamiltonian: H = χ (a†a)²
# Intensity-dependent phase: φ = χ|α|²
# Feedback depth: D = 30–230 (integrated platforms)
# Loss per round-trip: η ≈ 0.9–0.99
```

**Applications**: Nonlinear channel equalization, temporal sequence prediction with cross-time correlations, photonic neural networks.

## Hybrid Quantum-Classical Reservoirs (arXiv:2606.21327)

**Core finding**: Hybrid QRC+ESN architecture overcomes linearity barrier of standalone QRC for nonlinear functionals (purity, entropy).

**Key insight**: QRC alone is fundamentally linear for single input states. Classical ESN provides nonlinear approximation; quantum reservoir provides enhanced information retrieval.

**Results**:
- Hybrid > max(quantum alone, classical alone) in both linear and nonlinear tasks
- Advantage persists under partial measurements (single-axis)
- Online monitoring protocol accounts for measurement back-action and finite shot counts

**Architecture**:
```
Quantum Input States → Quantum Reservoir (qubits) → Measurements → Classical ESN → Output
```

**Practical guidance**: Single-axis measurements sufficient for advantage; full tomography not required. Near-term practical for current qubit hardware.
