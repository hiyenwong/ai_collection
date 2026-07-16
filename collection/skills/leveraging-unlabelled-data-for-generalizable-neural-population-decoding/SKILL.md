---
name: leveraging-unlabelled-data-for-generalizable-neural-population-decoding
description: Skill for understanding and applying the research from arXiv:2607.14086 "Leveraging unlabelled data for generalizable neural population decoding"
category: ai_collection
---

# leveraging-unlabelled-data-for-generalizable-neural-population-decoding

## Paper Information
- **Title**: Leveraging unlabelled data for generalizable neural population decoding
- **arXiv ID**: 2607.14086
- **Authors**: Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo, Matthew G. Perich, Guillaume Lajoie
- **Published**: 2026-07-16 (based on arXiv listing)
- **Subjects**: Machine Learning (cs.LG); Neurons and Cognition (q-bio.NC)
- **Comments**: Not specified in the arXiv listing

## Core Concepts

### MOJO Framework
The paper introduces MOJO (Masked autoEncoder-based Joint training), a training framework for spike-tokenizing models that jointly leverages self-supervised learning (SSL) via masked autoencoding and supervised learning (SL) objectives.

### Key Findings
1. Current spike-based models are restricted to supervised learning, limiting training to datasets with paired behavioral labels
2. MOJO combines SSL (via masked autoencoding) with SL objectives to improve decoding performance
3. MOJO demonstrates superior performance over purely SL-trained models, especially with limited labeled data
4. SSL yields more interpretable neuronal representations, improving performance on brain region classification and spike-statistics prediction
5. MOJO generalizes beyond spiking data to human electrocorticography during speech, achieving performance comparable to neuro-foundation models
6. Augmenting spike-tokenizing models with SSL improves performance in label-impoverished settings and enables use of unlabelled data across tasks and species

### Technical Approach
- **Spike Tokenization**: Converting neural spike trains into discrete tokens for modeling
- **Masked Autoencoding**: Self-supervised objective where portions of the spike token sequence are masked and the model predicts them
- **Joint Training**: Combining the SSL reconstruction loss with supervised decoding loss
- **Cross-modal Generalization**: Demonstrating that the learned representations transfer to other neural modalities (e.g., ECoG)

## Applications in Agent Design
1. **Robust Neural Decoding**: Build more resilient brain-computer interface decoders that work with limited labeled data
2. **Self-supervised Pretraining**: Use large amounts of unlabeled neural data to pretrain decoding models
3. **Cross-task Generalization**: Develop neural representations that transfer across different behavioral tasks and species
4. **Interpretable Representations**: Learn neural representations that are meaningful for understanding brain function
5. **Multi-modal Integration**: Combine spike-based models with other neural signal types (EEG, ECoG, fMRI) through shared latent spaces

## Implementation Guidelines
For implementing MOJO-like approaches in neural decoding systems:

1. **Tokenization Pipeline**: Convert neural spike trains into discrete token sequences using methods like spike sorting or feature extraction
2. **Masking Strategy**: Implement random masking of tokens during training (typically 15-50% masking rate)
3. **Autoencoder Architecture**: Use transformer-based or recurrent architectures capable of sequence modeling
4. **Joint Loss Function**: Combine reconstruction loss (SSL) with prediction loss (SL) using appropriate weighting
5. **Pre-training Strategy**: Pre-train on large unlabeled datasets, then fine-tune on limited labeled data for specific tasks
6. **Evaluation Metrics**: Measure decoding accuracy, representation interpretability, and cross-task generalization

## Activation Keywords
unlabelled data, neural population decoding, MOJO, masked autoencoding, self-supervised learning, spike-tokenizing models, brain-computer interface, neural representation learning, computational neuroscience

## References
- arXiv:2607.14086 - Leveraging unlabelled data for generalizable neural population decoding
- Related work on self-supervised learning for neural data, masked autoencoding, and brain-computer interfaces