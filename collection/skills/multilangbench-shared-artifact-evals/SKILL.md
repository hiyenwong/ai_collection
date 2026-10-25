---
name: multilangbench-shared-artifact-evals
description: "Cross-language code evals via shared artifact interface"
---

# MultiLangBench: Shared-Artifact Cross-Language Code Evaluation

Methodology from OpenAI's "Advancing coding in low-resource programming languages" (Oct 2026), released as [github.com/openai/MultiLangBench](https://github.com/openai/MultiLangBench). Evaluate code generation in ANY language by testing behavior against a language-neutral artifact, instead of writing per-language test suites. Evidence: 20-language SQLite-reimplementation eval where GPT-6 Astra averaged 87.4% vs GPT-5.6 Sol's 26.8% (COBOL 10.9%→72.1%, Fortran 21.4%→83.5%, Visual Basic 27.5%→89.4%).

## When to Use

- Evaluating LLM coding in low-resource / legacy languages (COBOL, Fortran, Visual Basic, OCaml, ...) where no per-language test suites exist
- Comparing one model's capability across many languages with a single suite
- Building legacy-modernization / code-migration benchmarks
- Any eval where implementations differ but required behavior is identical (compilers, engines, protocol implementations)

## Core Design: Language-Neutral Shared Interface

1. Pick a canonical artifact as the I/O interface — here a database file.
2. A test = (initial artifact, operation/SQL query). A candidate program in ANY language receives them and must produce the modified artifact.
3. Verify the output artifact with a trusted reference implementation (SQLite checks SQLite clones) — content equivalence, not syntax or style.
4. Only the implementation language varies across runs; the suite, oracle, and difficulty scale are identical for all 20 languages.

Why it works: it tests final-state behavior rather than code form, so language idiosyncrasies (I/O conventions, string handling, build systems) don't contaminate the score, and per-language results are directly comparable.

## Companion Design: Migration Eval

- Task: migrate a real legacy codebase (COBOL) to a modern target; score functional equivalence.
- Report a capability-cost curve, not a point: accuracy BY reasoning effort AND cost per sample. GPT-6.1 Sol hit 86.6% at low effort at 61% of baseline cost (vs 5.4% for GPT-5.6 Sol), 97.9% at high effort — near saturation.

## Rules of Thumb

- If implementations in multiple languages must satisfy the same spec, test the shared artifact, not the code.
- Use a mature reference implementation as the oracle; its content checks are your ground truth.
- Report cost-per-sample next to pass rate, and break results down per language — the low-resource tail (COBOL 72% when 19/20 languages exceed 83%) is the real signal.
- For legacy modernization, compare models at matched reasoning effort and price, not just peak accuracy.

## Pitfalls

- Artifact choice bounds what is tested: a DB-state interface exercises engine semantics, not each language's CLI/UI/stdlib ecosystem.
- Averages hide the hardest language; even frontier models leave a large residual gap on the lowest-resource language — don't claim "solved" from the mean.
- Cost-per-sample moves with reasoning effort; fix the effort level before comparing models, or the comparison is meaningless.

## Activation Keywords

- low-resource programming languages
- MultiLangBench
- shared artifact interface evaluation
- COBOL migration benchmark
- cross-language code evaluation
- language-neutral test oracle
