---
name: opd2-on-policy-delta-distillation
description: OPD² for on-policy delta distillation.
trigger_words: [opd2, on-policy delta distillation, multilingual math reasoning]
---

# On-Policy Delta Distillation (OPD²)

## Overview
On-Policy Delta Distillation (OPD²) is an advanced variant of On-Policy Distillation (OPD) that uses the probability gap between a post-trained teacher and its base model as the learning signal. It shows particularly strong improvements in multilingual mathematical reasoning, especially for Korean and Japanese, and helps narrow the English-Korean performance gap.

## Key Features
- **Delta-based learning signal**: Uses probability gap between teacher and base model
- **Multilingual effectiveness**: Strong improvements in Korean and Japanese
- **Performance gap reduction**: Narrows English-Korean performance gap
- **Language preservation**: Maintains target-language responses better than English-only OPD

## When to Use
- For multilingual mathematical reasoning tasks
- When working with LLMs like Qwen3 for cross-lingual transfer
- To improve reasoning performance in low-resource languages
- When standard OPD is insufficient for multilingual settings

## Implementation Steps
1. **Prepare models**: Have both post-trained teacher and base model available
2. **Compute probability gaps**: Calculate difference in token probabilities between teacher and base
3. **Apply delta distillation**: Use probability gaps as learning signals during distillation
4. **Use multilingual data**: Ensure training data includes target languages to preserve responses
5. **Evaluate cross-lingual performance**: Test on multiple languages and difficulty levels
6. **Compare with baselines**: Benchmark against original OPD and other methods

## Pitfalls to Avoid
- **English-only training**: Can shift responses toward English, losing target language characteristics
- **Insufficient multilingual data**: May not preserve target-language response patterns
- **Base model quality**: Poor base model will affect delta signal quality

## Verification
- Measure performance improvement in target languages (Korean, Japanese)
- Compare English-Korean performance gap before and after
- Analyze response language distribution to ensure target language preservation

## References
- arXiv: 2608.05802v1
- Authors: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- Published: 2026-08-06