# High Performance Im2win and Direct Convolutions using Three Tensor Layouts on SIMD Architectures

**arXiv ID:** 2408.00278
**Authors:** Xiang Fu, Xinpeng Zhang, Jixiang Ma, Peng Zhao, Shuai Lu, Xu T. Liu
**Published:** 2024-08-01T04:37:03Z
**Abstract:**
Convolution is the core component within deep neural networks and it is computationally intensive and time consuming. Tensor data layouts significantly impact convolution operations in terms of memory access and computational efficiency. Yet, there is still a lack of comprehensive performance characterization on data layouts on SIMD architectures concerning convolution methods. This paper proposes three novel data layouts for im2win convolution: NHWC, CHWN, and CHWN8, and introduces a set of general optimization techniques for both direct and im2win convolutions. We compare the optimized im2win convolution with the direct convolution and PyTorch's im2col-based convolution across the aforementioned layouts on SIMD machines. The experiments demonstrated that the im2win convolution with the new NHWC layout achieved up to 355% performance speedup over NCHW layout. Our optimizations also significantly improve the performance of both im2win and direct convolutions. Our optimized im2win and direct convolutions achieved up to 95% and 94% of machine's theoretical peak performance, respectively.

## Skill Description

This skill is generated from the arXiv paper: High Performance Im2win and Direct Convolutions using Three Tensor Layouts on SIMD Architectures (2408.00278).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2408.00278](http://arxiv.org/abs/2408.00278v1)
