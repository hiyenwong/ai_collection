---
name: arxiv-2608-19890-reliable-neural-collapse-approximation-for-open-wo
description: 'Reliable Neural Collapse Approximation for Open-World Test-Time Adaptation (arXiv: 2608.19890)'
category: neuroscience
version: "1.0"
date: 2026-08-22
---

# Reliable Neural Collapse Approximation for Open-World Test-Time Adaptation

**Authors:** Jia-Qi Lin, Yuangang Pan, Chang-Dong Wang, Haizhang Zhang, Ivor W. Tsang, Joey Tianyi Zhou
**arXiv:** 2608.19890
**Utility:** 1.00
**Published:** 2026-08-20T10:57:44Z
**Link:** http://arxiv.org/abs/2608.19890

## Abstract

Test-Time Adaptation (TTA) methods aim to bridge the domain gap between the source and target domains. However, traditional TTA methods become ineffective when the label distribution shift occurs, a challenge commonly referred to as an open-world scenario. In this paper, we introduce a new method named Reliable Neural Collapse approximation (ReNC) for Open-World Test-Time Adaptation (OWTTA). Specifically, we leverage neural collapse as a structural prior for reliable target-domain adaptation. Guided by this prior, we justify that the pre-trained classifier weights can serve as the prototypes of the source domain. By measuring the similarity between samples and prototypes, we filter out the Out-Of-Distribution~(OOD) samples for reliable updates. Furthermore, we propose a neural collapse approximation mechanism to refine these prototypes, ensuring they can gradually adapt to the target domain while maintaining the neural collapse structure. Extensive experiments on several open-world benchmarks demonstrate the superiority of the proposed method. Our empirical analysis suggests that ReNC better preserves NC-related properties in the target domain, providing useful evidence for explaining reliable OWTTA and offering new insights for model design. Code is available at https://github.com/JiaqiLin-AI/ReNC.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Reliable Neural Collapse Approximation for Open-World Test-Time Adaptation". 
The paper presents novel ideas in neuroscience that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.19890
