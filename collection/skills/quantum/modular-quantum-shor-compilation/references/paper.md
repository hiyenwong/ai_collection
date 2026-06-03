# Paper Reference: Factoring 2048-bit RSA with Modular Atomic Processor

**arXiv**: 2605.03951
**Title**: Factoring $2048$ bit RSA integers with a half-million-qubit modular atomic processor
**Published**: 2026-05-06

## Abstract

Shor's algorithm is one of the most promising applications of quantum computers. However, since ~10^6 physical qubits are believed to be required for established approaches, the algorithm will need to be distributed across many modules. This paper provides a distributed compilation of Shor's algorithm on a modular atomic processor. An end-to-end compilation and optimization strategy focuses on the interplay between inter-module communication and intra-module clock rate. With a half-million-qubit modular atomic processor with a communication rate of 10^5 Bell pairs per second and a measurement time of 1 ms in a CPU-inspired architecture, 2048-bit RSA integers can be factored in only 16% more time than a single-module architecture. First end-to-end analysis and simulation of large-scale integer factorization on modular atomic hardware; provides a blueprint for future design of other large-scale modular algorithms.

## Key Contributions

1. First end-to-end distributed compilation of Shor's algorithm for 2048-bit RSA
2. Half-million-qubit modular atomic processor architecture
3. CPU-inspired modular design with photonic interconnects
4. Only 16% time overhead vs ideal single-module architecture
5. Blueprint for scaling other large-scale quantum algorithms

## Technical Details

- Communication rate: 10^5 Bell pairs/second
- Measurement time: 1 ms
- Architecture: CPU-inspired modular design
- Time overhead: 16% vs single-module
