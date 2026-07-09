---
name: intrinsic-noise-consolidation-doob
description: "Doob h-transform barrier-conditioned diffusion for continual learning on analog neuromorphic hardware. Converts intrinsic device noise from accuracy tax to consolidation dividend. Activation: Doob h-transform, barrier conditioning, analog noise, neuromorphic continual learning, BrainScaleS-2, intrinsic noise consolidation, inverted-U retention"
metadata:
  arxiv_id: "2607.06924"
  published: "2026-07-08"
  authors: "Gunner Levi Howe"
  tags: [neuromorphic, continual-learning, doob-h-transform, analog-noise, brain-scale-s-2, synaptic-plasticity]
---

# Intrinsic-Noise Consolidation via Doob Barrier-Conditioned Diffusion

## Core Innovation

Transform analog neuromorphic device noise from an accuracy tax into a memory consolidation resource using Doob h-transform barrier conditioning. The conditioned diffusion acquires a restoring force σ²∂_w log h that is **amplified by the noise variance itself** and diverges at memory-critical barriers.

## Key Theoretical Contribution

### Doob h-Transform as Synaptic Rule
- Cast per-synapse consolidation as conditioning weight dynamics on never crossing memory-critical barrier at μ±b
- Ground-state h-transform: h(w) = cos(π(w-μ)/2b)
- Conditioned drift: σ²∂_w log h(w) — noise-powered restoring force
- Barrier half-width: b_i = b₀/√(1 + s_i/median(s)) — high-Fisher synapses get tight barriers

### Novelty Claims (Explicit)
1. **Doob barrier-conditioning as synaptic rule** — first use in synaptic/plasticity/continual-learning (all prior h-transform uses are generative modeling or Schrödinger bridges)
2. **Falsifiable prediction**: intrinsic noise non-monotonically improves sequential-task retention (inverted-U curve) — anchored-drift methods (OU, EWC, MESU) cannot produce this

### What is NOT Novel
- Anchored drift term -s(w-μ) is small-noise limit of OUA/MESU/EWC — explicitly surrendered as re-derivation

## Methodology

### Weight Dynamics (Euler-Maruyama)
```
dw = [-s(w-μ) + σ²∂_w log h(w)]dt + σ dW
```
- First term: anchored drift (known from OUA/MESU/EWC)
- Second term: Doob barrier conditioning (novel)
- All methods receive identical injected noise at matched σ

### Experimental Validation
- **E0-E4 (GPU emulation)**: Split-MNIST domain-incremental, 5 binary tasks, MLP 784-100-100-2
  - Retention inverted-U: 10.9 pts lift at σ*=0.02 (p=0.004, 8 seeds)
  - OU/EWC/MESU anchors are monotone-decreasing in noise
  - Ablating conditioning (κ:1→0) flattens curve — effect is from conditioning, not generic noise
  
- **E2 (Device-faithful)**: BSS-2 noise model (colored AR(1) + multiplicative + fixed-pattern + 6-bit quantization)
  - Inverted-U survives on continual Yin-Yang benchmark
  
- **E5 (Real silicon measurement)**: BrainScaleS-2 chip hxcube7fpga3chip61_1
  - Intrinsic noise is additive, trial-to-trial independent
  - CV up to 12.0%, num_sends knob averages as ≈1/√N
  - Benign noise class at reachable amplitude
  
- **E7 (On-chip training)**: Real BrainScaleS-2 with analog MAC in training loop
  - Chip's own intrinsic noise + barrier conditioning retains prior task 15.6 pts better than unconditioned control
  - Single-seed proof of concept; retention measured, energy modeled

### Baselines
- OUA (Ornstein-Uhlenbeck Adaptation)
- EWC (Elastic Weight Consolidation)
- MESU (Bayesian continual learning)
- Benna-Fusi complex synapses
- Plain replay (stores data, lacks mechanism)

## Key Results

1. **Inverted-U retention curve**: Noise helps retention up to optimum σ*, then hurts — unique to barrier-conditioned rule
2. **Rehearsal-free**: Strongest rehearsal-free consolidation method tested (ties MESU, beats OU/EWC)
3. **Energy argument**: Analog substrate pays no energy to generate noise (it's intrinsic); digital accelerator must spend energy to inject it
4. **Hardware validation**: Mechanism works on real BrainScaleS-2 silicon with device's own noise

## Pitfalls

### Pre-Registration as Go/No-Go Gate
The inverted-U prediction was pre-registered as a hard go/no-go gate. If noise did not help retention beyond unconditioned anchor, the mechanism reduces to OUA/MESU and there is no paper. It passed.

### Single-Seed On-Chip Result
E7 (real silicon training) is single-seed, one operating point. Retention measured, energy modeled but not directly measured. Replication across seeds and chips needed.

### Emulation vs. Silicon
E0-E4 are GPU emulations. E2 uses device-faithful noise model but is still emulation. Only E5 (noise measurement) and E7 (on-chip training) are real-silicon results.

### Fair Comparison
All methods receive identical injected noise at matched σ. Methods differ only in drift term. This isolates barrier conditioning effect rather than generic noise effect.

## Applications

- **Analog neuromorphic hardware**: BrainScaleS-2, other analog accelerators with intrinsic noise
- **Continual learning**: Sequential task retention without rehearsal
- **Energy-efficient consolidation**: Leverage intrinsic noise instead of injecting artificial noise
- **Stability-plasticity balance**: Barrier conditioning provides tunable trade-off

## Related Work

- **OUA** (Garcia Fernandez et al., 2024): Mean-reverting OU diffusion — exactly the anchored drift term, but no barrier or first-passage conditioning
- **MESU** (Bonnet et al., 2025): Bayesian continual learning with variance-scaled anchor — treats device read-noise as sampling resource, never as retention optimum
- **EWC** (Kirkpatrick et al., 2017): Static Fisher-weighted quadratic anchor — deterministic ancestor
- **ANV** (Xie et al., 2021): Injects artificial neural variability to reduce forgetting — but variability is injected (digital regularizer), benefit is monotone, no barrier
- **Benna-Fusi** (2016): Multi-timescale cascade synapses — consolidates without barrier via deterministic cascade

## References

- arXiv:2607.06924 — Full paper with proofs, experimental details, and energy model
- BrainScaleS-2: Pehle et al., 2022; Weis et al., 2020
- Doob h-transform: Classical stochastic process theory
- Continual learning benchmarks: Split-MNIST, Yin-Yang (Kriener et al., 2022)
