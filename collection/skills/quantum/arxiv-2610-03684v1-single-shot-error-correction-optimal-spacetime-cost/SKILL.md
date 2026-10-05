---
name: arxiv-2610-03684v1-single-shot-error-correction-optimal-spacetime-cost
description: "Achieves optimal Omega(S(K+log(S/eps))) spacetime cost for QEC using quantum Tanner codes with single-shot syndrome extraction and parallel classical decoding"
tags: [arxiv, quantum, qec, quantum-tanner-codes, spacetime-optimality, single-shot, fault-tolerant]
arxiv_id: "2610.03684v1"
utility: 0.88
date_added: "2026-10-05"
---

# Single-Shot Error Correction at Optimal Spacetime Cost

**arXiv:** 2610.03684v1 | **Utility:** 0.88 | **Date:** 2026-10-05

## Abstract

Proves that the optimal Omega(S(K+log(S/eps))) spacetime cost for storing K logical qubits for S time steps with error at most eps can be achieved with an explicit noisy error-correction circuit and efficient decoding — counting ALL state-preparation, gate, measurement, and wait locations. Uses quantum Tanner codes with single-round syndrome extraction followed by parallel classical decoder steps.

## Key Contributions

- **Optimality proof**: Matches best known lower bound up to constant factors for spacetime cost
- **Explicit noisy construction**: Not just information-theoretic — provides actual circuit and decoder
- **Quantum Tanner codes**: Each memory step = one syndrome extraction round + fixed number of parallel classical decoder steps
- **General noise model**: Works for weak but general circuit noise, including syndrome extraction faults and correlated faults
- **Exponentially small failure**: Per-step failure probability while keeping cost linear in code size
- **Extends to Clifford operations**: Same analysis applies to certain constant-depth logical Clifford gates

## Methods

1. **Quantum Tanner codes**: Provide the underlying QEC structure
2. **Single-round extraction**: One syndrome measurement per memory step
3. **Parallel classical decoding**: Fixed number of decoder steps reduce residual error enough to keep later faults correctable
4. **Long-range connectivity**: Hardware must support long-range qubit connections and fast classical processing

## Relevance

Fundamental theoretical result establishing what's achievable for QEC spacetime overhead. The fact that reliability adds only logarithmic overhead (shared by all stored qubits) is a powerful statement. Requires long-range connectivity — relevant for architectures like ion traps or photonic interconnects. Sets the theoretical ceiling that practical implementations should aspire to.
