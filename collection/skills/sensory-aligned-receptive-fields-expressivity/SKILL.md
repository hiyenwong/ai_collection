---
name: sensory-aligned-receptive-fields-expressivity
description: Task-aligned receptive fields are a computational prior beyond sparsity; value shrinks as single-neuron expressivity grows. Use for wiring priors in SNNs.
category: ai_collection
---

# Sensory-Aligned Receptive Fields Depend on Neuronal Expressivity

Source: Adorante, Spieler & Levina (U Tübingen / MPI Biol. Cybernetics),
"The Computational Value of Sensory-Aligned Receptive Fields Depends on
Neuronal Expressivity" (arXiv:2609.26940, cs.NE/q-bio.NC, Sept 2026).

## Core Thesis

Receptive fields aligned with task-relevant sensory coordinates are a
**computational prior** — they improve generalization beyond what restricted
connectivity alone delivers, and beyond what generic sparsity can recover.
But this advantage is **capacity-dependent**: as individual neurons become
more expressive (more internal memory timescales), the benefit of structured
input wiring shrinks, converging at high expressivity (full convergence on
SHD, residual gap on DVS-Gesture).

## Experimental Design (reusable pattern)

- **Model**: Expressive Leaky Memory (ELM) network. Each neuron holds M memory
  units with fixed decay timescales spanning orders of magnitude; a small MLP
  per neuron combines synaptic input + memory states → output. M = single-
  neuron expressivity; N (hidden units) = network width. Vary M at fixed N
  and N at fixed M independently.
- **Synaptic budget control**: fixed ds synapses/neuron; fraction ρrec to
  recurrent, remainder to feed-forward. ONLY the feed-forward wiring pattern
  differs between conditions — parameter-count matched.
- **Conditions**:
  - Structured: each unit samples a restricted region of the task-relevant
    sensory coordinate (neighboring frequency channels / one motion-
    direction channel / a retinotopic patch).
  - Random: same number of input synapses, sampled uniformly (no geometry).
  - Full input: every unit sees the entire input (SHD only).
  - Scrambled coordinate: same overlap structure, correspondence to sensory
    space destroyed (key control).
- **Datasets & their task-relevant coordinates**:
  - SHD (spoken digits): frequency bands — 1D cochlear coordinate.
  - DVS-Gesture: motion direction via Hassenstein–Reichardt correlator with
    null-direction opponency (8 cardinal/diagonal channels).
  - CIFAR10-DVS: retinotopic axes (motion is class-shared → task-irrelevant).
- **Statistics**: n=10 seeds per condition, two-sided Welch t-tests with
  Benjamini–Hochberg correction. Unit of analysis = per-network test accuracy.

## Key Findings

1. Structured input beats random across all network sizes on both tasks
   (SHD, DVS-Gesture) at matched parameter count.
2. **Alignment matters, not restriction**: scrambling the coordinate removes
   the advantage; structure along a task-irrelevant coordinate gives none.
   Crossover proof: motion-aligned helps DVS-Gesture but not CIFAR10-DVS;
   spatial structure helps CIFAR10-DVS but not DVS-Gesture.
3. **Expressivity dilutes the prior**: increasing M (memory units) shrinks
   and can eliminate the structured-input advantage; increasing N does not.
   Simple units benefit most from task-aligned selectivity; expressive units
   can compensate for its absence.
4. **Full input overfits**: all-to-all feed-forward input has more capacity
   but LOWER test accuracy and larger train–test gap than structured input.
5. **ℓ1 sparsity regularization** on feed-forward weights: partially recovers
   performance, induces frequency-selective weight concentration (centers
   tracked via 50% cumulative-weight channel), but stays substantially below
   explicitly structured receptive fields. Sparsity alone ≠ structure.
   The emerging fields concentrate where input activity is high (26/128
   neurons receive no feed-forward input at all after regularization).

## Reusable Insights for Architecture Design

- When units are cheap/simple: invest in **task-geometry-aligned input
  wiring** — it is free accuracy at matched parameters.
- When units are expressive (multi-timescale memory): input wiring priors
  matter less; random wiring is acceptable.
- For spiking/event-based pipelines: derive the sensory coordinate first
  (cochlear frequency, Hassenstein–Reichardt motion opponency, retinotopic
  patches), then restrict feed-forward sampling windows to that coordinate.
- Sparsity regularization is a **partial** substitute for structure — useful
  when the task coordinate is unknown, but expect a performance ceiling.
- Conservation principle: computational load distributes between single-neuron
  expressivity and network structure; the two trade off.

## Related Skills

- `neural-receptive-fields-scale-free-geometry` — RF emergence geometry
- `federated-snn-heterogeneous-temporal` — heterogeneous SNN training
- `multi-timescale-conductance-snn` — multi-timescale neuronal dynamics
- `stochastic-plasticity-arbor` — structural plasticity simulation

## Pitfalls

- The advantage is *task-geometry*-dependent: verify the coordinate actually
  carries class information before structuring around it (CIFAR10-DVS motion
  is a negative control).
- Scrambled-coordinate control is essential — it separates "fewer inputs"
  effects from "aligned inputs" effects.
- Full-input comparisons are only feasible on small input spaces (SHD);
  event-camera inputs make all-to-all wiring prohibitive.
