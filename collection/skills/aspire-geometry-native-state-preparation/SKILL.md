---
name: aspire-geometry-native-state-preparation
description: Compile MPS state-prep circuits from entanglement geometry via greedy RQMI.
category: ai_collection
---

# ASPIRE: Geometry-Native Approximate MPS State Preparation

Methodology from "Breaking the chain: geometry-native state preparation with ASPIRE" (arXiv:2610.03528, quant-ph, 2 Oct 2026; Fredrik Hasselgren, Matthew L. Sims-Goh — Quantum Motion / Oxford / Melbourne).

## When to Use
- Compiling approximate state-preparation circuits for **MPS-representable states with long-ranged or non-1D entanglement**: DMRG ground states (molecules, 2D systems), multivariate amplitude-encoded functions (TCI), QPE guide states, quantum-finance distributions
- Target hardware whose connectivity is NOT a 1D chain (heavy-hex, trapped-ion all-to-all, neutral-atom reconfigurable, silicon shuttling) — avoid SWAP networks entirely
- NISQ regime (gate noise favors high-impact long-range gates, no routing) or early fault-tolerant regime (T-gate frugality: useful fidelity ≪ exact-preparation T count)
- Anywhere downstream tolerance is graceful (QPE repetition penalty only scales (1+2ε)) — exact compilation is wasteful when the MPS itself is already truncated

## Core Idea
Replace the MPD (matrix product disentangler) 1D nearest-neighbour "staircase" — whose lightcone grows ~1 site/layer, prohibitively deep for long-range correlations — with **entanglement-informed long-range gate placement**: pick gates that directly remove the most entanglement per native two-qubit gate, in parallel layers.

## Scoring: Removable QMI (RQMI)
1. Compute the two-site reduced density matrix ρ_ij via MPS contractions.
2. **One 4×4 eigendecomposition yields both the gate and its score**: the optimal disentangler U*_ij maps ρ_ij's eigenvectors (descending eigenvalue) onto |00⟩,|01⟩,|10⟩,|11⟩ — no SU(4) search needed.
3. `R_ij = S(ρ_i)+S(ρ_j) − S(ρ'_i) − S(ρ'_j)` = correlation the best gate on (i,j) can remove (bits).
4. Cost normalization: `R̃_ij = R_ij / c_ij` where c_ij = native 2q gates (3 CNOTs for a generic gate + 3 per required SWAP). Use R̃ for routed pairs, raw R for native pairs.

## Why This Is Principled (not just a heuristic)
- Total correlation `T = Σ_a S(ρ_a)` **is** the relative-entropy distance of the state to product states; the algorithm is greedy coordinate descent on this canonical distance (Prop 1)
- **Exact additivity**: gates on disjoint supports have zero cross-terms at all orders — a layer's ΔT = Σ per-gate Δ, so layer-wise matching is provably safe
- **Infidelity certificate (Thm 2)**: with Λ = Σ_a (1−λ_a) over single-site marginals of the residual, `ε* ≤ Λ/(2−Λ) ≤ Λ ≤ T/2` (tight coefficient Λ/4 for small Λ). Monitor Λ on the working state; add Fubini–Study angles δ_k for accumulated truncation
- Site-ordering invariance: T and Λ are permutation-invariant (unlike MPD's contiguous bond entropies) — snake-mapping pathologies don't hurt ASPIRE

## Algorithm Loop
```
(I)   Score all candidate pairs (i,j) admitted by connectivity matrix K → RQMI per native gate
(II)  Drop candidates below threshold τ̃ (bits/gate) or outside top decile
(III) Maximum-weight matching of disjoint pairs (Edmonds blossom, O(N³); restrict to top-32 candidates for large N)
(IV)  Apply gates to MPS (SWAP chains + bond-dimension truncation)
(V)   Recompute all ρ_ij on the updated state (a gate changes cross-marginals too); repeat
Stop: no candidate survives threshold, or native gate budget B reached
Output: C = inverses of applied gates, reversed  → state-prep circuit
```
Layer width knob: full matching commits N/2 gates per scoring; narrower layers re-score more often — no universal winner (narrower better on Heisenberg/random-MPS, full matching on TFIM); tune with budget B.

## Refinement: Unitary Procrustes sweeps
- Environment `F_m` = overlap with gate m cut out (two MPS contracted from both ends, O(N χ_w³)); SVD F=WΣV† → `U_new = W V†` maximizes |Tr U†F|; sweep gates in order until ε improvement < 1e-7 per interval
- **Warm-started selection score** `P(i,j) = ||F_ij||_1` (exact, rank-1): ranks pairs by attainable fidelity — but only fires once residual has |0…0⟩ weight (fails in S^z=0 sectors by symmetry) → schedule: k warm-start ASPIRE layers first, then switch to P-guided selection. Gains 1.5–2× infidelity reduction at matched cost

## Key Results
| Setting | Result |
|---|---|
| GHZ_N, all-to-all | exact prep in ⌈log₂N⌉ layers (optimal — any disjoint-layer circuit needs 2^D ≥ N) vs N−1 staircase |
| Bell-pair lattice (snake-mapped) | range ≥ 2L_x−1: orders of magnitude fewer gates than MPD, which can't touch most Bell connections |
| Heisenberg / TFIM ground states, random MPS | higher fidelity at equal budget; shallower circuits |
| Heavy-hex native connectivity | hardware-native gates only, no SWAPs, still beats MPD-with-routing |
| Early-FT | saturates useful fidelity with a fraction of exact-prep T count |
| Cost | candidate scan O(N²χ³)/layer; Procrustes sweep O(M·N·χ_w³) with χ_w = 2× target bond dim |

## Implementation Checklist
```python
# 1. Get target as MPS (DMRG/TCI), bond dim χ; pick working χ_w = 2χ
# 2. Build connectivity matrix K from device coupling graph (or radius r in MPS order; r=1 ≡ MPD)
# 3. Loop: eigendecompose all admissible ρ_ij → (R_ij, U*_ij); normalize by routing cost
# 4. Blossom-match disjoint top pairs; apply via SWAP chains; compress
# 5. Track Λ = Σ(1−λ_a) each layer → stop when Λ/(2−Λ) meets app tolerance (cheaper than budget exhaustion)
# 6. Optional: Procrustes sweeps; warm-start P-score after k layers if residual has product-basis weight
# 7. Compile SU(4) gates to native set; single-qubit rotations absorb free into neighbors
```

## Scope & Limits
- MPS-only input (area-law-ish); tree/belief-propagation extensions exist for other topologies but not covered here
- Working-state compression can hide correlation the recorded circuit hasn't removed — certify with the truncation-corrected bound or evaluate ε by applying C† to target afresh
- ε measured against the truncated MPS, not the true state — QPE guide-state use needs truncation error folded in
- For states whose correlations are genuinely 1D-local and short-range, plain MPD can remain competitive (check both)

## Related Skills
- `hypergraph-flow-matching-connectome-generation` — same maximum-weight-matching layer pattern
- `plasticity-network-framework` / other greedy-descent skills — this one descends a *canonical* relative-entropy distance with exact additivity, a reusable justification pattern
- `bbqram-state-preparation-finance` — state prep for finance amplitudes (ASPIRE alternative for multivariate functions)
- `qcnn-signature-kernels` — unrelated but shares tensor-network compile lineage
