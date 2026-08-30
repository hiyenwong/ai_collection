# Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models

**arXiv ID:** 2404.07724
**Authors:** Tuomas Kynkäänniemi, Miika Aittala, Tero Karras, Samuli Laine, Timo Aila, Jaakko Lehtinen
**Published:** 2024-04-11T13:16:47Z
**Abstract:**
Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models. Traditionally, a constant guidance weight has been applied throughout the sampling chain of an image. We show that guidance is clearly harmful toward the beginning of the chain (high noise levels), largely unnecessary toward the end (low noise levels), and only beneficial in the middle. We thus restrict it to a specific range of noise levels, improving both the inference speed and result quality. This limited guidance interval improves the record FID in ImageNet-512 significantly, from 1.81 to 1.40. We show that it is quantitatively and qualitatively beneficial across different sampler parameters, network architectures, and datasets, including the large-scale setting of Stable Diffusion XL. We thus suggest exposing the guidance interval as a hyperparameter in all diffusion models that use guidance.

## Skill Description

This skill is generated from the arXiv paper: Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models (2404.07724).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2404.07724](http://arxiv.org/abs/2404.07724v2)
