---
name: grid-state-qec-spam-improvement
category: quantum-systems
description: Grid-state qubit QEC achieving state preparation and measurement (SPAM) errors below 10^-3 using repeat-until-success preparation and improved measurement protocol with finite-energy envelope correction.
trigger_words: grid state qubit, SPAM error, state preparation measurement, repeat-until-success, photon loss, harmonic oscillator QEC, bosonic qubit, cardinal state, magic state, transmon comparison
created: 2026-07-09
source: arXiv 2607.06718
---

# Grid-State QEC with SPAM Below 10^-3

## Paper Summary

**Title**: Quantum error correction of a grid-state qubit with state preparation and measurement errors below 10^-3

**arXiv**: 2607.06718

**Core Problem**: Grid state qubits offer hardware-efficient QEC via large harmonic oscillator Hilbert spaces, but SPAM errors have been a major bottleneck — two orders of magnitude worse than transmon qubits.

## Key Innovations

### 1. Repeat-Until-Success State Preparation
- Leverages high-performance QEC for repeat-until-success preparation
- Works for both cardinal and magic states of single-mode grid-state qubit
- Achieves high-fidelity state initialization

### 2. Improved Measurement Protocol
- Corrects for finite-energy envelope errors
- Corrects for auxiliary qubit readout errors
- Increases robustness to photon loss

### 3. Breakthrough Performance
- Combined SPAM error **below 10^-3**
- **Two orders of magnitude** improvement over state of the art
- Brings grid-state platform on par with transmon SPAM levels

## Systems Engineering Patterns

### Pattern: Repeat-Until-Success via QEC
When state preparation fidelity is insufficient:
1. Use QEC cycle to detect preparation failures
2. Repeat preparation until syndrome indicates success
3. Trade time for fidelity deterministically

### Pattern: Multi-Error Correction in Measurement
For bosonic qubit readout:
1. Separate finite-energy envelope errors from readout errors
2. Correct each error channel independently
3. Design protocol robust to dominant physical noise (photon loss)

### Pattern: Hardware-Efficient QEC via Oscillators
For scalable fault-tolerant systems:
1. Exploit large Hilbert space of harmonic oscillators
2. Encode redundancy in mode structure rather than physical qubits
3. Target SPAM parity with conventional qubit platforms

## Performance Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| SPAM error | ~10^-1 | <10^-3 | 100x |
| Platform parity | Below transmon | On par with transmon | Competitive |

## Application Scenarios

- Fault-tolerant quantum computing with bosonic codes
- GKP codes and grid state implementations
- Superconducting circuit quantum computing
- Hardware-efficient QEC architectures

## Related Skills

- bosonic-gkp-parity-encoding
- grid-state-qec-spam-improvement
- measurement-free-quantum-error-correction
