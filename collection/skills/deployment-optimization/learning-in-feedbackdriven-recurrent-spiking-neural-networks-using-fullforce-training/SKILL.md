# Learning in Feedback-driven Recurrent Spiking Neural Networks using full-FORCE Training

**arXiv ID:** 2205.13585
**Authors:** Ankita Paul, Stefan Wagner, Anup Das
**Published:** 2022-05-26T19:01:19Z
**Abstract:**
Feedback-driven recurrent spiking neural networks (RSNNs) are powerful computational models that can mimic dynamical systems. However, the presence of a feedback loop from the readout to the recurrent layer de-stabilizes the learning mechanism and prevents it from converging. Here, we propose a supervised training procedure for RSNNs, where a second network is introduced only during the training, to provide hint for the target dynamics. The proposed training procedure consists of generating targets for both recurrent and readout layers (i.e., for a full RSNN system). It uses the recursive least square-based First-Order and Reduced Control Error (FORCE) algorithm to fit the activity of each layer to its target. The proposed full-FORCE training procedure reduces the amount of modifications needed to keep the error between the output and target close to zero. These modifications control the feedback loop, which causes the training to converge. We demonstrate the improved performance and noise robustness of the proposed full-FORCE training procedure to model 8 dynamical systems using RSNNs with leaky integrate and fire (LIF) neurons and rate coding. For energy-efficient hardware implementation, an alternative time-to-first-spike (TTFS) coding is implemented for the full- FORCE training procedure. Compared to rate coding, full-FORCE with TTFS coding generates fewer spikes and facilitates faster convergence to the target dynamics.

## Skill Description

This skill is generated from the arXiv paper: Learning in Feedback-driven Recurrent Spiking Neural Networks using full-FORCE Training (2205.13585).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2205.13585](http://arxiv.org/abs/2205.13585v1)
