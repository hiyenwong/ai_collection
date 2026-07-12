---
name: scaling-laws-expressive-neurons-recurrent
description: "Information-theoretic framework for optimal parameter allocation between neuron count (N), per-unit complexity (k_e), and connectivity (k_c) in recurrent networks. Introduces Expressive Leaky Memory (ELM) neurons for independent tuning of complexity vs width vs connectivity."
category: neural-architecture
tags:
  - scaling-laws
  - recurrent-neural-networks
  - expressive-neurons
  - ELM-neurons
  - parameter-allocation
  - information-theory
  - neuromorphic
created: "2026-05-14"
source:
  - title: "Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons"
    url: "https://arxiv.org/abs/2605.12049"
    arxiv_id: "2605.12049"
    date: "2026-05-13"
---

# Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons

## Overview

This paper addresses a fundamental architectural question in neural network design: how should one split a fixed parameter budget P between the number of units N, per-unit effective complexity k_e, and per-unit connectivity k_c? It challenges the mainstream ML default of extremely simple units by showing that cortical neurons' complexity may be normatively optimal.

## Key Innovation

The ELM (Expressive Leaky Memory) Network architecture allows independent tuning of three architectural axes while training stably across orders of magnitude in scale, enabling systematic study of scaling tradeoffs.

## Core Methodology

### The Three-Axis Tradeoff

For a fixed parameter budget P:
- **N** (number of units): Network width
- **k_e** (per-unit effective complexity): Neuron expressivity
- **k_c** (per-unit connectivity): Connection density

The optimal allocation emerges as a non-trivial optimum, not at the extremes.

### Information-Theoretic Model

The diminishing returns at the extremes are explained by:
1. **Per-neuron SNR saturation**: Individual neurons hit capacity limits
2. **Across-neuron redundancy**: Highly connected neurons develop correlated representations

### Scaling Law

Under a fixed budget P, performance follows a Pareto-frontier scaling law that captures the tradeoff surface.

## ELM Network Architecture

### ELM Neuron Design

Expressive Leaky Memory neurons mirror functional components of cortical neurons:
- **Memory component**: Tracks temporal dependencies
- **Expressive component**: Non-linear transformation capacity
- **Leak mechanism**: Forgetting/decay for stability

### ELM Layer

Recurrent layer built from ELM neurons with tunable:
- Per-neuron complexity (k_e)
- Connectivity pattern (k_c)
- Layer width (N)

### ELM Network

Stacked ELM layers with stable training across scales:
- Orders of magnitude in trainable parameters
- Two qualitatively different sequence benchmarks
- Monotonic improvement along each axis individually

## Experimental Results

### Benchmarks

1. **SHD-Adding Task**: Neuromorphic sequence task requiring temporal integration
2. **Enwik8 Character-Level LM**: Large-scale language modeling

### Key Findings

- Performance improves monotonically along each axis individually
- Under fixed budget: clear non-trivial optimum in tradeoff
- Larger budgets favor: more neurons AND more complex neurons
- Hyperparameter sweep (3 orders of magnitude) traces near-Pareto-frontier
- Results consistent with information-theoretic model

## Implications

1. **ML Design**: Simple-unit default may not be optimal
2. **Neuroscience**: Normative lens on cortex's reliance on complex integrators
3. **Architecture Search**: Framework for optimal resource allocation
4. **Scaling Laws**: Information-theoretic understanding of neural scaling

## Implementation

### Scaling Experiment Design

```python
def scaling_experiment(budget_P):
    """Find optimal N, k_e, k_c allocation for budget P."""
    results = []
    for N in logspace(10, 1000, 20):
        for k_e in range(1, 100):
            for k_c in range(1, 100):
                if N * (k_e + k_c) <= P:
                    model = ELMNetwork(N=N, k_e=k_e, k_c=k_c)
                    performance = train_and_evaluate(model)
                    results.append((N, k_e, k_c, performance))
    return find_pareto_frontier(results)
```

### Information-Theoretic Model

```python
def information_capacity(N, k_e, k_c, noise_level):
    """Predict performance from information-theoretic model."""
    # Per-neuron SNR saturation
    single_neuron_cap = log2(1 + k_e / noise_level)
    
    # Across-neuron redundancy (function of connectivity)
    redundancy = k_c * log2(N) / N
    
    # Total capacity
    total = N * single_neuron_cap * (1 - redundancy / N)
    return total
```

## Applications

1. **Architecture Design**: Optimal resource allocation for specific tasks
2. **Neuromorphic Hardware**: Design constraints for efficient neural chips
3. **Transfer Learning**: Understanding scaling across domains
4. **Neuroscience**: Explaining cortical architecture choices

## Pitfalls

1. **Task Dependence**: Optimal allocation varies by task type
2. **Training Stability**: Very large k_e may cause gradient issues
3. **Connectivity Sparsity**: k_c must balance expressivity vs computational cost
4. **Budget Definition**: P must include all trainable parameters

## References

- **Primary**: "Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons" (arXiv:2605.12049)
- **Related**: Expressive Leaky Memory neurons, neural scaling laws, information-theoretic capacity

## Activation

- scaling laws neural networks
- expressive neurons
- recurrent network tradeoffs
- ELM neurons
- parameter allocation
- neural architecture optimization
- information-theoretic capacity
