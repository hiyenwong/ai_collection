---
name: doob-barrier-noise-consolidation
description: "Doob-barrier-conditioned diffusion methodology for continual learning — turns analog device noise from an accuracy tax into a memory consolidation resource. Applies Doob h-transform to per-synapse weight dynamics, producing an inverted-U relationship between noise level and sequential-task retention. Validated on real BrainScaleS-2 neuromorphic silicon. arXiv:2607.06924"
---

## Source

**Title**: Intrinsic-Noise Consolidation: A Doob-Barrier-Conditioned Diffusion Turns Analog Device Noise into a Continual-Learning Resource
**Author**: Gunner Levi Howe
**arXiv**: 2607.06924 (July 8, 2026)
**Categories**: cs.LG, cs.NE

## Core Concept

On analog neuromorphic hardware (e.g., BrainScaleS-2), intrinsic device noise is normally treated as an accuracy tax. This paper asks whether it can instead be **steered to consolidate memories**. The answer: yes, via **Doob h-transform** barrier-conditioning of per-synapse stochastic dynamics.

## Key Innovation

### Doob h-Transform as Synaptic Rule

Cast per-synapse consolidation as conditioning each weight's stochastic dynamics on **never crossing a memory-critical barrier** around its consolidated value:

```
Conditioned diffusion gain = σ² · d/dw log(h)
```

Where:
- `σ²` = noise variance
- `h` = probability of never crossing the barrier
- The extra drift is a **restoring force toward the memory** that is **amplified by the noise variance itself** and **diverges at the barrier**

### Falsifiable Prediction: Inverted-U

The load-bearing prediction: increasing intrinsic noise **non-monotonically** improves sequential-task retention (inverted-U curve), which anchored-drift methods (OU, EWC, MESU) **cannot produce** because they are monotone-decreasing in noise.

## Method

### The Rule

Combined drift = anchored consolidation + Doob barrier-conditioning:
- **Anchored drift**: `-s(w - μ)` — not novel (limit of OUA, MESU, EWC)
- **Doob barrier drift**: `σ² · d/dw log(h)` — the novel contribution

### Barrier Parameter

The barrier defines how far a weight can drift from its consolidated value before the restoring force becomes strong. Key hyperparameters:
- Barrier width: how tight the consolidation zone is
- Noise amplitude: the intrinsic noise level (tunable on BrainScaleS-2 via `num_sends`)

### Noise Measurement on Hardware

On real BrainScaleS-2 silicon:
- Noise is **additive** and **trial-to-trial independent**
- Coefficient of variation up to 12.0%
- Tunable via on-chip averaging as `1/√(num_sends)`
- This is the "benign noise class" the mechanism needs

## Results

### Simulation (Split-MNIST, 8 seeds)
- Barrier-conditioned rule lifts retention by **10.9 percentage points** at interior optimum
- Ablating conditioning removes the effect
- Optimum tracks the barrier
- Inverted-U survives device-faithful noise model (colored, multiplicative, fixed-pattern)
- Strongest **rehearsal-free** consolidation method tested (matches MESU, beats OU and EWC)

### Real Hardware (BrainScaleS-2)
- Barrier-conditioning retains prior task **15.6 points better** than matched unconditioned control
- At matched average accuracy — a **stability-plasticity shift**, not a net-accuracy win
- Intrinsic noise steered by barrier-conditioning becomes a **consolidation dividend**

## Applications

- **Neuromorphic continual learning**: Turn hardware noise from liability into asset
- **Analog AI accelerators**: Any system with intrinsic noise can benefit
- **Energy-efficient memory**: Digital accelerators must spend energy to generate noise for consolidation; analog systems get it free
- **Rehearsal-free continual learning**: No data storage needed, unlike plain replay

## Mathematical Detail

### Doob h-Transform

For a diffusion process `dW_t = μ(W_t)dt + σ dZ_t`, conditioning on the event that `W_t` never crosses barrier `B`:

The conditioned process has drift:
```
μ̃(w) = μ(w) + σ² · d/dw log(h(w))
```

Where `h(w)` = probability of never hitting barrier starting from `w`.

For barrier at distance `d` from consolidated value `μ`:
```
h(w) ∝ (d - (w - μ)) for w < d
```

The restoring force `σ² · d/dw log(h)` diverges as `w → d`, preventing memory-critical drift.

### Inverted-U Mechanism

1. **Too little noise**: barrier drift is weak (σ² small) → insufficient consolidation
2. **Optimal noise**: barrier drift strong enough to prevent drift, but not so strong that it prevents learning
3. **Too much noise**: noise overwhelms the barrier → catastrophic forgetting

Anchored methods (OU, EWC, MESU) lack the σ² amplification → monotone decreasing retention with noise.

## Activation

Doob barrier, noise consolidation, continual learning, catastrophic forgetting, analog neuromorphic, BrainScaleS-2, h-transform, intrinsic noise, rehearsal-free learning, stability-plasticity, inverted-U, synaptic consolidation

## Pitfalls

### What this method does NOT do
- It is NOT a net-accuracy improvement — it's a stability-plasticity tradeoff
- The anchored drift component `-s(w-μ)` is not novel (re-derivation of OUA/MESU/EWC)
- Only the Doob barrier-conditioning + the inverted-U prediction are novel claims

### Noise requirements
- Needs **additive, trial-to-trial independent** noise — colored or multiplicative noise may not work as well
- The noise must be tunable to find the optimal operating point
- If hardware noise is too high, no barrier setting will help

### Barrier tuning
- The barrier width must be matched to the noise amplitude
- Too narrow: weights freeze, no learning on new tasks
- Too wide: consolidation is ineffective, forgetting occurs
- The optimal barrier tracks the noise level

### Hardware validation
- Paper validated on single seed, one operating point on BrainScaleS-2
- More extensive hardware validation needed for production use
- Energy modelled, not directly measured

## When to Use

- Building continual learning systems on analog neuromorphic hardware
- Systems with intrinsic noise that must maintain memories across task sequences
- Rehearsal-free learning scenarios where storing data is impractical
- Energy-constrained edge devices where analog noise is available for free
