---
name: sharp-pairwise-reduction-pgm-hypothesis-testing
description: Use when bounding PGM error in quantum state discrimination.
category: ai_collection
---

# Sharp Pairwise Reduction for Quantum Hypothesis Testing (PGM)

Source: Lee & Lami (Scuola Normale Superiore, Pisa), arXiv:2609.28440 [quant-ph], 23 Sep 2026.

## Core Result

**Theorem 1 (Pairwise reduction, sharp constant):** For every finite ensemble {A_i = p_i rho_i} (any Hilbert space dimension, finite or infinite, trace-class included):

Err*_N <= Err^pg_N <= 4 * SUM_{i<j} Err*_{ij}

where Err* is the optimal (Holevo-Helstrom) error and Err^pg is the pretty-good-measurement error. The coefficient **C = 4 is uniformly optimal** — no smaller constant works even for arbitrary global measurements.

This improves: (a) Cheng-Liu's C = 8 (arXiv:2606.06246), (b) resolves Audenaert-Mosonyi Conjecture 2.3 with the numerically suggested constant, and (c) gives the guarantee for the *standard PGM itself* (not a hard-to-implement sequential construction).

## Methodological Pipeline (reusable)

### Step 1: Reduce N-ary to pairwise benchmark
- Binary sub-problem has closed form: Err*(X,Y) = (Tr X + Tr Y - ||X-Y||_1)/2 (Holevo-Helstrom trace-norm formula).
- Goal shape: control global error by C * sum of pairwise binary errors, with C dimension- and N-independent.

### Step 2: Block Gram matrix representation of PGM
- Define D = diag(A_1..A_N), T = (A_1^{1/2} ... A_N^{1/2}), G = T^T T (block Gram matrix), S = TT^T = sum A_i.
- Polar decomposition: T^T S^{-1/2} T = G^{1/2}.
- PGM error = sum of squared Hilbert-Schmidt norms of off-diagonal blocks of G^{1/2}: Err^pg_N = sum_{i!=j} || (G^{1/2} - D^{1/2})_{ij} ||_2^2.

### Step 3: Hellinger-chi2 inequality (constant one)
Proposition 2: For X, Y >= 0, with Omega_Y = (L_Y + R_Y)/2 (left/right multiplication superoperators):
||X^{1/2} - Y^{1/2}||_2^2 <= <X - Y, Omega_Y^{-1}(X - Y)>

In the joint eigenbasis E^XY_{ij} = |x_i><y_j|, (L_X + R_Y) acts diagonally with eigenvalue (x_i + y_j), reducing the operator inequality to the scalar pointwise inequality (sqrt(x) - sqrt(y))^2 <= (x-y)^2/(x+y). This removes the factor-2 loss of prior work (Fact 2.25 + Prop 2.31 of tomography literature) — **essential** for sharpness.

### Step 4: Link quadratic forms to binary errors
Proposition 3: <X^{1/2}Y^{1/2}, (L_X + R_Y)^{-1}(X^{1/2}Y^{1/2})> <= Err*(X, Y).
Proof trick: define block-row superoperator T_op = L_{X^{1/2}} R_{Y^{1/2}} with T T^dag = L_X + R_Y; take W = Pi* Y^{1/2} ⊕ X^{1/2}(1-Pi*) for the Helstrom projector Pi*; then the quadratic form is bounded by ||W||_2^2 = Err*(X,Y) exactly.

### Step 5: Sharpness via regular simplex
Ensemble: A_i = |v_i><v_i|/N with <v_i|v_j> = -1/(N-1) (regular simplex in C^{N-1}). Both binary and global errors are explicit; the ratio of pairwise-sum to global error tends to 4 as N -> infinity, proving no constant < 4 is universally valid. Global error via dual SDP form Succ* = min Tr Y s.t. Y >= A_i, with candidate Y = 1/N giving Succ* = Succ^pg = (N-1)/N, i.e., Err* = 1/N.

### Step 6: One-shot pairwise Chernoff bound + copy complexity
Theorem 4: Err^pg_N <= 4 * sum_{i<j} alpha(s_ij) Tr A_i^{s_ij} A_j^{1-s_ij}, alpha(s) = s^s(1-s)^{1-s} in [1/2, 1), coefficient optimal per pair. Scalar proof: sup_t t^s/(t+1) = (1-s)^{1-s}s^s attained at t = s/(1-s).

Finite-copy corollary (s = 1/2, epsilon = max pairwise overlap sqrt of rho_i rho_j):
Err^pg_N(n) <= 2 sum sqrt(p_i p_j) epsilon^n <= (N-1) epsilon^n
=> sufficient copies n >= [log(N-1) - log delta] / log(1/epsilon) for global PGM error <= delta. Saves log 2/log(1/epsilon) copies vs the prior Chernoff branch (Cheng-Liu).

## Reusable Patterns

1. **Superoperator diagonalization**: left/right multiplications commute even when operators don't; their joint eigenbasis (Petz quasi-entropy basis) converts operator inequalities to scalar pointwise ones. Applicable to any quantum divergence manipulation.
2. **Block Gram analysis**: PGM/square-root measurement error decomposes into pairwise Hilbert-Schmidt blocks — try this before union-bound/sequential constructions.
3. **Harmonic-mean quadratic forms**: the quadratic form <X^{1/2}Y^{1/2}, (L_X+R_Y)^{-1}(...)> is the natural bridge between Hellinger-type distances and Helstrom binary error.
4. **Sharpness witness construction**: to prove a universal constant optimal, build symmetric ensembles (regular simplex) where all pairwise quantities are explicit and take N -> infinity limit.
5. **Trace-class extension by cutoff**: finite-rank truncation Pi_m A_i Pi_m converges (Prop 5), extending finite-dim proofs to bosonic/Fock settings (Gaussian optical ensembles without photon-number truncation).

## Applications

- State discrimination benchmarks: pairwise binary errors become a universal benchmark for both optimal and PGM global error.
- Copy complexity of discrimination: explicit n(delta) formulas.
- Bosonic/Gaussian state discrimination without photon truncation.
- Certified tomography: Bures chi2-to-Hellinger conversion without factor-2 loss (chi2 error <= eps implies Hellinger^2 <= eps at same confidence).

## Related Results in Corpus

- quantum-channel-steins-lemma (arXiv:2609.27196): asymptotic channel discrimination, complementary one-shot reduction.
- sequential-quantum-hypothesis-testing: composite hypothesis extension.
- Barnum-Knill theorem: PGM within factor 2 of optimal — this work supplies the pairwise-side guarantee.

## Verification Notes

- Constant-4 sharpness: ratio of pairwise-sum to global error for regular simplex -> 4 as N -> inf (explicit Helstrom formula + dual SDP).
- Theorem 4 constant: scalar concavity argument only.
