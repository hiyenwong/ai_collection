---
name: neurotrain-local-learning-snn-benchmarking
description: >
  NeuroTrain: Survey and benchmarking framework for SNN local learning rules.
  Comprehensive taxonomy of SNN training algorithms spanning surrogate-gradient
  backpropagation, local/three-factor learning, biologically inspired plasticity,
  ANN-to-SNN conversion, and non-standard optimization. Includes open-source
  benchmarking framework built on snnTorch for reproducible cross-method comparison.
  Activation: neurotrain, SNN training survey, spiking neural network benchmark,
  local learning rules, SNN taxonomy, snnTorch benchmarking framework,
  eligibility traces, STDP-inspired learning, surrogate gradient SNN
---

# NeuroTrain: Local Learning Rules for SNNs

Paper: arXiv:2605.15058v1 (May 14, 2026)
Authors: Alessio Caviglia, Filippo Marostica, Roberta Bardini, Alessandro Savino, Stefano Di Carlo (Politecnico di Torino)
GitHub: https://github.com/smilies-polito/neurotrain

## Core Problem

SNN training is challenging due to: (1) non-differentiable spike events requiring surrogate gradients, (2) temporal credit assignment across many timesteps, (3) computational/memory costs of BPTT that map poorly to neuromorphic hardware. The field lacks a unified taxonomy and standardized benchmarking framework.

## Taxonomy Architecture

### Primary Axis: Training Strategy
1. **Direct Training** — learn while simulating spiking dynamics (surrogate-gradient BPTT, local/three-factor rules, STDP variants)
2. **ANN-to-SNN Conversion** — train ANN first, then map to SNN
3. **Evolutionary/Population-based** — black-box optimization without gradients

### Secondary Axis: Learning Signal
- **Supervised** — labeled targets
- **Unsupervised** — input structure-driven objectives  
- **Reinforcement Learning** — reward-driven delayed signals

### Locality Dimensions
- **Temporal Locality** — updates depend only on current timestep info (+ bounded state like eligibility traces)
- **Spatial Locality** — updates use only synapse-local variables (pre/post activity + modulatory signal)

### Recurring Mechanisms (cross-cutting)
1. **Eligibility Traces** — `Δw ∝ e · M` (three-factor rule form)
2. **Direct Feedback Alignment (DFA)** — random projection of output error to hidden layers
3. **Direct Random Target Projection (DRTP)** — direct target projection, no output error needed
4. **Auxiliary Local Classifiers** — per-layer loss/readout heads
5. **STDP-Inspired** — spike-timing correlations adapted to supervised/RL objectives
6. **Spatial BP + Online Temporal** — spatial backprop per timestep, temporal credit online

## Key SNN Training Algorithms

### Supervised Direct Training
| Algorithm | Temporal Loc | Spatial Loc | Traces | STDP | DFA/DRTP | Local Clf |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| BPTT | ✗ | ✗ | | | | |
| E-prop | ✓ | ✗ | ✓ | | | |
| DECOLLE | ✓ | ✓ | ✓ | | | ✓ |
| OTTT | ✓ | ✗ | ✓ | | | |
| ESD-RTRL | ✓ | ✓ | ✓ | | | |
| Target Propagation | ✗ | ✗ | | | ✓ | |
| ETLP | ✓ | ✓ | ✓ | | | |
| STDP-like supervised | ✓ | ✓ | | ✓ | | |

### Unsupervised
| Algorithm | Temporal Loc | Spatial Loc | Traces | STDP |
|-----------|:---:|:---:|:---:|:---:|
| STDP variants | ✓ | ✓ | | ✓ |
| Hebbian learning | ✓ | ✓ | | ✓ |
| BCM rule | ✓ | ✓ | | |

## NeuroTrain Framework Architecture

### Repository
- **GitHub**: https://github.com/smilies-polito/neurotrain
- **License**: CC BY 4.0

Three modular components built on snnTorch + PyTorch:

1. **Dataloaders** — standardized interface for neuromorphic/rate-encoded datasets (NeuroBench, Tonic)
2. **Models** — library of benchmark SNNs (FC, Conv, Recurrent, VGG-style, LIF-based)
3. **Trainers** — Python classes implementing specific learning rules with common interface

### Execution Modes
- **Campaign mode** — orthogonal combination of trainers × models × datasets with auto-hyperparameter tuning (Optuna)
- **Custom mode** — predefined single experiment for targeted evaluation

### Reported Metrics
- Test/train accuracy, loss, execution time, time per epoch
- Parameters count, memory footprint, activation sparsity

## Benchmark Results Summary

Representative results across 8 datasets (MNIST, Fashion-MNIST, CIFAR-10, SVHN, N-MNIST, DVS Gesture, DVS CIFAR-10, SHD):

- **Best performers**: BPTT and Target Propagation on simple tasks (MNIST ~98%)
- **Most hardware-friendly**: DECOLLE, E-prop, OSTL (local in time+space)
- **Trade-off**: Local rules sacrifice some accuracy for neuromorphic compatibility
- ~850 GPU hours for comprehensive campaign

## Key Insights

1. Many training rules exhibit limited portability across datasets/architectures
2. Fair benchmarking requires unified hyperparameter optimization, not fixed settings
3. Stronger convergence needed between algorithmic benchmarking and hardware-aware evaluation
4. NeuroTrain designed as living, community-driven resource

## Activation Context

Use this skill when:
- Designing or comparing SNN training algorithms
- Understanding locality trade-offs in spiking network learning
- Building reproducible SNN benchmarks
- Selecting training methods for neuromorphic hardware deployment
- Studying three-factor learning rules, eligibility traces, or STDP variants
