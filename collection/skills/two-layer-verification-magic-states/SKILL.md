---
name: two-layer-verification-magic-states
category: ai_collection
description: Use when verifying magic-state prep in multi-logical codes.
version: "1.0.0"
source: arXiv:2610.32267
source_title: "Two-Layer Verification for Fault-Tolerant Magic-State Preparation in High-Rate Quantum Codes"
authors: "Naoyuki Kanomata, Hayato Goto (RIKEN RQC / Toshiba)"
author: qc-cron-2026-10-27
license: MIT
published: 2026-10-23
categories: quant-ph
metadata:
  hermes:
    tags: [quantum-computing, ftqc, magic-states, high-rate-codes, qec, fault-tolerance]
    related_skills: [trident-yoked-surface-code-memory-hierarchy, syndrome-mediated-deterministic-t-gates, magic-distillation-code-limits, spidercss-fault-tolerant-css-state-preparation, fault-tolerant-ancilla-preparation-bch]
arxiv_id: "2610.32267"
trigger_words:
  - magic state preparation
  - high-rate quantum codes
  - logical verification
  - product-type verification
  - even-parity ambiguity
  - zero-level distillation
  - magic state cultivation
  - error-detecting teleportation
  - Steane code magic state
  - '"[[21,3,5]] code"'
---

# Two-Layer Verification for Fault-Tolerant Magic-State Preparation

## When to Use

- Preparing encoded magic states (T/S/CCZ-type) in a HIGH-RATE code with k > 1 logical qubits, where the only transversal check is a PRODUCT of logical verification operators.
- Designing fault-tolerant state preparation that must beat first-order logical-error scaling (postselection leaving O(p_sub) residual → need O(p_sub²)).
- Extending physical-level verification / zero-level distillation / cultivation-style ideas to multi-logical-qubit blocks (bivariate-bicycle, hypercube, symplectic-double codes).
- Deciding whether an embedding-circuit design (subblocks + residual entangler) is verifiable at all.

## The Even-Parity Ambiguity (the problem)

Magic states are +1 eigenstates of Clifford operators (T state ↔ HXY = (X+Y)/√2 = TXT† = e^(−iπ/4)SX; all identities numerically verified). Suppose the target [[n,k,d]] code supports only a TRANSVERSAL PRODUCT of the k logical verification operators (true whenever transversal gates implement the tensor product over all logicals). The collective measurement yields only

```
Π_V = Π_j v_j = (−1)^E     (E = number of flipped verification eigenvalues)
```

Odd E flips the sign → detected. EVEN E leaves Π_V = +1 → UNDETECTED. In a high-rate code, two-logical-qubit errors occur at rates comparable to single-logical errors, so the even-parity channel leaves a leading FIRST-order contribution that no amount of product checking removes. (Product checks alone detect exactly odd flip counts — verified.)

## The Two-Layer Scheme

**Layer 1 (subblock verification):** prepare each constituent state — one per logical qubit of the target code — independently in its own small subblock and verify it there (e.g. Steane-code T states verified with physical CNOT/T/T† circuits via Steane's Clifford transversality + flag qubits + Reichardt-type syndrome checks). Only accepted subblock states advance.

**Embedding:** SWAP network rearranges physical qubits; a residual entangling circuit maps the k verified subblock states into the target code. (Derive by decomposing the arbitrary-state encoder: reorder CNOTs with the exchange rule — two noncommuting CNOTs swap at the cost of one compensating CNOT.)

**Layer 2 (product verification + error detection):** measure the transversal product-type logical verification on the embedded block, then run fault-tolerant syndrome measurements (error-detecting teleportation, EDT) to catch residual/embedding errors. Accept only if ALL local checks AND the product check AND syndrome checks pass.

**Effect:** layer 1 removes the per-subblock first-order term; the product check's even-parity blind spot now acts only on ALREADY-verified subblocks, so residual failure is second order in the subblock logical-error probability. Replacing T by S states gives an all-Clifford circuit ("magic state emulation" / Clifford-proxy simulation) enabling Stim-scale simulation of the pipeline.

## Concrete Instance: self-dual CSS [[21,3,5]] Code

- Stabilizers H_X = H_Z (9×21 binary, self-dual): H·H^T = 0 mod 2, rank 9 → k = 21 − 2·9 = 3 (all verified). 18 X+Z stabilizer generators; distance 5 verified by exhaustive enumeration of span(H,M)\span(H) (min logical weight = 5).
- Transversalities (self-duality + identical X/Z logical matrices): HL1HL2HL3 = H^⊗21, XL1XL2XL3 = X^⊗21, ZL1ZL2ZL3 = Z^⊗21, YL1YL2YL3 = −Y^⊗21, SL1SL2SL3 = S†^⊗21; transversal CNOT via CSS structure. This product transversality is exactly what layer 2 consumes.
- Logical Paulis (rows of M, verified): ZL1 = Z1Z4Z5Z6Z7Z8Z19, ZL2 = Z2Z5Z6Z7Z8Z9Z20, ZL3 = Z1Z2Z3Z5Z6Z8Z13 (X-type identical by self-duality; M·H^T = 0, M·M^T = I mod 2).
- Encoder decomposition: arbitrary-state encoder = 3 Steane-code magic-state subblocks + SWAP network + residual entangling circuit (zero-state encoder: 63 CNOTs → 44 after overlap-method reduction; add input-state CNOTs by Gaussian elimination on stabilizer+logical matrices).
- Layer-2 syndrome extraction: EDT (Knill-style error-detecting teleportation) with two logical zero states; EDT's own error detection allows cheap zero-state prep (flag-CNOT zero encoder instead of full Z-error detection circuit).
- Decoding: lookup-table decoder on the 8 relevant syndrome bits (enumerate weight-≤4 patterns; 2^8 rows) — near-optimal for this code size.

## Noise Model & Verified Results

Circuit-level noise: state prep/measurements bit-flip at p_circ; each CNOT followed by one of the 15 non-identity 2-qubit Paulis at p_circ/15; 1q gates/memory negligible. Logical failure = any of the 3 logical outputs wrong, conditioned on acceptance.

```
p_L ∝ p_circ^α :  α_T,ideal = 2.93(2)   (Qulacs, 3.36e7 shots/rate)
                 α_S,ideal = 3.04(2)   (Stim, 1.12e9 shots at p=1e-3,2e-3)
                 α_S,EDT  = 3.16(1)   (noisy EDT; still ~cubic)
```

~CUBIC scaling = distance-5 fault-tolerant behavior — physical-level faults need ≥3 faults to cause an accepted logical failure. T- and S-state preparations perform comparably (evidence the Clifford-proxy methodology is faithful). Logical-CNOT benchmark: p_block = 1−(1−p10)^(1/10) over 10 transversal-CNOT+ECT rounds, exponent 2.97(3). At p_circ ≈ 0.1% the S-state prep needs FEWER physical qubits than one FT logical CNOT — the low-space-overhead selling point vs magic-state distillation factories.

## Design Recipe (porting to another high-rate code)

1. Check the target code admits a transversal PRODUCT of the logical verification operators (self-dual CSS with matching X/Z logical matrices gives this for free).
2. Find an independently-preparable/verifiable subblock per logical qubit: small code with transversal logical Clifford + flag-based physical-level verification (Steane [[7,1,3]] is the canonical choice for HXY-type magic states).
3. Decompose the arbitrary-state encoder into subblock encoders + SWAP network + residual entangler (CNOT-exchange rule for reordering; overlap method for CNOT reduction).
4. Layer 2 = product-type logical verification (transversal physical gates, e.g. CNOT+T+T† pattern per logical) + fault-tolerant syndrome extraction (EDT with cheap logical zeros, or standard FT syndrome measurement).
5. Accept-condition = AND of all subblock checks ∧ product check ∧ syndromes. Validate with Clifford-proxy (S-state) simulation first — Stim handles k>1 stabilizer circuits at 1e9+ shots; reserve state-vector (Qulacs) for the true T-state spot checks.
6. Fit p_L vs p_circ on a log-log plot; demand α ≥ ~3 (code-distance-limited) before believing the construction is fault tolerant.

## Pitfalls

- Product-type verification ALONE is never sufficient at k ≥ 2: the even-parity channel is leading-order, not a correction.
- The embedding circuit is NOT fault tolerant by itself (single fault propagates through CNOTs) — it is only safe sandwiched between the two verification layers.
- EDT zero states can skip dedicated Z-error detection only because EDT catches those errors downstream — do not reuse that encoder outside an EDT context.
- pdftotext of this paper drops the matrix bracket structure (H renders as 7 visible rows; there are 9) and drops the superscript in the lookup-table row count (2^8, not "28").

## Verification Notes (2026-10-27 run)

All committed code claims verified from first principles (script verify_twolayer_20261027.py, 15 checks ALL PASS): HXY Clifford identity chain + |T⟩ eigenstate; H self-orthogonality (H·H^T=0), rank 9 → k=3; logical commutation (M·H^T=0) and canonical anticommutation structure (M·M^T=I); explicit ZL1..ZL3 == rows of M; code distance d=5 by exhaustive 4096-element coset enumeration; even-parity detection condition.
