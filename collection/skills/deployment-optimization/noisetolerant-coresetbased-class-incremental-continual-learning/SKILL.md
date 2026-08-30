# Noise-Tolerant Coreset-Based Class Incremental Continual Learning

**arXiv ID:** 2504.16763
**Authors:** Edison Mucllari, Aswin Raghavan, Zachary Alan Daniels
**Published:** 2025-04-23T14:34:20Z
**Abstract:**
Many applications of computer vision require the ability to adapt to novel data distributions after deployment. Adaptation requires algorithms capable of continual learning (CL). Continual learners must be plastic to adapt to novel tasks while minimizing forgetting of previous tasks.However, CL opens up avenues for noise to enter the training pipeline and disrupt the CL. This work focuses on label noise and instance noise in the context of class-incremental learning (CIL), where new classes are added to a classifier over time, and there is no access to external data from past classes. We aim to understand the sensitivity of CL methods that work by replaying items from a memory constructed using the idea of Coresets. We derive a new bound for the robustness of such a method to uncorrelated instance noise under a general additive noise threat model, revealing several insights. Putting the theory into practice, we create two continual learning algorithms to construct noise-tolerant replay buffers. We empirically compare the effectiveness of prior memory-based continual learners and the proposed algorithms under label and uncorrelated instance noise on five diverse datasets. We show that existing memory-based CL are not robust whereas the proposed methods exhibit significant improvements in maximizing classification accuracy and minimizing forgetting in the noisy CIL setting.

## Skill Description

This skill is generated from the arXiv paper: Noise-Tolerant Coreset-Based Class Incremental Continual Learning (2504.16763).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2504.16763](http://arxiv.org/abs/2504.16763v1)
