---
name: syndrome-mediated-deterministic-t-gates
description: Use when implementing fault-tolerant logical T gates on stabilizer codes.
category: ai_collection
---

# Syndrome-Mediated Deterministic Fault-Tolerant T Gates

**Source**: Bharti (QuICS/IonQ), Haug (TII), Tanggara (CQT/NTU), arXiv:2609.29890 (24 Sep 2026). Establishes a **general mechanism** for logical non-Clifford gates: a syndrome degree of freedom mediates an exact logical T gate on **every stabilizer code of distance d ≥ 2**, in a suitable logical basis — no magic-state distillation required.

## Core Mechanism: Two Rotations + One Syndrome Measurement

### 1. Logical Pauli factorization
For a Hermitian logical Pauli L ∈ N(S)\S, find Hermitian Pauli factors with **AB = iL**:
- Factors anticommute {A,B} = 0 (since BA = −iL)
- **Shared syndrome**: syn(A) + syn(B) = syn(L) = 0 ⟹ s := syn(A) = syn(B) ≠ 0 required (A must leave the code space)
- Balanced construction (Theorem 2): shared qubit q ∈ supp(L), partition remaining support into S_A ⊔ S_B, single-qubit Paulis A_q B_q = iL_q, then A = A_q ⊗ Π_{j∈S_A} L_j, B = B_q ⊗ Π_{j∈S_B} L_j
- Weight optimality: wt(A)+wt(B) ≥ wt(L)+1; balanced gives max factor weight ⌈(d+1)/2⌉ — **optimal among all factorizations of a minimum-weight logical**

### 2. The two-rotation identity (Theorem 1)
Apply R_B(π/4) then R_A(π/2), then measure the syndrome of C:
- Expansion: R_A(π/2)R_B(π/4) = (1/√2)R_L(π/4) − (i/√2)(cos(π/8)A + sin(π/8)B)
- First term preserves C; second maps C into the syndrome-s sector → **two orthogonal, equally-likely branches** (Pr(0)=Pr(s)=1/2)
- Branch correction: for outcome s, apply A then R_L(π/2); A returns the state to C carrying R_L(−π/4), and R_L(π/2)R_L(−π/4) = R_L(π/4) — both branches implement the **same** logical T up to phase.
- **Deterministic**: no postselection on branch outcome; feed-forward only.
- Pauli-only variant: replace R_A(π/2) and the conditional Clifford by adaptive Pauli measurements (G = iAh with outcome y, M = AhL with outcome r, h with outcome z; final Pauli rule L iff y=−1 and rz=−1). Every executed correction is a Pauli.

### 3. The intermediate code D (where protection lives during rotation)
- Both rotations preserve C ⊕ AC (B|ψ⟩ = iA(L|ψ⟩) ∈ AC since L preserves C).
- Retained checks S₀ = {g ∈ S : [g,A] = 0} — exactly **half** the stabilizer group (commutation-sign homomorphism S → ±1). D = code of S₀ encodes **k+1 qubits**: original k + one syndrome qubit p with X̄_p = A, Z̄_p = h (omitted check).
- Identification D ≅ C ⊗ C²: |ψ̄⟩ ↔ |ψ̄⟩⊗|0⟩_p, A|ψ̄⟩ ↔ |ψ̄⟩⊗|1⟩_p.
- **Intermediate distance (Theorem 4)**: δ = min{d, µ(s), ν(A)} where µ(s) = min weight of Pauli with syndrome s, ν(A) = min weight of stabilizer anticommuting with A.

### 4. Purity vs bounded checks (Theorem 5) — when protection grows
- **Pure code** (all nonidentity stabilizers ≥ d) + balanced factorization: d/2 ≤ δ = µ(s) ≤ (d+1)/2 → **δ grows with d**. 
- **Bounded-weight checks** (weight ≤ w generators, incl. ALL quantum LDPC families: surface/color codes): δ ≤ ν(A) ≤ w **no matter how large d** — protection during rotation is capped by check weight. Structural no-go for direct application to LDPC.

## Why Intermediate Distance ≠ Fault Tolerance
A single faulty location can hit the full rotation-axis support; a fault anticommuting with a later rotation axis **reverses the remaining angle** → undetectable logical error. Requirements beyond δ: controlled fault propagation through compilation (CNOT ladders: weight-w factor needs 2(w−1) CNOTs), correction after propagation, and measurement of checks that may not preserve D mid-circuit.

## Two Protected Constructions (single-fault tolerant, local stochastic noise)

### A. Fixed [[22,1,3]] code via selective concatenation
- Outer Steane [[7,1,3]]; rotations touch outer qubits 1, 2, 4.
- **Selective concatenation**: encode ONLY the rotation-touched qubits — qubit 1 (shared by both factors) in [[15,1,3]] Reed–Muller (transversal T supplies the non-Clifford layer, no CNOTs for that rotation), qubit 2 in 2-qubit Z-repetition, rest unencoded.
- Clifford-image encoding C_B C₀ makes the non-Clifford factor B′ = Z₁ → non-Clifford rotation = single transversal T-type layer.
- Theorem 7: 22 data qubits, **15 physical T-type gates**, Pauli measurements/corrections only, ≤33 qubits serial w/ ancilla reuse+reset. Recursive: level ℓ → 22^ℓ data, 15^ℓ T-gates, ≥2^ℓ faults needed, distance 3^ℓ → **positive threshold** via concatenation.

### B. Protected Golay [[23,1,7]] via transported check + monitor
- Keep pure Golay block; balanced factorization → intermediate [[23,2,4]] (µ(s)=4, ν(A)=8).
- **Transported check (Lemma 8)**: G_B = U_B h U_B† = (h − iBh)/√2 where U_B = R_B(π/4) — Hermitian, non-Pauli Clifford; the rotated state is a +1 eigenstate. Measuring G_B = measuring h in the rotated frame.
- **Exact angle filter (Lemma 9)**: Π₊R_B(π/4+ε)|ψ⟩ = cos(ε/2)R_B(π/4)|ψ⟩ — coherent overrotation errors projected out.
- **Local filter (Theorem 10)**: pure code, wt(B) = w < d ⟹ on rotation support Ω_B, only Paulis I and B commute with all retained checks (binary rank 2w−1) → every nonidentity Pauli fault on Ω_B detected **with certainty**; accepted state ideal for arbitrary coherent errors on that support.
- Monitor circuit: 2 verified 4-qubit cat states; recursive circuit-gauge method (Dasu–Criger) on released syndrome; rejection → full-syndrome extraction + decoder restricted to modeled support recovers **unknown input even after arbitrary errors on all of Ω_B** (incl. entanglement with external system) → gate retried.
- ≤32 qubits serial, 22 single-qubit T-type gates per attempt.

## Reusable Patterns
1. **Syndrome as a resource** — release a stabilizer constraint to expose an extra logical qubit inside the same block; use it to mediate gates, then restore via measurement + feed-forward.
2. **Factorized logical Paulis (AB = iL)** — split a logical into two physical factors sharing a syndrome; balanced factorization minimizes rotation support ⌈(d+1)/2⌉.
3. **Branch-invariant gadgets** — design rotations so syndrome measurement has few outcomes and Clifford feed-forward makes every branch implement the same logical operation (deterministic from stochastic parts).
4. **Transported observables** — conjugate a known-eigenvalue check through a unitary to get a measurable filter for the rotated state; doubles as an exact angle filter for coherent errors.
5. **Selective concatenation** — concatenate only the qubits touched by the dangerous operation, choosing inner codes per Pauli axis (RM for transversal-T, repetition for Z); get recursion + threshold without full-code overhead.
6. **Intermediate-code analysis** — always compute the code during the gate: δ = min{d, µ(s), ν(A)}; purity ⟹ δ ~ d/2, bounded-check families ⟹ δ ≤ w (LDPC caveat).

## Comparison to Alternatives
| Method | Non-Clifford source | Protection during gate |
|---|---|---|
| Magic-state distillation/cultivation | Ancillary resource consumed by teleportation | Gate itself is Clifford-only |
| Code switching / gauge fixing | Transversal gates of partner codes | Switching cost |
| This paper | In-block rotations + syndrome projection | Intermediate code D + monitor/selective concat |
Unbalanced factorization (S_B = ∅) reproduces state injection's ideal logical channel — the framework **contains injection as a special case**.

## Pitfalls
- LDPC/surface codes: bounded check weight caps intermediate distance at w — the direct gadget is NOT protected; use concatenated/monitored variants.
- Angle reversal: faults anticommuting with a later rotation axis flip remaining angles — a fault-path ambiguity that final syndrome cannot resolve (must be designed out, cf. Lemma 17).
- For the fixed 22-qubit code, replacing the transversal T† layer by T + Cliffords **breaks** the single-fault guarantee (Proposition 18).
- Complied multi-qubit rotations don't preserve D at intermediate steps — FT proofs must track propagation at specified correction/measurement points only.

## Verification Hook
Simulator test: Steane code, A = X₁Z₂, B = Y₁Z₄ (AB = iZ̄, Z̄ = Z₁Z₂Z₄), omitted check h = Z₁ (Fig. 1). Ideal circuit: R_B(π/4), R_A(π/2), syndrome measurement, feed-forward → logical R_Z̄(π/4) on every input state, 50/50 branch statistics, intermediate code [[7,2,2]].
