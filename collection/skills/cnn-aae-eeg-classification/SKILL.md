---
name: cnn-aae-eeg-classification
description: "EEG classification using Convolutional Neural Networks combined with Adversarial Autoencoders. Learns robust latent representations of EEG patterns for motor imagery and emotion recognition. Activation: CNN AAE EEG, adversarial autoencoder EEG, EEG classification, motor imagery recognition."
---

# CNN-AAE EEG Classification

> EEG classification framework combining Convolutional Neural Networks with Adversarial Autoencoders to learn robust representations of EEG patterns, filtering out noise and artifacts for improved classification performance.

## Metadata
- **Source**: arXiv:2604.04313
- **Authors**: Ahmed Hassan, Priya Sharma, Li Wei
- **Published**: 2026-04-05
- **Category**: eess.IV

## Core Methodology

### Problem Statement
EEG data analysis faces significant challenges in neuroscience applications:
- **High noise**: Artifact contamination from muscle movement, eye blinks
- **Low SNR**: Signal-to-noise ratio varies across conditions
- **Inter-subject variability**: Large differences between individuals
- **Limited data**: Expensive to collect large labeled datasets

### Adversarial Autoencoder (AAE) Approach

#### AAE Architecture
- **Encoder**: Maps EEG images to latent space
- **Decoder**: Reconstructs EEG from latent representation
- **Discriminator**: Distinguishes real vs generated latent codes

#### Benefits for EEG
- **Denoising**: Learns to reconstruct clean signals from noisy inputs
- **Feature learning**: Latent space captures essential EEG patterns
- **Regularization**: Adversarial training prevents overfitting
- **Representation quality**: Smooth, interpretable latent space

### CNN-AAE Classification Pipeline

```
EEG Input -> AAE Encoder -> Latent Space -> CNN Classifier
                 ↓
           [Denoised Features]
                 ↓
           AAE Decoder -> Reconstruction (optional)
```

## Implementation Guide

### Prerequisites
- EEG data in image format (e.g., spectrograms, topographic maps)
- Or raw EEG transformed to 2D representations
- PyTorch or TensorFlow
- Labeled dataset for classification task

### Architecture Implementation

#### Step 1: Adversarial Autoencoder
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class EEGEncoder(nn.Module):
    """Encoder: EEG image -> latent space"""
    def __init__(self, input_shape=(64, 64), latent_dim=128):
        super().__init__()
        self.input_shape = input_shape
        
        # Convolutional encoder
        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, 4, 2, 1),  # 64x64 -> 32x32
            nn.LeakyReLU(0.2),
            nn.Conv2d(32, 64, 4, 2, 1),  # 32x32 -> 16x16
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, 4, 2, 1),  # 16x16 -> 8x8
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.Conv2d(128, 256, 4, 2, 1),  # 8x8 -> 4x4
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
        )
        
        # Fully connected to latent
        self.fc = nn.Linear(256 * 4 * 4, latent_dim)
        
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        z = self.fc(x)
        return z

class EEGDecoder(nn.Module):
    """Decoder: latent space -> EEG image"""
    def __init__(self, latent_dim=128, output_shape=(64, 64)):
        super().__init__()
        self.output_shape = output_shape
        
        # Fully connected from latent
        self.fc = nn.Linear(latent_dim, 256 * 4 * 4)
        
        # Deconvolutional decoder
        self.deconv = nn.Sequential(
            nn.ConvTranspose2d(256, 128, 4, 2, 1),  # 4x4 -> 8x8
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, 4, 2, 1),  # 8x8 -> 16x16
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, 4, 2, 1),  # 16x16 -> 32x32
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 1, 4, 2, 1),  # 32x32 -> 64x64
            nn.Sigmoid(),  # Output [0, 1]
        )
        
    def forward(self, z):
        x = self.fc(z)
        x = x.view(x.size(0), 256, 4, 4)
        x = self.deconv(x)
        return x

class EEGDiscriminator(nn.Module):
    """Discriminator: real latent vs generated latent"""
    def __init__(self, latent_dim=128):
        super().__init__()
        
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
        
    def forward(self, z):
        return self.model(z)
```

#### Step 2: CNN Classifier on Latent Space
```python
class LatentCNNClassifier(nn.Module):
    """CNN classifier operating on latent representations."""
    def __init__(self, latent_dim=128, num_classes=4):
        super().__init__()
        
        # Reshape latent to 2D for CNN
        self.reshape_dim = int(latent_dim ** 0.5)  # e.g., 128 -> 11x11
        
        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
        )
        
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(64, num_classes)
        )
        
    def forward(self, z):
        # Reshape latent vector to 2D
        batch_size = z.size(0)
        side = int(z.size(1) ** 0.5)
        x = z.view(batch_size, 1, side, side)
        
        x = self.conv(x)
        x = self.fc(x)
        return x
```

#### Step 3: Training Loop
```python
def train_aae(encoder, decoder, discriminator, dataloader, epochs=100):
    """Train Adversarial Autoencoder."""
    
    criterion_recon = nn.MSELoss()
    criterion_adv = nn.BCELoss()
    
    optim_encoder = torch.optim.Adam(encoder.parameters(), lr=1e-4)
    optim_decoder = torch.optim.Adam(decoder.parameters(), lr=1e-4)
    optim_disc = torch.optim.Adam(discriminator.parameters(), lr=1e-4)
    
    for epoch in range(epochs):
        for batch in dataloader:
            eeg_img = batch['eeg']  # (batch, 1, H, W)
            batch_size = eeg_img.size(0)
            
            # ========== Train Discriminator ==========
            optim_disc.zero_grad()
            
            # Real latent codes (sampled from prior, e.g., Gaussian)
            z_real = torch.randn(batch_size, latent_dim)
            d_real = discriminator(z_real)
            
            # Generated latent codes
            z_fake = encoder(eeg_img)
            d_fake = discriminator(z_fake.detach())
            
            # Discriminator loss
            loss_disc = criterion_adv(d_real, torch.ones_like(d_real)) +                        criterion_adv(d_fake, torch.zeros_like(d_fake))
            loss_disc.backward()
            optim_disc.step()
            
            # ========== Train Encoder + Decoder ==========
            optim_encoder.zero_grad()
            optim_decoder.zero_grad()
            
            # Reconstruction
            z = encoder(eeg_img)
            eeg_recon = decoder(z)
            loss_recon = criterion_recon(eeg_recon, eeg_img)
            
            # Adversarial (generator fool discriminator)
            d_fake = discriminator(z)
            loss_gen = criterion_adv(d_fake, torch.ones_like(d_fake))
            
            # Total loss with weighting
            loss_total = loss_recon + 0.1 * loss_gen
            loss_total.backward()
            optim_encoder.step()
            optim_decoder.step()

def train_classifier(encoder, classifier, dataloader, epochs=50):
    """Train CNN classifier on latent space."""
    
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(
        list(encoder.parameters()) + list(classifier.parameters()),
        lr=1e-4
    )
    
    encoder.train()
    classifier.train()
    
    for epoch in range(epochs):
        for batch in dataloader:
            eeg_img = batch['eeg']
            labels = batch['label']
            
            optimizer.zero_grad()
            
            # Encode to latent
            z = encoder(eeg_img)
            
            # Classify
            predictions = classifier(z)
            
            loss = criterion(predictions, labels)
            loss.backward()
            optimizer.step()
```

## Applications
- EEG Classification: Robust classification with denoising
- Motor Imagery Recognition: BCI applications
- Emotion Recognition: Affective computing
- Adversarial Autoencoders: Generative modeling for EEG
- Neuroimaging Denoising: Artifact removal

## Pitfalls
- Requires sufficient data to learn meaningful latent space
- AAE training is unstable compared to VAE
- Latent dimension is critical hyperparameter
- Classification performance depends on latent space quality
- May not generalize across different EEG recording setups

## Related Skills
- eeg2vision-multimodal-reconstruction
- brain-inspired-capture-evidence-driven
- eeg-brain-connectivity-bci
- motor-imagery-eeg-classification

## References
- Hassan et al. (2026). Convolutional Neural Network and Adversarial Autoencoder in EEG images Classification for Neuroscience Research. arXiv:2604.04313
- Makhzani et al. (2015). Adversarial Autoencoders
- Schirrmeister et al. (2017). Deep learning with convolutional neural networks for EEG decoding and visualization
