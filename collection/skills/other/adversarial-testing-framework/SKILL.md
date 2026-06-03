---
name: adversarial-testing-framework
description: "Self-evolving adversarial testing framework for code generation, agent evaluation, and robustness improvement. Based on the ACE (ICLR 2026) solver-adversary architecture. Use when: (1) improving code generation models through self-evolution, (2) designing adversarial test inputs to expose failure modes, (3) building self-improving loops without ground-truth labels, (4) optimizing agent behavior through execution-level feedback, (5) applying Kahneman-Tversky Optimization (KTO) for preference-based agent training. Activation: adversarial testing, solver-adversary, self-evolving coding, ACE framework, execution-based supervision, preference optimization, KTO training, fuzzing LLM, robust code generation."
---

# Adversarial Testing Framework

Self-evolving testing methodology based on the ACE framework (Huang et al., ICLR 2026). Uses a solver-adversary architecture where a single model alternates between generating solutions and generating adversarial tests that expose failure modes.

## Core Insight

Verifier-style tests that confirm correctness quickly saturate — once a solver reaches moderate proficiency, most tests pass and training signal degrades. Adversarial tests that induce execution failures (runtime errors, exceptions, non-termination) remain informative indefinitely and expose subtler failure modes.

## Architecture

```
Single LLM (shared parameters θ)
├── Solver role: generate candidate programs
└── Adversary role: generate adversarial unit test inputs
    └── No expected outputs required — only execution behavior matters
```

## Multi-Round Self-Evolution Loop

For each round r = 1..R:

### Step 1: Sampling

```
Solver:    C(p) = {c1, ..., ck1} ~ π_solver(θ_{r-1})
Adversary: T_adv(p) = {t1, ..., tk2} ~ π_adv(θ_{r-1})
```

### Step 2: Execution Boolean Table

Execute each candidate on ground-truth tests + adversarial tests:

```
E[i,j] = 1 if ci passes test j, else 0
```

- For GT tests: pass = correct output within resource limits
- For adversarial tests: pass = normal termination (no runtime error/exception/timeout)

### Step 3: Code Scoring

```
rGT_i = (1/|T_GT|) * Σ I[E(ci, t) = 1]
radv_i = (1/k2) * Σ I[E(ci, t_adv_j) = 1]
si = α * rGT_i + (1-α) * radv_i
```

### Step 4: Solver Data Selection

Filter codes that pass both GT threshold τ_GT and adversarial threshold τ_adv, then keep top ρ fraction. Use for SFT.

### Step 5: Adversary Preference Construction

For each adversarial test t_j:
- Count executions that succeed: e_j = Σ I[E_adv[i,j] = 0]
- Count that fail: s_j = k1 - e_j
- **Desirable** (y_j=1): induces BOTH successes and failures — discriminates code quality
- **Undesirable** (y_j=0): all codes succeed — no adversarial signal
- **Discard**: all codes fail — likely invalid input, not meaningful signal

### Step 6: Model Updates

```
Solver update:    θ_r ← SFT(θ_{r-1}, B_SFT)
Adversary update: θ_r ← KTO(θ_r, D_des, D_undes)
```

KTO objective with length penalty:

```
L = w_des * E[L_des(x)] + w_undes * E[L_undes(x)]
∆_θ(x) = log π_θ(x|p) - log π_ref(x|p)
∆_θ^LP(x) = ∆_θ(x) - λ * ℓ(x)
```

## Key Design Patterns

### Execution-Only Supervision

The entire loop requires NO:
- Ground-truth code
- External reward models
- Human annotations

Only execution outcomes (pass/fail/timeout/error) drive the learning signal.

### Discriminative Test Selection

A good adversarial test should split the candidate set — some pass, some fail. Tests where all pass are useless (no signal). Tests where all fail are ambiguous (likely invalid).

### Length Regularization

Add length penalty to adversary to prevent excessively long test inputs that waste tokens.

### Sandbox Execution

All tests run in sandboxed environments with strict time/memory limits. Discard tests violating input specs.

## Application to Agent Systems

### Agent Code Generation

```
Agent generates code → Adversarial tests probe edge cases → 
Robust code selected for training → Agent improves
```

### Tool Use Validation

```
Agent proposes tool calls → Adversarial inputs test tool boundaries → 
Discriminating tests selected → Tool-use policy optimized
```

### Reasoning Robustness

```
Agent produces reasoning → Adversarial counter-examples probe logic gaps → 
Sound reasoning selected → Reasoning quality improves
```

## Parameters

| Parameter | Typical Value | Purpose |
|-----------|--------------|---------|
| k1 (solver samples) | 16 | Candidate programs per problem |
| k2 (adversary samples) | 16 | Adversarial tests per problem |
| α | 0.5-0.7 | Balance between GT and adversarial score |
| ρ | 0.1-0.3 | Top fraction of codes for SFT |
| τ_GT | 0.8-1.0 | Minimum GT pass rate |
| τ_adv | 0.5-0.8 | Minimum adversarial pass rate |
| R (rounds) | 4-5 | Self-evolution rounds |
| λ (length penalty) | 0.01-0.1 | Penalize long test inputs |
| temperature | 1.0 | Stochastic decoding for diversity |

## Results Summary

ACE achieves 3-7% absolute gains in pass@1 over solver-verifier baselines on MBPP, CodeContests, and LiveCodeBench. Gains are largest on out-of-distribution benchmarks, indicating stronger robustness.

## Related Papers

- arXiv:2605.16299 — ACE: Self-Evolving LLM Coding Framework (ICLR 2026)
- KTO: Ethayarajh et al., 2024 — Kahneman-Tversky Optimization
- DPO: Rafailov et al., 2023 — Direct Preference Optimization
