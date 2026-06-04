---
name: fermionic-bell-sampling-non-gaussianity
description: "Fermionic non-Gaussianity analysis via Bell sampling — bridge degree monotone, Gaussian conversion no-go theorems, and efficient quantum algorithms for certifying non-Gaussian cost of state preparation."
category: quantum
---

# Fermionic Non-Gaussianity via Bell Sampling

## Context

Based on arXiv:2606.05066 (Tarabunga, Jun 2026). Fermionic non-Gaussianity is an essential resource for unlocking the full computational power of fermionic quantum platforms.

## Core Methodology

1. **Define the operator** Λ = Σ_{j=1}^{2n} γ_j ⊗ γ_j on two copies of an n-mode fermionic state, accessible via Bell sampling
2. **Bridge degree**: Introduce the bridge degree as the largest eigenvalue sector of Λ populated by two copies of the state — a novel non-Gaussianity monotone
3. **Prove monotonicity**: Show bridge degree is non-increasing under post-selected Gaussian protocols
4. **Derive no-go theorems**: Use monotonicity to prove stronger Gaussian conversion impossibility results than previously known monotones
5. **Irreversibility**: Show the resource theory of fermionic non-Gaussianity is irreversible in the exact-conversion setting
6. **Efficient witnessing**: The bridge degree is efficiently witnessed through Bell sampling with polynomial sample complexity
7. **Two algorithmic primitives**:
   - Two-copy Gaussianity test with perfect completeness (optimal among two-copy tests)
   - Test for state 2-design property of matchgate-invariant ensembles

## Implementation Steps

1. Prepare two copies of the target fermionic state
2. Perform Bell sampling to access the eigenvalue structure of Λ
3. Compute the bridge degree from the Bell sampling outcomes
4. Compare against known Gaussian states to certify non-Gaussianity
5. Use the approximate variant with efficiently measurable lower bound for experimental certification

## Key Results

- Bridge degree is easy to compute and efficiently witnessed through Bell sampling
- Lower-bounds the non-Gaussian gate complexity of state preparation
- Controls the non-Gaussian gate complexity of producing quantum state designs
- Extends naturally to mixed states via Choi–Jamiołkowski isomorphism
- Provides experimentally certifiable lower bound on non-Gaussian cost of approximately preparing any state

## Pitfalls

- Post-selected Gaussian protocols only: monotonicity holds under post-selection, not unconditional Gaussian operations
- The bridge degree is defined for even pure states; extension to mixed states requires Choi isomorphism
- Two-copy tests share the perfect completeness property; single-copy tests may have different completeness bounds

## Verification

- Verify bridge degree computation against known Gaussian states (should yield zero for Gaussian states)
- Test monotonicity: apply post-selected Gaussian protocol, verify bridge degree does not increase
- Compare with existing non-Gaussianity monotones to confirm stronger no-go theorems

## Activation

- fermionic non-gaussianity, bell sampling, bridge degree, gaussian conversion, fermionic quantum computing
- 费米子非高斯性, 贝尔采样, 桥接度, 高斯转换
