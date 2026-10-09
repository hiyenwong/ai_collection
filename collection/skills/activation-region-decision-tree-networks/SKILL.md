---
name: activation-region-decision-tree-networks
description: Use when analyzing piecewise-linear (ReLU) networks, activation regions, or neural selectivity geometry.
category: ai_collection
---

# Activation-Region Decision-Tree Framework for Piecewise-Linear Networks

**Source**: Tissot, Ranft & Boubenec (ENS Paris), "Neural networks as decision trees: an analytical solution for learning and neural selectivity", arXiv:2610.08228 (Oct 2026, q-bio.NC).

## Core Idea

At any stationary point of gradient-aligned learning, a piecewise-linear (ReLU) network — feedforward or recurrent — **decomposes into local affine regressions over its activation regions**. In the low-error regime each regional affine map converges to its own least-squares solution, so the trained network is (approximately) a **piecewise least-squares decomposition of the task**. This admits a decision-tree interpretation:

```
Computation = hierarchical routing of input to activation region (tree paths)
            + region-specific affine transformation (leaf = local least-squares)
```

## Key Results

1. **Stationarity ⇒ regional affine form**: network output in region R is affine, f(x) = A_R·x + b_R. Gradient stationarity forces the regional deviation D_R (distance from the region's independent least-squares solution) to be jointly constrained by weights shared across regions — deviations cancel collectively, and vanish as regional error → 0.
2. **MAP trees (Main Activation Pattern trees)**: fit decision trees to predict the dominant binary activation pattern from the input. This numerically recovers the latent routing structure — an interpretable approximation of the network's partition of input space. For empirical neural data (no ReLU threshold), activity states are defined relative to each neuron's mean firing rate.
3. **Selectivity geometry from activation regions**: the neural encoding Gram matrix S = (XᵀX)⁻¹XᵀY decomposes into **pairwise region-block interactions** — diagonal blocks = within-region activity statistics, off-diagonal = alignment between regions. Low-error regime: each block approaches the target Gram of its region ⇒ neural selectivity organizes into subpopulations tied to activation regions.
4. **Neural baseline as resolution knob**: bias/baseline controls activation-pattern diversity — low baseline → few, coarse regions (generalizing representations); high baseline → many fine-grained regions (expressive but poorer finite-sample generalization). A continuous coarse↔fine trade-off, empirically validated.
5. **Empirical validation**: predictions match selectivity geometry in simulated networks AND two empirical datasets (Reinert et al. sensory cortex; Hajnal et al. recordings).

## How to Use (Procedure)

**A. Interpret a trained ReLU network:**
1. Collect inputs; for each, record binary activation pattern (active iff pre-activation > 0) at target layer(s).
2. Take the dominant pattern per input (or per stimulus class); fit a decision tree (e.g., CART) input → pattern. The tree IS the recovered routing.
3. Within each region, fit the affine map independently and compare with the network's actual A_R, b_R — deviation should shrink with training error.
4. Validate: leaf-wise local least-squares retraining should approximately reproduce network outputs region-wise.

**B. Predict neural selectivity structure:**
1. Define neuron activity states relative to mean firing (empirical data).
2. Compute region-block decomposition of the activity Gram matrix.
3. Predict subpopulation structure: neurons sharing activation regions share selectivity statistics.

**C. Tune representation resolution:**
- Adjust bias/baseline parameters to trade off region count (expressivity) vs generalization; use activation-pattern diversity as the diagnostic metric.

## When to Apply

- Interpreting what a piecewise-linear network computes, region by region (alternative to global mechanistic interpretability)
- Predicting stimulus selectivity of recorded neurons from task structure
- Analyzing recurrent networks at equilibrium (fixed-point activation regions)
- Choosing bias initialization when generalization vs expressivity matters
- Related but distinct from: spline/affine-partition linearization (local analysis only), decision-tree distillation (post-hoc approximation) — here the tree structure is the *stationary-point property of learning itself*

## Limitations

- Region distribution across input space has no closed form — MAP trees are a numerical approximation.
- Low-error/large-sample regime required for exact least-squares convergence claims.
- Empirical neural "activation" requires thresholding convention (mean firing rate).
- Exact for piecewise-linear activations; extensions to smooth nonlinearities are approximate.
