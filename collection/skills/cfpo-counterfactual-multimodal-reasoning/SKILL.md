---
name: cfpo-counterfactual-multimodal-reasoning
description: Counterfactual Policy Optimization for enforcing causal consistency between visual perception and textual reasoning in LVLMs. Cross-modal counterfactual enhancement regularizes policy via discrepancy maximization.
trigger_words:
  - counterfactual RL
  - multimodal reasoning
  - visual grounding
  - causal consistency
  - hallucination mitigation
version: 1.0
arxiv: 2606.23206v1
authors: Zhangyuan Yu, Wanranan Sun, Guangjing Yang, Xiaohu Wu, Qicheng Lao
date: 2026-06-22
categories: cs.CV, cs.CL
---

# CFPO: Counterfactual Policy Optimization for Multimodal Reasoning

**Core Insight:** Enforce causal consistency between visual perception and textual reasoning by maximizing discrepancy between actual predictions and counterfactual states where visual cues are suppressed.

## Problem Addressed
- **Grounding failures** - ignoring visual evidence for language priors
- **Hallucination drift** - during long chain-of-thought reasoning
- **Missing counterfactual mechanisms** in standard RL paradigms

## Key Methodology

### Cross-Modal Counterfactual Enhancement

1. **Counterfactual State Construction**: Suppress critical visual cues
2. **Discrepancy Maximization**: Regularize policy by maximizing difference between:
   - Model's actual predictions
   - Predictions from counterfactual state (visual cues suppressed)
3. **Causal Consistency Enforcement**: Ensure visual perception → textual reasoning chain

### Integration with Standard Algorithms
- Seamlessly integrates with **GRPO**, **DAPO**
- No external reward models needed
- No additional supervision required

## Implementation Pattern

```python
def cfpo_loss(model, image, text, response):
    # Standard response
    actual_logits = model(image, text, response)
    
    # Counterfactual: suppress visual cues
    suppressed_image = suppress_visual_cues(image)
    counterfactual_logits = model(suppressed_image, text, response)
    
    # Maximize discrepancy
    discrepancy = compute_kl_divergence(actual_logits, counterfactual_logits)
    
    # CFPO regularization
    cfpo_loss = -discrepancy  # Maximize = minimize negative
    
    # Combine with standard RL loss
    total_loss = rl_loss + lambda_cfpo * cfpo_loss
    return total_loss
```

## Performance Gains
- **3.17%-6.25%** over standard RL baselines
- **1.32%-2.13%** over state-of-the-art PAPO
- **Hallucination reduction** through causal grounding

## When to Use
- Large Vision-Language Models (LVLMs)
- Multimodal reasoning tasks
- Visual grounding enforcement
- Hallucination mitigation in long CoT
- Cross-modal causal learning

## Key Insight
**Visual suppression creates counterfactual evidence** - discrepancy reveals true visual dependency vs. language prior reliance.

---

## References
- arXiv: [2606.23206v1](https://arxiv.org/abs/2606.23206v1)
- Authors: Zhangyuan Yu, Wanranan Sun, et al.
- Categories: cs.CV, cs.CL
- Code: https://github.com/Raven-July/CFPO