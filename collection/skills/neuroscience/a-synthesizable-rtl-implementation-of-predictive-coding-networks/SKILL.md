# A Synthesizable RTL Implementation of Predictive Coding Networks

**arXiv ID:** 2603.18066
**Authors:** Timothy Oh
**Published:** 2026-03-18T03:07:19Z
**Abstract:**
Backpropagation has enabled modern deep learning but is difficult to realize as an online, fully distributed hardware learning system due to global error propagation, phase separation, and heavy reliance on centralized memory. Predictive coding offers an alternative in which inference and learning arise from local prediction-error dynamics between adjacent layers. This paper presents a digital architecture that implements a discrete-time predictive coding update directly in hardware. Each neural core maintains its own activity, prediction error, and synaptic weights, and communicates only with adjacent layers through hardwired connections. Supervised learning and inference are supported via a uniform per-neuron clamping primitive that enforces boundary conditions while leaving the internal update schedule unchanged. The design is a deterministic, synthesizable RTL substrate built around a sequential MAC datapath and a fixed finite-state schedule. Rather than executing a task-specific instruction sequence inside the learning substrate, the system evolves under fixed local update rules, with task structure imposed through connectivity, parameters, and boundary conditions. The contribution of this work is not a new learning rule, but a complete synthesizable digital substrate that executes predictive-coding learning dynamics directly in hardware.

## Skill Description

This skill is generated from the arXiv paper: A Synthesizable RTL Implementation of Predictive Coding Networks (2603.18066).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2603.18066](http://arxiv.org/abs/2603.18066v2)
