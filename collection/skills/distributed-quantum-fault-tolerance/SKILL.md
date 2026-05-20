---
name: distributed-quantum-fault-tolerance
category: quantum-computing
description: Design fault-tolerant distributed quantum computing systems that tolerate device failure and maintain reliability through modular architectures. Updated with 2026-05-11 research on toric vs hyperbolic Floquet codes under node failure.
source: arXiv:2605.11088, arXiv:2604.22471, arXiv:2508.15580
tags: [quantum-computing, fault-tolerance, distributed-systems, reliability, error-correction]
---

# Distributed Quantum Fault Tolerance

## Trigger Conditions
- Designing distributed quantum computing architectures
- Building modular quantum systems with fault tolerance requirements
- Implementing quantum error correction across multiple QPUs
- Evaluating reliability of distributed quantum networks
- Planning device failure mitigation strategies
- Hot-swapping quantum devices during operation

## Core Principles

### 1. Modular Reliability Exceeds Component Reliability
A distributed quantum computer can operate despite replacement or failure of constituent components, allowing system reliability to exceed that of individual subcomponents.

### 2. Hot-Swappable Quantum Devices
When quantum error correction is performed over a modular quantum network:
- Quantum devices can be swapped out or replaced during operation
- Minimal impact on logical error rates during replacement
- QEC absorbs the transition without logical information loss

### 3. Distributed QEC Code Selection

#### Toric Code (Planar Topology)
- Outperforms monolithic implementation under catastrophic node failure
- Effective when physical error rate < 0.05%
- Better suited for regular grid-like QPU layouts
- Lower overhead but requires nearest-neighbor connectivity

#### Hyperbolic Floquet Code
- Higher encoding rate than toric code
- Better for irregular or sparse network topologies
- More complex decoding but handles non-local connections better
- Suitable for heterogeneous QPU networks

## Architecture Patterns

### Pattern 1: QPU Network Topology
```
[QPU-1]---(Bell)---[QPU-2]
  |                  |
(Bell)             (Bell)
  |                  |
[QPU-3]---(Bell)---[QPU-4]
```
- Each QPU holds intermediate number of physical qubits
- QPIs (Qubit-Photon Interfaces) enable Bell state generation
- Distributed QEC code encoded across all QPUs

### Pattern 2: Failure Resilience Threshold
- Catastrophic node failure probability: p/100
- Below physical error rate of 0.05%, distributed codes outperform monolithic
- Logical error suppression maintained during entire node failure

### Pattern 3: Modular QEC Integration
1. Encode logical qubits across multiple QPUs
2. Generate non-local Bell states via QPIs
3. Perform syndrome extraction across modules
4. Decode using distributed decoder (BP+OSD or MWPM)
5. Handle node failure by redistributing logical information

## Implementation Steps

1. **Network Design**
   - Determine QPU count and interconnect topology
   - Characterize QPI Bell state generation rate and fidelity
   - Map physical error rates per component type

2. **QEC Code Selection**
   - Choose between toric, surface, or hyperbolic Floquet codes
   - Consider encoding rate vs. decoding complexity tradeoff
   - Evaluate threshold performance under expected noise model

3. **Failure Mode Analysis**
   - Model node failure probability distribution
   - Simulate catastrophic vs. gradual failure scenarios
   - Identify critical paths in QEC syndrome extraction

4. **Decoder Implementation**
   - Deploy distributed BP+OSD or MWPM decoder
   - Handle syndrome staleness during node failure
   - Implement adaptive syndrome extraction scheduling

5. **Validation**
   - Monte Carlo simulation with circuit-level noise
   - Measure logical error rate vs. physical error rate
   - Verify fault-tolerant scaling with code distance

## Pitfalls

- **Ignoring QPI noise**: Qubit-Photon Interfaces add significant error; must be modeled separately from intra-QPU errors
- **Assuming perfect Bell states**: Entanglement generation is probabilistic; account for heralding failures
- **Monolithic decoder assumption**: Decoders must handle distributed syndrome information with communication delays
- **Overlooking syndrome staleness**: When skipping seam measurements, syndrome information becomes stale and degrades decoding

## Verification Steps

1. Simulate logical error rate scaling with code distance
2. Verify fault-tolerant threshold exists and is achievable
3. Test device swap procedure under realistic timing constraints
4. Measure impact of node failure probability on logical fidelity
5. Compare distributed vs. monolithic performance at target physical error rates

## Related Papers
- arXiv:2508.15580 - Universal Error Correction for Distributed Quantum Computing
- arXiv:2604.22471 - Boundary-Aware Stabilizer Scheduling for Distributed QEC
- arXiv:2605.04663 - Distributed QEC with Bivariate Bicycle Codes
- arXiv:2509.25093 - Distributed QEC with Permutation-Invariant Approximate Codes

## Key Metrics
- Logical error rate (LER) as function of physical error rate
- Threshold physical error rate for fault tolerance
- Encoding rate (k/n) for chosen QEC code
- Node failure tolerance (probability p/100)
- Bell state generation rate requirement