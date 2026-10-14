---
name: arxiv-2610-14423-scaling-laws-for-multimodal-data-mixtures
description: 'Scaling Laws for Multimodal Data Mixtures (arXiv: 2610.14423)'
metadata:
  {
    "arxiv_id": "2610.14423",
    "utility": 0.96,
    "title": "Scaling Laws for Multimodal Data Mixtures",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.14423"
  }
---

# Scaling Laws for Multimodal Data Mixtures

**arXiv ID:** 2610.14423
**URL:** https://arxiv.org/abs/2610.14423
**Utility Score:** 0.96

## Abstract

Frontier AI systems are increasingly natively multimodal, jointly pretrained on multiple modalities, such as text, vision, and audio. However, the scientific understanding of the multimodal data mixtures used to pretrain these systems --- how much of each modality to mix, and at what potential interference cost to the others --- is largely absent or gatekept. In this work, we derive data mixing scaling laws for three modalities: text, vision, and audio. Multimodal Large Language Models (MLLMs) increasingly adopt Mixture-of-Experts (MoE) architectures, as MoEs scale efficiently and partially limit cross-modal interference. We therefore use MoEs to conduct 268 experiments ranging from 457M to 8.3B parameters, on up to 150 billion tokens. Our work leads to multiple actionable insights into multimodal data mixing for training MLLMs. First, compute optima are modality-specific: audio modality is model-heavy, favoring scaling parameters over tokens, while text and vision require balanced scaling of model size and data. Second, repeating vision or audio data beyond 2x yields negligible benefits. Finally, cross-modal interactions are highly asymmetric: vision strongly interferes with audio, whereas audio&#39;s interference with learning text and vision is negligible. Overall, we provide a principled foundation for understanding the multimodal data mixtures needed to train frontier MLLMs.

## Key Topics

scaling law, vision, multimodal, pretrain

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.14423
