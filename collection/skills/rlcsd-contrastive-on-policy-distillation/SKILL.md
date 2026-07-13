---
name: rlcsd-contrastive-on-policy-distillation
description: Contrastive on-policy self-distillation methodology for reasoning models that mitigates privilege-induced style drift
trigger_words:
  - on-policy distillation
  - OPSD
  - reasoning distillation
  - contrastive distillation
  - privilege-induced style drift
  - RLCSD
version: 1.0.0
last_updated: 2026-06-13
source: arXiv:2606.11709v1
authors: Leyi Pan, Shuchang Tao, Yunpeng Zhai, Lingzhe Zhang, Zhaoyang Liu et al.
---

# RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation

## Problem Addressed

On-policy self-distillation (OPSD) aligns a model's distribution with its output under privileged context (verified solution). However, this creates **privilege-induced style drift**:
- Learning signal concentrates on style tokens (directness, brevity)
- Task-bearing tokens get less supervision
- Training destabilizes, response length shrinks

## Core Methodology

### Contrastive Principle
Contrast teacher-student gap under **correct hint** vs **wrong hint**:
- Suppresses style shift common to both conditions
- Concentrates signal on task-bearing tokens
- More discriminative for correctness

### Implementation Steps

1. **Setup OPSD baseline**
   - Teacher: model with privileged context (verified solution)
   - Student: model without privilege
   - Standard alignment: KL(student || teacher)

2. **Add contrastive component**
   ```
   loss = KL(student || teacher_correct) - KL(student || teacher_wrong)
   ```
   - teacher_correct: hint is verified solution
   - teacher_wrong: hint is incorrect solution

3. **Training procedure**
   - Generate hints (correct and wrong variants)
   - Compute both KL divergences
   - Subtract to isolate task-bearing signal
   - Combine with standard OPSD loss

### Key Insights

- **General principle**: Contrasting correct vs wrong hints suppresses shared style drift
- **Plug-and-play**: Can be integrated into existing OPSD methods
- **Cross-model extension**: Works for teacher-student distillation beyond self-distillation

## Experimental Validation

**Models tested**: Qwen3 (1.7B/4B/8B), Olmo-3-7B-Think
**Tasks**: Mathematical reasoning, logical reasoning
**Results**: Consistently outperforms GRPO and prior OPSD methods

## Use Cases

1. **Reasoning model training** - Improve token-level supervision quality
2. **LLM distillation** - Better signal for knowledge transfer
3. **Any OPSD variant** - Plug contrastive component into existing pipelines

## Practical Considerations

- Need verified solutions for correct hints
- Wrong hints should be plausible but incorrect
- Balance contrastive strength vs standard loss
- May need tuning for different task domains

## Related Methods

- GRPO (Group Relative Policy Optimization)
- Standard OPSD variants
- Cross-model on-policy distillation

## Limitations

- Requires access to verified solutions
- Wrong hints must be carefully constructed
- Computational overhead from dual-hint evaluation