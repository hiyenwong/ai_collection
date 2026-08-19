---
name: order-sensitive-fast-synapse-limits
description: Analyze E/I arrival order effects in threshold-reset SNNs.
arxiv_id: 2608.16701v1
authors:
  - Tonic Song
date: 2026-08-17
categories:
  - q-bio.NC
  - math.PR
---

# Order-Sensitive Fast-Synapse Limits in Sparse Excitatory-Inhibitory Threshold-Reset Networks

## Overview
This methodology addresses a fundamental limitation in sparse threshold-reset spiking neural networks: componentwise weak convergence of signed synaptic kernels does not, by itself, determine the fast-synapse limit. The key insight is that the microscopic arrival order of excitatory vs inhibitory inputs critically affects network behavior, even when both converge weakly to the same delta function.

## Core Contributions

### 1. Order-Sensitive Response Mechanism
- Constructs two families of networks where excitatory and inhibitory measures converge weakly to δ₀ but with reversed microscopic arrival orders
- Demonstrates that a target neuron fires in the excitatory-first family but not in the inhibitory-first family precisely when x+a-b < θ ≤ x+a
- Shows that strict margins preserve this response under perturbations of target state, aggregate E/I pulse masses, and bounded drift

### 2. Macroscopic Effect Persistence
- Proves the macroscopic effect persists on moderately sparse Dale-compatible random block graphs with q_N→∞ and q_N/N→0
- Shows that along every deterministic joint scale ε_N↓0, population-averaged firing counts differ by 1/2+o_{L^1}(1)
- Provides a bounded-degree construction showing the discrepancy is macroscopic and can persist through reset

### 3. Stable Regime Conditions
- Establishes that fixed positive-delay kernels with finitely many classes admit a stable regime
- Shows that before grazing, typewise-mixing sparse networks converge to a delayed class mean-field system
- For directed Erdos-Renyi graphs, yields the bound O_P(λ_N^{-1/2}+‖π_N-π‖_1) when λ_N→∞ and λ_N/N→0

## Key Insights

### Separation of Stable Averaging vs Singular Collapse
The methodology separates two distinct regimes:
1. **Stable averaging at fixed delay**: Networks converge to delayed class mean-field systems
2. **Singular collapse**: Componentwise weak convergence discards signed arrival-order information needed by threshold-reset response

### Practical Implications
- Traditional approaches that only consider weak convergence of synaptic measures may miss critical order-dependent effects
- The arrival order of E/I inputs must be explicitly modeled in sparse threshold-reset networks
- This has implications for understanding neural computation where precise timing matters

## Usage Guidelines

### When to Apply
Use this methodology when:
- Analyzing sparse spiking neural networks with threshold-reset dynamics
- Studying fast-synapse limits in excitatory-inhibitory networks
- Investigating order-dependent effects in neural population coding
- Modeling neural systems where precise spike timing affects network behavior

### Implementation Considerations
- Account for microscopic arrival order in synaptic kernel modeling
- Consider both stable averaging and singular collapse regimes
- Use the provided bounds for Erdos-Renyi graph analysis
- Validate against the strict margin conditions for robustness

## Mathematical Framework

The core mathematical framework involves:
- Causal event protocol with clamped refractoriness and smooth positive-delay kernels
- Weak convergence analysis of signed synaptic kernels
- Population-averaged firing count analysis
- Delayed class mean-field system convergence

## References
- arXiv:2608.16701v1 "Order-Sensitive Fast-Synapse Limits in Sparse Excitatory-Inhibitory Threshold-Reset Networks"
- DOI: 10.5281/zenodo.21915232