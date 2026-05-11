---
name: quantum-replay-buffer-engineering
description: Replay buffer engineering for quantum circuit optimization via RL. Use when: (1) training RL agents for quantum architecture search (QAS), (2) optimizing quantum circuits with reinforcement learning, (3) improving sample efficiency in quantum-classical hybrid training, (4) warm-starting noisy quantum device training, (5) amortizing expensive quantum evaluations during RL training. Covers ReaPER+ annealed replay, OptCRLQAS amortized evaluation, and noiseless-to-noisy trajectory transfer. Activation: replay buffer quantum, RL quantum optimization, quantum architecture search, quantum circuit RL, replay buffer engineering.
---

# Quantum Replay Buffer Engineering

Replay buffer optimization methodology for reinforcement learning-based quantum circuit optimization (arXiv:2604.21863).

## Problem Statement

RL for quantum circuit optimization faces three bottlenecks:
1. Replay buffers ignore TD target reliability
2. Curriculum RL triggers full quantum-classical evaluation at every step
3. Noiseless trajectories discarded when retraining under hardware noise

## ReaPER+ — Annealed Replay Rule

Transition from TD-error prioritization to reliability-aware sampling as training matures:

```python
class ReaPERPlus:
    """Annealed replay buffer for quantum circuit optimization."""
    
    def __init__(self, capacity, td_alpha=0.6, reliability_alpha=0.0):
        self.td_alpha = td_alpha
        self.reliability_alpha = reliability_alpha
        self.transition_steps = 0
    
    def sample_priority(self, td_error, visit_count, total_steps):
        """Compute sample priority with annealed reliability."""
        # Reliability increases with visit count
        reliability = 1 - (visit_count / total_steps)
        
        # Anneal from TD-driven to reliability-aware
        progress = min(1.0, self.transition_steps / total_steps)
        
        td_weight = (1 - progress) * self.td_alpha
        rel_weight = progress * self.reliability_alpha
        
        priority = (td_error ** td_weight) * (reliability ** rel_weight)
        return priority
```

**Results**: 4-32x sample efficiency gains over fixed PER, uniform replay.

## OptCRLQAS — Amortized Evaluation

Eliminate the quantum-classical evaluation bottleneck by amortizing expensive evaluations over multiple architectural edits:

```python
def amortized_crlqas(agent, circuit, num_edits=3):
    """Apply multiple edits before evaluating, reducing wall-clock time."""
    for _ in range(num_edits):
        edit = agent.propose_edit(circuit)
        circuit = apply_edit(circuit, edit)
    # Evaluate only once after all edits
    reward = evaluate_quantum(circuit)
    return reward
```

**Results**: 67.5% reduction in wall-clock time per episode on 12-qubit problems.

## Noiseless-to-Noisy Trajectory Transfer

Warm-start noisy setting learning by reusing noiseless trajectories:

```python
def transfer_replay(noiseless_buffer, noise_buffer, transfer_ratio=0.3):
    """Mix noiseless trajectories into noisy training buffer."""
    n_transfer = int(len(noiseless_buffer) * transfer_ratio)
    transferred = sample(noiseless_buffer, n_transfer)
    mixed_buffer = concat(transferred, noise_buffer)
    return mixed_buffer
```

**Results**: 85-90% reduction in steps to chemical accuracy, 90% reduction in final energy error on 6/8/12-qubit molecular tasks.

## Key Principles

1. **Experience storage is a primary algorithmic lever** — not just a caching mechanism
2. **Sampling strategy should adapt to training progress** — TD error early, reliability later
3. **Amortize expensive quantum evaluations** — multiple edits per evaluation
4. **Noiseless experience transfers to noisy settings** — reuse clean trajectories without weight transfer

## Workflow

1. Initialize replay buffer with noiseless trajectories
2. Start training with ReaPER+ (TD-error driven)
3. As value estimates mature, shift to reliability-aware sampling
4. Apply OptCRLQAS: batch edits before quantum evaluation
5. When introducing noise, transfer portion of noiseless buffer to warm-start

## Reference

- Replay-buffer engineering for noise-robust quantum circuit optimization
  - Authors: Akash Kundu, Sebastian Feld
  - arXiv: 2604.21863 (2026-04-23)
  - Categories: quant-ph, cs.AI, cs.ET
