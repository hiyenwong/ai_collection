---
name: hyperbolic-surface-code-geometry-optimization
description: "Use when constructing or benchmarking hyperbolic surface codes, optimizing code distance via periodic identifications, or modularizing non-Euclidean codes for hardware."
category: ai_collection
---

# Geometry-Optimized Hyperbolic Surface Codes (arXiv:2610.10948)

**Paper**: "Geometry-optimized hyperbolic codes for modular fault-tolerant quantum architectures" — Mahmoud & Rayan (Univ. of Saskatchewan quanTA, 2026-10-07)

Hyperbolic surface codes with kd²/n = C(log k)² scaling (Delfosse bound) — beyond the BPT O(1) limit of Euclidean codes — made hardware-realistic via distance-doubling periodic identifications and topology-aware modular compilation.

## Construction: self-dual prime-field {p,p} codes

- Tiling group: triangle group Δ_p = ⟨x, y | x^p = y^p = (xy)² = 1⟩; finite quotient Q = Δ_p/Γ_PBC ≅ **PSL(2,q)**, q prime, |Q| = q(q²−1)/2.
- Data qubits on edges (n = |Q|/2), Z-check per face, X-check per vertex — weight p each, each qubit in 2 checks of each type; ancillas = 4n/p; k = 2g (genus); rate k/n = (p−4)/p + 2/n.
- **Self-duality**: projective involution J ∈ PGL(2,q), y = JxJ⁻¹ (split/non-split); orbit-representative dedup under centralizer of J.
- **Exhaustive search** p ∈ {5,6,7,8} × 17 primes q<60 → 2,304 generator pairs → 38 classes. Global optimum: **{6,6} [[51330, 17112, 10]], η = kd²/n ≃ 33.34** (vs toric code η=1, ×33; vs best hyperbolic Floquet η≈5.01, ×6.65).

## Distance doubling at zero cost (central result)

At FIXED tiling, q, n, k, check weight: different periodic identifications (generating maps) change the systole (shortest non-trivial homology cycle = d). {7,7} q=41: identifications give d = 4, 6, or 8 → **choosing the best map doubles d, quadruples η, with no extra physical resources**. Practical rule: always enumerate quotient-group generator orbits before fixing boundary conditions; distance is a property of the COMPACTIFICATION, not just the tiling.

## Finite-size scaling (Delfosse-consistent)

Selected sequences (smallest code per new max distance):
- {5,5}: [[30,8,3]]→[[330,68,6]]→[[1710,344,8]]→[[7440,1490,10]]→[[51330,10268,12]], η 2.40→28.81; fits η ≈ 0.328(ln k)² + 1.53, R²=0.996.
- {7,7}: [[84,38,3]]→[[546,236,5]]→[[6090,2612,7]]→[[17220,7382,8]], η 4.07→27.44; η ≈ 0.347(ln k)² − 0.148, R²=0.998.
Distance grows linearly in ln k; efficiency grows with (ln k)² — optimal log-squared scaling realized by explicit finite codes.

## Topology-aware modular compilation (Algorithm 1)

Partition closed hyperbolic code into planar modules (B_max=80 qubits each; module = strict topological disk: connected, single boundary loop, no handles):
1. **Face partition** on dual graph: seed M regions far apart (max dual-graph distance), grow one face at a time prioritizing small regions / more shared edges; reject moves violating disk condition or face bounds f_min=⌊0.8F/M⌋, f_max=⌈1.2F/M⌉.
2. **Qubit assignment**: interior data qubits follow their faces; boundary qubits optimized against cost C̃ = Σ_c [10|S_c| − max_b t_cb + |{b: t_cb>0}| − 1] + Σ_b [max(0, ℓ_b − L)]² (t_cb = data qubits of check c in module b; L = target load).
3. **Validate**: capacity + planarity + connectivity, then compute 5 communication metrics: R (remote interactions/round), K (check fragmentation Σ(|modules per check|−1)), communicating module pairs, max partners, max remote load.

Benchmarks: {5,5} 92,394 qubits → 1,155 modules, R=69,021 (33.6% of 4n CNOTs remote). Topology-aware beats tested RSB on all 5 metrics (RSB often infeasible: only 1.8–11.2% connected modules); Mt-KaHyPar gets lower R but violates ALL geometric constraints (65–81% connected, 6 nonplanar modules) and higher K. Init-sensitivity δ<0.6% across 5 runs.

## Circuit-level thresholds under noisy long-range gates

Stim + PyMatching (MWPM), SI1000-inspired noise: local CNOT error p, **remote/inter-module CNOT error αp (α∈{1,2,3})**, reset 2p, meas 5p, idle p/10 (p/2 in wait layers); d rounds of Z-memory; circuit-fault distance D < homological d (D=4,5,7,8 vs d=6,8,10,12) — schedule-dependent.

- α=1: threshold ≈ **0.22%** (modular & monolithic identical circuits).
- α=3: **0.17%** (modular) / **0.18%** (monolithic) — i.e. tripling remote-gate error only degrades threshold ~22%/17%. Modular pays slightly more (more nonlocal CNOTs: 33.6% vs 31.6%).
- Conclusion: hyperbolic codes retain finite threshold under realistic long-range-gate penalties; efficiency gains (×4–33 over Euclidean) can justify the routing cost.

## Reusable patterns

1. **Boundary-condition optimization**: for any quotient-group surface code, search generator orbits for max systole — free distance at fixed resources.
2. **Disk-constrained partitioning**: spectral/KaHyPar baselines violate planarity+connectivity; enforce topological-disk growth with rejection + dual-graph farthest-seeding instead.
3. **αp remote-gate noise model**: benchmark modular vs monolithic by penalizing only designated nonlocal CNOTs — architecture-agnostic threshold comparison.
4. **Metric pair (R, K)**: remote-interaction count alone underestimates fragmentation cost; report K alongside.
5. Threshold estimation: median of pairwise code-size curve intersections, ≥10k shots/point, stop at 1000 failures or 250k shots, Wilson 95% intervals.
