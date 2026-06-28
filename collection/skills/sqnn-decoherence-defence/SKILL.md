---
name: sqnn-decoherence-defence
description: "Stochastic Quantum Neural Networks (SQNNs) adversarial robustness methodology. Decoherence-contraction theorem for depolarising channels, per-gate dropout as curvature-weighted L2 penalty, and noise-as-defence framework for quantum machine learning. Use when: SQNNs, quantum adversarial robustness, quantum dropout, decoherence contraction, Lindblad master equation, neural network security."
metadata:
  arxiv_id: "2606.24219"
  published: "2026-06-23"
  authors: "Gautier-Edouard Filardo"
  tags: [quantum, machine-learning, adversarial-robustness, sqnn, decoherence]
---

# SQNN Decoherence as Defence

## Description

Stochastic Quantum Neural Networks (SQNNs) encode neuronal activations as qubits, synaptic topology as entanglement, and neural noise through a Lindblad master equation. This methodology proves that decoherence acts as adversarial defence rather than degradation.

## Activation Keywords
- sqnn decoherence defence
- stochastic quantum neural network robustness
- quantum dropout
- decoherence contraction theorem
- depolarising channel regularisation
- quantum adversarial robustness
- lindblad master equation neural
- per-gate stochastic deactivation

## Core Contributions

### 1. Decoherence-Contraction Theorem

A depolarising channel of strength γ over L entangling layers contracts every weight-w Pauli read-out by factor:

```
(1 - 4γ/3)^(wL)
```

For weight-1 read-out: `(1 - 4γ/3)^L`

**Key insight**: Depolarising noise reshapes the training boundary rather than contracting attack-time gradients. This prevents catastrophic robustness collapse seen in noiseless circuits.

### 2. Per-Gate Dropout as Curvature-Weighted L2 Penalty

Per-gate dropout implements:

```
p(1-p)/2 × Σ θ² ∂²_θ L
```

in weight space, maximised at p=1/2. Depolarising noise implements an output-space penalty instead.

**Practical result**: Both mechanisms reduce train-test gap by ~0.01 (p<10⁻⁴), statistically indistinguishable. Effect concentrated where overfitting is largest.

### 3. Empirical Validation

- NSL-KDD dataset under FGSM and PGD attacks
- 30-seed study confirms dropout formula prediction
- Increasing dropout past 1/2 does not help
- Noiseless models fall from 95% to 47% under PGD-20; SQNN never suffers catastrophic collapse

## Usage Workflow

### Step 1: SQNN Architecture Design

1. Encode neuronal activations as qubits
2. Map synaptic topology to entanglement structure
3. Choose ring topology for non-local anomaly detection

### Step 2: Noise Mechanism Selection

| Mechanism | Effect | Best For |
|-----------|--------|----------|
| Depolarising (γ) | Output-space penalty | General robustness |
| Per-gate dropout (p) | Curvature-weighted L2 | Overfitting prevention |
| Combined | Both penalties | Maximum robustness |

### Step 3: Training with Noise-as-Defence

1. Apply depolarising channel during training (not just inference)
2. Set dropout rate p ≤ 0.5 (optimal at p=1/2)
3. Monitor robustness variance (should decrease ~2×)
4. Validate under white-box FGSM and PGD attacks

### Step 4: Neutral-Atom Realisation

For hardware deployment:
- Map SQNN to neutral-atom architecture
- Perform feasibility analysis by N qubits
- Account for native gate set and connectivity

## Pitfalls

1. **Depolarising ≠ dropout**: Depolarising channel acts as output noise, not dropout-style regulariser. Use per-gate dropout for weight-space effects.
2. **Optimal dropout at p=0.5**: Increasing beyond 0.5 does not improve generalisation.
3. **Single-seed results unreliable**: Prior work with single seeds showed false dichotomy; use 30+ seeds.
4. **Robustness from boundary reshaping**: Robustness comes from noise-reshaped training boundary, not gradient contraction during attack.

## Related Skills
- `stochastic-quantum-neural-network` — SQNN basics (arXiv:2511.11609)
- `qmt-quantum-measurement-temperature` — QNN training stability (arXiv:2606.22551)
- `qpinn-integro-fractional-pde` — QPINN methodology (arXiv:2606.26865)
- `qml-adversarial-robustness-sok` — QML robustness SoK
