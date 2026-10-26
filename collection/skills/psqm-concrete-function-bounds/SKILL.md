---
name: psqm-concrete-function-bounds
description: PSQM bounds for equality, majority, and AND functions.
trigger: private simultaneous quantum messages, PSQM, PSM communication complexity, secure multiparty computation noninteractive, referee privacy, GHZ protocol, entanglement-assisted communication, unique preimage impossibility, qudit protocol, multicolored sum-free family, communication complexity lower bounds
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: quantum-auction-summation-reductions, genuinely-nonlocal-sets-discrimination, no-signaling-quantum-games-operator-algebra, information-science-quantum-security, private-capacity-superactivation
---

# PSQM Concrete-Function Bounds: Quantum Advantages vs Unique-Preimage Barrier

**Source**: arXiv 2610.23090 (Harumichi Nishimura, Nagoya University, Oct 2026). Communication complexity of PRIVATE SIMULTANEOUS QUANTUM MESSAGES (PSQM) for familiar total functions — k players with private classical inputs each send ONE message to a referee (no interaction); referee must recover f(x) and learn nothing beyond it; messages may be quantum; prior entanglement + shared classical randomness allowed.

## Central Contrast (the reusable insight)

PSQM complexity is NOT determined by algebraic simplicity of the function. Majority-type functions (symmetric accepting sets) get genuine entanglement advantages; functions with a UNIQUE PREIMAGE (AND, point functions) hit a rank-based obstruction in the one-qubit local-unitary model that only increasing local dimension (qutrits/qudits) removes. The structure of accepting/rejecting input sets — not circuit complexity — governs private quantum communication.

## Results Table

| Function | Classical PSM | Entanglement-assisted PSQM |
|---|---|---|
| EQ_{k,n} (k-party equality of n-bit strings) | ≥ kn bits | ≤ √(k/(2h₂²(1/k)))·n + O_k(√n) qubits; k=3: (1.633...)n |
| EQ_{k,n} without entanglement | — | ≥ kn qubits (any shared classical randomness) → strict separation for fixed 3 ≤ k ≤ 9 |
| MAJ3 | 6 bits (optimal, Shinagawa–Nuida) | 3 qubits: one shared GHZ + local Pauli encodings + one transmitted qubit per player, perfect correctness AND perfect privacy |
| EQ3 | 3·log₂3 bits (optimal) | 3 qubits (local parity twist of the MAJ3 protocol) |
| AND3 | [6, 3·log₂5] bits (open classically) | IMPOSSIBLE in one-qubit local-unitary model; ≤ 3·log₂3 qubits via one 3-qutrit GHZ + one qutrit per player → strict advantage vs 6-bit lower bound |
| ANDk (k≥3) | ≤ k·log₂ℓ_k bits | ≤ k·log₂p_k ≤ k·log₂k qubits, p_k = smallest prime with k ≤ 2(p_k−1), p_k ≤ k by Bertrand's postulate |

Plus: protocols for exactly 80 three-bit Boolean functions — writing the ANF f(x,y,z) = c ⊕ ax ⊕ by ⊕ dz ⊕ αxy ⊕ βxz ⊕ γyz ⊕ δxyz, whenever δ = 0 and (α,β,γ) ∈ {(0,0,0), (1,0,0), (0,1,0), (0,0,1), (1,1,1)}.

## Technique 1 — Multicolored Sum-Free Family Embedding (equality upper bound)

Reduce EQ to generalized equality via combinatorial embeddings: use the asymptotically tight tri-colored sum-free family (Kleinberg–Sawin–Speyer, completed by Pebody) giving local embeddings into F²_d with d = √(n/h₂(1/3)) + O(√n) → the 1.633n = √(3/(2h₂²(1/3))) coefficient; general fixed k via Lovász–Sauermann constructions. For ODD k, the known protocol incurred a dummy-user penalty; remove it with a one-shot FOUR-COORDINATE SECURE-SUM layer (inspired by Lu–Yao–Jafar odd-party secure sum) on top of a binary physical two-user Bell primitive, applied blockwise over the embedding.

## Technique 2 — GHZ Labels + Local Pauli Encodings (3-bit functions)

One shared GHZ state; each player's input selects a local Pauli (or small unitary) encoding applied to their GHZ qubit, which they then transmit. The referee's 3-qubit measurement distinguishes exactly two output-dependent density operators ϱ_0, ϱ_1 (perfect correctness), and each individual message is input-independent given the output (perfect privacy). Shared randomness compressible to 2 bits while preserving the same pair of output-dependent density operators. A local parity twist on the MAJ3 protocol yields EQ3.

## Technique 3 — Unique-Preimage Impossibility (rank sandwich)

For any f: {0,1}^k → {0,1} where some output value has EXACTLY ONE preimage (all point functions, ANDk, and complements — WLOG the unique input has output 1):
1. Perfect correctness forces vanishing overlaps between the unique input's received state and the states under any nonempty set of input flips.
2. One-qubit structural lemma (Lemma 2.4): for single-coordinate flips these vanishing-overlap conditions force the relative unitaries to be Hermitian involutions up to global phase.
3. The full family of flip conditions then yields 2^k − 1 MUTUALLY ORTHOGONAL pure-state components inside ϱ_0 (the referee's output-0 state) → rank(ϱ_0) ≥ 2^k − 1.
4. The one-qubit structure + perfect privacy confine ϱ_0's support to a 3-dimensional local-action subspace → rank(ϱ_0) ≤ 3.
5. Incompatible for k ≥ 3 → NO perfectly correct and perfectly private protocol exists in the one-qubit local-unitary model, for ANY shared k-qubit mixed state and ANY local U(2) encodings.

This is a rank lower bound (correctness, via purification) sandwiched against a rank upper bound (privacy) — a transferable proof pattern for referee-only privacy models.

## Technique 4 — Qudit Escape via Zero-Sum-Free Constructions (ANDk upper bound)

A zero-sum-free construction ensures the all-ones input is distinguished from every other input; finite-field randomization hides WHICH rejecting input occurred. For every prime p with k ≤ 2(p−1): one p-dimensional qudit per player, total cost k·log₂p. Bertrand's postulate guarantees p ≤ k. For k=3: p=3, one shared three-qutrit GHZ, total 3·log₂3 ≈ 4.75 < 6-bit classical lower bound.

## When to Use
- Bounding communication in noninteractive secure MPC / referee-only privacy architectures (PSM/PSQM model and variants).
- Deciding whether to spend entanglement vs message dimension: symmetric functions → GHZ; unique-preimage functions → qudits, not more entanglement.
- Proving impossibilities in one-message quantum privacy models: adapt the rank-sandwich (orthogonality from correctness, dimension confinement from privacy).
- Connections: PSQM ↔ nonlocal quantum computation / position verification (coherent function evaluation), low-T-depth referee → classical-message PSM transforms.

## Pitfalls
- Two-party AND2 DOES have a one-qubit entanglement-assisted protocol (Bell pair + one qubit each, Christensen–Popovski over prime fields; optimal classical cost 2·log₂3 bits) — the unique-preimage obstruction STARTS at k = 3. Do not over-generalize the impossibility.
- The impossibility is specific to the ONE-QUBIT LOCAL-UNITARY model (arbitrary shared state, U(2) encodings); it is not a PSQM lower bound — the qutrit protocol beats it.
- Without prior entanglement, EQ needs ≥ kn qubits EVEN with arbitrary shared classical randomness — entanglement, not shared randomness, drives the separation.
- AND3's exact classical complexity remains OPEN ([6, 3·log₂5] bits); the quantum advantage statement is vs the 6-bit lower bound only.

## References
- arXiv 2610.23090 — Concrete Functions in Private Simultaneous Quantum Messages (Nishimura)
- Kawachi–Nishimura (PSQM model introduction), Shinagawa–Nuida (optimal classical bounds for MAJ3/EQ3), Girish–May–Orshansky–Waddell (robust exponential separations), Lu–Yao–Jafar (odd-party secure sums).
