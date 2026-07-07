---
name: chronic-stress-ei-rnn-resilience
description: Computational modeling methodology for chronic stress as E/I perturbation in recurrent working-memory networks. Identifies enhanced inhibitory-to-excitatory synaptic strength as best-fit mechanism and reveals resilience-generalization trade-off.
tags: [neuroscience, RNN, excitatory-inhibitory, chronic-stress, working-memory, prefrontal-cortex, resilience, Dale-law, EI-balance, dynamical-subspace]
arxiv_id: "2606.27529"
---

# Chronic Stress as E/I Perturbation in Recurrent Working-Memory Networks

## Core Contribution

Systematic computational framework modeling chronic stress as excitatory-inhibitory (E/I) perturbation in recurrent neural networks. Enhanced inhibitory-to-excitatory synaptic strength (W_I→E) best recapitulates three experimental signatures: inhibitory dominance, excitatory hypofunction, impaired performance.

## Key Findings

1. Single Best Stress Mechanism: Of 8 candidate operators, S[W_I→E] best fits experimental data
2. Resilience-Generalization Trade-off: Resilient networks maintain in-distribution performance but lose out-of-distribution generalization, analogous to habit-like behavior in stressed animals
3. Dynamical Conservation: Resilient networks preserve same dynamical subspace and energetic regime with/without stress
4. Energy Signature: Naive networks show -28% to -37% energy reduction under stress; Resilient networks show +2.5% to +5.7% increase

## Methodology

### Network Architecture
- All-to-all connected RNN with Dale's law constraint
- N_E excitatory + N_I inhibitory neurons
- Each neuron's outgoing synapses are purely excitatory or purely inhibitory

### Stress Operators (8 tested)
1. S[W_I→E]: ↑ inhibitory→excitatory weights ← BEST FIT
2. S[W_E→I]: ↑ excitatory→inhibitory weights
3. S[W_E→E]: ↓ excitatory→excitatory weights
4. S[W_I→I]: ↓ inhibitory→inhibitory weights
5. S[r_I]: ↑ inhibitory activity
6. S[r_E]: ↓ excitatory activity
7-8. Combined operators

### Training Protocols
- Naive: Task training only
- Resilient: Task training + simultaneous stress application (stress inoculation)

### Analysis Metrics
- Trajectory displacement (lower = more stable)
- Subspace preservation ρ (higher = more conserved)
- Synaptic cost decomposition: S_E→E, S_I→E, S_E→I, S_I→I
- Delay generalization: within-distribution vs. out-of-distribution

## Key Results

Network Energy Comparison:
- Naive baseline: 0.845, stress δ=0.25: 0.501 (-41%), stress δ=0.5: 0.390 (-54%)
- Resilient baseline: 0.729, stress δ=0.25: 0.680 (-7%), stress δ=0.5: 0.652 (-10%)

Inhibitory synaptic cost (S_I→E):
- Naive: -28.4% to -36.7% change
- Resilient: +2.5% to +5.7% change

## Biological Interpretation

- Chronic stress shifts medial PFC toward inhibitory dominance, weakening cognitive control
- Stress inoculation preserves dynamical regime but promotes specialized/rigid solutions
- Maps to animal findings where stressed animals show habit-like, inflexible behavior
- Trade-off persists across stress magnitude (p=0.039) and network size (p=1.6×10⁻⁶)

## Implementation

- Python, JAX, Optax
- Dale's law: W[i,:] ≥ 0 for excitatory, ≤ 0 for inhibitory neurons
- Working memory task: compare S1 vs S2 with variable delay
- 8-layer Transformer encoder, 6-layer decoder
- Hidden dimension: 1024

## Pitfalls

1. Don't assume single mechanism - test multiple stress operators systematically
2. Don't ignore generalization - resilience at one scale may impair another
3. Energy analysis crucial - distinguishes naive vs resilient network strategies
4. Dale's law constraint essential - unconstrained networks don't capture E/I biology

## Activation

chronic stress, E/I balance, prefrontal dysfunction, working memory deficits, stress resilience, inhibitory dominance, Dale's law RNN, dynamical subspace preservation, stress inoculation, behavioral rigidity, excitatory-inhibitory perturbation