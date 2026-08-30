# Replay4NCL: An Efficient Memory Replay-based Methodology for Neuromorphic Continual Learning in Embedded AI Systems

**arXiv ID:** 2503.17061
**Authors:** Mishal Fatima Minhas, Rachmad Vidya Wicaksana Putra, Falah Awwad, Osman Hasan, Muhammad Shafique
**Published:** 2025-03-21T11:33:22Z
**Abstract:**
Neuromorphic Continual Learning (NCL) paradigm leverages Spiking Neural Networks (SNNs) to enable continual learning (CL) capabilities for AI systems to adapt to dynamically changing environments. Currently, the state-of-the-art employ a memory replay-based method to maintain the old knowledge. However, this technique relies on long timesteps and compression-decompression steps, thereby incurring significant latency and energy overheads, which are not suitable for tightly-constrained embedded AI systems (e.g., mobile agents/robotics). To address this, we propose Replay4NCL, a novel efficient memory replay-based methodology for enabling NCL in embedded AI systems. Specifically, Replay4NCL compresses the latent data (old knowledge), then replays them during the NCL training phase with small timesteps, to minimize the processing latency and energy consumption. To compensate the information loss from reduced spikes, we adjust the neuron threshold potential and learning rate settings. Experimental results on the class-incremental scenario with the Spiking Heidelberg Digits (SHD) dataset show that Replay4NCL can preserve old knowledge with Top-1 accuracy of 90.43% compared to 86.22% from the state-of-the-art, while effectively learning new tasks, achieving 4.88x latency speed-up, 20% latent memory saving, and 36.43% energy saving. These results highlight the potential of our Replay4NCL methodology to further advances NCL capabilities for embedded AI systems.

## Skill Description

This skill is generated from the arXiv paper: Replay4NCL: An Efficient Memory Replay-based Methodology for Neuromorphic Continual Learning in Embedded AI Systems (2503.17061).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2503.17061](http://arxiv.org/abs/2503.17061v1)
