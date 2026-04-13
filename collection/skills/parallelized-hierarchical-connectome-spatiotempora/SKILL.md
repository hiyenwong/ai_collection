---
name: parallelized-hierarchical-connectome-spatiotempora
description: "This work presents the Parallelized Hierarchical Connectome (PHC), a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks.... Activation: connectome, spatiotemporal, SSM, hierarchical, quantized, integer-state"
---

# Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models

## Overview
This work presents the Parallelized Hierarchical Connectome (PHC), a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks. Conventional SSMs achieve high-speed sequence processing through parallel scans, yet are limited to temporal recurrence without lateral or feedback interactions within a single timestep. PHC maps the diagonal SSM core to a shared Neuron Layer and inter-neuronal communication to a shared Synapse Layer, where neurons are partitioned into hierarchical regions governed by the connectome topology. A Multi-Transmission Loop enables intra-slice spatial recurrence, allowing signals to propagate across the hierarchical connectome within each temporal window while preserving O(logT) parallelism. This framework enables integration of neuro-physical priors typically intractable for standard SSMs, including adaptive leaky integrate-and-fire dynamics, Dale's Law, short-term plasticity, and reward-modulated spike-timing-dependent plasticity. The framework is instantiated as PHCSSM, the first model to unify recurrent spiking neural network dynamics with diagonal SSM parallelism while enforcing all five biological constraints and learnable lateral connections within a fully parallelizable training pipeline. Empirical results on physiological benchmarks from the UEA multivariate time-series archive demonstrate that PHCSSM achieves performance competitive with state-of-the-art SSMs while reducing parameter complexity from Theta(D^2 L) for L-layer stacked architectures to Theta(D^2). These findings suggest that biologically grounded inductive biases offer a principled route to parameter-efficient sequence modeling, opening diagonal SSMs to spatiotemporal recurrence and enabling fully parallelizable recurrent spiking neural network training.

## Source Paper
- **Title:** Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models
- **Authors:** Po-Han Chiang
- **arXiv:** 2604.01295v1
- **Categories:** q-bio.NC, cs.LG
- **PDF:** https://arxiv.org/pdf/2604.01295v1

## Core Concepts

### Key Contributions
1. **Hierarchical Connectome Architecture** - Spatiotemporal SSM framework
2. **Parallel Processing** - Efficient computation for large-scale networks
3. **Neural Dynamics Modeling** - Capturing temporal and spatial dependencies

## Practical Applications

### Primary Use Cases
- Large-scale brain network modeling
- Spatiotemporal neural data analysis
- Efficient SSM implementations

## Activation Keywords
- connectome
- spatiotemporal
- SSM
- hierarchical
- quantized
- integer-state
- SNN
- hardware

## Tools Used

- `exec`
- `read`
- `write`


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
