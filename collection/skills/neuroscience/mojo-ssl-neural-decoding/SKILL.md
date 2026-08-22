---
name: mojo-ssl-neural-decoding
description: MOJO (Masked autOencoder-based JOint training) framework for leveraging unlabelled neural data via self-supervised learning combined with supervised objectives. Enables robust neural population decoding with limited labelled data across species and modalities.
---

# MOJO SSL Neural Decoding

MOJO (Masked autOencoder-based JOint training) is a training framework for spike-tokenizing models that jointly leverages self-supervised learning (SSL) via masked autoencoding and supervised learning (SL) objectives.

## Use when

- Training neural decoders with limited labelled behavioral data
- Working with multi-session neural recording datasets across species
- Needing few-shot fine-tuning capabilities for new experimental sessions
- Building neuro-foundation models that generalize across neural modalities (spiking to continuous signals like ECoG)

## Core methodology

1. **Spike tokenization**: Convert neural spiking data into discrete tokens at the individual spike level
2. **Joint training objective**: Combine masked autoencoding (SSL) with supervised behavioral prediction (SL)
3. **Multi-session pretraining**: Pretrain on large unlabelled datasets, then fine-tune on small labelled datasets
4. **Cross-species generalization**: Framework works across monkey motor cortex, mouse multi-regional recordings, and human ECoG

## Key benefits

- Superior performance over purely supervised models, especially with limited labelled data
- Enhanced few-shot fine-tuning capabilities for new sessions
- More interpretable neuronal representations (improved brain region classification)
- Generalization beyond spiking data to continuous neural signals (ECoG during speech)
- Comparable performance to specialized neuro-foundation models despite broader applicability

## Implementation steps

1. **Data preprocessing**: Tokenize neural spiking data at spike level using established methods
2. **Model architecture**: Implement transformer-based architecture with masked autoencoding capability
3. **Joint loss function**: Combine reconstruction loss (SSL) with behavioral prediction loss (SL)
4. **Pretraining**: Train on large unlabelled datasets across multiple sessions/species
5. **Fine-tuning**: Adapt to specific tasks with limited labelled data from target sessions

## Evaluation metrics

- Behavioral decoding accuracy (primary task performance)
- Brain region classification accuracy (representation interpretability)
- Spike statistics prediction quality
- Cross-modal transfer performance (spiking → ECoG)
- Few-shot learning curves with varying amounts of labelled data

## Pitfalls to avoid

- Ensure proper spike tokenization that preserves temporal structure
- Balance SSL and SL loss weights appropriately for your specific dataset
- Account for session-specific variability when pretraining across multiple recordings
- Validate cross-species generalization carefully as neural coding principles may differ

## References

- Original paper: "Leveraging unlabelled data for generalizable neural population decoding" (arXiv:2607.14086)
- Related work: Spike-tokenizing models, neuro-foundation models, masked autoencoders in neuroscience

## Activation keywords

MOJO, masked autoencoder, self-supervised neural decoding, spike tokenization, few-shot neural decoding, neuro-foundation models, joint SSL-SL training