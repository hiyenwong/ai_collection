---
name: adaptive-acquisition-bbo
description: "Adaptive acquisition function selection for discrete black-box optimization (BOCS + GP-LCB hybrid). Based on arXiv:2605.10856 (Shikanai & Ohzeki, 2026). Use when optimizing QUBO, HUBO, or any discrete-variable black-box problem where BOCS stagnates. Combines parametric surrogate with Gaussian-process-based adaptive LCB selection for exploration-exploitation balance. Also applicable to quantum annealing sparse surrogate construction and combinatorial search. Activation: adaptive acquisition, BOCS stagnation, discrete Bayesian optimization, QUBO optimization, HUBO optimization, black-box optimization, quantum-inspired search, combinatorial optimization"
---

# Adaptive Acquisition Black-Box Optimization

## Overview

A hybrid search framework combining **BOCS** (Bayesian Optimization of Combinatorial Structures) as the primary parametric surrogate with a **Gaussian Process + adaptive Lower Confidence Bound (LCB)** component that activates only when stagnation is detected. Solves the fundamental problem of BOCS repeatedly proposing already-evaluated points as observations grow.

Based on: Shikanai & Ohzeki (2026), *Improving search efficiency via adaptive acquisition function selection in discrete black-box optimization*, arXiv:2605.10856.

## When to Use

- QUBO/HUBO problems with expensive evaluations
- BOCS or similar parametric Bayesian optimization on discrete variables
- Quantum annealing sparse surrogate construction
- Any discrete black-box search showing stagnation (repeated proposals)

## Core Algorithm

### Step 1: Run BOCS as Primary Search

BOCS fits a parametric surrogate model (sparse regression) over binary variables and proposes candidates via its acquisition function. Works well for early-stage optimization with few observations.

### Step 2: Detect Stagnation

**Stagnation criteria**: BOCS proposes a point that has already been evaluated (duplicate). This signals the parametric surrogate has exhausted its unique proposals.

### Step 3: Activate GP-LCB Component (On Stagnation Only)

When stagnation is detected:

1. **Train a Gaussian Process** on all observed data using a Hamming-distance kernel:
   ```
   k(x, x') = σ² · exp(-λ · d_H(x, x')/d)
   ```
   where d_H is the Hamming distance, d is the problem dimension.

2. **Compute multiple LCB acquisition functions** with varying exploration parameters β:
   ```
   LCB_β(x) = μ(x) - β · σ(x)
   ```
   Use β ∈ {0.1, 0.5, 1.0, 2.0, 5.0} to span exploitation-to-exploration spectrum.

3. **Adaptively select the best β** based on recent search progress:
   - Track improvement in objective over the last k iterations
   - If recent progress > 0: favor smaller β (exploitation)
   - If recent progress ≈ 0: favor larger β (exploration)
   - Simple rule: select β that maximizes acquisition value at unevaluated points

4. **Generate alternative unevaluated point** by minimizing the selected LCB among unevaluated candidates. Use a short random restart or local search over the Hamming neighborhood.

### Step 4: Evaluate and Update

Evaluate the proposed point on the true black-box function, add to observation set, and return to Step 1.

## Key Design Principles

1. **On-demand GP activation**: GP component only runs when BOCS stalls, keeping computational cost low.

2. **Hamming-neighborhood awareness**: The effectiveness comes from selecting points that promote search progress within Hamming-distance neighborhoods, not from simply adding low-energy points near promising solutions.

3. **Near-fully connected representational capacity**: For quantum annealing sparse surrogate applications, retaining near-fully connected capacity in the surrogate model is important. Overly sparse models degrade search quality.

4. **Adaptive β selection**: Dynamically adjusts exploration-exploitation balance based on optimization trajectory, outperforming fixed-β or random-point addition strategies.

## Application to QUBO

For Quadratic Unconstrained Binary Optimization:

```python
# Pseudocode for the hybrid BOCS + GP-LCB method
observations = []  # list of (x, f(x)) pairs

for iteration in range(max_iterations):
    # Step 1: BOCS proposes
    candidate = bocs_propose(observations)
    
    # Step 2: Check for stagnation
    if candidate in [x for x, _ in observations]:
        # Step 3: Activate GP-LCB
        gp = train_gp(observations, kernel='hamming')
        beta = select_beta(recent_progress=observations[-k:])
        candidate = minimize_lcb(gp, beta, exclude=observations)
    
    # Step 4: Evaluate
    fx = evaluate(candidate)
    observations.append((candidate, fx))
```

## Application to HUBO

For Higher-order Unconstrained Binary Optimization, the same framework applies. The BOCS surrogate should include higher-order interaction terms. The GP-LCB component handles higher-order interactions implicitly through the Hamming kernel.

## Quantum Annealing Surrogate Construction

When building sparse surrogate models for quantum annealers:

- Use BOCS to identify important interaction terms
- Apply the adaptive GP-LCB method to explore the configuration space
- Retain near-fully connected representational capacity — over-sparsification degrades performance
- The sparse surrogate can then be embedded on the quantum annealer's topology

## Performance Characteristics

- Outperforms random-point addition on both QUBO and HUBO benchmarks
- Effective with limited evaluation budget (typical for expensive black-box functions)
- GP component computational cost is bounded by on-demand activation
- Scales to moderate dimensions (d ~ 20-50) with Hamming-distance kernels

## Activation Keywords

- adaptive acquisition function selection
- BOCS stagnation fix
- discrete Bayesian optimization
- QUBO optimizer
- HUBO optimizer
- quantum-inspired black-box optimization
- combinatorial Bayesian optimization
- adaptive LCB selection
- Gaussian process combinatorial search
