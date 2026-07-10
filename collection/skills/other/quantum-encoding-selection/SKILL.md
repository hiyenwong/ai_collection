---
name: quantum-encoding-selection
category: quantum-computing
description: Quantum machine learning data encoding selection methodology based on arXiv:2606.05387. Provides a three-axis taxonomy (cost-expressivity-robustness), depth-fidelity bounds under NISQ decoherence, and a five-regime decision framework for choosing optimal encoding strategies.
source: "arXiv:2606.05387"
source_title: "Feature Encoding in Quantum Machine Learning: A Survey and Practical Guidelines"
source_author: "Vincenzo Sammartino"
keywords:
  - quantum machine learning
  - data encoding
  - NISQ
  - amplitude encoding
  - angle encoding
  - barren plateaus
  - quantum kernels
---

# Quantum ML Encoding Selection

## Overview

Systematic methodology for selecting optimal quantum data encoding strategies on NISQ devices. Based on a survey of 66 primary works (2017-2026) with a PRISMA-adapted protocol.

**Trigger**: When designing quantum machine learning pipelines, choosing data encoding strategies, analyzing QML trainability, or optimizing encoding circuits for NISQ hardware.

**arXiv**: 2606.05387 | **Author**: Vincenzo Sammartino

## Core Framework: Three-Axis Taxonomy

Classify all encoding families along three independently measurable axes:

### 1. Cost Axis
- **Gate depth**: Total circuit depth required for encoding
- **Qubit count**: Number of qubits needed (amplitude encoding: log₂(D), basis encoding: D)
- **Classical preprocessing**: Computational overhead before quantum circuit

### 2. Expressivity Axis
- **Fourier expressivity**: Range of frequencies the encoding can represent
- **Feature map rank**: Dimension of the span of encoded states
- **Kernel richness**: Ability to separate data classes in Hilbert space

### 3. Robustness Axis
- **Noise resilience**: Sensitivity to NISQ decoherence channels
- **Barren plateau resistance**: Gradient scaling behavior with qubit count
- **Kernel concentration**: Variance of kernel values under noise

## Encoding Families Reference

| Encoding | Qubits | Depth | Expressivity | NISQ Viable |
|----------|--------|-------|-------------|-------------|
| Basis | D | O(1) | Low | Yes |
| Angle | n | O(n) | Medium | Yes |
| Dense-Angle | n | O(n) | Medium-High | Yes |
| Amplitude | log₂(D) | O(D) | High | Only if p < 10⁻³ |
| Data Re-uploading | n | O(n×L) | Very High | Limited |
| IQP | n | O(n²) | High | Limited |

## Critical Threshold

**Gate-error rate p* ~ 10⁻³** is the critical threshold below which amplitude encoding is viable. For p ≥ 10⁻³ (current NISQ reality), shallow angle-based encodings consistently outperform amplitude encoding despite the latter's exponential qubit advantage.

## Five-Regime Decision Framework

Map (D, n, p, τ) to encoding recommendation:

1. **Low-D, High-p**: Basis encoding (minimal depth, safe)
2. **Medium-D, Medium-p**: Angle/dense-angle encoding (balanced)
3. **High-D, Low-p (< 10⁻³)**: Amplitude encoding (exponential compression)
4. **Complex features, Any-p**: Data re-uploading (iterative expressivity)
5. **Hardware-aware**: IQP encoding when hardware connectivity permits

## Trainability Analysis

Unified treatment of three trainability concerns as functions of encoding circuit:

1. **Barren plateau onset**: Exponential gradient vanishing with qubit count
   - Mitigated by: Local encodings, shallow circuits, structured data
2. **Quantum kernel concentration**: Kernel values collapsing under noise
   - Mitigated by: Encoding depth optimization, noise-aware kernels
3. **Fourier spectrum gaps**: Missing frequency components in feature map
   - Mitigated by: Data re-uploading, hybrid encoding strategies

## Pitfalls

- Amplitude encoding's exponential qubit advantage is nullified by decoherence at current error rates
- Fixed embedding ansatz selection without data geometry analysis leads to suboptimal performance
- Ignoring the cost-expressivity-robustness tradeoff triad results in untrainable circuits
- Wasserstein distance in input space provides an a priori diagnostic for encoding optimization saturation

## Verification Steps

1. Compute gate-error rate p of target hardware
2. If p ≥ 10⁻³, default to angle-based encoding
3. Check barren plateau scaling: verify gradient norm doesn't vanish exponentially
4. Validate kernel concentration: ensure kernel variance remains above noise floor
5. Cross-reference with hardware connectivity for depth optimization
