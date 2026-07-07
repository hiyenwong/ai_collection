---
name: rl-list-sequential-qldpc-decoding
description: "Reinforcement learning-based list sequential belief propagation decoder for QLDPC codes — extends RL-S scheduling with list-based branch exploration for improved decoding convergence."
version: "1.0"
created: "2026-06-28"
source: "arxiv"
---

# RL-Based List Sequential QLDPC Decoding

## Description

Methodology for decoding quantum low-density parity-check (QLDPC) codes using reinforcement learning with list-based sequential belief propagation. Extends the RL-S (reinforcement-learning-based sequential variable-node scheduling) framework with list-based search to address short cycles, degeneracy, and poor convergence of standard BP decoders.

## Activation Keywords
- RL QLDPC decoder
- list sequential belief propagation
- reinforcement learning quantum error correction
- QLDPC decoding
- RL-S decoder
- 量子LDPC解码
- sequential BP scheduling

## Core Problem

QLDPC codes are strong candidates for fault-tolerant quantum computation, but efficient decoding is challenging due to:
1. **Short cycles** in Tanner graphs causing BP oscillation
2. **Degeneracy** — multiple error patterns yield same syndrome
3. **Poor convergence** of standard belief propagation decoders

## Methodology

### RL-Sequential Scheduling (RL-S)
- Learned policy selects the next variable node to update at each BP iteration
- Improves convergence over random or fixed scheduling
- Policy trained via reinforcement learning on representative QLDPC codes

### List-Based Extension (RL-LS)
At each scheduling step:
1. **Main trajectory**: Policy selects variable node, performs standard RL-S update
2. **Competing branch**: Softly bias post-update LLR pair toward the **second-most likely Pauli symbol**
3. **Recompute**: Update incident local BP messages for the alternative branch
4. **Set**: Mark visited variable node to second-best symbol
5. **Rank & Prune**: Candidate trajectories ranked by cumulative path metric

### Cumulative Path Metric
- Tracks quality of each candidate trajectory
- Enables pruning of unpromising branches
- Balances exploration vs. computational cost

## Implementation Patterns

### Decoder Architecture
```
For each BP iteration:
  1. RL policy → select variable node v
  2. Main path: standard BP update at v
  3. List path: bias LLR → second-best Pauli symbol
  4. Recompute local messages for list branch
  5. Update cumulative path metrics
  6. Prune: keep top-K trajectories
  7. Select best trajectory for next iteration
```

### Training Setup
- Train on representative QLDPC benchmark codes
- Depolarizing channel noise model
- Reward: successful decoding / convergence speed
- State: current syndrome, BP message configuration

### Hyperparameters
- List size K: trade-off between performance and complexity
- Bias strength: how strongly to push toward second-best symbol
- Pruning threshold: when to discard candidate trajectories

## Performance Characteristics

- **Improves** over standard BP-based decoding methods
- **Extends** RL-S convergence with list exploration
- **Trade-off**: larger list → better performance, higher complexity
- Tested on representative QLDPC benchmark codes over depolarizing channel

## Applications

1. **Fault-tolerant quantum computing**: Reliable QLDPC decoding
2. **Quantum memory**: Long-term storage with error correction
3. **Quantum communication**: Error correction in quantum channels
4. **Surface codes**: Generalizable to topological codes

## Related Concepts
- Belief propagation decoding
- Quantum LDPC codes
- Reinforcement learning for scheduling
- List decoding
- Syndrome-based error correction
- Degenerate quantum codes

## arXiv Reference
- Paper: "Learning-Based List Sequential Belief Propagation Decoding of Quantum LDPC Codes"
- ID: 2606.20926
- URL: https://arxiv.org/abs/2606.20926
- Authors: Mohsen Moradi, Taejoon Kim, Remi A. Chou
- Published: 2026-06-18
- Categories: cs.IT, quant-ph

## Notes
- Key innovation: combining learned scheduling with list exploration
- The second-best Pauli symbol exploration captures degeneracy
- Cumulative path metric enables principled pruning
