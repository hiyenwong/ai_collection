---
name: dendritic-icl-snn
description: "Dendritic In-Context Learning (DendriCL) — single-layer compartmental SNN that achieves ICL via dendritic subthreshold dynamics implementing online LMS. Use when: designing SNN architectures for in-context learning, exploring biologically-plausible ICL mechanisms, studying dendritic computation, implementing seed-stable ICL beyond moderate task dimensions, analyzing compartmental neuron models."
tags: [spiking-neural-networks, in-context-learning, dendritic-computation, neuromorphic, online-lms, compartmental-snn, biological-plausibility, icl-benchmark, seed-stability, single-layer-snn, garg-2022-benchmark]
published: 2026-07-02
arxiv_id: "2607.02283"
authors: ["Juwei Shen", "Yujie Wu", "Changwen Chen"]
---

# Dendritic In-Context Learning (DendriCL)

**arXiv**: 2607.02283 (2026-07-02)
**Authors**: Juwei Shen, Yujie Wu, Changwen Chen

## Overview

In-context learning (ICL) has been demonstrated in Transformers, Mamba, state-space models, and MLPs through implicit gradient descent embedded in the forward pass. However, **existing Spiking Neural Networks fail the Garg-2022 ICL benchmark at non-trivial task dimensions**.

**Key Insight**: Prior SNN designs route adaptation through inference-time synaptic plasticity, treating the dendritic compartment as a passive conduit for error/teacher signals. The authors challenge this assumption — **the subthreshold dynamics of a single dendritic compartment already implement a complete online learning algorithm**.

**DendriCL** is a single-layer compartmental spiking architecture whose apical recurrence is structurally identical to leaky online Widrow-Hoff LMS. This dynamics-only update collapses the architectural depth required for general-purpose ICL to a single layer.

## Core Technical Contributions

### 1. Dendritic Compartment as Computational Substrate

The apical membrane potential of the dendritic compartment evolves as:

$$v[t] = (1 - \lambda) \cdot v[t-1] + \lambda \cdot (w^T x[t]) - \eta \cdot e[t]$$

where:
- $\lambda$ is the leaky factor controlling temporal integration
- $w$ are synaptic weights
- $x[t]$ are input spikes
- $\eta$ is the learning rate
- $e[t]$ is the prediction error signal

This directly implements **leaky online Widrow-Hoff (LMS)** learning without backpropagation or inference-time plasticity rules.

### 2. Architectural Design

- **Single-layer compartmental neurons** with separate basal and apical dendritic compartments
- **Apical recurrence** creates the feedback loop for online LMS
- **Basal compartment** receives input spikes and produces output
- **Apical compartment** implements the learning dynamics
- No depth, no attention, no inference-time plasticity required

### 3. Seed-Stable ICL at Super-Dimensional Dimensions

Key empirical finding: **DendriCL is uniquely seed-stable at super-dimensional Garg-2022 ICL**, where dense Transformers exhibit grokking-style instability and fail past moderate task dimension.

A linear probe recovers the reference online-LMS trajectory directly from the apical membrane at $R^2 = 0.93$, confirming the algorithm is **structurally embedded in the dynamics rather than implicitly discovered during training**.

### 4. Key Findings

- ICL requires **neither attention, depth, nor inference-time plasticity**
- A single compartment with online-LMS dynamics is **sufficient**
- Seed stability: DendriCL maintains performance across random seeds at task dimensions where Transformers fail
- The online-LMS trajectory is directly recoverable from apical membrane potential ($R^2 = 0.93$)

## Implementation Guidelines

### Compartmental Neuron Model

Each neuron has two compartments:

```
Basal compartment (input integration):
  - Receives input spikes x[t]
  - Integrates with synaptic weights w
  - Produces output y[t]

Apical compartment (learning dynamics):
  - Receives prediction error e[t]
  - Updates internal state via leaky LMS
  - Provides feedback to basal compartment
```

### Online LMS Implementation

```python
# Pseudocode for leaky online LMS dynamics
v_apical[t] = (1 - leak) * v_apical[t-1] + leak * (w.T @ x[t])
prediction = sigmoid(v_apical[t])
error = target[t] - prediction
v_apical[t] += learning_rate * error  # LMS update
```

### Garg-2022 ICL Benchmark

DendriCL should be evaluated on:
- **Garg-2022 ICL benchmark** with varying task dimensions
- **Seed stability analysis** across multiple random initializations
- **Linear probe analysis** to verify LMS trajectory recovery

### Comparison Baselines

Compare against:
- Dense Transformers (grokking-style failure at high dimensions)
- Prior SNN-ICL approaches (fail at non-trivial task dimensions)
- Reference online-LMS trajectory

## Design Patterns

### Pattern 1: Single-Layer ICL via Compartmental Dynamics

Replace multi-layer SNN architectures with single-layer compartmental neurons for ICL tasks. The apical dendritic compartment naturally implements the learning algorithm.

### Pattern 2: Seed-Stable Architecture Design

When seed instability is observed at high task dimensions, consider whether the learning dynamics are structurally embedded (like DendriCL) or implicitly discovered (like Transformers).

### Pattern 3: Linear Probe Verification

Use linear probes on internal states to verify that target algorithms (e.g., LMS) are structurally embedded in the dynamics.

## Activation Keywords

dendritic, dendrite, in-context learning, ICL, compartmental, online-LMS, Widrow-Hoff, seed-stable, Garg-2022, single-layer, spiking, SNN, apical, basal, subthreshold, implicit gradient, biologically plausible, grokking, stability

## Pitfalls

1. **Prior SNN-ICL failures**: Existing SNNs fail Garg-2022 at non-trivial dimensions. Don't assume SNNs can do ICL without compartmental dynamics.

2. **Synaptic plasticity ≠ ICL**: Prior approaches using inference-time synaptic plasticity fail. The learning must be embedded in compartmental dynamics.

3. **Seed stability matters**: Transformers exhibit grokking-style instability at high dimensions. DendriCL's seed stability is a key advantage.

4. **Apical vs basal compartments**: Must maintain separate compartments. Treating dendrites as passive conduits loses the ICL capability.

5. **Garg-2022 benchmark**: Standard ICL benchmarks may not capture seed stability. Use Garg-2022 for rigorous evaluation.

## Related Skills

- `spiking-neural-network-analysis`
- `spikingjelly-framework`
- `adaptive-spiking-neuron-asn`
- `meta-learning-in-context-brain-decoding`
- `dendrocentric-snn-event-classification`
- `working-memory-heterogeneous-delays`
