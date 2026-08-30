# Gradient-Free Continual Learning in Spiking Neural Networks via Inter-Spike Interval Regularization

**arXiv ID:** 2604.16496
**Authors:** Samrendra Roy, Kazuma Kobayashi, Souvik Chakraborty, Sajedul Talukder, Syed Bahauddin Alam
**Published:** 2026-04-14T03:16:26Z
**Abstract:**
Continual learning, the ability to acquire new tasks sequentially without forgetting prior knowledge, is essential for deploying neural networks in dynamic real-world environments, from nuclear digital twin monitoring to grid-edge fault detection. Existing synaptic importance methods, such as Elastic Weight Consolidation (EWC) and Synaptic Intelligence (SI), rely on gradient computation, making them incompatible with neuromorphic hardware that lacks backpropagation support. We propose ISI-CV, the first gradient-free synaptic importance metric for SNN continual learning, derived from the Coefficient of Variation (CV) of Inter-Spike Intervals (ISIs). Neurons that fire regularly (low CV) encode stable, task-relevant features and are protected from overwriting; neurons with irregular firing are permitted to adapt freely. ISI-CV requires only spike time counters and integer arithmetic, all of which are native to every neuromorphic chip. We evaluate on four benchmarks of increasing difficulty: Split-MNIST, Permuted-MNIST, Split-FashionMNIST, and Split-N-MNIST using real Dynamic Vision Sensor (DVS) event data. Across three seeds, ISI-CV achieves zero forgetting (AF = 0.000 +/- 0.000) on Split-MNIST and Split-FashionMNIST, near-zero forgetting on Permuted-MNIST (AF = 0.001 +/- 0.000), and the highest accuracy with the lowest forgetting on real neuromorphic DVS data (AA = 0.820 +/- 0.012, AF = 0.221 +/- 0.014). On N-MNIST, gradient-based methods produce unreliable importance estimates and perform worse than no regularization; ISI-CV avoids this failure by design.

## Skill Description

This skill is generated from the arXiv paper: Gradient-Free Continual Learning in Spiking Neural Networks via Inter-Spike Interval Regularization (2604.16496).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.16496](http://arxiv.org/abs/2604.16496v1)
