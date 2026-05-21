---
name: coherent-quantum-inference
description: "Coherent quantum inference methodology preserving quantum coherence during inference for exponential sample-complexity advantage over incoherent protocols. Use when designing quantum inference protocols, quantum purity amplification, mixed-state purification, or density matrix exponentiation. Keywords: coherent quantum inference, quantum purity amplification, sample complexity"
---

# Coherent Quantum Inference

## Core Concepts

### Coherent vs Incoherent Inference
- **Incoherent inference**: Quantum data → measurement → classical output
- **Coherent inference**: Quantum data → coherent quantum processing → quantum output (preserves coherence)

### Exponential Sample-Complexity Advantage
For quantum purity amplification (QPA) with principal eigenstate targets and d-dimensional inputs:

| Protocol Type | Sample Complexity |
|---|---|
| Coherent | O(1/ε) copies |
| Incoherent | Ω(d/ε) copies |

This represents an exponential advantage in the dimension parameter d.

## Usage Patterns

### Pattern 1: Protocol Classification
When analyzing a quantum inference task:
1. Identify whether output must be quantum (coherent) or classical (incoherent)
2. If quantum output is needed, apply coherent protocol for exponential advantage
3. Compute the entanglement-breaking limit to bound the optimal incoherent counterpart

### Pattern 2: Quantum Purity Amplification
For QPA with d-dimensional inputs targeting principal eigenstates:
1. Use coherent processing: O(1/ε) copies for error ε
2. Incoherent alternative requires Ω(d/ε) copies
3. Design the coherent unitary that maps n input copies to a purified output state

### Pattern 3: Mixed-State Approximate Purification
When approximate purification is needed:
1. Determine if coherent or incoherent output is acceptable
2. If coherent output acceptable, design coherent protocol
3. Use coherent-incoherent separation to quantify advantage

### Pattern 4: Density Matrix Exponentiation
For tasks requiring ρ → e^{-iρt}:
1. Coherent protocol uses O(1/ε) copies
2. Incoherent requires Ω(d/ε) copies
3. Apply Lloyd-Mohseni-Rebentrost algorithm with coherent processing

## Mathematical Framework

### Entanglement-Breaking Limit
The optimal incoherent protocol for any coherent task is obtained by:
1. Apply entanglement-breaking channel to quantum data
2. Process classical outputs optimally
3. The gap between coherent and EB-optimal quantifies the coherence advantage

### Coherent-Incoherent Separation
For task T with input dimension d and error ε:
```
advantage = samples_incoherent / samples_coherent = Ω(d)
```

## Error Handling

### Hardware Coherence Limits
- If coherence time < protocol duration, hybrid coherent-classical approach needed
- Decompose protocol into coherence-preserving segments

### Dimension-Dependent Advantage
- Advantage scales with d; for small d, incoherent may be simpler to implement
- Consider overhead of maintaining coherence vs sample savings

## Resources
- Paper: arXiv:2605.21457 "An Exponential Sample-Complexity Advantage for Coherent Quantum Inference" by Li, Theil, Harrow, Chuang
