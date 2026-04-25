---
name: energy-based-transformers
description: 'Research paper: Energy-Based Transformers are Scalable Learners and Thinkers. Introduces EBTs - a new class of Energy-Based Models that scale 35% faster than Transformer++ and improve System 2 Thinking by 29% through gradient descent-based energy minimization.'
metadata:
  openclaw:
    emoji: "⚡"
    tags: ["research", "arxiv", "energy-based-models", "transformers", "system-2-thinking", "unsupervised-learning", "multi-modal", "scaling"]
---

# Energy-Based Transformers are Scalable Learners and Thinkers

**arXiv ID:** 2507.02092  
**Published:** 2025-07-02  
**Authors:** Alexi Gladstone, Ganesh Nanduru, Md Mofijul Islam, Peixuan Han, Hyeonjeong Ha, Aman Chadha, Yilun Du, Heng Ji, Jundong Li, Tariq Iqbal  
**Categories:** cs.LG, cs.AI, cs.CL, cs.CV  
**Utility Score:** 0.95

## Abstract

Inference-time computation techniques, analogous to human System 2 Thinking, have recently become popular for improving model performances. However, most existing approaches suffer from several limitations: they are modality-specific (e.g., working only in text), problem-specific (e.g., verifiable domains like math and coding), or require additional supervision/training on top of unsupervised pretraining (e.g., verifiers or verifiable rewards). In this paper, we ask the question "Is it possible to generalize these System 2 Thinking approaches, and develop models that learn to think solely from unsupervised learning?" Interestingly, we find the answer is yes, by learning to explicitly verify the compatibility between inputs and candidate-predictions, and then re-framing prediction problems as optimization with respect to this verifier. Specifically, we train Energy-Based Transformers (EBTs) -- a new class of Energy-Based Models (EBMs) -- to assign an energy value to every input and candidate-prediction pair, enabling predictions through gradient descent-based energy minimization until convergence. Across both discrete (text) and continuous (visual) modalities, we find EBTs scale faster than the dominant Transformer++ approach during training, achieving an up to 35% higher scaling rate with respect to data, batch size, parameters, FLOPs, and depth. During inference, EBTs improve performance with System 2 Thinking by 29% more than the Transformer++ on language tasks, and EBTs outperform Diffusion Transformers on image denoising while using fewer forward passes. Further, we find that EBTs achieve better results than existing models on most downstream tasks given the same or worse pretraining performance, suggesting that EBTs generalize better than existing approaches. Consequently, EBTs are a promising new paradigm for scaling both the learning and thinking capabilities of models.

## Key Contributions

1. **Energy-Based Transformers (EBTs)**: New class of EBMs assigning energy values to input-prediction pairs
2. **Superior Scaling**: 35% higher scaling rate vs Transformer++ across data, batch size, parameters, FLOPs, depth
3. **Enhanced System 2 Thinking**: 29% improvement over Transformer++ on language tasks
4. **Cross-Modal**: Works across discrete (text) and continuous (visual) modalities
5. **Better Generalization**: Superior downstream task performance
6. **Unsupervised Learning**: Learns to think without additional supervision

## Technical Approach

### Core Mechanism

Traditional autoregressive models predict tokens sequentially. EBTs instead:
1. Define energy function E(x, y) measuring compatibility between input x and candidate prediction y
2. Use gradient descent to find y minimizing E(x, y)
3. Iterate until convergence

### Advantages

| Limitation | Solution |
|------------|----------|
| Modality-specific | Works across text and vision |
| Problem-specific | General prediction framework |
| Requires supervision | Learns from unsupervised data |

## Relevance to AI Systems

- **System 2 Thinking**: Generalizes inference-time computation without supervision
- **Multi-Modal**: Unified framework for text and vision
- **Scalability**: Better scaling laws than Transformer++
t- **Generalization**: Superior transfer to downstream tasks

## Technical Keywords

energy-based models, transformers, system 2 thinking, inference-time computation, unsupervised learning, multi-modal, scaling laws, gradient descent, energy minimization

## URL

https://arxiv.org/abs/2507.02092

---

**Tracked:** 2026-04-22  
**Source:** arXiv Paper Tracker
