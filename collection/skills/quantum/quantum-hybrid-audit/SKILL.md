---
name: quantum-hybrid-audit
description: "Quantum-classical hybrid system audit methodology for measuring actual quantum contribution, decomposing wall-clock time, and identifying where quantum advantage truly exists in hybrid optimization workflows."
---

# Quantum Hybrid Audit Methodology

## Description
Systematic methodology for auditing and decomposing quantum-classical hybrid optimization workflows to measure the actual quantum contribution versus classical computation. Provides quantitative framework for distinguishing genuine quantum advantage from classical post-processing, enabling informed investment decisions in quantum computing applications.

Based on paper: "Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization" (arXiv:2605.17623) — audits D-Wave's hybrid quantum-classical portfolio optimization service, finding QPU access time is only 0.7% of wall-clock budget while the hybrid solver matches Gurobi MIQP optimum on all 54 proven instances.

## Activation Keywords
- quantum hybrid audit, hybrid quantum audit, quantum contribution measurement
- D-Wave hybrid analysis, quantum advantage audit
- hybrid solver decomposition, QPU time analysis
- 量子混合审计, 量子贡献测量, 混合求解器分析
- quantum classical decomposition, hybrid optimization audit

## Core Concepts

### Key Finding from arXiv:2605.17623
When auditing D-Wave's `LeapHybridCQM` solver on cardinality-constrained mean-variance-turnover portfolio optimization (N=10 to 640 assets):
- **QPU access time**: 0.034 seconds out of 5-second wall-clock budget (~0.7%)
- **Classical overhead**: ~99.3% of execution time (problem decomposition, classical post-processing, communication)
- **Solution quality**: Matches Gurobi MIQP proven optimum on all 54 instances where Gurobi proves optimality
- **Implication**: The hybrid solver is highly effective, but the quantum contribution is minimal — classical components dominate

### Audit Dimensions
1. **Time decomposition**: QPU access time vs wall-clock time vs classical processing time
2. **Solution quality comparison**: Against classical baseline (Gurobi, CPLEX, etc.)
3. **Problem size scaling**: How quantum/classical ratio changes with problem size
4. **Constraint handling**: Which constraints are handled by QPU vs classical post-processing
5. **Energy landscape**: Whether quantum or classical components explore the solution space

## Tools Used
- exec: Run benchmark scripts, solver comparisons, timing analysis
- read: Read solver logs, timing profiles, benchmark results
- write: Generate audit reports, comparison tables
- search: Find relevant quantum benchmark papers and baselines

## Usage Patterns

### Pattern 1: Hybrid Solver Audit
Audit a hybrid quantum-classical solver to measure actual quantum contribution.

### Pattern 2: Investment Decision Support
Evaluate whether quantum investment claims are backed by actual quantum advantage or classical heuristics.

### Pattern 3: QPU Utilization Analysis
Analyze the ratio of QPU time to wall-clock time across different problem sizes and formulations.

## Instructions for Agents

### Phase 1: Audit Setup
1. **Define the benchmark problem**: Identify the optimization problem being solved
2. **Select classical baseline**: Choose equivalent classical solver (Gurobi MIQP, CPLEX, etc.)
3. **Configure hybrid solver**: Set up the hybrid quantum-classical solver with identical parameters
4. **Define metrics**: QPU time, wall-clock time, solution quality, feasibility rate

### Phase 2: Decomposition Analysis
1. **Time decomposition**:
   ```
   Wall-clock time = QPU access time + Classical preprocessing + Classical post-processing + Communication overhead
   ```
2. **QPU contribution ratio**: `QPU_time / Wall_clock_time × 100%`
3. **Classical dominance threshold**: If QPU time < 5% of wall-clock, classical components dominate

### Phase 3: Solution Quality Comparison
1. **Optimality gap**: Compare hybrid vs classical optimal solution
2. **Feasibility rate**: Percentage of solutions satisfying all constraints
3. **Time-to-quality**: Time required to reach equivalent solution quality

### Phase 4: Scaling Analysis
1. **Problem size sweep**: Test N=10, 50, 100, 200, 500, 1000+ variables
2. **QPU ratio trajectory**: Does quantum contribution increase with problem size?
3. **Break-even point**: Where does quantum become the dominant component (if ever)?

## Audit Framework

### The Quantum Contribution Index (QCI)
```
QCI = (QPU_time × Solution_Quality_Improvement) / Wall_Clock_Time
```
Where:
- QCI << 1: Classical dominates, quantum is negligible
- QCI ≈ 1: Balanced hybrid system
- QCI >> 1: Quantum dominates the solution process

### Red Flags for Investment Claims
1. **QPU time < 1% of wall-clock**: Quantum is not the bottleneck
2. **No optimality gap improvement**: Hybrid = classical in solution quality
3. **Classical post-processing required**: QPU output is infeasible without classical fixup
4. **Problem decomposition hides complexity**: Classical pre/post-processing does the real work

## Error Handling

### Solver Not Available
- If D-Wave or other quantum hardware is unavailable: Use simulation/emulation with reported timing profiles from literature
- Reference published benchmark results when live access is not possible

### Baseline Comparison Missing
- Use Gurobi Community Edition or open-source alternatives (SCIP, CBC)
- Report optimality gaps rather than absolute comparison when baseline cannot solve to optimality

### QPU Time Data Unavailable
- Many quantum cloud providers do not expose detailed timing breakdowns
- Use published papers' reported values as proxy benchmarks
- Note the limitation clearly in audit reports

## Resources
- arXiv:2605.17623 - "Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization"
- arXiv:2605.17628 - "A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization"
- D-Wave Leap Hybrid CQM documentation
- Gurobi MIQP benchmarking guidelines

## Related Skills
- penalty-free-quantum-annealing-portfolio
- qaoa-xy-mixers-portfolio
- quantum-finance-portfolio
- quantum-systems-engineering
