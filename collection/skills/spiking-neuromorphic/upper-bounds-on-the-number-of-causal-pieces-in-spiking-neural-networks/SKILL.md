---
name: upper-bounds-on-the-number-of-causal-pieces-in-spiking-neural-networks
description: 'Upper bounds on the number of causal pieces in spiking neural networks (arXiv: 2610.22484v1). Utility: 0.90. Categories: cs.NE, cs.AI, cs.LG, q-bio.NC, stat.ML'
metadata:
  {
    "arxiv_id": "2610.22484v1",
    "utility": 0.8999999999999999,
    "title": "Upper bounds on the number of causal pieces in spiking neural networks",
    "authors": "Dominik Dold, Dennis Elbrächter, Philipp Petersen",
    "url": "https://arxiv.org/abs/2610.22484v1",
    "categories": "cs.NE, cs.AI, cs.LG, q-bio.NC, stat.ML"
  }
---

# Upper bounds on the number of causal pieces in spiking neural networks

**arXiv ID:** 2610.22484v1
**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen
**URL:** https://arxiv.org/abs/2610.22484v1
**Utility Score:** 0.90
**Categories:** cs.NE, cs.AI, cs.LG, q-bio.NC, stat.ML

## Abstract

The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-spike neural networks. First, we establish a combinatorial bound given by the poly-Bernoulli numbers, which applies to a broad class of spiking neuron models. The bound is of order $e^{2(L-1)N\log N+\mathcal{O}(N)}$, with network depth $L$ and maximum layer width $N$. Second, for a specific set of neuron models, we derive a bound based on hyperplane arrangements. Applying the latter framework, we obtain bounds of order $\mathcal{O}\!\left(N^{(4L-3)(N_0-1)}\right)$ for the non-leaky integrate-and-fire model with exponential synapses and the ReLU-type spike response model, and $\mathcal{O}\!\left(N^{L(N_0-1)}\right)$ for the leaky integrate-and-fire model with Dirac-$δ$ synapses, where $N_0$ is the input dimension. For the non-leaky integrate-and-fire model with Dirac-$δ$ synapses, additional temporal structure allows us to sharpen the general combinatorial bound to one that depends only on $N_0$, independently of the network depth and widths.

## Key Concepts

- This paper addresses important questions in: cs.NE, cs.AI, cs.LG, q-bio.NC, stat.ML
- Published: 2026-10-15

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows and research tracking.

## References

- arXiv: https://arxiv.org/abs/2610.22484v1
