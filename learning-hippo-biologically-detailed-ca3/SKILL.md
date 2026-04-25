---
name: learning-hippo-biologically-detailed-ca3
version: 1.0.0
description: Biologically detailed CA3 auto-associative memory model extending Hopfield/Marr with 10 populations, 47 compartments, 5 plasticity rules, and cholinergic modulation. Demonstrates multi-attractor dynamics absent from minimal baselines.
date: 2026-04-23
source: arXiv:2604.20679
authors: Daniele Corradetti, Renato Corradetti
tags: [hopfield, hippocampus, CA3, auto-associative-memory, attractor-dynamics, multi-attractor, biological-plausibility, Hebbian-learning, BCM, cholinergic-modulation, inhibitory-interneurons, pattern-completion]
activation: hippocampus, CA3, Hopfield, attractor memory, auto-associative, pattern completion, multi-attractor, biological detail, Marr
---

# Learning Hippo: Biologically Detailed CA3 Auto-Associative Memory

## Overview
Biologically detailed extension of the classical Hopfield/Marr auto-associative memory model for hippocampal region CA3. Implements ten neural populations with 47 compartments and multi-rule plasticity, demonstrating three qualitative signatures absent from minimal Hopfield baselines.

**arXiv:** 2604.20679v1 [cs.NE] | **Submitted:** 22 April 2026

## Core Architecture

### Neural Populations (10 total)
- **2 pyramidal subtypes** (asymmetric)
- **8 GABAergic interneuron classes** — matching biological CA3 diversity

### Compartments
- **47 compartments** per neuron model — enabling dendritic computation

### Multi-Rule Plasticity (5 mechanisms)
1. **Recurrent Hebb** — standard associative learning at recurrent synapses
2. **BCM anti-saturation** — Bienenstock-Cooper-Munro rule preventing runaway excitation
3. **Mossy-fiber short-term plasticity** — DG→CA3 pathway dynamics
4. **Endocannabinoid iLTD** — inhibitory long-term depression via retrograde signaling
5. **Burst-gated Hebb** — Hebbian learning gated by burst patterns

### Cholinergic Modulation
- **Bimodal cholinergic cycle**: encoding mode (high ACh) vs. consolidation mode (low ACh)
- Implements theta/gamma rhythm-dependent memory processing

## Key Results — Three Qualitative Signatures

### 1. Multi-Attractor Cross-Seed Behavior
- At K=5 stored patterns with biologically realistic inhibitory proportions
- 2 of 5 seeds converge to positive attractors with margin +0.10–0.22
- Effect size: Cohen's d=0.71, one-sided p=0.08
- **Absent** from minimal Hopfield baseline

### 2. Target-Selective Associative Recall
- Paired (A, B) memory at K≥5 stored patterns
- Full model retrieves B from partial cue of A (true associative recall)
- Minimal model echoes A (pattern completion, not association)
- Pearson margin Δ=+0.163 at K=5

### 3. Reduced Cross-Seed Variance
- Full model variance below minimal baseline under clean upstream input
- Variance ratios: 1.0–3.0 (full model lower)
- Indicates more robust attractor basins

## Evaluation Protocols
- **Auto-associative** — pattern completion from partial cues
- **Associative** — paired (A,B) recall across patterns
- **Temporal** — sequential pattern recall
- **Inhibitory-proportion manipulation** at N=256 neurons — systematic sweep of inhibition levels

## Methodological Contributions

### Biological Plausibility Checklist
- [x] Multiple interneuron types (8 GABAergic classes)
- [x] Asymmetric pyramidal subtypes
- [x] Dendritic compartments (47 per neuron)
- [x] Multiple plasticity mechanisms (5 rules)
- [x] Cholinergic neuromodulation
- [x] Realistic inhibitory proportions

### Architecture-Specific Signatures
All three signatures appear consistently across independent evaluation regimes and are absent from minimal control — demonstrating that biological detail is *functionally necessary*, not merely cosmetic.

## Implementation Guide

### Model Parameters
```
N = 256 neurons (evaluated)
K = 5+ stored patterns
Populations = 10 (2 pyramidal + 8 interneuron)
Compartments = 47 per neuron
Plasticity rules = 5 (Hebb, BCM, STP, iLTD, burst-gated)
Cholinergic modes = 2 (encode, consolidate)
```

### Key Design Decisions
1. **Inhibitory proportion** is a critical parameter — multi-attractor behavior emerges only at biologically realistic ratios
2. **BCM rule** prevents saturation while maintaining selectivity
3. **Endocannabinoid iLTD** enables dynamic inhibitory balance adjustment
4. **Burst-gating** implements behavioral relevance filtering

## Comparison: Full vs. Minimal Hopfield

| Feature | Minimal Hopfield | Learning Hippo |
|---------|-----------------|----------------|
| Populations | 1 (binary units) | 10 (2 pyr + 8 GABA) |
| Compartments | 0 | 47 |
| Plasticity rules | 1 (Hebb) | 5 |
| Neuromodulation | None | Cholinergic (bimodal) |
| Multi-attractor cross-seed | No | Yes (K=5) |
| Target-selective recall | No | Yes (Δ=+0.163) |
| Variance robustness | Baseline | Below baseline |

## Relevance and Applications

### Computational Neuroscience
- Demonstrates *minimum biological complexity* needed for multi-attractor dynamics
- Provides ground truth for simplified models — which biological details are essential?

### Neuromorphic Engineering
- Multi-compartment, multi-population design is implementable in hardware
- Cholinergic gating translates to mode-switching circuits
- BCM rule provides inherent homeostatic regulation

### Brain-Inspired AI
- Associative memory beyond simple pattern completion
- Multi-attractor landscapes enable richer memory representations
- Burst-gated learning translates to attention-gated learning in artificial systems

## Pitfalls and Limitations
- N=256 is small — scaling behavior unknown
- Single-region model (CA3 only, no EC/DG/subiculum)
- No spike-timing dependent plasticity (STDP) in current version
- Cholinergic modulation is simplified (binary, not continuous)
- p=0.08 for cross-seed effect is marginal significance

## Key Takeaway
> Biological detail matters. Multi-attractor dynamics, target-selective recall, and robust variance are emergent properties that require the full architecture — they cannot be recovered by tuning a minimal Hopfield network.

## References
- Corradetti and Corradetti (2026). "Learning Hippo: Multi-attractor Dynamics and Stability Effects in a Biologically Detailed CA3 Extension of Hopfield Networks." arXiv:2604.20679
- Hopfield (1982). "Neural networks and physical systems with emergent collective computational abilities."
- Marr (1971). "Simple memory: a theory for archicortex."
- Bienenstock, Cooper, Munro (1982). "Theory for the development of neuron selectivity."
