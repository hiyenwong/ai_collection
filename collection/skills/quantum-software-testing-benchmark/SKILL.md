---
name: quantum-software-testing-benchmark
category: quantum
description: Qolumbina benchmark infrastructure for quantum software testing (QST) — curates 40 scalable quantum programs from open-source repos with systematic selection, refactoring, specifications, unit tests, and standardized interfaces. Introduces QST-oriented criteria along functionality, output behavior, development complexity, and quantum-specific execution complexity.
tags: [quantum, software-testing, benchmarking, QST, software-engineering]
arxiv_id: "2607.02029v1"
created: "2026-07-07"
---

# Quantum Software Testing Benchmark (Qolumbina)

## Overview
Qolumbina addresses a critical gap in quantum software testing (QST) research: existing studies rely on small hard-coded or circuit-level benchmarks, while available quantum programs are scattered across repositories without clear selection criteria. Qolumbina provides a controlled, scalable benchmark infrastructure for rigorous empirical QST evaluation.

## Core Contribution

### Program Curation Pipeline
1. **Collection**: Gather 40 programs from open-source quantum repositories
2. **Selection**: Apply systematic criteria for test-relevance
3. **Refactoring**: Standardize code structure and interfaces
4. **Specifications**: Define expected behavior for each program
5. **Test Cases**: Create unit test examples with known outcomes
6. **Standardization**: Provide uniform interfaces for testing tools

### QST-Oriented Characterization Criteria
Quantum programs are characterized along four dimensions:

1. **Functionality**: What the program computes (e.g., optimization, simulation, ML)
2. **Output Behavior**: Deterministic vs probabilistic, scalar vs distribution
3. **Development Complexity**: Code size, dependency depth, language constructs used
4. **Quantum-Specific Execution Complexity**: Qubit count, circuit depth, gate types, backend requirements

### Scalability Analysis
- Supports scalability analysis beyond fixed-size circuit benchmarks
- Programs can be parameterized to test at different scales
- Enables studying how testing approaches perform as programs grow

## Empirical Findings

### Benchmark Coverage
Qolumbina covers diverse testing-relevant properties including:
- Multiple quantum programming frameworks
- Various algorithm categories (VQA, QAOA, quantum ML, etc.)
- Different circuit depths and qubit counts
- Both simulation-ready and hardware-targetable programs

### Testing Approach Evaluation
Through controlled experiments with two recent QST approaches:
- Demonstrated feasibility for **execution-cost studies**
- Demonstrated feasibility for **fault-detection studies**
- Identified **backend-dependent effects** that can influence QST result interpretation

## Implementation Pattern

### Setting Up a QST Experiment
```
1. Select programs from Qolumbina matching your testing criteria
2. Define the testing approach/mutation strategy
3. Run tests across the benchmark suite
4. Measure: fault detection rate, execution cost, false positives
5. Analyze backend-dependent effects on results
6. Report results with locked audit scope (see CLAIMSTAB-QC skill)
```

### Integration with CLAIMSTAB-QC
For auditing empirical comparisons between testing approaches:
- Record baselines, metrics, and admissible evidence
- Lock comparison design before computing outcomes
- Classify results as Sustained, Unresolved, or Reversed

## When to Use
- Developing new quantum software testing approaches
- Benchmarking existing QST tools
- Studying scalability of quantum testing methods
- Comparing quantum testing approaches fairly
- Understanding backend effects on test results

## Activation Keywords
quantum software testing, QST, Qolumbina, quantum benchmark, quantum program testing, quantum test infrastructure, quantum testing scalability, backend-dependent testing, quantum mutation testing
