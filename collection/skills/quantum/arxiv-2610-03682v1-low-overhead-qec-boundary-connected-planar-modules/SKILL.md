---
name: arxiv-2610-03682v1-low-overhead-qec-boundary-connected-planar-modules
description: "Google QAI + DeepMind: Modular hyperbolic surface/color codes with boundary connections achieve 30x overhead reduction vs surface code (Oct 2026)"
tags: [arxiv, quantum, qec, surface-code, modular-codes, google-quantum-ai, deepmind, hyperbolic-codes]
arxiv_id: "2610.03682v1"
utility: 0.95
date_added: "2026-10-05"
---

# Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules

**arXiv:** 2610.03682v1 | **Utility:** 0.95 | **Date:** 2026-10-05 | **Authors:** Google Quantum AI + Google DeepMind + MIT

## Abstract

Demonstrates that partitioning quantum processors into flat modules with sparse, static boundary connections enables modular hyperbolic surface and color codes based on new semi-hyperbolic code families. Circuit-level simulations show 10x+ physical qubit overhead reduction vs surface code, with projections to 30x+ reduction while maintaining mostly nearest-neighbor gates within planar modules.

## Key Contributions

- **Semi-hyperbolic code families**: New codes constructed from boundary-connected planar modules
- **30x overhead reduction**: Encoding rate k/n = 1/16, distance d ≥ 22, exceeding [[288,12,18]] bivariate bicycle code
- **Fault-tolerant walking circuits**: Implement logic via code automorphisms, co-designed with low-weight logical bases
- **Modular extractor system**: ≈4.5× smaller than the code itself
- **Practical feasibility**: Works under elevated inter-module seam error rates; mostly nearest-neighbor gates within modules

## Methods

1. **Modular architecture**: Planar modules connected by sparse boundary links
2. **Semi-hyperbolic codes**: New families bridging surface codes and hyperbolic geometry
3. **Neural network + matching decoders**: Efficient decoding for modular syndrome extraction
4. **Code automorphisms**: Fault-tolerant gate implementation via lattice surgery-like operations
5. **Modular syndrome extraction**: Circuits co-designed with the code structure

## Relevance

Landmark result from Google QAI + DeepMind. Solves the fundamental overhead problem of surface codes by introducing modular geometry. The 30x reduction means practical fault-tolerant quantum computing becomes feasible with far fewer physical qubits. The modular approach is also fabrication-friendly — each module can be manufactured separately and connected. This could accelerate the timeline for useful quantum computers significantly.
