---
name: medical-domain-adaptation
description: >
  Medical image domain adaptation and transfer learning methodology.
  Use when working with medical imaging AI tasks including: (1) adapting pre-trained
  models to new clinical domains with scarce annotated data, (2) parameter-efficient
  fine-tuning for medical image segmentation/classification, (3) handling domain shift
  between different medical imaging sites/modalities, (4) federated learning for medical
  images across institutions. Covers RKHS-MMD, PEFT, MedSR, and imbalanced classification
  in medical datasets.
---

# Medical Domain Adaptation

## Core Challenge
Adapting pre-trained deep learning models to new clinical domains where annotated target data is scarce.

## Key Methodologies

### 1. RKHS-MMD Domain Adaptation
- Use Reproducing Kernel Hilbert Space Maximum Mean Discrepancy for distribution alignment
- Minimizes distribution shift between source and target clinical domains
- Effective for segmentation and classification transfer

### 2. Parameter-Efficient Fine-Tuning (PEFT)
- Selectively update small subset of model parameters (adapters, LoRA)
- Preserves pre-trained knowledge while adapting to new domain
- Reduces overfitting on small medical datasets

### 3. Medical Image Super-Resolution (MedSR)
- Multi-domain super-resolution: MRI, CT, X-ray, Ultrasound, Fundus
- Preserve anatomical accuracy while enhancing resolution
- Multi-modal training with domain-specific adapters

### 4. Imbalanced Classification
- Medical datasets have long-tailed class distributions
- Rare classes often clinically critical (rare diseases)
- Use capacity-aware loss weighting and focal loss variants

## Implementation Steps

1. **Assess domain gap**: Compute MMD or similar metric between source/target distributions
2. **Choose adaptation strategy**:
   - Small gap: fine-tune last layers only
   - Medium gap: PEFT (LoRA/adapters)
   - Large gap: full domain adaptation with MMD loss
3. **Handle class imbalance**: Apply focal loss, class weights, or oversampling
4. **Validate cross-site**: Test on held-out clinical sites

## Common Pitfalls
- Domain shift between imaging devices/vendors causes performance drops
- Anatomical variation across populations not captured in source data
- Regulatory compliance requires model re-validation on target site

## Recent Papers (2026-05-05)
- **Imbalanced Classification under Capacity Constraints**: Long-tailed class distributions in medical datasets
- **MedSR-Vision**: Multi-domain medical image super-resolution (MRI, CT, X-ray, Ultrasound)
- **Dante**: Open source pre-training/fine-tuning tool for federated medical image segmentation
- **RKHS-MMD Domain Adaptation**: Robust unsupervised domain adaptation for medical image classification

## Related Skills
- physics-guided-neural-network
- quantum-ml-healthcare
- neuroscience
- quantum-kernel-medical-embeddings
