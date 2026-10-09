---
name: qudit-many-hypercube-qec-codes
description: Use when building high-rate qudit QEC codes or qudit FTQC.
category: quantum
---

# Qudit Many-Hypercube (MHC) QEC Codes (arXiv:2610.11225)

**Paper**: "High-Rate Concatenated Quantum Error-Correcting Codes for Qudits" — Nishi & Goto (RIKEN/Toshiba, 2026-10-08)

Extends many-hypercube codes from qubits to qudits of prime dimension q — threshold nearly **doubles from 5.1% (qubit) to 10.0% (q=13)**, with a waterfall regime beyond distance-based scaling.

## Code Construction (finite field F_q, q prime)

Base code: **[[6,4,2]]_q** error-detecting code. Level-L concatenation:

```
level-2: [[6², 4², 2²]]_q        level-3: [[6³, 4³, 2³]]_q
```

Rate stays R = (4/6)^L → exponential logical dimension q^(4^L) in 6^L physical qudits.

**Why prime q**: Pauli group P = {ω^c X^a Z^b} with arithmetic over finite field F_q ≅ Z_q only when q = p (r=1). For q = p^r, r>1, use Galois qudits instead (open problem).

### Qudit gate set (modular-qudit formalism)

- Pauli: `X|n⟩ = |n+1⟩`, `Z|n⟩ = ω^n|n⟩`, ω = exp(i2π/q); commutation `X^a Z^b · X^c Z^d = ω^{bc−ad} · X^c Z^d X^a Z^b`
- Clifford generators: Fourier `F` (≈Hadamard), phase `S`, `SUM_{c→t}` (≈CNOT)
- Conjugation rules: `F X^a F† = Z^a`, `F Z^a F† = X^{−a}`; `SUM: X_c^a⊗X_t^b → X_c^a⊗X_t^{a+b}`, `Z_c^a⊗Z_t^b → Z_c^{a−b}⊗Z_t^b`
- Syndrome measurement outcomes live in Z_q (q-ary syndrome alphabet)

## Two Decoders

1. **HD (hard-decision)** — Knill-style concatenated scheme; q-dependence weak, no clear threshold trend
2. **LLMD (level-by-level minimum-distance)** — generalized from qubit MHC; **the decoder that matters**: threshold ↑ monotonically with q (Hamming distance over Z_q per level, minimum-distance decision at each level)

## Key Results (qudit X-error model, code-capacity)

| q | LLMD threshold | Notes |
|---|---|---|
| 2 | 5.1% | qubit baseline |
| 5 | ~higher | waterfall regime ONSET (exponent > 4) |
| 7 | ~higher | p₅ also suppressed |
| 13 | **10.0%** | trapped-ion hardware already demoed q=13 control |

- **Waterfall regime** (q ≥ 5): fitted exponents exceed distance-based expectation ⌊(d+1)/2⌋ = 4, reaching >5 — LLMD suppresses high-weight failure classes beyond decoding radius (cf. neural-decoder waterfall in qubit qLDPC)
- **Error-floor regime** (low ε): exponents converge toward distance-based values

## Entropy-Based Interpretation (the analytic core)

q-ary channel entropy (normalized, max=1 at ε=(q−1)/q):

```
H_q(ε) = −(1−ε)·log_q(1−ε) − ε·log_q(ε/(q−1))
```

Plotting logical error rate vs **H_q** (not vs ε) collapses level-2 curves onto ONE curve — channel entropy dominates decoding performance. Residual q-dependence = competition between:

1. **Syndrome richness** (+): larger q → richer syndrome alphabet → better logical-class distinguishability → wins in error-floor regime
2. **Typical error weight** (−): at fixed H_q, larger q → higher ε → larger typical weight `w ≈ n·ε` relative to decoding radius (`ξ = n·ε/(d/2)` grows with q) → wins in waterfall regime

This entropy-competition frame explains BOTH the threshold doubling and the waterfall onset.

## Methodological Patterns (reusable)

1. **Finite-field Pauli formalism**: when generalizing qubit code families to qudits, restrict to prime q first so F_q ≅ Z_q; defer Galois qudits
2. **Replot vs channel entropy H_q, not raw ε** — collapses dimension-dependence, reveals mechanism
3. **Weight-ratio diagnostic**: ξ = n·ε/(d/2) predicts when typical weight crosses decoding radius
4. **Threshold via level-2/level-3 crossing** — concatenated-code threshold convention
5. **Error model focus**: X-error-only model isolates decoder behavior (Z/X decouple under Clifford structure)

## When to Use

- Designing qudit FTQC architectures (trapped ions/neutral atoms with demonstrated q=13)
- Estimating whether raising local dimension q helps YOUR concatenated/code family
- Analyzing waterfall vs error-floor regimes in ANY decoder (qLDPC analog)
- High-rate encoding: more logical qudits per physical carrier

**Activation**: qudit, qudit qec, many-hypercube, mhc code, concatenated quantum code, high-rate code, llmd decoder, qudit threshold, q-ary entropy, waterfall regime, error floor, galois qudit, qudit ftqc
