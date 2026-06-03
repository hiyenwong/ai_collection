---
name: quantum-dl-feasibility-assessment
description: >
  Assess whether Quantum Deep Learning (QDL) approaches can practically deliver
  advantages given current and projected hardware constraints. Based on systematic
  survey of quantum algorithms mapped to deep learning applications. Use when:
  (1) Evaluating QDL proposals for practical viability, (2) Estimating qubit/gate
  requirements for quantum neural networks, (3) Deciding between quantum vs classical
  approaches for ML tasks, (4) Research planning in quantum machine learning.
  Triggers: quantum deep learning feasibility, QDL assessment, quantum advantage timeline,
  NISQ deep learning, qubit requirements, quantum leap analysis.
---

# Quantum Deep Learning Feasibility Assessment

## Overview

Evaluate QDL proposals against a structured feasibility framework based on the
three-category taxonomy from "Quantum Deep Learning Still Needs a Quantum Leap"
(arxiv:2511.01253):

1. **Exponential speedup proposals** — theoretically promising but require
   fault-tolerant quantum computers (FTQC) with millions of logical qubits
2. **Variational quantum algorithms (VQAs)** — NISQ-compatible but face
   barren plateaus, optimization difficulties, and limited expressivity
3. **Quantum algorithms for DL primitives** — potential advantages for specific
   subroutines (linear algebra, sampling) but often require QRAM or FTQC

## Assessment Framework

### Step 1: Categorize the Proposal

Classify into one of three categories above. Most QDL papers fall into category 2
or 3. Category 1 proposals require ~10^6+ logical qubits.

### Step 2: Estimate Resource Requirements

| Resource | NISQ-era (2025-2030) | FTQC-era (2035+) |
|----------|---------------------|------------------|
| Logical qubits | < 1,000 | 10^4 - 10^7 |
| Circuit depth | < 1,000 gates | 10^6+ gates |
| Error rate | 10^-3 (physical) | 10^-15 (logical) |
| QRAM | Not available | Potentially available |

### Step 3: Identify Key Bottlenecks

- **Barren plateaus**: Gradients vanish exponentially with qubit count in
  deep variational circuits
- **Data loading**: O(N) classical-to-quantum encoding erases theoretical
  speedups for many algorithms
- **Measurement overhead**: ~O(1/ε²) shots needed for ε-precision estimation
- **Noise sensitivity**: NISQ devices limit practical circuit depth

### Step 4: Classical Baseline Comparison

Always compare against:
- Classical algorithms with similar asymptotic complexity
- GPU/TPU-optimized implementations
- Classical approximation methods (tensor networks, low-rank approximations)

### Step 5: Timeline Estimate

Based on current hardware trajectories:
- **Exponential speedup QDL**: 15-20+ years to practical advantage
- **VQA-based QDL**: May show advantage on specialized problems in 5-10 years
- **Quantum-inspired classical**: Often achieves most practical gains today

## Decision Matrix

| Scenario | Recommendation |
|----------|---------------|
| Small dataset, unique quantum structure | Explore VQA approach |
| Large-scale DL training | Use classical; quantum not viable |
| Research/academic exploration | Study all three categories |
| Production ML system | Classical or quantum-inspired only |
| Specific linear algebra subroutine | Evaluate quantum algorithms if QRAM available |

## Key Papers

- "Quantum Deep Learning Still Needs a Quantum Leap" (arxiv:2511.01253)
- "Quantum computing and AI: status and perspectives" (arxiv:2505.23860)
- "Comprehensive Survey of QML" (arxiv:2501.09528)
- "Learning to Learn with Quantum Optimization via QNNs" (arxiv:2505.00561)

## Related Skills

- `quantum-ml-robustness`: QML model testing and robustness
- `qml-mutation-testing`: Systematic QML mutation testing
- `variational-quantum-algorithms`: VQA methodology
- `quantum-neural-architecture`: QNN design patterns
