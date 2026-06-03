---
name: progressive-swapping-quantum-network-protocol
description: "Progressive Swapping to the Middle (PSM) protocol methodology for efficient entanglement distribution in quantum networks with imperfect quantum memories. Combines nested entanglement swapping with memory-aware scheduling. Use when designing quantum network protocols, entanglement distribution strategies, quantum repeater architectures, or optimizing quantum communication under memory decoherence constraints. Activation: progressive swapping, PSM protocol, quantum memory entanglement distribution, quantum repeater scheduling, imperfect quantum memory protocol, 量子网络纠缠分发"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.31493"
  published: "2026-05-29"
  authors: "Claire Mesny, Fabrice Guillemin, Claire Goursaud"
  tags: [quantum-networks, entanglement-distribution, quantum-memory, PSM-protocol, quantum-communication]
---

# Progressive Swapping Quantum Network Protocol

## Core Concept

The Progressive Swapping to the Middle (PSM) protocol optimizes entanglement distribution across multi-hop quantum networks by performing entanglement swapping progressively toward the middle of the communication path, rather than sequentially end-to-end. This approach is specifically adapted for networks with imperfect quantum memories that suffer from decoherence.

## Key Insights

### Problem with Sequential Swapping

Standard entanglement swapping performs Bell measurements sequentially along a path:
- Node A↔B → B↔C → C↔D → ... → final entanglement
- Each waiting hop accumulates memory decoherence
- Total fidelity drops exponentially with path length

### PSM Protocol Strategy

1. **Divide path into segments** of equal or optimized length
2. **Establish entanglement in parallel** on all segments simultaneously
3. **Progressively swap toward the middle**: inner nodes perform Bell measurements first
4. **Outer segments swap last**, minimizing total memory holding time
5. **Memory-aware scheduling**: account for coherence times when planning swap order

### Mathematical Framework

For a path of length L with n hops:
- **Sequential**: max memory time = (n-1) × t_swap
- **PSM (binary tree)**: max memory time ≈ log₂(n) × t_swap
- **Fidelity improvement**: F_PSM > F_sequential when memory coherence time T_coh < (n-1) × t_swap

## Usage Patterns

### Pattern 1: Network Protocol Design

When designing quantum network protocols:
1. Characterize quantum memory coherence times (T₁, T₂)
2. Calculate entanglement generation rates per link
3. Determine optimal segment division (equal vs. adaptive)
4. Schedule swapping order to minimize max memory time
5. Simulate protocol under realistic noise models

### Pattern 2: Imperfect Memory Adaptation

When memories are heterogeneous:
1. Map each node's memory quality (coherence time, fidelity)
2. Assign shorter segments to nodes with worse memories
3. Prioritize swapping through high-quality memory nodes
4. Use memory purification before swapping if needed

### Pattern 3: 6G Quantum Network Integration

For quantum-classical hybrid networks:
1. PSM protocol integrates with classical control plane
2. Classical signaling coordinates swap timing
3. Resource allocation jointly optimizes quantum and classical bandwidth
4. Presented at 2026 EuCNC & 6G Summit — designed for near-term deployment

## Pitfalls

### Memory Decoherence Underestimation
PSM only helps if memory coherence time is the bottleneck. If entanglement generation rate is the limiting factor, sequential swapping may perform similarly.

### Synchronization Overhead
PSM requires more coordination between nodes than sequential swapping. Classical communication latency for coordination must be factored into the protocol timing.

### Segment Size Optimization
Equal-length segments are simple but not always optimal. Adaptive segment sizing based on per-link entanglement generation rates and per-node memory quality yields better results.

### Scalability Limit
For very long paths (>20 hops), PSM may require intermediate purification stages. The basic PSM protocol assumes sufficiently high initial entanglement fidelity.

## References

- arXiv:2605.31493 — Original PSM protocol paper (EuCNC 2026)
- Related: `quantum-network-control`, `quantum-entanglement-detection`, `quantum-network-routing-hamiltonian`
