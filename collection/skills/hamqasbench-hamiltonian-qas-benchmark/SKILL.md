---
name: hamqasbench-hamiltonian-qas-benchmark
description: "Hamiltonian-informed diagnostic benchmark for Quantum Architecture Search (QAS). Organizes molecules into structural tiers via Pauli operator fingerprints, computational basis representation, and ground-state entanglement. Detects failure modes invisible to energy-only metrics: over-parameterization, eigenstate commitment, representation bottleneck, topology-induced routing failure. Activation: QAS benchmark, Hamiltonian structure, quantum architecture search evaluation, circuit structure analysis, variational circuit diagnostics"
metadata:
  arxiv_id: "2607.04845"
  published: "2026-07-06"
  authors: "HamQASBench authors"
  tags: [quantum, architecture-search, benchmark, hamiltonian, variational]
---

# HamQASBench: Hamiltonian-Informed QAS Benchmark

## Core Methodology

**Problem**: Existing QAS benchmarks organize by molecular identity or qubit count — criteria agnostic to Hamiltonian structure. They rely solely on energy accuracy, which cannot detect structural failures (over-parameterization, eigenstate commitment under degeneracy, representation bottleneck).

**Solution**: HamQASBench organizes 11 molecules into 5 structural tiers via fingerprints from:
1. **Pauli operator basis** — Hamiltonian term structure
2. **Computational basis representation** — sparsity patterns
3. **Ground-state entanglement** — per-qubit entanglement analysis

**Key diagnostic tools**:
- Post-hoc critical-structure extraction: identifies minimal circuits consistent with each tier's requirements
- Per-qubit entanglement analysis
- Pairwise state fidelity (beyond energy accuracy)

## Failure Modes Detected

| Failure Mode | Regime | Detection Method |
|---|---|---|
| Over-parameterization | Minimalism regime | Critical-structure extraction vs actual circuit size |
| Eigenstate commitment | Degenerate systems | Pairwise state fidelity |
| Representation bottleneck | Strongly correlated systems | Per-qubit entanglement analysis |
| Topology-induced routing failure | Hardware-constrained search | Circuit topology vs Hamiltonian structure |
| Search space growth | Scalability | Circuit complexity vs qubit count |

## Usage Patterns

### Pattern 1: QAS Method Evaluation
When evaluating a QAS method, use Hamiltonian-informed tiering instead of molecule-by-molecule benchmarking:
1. Extract Pauli fingerprints from target Hamiltonian
2. Assign molecule to structural tier (1-5)
3. Run QAS method, measure per-tier performance
4. Apply critical-structure extraction to check minimal circuit consistency
5. Compute per-qubit entanglement and pairwise fidelity

### Pattern 2: Detecting Structural Failures
When energy accuracy looks good but results are suspect:
1. Check per-qubit entanglement distribution vs expected
2. Run pairwise state fidelity between QAS output and known structure
3. Extract minimal circuit from result and compare to tier requirements
4. Flag over-parameterization if circuit >> minimal requirement

### Pattern 3: Hardware-Aware QAS
When evaluating QAS under hardware topology constraints:
1. Map Hamiltonian structure to device topology
2. Identify routing conflicts (structure vs connectivity mismatch)
3. Measure topology-induced performance degradation per tier

## Activation Keywords
- quantum architecture search benchmark
- Hamiltonian-informed benchmark
- QAS evaluation
- variational circuit structure analysis
- quantum circuit diagnostics
- ground-state entanglement analysis
- QAS failure mode detection
- 量子架构搜索基准
- 哈密顿量结构分析

## Tools Used
- terminal: Run benchmarking scripts, analyze results
- write_file: Create benchmark configurations
- search_files: Check existing QAS skills

## Related Skills
- `quantum-neural-architecture-search` — QAS methodology
- `magic-informed-quantum-architecture-search` — magic-state-based QAS
- `zero-shot-quantum-nas` — zero-shot QAS approach
- `quantum-ml-patterns` — QML evaluation patterns
