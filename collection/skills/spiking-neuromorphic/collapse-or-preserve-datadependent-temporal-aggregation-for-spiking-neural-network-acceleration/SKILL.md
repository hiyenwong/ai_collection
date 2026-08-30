# Collapse or Preserve: Data-Dependent Temporal Aggregation for Spiking Neural Network Acceleration

**arXiv ID:** 2603.13810
**Authors:** Jiahao Qin
**Published:** 2026-03-14T07:30:22Z
**Abstract:**
Spike sparsity is widely believed to enable efficient spiking neural network (SNN) inference on GPU hardware. We demonstrate this is an illusion: five distinct sparse computation strategies on Apple M3 Max all fail to outperform dense convolution, because SIMD architectures cannot exploit the fine-grained, unstructured sparsity of i.i.d. binary spikes. Instead, we propose Temporal Aggregated Convolution (TAC), which exploits convolution linearity to pre-aggregate $K$ spike frames before a single convolution call, reducing $T$ calls to $T/K$. On rate-coded data, TAC achieves 13.8times speedup with +1.6% accuracy on MNIST and +5.4% on Fashion-MNIST -- a simultaneous improvement in both speed and accuracy. However, on event-based data where the temporal dimension carries genuine motion information, TAC's temporal collapse is harmful. We therefore introduce TAC-TP (Temporal Preservation), which shares each group's convolution output across K independent LIF steps, preserving full temporal resolution for downstream layers. On DVS128-Gesture, TAC-TP achieves 95.1% accuracy (vs. 96.3% baseline) with 50% fewer convolution calls, while standard TAC drops to 91.3%. Our key finding is that the optimal temporal aggregation strategy is data-dependent: collapse the temporal dimension for rate-coded data (noise reduction) but preserve it for event data (information retention). Speedup is hardware-agnostic: TAC achieves 11.0times on NVIDIA V100, confirming the mechanism transfers across GPU architectures. All operators in the mlx-snn library are open source.

## Skill Description

This skill is generated from the arXiv paper: Collapse or Preserve: Data-Dependent Temporal Aggregation for Spiking Neural Network Acceleration (2603.13810).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2603.13810](http://arxiv.org/abs/2603.13810v1)
