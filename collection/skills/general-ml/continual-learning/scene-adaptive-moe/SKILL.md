---
name: scene-adaptive-moe
description: "Scene-Adaptive Mixture of Experts (SAMoE-C) for continual learning in CSI-based human activity recognition. Uses MoE architecture with domain-specific expert routing and scene-adaptive gating for domain-incremental HAR. Use when: CSI sensing, HAR, domain-incremental learning, MoE continual learning, wireless sensing CL."
---

# Scene-Adaptive MoE for CSI Continual Learning

## Problem

CSI-based HAR suffers from domain shift across physical environments. Standard CL methods struggle with scene-specific patterns.

## SAMoE-C Architecture

- **Mixture of Experts**: Domain-specific experts for different physical scenes
- **Scene-Adaptive Gating**: Routes inputs to appropriate experts
- **Continual Expansion**: Adds new experts for new scenes without forgetting old ones

## Results

Significant improvement over EWC, LwF, and experience replay on multi-scene HAR benchmarks.

## Paper

- Zheng et al., arXiv:2605.06447, 2026
