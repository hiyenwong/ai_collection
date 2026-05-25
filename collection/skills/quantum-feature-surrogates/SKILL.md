---
name: quantum-feature-surrogates
description: "Quantum feature surrogates framework for production-scale quantum feature extraction. Uses small representative subsamples processed on quantum hardware to train classical surrogates, enabling quantum-advantaged inference at near-zero cost. (arXiv: 2605.19801)"
category: quantum-computing
version: 1.0.0
tags: [quantum, feature-extraction, surrogate-model, industrial-quantum, quantum-advantage, production-ml, subsampling]
trigger: quantum feature surrogate, quantum feature extraction industrial, quantum subsample teacher, production quantum ML, Kipu Quantum quantum advantage, quantum representation teacher, quantum-to-classical distillation
---

# Quantum Feature Surrogates: Off-line Quantum-Advantage Feature Extraction for Industrial Production

## Source
- arXiv: 2605.19801
- Authors: Carlos Flores-Garrigos, Gabriel D. Alvarado Barrios, Qi Zhang, Anton Simen, Enrique Solano
- Category: quant-ph

## Overview

Quantum feature surrogates is a framework developed by Kipu Quantum that enables quantum-advantage feature extraction for industrial-scale production systems. Instead of running quantum circuits on every data sample (prohibitively expensive at millions of samples), the framework processes a carefully chosen subsample on quantum hardware and trains a classical surrogate model to apply the learned quantum patterns to the full dataset at near-zero cost.

## Core Methodology

### Problem Statement

Industrial processors now exceed 100 qubits and can extract quantum-advantaged features from data. However, per-sample quantum execution cost makes direct application infeasible for large datasets (millions of customers, transactions, images, etc.).

### Quantum Feature Surrogates Framework

**Step 1: Representative Subsampling**
- Select a small, carefully chosen subsample from the full dataset
- Subsample distribution must faithfully represent the full dataset
- Selection can use stratified sampling, core-set selection, or active learning

**Step 2: Quantum Feature Extraction**
- Run quantum feature extraction circuits on the subsample only
- Quantum processor acts as a "teacher of representations"
- Extract richer feature representations that classical models struggle to match

**Step 3: Surrogate Training**
- Train a simple classical model (the "surrogate") to learn the quantum-induced patterns
- Surrogate learns to map raw inputs → quantum-extracted features
- Training cost is negligible compared to per-sample quantum execution

**Step 4: Production Inference**
- Deploy the classical surrogate for production inference
- Full dataset processed at near-zero computational cost
- Quantum hardware is no longer needed at inference time

### Architecture Pattern

```
[Full Dataset] → [Subsample Selection] → [Quantum Processor] → [Quantum Features]
                                              ↓
                                        [Surrogate Training]
                                              ↓
[Full Dataset] → [Classical Surrogate] → [Production Inference]
```

## Key Benefits

| Aspect | Direct Quantum | Quantum Surrogate |
|--------|---------------|-------------------|
| Quantum executions | O(N) for N samples | O(S) for S << N samples |
| Inference cost | O(N) × quantum cost | O(N) × classical cost |
| Scalability | Limited by quantum access | Unlimited |
| Accuracy | Quantum-advantaged | Quantum-advantaged (via surrogate) |

## When to Use

Use this skill when:
- Quantum feature extraction shows advantage but per-sample execution is too expensive
- Production ML systems need quantum-advantaged features at scale
- Industrial applications with large datasets (millions of samples)
- Cost-constrained quantum ML deployment scenarios
- Hybrid quantum-classical ML pipeline design

## Implementation Steps

1. **Identify quantum feature extraction method** that shows advantage for your data type
2. **Design subsampling strategy**: Ensure representative coverage of data distribution
3. **Determine subsample size**: Trade-off between quantum cost and surrogate fidelity
4. **Run quantum feature extraction** on the subsample
5. **Train classical surrogate**: Map raw inputs → quantum features
6. **Validate surrogate quality**: Compare surrogate features vs. direct quantum features
7. **Deploy for production**: Classical inference at scale with quantum-advantaged features

## Pitfalls

- **Subsample must be representative**: Poor sampling leads to biased surrogates
- **Surrogate capacity must match quantum feature complexity**: Too simple → information loss
- **Quantum advantage must exist**: Only valuable when quantum features genuinely outperform classical
- **Subsample size trade-off**: Too small → poor surrogate; too large → expensive quantum runs
- **Distribution shift**: Surrogate may degrade if production data distribution drifts from training

## Related Papers

- Q-PhotoNAS (arXiv:2605.22097) — NAS for photonic quantum ML
- Quantum Reservoir Computing with Tunable Memory (arXiv:2605.12713)
- Distributed QNN Training via Circuit Cutting (arXiv:2602.16233)
