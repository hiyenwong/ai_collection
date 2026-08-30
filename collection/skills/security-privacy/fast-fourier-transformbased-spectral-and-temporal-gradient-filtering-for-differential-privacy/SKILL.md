# Fast Fourier Transform-Based Spectral and Temporal Gradient Filtering for Differential Privacy

**arXiv ID:** 2505.04468
**Authors:** Hyeju Shin,  Vincent-Daniel, Kyudan Jung, Seongwon Yun
**Published:** 2025-05-07T14:38:58Z
**Abstract:**
Differential Privacy (DP) has emerged as a key framework for protecting sensitive data in machine learning, but standard DP-SGD often suffers from significant accuracy loss due to injected noise. To address this limitation, we introduce the FFT-Enhanced Kalman Filter (FFTKF), a differentially private optimization method that improves gradient quality while preserving $(\varepsilon, δ)$-DP guarantees. FFTKF applies frequency-domain filtering to shift privacy noise into less informative high-frequency components, preserving the low-frequency gradient signals that carry most learning information. A scalar-gain Kalman filter with a finite-difference Hessian approximation further refines the denoised gradients. The method has per-iteration complexity $\mathcal{O}(d \log d)$ and achieves higher test accuracy than DP-SGD and DiSK on MNIST, CIFAR-10, CIFAR-100, and Tiny-ImageNet with CNNs, Wide ResNets, and Vision Transformers. Theoretical analysis shows that FFTKF ensures equivalent privacy while delivering a stronger privacy--utility trade-off through reduced variance and controlled bias.

## Skill Description

This skill is generated from the arXiv paper: Fast Fourier Transform-Based Spectral and Temporal Gradient Filtering for Differential Privacy (2505.04468).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2505.04468](http://arxiv.org/abs/2505.04468v2)
