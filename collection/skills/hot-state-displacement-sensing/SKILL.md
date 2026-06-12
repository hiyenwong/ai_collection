---
name: hot-state-displacement-sensing
description: "Quantum-enhanced displacement sensing using hot (thermal) quantum states without mandatory ground-state cooling. Identifies parity-selection and coherence mechanisms for maintaining sensitivity with mixed states, and formulates optimization comparing cooling vs direct hot-state preparation under decoherence. (arXiv: 2606.13650)"
category: quantum-metrology
metadata:
  arxiv_id: "2606.13650"
  authors: "Piotr T. Grochowski"
  submitted_date: "2026-06-11"
  subjects: "quant-ph"
---

## Context

Quantum-enhanced displacement sensing with bosonic systems traditionally assumes near-ground-state initialization before nonclassical probe preparation. This paper proves that complete cooling is NOT universally optimal — sensitive probes can be generated directly from thermal (hot) states.

## Core Methodology

### Two Mechanisms for Hot-State Sensitivity

1. **Parity Selection**: Projecting a mixed probe onto a definite parity sector removes thermal suppression of displacement quantum Fisher information (QFI), which can INCREASE with initial thermal occupation.

2. **Coherent Superposition**: Superpositions of opposite displacements retain sensitivity through coherence between displaced components, even when the underlying state is mixed.

### Protocol Classification

Hot-state protocols are classified by their sensitivity source:
- **Parity-only**: sensitivity from parity selection
- **Coherence-only**: sensitivity from coherence between displaced components
- **Hybrid**: sensitivity from both mechanisms

### Optimization Framework

Compare initial cooling cost vs. direct hot-state preparation under realistic decoherence:
- Model decoherence as phase damping + amplitude damping channels
- Optimize total QFI per unit time (including cooling overhead)
- Show cooling is suboptimal when: (a) decoherence rate > cooling rate, (b) target displacement amplitude exceeds thermal scale

## Implementation Steps

1. **Hot-State Preparation**: Apply squeezing S(r), number-raising a†, or cat-state generation to thermal input ρ_th(n̄)
2. **QFI Calculation**: Compute displacement QFI F_Q[ρ(α)] for each protocol
3. **Parity Projection**: Apply parity operator Π = (-1)^n̂, compute projected QFI
4. **Decoherence Modeling**: Apply Lindblad master equation with γ_φ, γ rates
5. **Optimization**: Maximize F_Q/T_total where T_total = T_cool + T_prep + T_sense

## Pitfalls

- **Thermal QFI suppression**: Without parity projection or coherence, displacement QFI scales as 1/(2n̄+1) — vanishes for hot states
- **Decoherence dominance**: Hot states are MORE susceptible to phase damping; coherence-based protocols fail when γ_φ T >> 1
- **Not universally better**: Cooling remains optimal when (a) target precision requires ground-state fidelity, (b) decoherence times are long relative to cooling time
- **Cat-state fragility**: Schrödinger cat states from thermal inputs require exponentially large squeezing for large n̄

## Verification

1. Verify parity-projected QFI increases with n̄ for squeezed thermal states
2. Verify cat-state coherence scales as exp(-2|α|²(2n̄+1))
3. Confirm optimization shows cooling suboptimal when γ/κ > threshold
4. Cross-check with experimental parameters from circuit QED systems

## Activation

quantum metrology, displacement sensing, hot quantum states, thermal states, quantum Fisher information, parity projection, bosonic sensing, quantum sensing without cooling, coherence-based sensing