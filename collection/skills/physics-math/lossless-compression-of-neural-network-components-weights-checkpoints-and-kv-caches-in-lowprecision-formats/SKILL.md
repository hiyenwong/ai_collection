# Lossless Compression of Neural Network Components: Weights, Checkpoints, and K/V Caches in Low-Precision Formats

**arXiv ID:** 2508.19263
**Authors:** Anat Heilper, Doron Singer
**Published:** 2025-08-20T12:46:50Z
**Abstract:**
As deep learning models grow and deployment becomes more widespread, reducing the storage and transmission costs of neural network weights has become increasingly important. While prior work such as ZipNN has shown that lossless compression methods - particularly those based on Huffman encoding floating-point exponents can significantly reduce model sizes, these techniques have primarily been applied to higher-precision formats such as FP32 and BF16. In this work, we extend the ZipNN approach to lower-precision floating-point formats, specifically FP8 and FP4, which are gaining popularity for efficient inference. We design a compression method that separates and compresses the exponent and mantissa components independently using entropy coding. Our evaluation shows compression ratios up to 62% for BF16 and 83% for FP8. We also investigate the compressibility of key-value (K/V) cache tensors used in large language models (LLMs), finding that they, too, exhibit compressible patterns, enabling memory savings during deployment.

## Skill Description

This skill is generated from the arXiv paper: Lossless Compression of Neural Network Components: Weights, Checkpoints, and K/V Caches in Low-Precision Formats (2508.19263).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2508.19263](http://arxiv.org/abs/2508.19263v1)
