---
name: zx-diagram-entanglement-magic-bounds
description: Use when bounding entanglement or magic of ZX-diagrams.
category: quantum
---

# ZX-Diagram Entanglement & Magic Bounds (arXiv:2610.12447)

**Paper**: "Entanglement entropy and magic of ZX-diagrams" — Szyniszewski, Shaikh, Kissinger (Oxford, 2026-10-08)

Estimate bipartite entanglement entropy AND magic (log stabilizer extent) of a quantum state **directly from its ZX-diagram**, with NO tensor contraction and NO exponential optimization — even when the state has volume-law entanglement.

## Core Method: Flow-Based Normal Form

Any ZX-diagram with **flow** (ZX-flow ≡ Pauli flow up to Cliffords) converts in polynomial time to:

```
|ψ⟩ = U_N ··· U_1 |G⟩ ,   U_i = exp(-i·φ_i·P_i/2)
```

- `|G⟩` — graph state (stabilizer backbone; may carry EXTENSIVE entanglement, still free)
- `U_i` — **Pauli gadgets** (Pauli exponentials with possibly non-Clifford phases φ_i)

This separates the two complexity resources: graph-theoretic stabilizer entanglement vs. additive non-Clifford deformations.

## Bound 1: Entanglement Entropy (von Neumann, bipartition A|B)

Let `Γ_AB` = adjacency submatrix of the graph across the cut; `C` = gadgets whose Pauli support CROSSES A|B:

```
S ≤ rank_F2(Γ_AB) + Σ_{i∈C} h₂(sin²(φ_i/2))
S ≥ rank_F2(Γ_AB) − Σ_{i∈C} h₂(sin²(φ_i/2))
```

- `rank_F2` — rank over the 2-element field (efficient even when extensive; classical stabilizer result)
- `h₂(x) = −x·log₂x − (1−x)·log₂(1−x)` — binary entropy
- **Exact in the Clifford limit** (all φ = kπ/2 → gadget terms vanish)
- Rényi-α version: replace h₂ by `h₂,α(x) = (1−α)⁻¹·log₂(x^α + (1−x)^α)` in the upper bound; use conjugate index `α' = 1/(2−1/α)` in the lower bound (asymmetric unless α=1)
- vs. generic entangling-capacity bounds: improvement from linear to **quadratic-logarithmic scaling** in small φ — stays informative at depths where generic bounds saturate [0, min(|A|,|B|)]

## Bound 2: Magic (logarithmic stabilizer extent)

```
M(|ψ⟩) = log₂ min_{|ψ⟩=Σα cα|φα⟩} (Σα |cα|)²   ≤   2·Σ_{i∈O} log₂(√(1−|sin φ_i|) + √(1−|cos φ_i|))
```

- `O` = all gadgets whose Pauli is NOT a stabilizer of the current state
- **No branch-interference assumption needed** (unlike entropy bounds)
- Additive over gadgets, vanishes at Clifford angles, tight near stabilizer limit

## Validity Condition & Preprocessing (critical!)

Entropy bounds hold when branches do NOT coherently interfere: `P_{i1}···P_{ik} ≠ γ·Stab(|G⟩)` for any gadget subsequence (γ=±1 even k, ±i odd k). Preprocessing to enforce/tighten:

1. **Gadget fusion**: fuse commuting gadgets with identical Pauli supports (automatable via PauliOpt) → single gadget with φ₁±φ₂
2. **Stabilizer fusion**: within a commuting region, fuse two gadgets whose Paulis differ by a stabilizer of the preceding state
3. **Clifford unfusing**: gadgets with |φ| > π/4 → split off residual Clifford part, push to graph state
4. **One-sided exclusion**: if P_i × (stabilizer) lands entirely in one subsystem, remove from crossing set C

Only pairwise fusions are searched — generic/random circuits work well; **repeated structure (Trotter/Floquet) is vulnerable** (observed first violation at step 64 = Clifford-circuit periodicity).

## Numerical Results

| Setup | Result |
|---|---|
| Random Clifford+small-phase, L=20, depth 400 | Bounds track exact entropy; 0 violations over 300 realizations |
| Trotterized XY Z Hamiltonian + Clifford layers, L=26 | Generic bounds fill trivial interval; Eq.(2) tracks until step 64 |
| Magic: random + monitored circuits, L=8 | Exact magic nearly SATURATES the bound; measurement frequency p drives magic→stabilizer crossover |

## Tooling

- **PyZX** — construct/simplify ZX-diagrams, flow extraction
- **PauliOpt** — Pauli gadget manipulation/fusion
- Monitored circuits still have flow: Z-strings commute through CNOT layers, phases, and Z-projectors

## When to Use

- Estimating entanglement/magic of deep or large circuits where statevector/tensor-network methods are infeasible
- Resource-aware ZX compilation cost functions
- Probing measurement-induced entanglement/magic transitions diagrammatically
- Volume-law states where bond-dimension methods fail

**Activation**: zx-calculus, zx-diagram, entanglement entropy bound, stabilizer extent, magic estimation, pauli gadget, graph state, flow, rank f2, binary entropy, monitored circuits, pyzx
