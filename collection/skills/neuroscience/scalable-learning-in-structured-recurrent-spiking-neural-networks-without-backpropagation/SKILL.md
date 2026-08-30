# Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation

**arXiv ID:** 2605.00402
**Authors:** Bo Tang, Weiwei Xie
**Published:** 2026-05-01T04:45:21Z
**Abstract:**
Spiking Neural Networks (SNNs) provide a promising framework for energy-efficient and biologically grounded computation; however, scalable learning in deep recurrent architectures with sparse connectivity remains a major challenge. In this work, we propose a structured multi-layer recurrent SNN architecture composed of locally dense recurrent layers augmented with sparse small-world long-range projections to a readout population. The long-range connectivity is largely fixed, preserving routing efficiency and hardware scalability, while synaptic adaptation is performed using strictly local plasticity mechanisms. To enable supervised learning without backpropagation or surrogate gradients, we introduce a biologically motivated learning framework that combines: (i) population-based winner-take-all (WTA) teaching signals at the output layer, (ii) fixed random broadcast alignment feedback pathways, and (iii) low-dimensional modulatory neuron populations that gate synaptic updates through three-factor learning rules with eligibility traces. This design supports deep recurrent computation with sparse global communication and purely local synaptic updates. We analyze the algorithmic properties, computational complexity, and hardware feasibility of the proposed approach, and demonstrate stable learning and competitive performance on benchmark classification tasks. The results highlight the potential of structured recurrence and neuromodulatory learning to enable scalable, hardware-compatible SNN training beyond gradient-based methods.

## Skill Description

This skill is generated from the arXiv paper: Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation (2605.00402).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.00402](http://arxiv.org/abs/2605.00402v1)
