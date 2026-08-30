# SpikeRL: A Scalable and Energy-efficient Framework for Deep Spiking Reinforcement Learning

**arXiv ID:** 2502.17496
**Authors:** Tokey Tahmid, Mark Gates, Piotr Luszczek, Catherine D. Schuman
**Published:** 2025-02-21T05:28:42Z
**Abstract:**
In this era of AI revolution, massive investments in large-scale data-driven AI systems demand high-performance computing, consuming tremendous energy and resources. This trend raises new challenges in optimizing sustainability without sacrificing scalability or performance. Among the energy-efficient alternatives of the traditional Von Neumann architecture, neuromorphic computing and its Spiking Neural Networks (SNNs) are a promising choice due to their inherent energy efficiency. However, in some real-world application scenarios such as complex continuous control tasks, SNNs often lack the performance optimizations that traditional artificial neural networks have. Researchers have addressed this by combining SNNs with Deep Reinforcement Learning (DeepRL), yet scalability remains unexplored. In this paper, we extend our previous work on SpikeRL, which is a scalable and energy efficient framework for DeepRL-based SNNs for continuous control. In our initial implementation of SpikeRL framework, we depended on the population encoding from the Population-coded Spiking Actor Network (PopSAN) method for our SNN model and implemented distributed training with Message Passing Interface (MPI) through mpi4py. Also, further optimizing our model training by using mixed-precision for parameter updates. In our new SpikeRL framework, we have implemented our own DeepRL-SNN component with population encoding, and distributed training with PyTorch Distributed package with NCCL backend while still optimizing with mixed precision training. Our new SpikeRL implementation is 4.26X faster and 2.25X more energy efficient than state-of-the-art DeepRL-SNN methods. Our proposed SpikeRL framework demonstrates a truly scalable and sustainable solution for complex continuous control tasks in real-world applications.

## Skill Description

This skill is generated from the arXiv paper: SpikeRL: A Scalable and Energy-efficient Framework for Deep Spiking Reinforcement Learning (2502.17496).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2502.17496](http://arxiv.org/abs/2502.17496v1)
