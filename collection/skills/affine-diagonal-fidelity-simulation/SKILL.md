---
name: affine-diagonal-fidelity-simulation
description: Benchmark noisy non-Clifford FT circuits via affine-diagonal backpropagation.
category: ai_collection
---

# Exact Fidelity Simulation of Affine-Diagonal (Non-Clifford) Fault-Tolerant Circuits

Methodology from "Efficient fidelity simulation of high-rate magic distillation circuits" (arXiv:2610.03605, quant-ph, 2 Oct 2026 dated 5 Oct; Xiao Xiao, Dominik Hangleiter, J. Pablo Bonilla Ataides, Rohan Mehta, Varun Menon, Mikhail D. Lukin, Michael J. Gullans — QuEra / UMD QuIC / Berkeley Simons / ETH Zürich / Harvard).

## When to Use
- Estimating logical fidelity / syndrome statistics of **noisy fault-tolerant circuits containing non-Clifford gates** (T, CCZ, controlled-S, IQP blocks) under circuit-level stochastic Pauli noise
- Benchmarking magic-state distillation/cultivation factories, encoded IQP sampling, transversal-CCZ qLDPC protocols — including **high-rate codes** where #logical qubits is large
- Deciding whether a Pauli-twirl approximation of correlated CCZ fault propagation is trustworthy (compare against exact)
- Designing Z-syndrome extraction / postselection strategies for magic factories

## Core Insight
**Benchmarking a fault-tolerant non-Clifford circuit is easier than fully simulating it.** Full simulation is classically hard (faults propagate to non-Pauli operators; cost exponential in non-Clifford count / magic). But if you only need syndrome statistics + logical fidelity + Pauli observables, you can **backpropagate everything to the input** and the ideal non-Clifford evolution cancels from the overlap.

## Affine-Diagonal Circuit Family
- Gates: {X, CNOT} ∪ diagonal level-ℓ Clifford-hierarchy gates (T, CS, CCZ ∈ D_n^(3))
- Equivalent to CNOT-dihedral: the only non-Clifford element is R_ℓ = diag(1, e^{2πi/2^ℓ})
- Normal form: `U = D_f · A` where A ∈ affine group A_n (bit-linear Lx+b), D_f = phase polynomial exp[2πi f(x)/2^q]
- Level formula: gate with phase precision q and monomial degree g has hierarchy level (q−1)+deg(g)
- Covers: triorthogonal & 3D color codes (transversal T), 3D surface codes (transversal CCZ), rainbow/GBP/sheaf/product qLDPC codes with transversal-T or constant-depth-CCZ, plus arbitrary Clifford circuits before/after, plus teleportation gadgets with feedforward (via unitary rewriting)
- Requirement: ideal circuit maps input stabilizer subspace to output stabilizer subspace (code deformations, logical gates, syndrome extraction all qualify)

## Hierarchy-Reduction Lemmas (the engine)
- **Lemma 1**: propagated Pauli error `U P U† ∈ X · D_n^(ℓ−1)` — one level DOWN per propagation
- **Lemma 2**: commutator of two propagated errors `[E1, E2] ∈ D_n^(ℓ−2)` — TWO levels down
- Consequence for ℓ=3 (T/CCZ circuits): propagated faults are Clifford (X·D^(2)), and their pairwise commutators are **Z-type Paulis** — this is what makes syndrome sampling exact and polynomial

## Algorithms (per sampled Pauli fault configuration e)
1. **Syndrome sampling (exact, ℓ≤3)**: Backpropagate e and every final stabilizer measurement M to input. `⟨M⟩ = Tr[(e^ini)†, M^ini] ρ^ini` — a Z-Pauli for AD(3), so deterministic ±1 outcomes form a linear subspace V ⊆ Z_2^m. Syndrome distribution is **uniform on the affine space s₀ + V⊥**. Solve via: symplectic-inner-product table B, kernel basis G (Gaussian elimination), shift solve Gs₀=a, sample s = s₀ + Nz. → pairs with **any decoder and any postselection rule**
2. **Logical fidelity**: `F_out = Σ_{e,s} p_e |⟨ψ|C_s†C_e|ψ⟩|²` — both C_s (recovery) and C_e (fault) are Clifford ⇒ each term is a **stabilizer-state overlap**. Missing syndrome bits supplied by perfect virtual measurements + Pauli recovery
3. **Pauli observables**: O ∈ X·D^(2) propagated = Clifford ⇒ conditional expectations on stabilizer states, polynomial per sample
4. **ℓ=4 extension**: unbiased estimators of individual stabilizer-check expectations (commutator = Clifford circuit overlap)

**Cost**: O(n³T) per Monte Carlo sample after preprocessing (constant # fault layers per check); **no dependence on number of logical qubits** (unlike prior cultivation work) — this is what unlocks high-rate codes. Measured: precompute scales n^2.51 for hypercube-IQP [[8,3,2]] up to n=256.

## Application: Tricycle [[27,3,3]] Magic Factory (depth-2 transversal CCZ)
Protocol space explored (single-shot |+⟩^L prep in 3 data blocks → CCZ network → 9-qubit encoded hypergraph state):
- Z-syndrome strategies: none / noiseless-lower-bound / bare ancillas / Steane-style per-block / **one shared ancilla block** (best)
- Shared-block with **metacheck repair** > metacheck postselect; infidelity ≈ 1e-7 scale at ~0.5 acceptance, 10:1 Z-biased 2-qubit depolarizing 1e-3 + CCZ noise 2e-3
- **Exact simulation validates Pauli-twirl approximation** for this protocol family (no large deviation) — twirled-CZ-error channel on the input state is a safe shortcut here
- BP+OSD decoding throughout; extra fictitious Z round at end to correct back to code space for fidelity accounting

## Also Handles
- **Cultivation checks**: H_XY = (X+Y)/√2 measurement via CNOT + level-3 diagonal gates (color codes, RP2 surface codes); Steane-code H-state cultivation via frame change `(I⊗K†)CH(I⊗K) = T†·CS·CNOT ∈ AD(3)` — Pauli errors stay Pauli in the new frame
- **Hypercube-IQP**: [[2^D, D, 2]] code blocks on hypercube vertices, CCZ from 8 transversal T gates; benchmarking classically-hard sampling demonstrations under noise

## Implementation Checklist
```python
# 1. Put circuit in affine-diagonal normal form U = D_f·A (level ℓ ≤ 3 for exact sampling)
# 2. Verify U Π_in U† = Π_out (stabilizer-subspace mapping incl. feedforward rewrites)
# 3. Monte Carlo loop over Pauli fault configurations e:
#    a. Backpropagate e + measured stabilizers to input
#    b. Build commutator table (Z-Paulis for ℓ=3); find deterministic subspace V
#    c. Sample syndrome uniformly on s0 + V⊥; apply your decoder/postselection
#    d. Fidelity term = |⟨ψ|C_s† C_e|ψ⟩|² (stabilizer overlap — use Stim/tableau)
# 4. Average; for ℓ=4 use the unbiased per-check estimators instead of exact syndromes
# 5. Sanity-check any twirled approximation against exact on a small instance first
```

## Scope & Limits
- Circuit-level **stochastic Pauli noise only** — coherent errors, atom loss out of scope (open direction)
- Exact syndrome sampling limited to ℓ≤3; ℓ≥5 diagonal gates not covered
- Requires the ideal circuit to preserve stabilizer subspaces (universal-computation interleavings of AD blocks + Clifford remain open, though Clifford layers before/after are free)
- Independent concurrent works exist on FT non-Clifford benchmarking ([50,51] in paper) — check before claiming novelty

## Related Skills
- `gkp-qldpc-circuit-benchmarks` — circuit-level benchmarks of BB/tricycle qLDPC codes (the tricycle family this paper simulates)
- `lottery-bp-decoding`, `bf-osd-qldpc-decoding` — decoders compatible with the sampled syndromes
- `borrowed-identity-magic-distillation` — distillation protocol side (this skill = the benchmarking simulator side)
- `logical-catalyst-dyadic-phase` — cultivation-style reusable logical ancillas
