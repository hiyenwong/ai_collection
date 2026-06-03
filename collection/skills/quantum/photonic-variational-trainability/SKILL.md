---
name: photonic-variational-trainability
description: >
  Pre-asymptotic trainability analysis for photonic variational quantum circuits under
  postselection. Covers barren plateau dynamics in passive linear-optical circuits,
  Lie algebra dimension scaling, postselection-induced gradient concentration
  (allow-bunching, collision-free, dual-rail), and design guidance for near-term
  photonic variational architectures. Use when: analyzing photonic QNN trainability,
  designing variational photonic circuits, understanding gradient concentration under
  postselection, or comparing postselection regimes for optical quantum computing.
  Trigger keywords: photonic barren plateau, variational photonic circuits, postselection
  gradient concentration, linear optical quantum computing, dual-rail postselection,
  collision-free filtering, photonic QNN trainability.
---

# Photonic Variational Trainability

From arXiv:2605.11879 "Pre-Asymptotic Trainability in Photonic Variational Circuits under Postselection" (Xie, Notton, Senellart, 2026).

## Core Problem

Barren plateaus in variational quantum circuits cause gradient variance to vanish
exponentially with system size. Passive photonic circuits challenge this picture:
although their Hilbert space is exponentially large, dynamics are constrained to a
Lie algebra of dimension O(m²) where m = number of modes.

## Key Finding: Postselection Determines Trainability

Gradient concentration is governed not by Hilbert-space dimension but by how
postselection reshapes the effective observable.

### Three Postselection Regimes

| Regime | Gradient Scaling | Trainability |
|--------|-----------------|--------------|
| **Allow-bunching** | Polynomial decay | ✅ Trainable |
| **Collision-free filtering** | Polynomial decay | ✅ Trainable |
| **Dual-rail postselection** | Exponential concentration | ❌ Barren plateau |

### Mechanism

1. **Allow-bunching**: No postselection filtering → full Lie algebra access
   - Gradient variance ~ O(1/poly(m))
   - Remains trainable for moderate system sizes

2. **Collision-free filtering**: Post-select on no two photons in same mode
   - Restricts accessible subspace but preserves polynomial scaling
   - Trainability maintained across initialization ensembles

3. **Dual-rail postselection**: Encode qubits in dual-rail basis, post-select
   - Induces exponential gradient concentration beyond moderate m
   - Robust across three initialization ensembles tested
   - **Critical insight**: dual-rail encoding + postselection = barren plateau

## Design Guidelines for Photonic Variational Architectures

### When Trainability is Expected
- Use allow-bunching or collision-free regimes
- Keep observable support localized (few-body operators)
- Avoid dual-rail postselection for variational training

### When to Expect Barren Plateaus
- Dual-rail encoding with postselection beyond moderate system sizes
- Global observables spanning many modes
- Deep circuits with extensive mode mixing

## Practical Recommendations

1. **Initialization matters**: Results robust across three ensembles, but
   initialization choice affects pre-asymptotic behavior
2. **Observable choice**: Local observables preserve trainability longer
3. **Mode count**: Polynomial regime extends to moderate m (tested up to ~20 modes)
4. **Postselection geometry**: The shape of the postselected subspace, not just
   its dimension, determines gradient behavior

## Pitfalls

- Assuming photonic circuits are immune to barren plateaus — dual-rail
  postselection DOES cause exponential concentration
- Extrapolating small-system behavior: polynomial scaling eventually breaks
- Ignoring observable structure: global observables accelerate concentration

## Related Patterns

- See `quantum-neural-barren-plateau` for general QNN barren plateau mitigation
- See `photonic-qnn-algorithmic-advantage` for photonic QNN expressivity analysis
