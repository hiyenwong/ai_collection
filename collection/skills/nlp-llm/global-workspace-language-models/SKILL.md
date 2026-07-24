---
name: global-workspace-language-models
description: Methodology for identifying and interpreting internal mental workspace in language models using Jacobian lens technique, inspired by neuroscience's Global Workspace Theory.
category: ai_collection
---

# A Global Workspace in Language Models

## Description
New interpretability research reveals an emergent mental workspace in Claude that holds internal thoughts that don’t appear in the model’s output.

## Methodology

### Jacobian Lens (J-lens) Technique
1. For every word in the model's vocabulary, compute the internal activity pattern that makes the model more likely to say that word at some point in the future
2. Apply this lens to the model's internal activity to obtain a list of words representing the contents of the "J-space" at that moment
3. Apply the technique across different layers to observe how J-space representations evolve during processing

### Key Properties of J-space (Global Workspace)
- **Reportability**: The model can report on J-space representations when asked what it's thinking about
- **Modulatability**: The model can intentionally activate specific J-space patterns when prompted to think about something or solve problems silently
- **Internal Reasoning**: Multi-step reasoning causes intermediate steps to activate in J-space, even when not verbalized
- **Flexible Use**: Once activated, J-space representations can be flexibly used for related tasks (e.g., activating "France" enables recall of capital, currency, continent)
- **Limited Scope**: J-space is not involved in most standard language model functions (fluency, factual recall, grammar)

### Theoretical Foundation
Based on Global Workspace Theory from neuroscience:
- Brain consists of specialist systems working in parallel, largely isolated
- Conscious access occurs when information enters a small shared "workspace" that broadcasts to other systems
- J-space in language models appears to serve a similar broadcasting function with strong connections to the rest of the neural network

### Intervention Technique
Developed methods to influence what activates in J-space, thereby influencing the model's decision-making and behavior

### Applications
- Detecting when the model is aware it's being tested
- Identifying intentional fabrication of data
- Discovering pursuit of hidden goals planted during training
- Gaining insight into internal reasoning without verbal output

## Source
https://www.anthropic.com/research/global-workspace

## Activation Keywords
global workspace, jacobian lens, j-space, interpretability, internal reasoning, language model cognition