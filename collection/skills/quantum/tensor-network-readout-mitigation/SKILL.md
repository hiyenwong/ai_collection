---
name: tensor-network-readout-mitigation
description: "Tensor network (MPO) framework for characterizing and mitigating correlated readout errors in quantum processors. Use when modeling readout noise beyond uncorrelated approximations, estimating nonlocal observables with correlated measurement errors, or integrating readout mitigation with quantum error correction decoders. Triggers: tensor network readout, MPO readout error, correlated measurement error, readout mitigation, matrix product operator calibration, classical shadows readout, noise-aware quantum data processing."
metadata:
  arxiv_id: "2606.25974"
  published: "2026-06-24"
  authors: "Yuchen Guo, Shuo Yang"
  tags: [quantum, tensor-network, readout-error, MPO, error-mitigation, scalability]
---

# Tensor Network Readout Error Mitigation

## Core Concept

Model quantum readout errors as a **Matrix Product Operator (MPO)** rather than assuming independent single-qubit errors. This captures spatial correlations in measurement noise with sample cost growing only near-linearly in system size, versus exponential for full correlation models.

## When to Use

- Readout error mitigation on processors with correlated measurement noise
- Nonlocal observable estimation with noisy measurements
- Classical shadows or tomography protocols with correlated readout errors
- Integration with tensor-network QEC decoders for joint data+readout inference

## MPO Readout Model

### Step 1: Model the Readout Process

The noisy measurement process is modeled as:

```
P(noisy outcome | true state) = Tr[MPO · ρ_true]
```

Where the MPO encodes correlated bit-flip errors across qubits with bond dimension χ controlling the correlation range.

### Step 2: Train via Likelihood Optimization

1. Collect calibration data: prepare known states, record noisy readout outcomes
2. Optimize MPO tensors to maximize likelihood of observed outcomes
3. Bond dimension χ is a hyperparameter — larger χ captures longer-range correlations

### Step 3: Apply to Target Tasks

The trained MPO readout model supports:

- **Nonlocal observable estimation**: Correct expectation values by inverting the MPO channel
- **Random circuit sampling**: Debias output distributions using MPO-inferred true probabilities
- **Classical shadows**: Modify shadow reconstruction to account for correlated measurement noise
- **Learning-based tomography**: Joint inference over state and readout errors

### Step 4: Scale to 2D Systems

For 2D qubit arrays:
- Use PEPO (Projected Entangled Pair Operator) generalization of MPO
- Integrate with tensor-network QEC decoders for joint inference over syndrome data and readout errors

## Key Results

- Sample complexity scales **near-linearly** with system size (vs exponential for full correlation)
- Captures correlated errors that uncorrelated tensor product models miss
- Validated on superconducting processors up to 20 qubits
- Compatible with classical shadows, randomized measurement protocols, and QEC decoding

## Implementation Workflow

```
Calibration data → MPO likelihood optimization → Trained MPO model
  → Task-specific application (observable estimation / shadows / tomography / QEC)
```

1. Prepare calibration states (computational basis states or random states)
2. Collect noisy readout outcomes for each calibration state
3. Optimize MPO bond dimension and tensor parameters via maximum likelihood
4. Validate model on held-out calibration data
5. Apply to target quantum computation by correcting measurement outcomes

## Pitfalls

- **Bond dimension selection**: Too small χ misses correlations; too large χ overfits and increases computation. Use cross-validation on calibration data.
- **Calibration overhead**: Requires O(N·χ²) calibration measurements — manageable but non-negligible for large N.
- **Temporal drift**: Readout error models drift over time — recalibrate periodically.
- **2D scaling**: PEPO generalization increases computational complexity significantly vs 1D MPO.

## Related Skills

- `quantum-error-correction-methods` — General QEC patterns
- `quantum-fault-tolerance-benchmark` — QEC benchmarking
- `speculative-window-decoder-qec` — QEC decoding strategies
- `classical-shadow-unitary-channel-estimation` — Classical shadow protocols
