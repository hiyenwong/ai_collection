---
name: OmniMouse Multi-Modal Brain Model
description: Scaling properties of multi-modal, multi-task brain models trained on 150B neural tokens from 3.1M neurons across 73 mice. Key insight: data scaling drives performance more than model size, inverting standard AI scaling laws.
version: "1.0"
paper_id: "2604.18827"
arxiv_url: "https://arxiv.org/abs/2604.18827"
code_url: "https://github.com/enigma-brain/omnimouse"
authors:
  - Konstantin F. Willeke
  - Polina Turishcheva
published: "2026-04-20"
categories:
  - q-bio.NC
  - cs.AI
tags:
  - neuroscience
  - brain-model
  - neural-scaling
  - multi-modal
  - multi-task
  - neural-prediction
  - behavioral-decoding
  - neural-forecasting
  - mouse-visual-cortex
  - scaling-laws
keywords:
  - OmniMouse
  - neural tokens
  - brain scaling laws
  - data scaling
  - phase transitions
  - visual cortex
  - multi-session
  - neural encoding
---

# OmniMouse: Scaling Properties of Multi-Modal, Multi-Task Brain Models

## Overview

OmniMouse investigates whether AI-style scaling principles (bigger data + bigger models) apply to modeling brain activity. The work trains multi-modal, multi-task models on an unprecedented dataset of **150B+ neural tokens** recorded from **3.1 million neurons** across **73 mice** in **323 recording sessions** from mouse visual cortex.

**Central finding:** Data scaling drives performance more than model size — inverting the standard AI scaling story where model parameters are typically the dominant factor. This suggests fundamentally different scaling dynamics in neural data modeling compared to artificial neural networks.

## Key Contributions

1. **Massive neural dataset:** 150B+ neural tokens from 3.1M neurons across 73 mice and 323 sessions, recorded during natural movies, images, parametric stimuli, and behavioral tasks.
2. **Multi-modal, multi-task framework:** A single model supports three core tasks — neural prediction, behavioral decoding, and neural forecasting.
3. **Inverted scaling relationship:** Unlike standard AI where model size is paramount, here data scaling dominates performance gains.
4. **Phase transition hypothesis:** Evidence suggesting possible phase transitions in neural modeling performance as data scales.
5. **State-of-the-art results:** Achieves best reported performance on neural prediction, behavioral decoding, and neural forecasting benchmarks.

## Tasks Supported

| Task | Description |
|------|-------------|
| **Neural Prediction** | Predict neural activity from stimulus input |
| **Behavioral Decoding** | Decode behavioral variables from recorded neural activity |
| **Neural Forecasting** | Forecast future neural activity from past neural activity |

## Stimulus Modalities

- Natural movies
- Static images
- Parametric stimuli
- Behavioral task conditions

## Scaling Insights

- **Data > Model Size:** Increasing training data (more sessions, more neurons, more tokens) yields larger performance gains than increasing model parameters.
- **Multi-session aggregation:** Combining data across many animals and sessions is critical for scaling.
- **Multi-modal training:** Training on multiple stimulus types and tasks simultaneously improves generalization.
- **Potential phase transitions:** Hints of qualitative performance shifts at certain data thresholds, analogous to emergent capabilities in large language models.

## Code & Resources

- **Repository:** [https://github.com/enigma-brain/omnimouse](https://github.com/enigma-brain/omnimouse)
- **Paper:** [arXiv:2604.18827](https://arxiv.org/abs/2604.18827)

## Relevance

This work is significant for researchers interested in:
- **Brain-AI analogies:** Whether and how AI scaling laws transfer to biological neural modeling.
- **Large-scale neural data science:** Methodologies for training on massive, multi-session, multi-animal datasets.
- **Neural coding:** Understanding how visual cortex represents diverse stimuli and drives behavior.
- **Foundation models for neuroscience:** Building general-purpose models of brain activity that transfer across tasks.
- **Scaling theory:** The inverted data-vs-model-size relationship may inform theoretical understanding of biological computation.
