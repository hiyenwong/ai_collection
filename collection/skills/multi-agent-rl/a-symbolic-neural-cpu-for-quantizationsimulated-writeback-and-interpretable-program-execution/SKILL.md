# A Symbolic Neural CPU for Quantization-Simulated Writeback and Interpretable Program Execution

**arXiv ID:** 2607.10021
**Authors:** Jose Luis Lima de Jesus Silva
**Published:** 2026-07-10T22:55:23Z
**Abstract:**
Neural networks can learn algorithmic input-output mappings, but trusting a learned executor requires more than a correct final answer because the state transitions that produce it are usually hidden. To make those transitions visible, we introduce a trace-supervised symbolic neural CPU, a factorized learned execution architecture that combines recurrent control, an explicit operation router over a fixed differentiable arithmetic-logic unit bank, destination-masked register writeback, complete trajectory supervision and matched fixed-point replay. The model exposes the selected operation, source and destination registers, register trajectory, memory signals and writeback semantics at every step. On the principal 16-wide benchmark, the non-quantized executor reproduces reference execution exactly, while the eight-bit quantization-simulated executor preserves the symbolic operation path through programs of 1,000 instructions. When the same execution is evaluated against a matched fixed-point replay, the residual numerical drift disappears, showing that it comes from a mismatch between continuous and low-precision reference semantics rather than from execution failure. We compare recurrent, Transformer, temporal-convolution, temporal graph-inspired and state-space controllers, and the ablations show that operation-gate supervision is necessary for an inspectable execution path. Hidden-opcode memory-pressure tasks expose the remaining limits in delayed state use and temporal binding. We also extend the interface with ValueMemory, hybrid adaptive leaky integrate-and-fire controllers, candidate-constrained symbolic control trained through behaviour cloning and actor-critic reinforcement learning, and an RV32I base-integer semantic bridge. Together, these results establish a trace-verifiable framework for interpretable, low-precision and controllable neural execution.

## Skill Description

This skill is generated from the arXiv paper: A Symbolic Neural CPU for Quantization-Simulated Writeback and Interpretable Program Execution (2607.10021).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2607.10021](http://arxiv.org/abs/2607.10021v1)
