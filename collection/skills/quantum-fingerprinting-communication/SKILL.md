---
name: quantum-fingerprinting-communication
description: "Experimental demonstration of quantum advantage in communication complexity using quantum fingerprinting for Euclidean distance computation. Uses coherent state pulses in simultaneous message passing (SMP) model. Shows quantum advantage in transmitted information for input size 10^8 with amplitude modulation encoding and superconducting nanowire single-photon detectors. Activation: quantum fingerprinting, communication complexity, Euclidean distance, SMP model, coherent states, quantum advantage, amplitude modulation, SNSPD"
metadata:
  arxiv_id: "2605.31516"
  published: "2026-05-29"
  authors: "Verena Yacoub, Niraj Kumar, Iordanis Kerenidis, Eleni Diamanti"
  tags: [quantum, communication-complexity, fingerprinting, experimental, smp, coherent-states]
---

## Core Protocol: Quantum Fingerprinting for Euclidean Distance

### Communication Complexity Setting

**Simultaneous Message Passing (SMP) model**:
- Alice and Bob each hold a vector ($x$ and $y$)
- Neither communicates with the other
- Both send messages to a third-party referee
- Referee computes $||x - y||^2$

**Quantum advantage**: Quantum fingerprints require exponentially less transmitted information than classical protocols for the same precision.

### Experimental Implementation

Instead of requiring highly entangled qubit states (impractical for large inputs), uses:

1. **Coherent state pulse trains**: Practical quantum fingerprints
2. **Amplitude modulation**: Encoding non-binary real-valued data sets
3. **Superconducting nanowire single-photon detectors (SNSPD)**: High-performance detection for large input sizes

### Results

- **Input size**: $10^8$ (demonstrates quantum advantage surpassing best classical protocol)
- **Data types**: Diverse real-valued datasets including grayscale images
- **Precision**: Reasonable precision with bounded error
- **Advantage metric**: Transmitted information (quantum < classical for same task)

## Key Technique: Coherent State Fingerprints

```
|fingerprint(x)⟩ = ⊗_k |α · x_k⟩   (coherent state pulses)
```

where $α$ is amplitude encoding the data value. The referee performs interference measurements to estimate Euclidean distance.

## When to Apply

- Communication-constrained distributed computation
- Privacy-preserving distance computation between parties
- Large-scale data comparison with bandwidth limitations
- Quantum networking demonstrations

## Advantages Over Prior Work

- Previous protocols required entangled states (hard to generate at scale)
- Coherent state approach is experimentally practical
- Demonstrated at input size $10^8$ (beyond prior experimental demonstrations)

## Pitfalls

- Requires high-quality single-photon detectors
- Amplitude modulation precision limits achievable accuracy
- Coherent state fingerprints approximate ideal quantum fingerprints
