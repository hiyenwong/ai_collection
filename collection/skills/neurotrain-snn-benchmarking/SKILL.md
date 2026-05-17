---
name: neurotrain-snn-benchmarking
description: >
  Comprehensive SNN training algorithm taxonomy and open benchmarking framework methodology from arXiv:2605.15058 (NeuroTrain, 2026-05-14).
  Covers surrogate-gradient backpropagation, local/three-factor learning rules, biologically inspired plasticity, ANN-to-SNN conversion, and non-standard optimization.
  Use when: researching SNN training methods, comparing learning rules, designing neuromorphic training pipelines,
  or benchmarking spiking neural network algorithms. Activation: SNN training, spiking neural network learning,
  neurotrain, surrogate gradient, local learning rules, three-factor learning, ANN-to-SNN conversion,
  snnTorch benchmarking, neuromorphic training.
---

# NeuroTrain: SNN Training Algorithm Taxonomy & Benchmarking Framework

**arXiv:** 2605.15058 | **Date:** 2026-05-14 | **Authors:** Caviglia, Marostica, Bardini, Savino, Di Carlo

## Core Contribution

First unified, fine-grained taxonomy of SNN training algorithms spanning the full landscape of approaches.
Releases **NeuroTrain** — an open-source snnTorch-based framework for consistent benchmarking across
datasets, architectures, and training regimes.

## Taxonomy of SNN Training Algorithms

### 1. Surrogate-Gradient Backpropagation (BP)
- **Principle:** Replace non-differentiable spike function with smooth surrogate during backward pass
- **Learning Signal:** Global error gradient via chain rule
- **Locality:** Non-local (requires backprop through time)
- **Representative methods:** SuperSpike, STDP-BP, slayer
- **Strengths:** High accuracy on complex tasks
- **Weaknesses:** Biologically implausible, memory-intensive BPTT

### 2. Local Learning Rules
- **Principle:** Weight updates depend only on pre/post-synaptic activity
- **Learning Signal:** Local activity correlation
- **Locality:** Fully local (synapse-level)
- **Representative methods:** STDP, Hebbian learning, eligibility traces
- **Strengths:** Hardware-friendly, biologically plausible
- **Weaknesses:** Limited to simpler tasks, slower convergence

### 3. Three-Factor Learning Rules
- **Principle:** Local pre/post activity modulated by global third factor (reward, error, neuromodulator)
- **Learning Signal:** Local activity × global modulatory signal
- **Locality:** Semi-local (requires broadcast signal)
- **Representative methods:** Reward-modulated STDP, e-prop
- **Strengths:** Balance of biological plausibility and learning power
- **Weaknesses:** Third factor computation can be complex

### 4. Biologically Inspired Plasticity
- **Principle:** Mechanisms mimicking biological synaptic plasticity
- **Learning Signal:** Intrinsic biological signals (calcium, dopamine)
- **Locality:** Local to semi-local
- **Representative methods:** Calcium-based plasticity, homeostatic scaling
- **Strengths:** High biological fidelity, self-regulating
- **Weaknesses:** Task-specific tuning difficult

### 5. ANN-to-SNN Conversion
- **Principle:** Train ANN first, then convert to equivalent SNN
- **Learning Signal:** Standard ANN backprop
- **Locality:** N/A (conversion step is deterministic)
- **Representative methods:** Rate coding conversion, spike-based calibration
- **Strengths:** Leverages mature ANN training, high accuracy
- **Weaknesses:** Requires long simulation timesteps, latency overhead

### 6. Non-Standard Optimization
- **Principle:** Methods outside gradient-based frameworks
- **Learning Signal:** Various (evolutionary, direct search, etc.)
- **Locality:** Varies
- **Representative methods:** Evolutionary algorithms, direct policy search
- **Strengths:** No gradient computation needed
- **Weaknesses:** Sample inefficient, limited scalability

## NeuroTrain Framework

- **Built on:** snnTorch
- **Design:** Modular, extendable architecture
- **Capabilities:**
  - Implements representative algorithms from each taxonomy class
  - Unified API for consistent benchmarking
  - Supports multiple datasets, architectures, training regimes
  - Reproducible research framework

## Key Insights

1. **Fragmentation problem:** SNN training literature is highly fragmented — NeuroTrain consolidates it
2. **Trade-off triangle:** Biological plausibility ↔ computational efficiency ↔ task performance
3. **No single winner:** Each class has distinct advantages for different use cases
4. **Hardware considerations:** Local rules are most suitable for neuromorphic chips
5. **Future direction:** Hybrid approaches combining local learning with global supervision

## Pitfalls

- Surrogate gradient choice critically impacts training stability (not just approximation quality)
- Local learning rules may require careful temporal credit assignment design
- ANN-to-SNN conversion accuracy depends heavily on simulation timestep count
- Three-factor rules need careful design of the modulatory signal pathway

## Verification

- Compare trained SNN against baseline on standard benchmarks (MNIST, CIFAR-10, N-MNIST)
- Verify spike sparsity meets energy efficiency targets
- Check that local rules maintain weight stability over long training periods
