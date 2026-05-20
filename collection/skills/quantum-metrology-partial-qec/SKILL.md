---
name: quantum-metrology-partial-qec
description: Quantum metrology enhanced by partial quantum error correction — using error correction techniques to improve sensing precision beyond the standard quantum limit. Use when designing quantum sensors, metrology protocols, or noise-resilient quantum sensing.
---

# Quantum Metrology via Partial QEC

## Core Concept

Partial quantum error correction (pQEC) improves quantum metrology by correcting dominant noise channels while preserving sensitivity to the signal parameter. Unlike full QEC which corrects all errors, pQEC selectively corrects noise that degrades sensing without eliminating the signal.

## Mathematical Framework

1. **Signal Hamiltonian**: H_s = ωG (G = generator of signal encoding)
2. **Noise Channel**: L_k (Lindblad operators representing decoherence)
3. **pQEC Condition**: Correct noise L_k while preserving [C, G] ≠ 0 (signal not corrected away)
4. **Precision Scaling**: Δω ~ 1/(√N · T · √η) where η is QEC efficiency

## Usage Patterns

### Pattern 1: Noise-Adaptive Metrology
1. Characterize dominant noise channel L_k
2. Design QEC code that corrects L_k
3. Verify signal generator G not in correctable subspace
4. Implement periodic pQEC cycles during sensing

### Pattern 2: Entanglement-Enhanced Sensing
1. Prepare entangled probe state (GHZ, spin-squeezed)
2. Apply pQEC during signal accumulation
3. Measure with optimal observable
4. Achieve precision approaching Heisenberg limit

## Key Insights
- Full QEC can destroy signal — pQEC preserves sensing capability
- Optimal pQEC balances noise suppression vs. signal preservation
- Error bias in hardware determines which pQEC codes are effective
- pQEC enables longer coherence times for precision measurements

## Activation Keywords
- quantum metrology partial QEC
- quantum error correction sensing
- noise-resilient quantum sensor
- entanglement-enhanced metrology
- quantum sensing precision
- Heisenberg limit sensing
