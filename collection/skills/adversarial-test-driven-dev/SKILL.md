---
name: adversarial-test-driven-dev
description: Self-evolving code generation combining adversarial unit test generation with test-driven development. Two patterns: (1) ACE framework uses solver-adversary architecture where LLM alternates between generating code and adversarial tests optimized to induce execution failures; (2) TDDev automates TDD for web apps via requirement-to-acceptance-tests conversion, browser-based validation, and structured repair reports. Use when building self-improving coding agents, test-driven code generation, adversarial testing frameworks, or web app generation from requirements. Based on ACE (arXiv: 2605.16299) and TDDev (arXiv: 2605.17242).
---

# Adversarial Test-Driven Development

Two complementary patterns for self-evolving code generation (ACE + TDDev).

## Pattern 1: ACE — Adversarial Self-Evolution

### Architecture
```
Solver (generates code) ←→ Adversary (generates breaking tests)
         ↓                          ↓
   SFT on passing           KTO on test outcomes
```

### Workflow
1. **Generate candidate program** from problem spec
2. **Generate adversarial tests** optimized to find failures:
   - Runtime errors, exceptions, non-termination
   - Edge cases, boundary conditions
3. **Execute tests** → derive supervision signal:
   - Robust programs → supervised fine-tuning
   - Adversarial tests → Kahneman-Tversky Optimization
4. **Iterate**: No ground-truth code needed; execution is the only supervisor

### Key Insight
Verifier-generated tests confirm correctness; adversarial tests expose failure modes. The adversary prioritizes active failure discovery.

## Pattern 2: TDDev — Test-Driven Web Development

### Three-Stage Pipeline

**Stage 1: Requirements → Acceptance Tests**
```
High-level spec → Structured acceptance tests (before any code)
```

**Stage 2: Browser-Based Validation**
```
Deploy app → Simulate browser interactions → Observe failures
```

**Stage 3: Structured Repair**
```
Browser failures → Structured repair report → Code agent fixes
```

### Protocol Selection

The optimal TDD protocol depends on the model's generation style:
- **Holistic builders** → benefit from agentic enforcement
- **Conservative extenders** → benefit from incremental enforcement
- **Mismatching protocol** → eliminates TDD benefit + 25x token cost

### Results
- TDD improves generation quality by **34-48 percentage points**
- Reduces manual developer intervention to zero
- Shifts workload from prompt engineering to autonomous refinement

## When to Use

- Building self-improving coding agents
- Code generation without ground-truth solutions
- Web application generation from natural language
- Need execution-driven supervision (no reward models)

## Pitfalls

- Match TDD protocol to model's generation style (holistic vs conservative)
- Adversarial tests must be optimized for failures, not just coverage
- Browser validation requires full deployment, not source analysis
- Token cost can multiply 25x with wrong protocol choice
