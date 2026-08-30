# MXNorm: Reusing MXFP block scales for efficient tensor normalisation

**arXiv ID:** 2603.13180
**Authors:** Callum McLean, Luke Y. Prince, Alexandre Payot, Paul Balança, Carlo Luschi
**Published:** 2026-03-13T17:14:06Z
**Abstract:**
Matrix multiplication performance has long been the major bottleneck to scaling deep learning workloads, which has stimulated the design of new accelerators that use increasingly low-precision number formats. However, improvements in matrix multiplication performance have far outstripped improvements in performance on reductions and elementwise computations, which are still being performed in higher precision. In this work, we propose MXNorm, a drop-in replacement for RMSNorm that estimates the RMS using only the block scales calculated as part of the MXFP8 cast and enables a 32x decrease in the size of reduction needed for normalization. We validate our approximation method on pre-training of Llama 3 models of 125M, 1B and 8B parameters, finding minimal loss of training accuracy compared to a baseline using RMSNorm with MXFP8 matmuls. We also show practical kernel speedups using only torch.compile of up to 2.4x for MXNorm over RMSNorm, corresponding to a 1.3% speedup in Llama 3 8B transformer layers in MXFP8 and a 2.6% speedup in NVFP4.

## Skill Description

This skill is generated from the arXiv paper: MXNorm: Reusing MXFP block scales for efficient tensor normalisation (2603.13180).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2603.13180](http://arxiv.org/abs/2603.13180v1)
