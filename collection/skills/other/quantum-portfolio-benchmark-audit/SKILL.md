---
name: quantum-portfolio-benchmark-audit
description: "Critical benchmark methodology for evaluating quantum portfolio optimization claims. Provides systematic comparison framework testing quantum annealing and QAOA against classical solvers (MIP, simulated annealing, tabu search, problem-tailored heuristics) on real-world instances up to 1,000 assets. Key finding: classical MIP solves all instances to proven optimality in seconds; problem-tailored heuristics consistently outperform quantum approaches in solution quality for fixed runtime. Use when: evaluating quantum advantage claims for portfolio optimization, benchmarking quantum vs classical solvers, designing fair quantum-classical comparisons."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2509.17876"
  published: "2025-09-22"
  authors: "Eric Stopfer, Friedrich Wagner"
  tags: [quantum, portfolio, optimization, benchmark, classical-comparison, quantum-annealing, qaoa, mixed-integer-programming, quantum-advantage-audit]
---

# Quantum Portfolio Benchmark Audit

## Overview
Critical benchmark methodology for evaluating quantum portfolio optimization claims against state-of-the-art classical solvers. Demonstrates that for practical portfolio optimization, classical mixed-integer programming and problem-tailored heuristics significantly outperform quantum approaches (quantum annealing, QAOA) on real-world instances up to 1,000 assets.

## Source
- **Paper**: "Quantum Portfolio Optimization: An Extensive Benchmark"
- **arXiv**: 2509.17876 (Sep 2025)
- **Authors**: Eric Stopfer, Friedrich Wagner
- **Enhanced**: 2026-06-14 - Added Expert Analysis Evaluation cross-reference (arXiv:2507.20532) and Hot-Starting methodology (arXiv:2510.11153)

## Core Methodology

### 1. Benchmark Instance Design
- 250 portfolio optimization instances from actual stock data
- Up to 1,000 assets per instance
- Variant of portfolio optimization particularly difficult for classical solvers
- Real-world data, not synthetic benchmarks

### 2. Classical Baselines (Must-Compare)
Any quantum portfolio optimization study MUST compare against:
- **Mixed-Integer Programming (MIP)**: Proven optimality in seconds for all instances
- **Simulated Annealing**: General-purpose metaheuristic
- **Steepest Descent Local Search**: Simple but effective baseline
- **Tabu Search**: Memory-enhanced local search
- **Problem-Tailored Heuristics**: Custom algorithms exploiting problem structure

### 3. Quantum Approaches Tested
- **Quantum Annealing**: D-Wave Advantage quantum annealer
- **QAOA**: Quantum Approximate Optimization Algorithm

### 4. Evaluation Metrics
- **Solution Quality**: Optimality gap from proven optimal
- **Runtime**: Fixed runtime comparison
- **Scalability**: Performance as asset count increases
- **Proven Optimality**: Whether solver can certify optimality

### 5. Key Findings
- MIP solves ALL instances to proven optimality in seconds
- Problem-tailored heuristic consistently outperforms quantum approaches
- Very limited room for potential quantum advantage in portfolio optimization
- Classical solvers dominate in both solution quality and runtime

## Benchmark Protocol

### Step 1: Define Problem Instance
```
Input: N assets, return matrix R, covariance matrix Sigma
Constraints: Cardinality, budget, sector limits
Objective: Minimize risk (variance) subject to return target
```

### Step 2: Establish Classical Baselines
```python
# MIP baseline (Gurobi/CPLEX)
model = mip_model(assets, returns, covariances, constraints)
solution, gap, time = model.solve()

# Heuristic baselines
sa_solution = simulated_annealing(assets, returns, covariances)
tabu_solution = tabu_search(assets, returns, covariances)
custom_solution = problem_tailored_heuristic(assets, returns, covariances)
```

### Step 3: Run Quantum Solvers
```python
# Quantum Annealing
qa_solution = quantum_annealer(assets, returns, covariances, QPU=QPU_DWAVE)

# QAOA
qaoa_solution = qaoa_solver(assets, returns, covariances, p_depth=p)
```

### Step 4: Compare Results
- Optimality gap for each method
- Runtime comparison
- Solution quality under fixed time budget
- Scalability analysis (10, 50, 100, 500, 1000 assets)

## Critical Evaluation Checklist

When reviewing quantum portfolio optimization papers, check:

1. [ ] Are classical baselines included? (MIP, simulated annealing, tabu search)
2. [ ] Is problem-tailored heuristic tested?
3. [ ] Are instances from real-world data?
4. [ ] Is solution quality measured against proven optimal?
5. [ ] Is runtime comparison fair (fixed time budget)?
6. [ ] Is scalability analyzed across instance sizes?
7. [ ] Are problem-tailored classical algorithms considered?

## Applications
- **Quantum Advantage Verification**: Critical assessment of quantum portfolio claims
- **Algorithm Benchmarking**: Fair comparison framework for quantum vs classical solvers
- **Investment Decision**: When to use quantum vs classical for portfolio problems
- **Research Quality Control**: Preventing over-claiming of quantum advantage

## Pitfalls
1. **Over-Claiming**: Many papers claim quantum advantage without proper classical baselines
2. **Synthetic Instances**: Synthetic benchmarks may not reflect real-world difficulty
3. **Small Instances**: Quantum may work for tiny instances but classical dominates at scale
4. **Unfair Comparison**: Comparing against naive classical algorithms, not state-of-the-art
5. **Ignoring Heuristics**: Problem-tailored heuristics often outperform both quantum and MIP

## Activation
- **When**: Evaluating quantum portfolio optimization papers, designing benchmark studies, assessing quantum advantage claims, comparing quantum vs classical solvers
- **Keywords**: quantum portfolio benchmark, portfolio optimization audit, quantum vs classical comparison, quantum advantage verification, portfolio benchmarking, QAOA portfolio audit, quantum annealing portfolio comparison

## Related Skills
- quantum-portfolio-optimizer
- qaoa-manifold-optimization
- quantum-optimization-landscape-analysis
- qml-fraud-detection-comparison