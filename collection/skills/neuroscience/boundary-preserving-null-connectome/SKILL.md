---
name: boundary-preserving-null-connectome
description: Use when randomising connectomes/graphs as baselines. Boundary edges decide verdicts.
category: ai_collection
version: "1.0.0"
metadata:
  arxiv_id: "2609.39248"
  published: "2026-09-30"
  authors: "Gyujeong Park (IonLabs)"
  source_title: "Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison"
  categories: "cs.NE, q-bio.NC"
trigger_words:
  - connectome null model
  - randomised wiring baseline
  - degree-preserving edge swap
  - column shuffle null
  - sensory-motor boundary
  - connectome-constrained evolution
  - boundary-preserving null
  - network randomisation confound
---

# Boundary-Preserving Null Models for Connectome Comparisons

**Source**: arXiv:2609.39248 — "Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison" by Gyujeong Park (IonLabs), 2026-09-30

## Overview

A pre-registered evolutionary study showing that the **verdict of connectome-vs-randomised comparisons is decided by what the null preserves at the sensory-motor boundary**, not by interior wiring. Two standard randomisations (column shuffle, degree-preserving edge swaps) route 10.6–10.7% of olfactory output directly onto descending motor groups versus 0.012% in the real fly connectome — creating reactive shortcuts that flip the comparison's outcome in embodied foraging.

## Core Methodology

### Experimental Setup

- **Brain**: compressed adult Drosophila connectome (FlyWire v783): 512 cell-type groups + 1,000 Kenyon cells; 14,989 non-zero signed weights (synapse counts × predicted neurotransmitters); sensory rows zeroed (sensors as transducers); leaky rectified-tanh group dynamics; APL-like inhibition holding 7–9% of Kenyons active; dopamine-gated plastic KC→output matrix reset at birth.
- **Embodiment**: 24 bilateral descending-neuron types read out forward speed/turning/eating; innate feeding reflex.
- **World**: unit square, 24 odor-marked patches (nutritious/toxic/neutral), odor-to-role redrawn every 400-step lifetime; 4 ecologies = {predator P0/P1} × {toxicity T0/T1}; islands of 512 agents, 600 generations, 10 seeds.

### The Confound Discovered

| Wiring condition | Direct olfactory→motor output | Median path sensory→motor |
|---|---|---|
| Connectome | 0.012% | 3 synapses (52 of 53 descending groups ≥2 synapses from olfaction) |
| N1 column shuffle | 10.6% | 1 synapse |
| N2 degree-preserving swaps | 10.7% | 1 synapse |

Standard nulls inject ~1000× more direct sensory-to-motor connectivity than biology has. In a reactive foraging task this is a functional shortcut, so "randomised wiring out-evolves the connectome" is really "our nulls built in a reflex path".

### The Boundary-Preserving Fix

**N4/N5 controls**: keep EVERY edge out of sensory groups and EVERY edge into motor groups; rewire/shuffle only the interior (~90% of interior edges replaced). Result: connectome's end-of-run disadvantage shrinks to within a ±0.10 equivalence bound on seed means (+0.002 / −0.074; robust to a calibration matching activity spread). Per-ecology heterogeneity: interior column shuffle ahead by 0.26 in 1 of 4 ecologies at 10 seeds — **not replicated** by 10 further pre-registered seeds.

### Causal Transplant Experiments (the decisive move)

- **Shortcut transplant** into the connectome: fitness +0.44 (10/10 seeds), olfaction dependence 0.15 → 0.99.
- **Graded doses** raise both fitness and olfaction dependence in step.
- **Interior-only sham** (same swap count, no boundary change): does NOT reproduce it (full dose ahead by 0.53).
- **Boundary sham** (rewires the same boundary edges WITHOUT creating shortcuts): matches the connectome (+0.007) while the full dose is ahead of it by 0.60.

Conclusion: the effect is the shortcut itself, not the number or location of rewired edges.

## Reusable Patterns

1. **Audit what a null actually changes before trusting a comparison**: compute the path statistics of the property under test (here: sensory→motor direct-connection share and path length) in both real graph and every null. A null "preserving degree" can silently change a functionally decisive macro-property by 1000×.
2. **Boundary-preserving null family**: when a network has functional interface classes (sensors/actors, input/output layers, source/sink nodes), freeze ALL edges incident to interface classes and randomize only the interior. This isolates "does interior wiring matter?" from "did the null build a shortcut?"
3. **Transplant + dose-response + double sham**: to prove a structural confound is causal — (a) transplant the confounded property into the real graph (effect should appear), (b) dose it (effect should scale), (c) sham with matched edit count but no property change (effect should vanish), (d) sham on the same edges without the property (effect should vanish).
4. **Pre-registration with equivalence bounds**: register primary endpoint (run-averaged fitness) AND report last-probe differences with 90% CIs on seed means against a ±0.10 equivalence bound — detects "no difference" instead of only "difference".
5. **Replication discipline for per-condition heterogeneity**: a single-ecology lead at 10 seeds gets 10 fresh pre-registered seeds before any claim.

## Activation

connectome null model, randomised wiring baseline, degree-preserving edge swap, sensory-motor boundary, connectome-constrained evolution, boundary-preserving null, network randomisation confound, null model path statistics

## Pitfalls

- The equivalence bound (±0.10) is a **fitness-difference scale**, not a statistical CI — both are needed and they answer different questions.
- Boundary preservation is not "more conservative is better": the standard nulls answer "is the whole wiring special?" while N4/N5 answer "is the interior special given the boundary?" — choose per the hypothesis.
- Compression choices (dropping optic lobe, keeping named descending neurons) deliberately keep the boundary shared across conditions — comparisons are conditional on that compression.
- A null result under boundary-preservation does NOT mean interior wiring is useless in general — only that in these ecologies at this compression, its contribution is within ±0.10 on seed means.
