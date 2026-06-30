---
name: fermionic-shadow-tomography
description: "Fermionic-shadow tomography using random orbital rotations for provably efficient estimation of k-body fermionic correlations with O_k(η^k/ε²) sample complexity independent of system size."
category: quantum
---

# Fermionic Shadow Tomography

## Description
Framework for number-conserving fermionic-shadow tomography based on random orbital rotations. Proves O_k(η^k/ε²) sample complexity for simultaneous estimation of all k-body fermionic correlations, independent of system size N, with matching information-theoretic lower bound.

## Activation Keywords
- fermionic shadow tomography
- particle-number symmetry
- fermionic correlation estimation
- quantum many-body correlations
- random orbital rotations
- shadow tomography fermions
- sample complexity fermionic
- k-body correlation estimation
- quantum state tomography fermions

## Core Concepts

### Problem: Fermionic Correlation Estimation
Predicting local fermionic correlations is central to quantum many-body physics. Particle-number symmetry imposes structural constraints suggesting fewer samples should suffice, but provable advantage was unclear.

### Solution: Number-Conserving Shadow Tomography
1. **Framework**: Random orbital rotations for fermionic-shadow tomography
2. **Sample Complexity**: O_k(η^k/ε²) for all k-body correlations simultaneously
3. **Independence**: Sample count independent of system size N
4. **Optimality**: Matching lower bound Ω_k(η^k/ε²) for any adaptive single-copy protocol
5. **Practical Impact**: ~10x query count reduction for N=100, η=20, ε=10⁻²

## Usage Patterns

### Pattern 1: k-Body Correlation Estimation
For quantum systems with particle-number symmetry:
1. Determine k (correlation order)
2. Determine η (particle count), ε (target variance)
3. Apply random orbital rotations
4. Collect O_k(η^k/ε²) samples
5. Simultaneously estimate all k-body correlations

### Pattern 2: System Size Scaling
- For large N systems: sample complexity independent of N
- Only depends on η (particle count) and k (correlation order)
- Dramatic advantage for sparse systems (η << N)

## Error Handling

### High Particle Density
- When η approaches N, advantage diminishes
- Best suited for sparse fermionic systems
- Consider alternative tomography for dense regimes

### Higher-Order Correlations
- Constants depend on k
- Higher k increases sample requirement polynomially
- Trade-off between correlation order and sample budget

## Resources
- arXiv:2606.30601 - "Provably Efficient Learning of Fermionic Correlations under Particle-Number Symmetry"
- Related: `classical-shadow-estimation`, `quantum-state-fidelity-neural-networks`, `quantum-tomography-retrodiction`
