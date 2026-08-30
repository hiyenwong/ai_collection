# Dynamic Reinforcement Learning for Actors

**arXiv ID:** 2502.10200
**Authors:** Katsunari Shibata
**Published:** 2025-02-14T14:50:05Z
**Abstract:**
Dynamic Reinforcement Learning (Dynamic RL), proposed in this paper, directly controls system dynamics, instead of the actor (action-generating neural network) outputs at each moment, bringing about a major qualitative shift in reinforcement learning (RL) from static to dynamic. The actor is initially designed to generate chaotic dynamics through the loop with its environment, enabling the agent to perform flexible and deterministic exploration. Dynamic RL controls global system dynamics using a local index called "sensitivity," which indicates how much the input neighborhood contracts or expands into the corresponding output neighborhood through each neuron's processing. While sensitivity adjustment learning (SAL) prevents excessive convergence of the dynamics, sensitivity-controlled reinforcement learning (SRL) adjusts them -- to converge more to improve reproducibility around better state transitions with positive TD error and to diverge more to enhance exploration around worse transitions with negative TD error. Dynamic RL was applied only to the actor in an Actor-Critic RL architecture while applying it to the critic remains a challenge. It was tested on two dynamic tasks and functioned effectively without external exploration noise or backward computation through time. Moreover, it exhibited excellent adaptability to new environments, although some problems remain. Drawing parallels between 'exploration' and 'thinking,' the author hypothesizes that "exploration grows into thinking through learning" and believes this RL could be a key technique for the emergence of thinking, including inspiration that cannot be reconstructed from massive existing text data. Finally, despite being presumptuous, the author presents the argument that this research should not proceed due to its potentially fatal risks, aiming to encourage discussion.

## Skill Description

This skill is generated from the arXiv paper: Dynamic Reinforcement Learning for Actors (2502.10200).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2502.10200](http://arxiv.org/abs/2502.10200v1)
