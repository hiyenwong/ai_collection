---
name: lightstim-qec-protocol-evaluation
description: "LightStim framework for automated QEC protocol evaluation and prototyping with automated Detector Error Model (DEM) construction. Solves the manual DEM annotation bottleneck that limits QEC evaluation to simple memory experiments. Uses concurrent circuit compilation and DEM generation via Pauli frame tracking. Activation: LightStim, QEC protocol evaluation, DEM construction, detector error model, quantum error correction prototyping, fault-tolerant evaluation."
metadata:
  arxiv_id: "2604.21472"
  categories: ["quant-ph"]
---

## LightStim: QEC Protocol Evaluation Framework

Methodology from arXiv:2604.21472 (April 2026). LightStim automates Detector Error Model (DEM) construction concurrently with circuit compilation by maintaining a Pauli frame, enabling rigorous circuit-level evaluation of diverse QEC protocols.

## Problem Statement

Fault-tolerant quantum computing requires rigorous, circuit-level evaluation of QEC protocols. Current evaluation pipeline has a critical bottleneck:

- **DEM construction is manual**: Requires tedious, error-prone annotation of physical circuits
- **Limited to memory experiments**: Manual DEM only scales to simple scenarios
- **Blocks innovation**: New QEC protocols can't be evaluated efficiently

## Core Methodology

### Automated DEM Construction

LightStim solves the DEM construction bottleneck via:

1. **Concurrent compilation + DEM**: Builds DEM while compiling the physical circuit
2. **Pauli frame tracking**: Maintains Pauli frame through circuit execution to automatically identify error propagation paths
3. **Automated detector identification**: Identifies syndrome measurements and their error sensitivities
4. **End-to-end logical error estimation**: Computes logical error rates without manual annotation

### Framework Architecture

```
Physical Circuit Description
         ↓
   Circuit Compilation ←→ DEM Construction (concurrent)
         ↓
   Pauli Frame Tracking
         ↓
   Detector Error Model (DEM)
         ↓
   Logical Error Rate Estimation
```

### Key Features

- **Protocol-agnostic**: Works with any QEC code (surface code, color code, LDPC codes)
- **Scalable**: Handles complex protocols beyond simple memory experiments
- **Automated**: Eliminates manual DEM annotation entirely
- **Circuit-level**: Provides rigorous end-to-end logical error estimation

## Implementation Patterns

### Pattern 1: QEC Protocol Prototyping

```python
# Conceptual workflow
from lightstim import QECProtocol, compile_and_dem

# Define new QEC protocol
protocol = QECProtocol(
    code="surface_code",
    distance=5,
    rounds=10,
    gateset="clifford+T"
)

# Automatic compilation + DEM
result = compile_and_dem(protocol)

# Get logical error rate
logical_error_rate = result.estimate_logical_error_rate()
```

### Pattern 2: DEM Generation via Pauli Frame

The core innovation is using Pauli frame tracking to automatically generate DEMs:

1. **Track Pauli frame** through each gate operation
2. **Identify error propagation** paths from physical errors to detectors
3. **Construct DEM** by accumulating error contributions
4. **Validate** against known benchmarks (e.g., surface code threshold)

### Pattern 3: Multi-Protocol Comparison

Use LightStim to compare QEC protocols at the circuit level:

- Surface code vs. color code vs. LDPC codes
- Different decoding algorithms
- Different physical error models
- Different syndrome extraction schedules

## Reusable Skill Patterns

### Pattern: Automated Error Model Construction

The key reusable pattern is the automated construction of error models from circuit descriptions:

1. **Circuit description** → Gate-level representation
2. **Pauli frame propagation** → Error tracking through circuit
3. **Detector identification** → Syndrome measurement mapping
4. **DEM assembly** → Error model for decoder
5. **Logical error estimation** → Performance prediction

This pattern applies to any fault-tolerant quantum protocol evaluation.

### Pattern: Concurrent Compilation-DEM Pipeline

By building DEM during compilation (not after), LightStim avoids redundant analysis:

- Shared intermediate representation
- Error information flows naturally from compilation
- No separate DEM annotation step needed

## Pitfalls

1. **Circuit complexity**: Very large circuits may still have compilation overhead
2. **Error model assumptions**: DEM accuracy depends on physical error model fidelity
3. **Decoder compatibility**: Generated DEM must match decoder input format
4. **Non-Pauli errors**: Framework assumes Pauli error channels; coherent errors need additional treatment

## Related Skills

- [[quantum-error-correction-methods]]: Reusable patterns from QEC research
- [[quantum-fault-tolerance-benchmark]]: Evaluating QEC codes under hardware models
- [[dart-q-realtime-qldpc-decoding]]: Real-time QLDPC decoding framework

## Tags

QEC-protocol-evaluation, detector-error-model, DEM-construction, Pauli-frame-tracking, fault-tolerant-quantum, circuit-level-evaluation, QEC-prototyping, lightstim, quantum-error-correction, logical-error-rate
