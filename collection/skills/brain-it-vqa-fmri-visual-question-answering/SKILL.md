---
name: brain-it-vqa-fmri-visual-question-answering
description: Brain-IT-VQA framework for visual question answering from fMRI signals. Decodes language tokens from brain activity and integrates with language models to answer questions about seen images. Introduces NSD-VQA benchmark dataset with 20 controlled question categories. Use when studying fMRI decoding, brain-to-text, or visual understanding from neural signals.
version: 1.0.0
author: Hermes Agent (Cron Job)
arxiv_id: 2605.29588
date_created: 2026-05-29
tags: [fMRI, VQA, brain-decoding, Brain-IT, NSD-VQA, language-tokens, visual-understanding, brain-representation]
activation_keywords: [Brain-IT, VQA, fMRI decoding, brain question answering, NSD-VQA, brain-to-text, visual understanding]
---

# Brain-IT-VQA: From Brain Signals to Answers

**arXiv:2605.29588** | Submitted: 2026-05-28 | Categories: cs.CV, cs.AI, q-bio.NC

## Authors
Roman Beliy, Matias Cosarinsky, Oliver Heinimann, Navve Wasserman, Michal Irani

## Abstract
Decoding visual content from fMRI signals recorded while a person views images, and specifically answering questions about the seen images, is a long-standing challenge. While significant progress has been made in recent years in visual question answering (VQA) from fMRI, performance remains limited. Moreover, although recent models can make increasingly accurate predictions, they have rarely been used as tools for understanding the structure of visual representations in the brain. We present Brain-IT-VQA, a framework for visual question answering from fMRI. Building on the Brain Interaction Transformer (Brain-IT), our method decodes language tokens from brain activity and integrates them with a language model to answer visual questions. Our model substantially outperforms previous fMRI-based captioning and VQA approaches. We further introduce NSD-VQA, a new dataset and benchmark for visual question answering from fMRI. Unlike existing image-fMRI VQA datasets, which typically provide only a few broad and weakly controlled questions per image, NSD-VQA provides on average 20 question-answer pairs per image across 20 controlled question categories that disentangle multiple levels of visual understanding. This enables more reliable and interpretable evaluation despite limited fMRI test data. Together, Brain-IT-VQA and NSD-VQA provide both a strong predictive framework and a tool for studying brain representations. Using this benchmark, we quantify which forms of visual and semantic information can be reliably decoded from fMRI responses to natural images. We further analyze the contributions of different brain regions across question types.

## Core Innovation

### Brain-IT-VQA Framework
End-to-end pipeline for **Visual Question Answering from fMRI**:
1. **Brain Interaction Transformer (Brain-IT)** - Decodes language tokens from brain activity
2. **Language Model Integration** - Uses decoded tokens to answer visual questions
3. **Multi-level Understanding** - Disentangles visual/semantic information from brain signals

**Key Achievement**: Substantially outperforms previous fMRI-based captioning and VQA approaches.

### NSD-VQA Benchmark Dataset
**First comprehensive VQA dataset from fMRI**:
- **20 question-answer pairs** per image (vs. few in existing datasets)
- **20 controlled question categories** (vs. broad/weakly controlled)
- **Disentangled visual understanding levels** (enables interpretable evaluation)
- **Reliable evaluation despite limited fMRI test data**

## Technical Architecture

### Brain-IT (Brain Interaction Transformer)
```
fMRI Signal → Brain-IT → Language Tokens → LM → Answer

Components:
1. fMRI Encoder: Spatial-temporal brain representation
2. Token Decoder: Predict language tokens from brain activity
3. LM Integration: Generate answers from decoded tokens
```

### Token-Level Decoding Strategy
Unlike traditional image reconstruction:
- **Direct token prediction** from fMRI (not pixel-level reconstruction)
- **Language-level representation** of visual content
- **Question-conditional decoding** (answer generation guided by question)

## Key Findings

1. **Token-Level Works Better**: Language token decoding > pixel reconstruction for VQA
2. **Question Categories Matter**: Controlled categories enable reliable evaluation
3. **Brain Regions Decodable**: Quantify what visual/semantic information can be decoded
4. **LM Integration Powerful**: Language models amplify decoded brain signals

## Applications

### Neuroscience Research
- Study brain representation structure via decoding
- Map brain regions to visual understanding levels
- Probe visual cognition through VQA tasks

### Clinical Applications
- Objective assessment of visual understanding
- Brain-based communication aids
- Visual perception diagnostics

### BCI Development
- Brain-to-text communication
- Visual content retrieval from memory
- Augmented perception systems

## References

- arXiv:2605.29588
- DOI: https://doi.org/10.48550/arXiv.2605.29588
- NSD Dataset: https://naturalscenesdataset.org
- Brain-IT: Prior work on brain signal transformers