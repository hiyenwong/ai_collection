---
name: quantum-finance-stack
description: "Financial computation stack framework for evaluating quantum computing applications in finance. Covers five connected domains: constrained portfolio optimisation, derivative pricing, tail-risk and scenario estimation, quantum machine learning, and post-quantum security. Use when: assessing quantum advantage claims in finance, designing hybrid quantum-classical financial workflows, evaluating quantum algorithms for financial applications, conducting quantum finance benchmarks, or building quantum-assisted decision-making pipelines."
---

# Quantum Finance Stack Analysis Framework

## Core Concept

Evaluate quantum finance not as isolated demonstrations but as a connected financial-computation stack. Apply common evaluative logic across all domains:

1. **Identify the financial bottleneck** — What's the binding constraint?
2. **Specify the relevant quantum primitive** — Which quantum algorithm applies?
3. **Compare with explicit classical benchmark** — What's the classical baseline?
4. **Assess under realistic implementation constraints** — Hardware, governance, timelines

## Five Domains

### 1. Constrained Portfolio Optimisation
- **Bottleneck**: Combinatorial search with cardinality, sector, and risk constraints
- **Quantum Primitive**: QAOA, quantum annealing, warm-start QUBO
- **Classical Baseline**: Mixed-integer programming (solves 1000-asset instances in seconds)
- **Assessment**: Limited near-term advantage; strongest case when constrained search dominates

### 2. Derivative Pricing
- **Bottleneck**: Repeated expectation evaluation (Monte Carlo)
- **Quantum Primitive**: Amplitude estimation (quadratic speedup)
- **Classical Baseline**: Monte Carlo with variance reduction
- **Assessment**: Credible advantage path; binding cost is expectation evaluation count

### 3. Tail-Risk and Scenario Estimation
- **Bottleneck**: Rare-event analysis, stress testing
- **Quantum Primitive**: Quantum sampling, amplitude amplification
- **Classical Baseline**: Importance sampling, extreme value theory
- **Assessment**: Task-dependent; depends on distribution complexity

### 4. Quantum Machine Learning
- **Bottleneck**: Representation learning, high-dimensional patterns
- **Quantum Primitive**: QNNs, quantum kernels, variational circuits
- **Classical Baseline**: Deep learning ensembles
- **Assessment**: Highly task-dependent; avoid blanket advantage claims

### 5. Post-Quantum Security
- **Bottleneck**: Long-horizon cryptographic resilience
- **Quantum Primitive**: N/A (defensive, not offensive)
- **Classical Baseline**: RSA, ECC (vulnerable to Shor's algorithm)
- **Assessment**: Already strategically necessary; migrate before fault-tolerant attacks

## Evaluation Methodology

For each quantum finance claim, check:

1. **Is the classical baseline strong enough?** Many papers compare against weak classical baselines
2. **Are constraints realistic?** Real-world portfolios have cardinality, sector, liquidity constraints
3. **Is expert evaluation included?** Algorithmic performance ≠ financial applicability
4. **What's the timeline?** NISQ-era vs fault-tolerant capabilities differ dramatically

## Key Findings from Recent Benchmarks

### D-Wave Hybrid Audit (2605.17623, Lozano 2026)
- **QPU time is only 0.7% of wall-clock**: On 54 cardinality-constrained mean-variance-turnover instances (N=10–640), D-Wave's LeapHybridCQM mean QPU access time = 0.034s out of 5s budget
- **99% is classical pipeline**: Classical decomposition, sub-problem assembly, feasibility-aware reassembly
- **Hybrid win = constraint-native classical pipeline + small QPU contribution**, not a quantum-sampling win
- **Cardinality penalty collapses density**: Creates dense rank-one term making logical graph fully connected regardless of original covariance density
- **Determinism**: Constraint-native service returns identical solutions at every wall-clock budget (5–300s) and across 10 repeated calls
- **Practical implication**: When evaluating quantum finance benchmarks, always audit the QPU vs classical time split; constraint-native interfaces hide the decomposition cost

### Large-Scale Benchmark (2509.17876, Stopfer & Wagner 2025)
- **250 instances with up to 1000 assets**: Classical MIP solves all to proven optimality in seconds
- **Quantum annealing + QAOA vs 6 classical baselines**: Problem-tailored heuristic consistently outperforms all quantum approaches
- **Conclusion**: Only very limited room for quantum advantage in portfolio optimization

### Expert Analysis Evaluation (2507.20532, Innan et al. 2025)
- VQE/QAOA portfolios often violate financial criteria (diversification, risk exposure) despite algorithmic convergence

## Workflow for Quantum Finance Projects

1. **Define the specific financial problem** with realistic constraints
2. **Establish classical baselines** (MIP, heuristics, Monte Carlo)
3. **Select quantum primitive** matching the bottleneck type
4. **Design hybrid workflow** (quantum for hardest subproblem, classical for rest)
5. **Include expert evaluation** — financial professionals assess economic soundness
6. **Benchmark honestly** against strongest classical alternatives

## Error Handling

### Weak Classical Baseline
Always compare against problem-tailored classical heuristics, not just generic solvers.

### Overstated Quantum Advantage
Apply the stack framework: identify which specific domain layer shows advantage.

### Missing Expert Validation
Algorithmic convergence ≠ financial viability. Always include domain expert assessment.

## Related Skills
- quantum-portfolio-optimizer: Practical portfolio optimization implementations
- quantum-finance-analysis: Broader quantum finance applications
- hotstart-quantum-portfolio: Warm-start methodology for portfolio QUBO

## References
- arXiv: 2605.17623 - "Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization" (Lozano, 2026) — D-Wave hybrid audit revealing QPU contributes only 0.7% of runtime
- arXiv: 2604.08180 - "Quantum Computing for Financial Transformation" (Gong et al., 2026) — 134-page comprehensive review
- arXiv: 2509.17876 - "Quantum Portfolio Optimization: An Extensive Benchmark" (Stopfer & Wagner, 2025)
- arXiv: 2507.20532 - "Quantum Portfolio Optimization with Expert Analysis Evaluation" (Innan et al., 2025)
