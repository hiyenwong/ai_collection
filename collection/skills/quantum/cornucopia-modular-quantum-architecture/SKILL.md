---
name: cornucopia-modular-quantum-architecture
description: Use for modular qLDPC FTQC design. Symmetry-orbit gadgets.
category: ai_collection
---

# Cornucopia Modular Quantum Architecture

**Paper**: A modular quantum computer based on Cornucopia codes (arXiv:2610.19073, Lu, Li, Ma, ..., Deng — Tsinghua/SQZ, 13 Oct 2026)

## Core Problem

Ultra-high-rate qLDPC codes (rate > 1/2) store thousands of logical qubits per block cheaply, but a quantum **memory is not a computer**: universal logical operations on *individually addressable* logical qubits normally require heavy ancilla (logical representatives weigh far more than code distance), eroding the encoding-rate advantage. The paper turns one [[2844, 1426, 18]] Cornucopia block (1,426 logical qubits in 4,266 physical, logical error 2.6e-16/qubit/cycle @ p=1e-3) into a **universal logical processor** at 4.1 physical qubits/logical qubit (vs 3.0 for memory alone; bicycle architecture needs 61.2).

## Architecture Blueprint

### 1. Symmetry-adapted canonical basis (the enabling trick)
- The column translation T (shift all data tiles one column) is a **code automorphism** — it commutes with all checks.
- Apply **Gottesman's standard form to whole symmetry orbits** (symmetry-adapted standard form), not individual qubits: partition the 36 fibres into 9 X-pivot + 9 Z-pivot + 18 free information fibres.
- Result: **18 cyclic registers of 79 logical qubits** + 4 invariant modes = 1,426. T acts as cyclic shift (i, t) → (i, t+1).
- Consequence: **one gadget built for logical qubit (i, 0) is automatically a certified gadget for all 79 qubits of register i** — 54 seed gadgets cover all single-qubit Pauli measurements on 1,422 register qubits.

### 2. Representative weight optimization (three freedoms, applied jointly)
- Optimize the canonical basis over: (a) fibre partition choice — randomized search + **simulated annealing** (11,580 → 4,060 total seed weight), (b) polynomial symplectic shears (greedy, 17 steps → 3,740; mixes registers, exits standard form), (c) stabilizer dressing. Final seed weights 62–231 vs distance-18.

### 3. Certified graph-surgery gadgets
A gadget = connected graph; vertices = new checks, edges = new ancilla qubits. Rules:
- Each vertex attaches to ≤1 qubit in the support of the target's physical representative P.
- Every old check that anticommutes locally with P is **deformed onto skeleton edges**.
- One extra check per cycle of a complete cycle basis (prevents encoding spurious logicals).
- Distance preservation certificate: edge expansion h ≥ 1 ⟺ **λ2 > 2** (second-smallest Laplacian eigenvalue), proven with **exact certificates** — for the translation-covariant fixed extractor the Laplacian decomposes into 79 Fourier blocks (40 inequivalent, 54×54); certify each block exactly (λ2 = 2.501).

### 4. Load-aware cycle bases (degree control)
Spanning-tree cycle bases route many cycles through edges near the root → ancilla degree up to 256. Fix: add short cycles **one at a time, preferring edges whose current load (number of acting checks) is low** — any invertible transformation of the cycle basis leaves the merged stabilizer group unchanged. Result: ≤ 9 checks per ancilla data qubit. **Reusable principle: since cycle-check transformations are stabilizer-preserving, use the freedom to balance degree/load instead of accepting combinatorial defaults.**

### 5. Matching bridges (b ≥ d edges + b−1 square cycle checks)
Join two compatible gadgets (vertex attachments on shared data qubits carry the same Pauli factor) with a bridge of b ≥ d ancilla edges: merged code measures exactly the product of targets, distance preserved. b ≥ d is **tight** — X on the b bridge qubits is itself a logical operator. 18-edge bridges give distance exactly 18. Every gadget carries a **fixed 18-vertex port**; two-qubit XjXk / ZjZk = two translated seeds + port bridge, no pair-specific optimization. The SAME bridge mechanism does magic-state injection (d=18 surface patch holding |T⟩, bridge to seed, X-basis readout = teleportation up to Pauli correction) and **inter-module links** (extractor-to-extractor, teleportation = 1 inter-module ZZ + 1 local X; CNOT = work qubit + 3 measurements, only 1 crossing the boundary).

### 6. Three universal instruction sets (complementary tiers)
- **IB (basic)**: single-qubit X/Y/Z + two-qubit XX/ZZ on all register qubits, |T⟩ injection. Minimizes workspace per op.
- **IH (high-throughput)**: direct sums of compatible gadgets in ONE merged code; local compatibility rules (Prop. 2) predict all check weights/degrees without assembly; shortcut hyperedges when accumulated deformations would exceed weight 16. Greedy packing: up to 37 simultaneous single-qubit measurements, 9 bridged two-qubit, 20 simultaneous |T⟩ injections; random 3,000-instruction workloads average **19.3 instructions/layer ≈ 20× logical-depth reduction**. Native weight-36 operator families (block-convolutional latent rows: 79 translates partition the data qubits, 78 independent outcomes per family; 6 families = 468 commuting multi-qubit observables).
- **IF (fixed extractor)**: ONE ancilla system (21,330 ancilla data qubits on the Tanner graph, connections software-selected) measuring **any** logical Pauli product; Fourier-block λ2 > 2 certificate covers all 4^1426−1 targets at once. Makes Pauli-based computation (e−iπP/8 via |T⟩ source + Clifford correction) native.

## Reusable Engineering Patterns

1. **Symmetry-orbit standard form**: when a code has an automorphism group, derive logical bases/gadgets per ORBIT, not per qubit — construction cost amortizes over the orbit (54 gadgets → 1,422 addressable qubits).
2. **Exact certificates over spectral conditions**: replace per-instance numerical checks with a single spectral property (λ2 > 2) proven per Fourier block — verification cost decouples from the number of software-selectable targets.
3. **Load-aware basis selection**: stabilizer-preserving freedoms (cycle-basis transformations) are free optimization dimensions — use them for physical-degree balancing.
4. **Bridge-as-universal-interconnect**: one bridge mechanism (b ≥ d edges + cycle checks) serves two-qubit measurement, module interconnect, and magic-state injection — minimize distinct interface types in modular architectures.
5. **Tiered instruction sets**: basic (min workspace) / high-throughput (max ops per cycle) / fixed-extractor (max expressiveness on fixed hardware) — expose the same logical ISA at three hardware cost points and let the compiler choose.
6. **Space-time trade-off quantification**: 1 workspace = 3,000 cycles; high-throughput = 151 cycles avg at ≤29,755 qubits (3.9× space-time volume reduction); extractor = 1 cycle per high-weight Pauli product.

## Key Numbers

| Quantity | Value |
|---|---|
| Code | [[2844, 1426, 18]], rate 1/3, weight-12 checks |
| Physical/logical (memory) | 3.0 |
| Physical/logical (memory + full basic workspace) | 4.1 |
| vs bicycle (Tour de gross, 119 modules) | 61.2 per logical |
| Fixed extractor total | 46,927 physical qubits |
| Seed gadget ancilla | 179–752 data qubits; bridged 376–772 |
| Merged-code constraints | wmax ≤ 16, Δmax ≤ 8–16, distance exactly 18 |
| Native families | 6 × 79 translates, 468 commuting observables, weight 36 |

## Limitations / Open Items
- Distance guarantees are for merged codes; **circuit-level distance** depends on syndrome-extraction schedule (future work). Logical error per instruction not yet established by circuit-level simulation.
- Invariant modes reachable only via extractor; four modes not in basic set.
- Hardware mapping to reconfigurable atom arrays (ancilla placement, atom motion for bridges) not yet done.

## Related Skills
- [[aries-qisa-ftqc-instruction-hierarchy]] — instruction-hierarchy FTQC control stacks
- [[logical-catalyst-dyadic-phase]] — surface-code cultivation for reusable catalysts
- [[round-robin-sparsification-addressable-gates]] — addressable transversal CZ
- [[ultra-high-rate-quantum-codes]] — high-rate code design
