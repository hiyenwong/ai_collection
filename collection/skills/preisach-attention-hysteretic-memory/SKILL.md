---
name: preisach-attention-hysteretic-memory
description: "Preisach Attention Layer (PAL) — a novel sequence modeling architecture that replaces softmax attention with the classical Preisach hysteresis operator from mathematical physics. Uses binary relay operators with learned thresholds and a stack of local extrema as internal state. Achieves Turing-completeness at O(1) depth via two-stack PDA simulation. Activation: attention, hysteresis, sequence modeling, episodic memory, transformer alternative, rate-independent computation"
---

# Preisach Attention: A Hysteretic Model of Sequential Memory

**arXiv**: [2605.23603](https://arxiv.org/abs/2605.23603) (cs.LG, cond-mat.dis-nn, cs.AI, cs.NE)
**Author**: Piotr Frydrych (Warsaw University of Technology)
**Submitted**: 22 May 2026

## Overview

Preisach Attention Layer (PAL) introduces a fundamentally new sequence modeling architecture grounded in the classical Preisach hysteresis operator from mathematical physics. Rather than computing attention weights via softmax over query-key similarities, PAL replaces the attention mechanism with a **binary relay operator** parameterized by learned activation and deactivation thresholds, maintaining a **stack of local extrema** as its internal state.

This is a cross-disciplinary breakthrough bridging condensed matter physics (hysteresis in magnetic materials), theoretical computer science (Turing completeness, expressiveness), and deep learning (sequence modeling).

## Key Innovations

### 1. Preisach Hysteresis Operator as Attention
- Replaces softmax(QK^T) with binary relay operators γ̂_{α,β} from Preisach theory
- Each relay has a learned activation threshold α and deactivation threshold β
- Internal state = stack of local extrema of the input sequence
- Responds to the **sequence of local extrema**, not absolute token positions or temporal spacing

### 2. Turing Completeness at O(1) Depth
- A single-layer PAL-Transformer with O(1) depth is Turing-complete under arbitrary precision arithmetic
- Achieved through simulation of a **two-stack pushdown automaton**
- Contrast: standard hard-attention transformers require O(log n) depth for Turing completeness

### 3. Incomparable Expressiveness with Transformers
PAL and standard transformers compute **incomparable** function classes:

| Property | PAL | Transformer |
|----------|-----|-------------|
| Historical range statistics | O(1) layers | O(log n) layers |
| Random-access retrieval | Cannot perform without auxiliary state | Natural |
| Rate-independence | ✅ Inherent property | ❌ Position-sensitive |
| Long episodic memory | ✅ Efficient (O(n log n)) | ❌ Quadratic (O(n²)) |
| Positional dependence | Weak | Strong |

### 4. Rate-Independence as the Separating Property
- PAL responds only to **local extrema** of the input, not to absolute timing or spacing
- This matches the **wiping property** of classical hysteresis: smaller loops are "wiped" by larger excursions

### 5. Minimal Sufficient Statistic
- The extremum stack constitutes a **minimal sufficient statistic** of input history for all rate-independent functionals

### 6. Computational Efficiency
- **O(n log n)** total inference cost vs O(n²) for standard attention
- Particularly efficient for tasks with long sequences and weak positional dependence

### 7. Connection to Random-Field Ising Model
- PAL's behavior maps to the **random-field Ising model** (RFIM) from statistical physics
- Provides a physical interpretation of the memory dynamics

## Method Details

### PAL Architecture
```
Input sequence x₁, x₂, ..., xₙ
  ↓
Binary relay operators γ̂_{α,β} for each (α, β) pair
  ↓
Each relay tracks: current state (0 or 1), internal extremum stack
  ↓
Relay state updates based on whether input exceeds α (activate) or drops below β (deactivate)
  ↓
Output = weighted combination of relay states
  ↓
Learned thresholds α, β via gradient descent (straight-through estimator for binary ops)
```

### Key Equations
- Relay operator: γ̂_{α,β}(x) = 1 if x ≥ α, 0 if x ≤ β, unchanged otherwise
- Extremum stack: Pushes when input exceeds current max or drops below current min
- Output: y(t) = ∫∫ μ(α,β) γ̂_{α,β}(x(t)) dα dβ (Preisach plane integration)

## When to Use

This skill is relevant when:
- Working on **sequence modeling** with long-range dependencies
- Designing **alternative attention mechanisms** for transformers
- Tasks with **weak positional dependence** (e.g., certain EEG, fMRI, time-series)
- **Long episodic memory** tasks where O(n²) attention is prohibitive
- **Neuro-inspired computing** — hysteresis is a fundamental property of biological neural systems
- Architecture search for **memory-augmented neural networks**

## Limitations

- Currently only theoretical/analytical — no empirical validation on standard benchmarks
- Lacks positional encoding integration strategy for position-dependent tasks
- Binary relay operators may be harder to train with gradient descent (discrete nature)
- No comparison with linear attention variants (e.g., linearized attention, state-space models)
- Implementation details for gradient estimation through binary relays need development

## Activation

**Keywords**: preisach attention, hysteresis, sequence modeling, episodic memory, transformer alternative, rate-independent computation, binary relay operator, extremum stack, Turing completeness, attention mechanism, long-range dependence
