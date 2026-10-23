---
name: patchwork-lattice-surgery-parallel-decoding
description: Use for lattice surgery or parallel surface-code decoding.
trigger: lattice surgery, multi-qubit Pauli measurement, real-time decoding, commit buffer cleanup regions, wavefront partitioning, twist defect, logical Y measurement, DEM partitioning, surface-code compiler, multi-commodity Steiner routing, exponential decoding backlog
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: lattice-surgery-surface-code, surface-code-lattice-surgery, spacetime-lifting-quantum-fault-tolerance, real-time-qec-system-stack, sparse-mamba-decoder-qec, speculative-window-decoder-qec
---

# Patchwork: Automated Lattice Surgery + Space-Time Partitioning for Real-Time Decoding

**Source**: arXiv 2610.22112 (Chamberland, Li, Thornton, Lietz, Ren, deMarti iOlius — NVIDIA, Oct 2026). A lattice-surgery compiler for arbitrary multi-qubit Pauli measurements (PPMs) on narrow-corridor 2D surface-code layouts, plus a wavefront algorithm that partitions merged patches into space-time commit/buffer/cleanup regions for parallel decoding.

## Problem It Solves

1. A logical Pauli measurement requires compatible patch geometry + stabilizer placement + measurement schedule; Y measurements add twist defects that can cut effective code distance. Manual constructions don't scale with measurement weight.
2. Merged patches grow with the number of participating logical qubits → monolithic decoding latency grows; real-time decoding is required to avoid the exponential backlog problem (decode time exponential in consecutive non-Clifford gates).

## Component 1 — Narrow-Corridor Layout

Unit cells of 4 logical patches. Vertical routing corridors width d+3, horizontal height d+1. Green strips inside corridors constrain where stabilizers may be placed. Checkpoint lines (intra-cell ICCL, vertical-corridor VCCL) mark where a corridor-crossing stabilizer triggers ELONGATION of the adjoining stabilizer column — systematic resolution of stabilizer-type/ancilla conflicts instead of ad-hoc fixes.

## Component 2 — Multi-Commodity Steiner Routing

Model the routing network as graph G=(V,E): vertices = corridor junctions, edges = allowed junction connections, UNIT capacity on both edges and vertices (vertex capacity forbids two measurements crossing at a shared junction). Each PPM = one commodity with a root patch; connectivity enforced root→every terminal via Steiner trees solved JOINTLY across all concurrent PPMs. Branches of the same tree may share corridor segments; distinct measurements may not.

## Component 3 — Stabilizer Zoo and Y Measurements

- Bulk weight-4 (e/f schedules), boundary weight-2, elongated rectangles (weight-4/3/2 spanning inactive sites), domain walls (dw1 = Z⊗Z⊗X⊗X, dw2 = X⊗X⊗Z⊗Z), weight-5 twist (X⊗X⊗Z⊗Y⊗X).
- Logical Y measurements via twist defects + Y-EXTENSION patches with PROTRUDING LOBES that occupy existing routing corridors (no physical-layout change). At d ≤ 11, exhaustive numerical search found no logical failures from ≤ (d−1)/2 circuit faults → full effective code distance preserved for the validated constructions. Alternatives: doubled corridors, or ancilla-assisted decomposition of Y into X⊗Z measurements.

## Component 4 — Logical Observables

Spacelike observables via a common boundary-walk procedure on the merged-patch boundary (X reps, Z reps, Y-extension reps, consistent endpoint boundaries, label dedup); timelike observables for measurement outcomes across the d rounds. Cut lines / junction cells specify where gate schedules change to keep fault propagation controlled as observable orientations change.

## Component 5 — Wavefront Space-Time Partitioning (CORE)

Spatial commit/buffer/cleanup construction per connected merged patch (d odd ≥ 3):

1. **Seed commits**: one per participating logical patch. X/Z seeds = full patch footprint; Y seeds = full Y-extension patch EXCLUDING protruding lobes.
2. **Seed pairing**: neighboring seeds (same PPM, joinable within ≤ d+3 active steps) combine if both-Y or both-non-Y, no third-seed data enclosed, span ≤ bounds L_{X/Z} = 3d+3, L_Y = 4d+4. Chains pair into adjacent pairs + one unpaired when odd.
3. **Wavefront extension**: propagate ℓ_seed = (d+1)/2 active steps outward from each seed face exposed to measured routing corridors; retain measured stabilizers/data determining the enclosure; rectilinear boundary completion. KEY EFFICIENCY: fill the measured enclosure and merge equivalent propagation states — do NOT enumerate all length-ℓ paths. If an extended face lies < d steps from the merged-patch boundary, extend it to the boundary (blocks cleanup regions from connecting around the seed). Observed construction cost ~O(d³) (numerical evidence, not a proven bound).
4. **Buffers**: depth d wavefront from each commit's exposed perimeter. Buffers supply syndrome context; corrections are APPLIED ONLY to commit data. Buffer data outside commits stay cleanup-owned.
5. **Cleanup separators**: one-coordinate-wide horizontal/vertical lines (L/T/cross combinations allowed), placed ≥ 1 step beyond the protected ℓ_seed extension, spanning the full local corridor, satisfying connectivity + stabilizer-ownership conditions (a stabilizer touching both commits must also touch separator data). For Y chains: midpoint cuts — horizontal chains get vertical separators (left-middle column if two), vertical chains get horizontal separators (upper-middle row); only the specified midpoint is tested; if invalid, interface stays uncut.
6. **Child commits**: for far-apart seeds, place additional commits along corridors to bound cleanup size. From an endpoint seed's buffer, propagate d active steps → candidate frontier; next d steps → pre-buffer; further d-step construction → child commit. Elongated edges count as one step. Children cover complete junctions (if a child would land within distance d of a junction, shift it to own the whole junction; separator segments inside become commit-owned). Rebuild buffers after every placement/move.
7. **Final coalescence**: any measured stabilizer fully owned by two commits forces their combination (repeated until none); enclosed single rows/columns with all-stabilizer support in one commit are absorbed; cleanup regions = connected components of remaining data. Ownership rule: a stabilizer belongs to a commit iff its ENTIRE active support lies inside it; otherwise cleanup-owned (may still inform via buffers).

**Temporal extension**: each PPM measured over d rounds, consecutive PPMs separated by d idle rounds (idle rounds = temporal buffer during commit decoding, temporal cleanup after). A shared idle interval between consecutive measurements is created once. Decoding volumes are 3D (space × the d rounds).

## Component 6 — DEM Partitioning and Staged Decoding

- Build local DEMs with Stim from the syndrome-extraction circuit + noise model. Commit decoders observe commit+buffer volumes; only commit-owned error components contribute to the correction response.
- All commit decoders act on the ORIGINAL syndrome in parallel; their responses' full detector+logical effects are XOR-ed (mod 2) into the global syndrome. Cleanup then decodes the residual: remaining effect of fault e is r_e = (d_e, ℓ_e) ⊕ ⊕_i (∆D, ∆L)(c_i[e]) — e.g. fault flips {a,c}, selected commit response flips {a,b} → cleanup sees edge {b,c} with the ORIGINAL fault probability (correction changes the represented effect, not the probability).
- Cleanup regions are decoded together (transitive grouping) iff their allowed corrections can change a common detector outcome. Sharing DEM information alone does NOT force grouping.
- Independent-execution safety is verified by checking correction effects on DEM detectors (not by proximity heuristics).

## Verified Results (paper, single-p circuit-level depolarizing noise)

ExpD: 3 sequential PPMs on 10 logical qubits including Y factors (P1 = Y⊗Z⊗Z⊗X⊗X⊗X, P2 = Z⊗Z⊗X, P3 = Y⊗Y⊗Y⊗Y), 12 deterministic logical parity observables, p ∈ {0.001..0.005}, d ∈ {5..21}: staged (commit-then-cleanup) total failure rate ≈ monolithic decoding — slightly higher, with discrepancies ONLY from failure events of size > (d−1)/2. DEM scaling: 16 random PPMs per weight w ∈ {2,4,8,16,32,64} at d=11 — largest commit/cleanup areas grow sublinearly vs full merged-patch area (data-qubit sites).

## When to Use

- Compiling arbitrary multi-qubit Pauli measurements (Clifford + non-Clifford via magic-state-free joint measurements) on 2D local-connectivity surface-code layouts.
- Partitioning decoder workloads so merged-patch decoding latency stays flat as measurement weight grows (spatial block-wise decoding complements temporal window decoding of memory experiments).
- Fault-tolerant logical Y measurement constructions that provably preserve effective code distance.
- Sizing real-time decoding resources: number/area of parallel commit decoders + one cleanup pass.

## Pitfalls

- The d idle rounds between consecutive PPMs are REQUIRED by the current wavefront algorithm: a logical qubit in both P_j and P_{j+1} needs its seed-commit assignment to hold; without idles it would need a spatial-cleanup assignment during P_{j+1}, a variant left to future work.
- Trimming protruding lobes reduces effective code distance — lobes are distance-preserving only in the validated configurations (d ≤ 11 exhaustive checks; shortening them voids the guarantee).
- O(d³) construction cost is numerical evidence over tested geometries, not a theorem for arbitrary routing.
- Cleanup grouping criterion is correction-effect overlap, not DEM sharing — grouping by shared DEM info alone over-serializes.
- A cleanup separator must satisfy stabilizer-ownership conditions: a stabilizer supported entirely on the two facing commits re-merges them.

## References
- arXiv 2610.22112 — Patchwork: automated lattice surgery and space-time partitioning for real-time decoding (NVIDIA).
- Integration target: CUDAQ Logical framework; planned ~100-logical-qubit real-time decoding experiments.
