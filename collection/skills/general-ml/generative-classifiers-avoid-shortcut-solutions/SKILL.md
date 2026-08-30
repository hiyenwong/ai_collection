# Generative Classifiers Avoid Shortcut Solutions

**arXiv ID:** 2512.25034
**Authors:** Alexander C. Li, Ananya Kumar, Deepak Pathak
**Published:** 2025-12-31T18:31:46Z
**Abstract:**
Discriminative approaches to classification often learn shortcuts that hold in-distribution but fail even under minor distribution shift. This failure mode stems from an overreliance on features that are spuriously correlated with the label. We show that generative classifiers, which use class-conditional generative models, can avoid this issue by modeling all features, both core and spurious, instead of mainly spurious ones. These generative classifiers are simple to train, avoiding the need for specialized augmentations, strong regularization, extra hyperparameters, or knowledge of the specific spurious correlations to avoid. We find that diffusion-based and autoregressive generative classifiers achieve state-of-the-art performance on five standard image and text distribution shift benchmarks and reduce the impact of spurious correlations in realistic applications, such as medical or satellite datasets. Finally, we carefully analyze a Gaussian toy setting to understand the inductive biases of generative classifiers, as well as the data properties that determine when generative classifiers outperform discriminative ones.

## Skill Description

This skill is generated from the arXiv paper: Generative Classifiers Avoid Shortcut Solutions (2512.25034).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2512.25034](http://arxiv.org/abs/2512.25034v1)
