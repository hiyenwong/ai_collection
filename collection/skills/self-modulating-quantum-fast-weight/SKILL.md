---
name: self-modulating-quantum-fast-weight
description: Self-Modulating Quantum Fast-Weight Programmers (QFWP) for quantum sequence modeling — stores temporal info in dynamically programmed variational-circuit parameters. Introduces bounded old-state modulation with tanh gate to prevent long-sequence divergence.
category: quantum
trigger_words: quantum fast-weight programmer, quantum sequence modeling, QFWP, self-modulating QFWP, bounded memory gate, quantum dynamics forecasting, variational quantum sequence, temporal quantum memory
arxiv_id: 2607.02363
created: 2026-07-05
---

# Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

## Core Methodology

### 1. Quantum Fast-Weight Programmers (QFWP)
- Store temporal information in **dynamically programmed variational-circuit parameters**
- Alternative to nonlinear recurrent hidden states
- Practical route to quantum sequence modeling on near-term hardware

### 2. Self-Modulating QFWP Architecture
- Uses **input-dependent gates** for:
  - New fast-weight updates
  - Accumulated fast-weight state modulation
- Original unbounded old-state multiplier **diverges** in long-sequence regimes

### 3. Bounded Old-State Modulation (Key Innovation)
- Apply **sign-preserving tanh gate** ONLY to recurrent memory branch
- Leave additive update and new-update modulation **unchanged**
- Removes long-sequence divergence while improving aggregate robustness

### 4. Evaluation Tasks
- CUDA-Q quantum-dynamics forecasting
- Milan SMS telecommunication activity prediction
- Ablation: Standard QFWP vs Full Self-Modulating vs Only-New vs Only-Old

### 5. Key Findings
- **Old-state modulation** is the most consistent source of improvement
- Bounding the old-state gate removes divergence AND improves robustness
- On Milan SMS: unbounded Self-Modulating converges, clearest gains at longer windows

## Implementation Steps

1. Define variational circuit with fast-weight parameters
2. Implement input-dependent gating:
   ```
   new_state = gate_new(input) * update(input)
   old_state = tanh(gate_old(input)) * accumulated_state  # bounded
   fast_weight = new_state + old_state
   ```
3. Train on sequence prediction tasks
4. Validate with ablation studies (Only-New, Only-Old variants)

## Pitfalls

- Unbounded self-modulation diverges on long sequences
- CUDA-Q backend required for quantum circuit simulation
- Classical baseline comparison essential for demonstrating quantum advantage
- Only-New ablation may underperform — accumulated memory is key
