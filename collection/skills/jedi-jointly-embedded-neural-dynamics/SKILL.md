---
name: jedi-jointly-embedded-neural-dynamics
version: 1.0.0
created: 2026-04-24
source: arXiv:2603.10489v1
categories: [q-bio.NC, cs.AI, cs.LG]
status: active
trigger: neural dynamics, RNN, embedding, motor cortex, multi-task, fixed points, eigenspectrum, monkey reaching, hierarchical model
description: "JEDI: Jointly Embedded Inference of Neural Dynamics"
---

# JEDI: Jointly Embedded Inference of Neural Dynamics

**arXiv**: [2603.10489v1](https://arxiv.org/abs/2603.10489v1)
**Authors**: Anirudh Jamkhandi, Ali Korojy, Olivier Codol, Guillaume Lajoie, Matthew G. Perich
**Published**: 2026-03-11
**Categories**: q-bio.NC, cs.AI, cs.LG

## Overview

Animal brains flexibly and efficiently achieve many behavioral tasks with a single neural network. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying neural populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental neural recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While recurrent neural networks (RNNs) directly constrained neural data have been effective in inferring underlying dynamical mechanisms, they are typically limited to single-task domains and struggle to generalize across behavioral conditions. Here, we introduce JEDI, a hierarchical model that captures neural dynamics across tasks and contexts by learning a shared embedding space over RNN weights. This model recapitulates individual samples of neural dynamics while scaling to arbitrarily large and complex datasets, uncovering shared structure across conditions in a single, unified model. Using simulated RNN datasets, we demonstrate that JEDI accurately learns robust, generalizable, condition-specific embeddings. By reverse-engineering the weights learned by JEDI, we show that it recovers ground truth fixed point structures and unveils key features of the underlying neural dynamics in the eigenspectra. Finally, we apply JEDI to motor cortex recordings during monkey reaching to extract mechanistic insight into the neural dynamics of motor control. Our work shows that joint learning of contextual embeddings and recurrent weights provides scalable and generalizable inference of brain dynamics from recordings alone.

## Methodology

### Core Architecture: JEDI

JEDI is a hierarchical model that captures neural dynamics across tasks and contexts by learning a shared embedding space over RNN weights.

### Key Innovation: Joint Embedding of RNN Weights

1. **Hierarchical Model Design**
   - Learns shared embedding space over RNN weight parameters
   - Captures both condition-specific and shared dynamical structure
   - Scales to arbitrarily large and complex datasets

2. **Context-Specific Embeddings**
   - Each behavioral condition gets a learned embedding
   - Embeddings modulate RNN dynamics to capture task-specific rules
   - Enables cross-task generalization and transfer

3. **Mechanistic Recovery**
   - Reverse-engineers learned weights to recover fixed point structures
   - Reveals eigenspectrum features of underlying neural dynamics
   - Provides interpretable mechanistic insights

### Validation Approach
- **Simulated RNN datasets**: Demonstrates accurate learning of robust, generalizable embeddings
- **Ground truth recovery**: Recovers known fixed point structures
- **Real neural data**: Applied to motor cortex recordings during monkey reaching
- **Scalability**: Handles multiple behavioral conditions in unified model

## Applications

- **Multi-task Neural Dynamics**: Infer dynamics across multiple behavioral conditions simultaneously
- **Motor Control Research**: Extract mechanistic insights into motor cortex dynamics
- **Scalable Neural Recording Analysis**: Handle large-scale, multi-condition datasets
- **Cross-condition Generalization**: Predict dynamics for novel behavioral conditions
- **Neuroscience Discovery**: Uncover shared vs. condition-specific dynamical structures

## Technical Details

### Input Specifications
- Neural signal modality and format appropriate to the methodology
- Sampling rate and temporal resolution requirements vary by application
- Spatial resolution depends on recording technique (EEG, fMRI, neural recording)

### Output Specifications
- Task-specific output format (forecasting, generation, control, decoding)
- Confidence/uncertainty estimates where applicable
- Interpretable representations for neuroscientific analysis

### Computational Requirements
- GPU recommended for training deep learning components
- Memory requirements scale with data dimensionality
- Real-time inference feasible for control and BCI applications

## Limitations & Considerations

- Model performance depends on data quality, quantity, and preprocessing
- Generalization across subjects, recording setups, and tasks may be limited
- Interpretability vs. performance trade-offs should be evaluated
- Biological plausibility assumptions should be validated experimentally

## References

- Original paper: arXiv:2603.10489v1 (2026-03-11)
- Tested on relevant neuroscience datasets as described in the paper

## Relevance to Other Skills

This methodology complements existing skills in brain signal processing, neural dynamics modeling, and computational neuroscience. Related skills include neural dynamics analysis, brain network construction, and neural decoding frameworks.
