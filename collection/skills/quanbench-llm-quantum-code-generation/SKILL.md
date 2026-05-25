---
name: quanbench-llm-quantum-code-generation
description: "QuanBench+ benchmark methodology for evaluating LLM-based quantum code generation across multiple frameworks (Qiskit, PennyLane, Cirq). Uses executable functional tests, Pass@1/Pass@5 metrics, KL-divergence acceptance for probabilistic outputs, and feedback-based repair. Activation: quantum code generation, LLM quantum coding, QuanBench, quantum programming benchmark, quantum code evaluation."
---

# QuanBench+: LLM-Based Quantum Code Generation Benchmark

Unified multi-framework benchmark for evaluating Large Language Models on quantum code generation, covering Qiskit, PennyLane, and Cirq with 42 aligned tasks.

**Source**: arXiv:2604.08570 — "QuanBench+: A Unified Multi-Framework Benchmark for LLM-Based Quantum Code Generation"

## Problem

- LLMs increasingly used for code generation
- Quantum code generation evaluated mostly within single frameworks
- Cannot separate quantum reasoning from framework familiarity
- No unified benchmark spanning multiple quantum frameworks

## Benchmark Design

### Task Coverage (42 tasks across 3 frameworks)
1. **Quantum Algorithms** — Implement standard quantum algorithms
2. **Gate Decomposition** — Decompose gates into basis gate sets
3. **State Preparation** — Prepare specific quantum states

### Evaluation Frameworks
- **Qiskit** (IBM) — Industry standard
- **PennyLane** (Xanadu) — Quantum ML focused
- **Cirq** (Google) — NISQ device focused

### Evaluation Metrics

| Metric | Description |
|--------|-------------|
| Pass@1 | Single-shot code generation accuracy |
| Pass@5 | Best of 5 attempts accuracy |
| Pass@1 + Repair | Accuracy after feedback-based repair (model revises after runtime error) |
| KL-divergence | Acceptance criterion for probabilistic outputs |

### Key Results

| Framework | Pass@1 (best) | Pass@1 + Repair (best) |
|-----------|---------------|------------------------|
| Qiskit    | 59.5%         | 83.3%                  |
| Cirq      | 54.8%         | 76.2%                  |
| PennyLane | 42.9%         | 66.7%                  |

### Implementation Pattern

```python
class QuanBenchEvaluator:
    def __init__(self, frameworks=['qiskit', 'pennylane', 'cirq']):
        self.frameworks = frameworks
        self.tasks = load_42_aligned_tasks()
        
    def evaluate(self, model):
        results = {}
        for framework in self.frameworks:
            framework_tasks = self.get_framework_tasks(framework)
            passes = 0
            for task in framework_tasks:
                # One-shot evaluation
                code = model.generate(task.prompt, framework)
                if self.execute_and_test(code, task):
                    passes += 1
                else:
                    # Feedback-based repair
                    error = self.get_error(code, task)
                    repaired = model.repair(code, error, task)
                    if self.execute_and_test(repaired, task):
                        passes += 1
            
            results[framework] = {
                'pass@1': passes / len(framework_tasks),
                'pass@5': self.compute_pass_at5(model, task),
                'pass@1_repair': self.compute_pass_at1_repair(model, framework_tasks)
            }
        return results
    
    def evaluate_probabilistic(self, code, expected_distribution):
        """KL-divergence acceptance for probabilistic quantum outputs"""
        actual = execute_and_measure(code, n_shots=1000)
        kl = kl_divergence(actual, expected_distribution)
        return kl < threshold
```

## When to Use

- Evaluating LLMs for quantum programming tasks
- Comparing quantum code generation across frameworks
- Assessing whether models understand quantum concepts vs. framework syntax
- Building quantum coding assistants or automated quantum code generation pipelines

## Key Insights

1. **Framework dependency**: Strong models still framework-dependent (Qiskit > Cirq > PennyLane)
2. **Repair helps**: Feedback-based repair significantly boosts scores (59.5% → 83.3% for Qiskit)
3. **Multi-framework gap**: Reliable multi-framework quantum code generation remains unsolved
4. **Quantum reasoning vs. syntax**: Need benchmarks that separate quantum understanding from framework familiarity

## Pitfalls

- Probabilistic quantum outputs require special evaluation (KL-divergence, not exact match)
- Framework-specific knowledge dominates current LLM performance
- 42 tasks may not cover all quantum programming patterns
- NISQ-era constraints (noise, limited qubits) affect code correctness testing

## Related Skills

- `quantum-program-analysis` - quantum code quality assurance
- `quantum-program-linting` - static analysis for quantum programs
- `qml-model-testing` - QML model testing and robustness