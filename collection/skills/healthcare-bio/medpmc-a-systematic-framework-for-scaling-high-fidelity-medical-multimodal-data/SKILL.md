---
name: medpmc-a-systematic-framework-for-scaling-high-fidelity-medical-multimodal-data
description: 'Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to l. Based on arXiv:2607.07673.'
---

# MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models

**arXiv**: 2607.07673 | **Authors**: Hyunjae Kim, Dain Kim, Pan Xiao, Serina S. Applebaum, Younjoon Chung et al. | **Utility**: 0.85

## Overview

Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable framework that transforms permissively licensed literature into high-fidelity infrastructure for medical multimodal models. Applied to 6.1 million PMC articles, MedPMC curated 11 million medical image-text pairs. Component evaluations showed strong performance for initial screening (F1 = 93.2), multi-panel figure detection (F1 = 96.5), figure separation (mAP = 89.8), caption separation and alignment (F1 = 81.4; ROUGE-L = 85.3), and medical figure classification (F1 = 96.5). Manual review by five annotators, three with medical training, found 95.3% of MedPMC images medically relevant, versus 19.7% in a prior PMC-derived dataset. Across 26 benchmarks spanning 11 specialties, a MedPMC-trained CLIP-style model improved average zero-shot AUC by 7.1 percentage points over the strongest architecture-matched biomedical CLIP baseline despite using fewer than half as many image-text pairs. As the vision encoder in a multimodal large language model, it improved medical visual question-answering by 1.9 and 16.9 percentage points across two benchmarks. In 10,524 Yale New Haven Health System dermatology photographs, it improved morphology-to-image retrieval Recall@5 by 11.7 percentage points. These findings show that high-fidelity literature curation strengthens medical multimodal foundation models across benchmark and clinical settings. We publicly release the framework, corpus, benchmarks, and pretrained models.

## Key Contributions

1. Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams.
2. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data.
3. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation.
4. We introduce MedPMC, an automated, continuously updatable framework that transforms permissively licensed literature into high-fidelity infrastructure for medical multimodal models.

## Implementation Notes

- **Keywords**: medical-ai
- **Categories**: cs.CV, cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: medical-ai.
