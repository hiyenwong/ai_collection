---
name: illusion-of-equivalency-quantization-effects-llms
description: "Shows that post-training quantization evaluation via accuracy/perplexity fails to capture behavioral changes. Introduces correctness agreement metric. Reveals non-linear breakpoints at low bit-widths. Query/key projections more sensitive than value/output. Activation: quantization, LLM deployment, behavioral change, correctness agreement, post-training quantization."
metadata:
  arxiv_id: "2607.08734"
  published: "2026-07-09"
  authors: "Baha Rababah, Cuneyt Gurcan Akcora, Carson K. Leung"
  tags: [quantization, llm-deployment, behavioral-change, correctness-agreement, post-training-quantization]
---

# The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs

## Overview

Post-training quantization is widely used to deploy LLMs in resource-constrained settings, yet its evaluation relies almost exclusively on accuracy and perplexity. This paper shows that these metrics fail to capture behavioral changes induced by quantization, introducing "correctness agreement" as a decision-level metric that reveals the illusion of equivalency between base and quantized models.

## Key Innovations

### Correctness Agreement Metric
- Decision-level metric measuring overlap in correct predictions between base and quantized models
- Independent of absolute accuracy
- Reveals behavioral divergence even when task performance appears preserved

### Behavioral Divergence Under Quantization
- Divergence emerges under moderate quantization (not just extreme)
- Multiple models and quantization schemes tested (8-bit to 2-bit)
- Standard metrics (accuracy, perplexity) miss these behavioral changes

### Layer-Wise Sensitivity Analysis
- Quantization analyzed as structural operator on attention weights
- Statistical and distributional measures of layer-wise distortions
- Non-linear breakpoints identified at low bit-widths
- Query and key projections consistently more sensitive than value and output projections

## Methodology

1. **Quantization**: Apply multiple schemes from 8-bit to 2-bit
2. **Correctness Agreement**: Measure prediction overlap between base and quantized
3. **Layer Analysis**: Quantify distortions per layer using statistical measures
4. **Sensitivity Ranking**: Compare Q, K, V, O projection sensitivity
5. **Breakpoint Detection**: Identify non-linear behavioral change points

## Implications

- Accuracy and perplexity are insufficient for quantization evaluation
- Behavioral evaluation reveals hidden degradation in quantized models
- Layer-wise sensitivity analysis guides targeted quantization strategies
- Protecting Q/K projections while relaxing V/O can preserve behavior

## Pitfalls

- Correctness agreement is binary and may miss nuanced behavioral differences
- Analysis limited to attention weights — other components (FFN, embeddings) not analyzed
- Specific models and quantization schemes may not generalize
- No proposed mitigation strategy — purely diagnostic

## Activation Keywords

quantization, LLM deployment, behavioral change, correctness agreement, post-training quantization, attention weight distortion, layer sensitivity, Q/K projections, evaluation metrics

## Paper Reference

arXiv:2607.08734 - "The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs" (Jul 2026)
