---
name: pan-fm-pan-organ-foundation
description: >
  Pan-Organ Foundation Model (Pan-FM) for multimodal biomedical imaging with missing-organ robustness.
  Pre-trained on seven organs (Brain, Heart, Adipose, Liver, Kidney, Spleen, Pancreas) using
  Saliency-Guided Masking (SGM) to prevent dominant-organ shortcut learning bias. Introduces
  masking-based self-distillation for handling realistic missing-organ scenarios.
  Use when: (1) building multi-organ medical imaging foundation models, (2) handling missing
  modalities/organs in biomedical data, (3) designing saliency-guided masking strategies,
  (4) developing whole-body representation learning systems, (5) addressing dominant-organ
  shortcut learning in multimodal pre-training. Activation keywords: pan-organ foundation model,
  missing organ robustness, saliency-guided masking, multimodal biomedical imaging, dominant-organ
  shortcut learning, whole-body representation learning, UK Biobank multi-organ.
---

# Pan-FM: Pan-Organ Foundation Model with Saliency-Guided Masking

**arXiv:2605.07055** | Wu, McIlvain, Yu, & Wen (2026)

## Core Problem

Medical foundation models are trained on **single organs in isolation**, but human aging and disease
arise from **coordinated biological processes across organs**. Real-world multimodal biomedical data
have organs **missing not at random** (MNAR), causing:
- Reduced statistical power
- Limited generalizability
- Systematic bias

## Key Innovation: Saliency-Guided Masking (SGM)

### Dominant-Organ Shortcut Learning

Naive multimodal pre-training causes models to **over-rely on dominant organs** (adipose, heart)
as shortcuts, ignoring subtler cross-organ signals.

### SGM Mechanism

1. **Compute attention distribution** across organs during forward pass
2. **Adaptively mask dominant organs** based on attention scores
3. **Force balanced learning** — model must learn from all organs, not just the strongest signals
4. **Negligible overhead** — integrates seamlessly into existing self-supervised frameworks

```python
# Pseudocode for Saliency-Guided Masking
def saliency_guided_masking(attention_weights, threshold=0.7, mask_prob=0.3):
    """Mask organs with disproportionately high attention."""
    # attention_weights: [batch, num_organs, seq_len]
    organ_attention = attention_weights.mean(dim=-1)  # [batch, num_organs]
    dominant_mask = organ_attention > threshold
    random_mask = torch.rand_like(organ_attention) < mask_prob
    # Only mask dominant organs probabilistically
    return dominant_mask & random_mask
```

## Architecture

| Component | Description |
|-----------|-------------|
| **Unified backbone** | Single architecture handling all 7 organs with organ-specific adapters |
| **Masking-based self-distillation** | Teacher-student framework with organ masking during pre-training |
| **Missing-organ handling** | Built into training AND inference — no post-hoc imputation needed |
| **Cross-organ attention** | Models inter-organ dependencies explicitly |

## Evaluation Results

- **Dataset**: UK Biobank
- **Tasks**: 13 disease categories + 14 single disease entities
- **Baselines outperformed**: Single-organ FMs and naive multi-organ models
- **Key metric**: Improved robustness under missing-organ settings

## When to Use

### Apply this skill when:
- Building foundation models spanning multiple organs/body systems
- Handling MNAR (Missing Not At Random) data in medical imaging
- Designing masking strategies for self-supervised learning
- Addressing modality imbalance in multimodal models
- Developing whole-body or system-level biomedical representations

### Do NOT use when:
- Working with single-organ data only
- The task doesn't involve medical/biomedical imaging
- Missing data is MCAR (Missing Completely At Random) — simpler methods suffice

## Implementation Patterns

### Multi-Organ Pre-Training Pipeline

```python
import torch

class PanFMPreTraining:
    def __init__(self, organs, backbone, sgm_threshold=0.7):
        self.organs = organs
        self.backbone = backbone
        self.sgm_threshold = sgm_threshold
    
    def sgm_mask(self, attention_scores):
        """Saliency-Guided Masking to prevent dominant-organ shortcuts."""
        organ_importance = attention_scores.mean(dim=-1)
        dominant = organ_importance > self.sgm_threshold
        mask = dominant & (torch.rand_like(organ_importance) < 0.3)
        return mask
    
    def forward_with_sgm(self, batch):
        # Standard forward pass
        features, attention = self.backbone(batch)
        # Apply SGM
        mask = self.sgm_mask(attention)
        # Masked self-distillation
        teacher_features = features.detach()
        student_features = self.backforward(batch, mask=mask)
        return self.distillation_loss(teacher_features, student_features)
```

### Missing-Organ Inference

```python
def predict_with_missing_organs(model, available_organs, missing_mask):
    """Handle inference when some organs are missing."""
    # Model handles missing organs natively — no imputation needed
    return model.predict(available_organs, mask=missing_mask)
```

## Best Practices

1. **Always use SGM** when pre-training on heterogeneous multi-organ data
2. **Monitor attention distributions** — if one organ dominates >60% of attention, SGM is essential
3. **Test missing-organ robustness** as part of model evaluation
4. **Report per-organ contribution** to final predictions
5. **Use UK Biobank as benchmark** for multi-organ model comparison

## Related Frameworks

- **Single-organ FMs**: brain-only, heart-only models (baseline comparison)
- **Naive multi-organ**: concatenation-based approaches (prone to shortcut learning)
- **Self-supervised learning**: DINO, MAE frameworks (SGM integrates with these)

## arXiv Reference

- **Paper**: "Pan-FM: A Pan-Organ Foundation Model with Saliency-Guided Masking for Missing Robustness"
- **Authors**: Qiangqiang Wu, Grace McIlvain, Zhou Yu, Junhao Wen
- **ID**: arXiv:2605.07055v1 | Categories: cs.CV, cs.AI | Date: 2026-05-08
- **Key contribution**: First foundation model pre-trained on 7 organs with SGM for MNAR robustness

## Related Skills

- tribe-v2-foundation-model: Multi-modal brain foundation model (video/audio/language)
- brain-foundation-biomarker-validation: Foundation model biomarker validation
- brain-foundation-model-batch-effects: Batch effects in brain foundation models
