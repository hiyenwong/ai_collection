# muNet: Evolving Pretrained Deep Neural Networks into Scalable Auto-tuning Multitask Systems

**arXiv ID:** 2205.10937
**Authors:** Andrea Gesmundo, Jeff Dean
**Published:** 2022-05-22T21:54:33Z
**Abstract:**
Most uses of machine learning today involve training a model from scratch for a particular task, or sometimes starting with a model pretrained on a related task and then fine-tuning on a downstream task. Both approaches offer limited knowledge transfer between different tasks, time-consuming human-driven customization to individual tasks and high computational costs especially when starting from randomly initialized models. We propose a method that uses the layers of a pretrained deep neural network as building blocks to construct an ML system that can jointly solve an arbitrary number of tasks. The resulting system can leverage cross tasks knowledge transfer, while being immune from common drawbacks of multitask approaches such as catastrophic forgetting, gradients interference and negative transfer. We define an evolutionary approach designed to jointly select the prior knowledge relevant for each task, choose the subset of the model parameters to train and dynamically auto-tune its hyperparameters. Furthermore, a novel scale control method is employed to achieve quality/size trade-offs that outperform common fine-tuning techniques. Compared with standard fine-tuning on a benchmark of 10 diverse image classification tasks, the proposed model improves the average accuracy by 2.39% while using 47% less parameters per task.

## Skill Description

This skill is generated from the arXiv paper: muNet: Evolving Pretrained Deep Neural Networks into Scalable Auto-tuning Multitask Systems (2205.10937).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2205.10937](http://arxiv.org/abs/2205.10937v2)
