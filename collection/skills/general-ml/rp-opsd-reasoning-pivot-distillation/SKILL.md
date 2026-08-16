---
name: rp-opsd-reasoning-pivot-distillation
description: RP-OPSD for reasoning-pivot-guided distillation.
trigger_words: [rp-opsd, reasoning pivot distillation, multilingual reasoning transfer]
---

# RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation

## Overview
RP-OPSD (Reasoning-Pivot-guided On-Policy Self-Distillation) is a method for multilingual reasoning transfer that concentrates privileged distillation around reasoning pivots - decisions that advance or redirect the reasoning process and shape subsequent inference. It uses distributional shift between matched teacher views with and without an English reference solution as an operational proxy to guide privileged distillation.

## Key Features
- **Reasoning pivot focus**: Concentrates distillation on tokens that control reasoning flow
- **Multilingual transfer**: Effective across 17 languages and multiple difficulty levels
- **Reference anchoring**: Uses English reference solutions to guide distillation
- **Operational proxy**: Uses distributional shift as proxy for reasoning importance

## When to Use
- When extending LLM reasoning capabilities to low-resource languages
- For mathematical reasoning tasks in multilingual settings
- When you want to improve cross-lingual reasoning transfer
- For on-policy self-distillation with explicit reasoning signal prioritization

## Implementation Steps
1. **Identify reasoning pivots**: Use distributional shift between teacher views as proxy
2. **Set up teacher models**: Create matched teacher views with/without English reference
3. **Compute distributional shift**: Measure differences in token distributions
4. **Apply weighted distillation**: Concentrate privileged distillation on high-shift tokens
5. **Implement reference anchoring**: Use English references to guide target language generation
6. **Evaluate multilingual performance**: Test across multiple languages and difficulty levels

## Pitfalls to Avoid
- **Surface vs reasoning tokens**: Ensure distillation focuses on reasoning-control tokens, not surface realization
- **Language drift**: Prevent target language responses from shifting toward English
- **Reference quality**: Ensure English reference solutions are high-quality and relevant

## Verification
- Compare against standard OPSD and other multilingual baselines
- Analyze token-level distillation weights to confirm reasoning pivot focus
- Measure performance gap reduction between high-resource and low-resource languages

## References
- arXiv: 2608.06347v1
- Authors: Xinye Wang, Junxiao Liu, Shujian Huang
- Published: 2026-08-06
- Code: https://github.com/NJUNLP/RP-OPSD