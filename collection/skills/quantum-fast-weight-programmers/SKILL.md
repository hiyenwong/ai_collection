---
name: quantum-fast-weight-programmers
description: Quantum Fast-Weight Programmers with bounded memory gates for stable quantum sequence modeling. Input-dependent gates for fast-weight updates with sign-preserving tanh stabilization for long-sequence regimes. Applicable to quantum dynamics forecasting and time series prediction.
trigger: quantum fast weight, QFWP, quantum sequence modeling, bounded memory gates, quantum dynamics forecasting, self-modulating quantum
category: ai_collection/collection/skills
---

# Stable Self-Modulating Quantum Fast-Weight Programmers

## Overview
Quantum Fast-Weight Programmers (QFWPs) store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states, offering a practical route to quantum sequence modeling.

## Problem
Self-Modulating QFWP uses input-dependent gates for both new fast-weight updates and the accumulated fast-weight state, but its **unbounded old-state multiplier can diverge** in long-sequence regimes.

## Solution: Bounded Old-State Modulation
Apply a **sign-preserving tanh gate** only to the recurrent memory branch while leaving the additive update and new-update modulation unchanged.

## Architecture Variants
1. **Standard QFWP**: Basic fast-weight programming
2. **Self-Modulating QFWP**: Full input-dependent gating (unbounded)
3. **Only-New**: Modulate only new updates
4. **Only-Old**: Modulate only accumulated state
5. **Bounded Old-State** (proposed): tanh-gated recurrent memory

## Key Findings
- Old-state modulation is the most consistent source of improvement over Standard QFWP
- Bounding the old-state gate removes long-sequence divergence
- Improves aggregate robustness on quantum-dynamics forecasting tasks
- Behavior close to Only-Old ablation on Milan SMS forecasting

## Implementation Pattern
```python
# Bounded old-state modulation
old_state = tanh(recurrent_memory)  # Sign-preserving bound
new_state = old_state * update_gate + additive_update
```

## Applications
- CUDA-Q quantum-dynamics forecasting
- Milan SMS telecommunication activity prediction
- Any quantum sequence modeling with long input windows

## Activation Keywords
quantum fast weight, QFWP, quantum sequence modeling, bounded memory gates, quantum dynamics, self-modulating, tanh gating

## Source
arXiv: 2607.02363 (2026-07-02)
