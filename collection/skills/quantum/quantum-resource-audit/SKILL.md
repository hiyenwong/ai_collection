---
name: quantum-resource-audit
description: "Methodology for auditing quantum resource utilization in hybrid quantum-classical optimization — measuring actual QPU time vs classical compute budget to determine genuine quantum advantage."
category: quantum-finance
---

# Quantum Resource Audit Methodology

## Description
When evaluating hybrid quantum-classical optimization services (like D-Wave's LeapHybridCQM), it's critical to audit how much of the computation is actually quantum. On cardinality-constrained mean-variance-turnover portfolio optimization instances (N=10 to 640), the mean QPU access time is only 0.034 seconds out of a 5-second wall-clock budget — roughly 0.7% of the run. The remaining ~99.3% is classical pre/post-processing.

This skill provides a systematic framework for auditing quantum resource utilization, identifying where genuine quantum advantage lies, and making informed decisions about quantum vs classical approaches.

## Trigger Conditions
- Evaluating quantum advantage claims for hybrid quantum-classical algorithms
- Benchmarking quantum optimization services against classical solvers
- Deciding whether to invest in quantum computing for specific problems
- Analyzing the quantum-to-classical compute ratio in hybrid algorithms

## Core Methodology

### Step 1: Establish Classical Baseline
- Use state-of-the-art classical solvers (Gurobi, CPLEX) as optimality anchors
- Record solve times, solution quality, and proof of optimality
- Identify the problem sizes where classical solvers succeed/fail

### Step 2: Decompose Hybrid Runtime
Break down the total wall-clock time into components:
- **QPU access time**: Actual quantum processor execution
- **Pre-processing**: Classical problem formulation, embedding, parameter tuning
- **Post-processing**: Solution repair, constraint enforcement, result aggregation
- **Classical subroutines**: Any classical optimization within the hybrid loop

### Step 3: Quantum Contribution Analysis
- Compare QPU contribution to total runtime
- Evaluate if quantum results exceed classical heuristics
- Measure solution quality improvement attributable to quantum component

### Step 4: Scaling Analysis
- Test across problem sizes (small N to large N)
- Identify crossover points where quantum becomes competitive
- Analyze asymptotic behavior of quantum vs classical components

## Key Metrics
| Metric | Formula | Target |
|--------|---------|--------|
| QPU ratio | QPU_time / wall_clock_time | >10% for genuine quantum contribution |
| Speedup | classical_time / quantum_time | >1x for advantage |
| Quality gap | (quantum_obj - optimal_obj) / optimal_obj | <1% for practical use |
| Embedding efficiency | logical_qubits / physical_qubits | >50% for efficient use |

## Activation Keywords
- quantum resource audit
- QPU time analysis
- hybrid quantum classical benchmark
- quantum advantage measurement
- D-Wave hybrid audit
- arXiv:2605.17623

## Pitfalls
- **Wall-clock illusion**: A fast total time doesn't mean quantum is doing the work
- **Classical anchor missing**: Without proven optimal solutions, quality claims are meaningless
- **Small-N bias**: Quantum may look competitive only on problems classical solves trivially
- **Parameter tuning cost**: Extensive parameter search inflates classical component

## References
- arXiv:2605.17623 — "Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization"
