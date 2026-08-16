---
name: simple-opd-on-policy-distillation
description: "Simple-OPD for OPD warm-up with LoRA and teacher CoT."
---

# Simple-OPD: Demystifying Warm-up for On-policy Distillation

## Overview
Simple-OPD is a plug-and-play initialization method for on-policy distillation (OPD) that addresses the critical warm-up stage before OPD training. The method warms up the student model on teacher-generated chain-of-thought (CoT) supervision using low-rank adaptation (LoRA) before proceeding to full OPD.

## Key Insights
- **Data Perspective**: Effective warm-up relies on teacher-compatible CoT supervision, not just correct answers. Even incorrect teacher rollouts provide comparable benefits to correct ones, suggesting warm-up primarily transfers thinking patterns rather than factual correctness.
- **Training Perspective**: LoRA with near-saturation training duration better balances in-domain adaptation and out-of-distribution generalization compared to full-parameter supervised fine-tuning (SFT).

## Implementation Steps
1. **Generate Teacher Rollouts**: Use the teacher model to generate CoT rollouts for the training dataset
2. **Warm-up with LoRA**: Train the student model using LoRA on the teacher-generated CoT data until near-saturation (typically 80-90% of full convergence)
3. **Proceed to OPD**: Switch to standard on-policy distillation using the warmed-up student as initialization
4. **Token-level Supervision**: Apply token-level supervision from teacher models during OPD phase

## Best Practices
- Use teacher-compatible CoT supervision even if some rollouts contain errors
- Avoid full-parameter SFT during warm-up; LoRA provides better generalization
- Monitor training saturation to avoid overfitting during warm-up phase
- Ensure sufficient warm-up duration for effective pattern transfer

## Use Cases
- Large Language Model distillation
- Chain-of-thought reasoning transfer
- Efficient fine-tuning of student models
- Cross-model knowledge distillation

## Activation Keywords
simple-opd, on-policy distillation, warm-up, chain-of-thought, LoRA, teacher-student, knowledge distillation

## References
- arXiv: [2608.06802v1](https://arxiv.org/abs/2608.06802v1)
- Original paper: "Simple-OPD: Demystifying Warm-up for On-policy Distillation"