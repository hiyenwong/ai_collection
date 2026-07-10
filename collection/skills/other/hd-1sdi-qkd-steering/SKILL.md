---
name: hd-1sdi-qkd-steering
category: quantum-computing
trigger_words: ["high-dimensional QKD", "one-sided device-independent", "quantum steering QKD", "1sDI-QKD", "transverse-spatial entanglement QKD", "QKD noise robustness dimension", "reverse reconciliation QKD"]
created: 2026-07-10
source: "arxiv:2607.08709"
---

# High-Dimensional One-Sided Device-Independent QKD via Quantum Steering

**Source**: Monika Mothsara et al., "Robust One-Sided Device-Independent Quantum Key Distribution via High-Dimensional Steering" (arXiv:2607.08709, July 2026)

## Overview

This paper proposes and experimentally demonstrates a robust high-dimensional (HD) one-sided device-independent QKD (1sDI-QKD) protocol using photons entangled in the transverse-spatial degree of freedom. It shows that increasing the Hilbert space dimension enhances robustness against both noise and loss.

## Key Problem

Standard QKD is limited by susceptibility to noise, losses, and device imperfections. One-sided device-independent QKD relaxes trust assumptions but typically suffers from low key rates and noise sensitivity. High-dimensional encoding offers a path to improved robustness.

## Core Methodology

### Protocol Design

- **One-sided DI**: One party's devices are trusted, the other's are untrusted
- **High-dimensional encoding**: Uses transverse-spatial modes of photons (up to dimension 11)
- **Quantum steering**: Certifies security through steering inequalities
- **Reverse reconciliation**: Evaluates achievable secret key rates

### Experimental Building Blocks

1. **HD entanglement source**: High-quality source of high-dimensional photonic entanglement in transverse-spatial modes
2. **Programmable measurement device**: Fully programmable, high-dimensional multi-outcome measurement (up to d=11)

### Key Findings

1. **Increasing dimension enhances robustness** against both noise and loss
2. **Positive key rates** for all investigated dimensions under fair-sampling assumption
3. **Highest key rates at d=7** (not the maximum dimension — there's an optimal trade-off)
4. **Dimension 11 demonstrated** as experimental capability

## Scaling Behavior

- Key rate vs dimension: peaks around d=7, then decreases
- Noise tolerance: monotonically increases with dimension
- Loss tolerance: monotonically increases with dimension
- Optimal dimension depends on the specific noise/loss regime

## When to Use

- Designing QKD systems operating in noisy/lossy channels
- Evaluating trade-offs between dimension and key rate
- Building device-independent or partially device-independent QKD
- Photonic QKD using spatial mode encoding

## Pitfalls

- Fair-sampling assumption required for current implementation
- Loophole-free implementation requires addressing detection efficiency
- Higher dimension doesn't always mean higher key rate — d=7 was optimal in this setup
- Transverse-spatial encoding requires specialized optical components

## Activation

Keywords: HD QKD, one-sided DI, quantum steering, transverse-spatial entanglement, reverse reconciliation, dimension trade-off, photonic QKD, noise robustness
