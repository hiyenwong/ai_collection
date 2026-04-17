---
name: von-economo-fast-lane-hypothesis
description: Computational model of Von Economo Neurons implementing a biological speed-accuracy tradeoff in spiking cortical circuits. Models VENs as fast LIF neurons with sparse dendritic fan-in enabling rapid social decisions.
version: 1.0.0
arxiv: 2604.09229v1
tags:
  - spiking-neural-networks
  - von-economo-neurons
  - speed-accuracy-tradeoff
  - computational-neuroscience
  - social-cognition
  - leaky-integrate-and-fire
---

# Von Economo Fast Lane Hypothesis

## Overview

This skill implements the **Fast Lane Hypothesis**: Von Economo Neurons (VENs) provide a sparse, fast projection pathway that enables rapid social decisions at the cost of deliberate processing accuracy. VENs are modeled as fast leaky integrate-and-fire (LIF) neurons with distinct biophysical properties compared to standard pyramidal neurons.

## Key Biological Findings

- **VENs are found exclusively** in the anterior cingulate cortex (ACC) and frontal insula of species with complex social cognition (humans, great apes, cetaceans)
- **Selective depletion** in frontotemporal dementia (FTD) and altered development in autism implicate VENs in rapid social decision-making
- **This is the first computational model** that asks what a Von Economo neuron actually computes

## Computational Model

### Neuron Parameters

| Parameter | VENs (Fast Lane) | Pyramidal Neurons |
|-----------|-----------------|-------------------|
| Membrane time constant (τ) | 5 ms | 20 ms |
| Dendritic fan-in (afferents) | 8 | 80 |
| Role | Rapid decision pathway | Deliberate processing |

### Network Architecture

- **Total neurons**: 2,000
- **VEN fraction**:
  - Typical: 2% VENs
  - Autism-like: 0.4% VENs
  - FTD-like: post-training VEN ablation
- **Training paradigm**: Spiking cortical circuit trained on social discrimination task
- **Evaluation**: 10 independent random seeds per condition

### Key Results

1. **Equivalent accuracy**: All configurations achieve ~99.4% asymptotic classification accuracy
2. **Speed modulation**: VENs modulate decision speed rather than representational capacity
3. **First-spike latency**: VENs produce median first-spike latencies 4 ms earlier than pyramidal neurons
4. **Reaction times** (mean ± std):
   - Typical: 20.70 ± 2.02 ms
   - Autism-like: 26.91 ± 9.01 ms (p=0.078 vs typical)
   - FTD-like: significantly slower (t=-23.31, p<0.0001)
5. **Evolutionary correspondence**: Model-optimal VEN fraction corresponds to primate phylogenetic gradient

## Implementation Guide

See `references/implementation.md` for detailed code patterns including:
- Dual LIF neuron model (VEN + Pyramidal)
- Sparse cortical circuit with VEN pathways
- Social discrimination task setup
- Three clinical condition simulations
- Reaction time and latency analysis

## Usage

This skill is applicable when:
- Building biologically plausible models of social cognition
- Investigating speed-accuracy tradeoffs in neural circuits
- Modeling neurological conditions (FTD, autism) with spiking networks
- Studying evolutionary neuroscience through computational models

## References

- **Paper**: "The Fast Lane Hypothesis: Von Economo Neurons Implement a Biological Speed-Accuracy Tradeoff"
- **arXiv**: 2604.09229v1
