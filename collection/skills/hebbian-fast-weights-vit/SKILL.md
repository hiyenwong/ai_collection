---
name: hebbian-fast-weights-vit
description: "Hebbian Fast-Weight (HFW) modules integrated into Vision Transformer architectures for few-shot learning. Activation triggers: hebbian fast weights, hebbian ViT, fast synaptic updates, transformer meta-learning, few-shot transformer, hebbian plasticity vision, swin hebbian, prototypical network hebbian, rapid adaptation transformer."
---

# Hebbian Fast Weights in Vision Transformers

> Empirical study of Hebbian fast-weight modules integrated into ViT backbones enabling rapid within-episode adaptation for few-shot character recognition.

## Metadata
- **Source**: arXiv:2605.02920
- **Authors**: Gavin Money, Sindhuja Penchala, Jiacheng Li, Noorbakhsh Amiri Golilarz
- **Published**: 2026-04-22
- **Subjects**: Neural and Evolutionary Computing (cs.NE), Computer Vision (cs.CV), Machine Learning (cs.LG)

## Core Methodology

### Key Innovation
Standard transformers lack mechanisms for rapid adaptation within an episode. Biological neural systems solve this through **fast synaptic updates** forming transient associative memories (Hebbian plasticity). HFW modules integrate this principle into ViT architectures, enabling few-shot learning without meta-training on the target task.

### Architecture Design
- **Backbones Tested**: ViT-Small, DeiT-Small, Swin-Tiny
- **HFW Module**: Hebbian fast-weight layer that forms transient associative memories during inference
- **Placement Strategy** (critical finding):
  - **Swin-Tiny**: Single HFW module on **final stage feature map** (after all hierarchical stages) — achieves 96.2% 1-shot, 99.2% 5-shot on Omniglot
  - **Per-block placement FAILS** for ViT/DeiT in low-data regime — causes training instability
  - Interaction between Swin's shifted window inductive bias and episode-level Hebbian binding is synergistic

### Implementation Pattern
1. Select backbone architecture (ViT, DeiT, Swin)
2. Add HFW module — use **single-module placement** on final stage output (NOT per-block)
3. Train under Prototypical Network meta-learning framework
4. Evaluate on N-way K-shot classification tasks
5. Analyze binding location impact on stability and accuracy

### Results Summary
| Model | 1-Shot | 5-Shot |
|-------|--------|--------|
| Swin-Hebbian | 96.2% | 99.2% |
| ViT-Hebbian | Lower | Lower |
| DeiT-Hebbian | Lower | Lower |

## Applications
- Few-shot image classification with rapid adaptation
- Bio-inspired transformer architecture design
- Meta-learning without explicit meta-training
- Character recognition and pattern matching
- Understanding fast/slow weight interaction in neural networks

## Pitfalls
- **Per-block HFW placement causes instability** for ViT/DeiT — use final-stage only
- Swin's hierarchical architecture uniquely benefits from HFW — other backbones may need different strategies
- Evaluated only on Omniglot — generalization to natural images needs validation
- Fast-weight modules add inference-time computation overhead

## Related Skills
- hebbian-learning-benchmark-memory
- feedback-hebbian-continual-learning
- transformer-prototype-readout
