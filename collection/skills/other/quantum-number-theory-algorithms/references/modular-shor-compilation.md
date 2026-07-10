# Modular Shor Compilation: Distributed RSA Factoring

**arXiv**: 2605.03951 (2026-05-06)
**Title**: Factoring 2048 bit RSA integers with a half-million-qubit modular atomic processor

## Summary
First end-to-end distributed compilation of Shor's algorithm for 2048-bit RSA factoring on a modular atomic processor. Uses half-million qubits with 10^5 Bell pairs/sec inter-module communication rate and 1ms measurement time. Only 16% time overhead vs ideal single-module architecture.

## Architecture Parameters

| Parameter | Value |
|-----------|-------|
| Total qubits | ~500,000 |
| Comm rate | 10^5 Bell pairs/second |
| Measurement time | 1 ms |
| Architecture | CPU-inspired modular |
| Time overhead | 16% vs single-module |

## Key Patterns for Number Theory Quantum Algorithms

1. **Bell Pair Budgeting**: Estimate total Bell pairs, pipeline with computation
2. **Module Partitioning**: Decompose circuit, minimize cross-module teleportation
3. **CPU-inspired Design**: Modular arrays + photonic interconnects + classical control hierarchy

## Scaling Estimates

| RSA bits | Qubits | Modules |
|----------|--------|---------|
| 1024 | ~200K | 4-8 |
| 2048 | ~500K | 8-16 |
| 4096 | ~1M+ | 16-32 |

## Relevance to Number Theory
This paper bridges the gap between theoretical quantum number theory algorithms (Shor's algorithm) and practical engineering constraints for large-scale implementation. The modular compilation approach is applicable to any quantum algorithm that exceeds single-module qubit capacity.
