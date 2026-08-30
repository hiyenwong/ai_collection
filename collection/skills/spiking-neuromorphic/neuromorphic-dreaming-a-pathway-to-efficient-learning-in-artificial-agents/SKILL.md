# Neuromorphic dreaming: A pathway to efficient learning in artificial agents

**arXiv ID:** 2405.15616
**Authors:** Ingo Blakowski, Dmitrii Zendrikov, Cristiano Capone, Giacomo Indiveri
**Published:** 2024-05-24T15:03:56Z
**Abstract:**
Achieving energy efficiency in learning is a key challenge for artificial intelligence (AI) computing platforms. Biological systems demonstrate remarkable abilities to learn complex skills quickly and efficiently. Inspired by this, we present a hardware implementation of model-based reinforcement learning (MBRL) using spiking neural networks (SNNs) on mixed-signal analog/digital neuromorphic hardware. This approach leverages the energy efficiency of mixed-signal neuromorphic chips while achieving high sample efficiency through an alternation of online learning, referred to as the "awake" phase, and offline learning, known as the "dreaming" phase. The model proposed includes two symbiotic networks: an agent network that learns by combining real and simulated experiences, and a learned world model network that generates the simulated experiences. We validate the model by training the hardware implementation to play the Atari game Pong. We start from a baseline consisting of an agent network learning without a world model and dreaming, which successfully learns to play the game. By incorporating dreaming, the number of required real game experiences are reduced significantly compared to the baseline. The networks are implemented using a mixed-signal neuromorphic processor, with the readout layers trained using a computer in-the-loop, while the other layers remain fixed. These results pave the way toward energy-efficient neuromorphic learning systems capable of rapid learning in real world applications and use-cases.

## Skill Description

This skill is generated from the arXiv paper: Neuromorphic dreaming: A pathway to efficient learning in artificial agents (2405.15616).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2405.15616](http://arxiv.org/abs/2405.15616v1)
