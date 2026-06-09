---
name: socratic-swe-self-evolving-coding-agents
description: "Self-Evolving Coding Agents via Trace-Derived Agent Skills (Socratic-SWE). Closed-loop framework that reuses solving traces to distill agent skills, generate targeted repair tasks, and iteratively improve Solver performance. Achieves 50.40% on SWE-bench Verified. Activation: self-evolving agent, coding agent training, trace-derived skills, SWE bench, agent skill distillation."
---

## Context

LLM-driven software engineering agents face a critical bottleneck: limited availability of high-quality SWE tasks for training. Existing synthetic data methods create tasks through fixed mutation or bug-injection procedures, producing task distributions independent of the agent's actual weaknesses and learning progress.

Socratic-SWE introduces a closed-loop self-evolution framework that treats solving traces not just as reward signals, but as substrates for skill extraction. These skills guide targeted task generation, creating a curriculum that adapts to the agent's specific failure patterns across successive iterations.

## Core Methodology

### 1. Trace-Derived Skill Distillation

**Extract Structured Skills from Solving Traces**
- Solving traces contain: (1) code changes, (2) test outcomes, (3) error messages, (4) reasoning steps
- Distillation process:
  1. Identify recurring failure patterns across traces
  2. Extract effective repair patterns that succeeded
  3. Cluster by failure type → skill per cluster
  4. Skill structure: `{failure_pattern, repair_strategy, verification_check}`

**Skill Schema**:
```json
{
  "skill_id": "skill_fix_import_error",
  "failure_pattern": "ImportError: module X not found",
  "repair_strategy": "Add missing import: 'import X' at top of file",
  "verification_check": "Run tests to confirm import resolves error",
  "frequency": 15,  // occurred 15 times in traces
  "success_rate": 0.80  // 80% repair success
}
```

**Distillation Algorithm**:
1. Parse trace → extract error messages, code diffs, test results
2. Pattern matching → group traces by error type
3. Extract repair templates → generalize specific fixes to patterns
4. Rank by frequency + success_rate → prioritize high-impact skills

### 2. Skill-Guided Task Generation

**Generate Targeted Repair Tasks from Skills**
- Input: Agent's distilled skills + real repository
- Output: Synthetic SWE tasks targeting specific weaknesses
- Task template: `{repo, skill, target_file, mutation_type, expected_fix}`

**Generation Process**:
```python
def generate_task(skill, repo):
    # 1. Select target file matching skill context (e.g., imports modules)
    target_file = find_file_with_imports(repo)
    
    # 2. Apply mutation based on skill's failure pattern
    # Example: skill = "import error"
    mutation = remove_import(target_file, module_name)
    
    # 3. Create task description
    task = {
        "repo": repo,
        "issue": f"Test failing due to ImportError: {module_name}",
        "expected_fix": skill["repair_strategy"]
    }
    
    # 4. Validate task (execution-based)
    if test_fails_after_mutation(task):
        return task  # task is verifiable
    else:
        return None  # discard invalid task
```

**Curriculum Adaptation**:
- Round 1: Skills from initial Solver traces → generate Round 1 tasks
- Round 2: Solver improves → new traces → new skills → Round 2 tasks (different focus)
- Round N: Curriculum evolves as Solver weaknesses shift

### 3. Solver-Gradient Alignment Reward

**Score Task Utility for Solver Improvement**
- Not all generated tasks are equally useful
- Reward function: `R(task) = gradient_alignment(task, Solver)`
- Gradient alignment measures: does solving this task improve Solver on similar tasks?

**Reward Calculation**:
```
R(task) = 1/N * Σ_i |∂Solver(task_i) / ∂θ|  dot  |∂Solver(task) / ∂θ|
where:
- task_i = tasks in Solver's training set
- θ = Solver model parameters
- dot product measures gradient alignment
```

**Interpretation**:
- High reward → solving this task moves Solver in direction beneficial for training set
- Low reward → orthogonal improvement, less useful for curriculum
- Filter: retain tasks with R(task) > threshold (e.g., 0.7)

### 4. Execution-Based Validation

**Verify Generated Tasks Before Retention**
- Task must be:
  1. **Verifiable**: Tests fail after mutation, pass after correct fix
  2. **Solvable**: Expected fix actually resolves the issue
  3. **Nontrivial**: Not trivially easy (e.g., single-character typo)

**Validation Pipeline**:
```
1. Apply mutation → create broken state
2. Run tests → verify failure (test status: FAIL)
3. Apply expected fix → create repaired state
4. Run tests → verify success (test status: PASS)
5. Check difficulty → reject trivial fixes (single-line, obvious typo)
6. Retain task if all checks pass
```

### 5. Iterative Self-Evolution Loop

**Closed-Loop Training Process**
```
Round 0:
  - Initial Solver S_0 (baseline)
  - Run on SWE-bench → generate traces T_0
  - Distill skills K_0 from T_0

Round 1:
  - Generate tasks D_1 using K_0
  - Validate D_1 (execution-based)
  - Score D_1 with gradient alignment
  - Train Solver S_1 on D_1 + SWE-bench

Round 2:
  - Run S_1 → new traces T_1
  - Distill new skills K_1 (different weaknesses)
  - Generate tasks D_2 using K_1
  - Train Solver S_2 on D_2

Round N:
  - Repeat until convergence or compute budget exhausted
```

**Convergence Criterion**:
- Solver improvement plateaus (SWE-bench score change < threshold)
- Or: skill diversity stabilizes (new skills are redundant)

## Implementation Steps

### Step 1: Trace Collection Infrastructure
1. Deploy Solver on SWE-bench datasets
2. Log: (a) code diffs, (b) test outputs, (c) error messages, (d) reasoning chain
3. Store traces in structured format (JSON/Parquet) for distillation

### Step 2: Skill Distillation Pipeline
1. Parse traces → extract error types via regex/pattern matching
2. Cluster by error category: ImportError, SyntaxError, TypeError, LogicError, etc.
3. For each cluster → extract repair pattern (template from successful fixes)
4. Rank skills by `(frequency * success_rate)` → prioritize high-impact

### Step 3: Task Generation Engine
1. Load skill + real repository
2. Identify target files matching skill context
3. Apply mutation (inject failure pattern)
4. Create issue description + expected fix
5. Return candidate task

### Step 4: Validation Framework
1. Execute mutation → run tests → check failure
2. Execute expected fix → run tests → check success
3. Measure difficulty → reject trivial tasks
4. Compute gradient alignment reward → filter by threshold

### Step 5: Solver Training Loop
1. Accumulate validated tasks across rounds
2. Fine-tune Solver on: (SWE-bench + generated tasks)
3. Use gradient alignment to prioritize task sampling
4. Evaluate on SWE-bench → track improvement

## Experimental Results (Paper)

- **SWE-bench Verified**: 50.40% after 3 iterations (baseline ~45%)
- **SWE-bench Lite**: Consistent improvement over self-evolving baselines
- **SWE-bench Pro**: Handles more complex tasks via skill-guided generation
- **Terminal-Bench 2.0**: Cross-domain transfer shows skill generalization

**Compute Budget**: Same for all methods (fair comparison)
- Socratic-SWE: 3 iterations → 50.40%
- Baseline self-evolution: ~45%
- Improvement: +5.4 percentage points

## Pitfalls

- **Skill Overfitting**: Skills may target narrow failure patterns → generate narrow tasks; balance diversity
- **Mutation Validity**: Some mutations produce invalid code → execution-based validation critical
- **Trivial Task Injection**: Easy tasks inflate training data but don't improve Solver; filter by difficulty
- **Compute Budget**: Each iteration requires Solver evaluation + task generation + training; estimate cost
- **Skill Redundancy**: Round N may produce skills overlapping with Round N-1 → deduplicate
- **Gradient Alignment Cost**: Computing gradients for all training tasks is expensive; use approximation

## Verification

1. **Trace Quality**: Inspect distilled skills → verify repair patterns are meaningful
2. **Task Validity**: Run validation pipeline → ensure tests pass/fail correctly
3. **Curriculum Diversity**: Check task distribution → confirm skills evolve across rounds
4. **Solver Improvement**: Track SWE-bench score → monotonic increase across iterations

## References

- arXiv:2606.07412 (June 2026)
- SWE-bench: real-world software engineering benchmark
- Self-evolution in RL agents (curriculum learning)
- Trace-based debugging and repair automation