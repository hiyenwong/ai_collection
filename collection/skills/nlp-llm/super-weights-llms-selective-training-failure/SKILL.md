---
name: super-weights-llms-selective-training-failure
description: "Shows that Super Weight pruning degradation doesn't universally apply. Training Super Weights in isolation drops accuracy to random-guessing. Parameter importance ≠ trainability. Vanilla LoRA with 0.16% parameters succeeds. Activation: super weights, LLM training, parameter pruning, critical parameters, selective training."
metadata:
  arxiv_id: "2607.08733"
  published: "2026-07-09"
  authors: "Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag"
  tags: [super-weights, llm-training, parameter-pruning, critical-parameters, selective-training]
---

# Super Weights in LLMs and the Failure of Selective Training

## Overview

Recent work identified Super Weights — individual parameters whose removal degrades LLM performance by orders of magnitude. This paper shows that pruning degradation doesn't universally apply to all LLMs, and more importantly, that parameter importance does not imply parameter trainability in isolation. Training Super Weights selectively fails catastrophically.

## Key Innovations

### Non-Universal Pruning Degradation
- Super Weight pruning degradation does not apply to all LLMs
- Challenges the universality of Super Weight importance

### Selective Training Failure
- Training Super Weights in isolation (100-8,192 parameters) drops accuracy to random-guessing
- Expanding to local neighborhoods (up to 36K parameters) provides no improvement
- Failure is specific to Super Weight coordinates, not sparsity itself

### Random Position Control
- Training equal number of randomly chosen positions in same layers improves over baseline
- Confirms the collapse comes from targeting Super Weights, not from sparsity

### LoRA Success
- Vanilla LoRA (updating every position via low-rank structure) succeeds with 0.16% of parameters
- Applying same low-rank update to down_proj succeeds as well
- 10-seed ablation confirms: constraining LoRA at Super Weight positions yields no benefit

## Methodology

1. **Pruning Analysis**: Test Super Weight pruning across multiple LLMs (OLMo-1B, OLMo-7B)
2. **Selective Training**: Train Super Weight parameters in isolation and neighborhoods
3. **Random Control**: Train randomly selected positions for comparison
4. **LoRA Experiments**: Test vanilla LoRA and Super Weight-constrained LoRA
5. **Statistical Validation**: 10-seed ablation for statistical significance

## Implications

- Parameter importance ≠ parameter trainability in isolation
- Effective fine-tuning relies on structured decompositions over entire layers
- Targeting individually important weights is counterproductive
- Low-rank structure over full layers is the key to efficient fine-tuning

## Pitfalls

- Findings specific to OLMo models — may not generalize to all architectures
- Super Weight definition and identification method affects results
- Isolated training setup may not reflect practical fine-tuning scenarios
- 10-seed ablation may be insufficient for some statistical claims

## Activation Keywords

super weights, LLM training, parameter pruning, selective training, LoRA, low-rank adaptation, parameter importance, trainability, OLMo, fine-tuning

## Paper Reference

arXiv:2607.08733 - "Super Weights in LLMs and the Failure of Selective Training" (Jul 2026)
