---
name: data-driven-distributed-control
description: >
  Data-driven distributed controller synthesis using spatial regret optimization.
  For synthesizing optimal distributed controllers directly from frequency-response data
  without requiring a parametric system model. Use when: (1) designing distributed control
  systems from experimental data, (2) comparing spatial regret vs H2/Hinf performance,
  (3) building data-driven controllers with communication structure constraints,
  (4) model-free controller synthesis for networked systems.
---

# Data-Driven Distributed Control via Spatial Regret

## Core Methodology (arXiv:2605.02506)

Synthesize optimal distributed controllers directly from frequency-response data using
**spatial regret** — measures performance gap between a structured distributed controller
and an oracle with enhanced communication topology.

## Key Concepts

### Spatial Regret
- Quantifies the cost of distributed communication constraints
- Compares structured controller performance against an oracle with richer communication
- Relaxes topology assumptions: oracle can use any enhanced structure
- Provides a principled trade-off between communication cost and control performance

### Data-Driven Synthesis
- Uses experimentally obtained frequency-response data (no parametric model needed)
- Preserves stability and desired communication structure
- Iterative solution (not single convex program) due to relaxed oracle assumptions
- Outperforms classical H2/Hinf designs in numerical benchmarks

## Workflow

### Step 1: Collect Frequency-Response Data
Obtain G(jw) from experiments or identification at discrete frequencies.

### Step 2: Define Communication Structure
Specify which subsystems can communicate via structural constraint matrix S
(S[i,j]=1 means subsystem i can access subsystem j measurements).

### Step 3: Solve Spatial Regret Problem (Iterative)
1. Initialize controller K with desired structure
2. Compute oracle K_oracle with relaxed constraints
3. Minimize regret: min_K [J(K) - J(K_oracle)]
4. Iterate until convergence

### Step 4: Validate
- Check stability margins
- Compare H2/Hinf performance metrics
- Verify communication structure preservation

## Comparison: Spatial Regret vs Classical Methods

| Criterion | H2/Hinf | Spatial Regret |
|-----------|---------|----------------|
| Model required | Yes (parametric) | No (frequency data) |
| Communication constraints | Hand-fixed | Explicitly optimized |
| Oracle comparison | None | Built-in |
| Conservatism | High | Reduced |
| Computation | Single program | Iterative |

## Pitfalls
- Iterative solution may not converge for ill-conditioned systems
- Frequency data quality critically affects synthesis result
- Oracle definition must be carefully chosen (too relaxed = trivial regret)

## Reference
arXiv:2605.02506 — Gupta, Martinelli, Ferrari-Trecate, Furieri, Karimi (2026)
