---
name: self-supervised-local-learning-hierarchy
description: "Biologically plausible local self-supervised learning rules that learn hidden hierarchical data structure as efficiently as supervised backprop. Demonstrates that Direct Feedback Alignment (DFA) methods fail on hierarchical tasks due to input-specific masking. Use for biologically plausible learning algorithms, local plasticity rules, self-supervised representation learning."
arxiv_id: "2605.18557"
date: "2026-05-18"
authors: "Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, Wulfram Gerstner"
tags: [local-learning, biologically-plausible, self-supervised, representation-learning, DFA, plasticity, computational-neuroscience]
---

# Self-Supervised Local Learning Rules Learn Hierarchical Structure

## Overview
From EPFL (Gerstner lab). Tests biologically plausible learning algorithms on the **Random Hierarchy Model (RHM)** — a controlled synthetic dataset with known hierarchical structure. Key finding: **local self-supervised learning rules match backprop's data efficiency**, while **DFA methods fail catastrophically** on hierarchical tasks.

## Key Findings

1. **Self-supervised local learning succeeds** — Layerwise contrastive (SimCLR-style) and non-contrastive (BYOL/Barlow Twins-style) loss functions learn RHM tasks as efficiently as full backpropagation
2. **DFA variants fail** — Direct Feedback Alignment and its extensions (DFA, DRL, SSP) cannot learn the hierarchical structure because they lack input-specific masking: the nonlinear derivative in backprop that varies per-sample
3. **Cortical plausibility** — Local layerwise objectives require no error transport, no weight symmetry, and no equilibrium convergence — fully compatible with known synaptic plasticity

## The RHM Benchmark
- Synthetic dataset with tunable hierarchical depth and complexity
- Requires deep enough networks to capture all hidden hierarchies
- Previously shown (Cagnetta et al., 2024) that shallow networks fail even with unlimited data
- Ideal testbed for evaluating whether a learning rule discovers hierarchical structure

## Why DFA Fails
- DFA uses fixed random feedback matrices — same for all inputs
- Backprop's Jacobian (derivative of ReLU etc.) creates input-dependent **masking** 
- This masking is essential for learning when hidden layers have many more units than output classes
- Without it, DFA's credit assignment becomes sample-independent noise on hierarchical tasks

## Why Local Self-Supervised Learning Succeeds
- Each layer optimizes its own representation quality (contrastive: maximize mutual info between augmentations; non-contrastive: decorrelate features)
- No error propagation needed — learning signal is local to each layer
- Data efficiency matches BP: ~10⁴–10⁵ examples for deep hierarchies (vs. ~10⁶ for DFA)

## Activation Keywords
local learning rules, biologically plausible learning, self-supervised representation learning, Random Hierarchy Model, Direct Feedback Alignment failure, local plasticity
