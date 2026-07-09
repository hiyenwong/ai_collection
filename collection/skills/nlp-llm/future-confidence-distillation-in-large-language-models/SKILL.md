---
name: future-confidence-distillation-in-large-language-models
description: 'Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation dep. Based on arXiv:2607.07626.'
---

# Future Confidence Distillation in Large Language Models

**arXiv**: 2607.07626 | **Authors**: Sahil Kale | **Utility**: 0.85

## Overview

Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation depend on accurately estimating answer reliability. Existing approaches, however, largely treat confidence as a property of completed responses, overlooking how confidence-related information evolves throughout the answering process. In this work, we investigate confidence from a temporal perspective by comparing pre-solution Feeling-of-Knowing (FOK) and post-solution Judgement-of-Learning (JOL) confidence estimates across frontier and open-source LLMs. We show that post-solution confidence is consistently better calibrated and more discriminative than pre-solution confidence, while linear probes trained on hidden representations recover substantially richer confidence-related information than models explicitly verbalise. Building on this observation, we introduce future confidence distillation, which trains predictors operating on pre-solution hidden representations using teacher confidence estimates produced by post-solution correctness probes. Despite requiring only pre-solution representations for inference, distilled predictors recover much of the calibration improvement achieved by post-solution confidence, remain highly sample efficient, and transfer across datasets within the same domain. Together, our findings demonstrate that confidence-related information evolves throughout the answering process and can be anticipated before answer generation is complete, enabling significantly more reliable yet low-cost confidence estimation.

## Key Contributions

1. Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation depend on accurately estimating answer reliability.
2. Existing approaches, however, largely treat confidence as a property of completed responses, overlooking how confidence-related information evolves throughout the answering process.
3. In this work, we investigate confidence from a temporal perspective by comparing pre-solution Feeling-of-Knowing (FOK) and post-solution Judgement-of-Learning (JOL) confidence estimates across frontier and open-source LLMs.
4. We show that post-solution confidence is consistently better calibrated and more discriminative than pre-solution confidence, while linear probes trained on hidden representations recover substantially richer confidence-related information than models explicitly verbalise.

## Implementation Notes

- **Keywords**: llm, tool-use, rope-embedding
- **Categories**: cs.CL, cs.AI
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, tool-use, rope-embedding.
