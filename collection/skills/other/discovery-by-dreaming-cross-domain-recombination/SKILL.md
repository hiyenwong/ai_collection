---
name: discovery-by-dreaming-cross-domain-recombination
description: "A skill for implementing cross-domain recombination inspired by dreaming, based on the paper \"Discovery by Dreaming: Cross-Domain Recombination in Artificial Memory\" (arXiv:2607.16256). This skill outlines how to implement a LoRA fine-tuning pipeline (DREAMS) and a symbolic engine (SAPIENCE) to recombine knowledge across domains, enhancing AI discovery and insight generation."
activation: discovery by dreaming, cross-domain recombination, dream-inspired AI, memory consolidation AI
---
# Discovery by Dreaming: Cross-Domain Recombination in Artificial Memory

## Overview
This skill implements the methodology from arXiv:2607.16256, which proposes that dreaming (offline recombination of experiences) is not merely for memory consolidation but for discovering novel cross-domain connections. The approach consists of two complementary systems:
1. **DREAMS**: A LoRA fine-tuning pipeline that recombines neural network weights.
2. **SAPIENCE**: A symbolic engine that replays structured knowledge objects.

Both systems generate cross-domain associations that improve performance on tasks requiring transfer learning, such as unseen math reasoning.

## Core Concepts
- **Recombination vs. Rehearsal**: Within-domain rehearsal does not yield discovery; cross-domain recombination does.
- **Substrate-General**: The principle applies across neural networks and symbolic systems.
- **Falsifiable Prediction**: Hippocampal recordings can distinguish recombination from rehearsal.

## Implementation Steps

### 1. DREAMS (LoRA Fine-Tuning Pipeline)
1. **Prepare Dataset**: Collect a diverse corpus spanning multiple domains (e.g., math, language, science).
2. **LoRA Configuration**: Apply Low-Rank Adaptation to the target model (e.g., LLaMA, Mistral).
3. **Recombination Objective**: During training, sample batches that mix examples from different domains to encourage cross-domain weight updates.
4. **Training Loop**: Train for a limited number of epochs, ensuring the model does not overfit to any single domain.
5. **Evaluation**: Test on tasks requiring cross-domain transfer (e.g., GSM8K for math reasoning) and compare to baseline.

### 2. SAPIENCE (Symbolic Engine)
1. **Knowledge Representation**: Encode knowledge as structured objects (e.g., semantic triples, frames).
2. **Replay Mechanism**: Periodically activate a recombination process that randomly pairs knowledge objects from different domains.
3. **Composition Rule**: Define how to combine objects (e.g., concatenation, property transfer, analogy mapping).
4. **Output Generation**: Generate novel hybrid concepts and evaluate their usefulness via downstream tasks or human judgment.

## Validation
- **Quantitative**: Measure improvement on benchmark tasks (e.g., +21 pp for symbolic arm, +5.64 pp overall for neural arm, +14.5 pp on cross-domain subtasks).
- **Qualitative**: Assess novelty and usefulness of generated combinations.
- **Neuroscience Alignment**: Predict hippocampal replay patterns that favor cross-domain co-activation.

## Usage Notes
- Ensure computational resources for LoRA training (GPU memory).
- For symbolic engine, define a clear knowledge schema and recombination operators.
- Combine both approaches for synergistic effects.

## References
- arXiv:2607.16256 - Discovery by Dreaming: Cross-Domain Recombination in Artificial Memory

## Activation Keywords
dreaming, recombination, cross-domain, memory consolidation, LoRA, symbolic AI, neuroscience-inspired AI