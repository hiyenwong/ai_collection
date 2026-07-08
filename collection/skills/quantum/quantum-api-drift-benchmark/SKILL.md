---
name: quantum-api-drift-benchmark
description: "Benchmark for measuring API drift in LLM-generated quantum code across successive SDK versions. Evaluates version fidelity, cross-version compatibility, failure modes, and documentation-guided repair. Instantiated with Qiskit v0.43, v1.3, v2.0. Activation: quantum SDK version testing, LLM quantum code evaluation, API drift benchmark, quantum code generation fidelity, Qiskit version compatibility, 量子API漂移"
metadata:
  arxiv_id: "2607.04072"
  published: "2026-07-05"
  authors: "quantum-api-drift authors"
  tags: [quantum, benchmark, llm, sdk, api-drift, code-generation]
---

# Quantum API Drift Benchmark

## Core Methodology

**Problem**: LLMs generate plausible quantum code but reliability across SDK versions is unknown. API drift (interface changes between SDK versions) causes subtle failures.

**Solution**: quantum-api-drift benchmark measuring 4 axes:
1. **Version fidelity** — execution success on requested SDK version
2. **Cross-version compatibility** — does code work on adjacent versions?
3. **Failure mode taxonomy** — broken imports vs deprecation vs semantic errors
4. **Documentation-guided repair** — can repair succeed with migration guidance?

**Scale**: 17 models × 50 tasks × 3 samples × 3 SDK versions = 7,650 executions per model.

## Key Findings

- Diagonal Pass@1 ranges 0.02–0.85 across models
- Stronger models fail at deprecation level; weaker models fail at import level
- Documentation-guided repair: 0.19–0.59 success rate
- Repair more effective for forward migration (v1.3→v2.0) than backward (v2.0→v1.3)
- Version alignment is a distinct evaluation axis beyond code correctness

## Usage Patterns

### Pattern 1: Version Fidelity Testing
When evaluating LLM quantum code generation:
1. Select target SDK version (e.g., Qiskit v2.0)
2. Generate code with specific version request in prompt
3. Execute on exact version — measure Pass@1
4. Repeat across versions to build diagonal accuracy matrix

### Pattern 2: Failure Mode Analysis
When diagnosing LLM quantum code failures:
1. Classify failure: import error, deprecation warning, semantic error, timeout
2. Correlate failure type with model strength tier
3. Weak models → broken imports; strong models → deprecation-level failures
4. Use taxonomy to target improvements (prompt engineering vs SDK-specific fine-tuning)

### Pattern 3: Documentation-Guided Repair
When attempting to fix version-mismatched quantum code:
1. Provide SDK migration documentation to LLM
2. Request version-specific fix
3. Measure repair success rate per direction (forward/backward migration)
4. Note: forward migration consistently easier than backward

## Activation Keywords
- quantum API drift
- SDK version testing
- LLM quantum code evaluation
- quantum code generation benchmark
- Qiskit version compatibility
- quantum software testing
- API version fidelity
- 量子API漂移
- 量子SDK版本测试

## Related Skills
- `quantum-software-testing-benchmark` — quantum software testing infrastructure
- `qpipe-agentic-quantum-code-gen` — agentic quantum code generation
- `quantum-program-analysis` — quantum program quality assurance
- `quantum-empirical-comparison-audit` — empirical audit frameworks
