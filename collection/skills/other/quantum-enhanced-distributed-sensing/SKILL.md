---
name: quantum-enhanced-distributed-sensing
description: "Quantum-enhanced distributed network sensing (DQN) using multiple quantum resources: catalysis, entanglement, and squeezing for multiphase estimation approaching Heisenberg limit. arXiv: 2605.19545."
---

# Quantum-Enhanced Distributed Network Sensing

**arXiv**: 2605.19545 (May 2026)
**Authors**: Rui Zhang, Zi-Yu Zhou, Wen-Quan Yang, Ya-Feng Jiao, Xun-Wei Xu, Le-Man Kuang
**Category**: quant-ph

## Overview

Theoretical scheme for quantum-enhanced distributed network sensing targeting multiphase estimation by leveraging three types of quantum resources (TQRs): quantum catalysis, entanglement, and squeezing.

## Three Types of Quantum Resources (TQRs)

### 1. Quantum Catalysis
- **Partial catalysis** provides stronger precision advantage than global catalysis
- Works in both ideal and noisy regimes
- Enables "loss catalysis dual enhanced sensitivity region" under photon loss

### 2. Entanglement
- Multimode W-type coherent states for distributed sensing
- Combined with catalysis and squeezing for maximum precision

### 3. Squeezing
- Reduces quantum noise below standard quantum limit
- Complements entanglement for multi-parameter estimation

## Key Findings

### Resource Combination Advantage
- Using all 3 TQRs > using only 2 TQRs (both lossless and lossy conditions)
- Precision approaches Heisenberg limit with full TQR combination

### Partial vs Global Catalysis
- Partial quantum catalysis outperforms global catalysis
- Better measurement sensitivity in practical homodyne measurement scheme
- Both exhibit loss catalysis dual enhanced sensitivity under photon loss

### Practical Measurement Scheme
- Homodyne measurement for globally/partially catalyzed multimode W-type coherent states
- Measurement sensitivity approaches corresponding quantum Cramer-Rao bound

## Design Principles

### Hybrid Resource Integration
1. Combine quantum catalysis + entanglement + squeezing
2. Optimize the balance between resources for target precision
3. Prefer partial catalysis over global for practical implementations

### Loss-Tolerant Design
1. Identify "loss catalysis dual enhanced sensitivity region"
2. Design measurement schemes that operate within this region
3. Use homodyne detection as practical measurement backbone

## Activation
quantum distributed sensing, multiphase estimation, quantum catalysis, entanglement squeezing, Heisenberg limit, DQN sensing, homodyne measurement

## Pitfalls
- Partial catalysis requires careful state preparation
- Homodyne measurement must approach quantum Cramer-Rao bound
- Photon loss significantly impacts performance — design for loss tolerance
- Three-resource combination has higher implementation complexity

## Reusable Patterns

### Pattern 1: Multi-Resource Quantum Enhancement
Combine multiple distinct quantum resources (catalysis, entanglement, squeezing) rather than optimizing a single resource. The synergy between resources provides super-additive performance gains.

### Pattern 2: Partial vs Global Resource Allocation
In quantum protocols, partial/local application of resources (e.g., partial catalysis) can outperform global/uniform application. This counterintuitive result holds in both ideal and noisy regimes.

### Pattern 3: Practical Measurement Alignment
Design measurement schemes (e.g., homodyne detection) that can approach theoretical bounds (quantum Cramer-Rao bound) while remaining experimentally feasible.
