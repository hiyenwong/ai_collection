# Quantum-Attention Hebbian Learning (arXiv:2606.02098)

> Attention-Like Hebbian Learning from Quantum Probability Flow and Quantum-Annealer Tests (June 2026)

## Core Idea

A transverse field Γ defines leakage channels from data states in an associative memory Hamiltonian. Minimizing the measured survival loss yields stability-driven local learning updates — no backpropagation needed.

## Two Dynamics Regimes

### Imaginary-Time Dynamics → Softmax Hebbian Rule

For imaginary-time, dephased dynamics:
```
F_leak = log(Σ_k exp(-ΔE_k))     ← local leakage free energy (log-sum-exp of energy gaps)
Δw_ij ∝ softmax(E_i - E_j) · (x_i · x_j)
```

The gradient of F_leak yields a **softmax-weighted Hebbian rule** — structurally identical to attention mechanisms.

### Real-Time Dynamics → Power-Law Weighting

For real-time stability:
```
Δw_ij ∝ (E_i - E_j)^(-α) · (x_i · x_j)
```

A power-law weighted Hebbian rule with long-range interactions.

## Empirical Validation

Tested on D-Wave quantum annealers (standard anneal + fast-anneal modes) using a one-hot attention forward map:

| Finding | Detail |
|---------|--------|
| Softmax > Power-Law | Imaginary-time dynamics better fitted to annealer data |
| Attention ≈ Hebbian | Attention and Hebbian learning unified under quantum probability flow |
| Physical grounding | Learning rates derived from physical parameters (Γ, ΔE), not hyperparameters |
| Local-only updates | Each synapse updates based on local quantum leakage |

## Implementation Pipeline

1. Encode memory patterns as low-energy states in H_data
2. Apply transverse field Γ for quantum fluctuations
3. Measure survival probability in target state
4. Compute leakage free energy: F_leak = log(Σ exp(-ΔE_k))
5. Apply softmax-weighted Hebbian update: Δw = softmax(ΔE) · x·x^T
6. Validate on D-Wave or simulated annealer

## Pitfalls

- **Annealing schedule matters**: fast-anneal vs standard-anneal give different fits to the softmax model
- **One-hot encoding required**: the forward map assumes one-hot representation for clean quantum dynamics
- **Temperature sensitivity**: imaginary-time dynamics assumes low effective temperature
- **Finite coherence**: real quantum hardware decoherence limits the imaginary-time regime
- **Not a replacement for backprop**: designed for associative memory / energy-based models, not deep supervised networks

## Integration with Existing Methodologies

- **SPATE** (2604.11022): SPATE encodes features into spike trains for quantum circuits; quantum-attention-hebbian provides the learning rule for the quantum circuit weights
- **SQDR-CNN** (2512.03895): Uses surrogate gradients; quantum-attention-hebbian offers a gradient-free alternative for associative memory layers
- **Q-SpiRL** (2605.20801): RL on spiking quantum networks; this methodology provides a principled weight update rule for the memory component
