---
name: abnat-attention-route-preservation
version: v1.0.0
last_updated: 2026-10-17
description: "Analog CIM robustness via attention-route distillation."
arxiv_id: "2610.22065"
authors: "Wenshuai Yao, Wenyong Zhou, Hanyong Shao, Zhiyuan Ning, Yizhe Chen et al."
tags: [noise-aware-training, analog-computing, transformers, distillation, hardware-robustness]
---

# ABNAT: Attention-Based Noise-Aware Training for Analog CIM Transformers

From arXiv:2610.22065 (2026-10-15).

## Problem

Analog compute-in-memory (CIM) is energy-efficient but its hardware non-idealities perturb stored weights and degrade transformers. Existing noise-aware training (NAT) injects noise during training but ignores attention — yet CIM noise reshapes attention maps severely, and NAT models stay overconfident even when their attention routes deviate from the clean reference.

## Method

**ABNAT (Attention-Based Noise-Aware Training):**

1. Two diagnostic observations: (a) clean-vs-noisy attention map divergence grows substantially in **deeper layers**; (b) conventional NAT remains overconfident while its attention routes drift.
2. Fix: teach the noisy student to **preserve the clean teacher's headwise attention routes** (head-level attention distillation under noise injection) rather than merely reproduce output answers.
3. Selective variants reduce training cost by distilling only the most noise-sensitive heads/layers.
4. No hardware changes, no inference overhead.

## Results

- Across vision, language, and multimodal transformers: noise-degraded accuracy improved by up to 11.28% over NAT baselines.
- Attention deviation reduced by up to 85.77%.

## Reusable Pattern

**Route-matching as the robustness target.** When a perturbed/quantized/noisy student must track a clean teacher, matching output logits is insufficient — the model can be right while taking a different, fragile internal path. Distilling intermediate **routing decisions** (headwise attention, MoE router logits, token-mixing patterns) preserves the computational pathway and yields robustness that answer-level distillation misses. The diagnostic transfers too: measure divergence of routing (not outputs) per layer to find where perturbation hurts, and target distillation there. Applies to quantization-aware training, noisy-storage inference (CIM/flash), and adversarial robustness.

## Resources

- Paper: https://arxiv.org/abs/2610.22065
