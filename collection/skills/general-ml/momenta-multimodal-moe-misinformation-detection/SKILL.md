---
name: momenta-multimodal-moe-misinformation-detection
description: >
  MOMENTA — Mixture-of-Experts over multimodal embeddings with neural temporal aggregation for 
  misinformation detection. Combines modality-specific MoE modules, bidirectional co-attention, 
  discrepancy-aware branch, and attention-based temporal aggregation with drift/momentum encoding.
  Use when: multimodal misinformation detection, MoE for multimodal learning, temporal aggregation, 
  cross-modal disagreement detection, fact-checking systems.
  Trigger: misinformation detection, multimodal MoE, cross-modal disagreement, temporal drift, 
  fake news detection, MOMENTA, 多模态虚假信息检测.
version: 1.0.0
author: Research Synthesis (arXiv:2604.16172)
license: MIT
metadata:
  hermes:
    tags: [misinformation, multimodal, mixture-of-experts, temporal-aggregation, fact-checking]
    source_paper: "MOMENTA: Mixture-of-Experts Over Multimodal Embeddings with Neural Temporal Aggregation for Misinformation Detection (arXiv:2604.16172)"
---

# MOMENTA: Multimodal MoE Misinformation Detection

## Overview

Unified multimodal misinformation detection framework combining:
- Modality-specific MoE modules for specialized processing
- Bidirectional co-attention for text-visual alignment
- Discrepancy-aware branch for cross-modal disagreement
- Attention-based temporal aggregation with drift/momentum encoding
- Domain-adversarial learning with prototype memory bank

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Input Modalities                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Text    │  │  Visual  │  │ Temporal │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       ↓             ↓             ↓                      │
│  ┌──────────┐  ┌──────────┐                              │
│  │ Text MoE │  │Vis MoE   │  ← Modality-specific experts │
│  └────┬─────┘  └────┬─────┘                              │
│       └──────┬──────┘                                     │
│              ↓                                             │
│  ┌─────────────────────┐                                  │
│  │ Bidirectional       │  ← Cross-modal alignment         │
│  │ Co-Attention        │                                  │
│  └──────────┬──────────┘                                  │
│              ↓                                             │
│  ┌─────────────────────┐  ← Detect contradictions         │
│  │ Discrepancy-Aware   │     between modalities            │
│  │ Branch              │                                  │
│  └──────────┬──────────┘                                  │
│              ↓                                             │
│  ┌─────────────────────┐  ← Drift/momentum encoding       │
│  │ Temporal Aggregation│     for temporal sequences        │
│  │ (Drift/Momentum)    │                                  │
│  └──────────┬──────────┘                                  │
│              ↓                                             │
│  ┌─────────────────────┐  ← Domain generalization         │
│  │ Domain-Adversarial  │     + prototype memory            │
│  │ + Prototype Memory  │                                  │
│  └──────────┬──────────┘                                  │
│              ↓                                             │
│         Misclassification (Real/Fake)                     │
└─────────────────────────────────────────────────────────┘
```

## Key Components

### 1. Modality-Specific MoE
- Separate expert pools for text and visual modalities
- Dynamic routing selects relevant experts per input
- Enables specialized feature extraction

### 2. Bidirectional Co-Attention
- Text attends to visual features AND visual attends to text
- Creates aligned cross-modal representations
- Captures inter-modal dependencies

### 3. Discrepancy-Aware Branch
- Specifically detects disagreements between modalities
- Key signal: text says one thing, image shows another
- Primary misinformation indicator

### 4. Temporal Aggregation
- Drift encoding: captures distribution shift over time
- Momentum encoding: maintains temporal consistency
- Attention-weighted aggregation of temporal features

## Evaluated Datasets
- Fakeddit, MMCoVaR, Weibo, XFacta

## Applications
- Social media content moderation
- Automated fact-checking systems
- News verification platforms
- Multimodal content analysis

## Activation Keywords
- misinformation detection, multimodal MoE, fact-checking
- cross-modal disagreement, temporal aggregation
- fake news detection, MOMENTA
- 虚假信息检测, 多模态专家混合

## References
- Yeganeh Abdollahinejad, Ahmad Mousavi, et al. "MOMENTA: Mixture-of-Experts Over Multimodal 
  Embeddings with Neural Temporal Aggregation for Misinformation Detection." arXiv:2604.16172
