---
name: trapped-ion-portfolio-optimization
description: "End-to-end pipeline for large-scale portfolio selection with cardinality constraints using trapped-ion quantum computers. Use when: executing portfolio optimization on trapped-ion QPU hardware; solving QUBO subproblems via BF-DCQO; decomposing large portfolios via correlation-guided splitting; implementing two-stage post-processing for cardinality constraints; benchmarking quantum vs classical portfolio methods. Keywords: trapped-ion, portfolio optimization, QUBO decomposition, BF-DCQO, correlation matrix, random matrix theory, cardinality constraints"
---

# Trapped-Ion Portfolio Optimization

## Core Concept

End-to-end pipeline that decomposes large portfolio optimization problems into hardware-embeddable QUBO subproblems, solves them on trapped-ion quantum processors using BF-DCQO (Bias-Field Digitized Counterdiabatic Quantum Optimization), and recombines solutions with cardinality-preserving post-processing.

## Workflow

### Phase 1: Correlation Analysis

1. **RMT-based Denoising**: Apply Random Matrix Theory to clean the correlation matrix
   - Compute eigenvalue spectrum of asset return correlations
   - Filter eigenvalues within the Marcenko-Pastur bulk (noise)
   - Reconstruct denoised correlation matrix from significant eigenvalues only

2. **Community Detection**: Identify groups of correlated assets
   - Apply Louvain or similar community detection on the correlation graph
   - Each community becomes a candidate subproblem

### Phase 2: QUBO Decomposition

3. **Correlation-Guided Greedy Splitting**: Cap each cluster by executable qubit budget
   ```
   For each community C:
     if |C| <= qubit_budget:
       subproblem = C
     else:
       split C into chunks of size <= qubit_budget
       using correlation-guided greedy partitioning
   ```

4. **BF-DCQO Execution**: Solve each subproblem non-variationally
   - No classical parameter-training loops (avoids barren plateaus)
   - Uses counterdiabatic driving terms for faster convergence
   - Bias fields steer optimization toward feasible solutions

### Phase 3: Recombination and Post-Processing

5. **Candidate Recombination**: Merge low-energy candidates into global portfolios

6. **Two-Stage Post-Processing**:
   - **Fast Repair**: Fix constraint violations (budget, cardinality)
   - **Cardinality-Preserving Swap Local Search**: Optimize within fixed cardinality

## Key Parameters

| Parameter | Typical Value | Description |
|-----------|--------------|-------------|
| Qubit Budget | 20-64 | Max qubits per subproblem (hardware-dependent) |
| Universe Size | 100-500 | Total assets in portfolio |
| Cardinality K | 10-50 | Number of assets to select |

## Pattern: Hardware-Aware Problem Decomposition

When NISQ devices have limited qubits:
1. Cluster the problem using domain knowledge (correlations)
2. Split clusters to fit hardware constraints
3. Solve subproblems independently
4. Recombine with feasibility-preserving operations

## Benchmarks

- Demonstrated on 250-asset S&P 500 universe
- Executed on 64-qubit Barium development system (IonQ Tempo line)
- Larger executable subproblems → reduced decomposition error → better risk-return trade-offs

## Pitfalls

- **Decomposition error**: Splitting loses cross-cluster correlations
- **Hardware noise**: NISQ errors accumulate with circuit depth
- **Post-processing bottleneck**: Repair step may degrade quantum advantage
- **Turnover**: High portfolio turnover increases transaction costs

## References

- arXiv: 2602.23976 - "Large-scale portfolio optimization on a trapped-ion quantum computer"
