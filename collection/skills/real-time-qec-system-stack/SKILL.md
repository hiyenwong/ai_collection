---
name: real-time-qec-system-stack
category: quantum-systems
description: Real-time Quantum Error Correction (QEC) system stack architecture and engineering methodology. Six-layer reference architecture from syndrome acquisition to logical operations with latency budget modeling.
created: 2026-06-04
source: arXiv:2605.30765
tags: [quantum, error-correction, systems-engineering, real-time, architecture]
---

# Real-Time QEC System Stack

## Background
Quantum error correction (QEC) is transitioning from physical feasibility demonstrations to systems engineering challenges. Google achieved below-threshold performance on distance-5/7 surface codes, while Riverlane and Rigetti demonstrated hardware-integrated low-latency feedback loops. The core challenge has shifted from algorithmic capability to system-level engineering.

## Key Insights

### Three Critical Bottlenecks
1. **QEC Round Time** — The complete cycle from syndrome measurement to correction must complete within the coherence window
2. **Tail Latency** — Average decoder speed is insufficient; P99 latency determines system reliability
3. **End-to-End Data Path Coordination** — Pipeline bottlenecks across syndrome acquisition → decoding → correction

### Six-Layer Reference Architecture
1. **Syndrome Acquisition Layer** — Physical qubit measurement, syndrome extraction
2. **Syndrome Preprocessing Layer** — Error filtering, data formatting, noise characterization
3. **Decoder Layer** — Real-time decoding algorithms (surface codes, qLDPC)
4. **Correction Computation Layer** — Determine Pauli frame updates
5. **Logical Operation Layer** — Execute logical gates, manage code switching
6. **System Orchestration Layer** — Resource management, fault monitoring, adaptive control

### Decoder Algorithm Readiness Assessment
- **Minimum Weight Perfect Matching (MWPM)**: Mature for surface codes, limited scalability
- **Union-Find Decoder**: Fast O(n·α(n)), good for real-time, but suboptimal threshold
- **Belief Propagation (BP)**: Scalable for qLDPC, needs post-processing for degenerate errors
- **BP-OSD**: Better accuracy, higher latency — needs parallelization for real-time use

## Application Steps
1. Map your QEC system to the six-layer reference architecture
2. Identify the bottleneck layer through latency profiling
3. Select decoder algorithm based on code type (surface vs qLDPC) and latency budget
4. Design for tail latency, not average performance
5. Implement adaptive decoding that switches strategies based on error rate

## Pitfalls
- Focusing on average decoder speed while tail latency causes system failures
- Ignoring data path coordination between syndrome extraction and correction application
- Using offline decoder benchmarks without accounting for hardware integration overhead
- Not accounting for syndrome measurement errors in the decoding pipeline

## Verification
- Measure end-to-end latency from syndrome measurement to correction application
- Benchmark P99 latency, not just average
- Validate decoder performance under realistic noise models (not idealized)

## Activation
quantum error correction, QEC, real-time decoding, surface codes, qLDPC, fault tolerance, system stack, latency budget, decoder benchmark, systems engineering