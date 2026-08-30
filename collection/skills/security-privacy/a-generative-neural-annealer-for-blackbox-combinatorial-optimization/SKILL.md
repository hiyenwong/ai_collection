# A Generative Neural Annealer for Black-Box Combinatorial Optimization

**arXiv ID:** 2505.09742
**Authors:** Yuan-Hang Zhang, Massimiliano Di Ventra
**Published:** 2025-05-14T19:05:19Z
**Abstract:**
We propose a generative, end-to-end solver for black-box combinatorial optimization that emphasizes both sample efficiency and solution quality on NP problems. Drawing inspiration from annealing-based algorithms, we treat the black-box objective as an energy function and train a neural network to model the associated Boltzmann distribution. By conditioning on temperature, the network captures a continuum of distributions--from near-uniform at high temperatures to sharply peaked around global optima at low temperatures--thereby learning the structure of the energy landscape and facilitating global optimization. When queries are expensive, the temperature-dependent distributions naturally enable data augmentation and improve sample efficiency. When queries are cheap but the problem remains hard, the model learns implicit variable interactions, effectively "opening" the black box. We validate our approach on challenging combinatorial tasks under both limited and unlimited query budgets, showing competitive performance against state-of-the-art black-box optimizers.

## Skill Description

This skill is generated from the arXiv paper: A Generative Neural Annealer for Black-Box Combinatorial Optimization (2505.09742).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2505.09742](http://arxiv.org/abs/2505.09742v2)
