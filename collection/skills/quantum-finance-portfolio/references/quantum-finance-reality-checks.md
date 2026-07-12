# Quantum Finance: Practical Reality Checks and Emerging Techniques

## Quantum Advantage Reality Check (from arXiv:2605.17623)

**D-Wave Hybrid Service Audit Finding**: When benchmarking D-Wave's LeapHybridCQM on cardinality-constrained mean-variance-turnover portfolio instances (N=10 to 640) against Gurobi MIQP:
- Matched Gurobi's proven optimum on all 54 instances where Gurobi proved optimality
- **Mean QPU access time: only 0.034 seconds out of 5-second wall-clock budget (~0.7%)**
- The remaining ~99.3% is classical preprocessing/postprocessing

**Implication**: Claims of "quantum portfolio optimization" on current hybrid services are largely classical computation with minimal quantum contribution. Always audit QPU utilization time when evaluating quantum finance benchmarks.

## End-to-End Quantum PDE Pricing (from arXiv:2605.26610)

Key advancement: First framework that includes ALL subroutines (encoding, solving, readout) with explicit complexity bounds for multi-asset European option pricing under:
- Black-Scholes (local volatility)
- Heston (stochastic volatility)

Achieves exponential speedup in dimension for N=2^n grid points per spatial dimension via QLSA + amplitude estimation.

## Quantum Stochastic Process Learning (from arXiv:2603.24069)

Quantum sequence models with recurrent quantum circuits can learn stochastic processes with exponential state space efficiency:
- n qubits represent 2^n-dimensional probability distributions
- Recurrent structure captures temporal dependencies
- Applications: risk analysis, importance sampling, Monte Carlo acceleration

## NISQ Credit Risk Adaptation (from arXiv:2601.06865)

Experimental study of hardware noise impact on quantum circuit-based credit risk adaptation. Key finding: NISQ processor noise sensitivity is a practical bottleneck that cannot be ignored in pre-fault-tolerant quantum finance algorithms.
