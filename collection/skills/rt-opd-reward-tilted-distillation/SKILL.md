---
name: rt-opd-reward-tilted-distillation
version: v1.0.0
last_updated: 2026-09-26
description: "RT-OPD methodology — reward-tilted on-policy distillation using teacher with-vs-without-modality log-probability contrast to force acoustic grounding in audio-language models. Use when: (1) multimodal students exploit text shortcuts and ignore perceptual evidence, (2) distilling multimodal models on-policy, (3) counterfactual modality-ablation reward design. Keywords: on-policy distillation, reward tilting, counterfactual contrast, audio-language, modality grounding."
arxiv_id: "2609.28778"
authors: "Kaiyang Li, Shaobo Han, Yue Tian, Shihao Ji"
tags: [distillation, on-policy, multimodal, counterfactual, reward-design, audio-language]
---

# RT-OPD: Reward-Tilted On-Policy Distillation

From arXiv:2609.28778 (2026-09-23). Code: https://github.com/KaiyangLi1992/RT-OPD

## Problem

Audio-language models exploit **textual shortcuts** — answering from linguistic priors while ignoring actual audio evidence. Vanilla OPD inherits this: the teacher's token distribution doesn't distinguish acoustic support from linguistic predictability.

## Method

**Counterfactual modality-contrast reward.** For each student-generated response:

1. Frozen teacher predicts next-token distribution **with** audio input: `P(y | text, audio)`
2. Same teacher predicts **without** audio: `P(y | text)`
3. The log-probability contrast `log P_with − log P_without` defines a per-token reward
4. This reward **tilts (reshapes) the teacher's target distribution** before reverse-KL distillation

Effect: supervision mass concentrates on tokens whose probability genuinely depends on audio — the marginal acoustic evidence — and discounts tokens predictable from language alone.

## Results

- Consistently beats Vanilla OPD across 2 students × 3 benchmarks
- 3B model reaches 72.72% on MMAU — best among 3B, competitive with 7B/8B models
- Silenced/replaced-audio probes confirm stronger reliance on acoustic evidence

## Reusable Pattern

**With-vs-without counterfactual reward for modality grounding.** Any multimodal student at risk of shortcut learning can be distilled with this recipe: freeze the teacher → compute per-token log-prob difference with the critical modality present vs ablated → convert contrast into a reward that reweights the distillation target. Generalizes to vision-language (image ablation), embodied (proprioception ablation), and tabular+context settings. The teacher needs no extra training — only two forward passes per step.

## Resources

- Paper: https://arxiv.org/abs/2609.28778
- Code: https://github.com/KaiyangLi1992/RT-OPD
