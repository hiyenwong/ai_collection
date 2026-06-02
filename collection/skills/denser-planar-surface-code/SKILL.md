---
name: denser-planar-surface-code
description: "Denser planar surface code methodology for quantum error correction on 2D hex grids with 4.5x encoding rate improvement over rotated surface codes. Features new stabilizer measurement cycles, padding-free lattice surgery, and Pareto frontier space-time trade-off analysis. arXiv:2605.30455."
---

## Paper

**Title**: A Denser Planar Surface Code
**arXiv**: [2605.30455](https://arxiv.org/abs/2605.30455)
**Authors**: Guang Hao Low, William J. Huggins, Dominic W. Berry, Tanuj Khattar, Alec F. White, Nicholas C. Rubin, Ryan Babbush
**Date**: 2026-05-28
**Category**: quant-ph

## Core Contribution

Presents a quantum error-correcting code implementable on a regular 2D hexagonal grid with **encoding rate up to 4.5×** that of a rotated surface code patch, under circuit-level noise at 10⁻³ error rate. Achieves **36× space** and **6.6× spacetime** improvement over previous state-of-the-art.

## Key Technical Innovations

### 1. Dense Twist Defect Packing
- Surface code **twist defects** packed densely on hexagonal grid
- New stabilizer measurement cycles with **optimal 4 layers** of nearest-neighbor two-qubit gates
- **Almost no distance-reducing hook errors**
- Enables efficient decoding

### 2. Padding-Free Lattice Surgery
- New lattice surgery protocols in **optimal bounding box** of 2d² data and measurement qubits per patch
- Eliminates padding overhead between logical qubit patches
- Space-efficient architecture for computing on densely packed logical qubits

### 3. Pareto Frontier Analysis
- Systematic space-time trade-off analysis for quantum computing resources
- **Minimum physical quantum volume**: 1.3 mega-qubit-hours
- Chemical accuracy for FeMoco nitrogen fixation catalyst (108 spin-orbitals) in <1 month with **89k noisy superconducting qubits**

## Reusable Patterns

### Pattern 1: Hex Grid Code Design
For surface code on non-square lattices:
1. Use **hexagonal connectivity** for denser qubit packing
2. Design stabilizer cycles with **minimal gate depth** (4 layers optimal)
3. Minimize hook errors through careful weight-6/weight-4 stabilizer placement

### Pattern 2: Twist Defect Optimization
- Twist defects enable **logical qubit encoding** with reduced overhead
- Pack defects at **hexagonal close-packing density**
- Design measurement schedules that **preserve code distance** while maximizing density

### Pattern 3: Resource Estimation Methodology
For fault-tolerant quantum computing resource estimates:
1. Define **target algorithm** (e.g., phase estimation for FeMoco)
2. Model **circuit-level noise** at realistic error rates (10⁻³)
3. Compute **Pareto frontier** of space vs. time resources
4. Report minimum quantum volume (qubit-hours) as unified metric

## Key Results

| Metric | This Work | Previous Best |
|--------|-----------|---------------|
| Encoding rate | 4.5× surface code | 1× (rotated surface code) |
| Space improvement | 36× | - |
| Spacetime improvement | 6.6× | - |
| Min quantum volume | 1.3 M qubit-hours | - |
| FeMoco (108 orbitals) | 89k qubits, <1 month | - |

## Pitfalls

- **Hardware topology requirement**: Requires 2D hex grid connectivity (not standard square grid superconducting processors)
- **Decoding complexity**: Dense packing may require more sophisticated decoders
- **Noise model assumptions**: Results based on uniform depolarizing noise; performance under biased noise may differ
- **Hook error sensitivity**: "Almost no" hook errors still requires careful scheduling

## Activation

**Keywords**: surface code, quantum error correction, QEC, hex grid, encoding rate, twist defect, lattice surgery, fault tolerance, resource estimation, FeMoco, nitrogen fixation, quantum volume, Pareto frontier

## Related Skills

- [[quantum-error-correction-methods]] - QEC patterns and methodology
- [[distributed-quantum-error-correction]] - Distributed QEC architecture
- [[state-adaptive-error-correction]] - Adaptive error correction
