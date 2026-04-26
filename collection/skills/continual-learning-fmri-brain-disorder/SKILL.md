---
name: continual-learning-fmri-brain-disorder
description: "Continual learning framework for fMRI-based brain disorder diagnosis using generative replay with functional connectivity matrices. Addresses catastrophic forgetting in multi-disorder diagnosis. Activation: continual learning fmri, brain disorder diagnosis, generative replay, functional connectivity, catastrophic forgetting, fMRI classification"
---

# Continual Learning for fMRI-Based Brain Disorder Diagnosis via Generative Replay

## Overview

This skill provides a framework for continual learning in fMRI-based brain disorder diagnosis, addressing the critical challenge of catastrophic forgetting when models learn multiple brain disorders sequentially. Uses functional connectivity (FC) matrices as input representations and generative replay to preserve knowledge from previous tasks.

## Source Paper

- **Title:** Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay
- **arXiv:** 2604.14259v1
- **Published:** 2026-04-14
- **Categories:** q-bio.TO, cs.LG, eess.IV

## Core Problem

Traditional deep learning models for brain disorder diagnosis suffer from **catastrophic forgetting** — when trained sequentially on new disorders, they forget previously learned diagnostic patterns. Clinical settings require models that can continuously learn new disorders without retraining on all previous data (which may be unavailable due to privacy).

## Key Concepts

### 1. Functional Connectivity (FC) Matrices
- fMRI time series correlation matrices capture brain region interactions
- Symmetric N x N matrices where N = number of brain regions (atlas-dependent)
- Serve as "brain fingerprints" for different disorders

### 2. Generative Replay
- Train a generative model (VAE/GAN) on FC matrices of each disorder
- When learning new disorders, generate synthetic FC matrices from previous disorders
- Mix real new data + synthetic old data for training the classifier
- Preserves knowledge without storing actual patient data (privacy-compliant)

### 3. Continual Learning Pipeline
```
Task 1 (e.g., Alzheimer's): Train classifier + Train generator
Task 2 (e.g., Schizophrenia): Generate synthetic Task 1 FC matrices
  -> Mix: real Task 2 + synthetic Task 1 -> Train classifier
  -> Update generator for Task 2
Task N: Repeat with all previous tasks
```

## Implementation Framework

### Step 1: FC Matrix Preparation
```python
import numpy as np
from scipy.stats import pearsonr

def compute_fc_matrix(fmri_timeseries):
    n_regions = fmri_timeseries.shape[0]
    fc_matrix = np.zeros((n_regions, n_regions))
    for i in range(n_regions):
        for j in range(i, n_regions):
            corr, _ = pearsonr(fmri_timeseries[i], fmri_timeseries[j])
            fc_matrix[i, j] = corr
            fc_matrix[j, i] = corr
    return fc_matrix

def vectorize_fc_upper(fc_matrix):
    n = fc_matrix.shape[0]
    indices = np.triu_indices(n, k=1)
    return fc_matrix[indices]
```

### Step 2: Generative Replay Model
```python
import torch
import torch.nn as nn

class FCGenerator(nn.Module):
    def __init__(self, n_regions, latent_dim=32):
        super().__init__()
        input_dim = n_regions * (n_regions - 1) // 2
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128), nn.ReLU(),
            nn.Linear(128, 64), nn.ReLU()
        )
        self.fc_mu = nn.Linear(64, latent_dim)
        self.fc_logvar = nn.Linear(64, latent_dim)
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64), nn.ReLU(),
            nn.Linear(64, 128), nn.ReLU(),
            nn.Linear(128, input_dim)
        )
    
    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        return mu + torch.randn_like(std) * std
    
    def forward(self, x):
        h = self.encoder(x)
        mu, logvar = self.fc_mu(h), self.fc_logvar(h)
        z = self.reparameterize(mu, logvar)
        return self.decoder(z), mu, logvar
    
    def generate(self, n_samples, device='cpu'):
        z = torch.randn(n_samples, 32).to(device)
        return self.decoder(z)
```

### Step 3: Continual Learning Trainer
```python
class ContinualBrainDiagnoser:
    def __init__(self, n_regions, n_classes):
        self.n_classes = n_classes
        self.generators = {}
        self.classifier = self._build_classifier(n_regions)
    
    def _build_classifier(self, n_regions):
        input_dim = n_regions * (n_regions - 1) // 2
        return nn.Sequential(
            nn.Linear(input_dim, 256), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(256, 128), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(128, self.n_classes)
        )
    
    def learn_task(self, task_id, fc_data, labels, epochs=50):
        gen = FCGenerator(int(np.sqrt(len(fc_data[0]) * 2) + 1))
        self._train_generator(gen, fc_data)
        self.generators[task_id] = gen
        
        # Generate replay from previous tasks
        replay_data, replay_labels = [], []
        for prev_id, prev_gen in self.generators.items():
            if prev_id != task_id:
                synthetic = prev_gen.generate(len(fc_data))
                replay_data.append(synthetic.detach())
        
        all_data = torch.cat([torch.tensor(fc_data)] + replay_data, dim=0)
        all_labels = torch.cat([torch.tensor(labels)] + replay_labels, dim=0)
        self._train_classifier(all_data, all_labels, epochs)
    
    def predict(self, fc_matrix):
        with torch.no_grad():
            return self.classifier(torch.tensor(fc_matrix, dtype=torch.float32))
```

## Workflow Steps

1. **Extract FC matrices** from fMRI time series using atlas-based parcellation
2. **Train initial classifier** + generator on first disorder dataset
3. **For each new disorder:** Train new generator, generate synthetic FC from all previous generators, retrain classifier on mixed data
4. **Evaluate** on all disorders (not just the latest)

## Practical Applications

- **Clinical deployment:** Models that improve over time as new disorder data arrives
- **Privacy compliance:** No raw patient data stored, only generative models
- **Multi-disorder screening:** Single model for ADHD, Alzheimer's, Schizophrenia, etc.
- **Transfer across sites:** Learn from Site A, adapt to Site B without forgetting

## Key Metrics

- **Average Accuracy (AA):** Mean accuracy across all tasks seen so far
- **Backward Transfer (BWT):** Performance change on old tasks after learning new ones
- **Forward Transfer (FWT):** How previous learning helps new tasks

## Limitations

- Generator quality depends on sample size per disorder
- May struggle with highly similar disorders (e.g., different subtypes)
- FC matrices lose temporal dynamics information
- Atlas choice significantly affects results

## Related Skills

- brain-foundation-model-batch-effects
- brain-graph-neural
- task-aware-brain-connectivity

## Activation Keywords

- continual learning fmri
- brain disorder diagnosis
- generative replay
- catastrophic forgetting
- functional connectivity matrices
- fMRI classification
- multi-disorder diagnosis
