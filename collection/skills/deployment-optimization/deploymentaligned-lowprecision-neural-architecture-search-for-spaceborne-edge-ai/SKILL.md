# Deployment-Aligned Low-Precision Neural Architecture Search for Spaceborne Edge AI

**arXiv ID:** 2604.24492
**Authors:** Parampuneet Kaur Thind, Vaibhav Katturu, Giacomo Zema, Roberto Del Prete
**Published:** 2026-04-27T13:58:18Z
**Abstract:**
Designing deep networks that meet strict latency and accuracy constraints on edge accelerators increasingly relies on hardware-aware optimization, including neural architecture search (NAS) guided by device-level metrics. Yet most hardware-aware NAS pipelines still optimize architectures under full-precision assumptions and apply low-precision adaptation only after the search, leading to a mismatch between optimization-time behavior and deployment-time execution on low-precision hardware that can substantially degrade accuracy. We address this limitation by integrating deployment-aligned low-precision training directly into hardware-aware NAS. Candidate architectures are exposed to FP16 numerical constraints during fine-tuning and evaluation, enabling joint optimization of architectural efficiency and numerical robustness without modifying the search space or evolutionary strategy. We evaluate the proposed framework on vessel segmentation for spaceborne maritime monitoring, targeting the Intel Movidius Myriad X Visual Processing Unit (VPU). While post-training precision conversion reduces on-device performance from 0.85 to 0.78 mIoU, deployment-aligned low-precision training achieves 0.826 mIoU on-device for the same architecture (95,791 parameters), recovering approximately two-thirds of deployment-induced accuracy gap without increasing model complexity. These results demonstrate that incorporating deployment-consistent numerical constraints into hardware-aware NAS substantially improves robustness and alignment between optimization and deployment for resource-constrained edge Artificial Intelligence (AI).

## Skill Description

This skill is generated from the arXiv paper: Deployment-Aligned Low-Precision Neural Architecture Search for Spaceborne Edge AI (2604.24492).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.24492](http://arxiv.org/abs/2604.24492v1)
