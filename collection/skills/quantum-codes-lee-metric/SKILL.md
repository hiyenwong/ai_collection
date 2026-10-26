---
name: quantum-codes-lee-metric
description: Design qudit codes for small-shift noise via the Lee metric.
category: ai_collection
trigger: Lee metric, qudit codes, small-shift noise, helical repetition code, Lee-LDPC, clock/shift errors, qudit QEC, Gray map qubitization, high-temperature quantum memory, GKP discretization
---

# Quantum Codes in the Lee Metric

**Source**: Guo, Han, Chakraborty, Jain, Liu, Albert, Lucas (CU Boulder / NIST-UMD), arXiv:2610.04834 [quant-ph + math.CO cross], Oct 2026.

## When to Use

- Qudit (q-dim) QEC where noise is dominated by SMALL Pauli shifts (X^±1, Z^±1 more likely than X^±2): nuclear-spin qudits, clock-transition ions, molecular spins.
- Designing codes whose distance should count shift magnitude, not number of qudits touched.
- Assessing whether large-q qudits give a real QEC advantage (they mostly don't for LDPC — see bounds below).
- Building high-temperature passive memories / self-correcting codes from on-site Hilbert-space growth.
- Qubitizing Z4 qudit codes for hardware with only qubits.

## Core Framework

### 1. Two Lee metrics for Pauli strings X^x Z^z (x, z ∈ Z_q^n)
- **Separate metric**: pair (|x|_L, |z|_L) — for CSS codes.
- **Joint metric**: |x|_L + |z|_L. For qubits it counts Y as weight 2, X/Z as 1 — appropriate when bit/phase flips are independent processes.
- Lee weight per site: min(x_i, q − x_i) (distance on the cyclic Z_q clock, NOT number of nonzero entries).
- Key inequality: d_H ≤ d ≤ ⌊q/2⌋ d_H for CSS codes — Lee distance can grow unboundedly with q at fixed n (unlike Hamming).

### 2. Better codes at small q (joint metric)
Maximize joint Lee distance over single-qubit Clifford frames for ≤9-qubit stabilizer codes:
- **[[9,1,5]]** corrects any two X/Z errors or any single Y — Hamming needs 11 qubits for two errors.
- **[[6,1,4]]** reaches a distance no [[6,1]] stabilizer code reaches in Hamming.
- Joint ≤ 2×separate; they coincide for CSS.

### 3. Perfect Lee codes (sphere-packing saturation)
- Single qudit Z_10 with stabilizer X²Z⁴; two-qudit families on Z_{3m}; **[[6,4,3⋄]]_5**.
- CSS perfect families from classical Golomb–Welch perfect Lee codes: distance-3 CSS codes on n ≥ 3 qudits of dim 2n+1 when n mod 3 ≠ 1.
- **Eastin–Knill FAILS in Lee metric**: the perfect two-qudit Z_10 code corrects all weight-1 errors yet admits continuous transversal family exp(iθ X₁X₅). (Metric-dependent theorem — No-Go is about the error model, not fundamental.)

### 4. CSS with torsion — Smith normal form machinery
- Codespace of classical code = SNF of parity-check H: C ≅ ⊕ Z_{d_i} (torsion factors = logical dits of dim < q).
- Quantum CSS logical quotient ker(H_Z)/im(H_X^T) = homology of an integer chain complex (Thm 4.5); SNF gives logical qudit dims dividing q + explicit conjugate logical-operator pairs.
- **Exact CSS/GKP correspondence** (Prop 4.12): Z_q stabilizer codes = multimode GKP codes; 1 unit Lee weight = one elementary GKP displacement (2π/q). Lee metric is the discretized displacement metric.

### 5. Fault tolerance — Lee-weight spread of Clifford gates
- Spread w_B(U) = max Lee weight of a column of U's symplectic matrix (Lemma 5.2).
- Phase gate, SUM gate: spread 2. MUL2: spread (q−1)/2 for odd q.
- Fault distance of logical Clifford ≥ ⌈d⋄ / (2 w_B(U))⌉.
- **Transversal ≠ automatically FT**: on perfect n-qudit codes, one fault before MUL_a^⊗n (a ≠ ±1) causes logical error for every weight-1-correcting decoder.
- Spread-1 gates (mod Paulis/phases) = qudit permutations + single-qudit Fourier — the natural equivalence of Lee stabilizer codes.
- Self-dual CSS (H_X = H_Z): every single-qudit Clifford G gives transversal G^⊗n up to Pauli correction; on Z_5 Reed–Solomon these realize the whole logical Clifford group ≅ binary icosahedral group (order 120).

### 6. Qubitization via quantum Gray map
- Gray map 0,1,2,3 → 00,01,11,10 is an isometry Lee(Z_4^n) → Hamming(Z_2^{2n}); promote to unitary relabeling each quartrit by 2 qubits.
- Z_4 Paulis → qubit Cliffords; Z_4 Cliffords → **level-3 Clifford hierarchy** (Thm 6.2).
- Qubitized code is a qubit Clifford stabilizer code iff φ(C) linear + closure condition (Prop 6.7); smallest instance = **[[4,1,2]] Chuang–Leung–Yamamoto** code.
- Semi-self-dual codes qubitize without distance loss (Cor 6.6); self-dual Z_4 CSS codes give 2-fold transversal non-qubit-Clifford gates after qubitization.

### 7. Lee-LDPC obstruction (the negative result)
For any (w_B, w_C)-Lee-LDPC CSS code on n qudits over Z_q:
- **Thm 7.7**: some nontrivial logical operator has energy barrier ≤ O(n).
- **Thm 7.8**: every noncommuting logical pair has a noncommuting witness of Lee weight ≤ O(n).
- ⇒ **Lee distance O(n) uniformly in q**. Proof: relax Z_q → R and apply geometry-of-numbers transference theorems. Large internal Hilbert space does NOT buy high-Lee-distance LDPC codes.

### 8. Helical repetition codes — the positive surprise
- Checks: a·x_j = b·x_{j+1} (mod q), coprime a > b ≥ 1. Codewords = geometric progressions with ratio a/b mod q.
- **Lee distance grows EXPONENTIALLY with n** (for q large enough).
- Two mechanisms for exp. memory time under single-site ±1 Metropolis:
  1. **Energetic** (PBC, q = a^n − b^n): code is linearly sound + confining (syndrome Lee weight ≈ Lee distance to codeword); memory exp in q at any fixed T. Evades Peierls 1D no-SSB because q grows with n.
  2. **Entropic** (open BC): energy barrier only O(n), yet memory ≥ e^{cn} once q > temperature-dependent multiple of n — flat logical direction with exponentially long path; leaving costs O(q). Glassy free-energy landscape (App H).
- **Hypergraph products** of helical codes → local 2D quantum CSS codes inheriting self-correction for Z errors (exp memory once q ≫ n² log q); X-sector self-correction OPEN.
- Whether a quantum Lee-LDPC code can protect BOTH sectors at arbitrarily high T remains open.

## Methodological Lessons (reusable patterns)

1. **Match the metric to the noise**: if error processes are graded (small shifts more likely), Hamming weight mis-models the problem; a structured metric (Lee = clock distance) can beat it with FEWER physical systems.
2. **No-Go theorems are error-model statements**: Eastin–Knill's failure under the Lee metric shows continuity/transversality constraints are metric-relative. Re-examine accepted No-Gos when the resource accounting changes.
3. **Homology/SNF over Z (not fields)**: composite-q codes need integer SNF — torsion factors are a feature (graded logical qudit dimensions), computable by the same chain-complex machinery as homological codes.
4. **Discretize a continuous theory to inherit its theorems**: Lee ↔ GKP displacement distance correspondence transfers CV intuition (error spreading, confinement) to discrete qudit codes.
5. **Gate error propagation = matrix-column norm**: Lee spread of a Clifford = max column Lee weight of its symplectic matrix — a one-line computable FT proxy.
6. **Separate energetic from entropic protection**: exp memory can come from barriers (confinement) OR from flat-but-long paths (entropic bottlenecks). Test which mechanism before designing decoders.
7. **Geometry of numbers as a proof relaxer**: Z_q → R relaxation + transference theorems yields uniform LDPC bounds — reusable for any modular-weight code family.

## Connections

- GKP codes (displacement metric), quantum double models (group-valued qudits), expander LDPC self-correction, generalized clock models, entropic order solids, CLY code, quantum Reed–Solomon over Z_5.
- Contrast: Hamming-metric LDPC bounds (good q^a scaling) vs Lee-metric O(n) obstruction.

## Verification Notes

- All theorems quoted from arXiv:2610.04834v1; Table 1 (9-qubit code optimizations), Table 2 (perfect codes), Thms 4.5, 6.2, 6.3, 6.5, 7.7, 7.8, Props 7.12, 8.1, 8.3, 8.5, 8.6 cross-checked against PDF text.
