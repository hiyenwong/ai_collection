---
name: psm-quantum-memory-distribution
description: "Progressive Swapping to the Middle (PSM) protocol for entanglement distribution in quantum networks with imperfect quantum memories. Optimizes entanglement swapping order to minimize decoherence from finite memory coherence times. Presented at 2026 EuCNC and 6G Summit."
arxiv_id: "2605.31493"
published: "2026-05-29"
authors: "Claire Mesny, Fabrice Guillemin, Claire Goursaud"
tags: [quantum-networks, entanglement-distribution, quantum-memory, swapping-protocol, decoherence, 6G]
---

# PSM: Progressive Swapping to the Middle for Quantum Networks

Entanglement distribution protocol optimized for imperfect quantum memories. Source: arXiv:2605.31493. Presented at 2026 EuCNC and 6G Summit.

## Core Problem: Memory-Limited Entanglement Distribution

In quantum repeater networks, entanglement is distributed by creating entangled pairs on adjacent links and performing Bell State Measurements (BSMs) to swap entanglement across the full path. With **imperfect quantum memories** (finite coherence time T₂), the order of swapping operations critically affects the final entanglement fidelity.

Naive swapping orders waste resources by performing swaps on links where one side has already decohered.

## PSM Protocol: Progressive Swapping to the Middle

### Algorithm

Given a linear chain of N nodes with links between adjacent nodes:

1. **Phase 1**: Simultaneously create entangled pairs on all adjacent links
2. **Phase 2**: Perform swaps progressively from both ends toward the center
   - Swap links (1,2) and (N-1,N) simultaneously
   - Swap links (2,3) and (N-2,N-1) simultaneously
   - Continue until meeting at the middle
3. **Result**: End-to-end entanglement between nodes 1 and N

### Why PSM Works

- **Minimizes idle time**: Quantum memories spend less time waiting before being swapped
- **Balanced decoherence**: Both sides of the chain age similarly, avoiding asymmetric degradation
- **Optimal for exponential decoherence**: Under exponential memory decay model, PSM minimizes the expected number of fresh pairs needed

### Complexity Analysis

For a chain of N nodes:
- **Total swaps needed**: N-1
- **Sequential steps (depth)**: ⌈(N-1)/2⌉ (parallelizable)
- **Memory lifetime utilization**: ~2x better than sequential end-to-end swapping

## Implementation Pattern

```python
def psm_swapping_schedule(n_nodes):
    """
    Generate PSM swapping schedule for a linear chain.
    Returns list of rounds, each round contains simultaneous swap operations.
    """
    rounds = []
    left, right = 0, n_nodes - 2  # link indices
    
    while left <= right:
        round_ops = []
        round_ops.append((left, left + 1))  # Swap at left end
        if left != right:
            round_ops.append((right, right + 1))  # Swap at right end
        rounds.append(round_ops)
        left += 1
        right -= 1
    
    return rounds

# Example: 5-node chain
schedule = psm_swapping_schedule(5)
# Round 0: Swap(0,1), Swap(3,4) — outermost links
# Round 1: Swap(1,2), Swap(2,3) — next inner
# Round 2: Swap(2,2) — middle (self, done)
```

## Performance Model

Under exponential memory decoherence with time constant T₂:

```
Fidelity_PSM ≈ exp(-T_swap / T₂ × ⌈(N-1)/2⌉)
Fidelity_sequential ≈ exp(-T_swap / T₂ × (N-1))
```

Where T_swap is the time per swapping operation. PSM achieves roughly **2x fidelity advantage** over naive sequential swapping for large N.

## Extensions

### With Classical Communication Delay

When BSM results must be communicated classically:
- PSM still beneficial but advantage reduced by communication latency
- For long distances, latency dominates decoherence → pipelined protocols preferred

### With Heterogeneous Memories

When different nodes have different T₂ times:
- PSM generalizes: swap from nodes with shorter T₂ first
- Optimization becomes: find permutation minimizing max(idle_time_i / T₂_i)

## When to Use

- Linear quantum repeater chains with imperfect memories
- Satellite-to-ground quantum links with atmospheric decoherence
- Quantum network routing protocols in 6G architectures
- Any scenario where memory coherence time is the limiting factor

## Pitfalls

1. **Not optimal for all topologies**: PSM is designed for linear chains; mesh/torus networks need different strategies
2. **Assumes synchronized operations**: All nodes need coordination for simultaneous swaps
3. **Ignores swap failure**: Protocol assumes deterministic BSM; probabilistic BSM requires retry mechanisms
4. **No error correction**: PSM optimizes swapping order but does not include quantum error correction

## Related Skills

- `diamond-color-center-quantum-networks`: Diamond NV center quantum networks
- `hopper-entanglement-distribution`: Hop-by-hop entanglement distribution
- `quantum-network-task-control`: Task-based quantum network control
- `progressive-swapping-quantum-network-protocol`: PSM protocol methodology

## Activation

progressive swapping quantum, PSM protocol, imperfect quantum memory, entanglement distribution optimization, quantum repeater chain, memory decoherence swapping, quantum network 6G, progressive swapping middle, entanglement swapping order, 量子存储器不完美交换协议

## References

- **Paper**: "An efficient Progressive Swapping to the Middle distribution protocol adapted to imperfect quantum memories in quantum networks"
- **arXiv**: 2605.31493
- **Authors**: Claire Mesny, Fabrice Guillemin, Claire Goursaud
- **Presented at**: 2026 EuCNC and 6G Summit
- **Published**: May 29, 2026
