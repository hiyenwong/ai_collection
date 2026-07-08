---
name: virtual-distillation-bosonic
category: quantum-error-mitigation
description: Virtual distillation framework extended to bosonic quantum systems using passive linear-optical interferometers for error-mitigated measurements in continuous-variable quantum computing.
trigger_words: virtual distillation bosonic, bosonic error mitigation, cyclic shift operator, linear-optical distillation, photon loss mitigation, continuous-variable QEC, bosonic quantum computing
arxiv_id: 2607.04914
authors: Leonardo Finocchiaro, Marco Robbio, Diogo Gomes, David Gunn, Adithi Udupa, Axel M. Eriksson, Leonardo Novo, Giulia Ferrini
---

# Virtual Distillation in Bosonic Systems

## Overview

Virtual distillation is an error-mitigation technique exploiting multiple copies of a noisy quantum state to estimate observables as if measured on a purified state. Originally developed for qubit systems, this skill extends the framework to bosonic quantum information processing and continuous-variable quantum computing.

## Core Methodology

### 1. Cyclic Shift Operator Diagonalization
- Implemented with passive linear-optical interferometers
- Enables experimentally accessible protocols for multi-copy measurements
- Diagonalizes the cyclic shift on bosonic modes

### 2. Virtually Distilled Observables
- **Number operators**: Recover noise-mitigated photon number expectations
- **Phase-shift operators**: Estimate phase observables with reduced noise
- **Arbitrary quadratures**: Extend to any quadrature measurement
- **Arbitrary-order correlators**: Via characteristic function of photon-number distribution

### 3. Noise Models Addressed
- **Photon loss**: Dominant noise in bosonic architectures
- **Dephasing**: Second major noise mechanism in CV systems
- Quantifies suppression of noise contributions for both

## Implementation Patterns

### Pattern 1: Multi-Copy Measurement Protocol
- Prepare n copies of the noisy state
- Apply cyclic shift via passive linear optics
- Measure in the diagonalized basis
- Combine outcomes to estimate purified observable

### Pattern 2: Characteristic Function Estimation
- For number operator correlators of arbitrary order
- Estimate characteristic function of photon-number distribution
- Recover higher-order moments from multi-copy measurements

### Pattern 3: Linear-Optical Implementation
- Use beam splitters and phase shifters (passive elements only)
- No active squeezing or displacement required
- Compatible with existing bosonic quantum hardware

## When to Use
- Error mitigation in bosonic quantum processors
- Continuous-variable quantum computing experiments
- Photon loss mitigation in optical quantum systems
- Multi-copy quantum state characterization

## Key Advantages Over Qubit Virtual Distillation
- Uses only passive linear-optical resources
- No need for active nonlinear operations
- Directly applicable to CV architectures
- Extends to arbitrary-order correlator estimation

## References
- arXiv: 2607.04914 - "Error Mitigation in Bosonic Systems via Virtual Distillation"
