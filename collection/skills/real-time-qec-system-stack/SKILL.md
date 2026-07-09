---
name: real-time-qec-system-stack
description: >
  Real-Time Quantum Error Correction System Stack — six-layer reference architecture
  from syndrome acquisition to logical operations with interface definitions and
  latency budget models. Quantifies gap between decoder performance and real-time
  requirements. Use when: designing QEC systems, fault-tolerant quantum computing
  architecture, real-time quantum decoding, QEC latency budgeting, or syndrome
  acquisition pipeline design. arXiv: 2605.30765
---

# Real-Time QEC System Stack

## Core Concept

QEC is transitioning from physical feasibility demonstrations to systems engineering challenges. The core challenge shifts from algorithmic capability to system-level engineering: QEC round time, tail latency, and end-to-end data path coordination.

## Key Findings (arXiv: 2605.30765)

- Six-layer reference architecture from syndrome acquisition to logical operations
- Benchmarks major decoders for surface codes and qLDPC codes for real-time readiness
- Quantifies gap between current decoder performance and real-time requirements
- Google achieved below-threshold performance on distance-5/7 surface codes
- Riverlane and Rigetti demonstrated hardware-integrated low-latency feedback loops

## Six-Layer Architecture

1. **Syndrome Acquisition** - Physical measurement collection
2. **Decoding** - Syndrome-to-error mapping (surface codes, qLDPC)
3. **Feedback** - Low-latency correction application
4. **Logical Operations** - Logical gate execution
5. **Coordination** - End-to-end data path management
6. **Monitoring** - System-level performance tracking

## Latency Budget

- Beyond average decoder speed: constraints lie in QEC round time, tail latency, and end-to-end data path coordination
- Each layer has strict latency requirements that compound
- Tail latency (not average) determines system reliability

## Pitfalls

- Substantial engineering gap remains between lab demonstrations and scalable FTQC
- Decoder benchmarks must evaluate real-time readiness, not just accuracy
- Interface definitions between layers are critical for system integration

## Activation Keywords

- real-time QEC, QEC system stack, quantum error correction architecture, fault-tolerant QC, syndrome decoding, qLDPC decoder, surface code decoder, latency budget, quantum systems engineering
