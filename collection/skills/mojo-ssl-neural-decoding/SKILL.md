---
name: mojo-ssl-neural-decoding
description: MOJO (Masked autOencoder-based JOint training) framework for decoding neural population activity using self-supervised learning with unlabelled data. Use when: working with limited labelled neural data, needing cross-session generalization, or wanting to leverage unlabelled spiking data for brain-computer interfaces.
---

# MOJO: Masked autOencoder-based JOint Training

## Overview

MOJO is a training framework for spike-tokenizing neural models that jointly leverages self-supervised learning (SSL) via masked autoencoding and supervised learning (SL) objectives. This approach addresses the limitation of current spike-based models that are restricted to supervised learning, which limits training to datasets with paired behavioral labels.

## Key Benefits

- **Superior performance** over purely SL-trained models, especially with limited labelled data
- **Few-shot finetuning capability** where only small amounts of labelled data from new sessions are available  
- **More interpretable neuronal representations** improving brain region classification and spike-statistics prediction
- **Cross-modality generalization** beyond spiking data to human electrocorticography during speech
- **Comparable performance** to neuro-foundation models (NFMs) designed specifically for continuous signals

## Implementation Steps

1. **Data Preparation**: Tokenize neural data at the spike level to facilitate multi-session pretraining
2. **Model Architecture**: Implement a transformer-based architecture capable of handling spike-tokenized sequences
3. **Joint Training Objective**: Combine SSL via masked autoencoding with SL objectives:
   - SSL: Randomly mask spike tokens and train model to reconstruct them
   - SL: Train on available labelled behavioral data for decoding tasks
4. **Training Protocol**:
   - Pretrain on large unlabelled datasets using SSL objective
   - Finetune on limited labelled data using combined SSL+SL objectives
5. **Evaluation**: Test on multiple neural datasets (monkey motor cortex, mouse multi-regional recordings, human ECoG)

## Use Cases

- Brain-computer interfaces with limited calibration data
- Cross-session neural decoding without extensive retraining
- Multi-species neural data analysis leveraging unlabelled recordings
- Neuro-foundation model pretraining for flexible downstream applications

## Evaluation Datasets

- Monkey motor cortex during reaching tasks
- Multi-regional mouse recordings during vision and decision making tasks  
- Human electrocorticography during speech production

## Activation Keywords

neural decoding, spike-tokenizing, self-supervised learning, few-shot finetuning, brain-computer interface, neuro-foundation models, unlabelled neural data

## References

- arXiv:2607.14086 - "Leveraging unlabelled data for generalizable neural population decoding"
- Subjects: Machine Learning (cs.LG), Neurons and Cognition (q-bio.NC)