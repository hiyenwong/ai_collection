---
name: arxiv-2608-19906-peta-parameter-efficient-test-time-adaptation-for
description: 'PETA:Parameter-Efficient Test-Time Adaptation for Virtual Screening (arXiv: 2608.19906)'
category: vision-generative
version: "1.0"
date: 2026-08-22
---

# PETA:Parameter-Efficient Test-Time Adaptation for Virtual Screening

**Authors:** Jia-Qi Lin, Yinghua Yao, Chang-Dong Wang, Yew-Soon Ong, Yuangang Pan
**arXiv:** 2608.19906
**Utility:** 1.00
**Published:** 2026-08-20T11:17:27Z
**Link:** http://arxiv.org/abs/2608.19906

## Abstract

Accurately ranking active ligands for a target protein pocket from massive chemical libraries remains a central challenge in virtual screening. DrugCLIP and its recent extensions substantially accelerate this process by encoding protein pockets and molecules into a shared embedding space. Despite this progress, further performance improvements typically require retraining the entire model, incurring substantial computational overhead and making target-specific customization inefficient. In this work, we formulate the specialization of pretrained virtual screening models to individual pockets as a test-time adaptation problem and propose PETA, a parameter-efficient framework that directly adapts pretrained model at test time. Given a target pocket, PETA constructs pocket-specific negatives through molecular diffusion and chemical validity filtering, and further moves them toward the reference ligand retrieved from structural databases via embedding-space mixup to create more challenging ranking tasks. A ranking objective then places greater emphasis on suppressing high-scoring invalid candidates that could contaminate the top-ranked screening results, providing structured supervision for lightweight adaptation. Experiments across diverse benchmarks demonstrate that this lightweight, pocket-specific adaptation outperforms both pretrained and fully retrained baselines while updating only the LayerNorm parameters, which account for approximately $0.03\%$ of the full model.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "PETA:Parameter-Efficient Test-Time Adaptation for Virtual Screening". 
The paper presents novel ideas in vision-generative that can be applied to agent systems.

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

- arXiv:2608.19906
