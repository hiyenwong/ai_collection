---
name: hermitian-inner-product-time-axis
description: "Mechanism for time-axis selection in quantum systems via Hermitian inner product choice — identifies the symmetry-breaking step that selects future-timelike axis and locates Born rule as projection onto that axis. Applicable to quantum foundations, Lorentz symmetry emergence from qubit structure, and Hilbert space construction."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2607.05447"
  published: "2026-07-04"
  authors: "Sebastian Zając"
  tags: [quantum-foundations, hermitian-form, born-rule, lorentz-symmetry, qubit, hilbert-space]
---

# Hermitian Inner Product Time Axis Selection

## Description
Resolves the mechanism of time-axis selection in quantum systems: the choice of a Hermitian inner product (positive reference form σ⁰) in passing from normed space to Hilbert space reduces SL(2,C) to SU(2), selecting a future-timelike axis. The Born rule enters one level later as the projection of the state's null vector onto σ⁰ — interpretable as energy in that frame, rescaling as Doppler shift under boosts. Corrects a natural misattribution in recent Lorentz-invariant qubit work.

## Activation Keywords
- hermitian inner product time axis
- born rule mechanism
- Lorentz symmetry from qubit
- time direction selection quantum
- SL2C to SU2 reduction
- quantum foundations time axis
- 厄米内积时间轴
- 波恩规则机制

## Core Concepts

### The Mechanism
1. **Bare spin space** (C², ε) is SL(2,C)-symmetric — singles out no axis
2. **Null cone** it generates also singles out no axis
3. **Hermitian inner product choice** (positive reference form σ⁰) → reduces SL(2,C) to SU(2), the stabilizer of σ⁰
4. **This is the symmetry-breaking step** — made before any probability is assigned
5. **Born rule** = projection of state's null vector onto σ⁰ = energy in that frame
6. **Under boost**: rescales as Doppler shift — frame-dependence of |ψ|² becomes empirical

### Key Distinction
- **Kinematic identification** of the step, NOT dynamical account of why particular axis is selected
- Ingredients are classical; the contribution is identifying them as the mechanism
- Born rule enters one level AFTER Hilbert structure is established

### Mathematical Framework
- 2×2 Hermitian matrices ↔ Minkowski 4-vectors correspondence
- σ⁰ as positive reference form selects future-timelike axis
- ⟨ξ|ξ⟩ = tr(σ⁰ ξξ†) as projection = energy
- Many-qubit case: tuple of such choices

## Instructions for Agents

### Step 1: Context Identification
- When analyzing quantum foundations papers addressing Lorentz symmetry emergence
- When investigating Born rule derivation or mechanism
- When studying qubit-to-spacetime correspondence

### Step 2: Framework Application
1. Identify the bare symmetric structure (SL(2,C) level)
2. Locate the Hermitian inner product choice point
3. Trace the symmetry reduction: SL(2,C) → SU(2)
4. Verify Born rule enters as projection onto selected axis

### Step 3: Critical Analysis
- Distinguish kinematic identification from dynamical explanation
- Check for misattribution of mechanism to wrong step
- For many-qubit systems: account for tuple of Hermitian form choices

## Error Handling
- **Not a dynamical theory**: Does not explain WHY a particular axis is selected, only HOW selection works
- **Not applicable to full spacetime**: Framework addresses internal qubit degrees of freedom, not external spacetime emergence

## Related Skills
- quantum-foundations-probability — Quantum foundations and probability analysis
- transformation-response-quantum-framework — Reformulation of quantum mechanics
