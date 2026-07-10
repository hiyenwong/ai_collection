---
name: lottery-bp-decoding
description: >
  Lottery BP methodology for scalable quantum error correction decoding.
  Introduces randomness during belief propagation decoding to improve accuracy
  by 2-8 orders of magnitude for topological codes (surface, toric, BB codes).
  Use when: quantum error correction, qLDPC decoding, scalable quantum decoders,
  belief propagation for quantum codes, syndrome processing, PolyQec architecture,
  or when building fault-tolerant quantum computing systems requiring real-time decoding.
---

# Lottery BP: Scalable Quantum Error Decoding

## Core Innovation

Standard Belief Propagation (BP) decoders for quantum LDPC codes suffer from error degeneracy
— multiple equivalent error patterns produce identical syndromes, causing BP to fail.
Lottery BP breaks this symmetry by introducing controlled randomness during decoding iterations.

## Key Concepts

### 1. Lottery BP Decoder

- Add randomness to variable node updates during BP message passing
- Each decode attempt uses different random seeds
- Multiple independent attempts → select lowest-weight solution
- Improves accuracy by 2-8 orders of magnitude over standard BP for topological codes

### 2. Syndrome Vote (Pre-processing)

- Compress multiple rounds of measurement syndromes into a single syndrome
- Majority voting across temporal syndrome rounds
- Increases latency margin and mitigates decoder backlog
- Essential for multi-round measurement error handling

### 3. PolyQec Architecture

Two-level decoding hierarchy:
- **Local decoder**: Lottery BP (fast, high accuracy for most errors)
- **Global decoder**: Ordered Statistics Decoding (OSD) (slow, used only when BP fails)
- Lottery BP's improved local accuracy reduces OSD invocations by 3-5 orders of magnitude

### 4. Syndrilla Simulator

- PyTorch-based modular decoding simulation pipeline
- GPU-accelerated (1-2 orders of magnitude faster than CPU)
- Extensible interface for adding new decoder types
- Integrated metrics for fair decoder comparison

## Algorithm Steps

```
def lottery_bp(syndrome, H, max_iterations, num_lotteries):
    """
    syndrome: measured syndrome vector
    H: parity check matrix
    max_iterations: BP iterations per lottery
    num_lotteries: number of random attempts
    """
    best_solution = None
    best_weight = infinity
    
    for lottery in range(num_lotteries):
        # Initialize with random perturbation
        messages = initialize_messages(H, seed=lottery)
        
        # Run BP with randomized updates
        for iteration in range(max_iterations):
            # Variable node update with random noise
            variable_msgs = update_variable_nodes(messages, random_noise=True)
            # Check node update  
            check_msgs = update_check_nodes(variable_msgs, H)
            messages = merge_messages(check_msgs)
            
            # Estimate error pattern
            estimate = compute_estimate(messages)
            
            if syndrome_check(estimate, H, syndrome):
                weight = hamming_weight(estimate)
                if weight < best_weight:
                    best_weight = weight
                    best_solution = estimate
                break  # Valid solution found
        
        if best_solution is not None:
            break  # Found valid solution
    
    return best_solution
```

## When to Use

- **Scalable quantum decoding**: Need to decode millions of qubits in real-time
- **Topological codes**: Surface code, toric code, bivariate bicycle codes
- **Resource-constrained QCIs**: Limited classical compute for quantum-classical interfaces
- **Error floor improvement**: Need better performance in low physical error rate regime

## Key Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| num_lotteries | Random decode attempts | 10-100 |
| max_iterations | BP iterations per attempt | 50-200 |
| syndrome_window | Rounds for syndrome voting | 3-7 |
| random_strength | Noise amplitude in updates | tuned per code |

## Pitfalls

- **Too few lotteries**: May not find valid solution for degenerate codes
- **Too many lotteries**: Increases latency, defeats scalability goal
- **Missing syndrome vote**: Multi-round measurement errors cause catastrophic failures
- **No OSD fallback**: Lottery BP may fail on rare error patterns; OSD fallback needed

## Related Patterns

- **Min-sum decoder**: Alternative to BP with lower complexity (works well for Margulis codes)
- **OSD (Ordered Statistics Decoding)**: Global fallback decoder, computationally expensive
- **Predecoding**: Lightweight first-pass decoding to reduce workload (see qLDPC predecoding)

## References

- arXiv:2605.00038 "Lottery BP: Unlocking Quantum Error Decoding at Scale"
  (Zhu et al., May 2026)
