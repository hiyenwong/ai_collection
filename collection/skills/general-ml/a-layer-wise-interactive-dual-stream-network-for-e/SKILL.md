---
name: a-layer-wise-interactive-dual-stream-network-for-e
description: "Electroencephalography (EEG) provides a non-invasive window into brain activity, offering high temporal resolution crucial for understanding and interacting with neural processes through brain-compute..."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, research, arxiv]
    source_paper: "LI-DSN: A Layer-wise Interactive Dual-Stream Network for EEG Decoding (arXiv:2604.01889v1)"
    published: "2026-04-02"
    relevance_score: 14
---

# LI-DSN: A Layer-wise Interactive Dual-Stream Network for EEG Decoding

## Overview
Electroencephalography (EEG) provides a non-invasive window into brain activity, offering high temporal resolution crucial for understanding and interacting with neural processes through brain-computer interfaces (BCIs). Current dual-stream neural networks for EEG often process temporal and spatial features independently through parallel branches, delaying their integration until a final, late-stage fusion. This design inherently leads to an "information silo" problem, precluding intermediate cross-stream refinement and hindering spatial-temporal decompositions essential for full feature utilization. We propose LI-DSN, a layer-wise interactive dual-stream network that facilitates progressive, cross-stream communication at each layer, thereby overcoming the limitations of late-fusion paradigms. LI-DSN introduces a novel Temporal-Spatial Integration Attention (TSIA) mechanism, which constructs a Spatial Affinity Correlation Matrix (SACM) to capture inter-electrode spatial structural relationships and a Temporal Channel Aggregation Matrix (TCAM) to integrate cosine-gated temporal dynamics under spatial guidance. Furthermore, we employ an adaptive fusion strategy with learnable channel weights to optimize the integration of dual-stream features. Extensive experiments across eight diverse EEG datasets, encompassing motor imagery (MI) classification, emotion recognition, and steady-state visual evoked potentials (SSVEP), consistently demonstrate that LI-DSN significantly outperforms 13 state-of-the-art (SOTA) baseline models, showcasing its superior robustness and decoding performance. The code will be publicized after acceptance.

## Authors
Chenghao Yue, Zhiyuan Ma, Zhongye Xia, Xinche Zhang, Yisi Zhang, Xinke Shen, Sen Song

## Publication Information
- **arXiv ID**: 2604.01889v1
- **Published**: 2026-04-02
- **Category**: brain network

## Key Insights
- Research focuses on advancing understanding in brain network
- Relevance score: 14/20

## Links
- arXiv Abstract: https://arxiv.org/abs/2604.01889v1
- arXiv PDF: https://arxiv.org/pdf/2604.01889v1

## References
Chenghao Yue, Zhiyuan Ma, Zhongye Xia, Xinche Zhang, Yisi Zhang, Xinke Shen, Sen Song. "LI-DSN: A Layer-wise Interactive Dual-Stream Network for EEG Decoding". arXiv:2604.01889v1, 2026-04-02.
