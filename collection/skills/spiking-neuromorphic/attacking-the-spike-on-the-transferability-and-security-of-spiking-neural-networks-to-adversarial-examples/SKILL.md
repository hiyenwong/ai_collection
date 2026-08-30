# Attacking the Spike: On the Transferability and Security of Spiking Neural Networks to Adversarial Examples

**arXiv ID:** 2209.03358
**Authors:** Nuo Xu, Kaleel Mahmood, Haowen Fang, Ethan Rathbun, Caiwen Ding, Wujie Wen
**Published:** 2022-09-07T17:05:48Z
**Abstract:**
Spiking neural networks (SNNs) have attracted much attention for their high energy efficiency and recent advances in classification performance. However, unlike traditional deep learning approaches, the study of SNN robustness to adversarial examples remains relatively underdeveloped. In this work, we advance the adversarial attack side of SNNs through three contributions. First, we show that successful white-box adversarial attacks on SNNs are highly dependent on the underlying surrogate gradient estimator, even for adversarially trained SNNs. Second, using the best single surrogate gradient estimator, we analyze the transferability of adversarial attacks across SNNs, Vision Transformers (ViTs) and CNNs. Our analysis reveals two key gaps: no existing white-box attack exploits multiple surrogate gradient estimators for SNNs, and no single-model attack reliably generates adversarial examples that simultaneously fool both SNN and non-SNN models. For our third contribution, we develop the Mixed Dynamic Spiking Estimation (MDSE) attack to address these issues. MDSE uses a dynamic gradient estimation scheme to fully exploit multiple surrogate gradient estimator functions and generates adversarial examples capable of fooling SNN and non-SNN models simultaneously. MDSE is up to 91.4% more effective on SNN/ViT model ensembles and provides a 3x boost on adversarially trained SNN ensembles compared to conventional white-box attacks like Auto-PGD. Experiments cover three datasets (CIFAR-10, CIFAR-100, ImageNet) and nineteen classifier models (seven per CIFAR dataset, five for ImageNet). Our implementation of MDSE and the evaluated models is publicly available at https://github.com/nuoxuxxx/attacking-the-spike-mdse.

## Skill Description

This skill is generated from the arXiv paper: Attacking the Spike: On the Transferability and Security of Spiking Neural Networks to Adversarial Examples (2209.03358).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2209.03358](http://arxiv.org/abs/2209.03358v5)
