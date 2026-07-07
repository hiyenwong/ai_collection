---
name: sqnn-adversarial-robustness
description: "Stochastic Quantum Neural Network (SQNN) adversarial robustness methodology combining decoherence-contraction theory, quantum dropout regularisation, and Lindblad master equation formulation. Use when: (1) Building adversarially robust quantum neural networks, (2) Studying noise as computational resource in QML, (3) Implementing quantum dropout or depolarising regularisation, (4) Analyzing adversarial robustness of quantum classifiers under FGSM/PGD attacks, (5) Designing hybrid quantum-classical intrusion detection or medical classifiers with noise-based defence, (6) Implementing SQNN on neutral-atom quantum hardware."
---

# SQNN Adversarial Robustness

## Core Architecture

SQNN encodes neuronal activations as qubits, synaptic topology as entanglement, and neural noise through a Lindblad master equation.

### N-Qubit SQNN Formulation

```
ρ' = -i[H(θ), ρ] + Σ_k γ_k (L_k ρ L_k† - ½{L_k†L_k, ρ}) + Σ_k ξ_k(t) L_k ρ + ξ_k*(t) ρ L_k†
```

where H(θ) is the variational Hamiltonian, L_k are Lindblad operators, and ξ_k(t) are Wiener processes.

## Decoherence Contraction Theorem

A depolarising channel of strength γ over L entangling layers contracts every weight-w Pauli read-out by factor **(1 - 4γ/3)^{wL}**. For weight-1 read-out: **(1 - 4γ/3)^L**.

This transforms the conservative adversarial bound |ΔA| ≤ ∥ε∥/(γ + ∥ε∥) into a predictive, operational law.

## Quantum Dropout vs Depolarising Noise

**Per-gate dropout** (replace variational rotation with identity with probability p):
- Implements curvature-weighted L2 penalty in weight space: (p(1-p)/2) Σ θ² ∂²_θ L
- Maximised at p = 1/2
- Weight-space penalty

**Depolarising noise**:
- Implements output-space penalty
- Same generalisation effect as dropout (statistically indistinguishable)
- But avoids catastrophic robustness collapse under adversarial attacks

## Key Experimental Findings

1. NSL-KDD dataset: depolarising SQNN significantly more robust under strong l∞/l2 attacks (p = 0.04)
2. No catastrophic robustness collapse (classical detectors: 95% → 47%)
3. Robustness variance cut roughly twofold
4. Effect from noise-reshaped training boundary, not attack-time gradient contraction
5. 30-seed study confirms adaptive-penalty formula (p < 10^{-4})
6. Increasing dropout past 1/2 does not help

## Implementation Pipeline

1. Encode input features as initial quantum state (amplitude or angle encoding)
2. Apply L layers of entangling gates + single-qubit rotations
3. Inject depolarising channel during training: D(ρ) = (1-γ)ρ + γ I/d
4. Measure expectation values for classification
5. Train via gradient descent on quantum circuit parameters

## Neutral-Atom Implementation

- Neutral-atom hardware provides native entanglement for ring-topology SQNN
- Rydberg blockade enables programmable entangling gates
- Feasibility analysis available for N = 4-20 qubits

## Pitfalls

- Single-seed studies give misleading conclusions (dichotomy doesn't survive replication)
- Depolarising channel perturbs measured expectation (label noise analogy), not masking subsystems
- Ring entanglement topology essential for non-local anomaly detection (+6 points on XOR-structured data)
- Gradient-trained classical detectors suffer catastrophic robustness collapse under PGD attacks

## References

- arXiv:2606.24219 — Filardo, "Decoherence as Defence" (Neurocomputing, 2026)
- arXiv:2606.28252 — Sonawane et al., "Parameter-Efficient CV Photonic QNN" (2026)
