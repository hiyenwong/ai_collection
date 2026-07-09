---
name: tile-code-planar-architectures
description: "Strictly local tile-code architectures for quantum error correction on 2D planar lattices. Tile codes are planar qLDPC codes with weight-6 stabilizers and open boundary conditions, offering up to 4x encoding efficiency vs. surface code. Uses SWAP-based routing schemes for syndrome extraction with nearest-neighbor interactions only, matching surface code connectivity. Activation: tile code architecture, planar qLDPC codes, SWAP routing syndrome extraction, quantum error correction architecture, surface code alternative, qLDPC on 2D lattice."
metadata:
  arxiv_id: "2607.05897"
  published: "2026-07-09"
  tags: [quantum, error-correction, qLDPC, tile-codes, planar-architecture, syndrome-extraction, surface-code]
---

# Tile-Code Planar Quantum Error Correction Architectures

## Description

Tile codes are a family of planar quantum low-density parity-check (qLDPC) codes with weight-6 stabilizers and open boundary conditions, offering encoding efficiency $kd^2/n$ up to 4x the surface code. This skill covers the design of strictly local tile-code architectures on 2D planar lattices using only nearest-neighbor interactions.

## Core Architecture

### Tile Code Properties
- **Stabilizer weight**: 6 (vs. 4 for surface code)
- **Boundary conditions**: Open (planar)
- **Encoding efficiency**: Up to 4x surface code ($kd^2/n$)
- **Connectivity**: 2D square lattice with nearest-neighbor only (matches surface code)

### SWAP-Based Routing
- Exhaustive search algorithm finds SWAP-based routing schemes for syndrome extraction
- Routes qubits through 2D lattice to enable multi-body stabilizer measurements
- Four tile-code families analyzed with explicit routed syndrome-extraction circuits

### Performance Trade-offs
- **Without routing constraint**: Threshold 0.23%-0.31% (SI1000 noise model)
- **With routing constraint**: Threshold 0.11%-0.13% (reduction factor 2-3x)
- **Crossover point**: At physical error rate $p^* \approx 0.08\%$, tile codes become more qubit-efficient than surface code
- **Below crossover**: Tile code advantage grows monotonically as physical error rate decreases

## Usage Patterns

### Pattern 1: Architecture Selection
1. Determine target physical error rate of hardware
2. If $p < 0.08\%$ (SI1000 model): tile codes offer better qubit efficiency
3. If $p > 0.08\%$: surface code may be preferable due to higher threshold
4. Evaluate routing overhead: factor of 2-3x threshold reduction must be offset by encoding efficiency gain

### Pattern 2: Syndrome Extraction Circuit Design
1. Select tile-code family from the four analyzed families
2. Use exhaustive search algorithm to find optimal SWAP-based routing
3. Construct explicit routed syndrome-extraction circuits
4. Decode with BP+OSD (Belief Propagation + Ordered Statistics Decoding)
5. Estimate circuit-level threshold under target noise model

### Pattern 3: Resource Footprint Analysis
1. Calculate physical qubits per logical qubit for tile code at target code distance
2. Compare against surface code baseline
3. Account for SWAP gate overhead in syndrome extraction
4. Include routing-induced error rate increase in total error budget

## Pitfalls

- **Threshold penalty underestimation**: Routing reduces threshold by 2-3x. Design margins must account for this, not just the nominal threshold.
- **Crossover rate dependency**: The 0.08% crossover point is specific to the SI1000 noise model. Different noise models will shift this point. Always recalculate for your hardware's noise characteristics.
- **BP+OSD decoder complexity**: BP+OSD is more complex than minimum-weight perfect matching used for surface codes. Factor in decoder latency and computational resources.
- **Four-family limitation**: Only four tile-code families were analyzed. Other families may offer different trade-offs — don't assume these four are exhaustive.
- **2D lattice constraint**: This architecture is specifically for 2D square lattices. 3D or non-square lattices may enable different routing schemes with lower overhead.

## Related Skills

- `quantum-error-correction-methods` — umbrella skill for QEC methodologies
- `surface-code-lattice-surgery` — surface code with lattice surgery operations
- `vine-codes-qldpc` — another qLDPC code family for comparison
