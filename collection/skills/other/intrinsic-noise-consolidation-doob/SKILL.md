---
name: intrinsic-noise-consolidation-doob
description: "Doob-Barrier-Conditioned Diffusion methodology that turns analog neuromorphic device noise into a continual-learning resource. Casts per-synapse consolidation as a Doob h-transform, creating a noise-amplified restoring force that consolidates memories — predicting an inverted-U relationship between noise level and sequential-task retention."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [neuromorphic, continual-learning, doob-h-transform, device-noise, brainscales2, memory-consolidation, analog-hardware, stability-plasticity]
    category: ai_collection
    arxiv_id: "2607.06924"
    arxiv_url: "https://arxiv.org/abs/2607.06924"
    published: "2026-07-08"
    authors: ["Gunner Levi Howe"]
    categories: ["cs.LG", "cs.NE"]
    trigger_words: ["doob barrier", "h-transform", "intrinsic noise", "consolidation", "analog noise", "neuromorphic hardware", "brainscales", "continual learning", "stability-plasticity", "inverted-u", "device noise"]
created: "2026-07-12"
updated: "2026-07-12"
---

# Intrinsic-Noise Consolidation: A Doob-Barrier-Conditioned Diffusion Turns Analog Device Noise into a Continual-Learning Resource

**arXiv**: 2607.06924 | **Published**: 2026-07-08 | **Author**: Gunner Levi Howe

## Core Thesis

On analog neuromorphic hardware, intrinsic device noise is normally treated as an **accuracy tax**. This paper asks: can it instead **consolidate memories**?

The key insight: cast per-synapse consolidation as a **Doob h-transform** — condition each weight's stochastic dynamics on never crossing a memory-critical barrier around its consolidated value.

### The Math

The conditioned diffusion gains an extra drift term:
```
σ² · d/dw log h(w)
```
This is a **restoring force amplified by the noise variance itself** that diverges at the barrier.

### Key Novelty Claims

1. **Doob barrier-conditioning as a synaptic rule** — every h-transform use found in literature is for generative modeling, none for synaptic consolidation
2. **Falsifiable prediction**: Increasing intrinsic noise **non-monotonically** improves sequential-task retention — an **inverted-U** that anchored-drift methods (OUA, MESU, EWC) cannot produce

## Experimental Results

### Simulation (Split-MNIST, 8 seeds)
- The rule lifts retention **10.9 points** at an interior optimum (paired Wilcoxon p=0.004)
- Matched OU/EWC/MESU anchors are **monotone** (no inverted-U)
- Ablating the conditioning removes the effect
- The optimum tracks the barrier
- The inverted-U survives a second task stream and forward-pass noise

### Hardware (BrainScaleS-2)
- Measured intrinsic noise on real silicon (additive, trial-to-trial independent, tunable via on-chip averaging)
- Barrier-conditioning retains prior task **15.6 points better** than matched control at matched average accuracy
- This is a **stability-plasticity shift**, not a net-accuracy win
- Single seed; retention measured, energy modeled

## Key Insight

**Intrinsic analog noise becomes a consolidation dividend** — a digital accelerator must spend energy to generate what analog hardware gets for free.

## Practical Applications

### 1. Neuromorphic Continual Learning

- Use device noise as a feature, not a bug
- Tune noise levels to find the inverted-U optimum
- Trade off stability vs. plasticity by adjusting the barrier

### 2. Hardware-Aware Algorithm Design

- When deploying on analog chips (BrainScaleS, Loihi analog mode), incorporate noise into the learning rule
- The Doob barrier provides a principled way to protect consolidated memories

### 3. Continual Learning Benchmarking

- Use the inverted-U prediction as a diagnostic: if a method shows monotone behavior, it's likely using anchored drift, not noise conditioning

## Implementation

### Doob Barrier-Conditioned Update Rule

```
dw = -∇L + σ² · d/dw log h(w) - s(w - μ)
      ↑            ↑                  ↑
    gradient    Doob barrier      anchored drift
                restoring force   (surrendered — not novel)
```

The novel contribution is the middle term: the Doob barrier drift.

### Finding the Optimal Noise Level

1. Measure intrinsic noise σ² on your hardware
2. Sweep noise levels (if tunable) or adjust the barrier height
3. Find the interior optimum where retention peaks
4. Expect an inverted-U curve, not monotone improvement

## References

- Howe (2026) — Intrinsic-Noise Consolidation (this paper)
- Pre-registered as a go/no-go gate; passes

## Trigger Words

doob barrier, h-transform, intrinsic noise, consolidation, analog noise, neuromorphic hardware, brainscales, continual learning, stability-plasticity, inverted-u, device noise
