---
name: from-msms-evidence-to-adaptive-spectroscopic
description: "From MS/MS evidence to adaptive spectroscopic char..."
tags: [cs.LG]
source: arxiv
arxiv_id: 2610.40264v1
utility: 0.91
published: 2026-10-29
---

# From MS/MS evidence to adaptive spectroscopic characterization: Reinforcement learning guided by candidate molecular structures

**Authors:** Bowen Gao, Lei Zhu, Yiying Wang, Wenjie Yu
**Published:** 2026-10-29
**arXiv:** [2610.40264v1](https://arxiv.org/abs/2610.40264v1)
**Categories:** cs.LG
**Utility Score:** 0.91

## Abstract

Small-molecule identification from tandem mass spectrometry (MS/MS) may require complementary measurements. Herein, we propose a structure-informed deep Q-network (SI-DQN) that uses existing MS/MS evidence to decide whether further characterization is needed, which measurement to request, and when to stop. The policy combines spectral representations and candidate rankings with score-weighted descriptors of the candidates' chemical features and structural differences. The policy was evaluated on 79,462 held-out samples with simulated MS/MS, infrared (IR), and nuclear magnetic resonance (NMR) spectra from the Multimodal Spectroscopic Dataset. Evaluation used fixed hard candidate sets containing the correct structure and equal normalized acquisition costs. Averaged across three training runs, SI-DQN increased Top-1 accuracy from 80.10% to 93.78% for positive-ion MS/MS starts and from 70.44% to 93.31% for negative-ion starts. The corresponding mean additional measurement counts were only 0.227 and 0.340 per sample, respectively. Complete acquisition achieved 97.72% accuracy with four additions, whereas SI-DQN reduced the additional measurement count by 94.3% and 91.5%. Relative to a rule-based policy, SI-DQN reduced the composite loss combining terminal ranking error and acquisition cost by 19.3% and 25.5%. Adding structural information to DQN further improved accuracy while reducing requests across all three training runs. At comparable ranking uncertainty, SI-DQN increased req

## Key Contributions

- Novel research in cs.LG
- Published 2026-10-29

## Activation

msms, evidence, adaptive, spectroscopic, characterization, reinforcement, learning, guided, candidate, molecular
