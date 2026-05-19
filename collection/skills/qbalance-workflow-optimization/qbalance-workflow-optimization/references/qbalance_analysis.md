# QBalance Paper Analysis Reference

## Paper Details
- Title: QBalance: A Reproducible Multi-Objective Workflow for Quantum Compilation, Noise Suppression, and Error-Mitigation Strategy Selection
- arXiv: 2605.02966
- Date: May 2026

## Key Contributions

### 1. Finite Multi-Objective Strategy Selection
Formalizes quantum workflow optimization as selecting from a finite set of strategies.

### 2. Survival-Product Error Proxy
Lightweight fidelity estimator: product of (1 - error_rate) for all gates.

### 3. Bayesian Linear Surrogate
Predicts strategy performance from circuit features when evaluation is expensive.

### 4. Thompson Sampling Ordering
Posterior sampling to order candidates, balancing exploration vs exploitation.

### 5. Distributional Diagnostics
Tracks statistical properties for reproducibility.

## Limitations (from paper)

1. Bandit orders candidates but does not reduce evaluations
2. Layout heuristic is greedy, partially topology-aware
3. ZNE is parity-centered (limited applicability)
4. Cutting integration is a hook, not full pipeline
5. Error proxy assumes independent gate errors

## Connections to Systems Engineering

| QBalance Concept | Systems Engineering Equivalent |
|-----------------|-------------------------------|
| Multi-objective selection | Multi-criteria decision analysis |
| Bayesian surrogate | Surrogate-assisted optimization |
| Survival-product proxy | Reliability engineering (series system) |
| Pareto selection | Pareto frontier analysis |
| Thompson sampling | Multi-armed bandit |
| Distributional diagnostics | Statistical process control |
