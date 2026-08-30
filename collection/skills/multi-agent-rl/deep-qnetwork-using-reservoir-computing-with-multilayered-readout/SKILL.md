# Deep Q-network using reservoir computing with multi-layered readout

**arXiv ID:** 2203.01465
**Authors:** Toshitaka Matsuki
**Published:** 2022-03-03T00:32:55Z
**Abstract:**
Recurrent neural network (RNN) based reinforcement learning (RL) is used for learning context-dependent tasks and has also attracted attention as a method with remarkable learning performance in recent research. However, RNN-based RL has some issues that the learning procedures tend to be more computationally expensive, and training with backpropagation through time (BPTT) is unstable because of vanishing/exploding gradients problem. An approach with replay memory introducing reservoir computing has been proposed, which trains an agent without BPTT and avoids these issues. The basic idea of this approach is that observations from the environment are input to the reservoir network, and both the observation and the reservoir output are stored in the memory. This paper shows that the performance of this method improves by using a multi-layered neural network for the readout layer, which regularly consists of a single linear layer. The experimental results show that using multi-layered readout improves the learning performance of four classical control tasks that require time-series processing.

## Skill Description

This skill is generated from the arXiv paper: Deep Q-network using reservoir computing with multi-layered readout (2203.01465).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2203.01465](http://arxiv.org/abs/2203.01465v1)
