---
name: qtestbench-llm-quantum-test-quality
description: Scoring LLM-written quantum test suites against oracles.
category: ai_collection
---

# QTestBench: Oracle-Grounded Evaluation of LLM-Generated Quantum Tests

> From "QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code" (arXiv:2610.13811, Terki, Innan, Shao, Kashif, Marchisio, Shafique — NYUAD, Oct 2026). Use when: evaluating whether LLM-generated unit tests can *discriminate* correct quantum code from faulty code, building test-quality benchmarks for Qiskit/PennyLane, or auditing LLM-written test suites in any probabilistic/tolerance-sensitive domain.

## Core Insight

Executability overstates test quality. LLMs reliably write quantum pytest suites that *run* (ES ≥ 0.79 for all five tested models, 1.00 for three), but the best generator only reaches test quality TQS = 0.71 on PennyLane QHack and 0.34 on Qiskit HumanEval. A suite that accepts incorrect code is worse than no suite at all — and a passing generated test is never ground truth.

Two canonical failure modes (both observed from real generators on the same task):
- **Too weak** (syntactic-only): structure checks pass, oracle-wrong solutions return wrong circuit values, Test=Pass while Checker=Wrong. The suite never executes the candidate on official inputs.
- **Too strict** (over-tight tolerance): `np.allclose(float(out), float(exp), atol=1e-4)` rejects the *human reference* that the benchmark checker accepts — two numerically close outputs land just outside the test's tolerance. Test=Fail while Checker=Correct.

## The Two-Stage Pipeline

### Stage 1 — Test Generation (per test type, single pass)
Materialize every task into three inputs: (1) task description + entry-point stub, (2) official I/O pairs, (3) official checker (oracle). The reference solution is **withheld** from the generation prompt so the model cannot copy correct answers into assertions.

Generate three suite types with one LLM call each (temperature 0.8, **no repair loop**):

| Type | Question | What runs | Ground truth used |
|------|----------|-----------|-------------------|
| Syntactic | Valid structure? | Parse/load candidate, no circuit execution | Required entry points only |
| Semantic | Correct outputs? | Candidate execution on official cases | Embedded official I/O values |
| Behavioral | Passes harness rules? | run() then candidate-local check() | Candidate's embedded check() |

Normalize output: strip markdown fences, validate Python syntax, prepend file header, embed official I/O pairs into the suite.

### Stage 2 — Oracle-Grounded Validation
1. **Build solution cohort**: trusted human reference + LLM-generated solutions + (optionally) synthetic mutants.
2. **Label with oracle**: run the benchmark's official checker on every probe → correct / wrong / unknown. Never the generated tests.
3. **Execute tests via runtime candidate injection**: write candidate to a temp module, inject into pytest harness namespace, parse pass/fail/error with timeouts (QHack: 180s/file, 60s/test; Qiskit: 240s/120s).
4. **Aggregate scores** by suite type, task, generator.

## Discrimination Metrics

For suite T with oracle-correct set Sc and oracle-wrong set Sw:

- **ES (executability)**: 1 if T runs on the trusted baseline without infrastructure failure, else 0.
- **CS (correctness acceptance)** = |{s ∈ Sc : T accepts s}| / |Sc| — fraction of correct candidates the suite accepts.
- **BDS (bug-detection)** = |{s ∈ Sw : T rejects s}| / |Sw| — fraction of wrong candidates rejected. Only defined when |Sw| > 0.
- **TQS (test quality)** = ES × CS × BDS (Config A: TQS = ES × CS since BDS undefined). Report **n/a, never zero**, when |Sw| = 0 — zeroing would penalize suites that accept all correct probes but simply had no wrong probes to reject.
- **Cin (checker-input coverage)**: fraction of official checker literals present in the test body.
- **CQ (composite quality)** = TQS × Cin.

Acceptance and rejection trade off: Qwen3-Coder rejects most wrong code (BDS 0.60) but accepts least correct code; Claude Opus 4.6 accepts most (CS 0.84) while rejecting less. No single metric suffices.

## Three Validation Cohorts

- **Config A (trusted-reference)**: reference solution only. Isolates executability + acceptance of known-correct code.
- **Config B (natural LLM cohort)**: reference + independently generated LLM solutions, oracle-labeled. Measures discrimination against bugs models *actually make* (BDS 0.45–0.60 observed).
- **Config C (synthetic mutant calibration)**: reference + oracle-verified mutants. Restores measurability when natural wrong solutions are scarce (3/10 Qiskit tasks attracted zero wrong solutions).

## Oracle-Verified Mutation Set (Config C)

Deterministic mutations applied to the trusted reference; **keep only mutants the official checker labels wrong**:
1. `return None`
2. Flip `==` to `!=`
3. Remove `measure_all()`
4. Replace the first CX or Hadamard with an X gate
5. Perturb numeric literals (1,000 → 10; 100 → 1)
6. Force a local `check()` failure (QHack only)

Try up to twelve candidates, keep first three confirmed-wrong probes. This couples mutation testing with oracle verification — unverified mutants may accidentally be equivalent programs.

## Implementation Notes

- QHack baseline selection: execute every human submission against all three suite types, pick the submission passing most sub-tests as s0 (compatibility with generated suites, not ground truth).
- Checker literals extraction powers Cin — but some checkers have none (Deutsch–Jozsa Cin = 0.00), pushing CQ to zero even at moderate acceptance; report Cin separately.
- Cross-SDK transfer: identical metrics on PennyLane and Qiskit; only task materialization and oracle execution differ. Fixed ten-task Qiskit scope chosen *before* generation.
- One request per test type, no re-prompting: repair loops would inflate scores by letting the model iterate against the very checker it is being judged by.

## Reuse Beyond Quantum

The pattern generalizes to any domain where correctness is defined by domain-specific oracles and outputs are probabilistic/tolerance-sensitive:
1. Never treat generated tests as ground truth — always score against an independent oracle.
2. Score discrimination (accept correct + reject wrong), not just execution.
3. Use n/a semantics for undefined metrics to avoid perverse incentives.
4. Calibrate bug-detection with oracle-verified synthetic mutants when natural faults are sparse.
5. Report acceptance–rejection trade-off per generator rather than a single quality number.
