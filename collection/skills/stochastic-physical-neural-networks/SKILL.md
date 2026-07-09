---
name: stochastic-physical-neural-networks
description: >
  Stochastic Physical Neural Networks (PNNs) methodology using single-electron
  and single-photon stochastic neurons. Training via empirical backward pass with
  few trials achieves >97% MNIST accuracy. Use when: physical neural networks,
  stochastic neurons, single-electron tunneling, quantum dot neurons, single-photon
  neurons, PNN training strategies, MNIST classification, noise-resilient deep
  learning, arXiv:2604.10861, stochastic physical computing, quantum neurons.
---

# Stochastic Physical Neural Networks

Train physical neural networks where neurons are realized by stochastic
activation switches — single-electron tunneling or single-photon processes.

## Electronic Stochastic Neuron

- **Implementation**: Single-electron tunneling through a quantum dot
- **Basis**: Charge state of the quantum dot
- **Stochasticity**: Inherent tunneling statistics

## Photonic Stochastic Neuron

- **Implementation**: Single-photon source driving one of two modes via
  controllable beam-splitter interaction
- **Basis**: Occupation of the undriven mode
- **Stochasticity**: Photon detection statistics

## Training Strategies

| Strategy | Forward Pass | Backward Pass | Key Finding |
|----------|-------------|---------------|-------------|
| True probability | Expected values | True gradients | Lower accuracy |
| **Empirical outputs** | Sampled values | **Empirical gradients** | **>97% MNIST accuracy** |

### Key Insight

Using **empirical outputs in the backward pass** (not true probabilities) achieves
significantly higher accuracy with fewer trials per layer.

### Noise Robustness

- Maintains >97% test accuracy under high noise and model uncertainty
- Works with single-hidden-layer architecture
- Simplicity enables practical implementation

## Training Protocol

1. Build single-hidden-layer stochastic PNN with electronic or photonic neurons
2. Vary number of trials per layer to control forward-pass stochasticity
3. Use empirical outputs (sampled values) for gradient estimation in backward pass
4. Train on target task — monitor convergence under noise conditions

## Architectural Simplicity

Unlike DNNs requiring backpropagation through time, stochastic PNNs:
- No BPTT needed
- Only simple readout training
- Natural noise resilience
- Compatible with quantum hardware constraints

## Activation Keywords

stochastic PNN, physical neural network, single-electron neuron, single-photon
neuron, quantum dot neuron, stochastic neuron training, empirical backward pass,
MNIST stochastic, Dou Kumara Burns
