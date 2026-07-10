---
name: quantum-program-analysis
description: >
  LLM-powered analysis and quality assurance for quantum programs.
  Use when: (1) linting quantum circuits/programs beyond simple rule checks,
  (2) analyzing quantum algorithm correctness and optimization opportunities,
  (3) evaluating quantum program performance under noise models,
  (4) benchmarking quantum primitives under hardware-motivated noise,
  (5) distributed quantum algorithm compilation and analysis.
  Covers LLM-based quantum linting, FTPrimitiveBench noise benchmarking,
  and topological quantum computing patterns.
---

# Quantum Program Analysis

## Core Challenge
Traditional static analysis (rule-based linters) is inadequate for complex quantum programs
that require understanding of quantum mechanics, circuit optimization, and noise behavior.

## Key Methodologies

### 1. LLM-Powered Quantum Linting
- Use LLMs to analyze quantum program correctness
- Detect optimization opportunities beyond syntactic rules
- Identify quantum-specific anti-patterns (unnecessary gates, suboptimal decompositions)
- Provide natural language explanations of issues

### 2. Noise-Aware Benchmarking (FTPrimitiveBench)
- Test quantum primitives under hardware-motivated noise models
- Biased noise models reflecting real quantum hardware error profiles
- Benchmark logical computation fidelity under different noise regimes
- Evaluate fault tolerance thresholds for specific architectures

### 3. Topological Quantum Computing Analysis
- Anyonic quantum computation patterns
- Braiding trajectory optimization for gate operations
- Two-qubit gate implementation challenges in topological models
- Error resistance properties of topological encoding

### 4. Distributed Quantum Algorithm Compilation
- Shor algorithm distributed across multiple quantum modules
- Inter-module communication latency analysis
- Compilation strategies for multi-qubit modular processors
- Resource estimation for large-scale factoring (2048-bit RSA)

### 5. Quantum Test Reliability and Flaky Test Detection
- Quantum programs have inherently probabilistic outputs, making tests susceptible to "quantum flakiness"
- Flaky tests: pass/fail inconsistently without code changes due to measurement noise, hardware variability
- LLM-based detection pipeline: classify issues/PRs as flaky vs non-flaky (Gemini F1=0.9420)
- Root cause identification from issue descriptions + code context (F1=0.9643)
- Cosine similarity expansion: discover previously unknown flaky tests by finding semantically similar issues
- Can expand known flaky test datasets by 50%+ using this methodology
- Root cause categories: probabilistic measurement outcomes, hardware noise variability, simulation seed differences, timing-dependent circuit execution
- **Key paper**: "Automating Detection and Root-Cause Analysis of Flaky Tests in Quantum Software" (arXiv: 2603.09029)

## Implementation Steps

1. **Program parsing**: Parse quantum circuit (QASM, Q#, Cirq, etc.)
2. **Static analysis**: Check basic correctness and gate validity
3. **LLM analysis**: Query LLM for optimization suggestions
4. **Noise simulation**: Evaluate under hardware-specific noise models
5. **Benchmark comparison**: Compare against FTPrimitiveBench baselines
6. **Test reliability assessment**: Detect flaky tests, classify root causes, expand test datasets

## Common Pitfalls
- Quantum programs may appear correct syntactically but have logical errors
- Noise models must match target hardware for accurate predictions
- Distributed compilation introduces non-trivial communication overhead
- Topological gate implementations require careful anyon braiding planning

## Related Skills
- quantum-ml-research
- quantum-error-correction-methods
- quantum-neural-architecture
- quantum-flaky-test-detection
- quantum-toolchain-mining
