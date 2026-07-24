---
name: arxiv-2607-14086
description: Skill generated from arXiv paper 2607.14086: Leveraging unlabelled data for generalizable neural population decoding
category: neuroscience
---

# arxiv-2607-14086

## Paper Information
- **Title**: Leveraging unlabelled data for generalizable neural population decoding
- **Authors**: Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo, Matthew G. Perich, Guillaume Lajoie
- **arXiv ID**: 2607.14086
- **Published**: 2026-07-15T17:58:00Z
- **Abstract**: Robust and accurate neural decoders are integral to neurotechnologies such as brain-computer interfaces and closed-loop experiments. Recent work has shown that tokenizing neural data at the spike level facilitates multi-session pretraining and delivers state-of-the-art decoding performance. However, current spike-based models are restricted to supervised learning (SL), limiting training to datasets with paired behavioural labels. To address this limitation, we introduce MOJO (Masked autOencoder-based JOint training), a training framework for spike-tokenizing models that jointly leverages self-supervised learning (SSL) via masked autoencoding and SL objectives. We evaluate MOJO on three spiking datasets spanning monkey motor cortex during reaching tasks and multi-regional mouse recordings during vision and decision making tasks, demonstrating superior performance over purely SL-trained models. This improvement is especially pronounced when training with limited labelled data, particularly in few-shot finetuning, where only a small amount of labelled data from a new session is available. Incorporating SSL also yields more interpretable neuronal representations, improving performance on brain region classification and spike-statistics prediction without explicit optimization for these tasks. We further show that MOJO generalizes beyond spiking data to human electrocorticography during speech, where it continues to outperform purely SL-trained models and achieves performance comparable to neuro-foundation models (NFMs) designed specifically for continuous signals. Overall, augmenting spike-tokenizing models with SSL improves performance in label-impoverished settings and enables the use of unlabelled data across various tasks and species, while generalizing to other neural modalities. These results suggest a path towards more flexible and scalable data usage when training NFMs.

## Core Ideas
1. **MOJO Framework**: Masked autoencoder-based joint training that combines self-supervised learning (SSL) via masked autoencoding with supervised learning (SL) objectives for spike-tokenizing models
2. **SSL Enhances SL**: Adding SSL objectives to spike-tokenizing models improves decoding performance, especially in label-impoverished settings
3. **Cross-Modality Generalization**: MOJO-trained models generalize beyond spiking data to other neural modalities like human electrocorticography
4. **Interpretable Representations**: SSL leads to more interpretable neuronal representations that improve performance on auxiliary tasks like brain region classification

## Key Contributions
- Introduces MOJO, a framework for jointly training spike-tokenizing models with SSL and SL objectives
- Demonstrates superior performance over purely SL-trained models on multiple spiking datasets
- Shows particular benefit in few-shot fine-tuning scenarios with limited labeled data
- Demonstrates generalization to human electrocorticography during speech tasks
- Provides a path toward more flexible and scalable neural field model training

## Methodology
- **Spike Tokenization**: Neural data is tokenized at the spike level to enable multi-session pretraining
- **Masked Autoencoder (MAE) Component**: Uses masked autoencoding as the SSL objective, where patches of spike tokens are masked and the model learns to reconstruct them
- **Supervised Learning Component**: Traditional decoding loss for predicting behavioral labels from neural activity
- **Joint Training**: Both SSL and SL objectives are optimized simultaneously
- **Evaluation**: Tested on three spiking datasets (monkey motor cortex, multi-regional mouse recordings) and human electrocorticography

## Potential Applications
- Brain-computer interfaces with limited calibration data
- Cross-session neural decoding without extensive retraining
- Neuroscience research requiring generalization across subjects/species
- Neurotechnology applications where labeled data is scarce or expensive to obtain
- Pre-training foundation models for neural data using large unlabeled datasets

## Activation Keywords
- neural decoding, spike sorting, motor cortex, electrocorticography, self-supervised learning, masked autoencoding, brain-computer interface, few-shot learning, neural population dynamics, motor cortex, vision tasks, decision making

## How to Use This Skill
This skill provides a framework for understanding and applying the MOJO approach to neural decoding problems. When working with neural spike data:
1. Consider tokenizing your neural data at the spike level
2. Implement a masked autoencoder objective alongside your supervised decoding objective
3. Evaluate performance improvements in low-label regimes
4. Explore cross-modal generalization to other neural signal types
5. Use the approach to build more robust and generalizable neural decoders

## References
- [arXiv:2607.14086](https://arxiv.org/abs/2607.14086)
- Mao, X., Krishna, N. H., Ryoo, A. H.-W., Perich, M. G., & Lajoie, G. (2026). Leveraging unlabelled data for generalizable neural population decoding. arXiv preprint arXiv:2607.14086.