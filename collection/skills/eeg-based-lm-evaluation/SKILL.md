---
name: eeg-based-lm-evaluation
description: Skill for evaluating language models using EEG signals to examine human-like next-word prediction behavior based on arXiv:2607.16549. Enables fine-grained analysis of cognitive plausibility of language models during reading comprehension tasks.
---
# EEG-Based Language Model Evaluation

## Overview
This skill encapsulates the methodology from arXiv:2607.16549, which proposes using EEG-recorded event-related potentials (ERPs) to evaluate the cognitive plausibility of language models during reading comprehension. The approach generates regressors based on information measures (top-1 prediction and surprisal) to predict ERP components, enabling fine-grained analysis of how well language models capture human linguistic processing.

## Core Concepts
- **Next-word predictability**: Both humans and language models exhibit predictability in word sequences during reading
- **ERP as cognitive signal**: Event-related potentials from EEG reflect different stages of cognitive processing
- **Information measures**: Top-1 prediction accuracy and surprisal (negative log probability) as predictors of ERP components
- **Surprisal correlation**: Surprisal potentially correlates with language-processing ERPs, especially for open-class words with high semantic content
- **Scaling limitations**: Increased model parameters and computational budgets do not consistently improve convergence with human-like linguistic processing

## Implementation Steps
1. **Data Collection**
   - Record EEG during reading comprehension tasks with millisecond resolution
   - Present identical text stimuli to human participants and language models
   - Extract event-related potentials (ERPs) time-locked to word onset

2. **Language Model Processing**
   - Generate probability distributions over vocabulary for each word context
   - Calculate top-1 prediction accuracy (correct prediction vs. actual word)
   - Compute surprisal as -log₂(P(word|context)) for each word

3. **Regressor Generation**
   - Create top-1 prediction regressor (binary: 1 if correct, 0 otherwise)
   - Create surprisal regressor (continuous: -log₂ probability)
   - Align regressors with EEG time series accounting for hemodynamic delay

4. **Statistical Modeling**
   - Perform linear regression: ERP amplitude ~ β₀ + β₁(top-1) + β₂(surprisal) + ε
   - Analyze coefficient significance and effect sizes
   - Examine topography and temporal dynamics of significant effects
   - Control for confounding variables (word length, frequency, etc.)

5. **Model Comparison**
   - Compare ERP prediction accuracy across different language model architectures
   - Evaluate impact of model size, training data, and architecture on neural alignment
  
   - Test whether scaling laws predict improved cognitive plausibility

6. **Validation**
   - Verify that only surprisal significantly correlates with language-processing ERPs
   - Confirm effects are stronger for open-class words with high semantic content
   - Check that prediction accuracy alone does not guarantee neural plausibility

## Verification
- Replicate the finding that surprisal correlates with N400 component (~200-500ms post-stimulus)
- Confirm top-1 prediction shows weaker or no correlation with ERP components
- Demonstrate that language model surprisal explains variance in ERP beyond control variables
- Validate that effects are modulated by word class (open vs. closed class words)

## References
- arXiv:2607.16549v1 - Encoding EEG Signals to Examine Human-Like Next-Word Prediction Behaviour in Language Models
- Supplementary material and code (if available) from the arXiv page.

## Notes
- This skill assumes familiarity with EEG preprocessing pipelines and ERP analysis
- Requires access to EEG equipment or existing datasets with reading paradigms
- Surprisal calculation requires language models that output full probability distributions
- The approach can be extended to other cognitive tasks beyond reading comprehension