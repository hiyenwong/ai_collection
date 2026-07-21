---
name: leveraging-unlabelled-neural-decoding
description: Skill for understanding and applying the MOJO framework for leveraging unlabeled data in neural population decoding via masked autoencoding and joint supervised learning.
activation: leveraging unlabelled neural decoding, MOJO framework, SSL for neural decoding
---
# Leveraging Unlabelled Data for Generalizable Neural Population Decoding

## Overview
This skill summarizes the MOJO (Masked autoencoder-based Joint training) framework introduced in arXiv:2607.14086v1. MOJO combines self-supervised learning (SSL) via masked autoencoding with supervised learning (SL) to train spike-tokenizing models for neural population decoding. It enables the use of unlabeled neural data across tasks and species, improving performance in label-scarce scenarios and yielding more interpretable neuronal representations.

## Core Concepts
- **Spike-tokenizing models**: Convert raw spike trains into discrete token sequences, enabling sequence modeling techniques.
- **Masked Autoencoding (MAE)**: A self-supervised objective where random tokens are masked and the model learns to reconstruct them, capturing rich spatiotemporal dependencies.
- **Joint Training**: MOJO optimizes a combined loss: L = λ * L_SSL + (1-λ) * L_SL, balancing representation learning and task-specific prediction.
- **Generalization**: By leveraging unlabeled data, MOJO learns robust features that transfer across sessions, subjects, and even modalities (e.g., to human ECoG).

## Methodology
1. **Tokenization**: Convert spike trains into discrete tokens using a learned vector-quantized variational autoencoder (VQ-VAE) or similar discretization.
2. **Masking**: Randomly mask a proportion (e.g., 15-40%) of tokens in the input sequence.
3. **SSL Objective**: Predict the masked tokens using an autoregressive or bidirectional transformer encoder-decoder.
4. **SL Objective**: Predict behavioral labels (e.g., movement direction, stimulus identity) from the latent representations.
5. **Optimization**: Jointly minimize the weighted sum of SSL and SL losses.
6. **Evaluation**: Assess decoding performance, robustness to limited labels, and interpretability via auxiliary tasks (brain region classification, spike-statistics prediction).

## Steps to Apply
1. **Prepare Spike Data**: Sort and bin spike trains into time bins (e.g., 10-50 ms) to create binned spike count matrices.
2. **Tokenize**: Train a tokenizer (e.g., VQ-VAE) on binned spike data to map sequences to discrete token IDs.
3. **Mask Tokens**: Randomly mask tokens in the tokenized sequences during training.
4. **Build Model**: Use a transformer-based architecture (encoder for context, decoder for reconstruction; optionally a prediction head for SL).
5. **Define Losses**:
   - SSL: Cross-entropy between predicted and actual masked tokens.
   - SL: Task-appropriate loss (e.g., cross-entropy for classification, MSE for regression).
   - Combined: L = α * L_SSL + (1-α) * L_SL (α typically 0.5).
6. **Train**: Optimize end-to-end on labeled and unlabeled data batches.
7. **Evaluate**: Test decoding accuracy on held-out labeled sessions; probe representational quality via downstream tasks.

## Pitfalls
- **Tokenization Quality**: Poor tokenization limits downstream performance; ensure the tokenizer captures sufficient spike-train variability.
- **Masking Ratio**: Too high masking reduces SSL signal; too low reduces regularization. Tune via validation.
- **Balancing α**: Imbalanced weighting can cause one objective to dominate; monitor both losses.
- **Generalization Gap**: Validate that SSL pretraining indeed improves few-shot adaptation, not just overall accuracy.
- **Modality Shift**: When applying to new modalities (e.g., ECoG), re-tokenize or fine-tune the tokenizer.

## References
- Primary paper: X. Mao et al., "Leveraging unlabelled data for generalizable neural population decoding", arXiv:2607.14086v1, 2026.
- Related works: Masked Autoencoders for vision (He et al., 2021), SpikeGPT (unknown), Neural Decoding literature.

## Activation Examples
- `leveraging unlabelled neural decoding`
- `MOJO framework neural decoding`
- `SSL for spike-tokenizing models`