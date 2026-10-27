---
name: agentic-verifiable-quantum-compilation
description: "Paradigm for AI-agent optimization of quantum circuit compilations whose bottleneck subroutines are constrained to classically verifiable structure (kickmix: reversible classical logic + diagonal phasing + measurement-based uncomputation). Fuzz testing on sampled basis inputs bounds failure rate ε, certifying fidelity ≥ (1−2ε)² and trace distance ≤ 2√ε; Fiat-Shamir seeded non-interactive verification (SHA-256 of circuit bytes + salt → PRNG) makes certification public and seed-grinding-proof; Clopper-Pearson gives ε+ ≈ 88.7/N at 2^-128 confidence. Use when running agentic closed-loop circuit optimization, building circuit-approximation test harnesses, or designing verifiable AI-research competitions. Activation: kickmix, Fiat-Shamir verification, fuzz testing quantum circuits, agentic circuit compilation, Toffoli count optimization, classically verifiable subroutine, Clopper-Pearson certification, ecdsa.fail, Qualtran, circuit synthesis competition."
---

# Leveraging Verifiable Structure in Quantum Circuits for Agentic AI Compilation

Methodology from arXiv:2610.23832 (Khattar, Rubin, Gidney, Broughton, Low, Babbush — Google Quantum AI, Oct 2026). Generalizes the verifiable-structure paradigm first exploited for quantum cryptanalysis (ecdsa.fail / Ref. [13] secp256k1 point-addition circuits, March 2026) into a reusable recipe for agentic quantum compilation, seeded as a Kaggle competition ($150k prize pool) over three benchmarks: 1/√x for Coulomb/fusion simulation, Reed-Solomon syndrome decoding for decoded quantum interferometry (DQI), and QROM + Majorana rotations for quantum chemistry (DFTHC block-encodings).

## The Core Paradigm (transferable recipe)

Agentic circuit optimization needs a fast, reliable, cheat-proof verifier. General unitary-equivalence checking is QMA-complete and classical simulation is exponential — but the subroutines that DOMINATE fault-tolerant resource estimates (integer arithmetic, QROM lookups, syndrome decoders) often don't use internal quantum interference. The recipe:

1. **Constrain the bottleneck** to classically-verifiable structure — no instruction may create a superposition over computational basis states.
2. **Simulate classically at linear cost** — each instruction maps a basis state to one basis state × scalar phase; simulator state = 1 bit/qubit + one phase accumulator.
3. **Fuzz-test on sampled basis inputs** — empirical failure rate ε̂ = k/N certifies approximate correctness (tolerates dropped carry bits, truncated registers, bounded iterations).
4. **Convert ε to a quantum guarantee** — fidelity ≥ (1−2ε)², trace distance ≤ √(1−(1−2ε)²) ≤ 2√ε (bound verified numerically; tight at small ε).
5. **Make verification non-interactive and cheat-proof** — Fiat-Shamir: seed the test-input PRNG from SHA-256 of the submitted circuit bytes (+ private salt in competitions, published later); one byte change → fresh challenge set; no secret test set to leak or overfit; salt blocks seed-grinding via no-op padding.
6. **Score by certified failure rate** — Clopper-Pearson upper bound ε+ from N shots at false-pass probability δ: ε+ ≈ ln(1/δ)/N = 88.7/N for δ=2⁻¹²⁸. N=10,240 zero-fail shots → ε+ < 1%; N=102,400 → ε+ ≈ 8.7×10⁻⁴ (verified exactly: 128·ln2=88.72).
7. **Open a competition** — fast verifier (seconds per submission) lets non-experts with AI agents compete; ecdsa.fail precedent: 100+ participants halved Toffoli counts.

## Kickmix Gate Set (the verifiable-structure family)

Four instruction classes, all controllable per-gate (`if b`) and via condition stack (PUSH/POP_CONDITION):
- **Reversible classical**: X, CX, CCX, SWAP — permute stored qubit bits directly.
- **Diagonal phase**: Z, CZ, CCZ, Z_POW, NEG — update the tracked output phase only (Z_POW uses a 128-bit fixed-point phase accumulator per trajectory).
- **Measurement/reset**: HMR ("hammer") = H + Z-basis measure + reset: |x⟩|f(x)⟩ → (−1)^(b·f(x)) |x⟩|0⟩. Phase kickback (−1)^f(x) is fixable with a classically-controlled diagonal gate when b=1 — replaces a Toffoli for AND-uncomputation. R = reset-to-|0⟩ for deallocation.
- **Classical bit ops**: BIT_STORE0/1, BIT_INVERT on classical registers.

**Loud-failure property** (the key debugging design): HMR on a qubit that's still entangled/junk (qt=1) without phase fixup flips the tracked phase with probability 1/2 per sampled input — the fuzz check FAILS, not silently corrupts. Same for R on a non-|0⟩ qubit. Uncleaned garbage is statistically self-detecting.

## Fuzz Certification Math (verified)

Fix the HMR/R outcome record r ∈ {0,1}^m; the circuit acts as linear map V_r on basis states; Kraus ops are 2^(−m/2) V_r; deferring measurements gives isometry W|ψ⟩ = 2^(−m/2) Σ_r V_r|ψ⟩⊗|r⟩. With failing-input weight ε_r = Σ_{x∈B_r}|α_x|² (B_r = inputs where V_r ≠ U), assuming V_r maps distinct inputs to distinct outputs (holds when every HMR/R target is a function of other qubits, as in measurement-based uncomputation):
- per-branch error: ‖(V_r − U)Σ_{x∈B_r}α_x|x⟩‖ ≤ 2√ε_r
- purified-output distance: ‖W|ψ⟩ − U|ψ⟩⊗|+⟩^⊗m‖² ≤ 4ε
- fidelity ≥ (1−2ε)²; after discarding the record: trace distance ≤ √(1−(1−2ε)²) ≤ 2√ε — also bounds TV distance of any later measurement.

Caveat: the verifier MUST sample inputs from the algorithm's actual input distribution |α_x|² (each benchmark specifies it). Certification is distribution-relative.

Per-shot checks (any violation = failed shot): (1) input/output registers hold expected bitstrings, (2) every scratch qubit returns to |0⟩, (3) accumulated output phase within benchmark tolerance. Benchmark I requires k=0 (all shots pass); Benchmark II allows failures and prices them via ε+.

## Software Engineering for 10^8-gate Loops (kickmix/Qualtran)

C++20 + Python bindings inside Qualtran. Performance patterns worth reusing in any massive-circuit simulator:
- **Struct-of-arrays** layout grouped by operand count (opcode byte array + separate 1/2/3-qubit arg arrays; opcode embeds operand-array flags) — no per-gate heap objects.
- **SIMD trajectory bit-packing**: 64–512 independent shots per instruction batch (exception: Z_POW scans the active shot mask sequentially per angle).
- **Binary .kmb format**: contiguous array blocks, no per-gate text parsing.
- Measured: build 2×10⁷ instr/s, simulate 6×10¹⁰ instr/s on ONE CPU core; 86M-gate DQI circuit built in <5 s; 102,400 decoder shots in 150 s.
- Builder ergonomics for agents: automatic downgrading (qubit/classical-bit/constant interchangeability), NumPy-style broadcasting over registers, dynamic workspace allocation within qubit budget, subroutine library with paired compute/uncompute variants, SVG flame charts of Toffoli/qubit spend.

## Benchmark Score Design (how to price a submission)

- **Benchmark I (1/√x, Coulomb/fusion)**: S = Q × C, C = Toffolis + T/4 (T gates at ¼ Toffoli); every shot must pass within tol(x) = 2⁻²⁴β/√x; verification recipe uses an isqrt-based fixed-point identity ⌊2⁶⁵β/√x⌋ = isqrt(⌊2¹³⁰β²/x⌋) — CAUTION: this identity is NOT exact for arbitrary (β,x) (counterexample found in random testing); it holds in the benchmark's specific rescaled domain x_norm ∈ [2,4). Do not reuse generically without re-verification.
- **Benchmark II (Reed-Solomon/DQI)**: S = R(ε+)·Q²·T — qubits weighted quadratically (1% qubit reduction ≈ 2% Toffoli reduction); repetition factor R(ε+) accounts for success-probability erosion p₀ → p₀−2ε: R = 1.02, 1.06, 1.21, 1.94 at ε+ = 10⁻⁵, 10⁻⁴, 10⁻³, 10⁻² (paper's Table; my p₀/(p₀−2ε) reconstruction does NOT reproduce these — the exact R form involves the DQI runtime formula; quote as-reported). ε+ ≥ 1/16 → no score. Zero-fail floor: R(8.7×10⁻⁴) ≈ 1.19.
- **Benchmark III (QROM + Majorana, chemistry)**: non-kickmix parts (arbitrary state prep) priced by analytical cost formulas so the score still reflects the full algorithm.

## Competition-Kinematics Lessons (ecdsa.fail → Kaggle)

- Verification in seconds per submission is the gating resource, not solver cleverness — it decouples organizer trust from participant trust.
- AI coding agents + fast harness let non-quantum participants contribute real improvements (ecdsa.fail: ~2× Toffoli reduction by >100 participants, mostly via AI agents).
- Allow approximate correctness (ε-certified) rather than exactness — this unlocks a much larger design space (precision trade-offs) that exact-match verifiers forbid.
- Two future directions from the paper: (1) score with a QEC-architecture cost model (physical qubits/runtime) while keeping kickmix for logical correctness; (2) machine-checkable proofs (Lean) for non-kickmix subroutines (state prep, QSP, fermionic rotations) — parameterized constructions + symbolic correctness for any problem size, where simulation can't reach.

## Verification Notes (pdftotext corruption log)

- Trace-distance formula extracted as "1 − (1 − 2ε)² ≤ 2 ε" — radicals dropped; correct form √(1−(1−2ε)²) ≤ 2√ε, confirmed by Fuchs–van de Graaf derivation AND numerics (D=0.06321 vs bound 0.06325 at ε=10⁻³).
- Per-branch bound "≤ 2 εr" is actually ≤ 2√ε_r (radical drop).
- Clopper-Pearson constants verified exactly: ln(2¹²⁸)=88.72; 0.99¹⁰²⁴⁰ = 2⁻¹⁴⁸·⁵ < 2⁻¹²⁸.
- A parallel independent work (their Ref. [32]) applies the same kickmix+agent pattern to overlapping benchmarks — convergent validation of the paradigm.

## When to Use

- Designing an AI-agent optimization loop over any artifact class where full verification is intractable but a constrained sub-family admits fast checking (circuit synthesis, code optimization with property tests, query planning).
- Building public benchmarks/competitions that must verify submissions without a trusted judge or secret tests.
- Compiling fault-tolerant subroutines (arithmetic, QROM, decoders, oracles) where Toffoli/qubit counts dominate cost estimates.
- Deciding verification strategy for approximate compilation: fuzz → Clopper-Pearson bound → repetition-overhead pricing.
