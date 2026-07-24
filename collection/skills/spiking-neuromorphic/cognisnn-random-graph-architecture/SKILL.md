---
name: cognisnn-random-graph-architecture
description: "CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks"
category: neuroscience
tags: [spiking neural network, random graph architecture, neuron-expandability, pathway-reusability, dynamic-configurability]
arxiv_id: 2512.11743
---

# CogniSNN: Random Graph Architecture for Spiking Neural Networks

## Context
This skill implements the CogniSNN framework introduced in arXiv:2512.11743, which addresses the limitations of traditional spiking neural networks (SNNs) that rigidly follow chain-like hierarchical architectures of traditional ANNs. The paper introduces Random Graph Architecture (RGA) to incorporate three key biological properties: Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability.

## Core Methodology
1. **Random Graph Architecture (RGA)**: Replace rigid hierarchical connections with stochastic interconnections mimicking biological neural networks
2. **Improved Pure Spiking Residual Mechanism**: Address network degradation and dimensional mismatch in deep pathways
3. **Adaptive Pooling Strategy**: Complement the residual mechanism for stable feature extraction
4. **Key Pathway-based Learning without Forgetting (KP-LwF)**: Selectively reuse critical neural pathways while retaining historical knowledge for efficient multi-task transfer
5. **Dynamic Growth Learning (DGL) Algorithm**: Allow neurons and synapses to grow dynamically along the internal temporal dimension

## Implementation Steps
1. **Network Initialization with RGA**:
   - Generate random connectivity patterns using Erdős–Rényi or Watts-Strogatz models
   - Ensure biological plausibility through connection probability tuning
   - Implement both excitatory and inhibitory connections with realistic ratios

2. **Spiking Neuron Model Selection**:
   - Choose appropriate spiking neuron model (LIF, Izhikevich, etc.)
   - Implement membrane potential dynamics and spike generation
   - Configure refractory periods and threshold dynamics

3. **Residual Connection Implementation**:
   - Design identity mapping connections that bypass problematic layers
   - Implement spike-based residual addition operations
   - Add adaptive pooling layers to complement residual connections

4. **KP-LwF Learning Mechanism**:
   - Identify critical pathways for task performance
   - Implement selective pathway reuse during task switching
   - Develop forgetting mitigation strategies for preserved knowledge

5. **Dynamic Growth Algorithm**:
   - Monitor network activity and performance metrics
   - Trigger neuron/synapse addition when performance plateaus
   - Integrate new components through structured growth protocols

6. **Training Procedure**:
   - Implement event-driven simulation for efficiency
   - Apply spike-timing dependent plasticity (STDP) or surrogate gradients
   - Validate on neuromorphic datasets (DVS-Gesture, CIFAR10-DVS) and Tiny-ImageNet

## Configuration Parameters
- Connection probability (p): 0.1-0.3 for sparse connectivity
- Neuron growth rate: Adaptive based on performance metrics
- Pathway reuse threshold: Task-specific similarity measure
- Temporal dimension growth rate: Configurable based on task complexity

## Verification
- Performance comparison with state-of-the-art SNNs on benchmark datasets
- Analysis of pathway reusability across sequential tasks
- Evaluation of dynamic growth impact on network robustness
- Verification of biological plausibility metrics

## Activation Keywords
cognisnn, random graph architecture, spiking neural network, neuron-expandability, pathway-reusability, dynamic-configurability, KP-LwF, DGL

## References
- arXiv:2512.11743: CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks