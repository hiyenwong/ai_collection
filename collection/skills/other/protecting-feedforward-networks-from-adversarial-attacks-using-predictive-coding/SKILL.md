# Protecting Feed-Forward Networks from Adversarial Attacks Using Predictive Coding

**arXiv ID:** 2411.00222
**Authors:** Ehsan Ganjidoost, Jeff Orchard
**Published:** 2024-10-31T21:38:05Z
**Abstract:**
An adversarial example is a modified input image designed to cause a Machine Learning (ML) model to make a mistake; these perturbations are often invisible or subtle to human observers and highlight vulnerabilities in a model's ability to generalize from its training data. Several adversarial attacks can create such examples, each with a different perspective, effectiveness, and perceptibility of changes. Conversely, defending against such adversarial attacks improves the robustness of ML models in image processing and other domains of deep learning. Most defence mechanisms require either a level of model awareness, changes to the model, or access to a comprehensive set of adversarial examples during training, which is impractical. Another option is to use an auxiliary model in a preprocessing manner without changing the primary model. This study presents a practical and effective solution -- using predictive coding networks (PCnets) as an auxiliary step for adversarial defence. By seamlessly integrating PCnets into feed-forward networks as a preprocessing step, we substantially bolster resilience to adversarial perturbations. Our experiments on MNIST and CIFAR10 demonstrate the remarkable effectiveness of PCnets in mitigating adversarial examples with about 82% and 65% improvements in robustness, respectively. The PCnet, trained on a small subset of the dataset, leverages its generative nature to effectively counter adversarial efforts, reverting perturbed images closer to their original forms. This innovative approach holds promise for enhancing the security and reliability of neural network classifiers in the face of the escalating threat of adversarial attacks.

## Skill Description

This skill is generated from the arXiv paper: Protecting Feed-Forward Networks from Adversarial Attacks Using Predictive Coding (2411.00222).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2411.00222](http://arxiv.org/abs/2411.00222v1)
