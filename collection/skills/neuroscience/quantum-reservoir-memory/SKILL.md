---
name: quantum-reservoir-memory
description: "Controllable quantum memory capacity methodology for quantum reservoir computing using tunable partial-SWAP gates. Unifies feedback-based and recurrent QRC architectures through partial-SWAP interpolation parameter, enabling controllable trade-off between memory capacity and processing speed. Use when: (1) designing quantum reservoir computing systems, (2) tuning quantum memory capacity, (3) choosing between feedback and recurrent QRC architectures, (4) implementing temporal quantum machine learning."
---

# Quantum Reservoir Memory Control

## Description
Unified framework for quantum reservoir computing (QRC) using tunable partial-SWAP gates that interpolates between feedback-based and recurrent architectures, providing a single hyperparameter for quantum memory capacity control.

## Activation Keywords
- quantum reservoir computing
- quantum memory capacity
- partial-SWAP QRC
- QRC architecture design
- feedback recurrent quantum reservoir
- temporal quantum machine learning
- quantum echo state network

## Architecture Paradigms

### Feedback-Based QRC
- Re-embed classical measurements from QRC back into system
- Classical readout → parameter update → quantum evolution
- Simple hardware requirements
- Limited by classical feedback latency

### Recurrent QRC
- Multi-register approach with dedicated memory and readout qubits
- Fully quantum information flow
- Higher hardware demands
- Better for complex temporal tasks

### Unified Framework: Tunable partial-SWAP
The partial-SWAP gate interpolates between paradigms:
```
SWAP(θ) = cos(θ)I - i·sin(θ)SWAP
```
- θ = 0: no coupling (feedback limit)
- θ = π/2: full swap (recurrent limit)
- 0 < θ < π/2: tunable memory capacity

## Memory Capacity Analysis

### Echo State Property
- Reservoir must satisfy echo state property (ESP)
- partial-SWAP parameter controls fading memory
- Trade-off: more memory → slower dynamics

### Memory Capacity Metrics
- **Total memory capacity**: sum over all time delays
- **Short-term memory**: recent input influence
- **Long-term memory**: historical input retention

## Design Guidelines

### Step 1: Characterize Task Memory Requirements
- Determine required memory depth
- Identify critical time scales in input

### Step 2: Tune partial-SWAP Parameter
- Start with θ ≈ π/4 for balanced behavior
- Adjust based on task performance
- Higher θ → more quantum memory, slower dynamics

### Step 3: Validate Echo State Property
- Check reservoir stability
- Ensure fading memory for inputs
- Verify non-divergent dynamics

## Advantages
1. Single hyperparameter controls architecture spectrum
2. Hardware-efficient compared to full recurrent design
3. Tunable trade-off between memory and processing
4. Validated on both simulation and hardware

## Limitations
- Partial-SWAP requires precise gate control
- Memory-accuracy trade-off is task-dependent
- Scaling to large reservoirs increases circuit depth

## Related Concepts
- Reservoir computing
- Echo state networks
- Quantum machine learning
- Temporal data processing

## Resources
- arXiv:2605.12713 - Controllable Quantum Memory Capacity in Quantum Reservoir Networks with Tunable partial-SWAPs
