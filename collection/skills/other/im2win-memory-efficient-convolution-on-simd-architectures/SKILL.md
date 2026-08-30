# Im2win: Memory Efficient Convolution On SIMD Architectures

**arXiv ID:** 2306.14320
**Authors:** Shuai Lu, Jun Chu, Xu T. Liu
**Published:** 2023-06-25T19:21:10Z
**Abstract:**
Convolution is the most expensive operation among neural network operations, thus its performance is critical to the overall performance of neural networks. Commonly used convolution approaches, including general matrix multiplication (GEMM)-based convolution and direct convolution, rely on im2col for data transformation or do not use data transformation at all, respectively. However, the im2col data transformation can lead to at least 2$\times$ memory footprint compared to not using data transformation at all, thus limiting the size of neural network models running on memory-limited systems. Meanwhile, not using data transformation usually performs poorly due to nonconsecutive memory access although it consumes less memory. To solve those problems, we propose a new memory-efficient data transformation algorithm, called im2win. This algorithm refactorizes a row of square or rectangle dot product windows of the input image and flattens unique elements within these windows into a row in the output tensor, which enables consecutive memory access and data reuse, and thus greatly reduces the memory overhead. Furthermore, we propose a high-performance im2win-based convolution algorithm with various optimizations, including vectorization, loop reordering, etc. Our experimental results show that our algorithm reduces the memory overhead by average to 41.6% compared to the PyTorch's convolution implementation based on im2col, and achieves average to 3.6$\times$ and 5.3$\times$ speedup in performance compared to the im2col-based convolution and not using data transformation, respectively.

## Skill Description

This skill is generated from the arXiv paper: Im2win: Memory Efficient Convolution On SIMD Architectures (2306.14320).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2306.14320](http://arxiv.org/abs/2306.14320v1)
