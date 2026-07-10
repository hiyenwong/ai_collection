# Quantum Software Engineering & Benchmarking Patterns

## Qolumbina: Scalable Quantum Software Testing Benchmark (arXiv: 2607.02029)
- 40 curated quantum programs with systematic selection, refactoring, specifications, unit tests, standardized interfaces
- QST criteria: functionality, output behavior, development complexity, quantum-specific execution complexity
- Backend-dependent effects can skew QST results — always test across multiple backends
- Supports scalability analysis beyond fixed-size circuit benchmarks

## CLAIMSTAB-QC: Auditing Empirical Comparisons (arXiv: 2607.00516)
- Framework for auditing empirical comparisons in quantum software papers
- Records baselines, metrics, relations, admissible evidence; locks design before outcomes
- 455 claims from 119 papers audited → only 8 had enough evidence for direct audit
- Classifies as Sustained/Unresolved/Reversed within locked scope
- **Materialization gap**: most quantum software comparisons cannot be audited without proxy reconstruction

## CV vs DV Quantum Paradigm Comparison (arXiv: 2607.00961)
- Controlled comparison: shared classical backbone + interchangeable quantum heads isolates quantum circuit as sole variable
- CV-QNN: 79.7% vs DV-QNN: 61.6% on WM-811K wafer-map defect classification (18-point gap)
- CV advantage sharpest on spatially localized patterns (Edge-Loc recall 0.66 vs DV ≤0.05)
- DV limitation is representational-capacity ceiling, not optimization failure
- On IBM hardware: DV holds at shallow depth, degrades at deepest circuit

## QPipe: LLM Agentic Quantum Application Generation (arXiv: 2607.00939)
- 6-agent pipeline: parse → formulate → generate → review → execute → verify
- 100% compilation, 96.7% execution rates across 20 NL requirements
- Generated solutions outperform genetic algorithm baseline on test optimization
- Ablation: advantage depends on code-gen skills, task knowledge, review feedback, multi-agent decomposition
