---
name: eeg-cnn-autoencoder
description: Computer vision approach for EEG classification using Convolutional Neural Networks and Adversarial Autoencoders. Converts EEG signals to 2D topographic images for motor cortex activity classification. Activation: eeg classification, cnn autoencoder, brain activity decoding, eeg topogram.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, eeg, cnn, autoencoder, computer-vision, motor-cortex]
    source_paper: "Convolutional Neural Network and Adversarial Autoencoder in EEG images classification (arXiv:2604.04313)"
    citations: 0
---

# EEG Classification with CNN and Adversarial Autoencoder

## Overview
This skill implements a computer vision approach for EEG signal classification. Raw EEG signals are converted to 2D topographic images (EEG topograms), then classified using CNN and Adversarial Autoencoders for supervised and semi-supervised learning.

## Core Concepts
- EEG Topogram Generation
- Convolutional Neural Networks for spatial feature extraction
- Adversarial Autoencoder for semi-supervised learning

## Implementation Pattern

```python
import torch
import torch.nn as nn
import numpy as np
from scipy.interpolate import griddata

class EEGTopogramConverter:
    def __init__(self, electrode_positions, grid_size=(32, 32)):
        self.positions = electrode_positions
        self.grid_size = grid_size
        
    def to_topogram(self, eeg_signal):
        points = np.array([self.positions[ch] for ch in eeg_signal.keys()])
        values = np.array(list(eeg_signal.values()))
        grid_x, grid_y = np.mgrid[min(points[:,0]):max(points[:,0]):self.grid_size[0]*1j,
                                  min(points[:,1]):max(points[:,1]):self.grid_size[1]*1j]
        topogram = griddata(points, values, (grid_x, grid_y), method='cubic')
        return np.nan_to_num(topogram, nan=np.mean(values))

class EEG_CNN(nn.Module):
    def __init__(self, num_classes=4):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 4 * 4, 256)
        self.fc2 = nn.Linear(256, num_classes)
        
    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = self.pool(torch.relu(self.conv3(x)))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        return self.fc2(x)
```

## Applications
- Motor Imagery Classification
- Brain-Computer Interfaces
- Neurofeedback

## References
- arXiv:2604.04313
- Schirrmeister et al. (2017)
