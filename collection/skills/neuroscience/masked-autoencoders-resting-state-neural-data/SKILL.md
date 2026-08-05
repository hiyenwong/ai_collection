---
name: masked-autoencoders-resting-state-neural-data
title: Masked Autoencoders Learn Perception-Relevant Representations from Resting State Neural Data
description: Self-supervised pretraining on spontaneous neural activity using masked autoencoders to improve perception decoding in clinical neuroprosthetics. Achieves 84.1% accuracy on psychometric tasks and 64.0% on threshold-level tasks.
arxiv_id: 2607.22615
date: 2026-06-15
authors:
  - Aleksandr Kovalev
  - Antonio Lozano
  - Fabrizio Grani
  - Cristina Soto Sanchez
  - Leili Soo
  - Rocío López-Peco
  - Adrian Villamarin-Ortiz
  - Roberto Morollón Ruiz
  - María del Mar Ayuso Arroyave
  - Alfonso Rodil
  - Eduardo Fernández
tags:
  - neuroscience
  - self-supervised learning
  - masked autoencoders
  - neural decoding
  - clinical neuroprosthetics
  - resting state activity
---

# Masked Autoencoders for Resting State Neural Data

## Overview
This methodology addresses the **data bottleneck** in clinical neuroprosthetics by leveraging **spontaneous neural activity** through **self-supervised learning**. The approach uses **masked autoencoders** pretrained on hours of unlabeled resting state neural data to improve perception decoding performance.

## Key Contributions

### 1. Data Utilization Strategy
- **Problem**: Labeled perception trials are scarce while spontaneous neural activity is abundant but underutilized
- **Solution**: Self-supervised pretraining on 14.6 hours of spontaneous multiunit activity from intracortical V1 array
- **Insight**: Spontaneous cortical activity contains rich, task-relevant structure, not just noise

### 2. Emergent Brain Structure
- **Spatial organization**: V1's spatial organization emerges purely from latent representations without supervision
- **Perceptual state separation**: Clear separation of perceptual states in latent space
- **Interpretability**: Captures biologically meaningful brain structure through unsupervised learning

### 3. Performance Results
- **General psychometric task**: 84.1% perception decoding accuracy using linear probing
- **Threshold-level task**: 64.0% accuracy on more difficult discrimination task  
- **Method**: Linear probing (logistic regression on frozen latents) with stimulation data

### 4. Clinical Impact
- **Data efficiency**: Reduces reliance on scarce labeled perception trials
- **Transfer learning**: Pretrained models can be fine-tuned for specific clinical applications
- **Neuroprosthetic enhancement**: Improves decoding accuracy for brain-computer interfaces

## Implementation Guidelines

### Model Architecture
```python
# Pseudocode for masked autoencoder implementation
class NeuralMaskedAutoencoder:
    def __init__(self, input_dim, hidden_dim, mask_ratio=0.75):
        self.encoder = TransformerEncoder(input_dim, hidden_dim)
        self.decoder = TransformerDecoder(hidden_dim, input_dim)
        self.mask_ratio = mask_ratio
    
    def forward(self, neural_data):
        # Apply random masking to neural activity
        masked_data, mask = self._apply_random_mask(neural_data, self.mask_ratio)
        # Encode visible tokens
        encoded = self.encoder(masked_data)
        # Decode to reconstruct original neural activity
        reconstructed = self.decoder(encoded)
        return reconstructed, mask
    
    def pretrain_on_resting_state(self, resting_state_data):
        # Self-supervised pretraining on spontaneous activity
        optimizer = AdamW(self.parameters())
        for epoch in range(num_epochs):
            loss = self._reconstruction_loss(resting_state_data)
            loss.backward()
            optimizer.step()
        return self
    
    def linear_probe_perception(self, stimulation_data, labels):
        # Freeze encoder and train linear classifier
        self.encoder.eval()
        with torch.no_grad():
            features = self.encoder(stimulation_data)
        classifier = LogisticRegression()
        classifier.fit(features, labels)
        return classifier
```

### Training Protocol
1. **Pretraining phase**: 
   - Use 14.6+ hours of spontaneous multiunit activity
   - Apply masked autoencoder objective (reconstruct masked neural activity)
   - Train until convergence on reconstruction loss

2. **Linear probing phase**:
   - Freeze pretrained encoder weights
   - Extract features from stimulation data
   - Train logistic regression classifier on extracted features
   - Evaluate on perception decoding tasks

3. **Evaluation metrics**:
   - General psychometric task accuracy
   - Threshold-level task accuracy  
   - Comparison with supervised-only baselines

## Applications

### Clinical Neuroprosthetics
- **Visual prosthetics**: Improve decoding for blind participants with V1 implants
- **Motor prosthetics**: Extend to motor cortex for movement intention decoding
- **Sensory restoration**: Apply to other sensory modalities (auditory, somatosensory)

### Neuroscience Research
- **Brain structure discovery**: Uncover latent organization in neural data
- **State representation**: Identify neural correlates of perceptual states
- **Cross-species analysis**: Apply to animal models for basic research

### AI/ML Applications
- **Self-supervised learning**: General framework for neural data with limited labels
- **Transfer learning**: Pretrain on abundant unlabeled data, fine-tune on scarce labeled data
- **Representation learning**: Learn interpretable representations from neural time series

## Limitations and Considerations

### Data Requirements
- Requires substantial amounts of resting state neural data (>10 hours recommended)
- Quality of spontaneous activity affects pretraining effectiveness
- May need adaptation for different brain regions or recording modalities

### Computational Resources
- Transformer-based architectures require significant memory
- Pretraining can be computationally expensive
- May need optimization for real-time applications

### Clinical Translation
- Requires validation across multiple patients and conditions
- Regulatory approval needed for clinical deployment
- Integration with existing neuroprosthetic systems

## Activation Keywords
Use this skill when working with:
- Neural decoding enhancement
- Self-supervised learning for neural data
- Resting state activity analysis
- Clinical neuroprosthetics
- Masked autoencoder pretraining
- Perception decoding accuracy
- Spontaneous neural activity utilization

## References
- **Primary**: Kovalev, A., et al. (2026). Masked Autoencoders Learn Perception-Relevant Representations from Resting State Neural Data. arXiv:2607.22615 [q-bio.NC]. Proceedings of the First Workshop on NeuroAI Multimodal Intelligence @ AAAI 2026, PMLR 308:93-98.
- **Related**: Self-supervised learning in computer vision (MAE, BEiT)
- **Applications**: Clinical neuroprosthetics and brain-computer interfaces

## Verification Steps
1. Collect sufficient resting state neural data (>10 hours)
2. Implement masked autoencoder architecture for neural time series
3. Pretrain model on spontaneous activity with reconstruction objective
4. Extract features from stimulation data using frozen encoder
5. Train linear classifier and evaluate on perception decoding tasks
6. Compare performance with supervised-only baseline approaches