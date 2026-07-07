---
name: quantum-probability-statistics
category: mathematics
description: Framework for applying quantum probability theory to statistical analysis, cognitive modeling, and decision-making — using square-root probability amplitudes, matrix-based observations, and quantum inference.
activation: quantum probability, confirmation bias, active inference, hypothesis testing, square-root probability, matrix observations, sequential evidence
created_at: 2026-06-26
arxiv: 2606.23325
source: arXiv:2606.23325v1
---

# Quantum Probability Statistics Framework

## Background

This framework reformulates probability theory using the mathematical structures of quantum mechanics — representing probabilities as square-root amplitudes and observations as matrices rather than random variables on a probability space. This enables modeling cognitive phenomena like confirmation bias as rational optimization outcomes.

## Core Concepts

### 1. Square-Root Probability Space
- Probabilities are represented as amplitudes: `p = |ψ|²`
- State vectors live in a Hilbert space over square-root probabilities
- Enables superposition-like interference effects in probability updates

### 2. Matrix-Based Observations
- Observations are modelled as operators (matrices), not scalar random variables
- Evidence choice becomes a matrix selection problem
- Sequential evidence sampling operates over the space of matrices

### 3. Optimal Evidence Selection
- In binary hypothesis testing, optimal evidence choice minimizes expected error probability
- Two evolutionary advantages emerge:
  - **Memory efficiency**: decision maker requires only minimal memory capacity
  - **Error reduction**: error probability decreases exponentially in sample size

### 4. Active Quantum Inference
- Decision maker seeks evidence providing maximum information
- Optimal evidence from active inference agrees with error-minimization approach
- Provides implementable protocol for adaptive evidence sampling

## Methodology

### Step 1: Problem Formulation
- Define hypothesis space as vectors in square-root probability space
- Represent observations as measurement matrices
- Establish prior probability amplitudes

### Step 2: Evidence Optimization
- Formulate evidence selection as matrix optimization
- Minimize expected error probability over matrix space
- Alternatively: maximize information gain (active inference)

### Step 3: Sequential Sampling Protocol
- Iteratively select optimal evidence matrices
- Update state via matrix transformations
- Track error probability convergence

### Step 4: Analysis of Confirmation Bias
- Show that optimal evidence choice naturally leads to confirmation bias
- This is rational: confirms existing beliefs because it minimizes error
- Bias emerges from optimality, not irrationality

## Applications

- **Cognitive modeling**: Understanding rational basis of cognitive biases
- **Sequential hypothesis testing**: Optimal evidence gathering strategies
- **Active learning**: Information-theoretic evidence selection
- **Decision theory**: Bridging quantum formalism with classical decision problems

## Key Mathematical Tools

- Square-root probability amplitudes
- Matrix-valued observations
- Expected error probability minimization
- Active inference / information maximization
- Sequential Bayesian updating in amplitude space

## Related Patterns

- Connects to Bayesian hypothesis testing
- Bridges quantum information theory with cognitive science
- Provides formal basis for understanding bounded rationality
- Links to active inference frameworks in neuroscience
