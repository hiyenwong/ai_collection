---
name: neurotrain-local-learning-snn-benchmarking
description: >
  Comprehensive survey and open benchmarking framework for local learning rules
  in Spiking Neural Networks (SNNs). Covers surrogate-gradient backpropagation,
  local/three-factor learning, biologically inspired plasticity, ANN-to-SNN conversion,
  and non-standard optimization strategies. Released as NeuroTrain (snnTorch-based).
  Activation: neurotrain, local learning SNN, SNN benchmarking, snn training survey,
  surrogate gradient, three-factor learning, ANN-to-SNN conversion, SNN taxonomy.
categories: ["neuroscience", "snn", "machine-learning"]
arxiv_id: "2605.15058"
authors: ["Alessio Caviglia", "Filippo Marostica", "Roberta Bardini", "Alessandro Savino", "Stefano Di Carlo"]
published: "2026-05-14"
url: "https://arxiv.org/abs/2605.15058"
---

# NeuroTrain: Local Learning Rules for SNNs - Survey & Benchmarking Framework

## Paper Metadata

- **Title:** NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework
- **Authors:** Alessio Caviglia, Filippo Marostica, Roberta Bardini, Alessandro Savino, Stefano Di Carlo
- **arXiv:** [2605.15058](https://arxiv.org/abs/2605.15058) [cs.NE, cs.AI]
- **Date:** 2026-05-14

## Core Problem

The rapid expansion of Spiking Neural Networks (SNNs) has led to a proliferation of training algorithms that differ widely in biological inspiration, computational structure, and hardware suitability. Despite this progress, the field lacks a unified, fine-grained taxonomy that systematically organizes these approaches and clarifies their conceptual relationships.

## Key Contributions

### 1. Comprehensive Taxonomy of SNN Training Algorithms

The survey provides a unified taxonomy spanning five major categories:

#### Category A: Surrogate-Gradient Backpropagation
- Replaces non-differentiable spike function with smooth surrogate gradient
- Enables gradient-based learning through temporal dynamics
- Common surrogates: sigmoid, fast sigmoid, triangular, multi-gaussian
- **Trade-off:** Good performance but biologically implausible (requires global error signals)

#### Category B: Local and Three-Factor Learning Rules
- **Two-factor rules:** Hebbian-like, pre-post spike correlation (STDP variants)
- **Three-factor rules:** Add neuromodulatory signal (reward, attention, dopamine)
  - Pre-synaptic activity × Post-synaptic activity × Modulatory signal
- Fully local: each synapse updates based on locally available information
- **Trade-off:** Biologically plausible but limited expressivity for complex tasks

#### Category C: Biologically Inspired Plasticity Mechanisms
- Homeostatic plasticity (synaptic scaling)
- Short-term plasticity (facilitation/depression)
- Structural plasticity (connection creation/removal)
- Metaplasticity (plasticity of plasticity)
- **Trade-off:** Realistic dynamics but computationally expensive

#### Category D: ANN-to-SNN Conversion Pipelines
- Train conventional ANN, then convert to SNN
- Rate coding: neuron firing rate ≈ ANN activation
- Methods: weight scaling, threshold balancing, calibration
- **Trade-off:** Leverages mature ANN training, but conversion loss and latency issues

#### Category E: Non-Standard Optimization Strategies
- Evolutionary algorithms for SNN parameters
- Reinforcement learning with spiking policies
- Direct spike-timing optimization
- **Trade-off:** Flexible but sample-inefficient

### 2. NeuroTrain Framework

- **Built on:** snnTorch (PyTorch-based SNN library)
- **Design:** Modular, extendable, unified benchmarking framework
- **Purpose:** Consistent benchmarking across datasets, architectures, and training regimes
- **Features:**
  - Representative implementations of each algorithm class
  - Unified evaluation pipeline
  - Reproducible experimental setup

### 3. Analysis Dimensions

Each algorithm class analyzed across:
- **Computational principles:** How learning signals are computed
- **Learning signals:** What information drives synaptic updates
- **Locality properties:** What information is available at each synapse
- **Hardware suitability:** Compatibility with neuromorphic hardware
- **Biological plausibility:** Alignment with known neurobiology

## Open Challenges Identified

1. **Scalability:** Many local learning rules struggle with complex tasks
2. **Standardization:** No consensus on evaluation protocols
3. **Hardware-software co-design:** Gap between algorithm design and neuromorphic deployment
4. **Theoretical foundations:** Limited understanding of convergence guarantees
5. **Cross-domain transfer:** Difficulty generalizing across task domains

## Key Takeaways for Practitioners

- **For maximum biological fidelity:** Three-factor learning rules with homeostatic mechanisms
- **For best performance:** Surrogate-gradient methods (but lose biological plausibility)
- **For rapid prototyping:** ANN-to-SNN conversion (leverage existing models)
- **For neuromorphic deployment:** Local learning rules with event-based computation
- **For research reproducibility:** Use NeuroTrain framework as common baseline

## Related Skills

- `snn-learning-survey`: Comprehensive SNN learning paradigm overview
- `spikingjelly-framework`: SNN deep learning framework
- `multi-plasticity-snn-training`: Multi-plasticity协同 training methodology
- `surrogate-gradient-snn-training`: Surrogate gradient learning details

## Activation Keywords

neurotrain, local learning SNN, SNN benchmarking, snn training survey, surrogate gradient, three-factor learning, ANN-to-SNN conversion, SNN taxonomy, snntorch, biological plasticity SNN, neuromorphic training
