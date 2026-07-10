---
name: eeg-tes-consciousness-measurement
description: "Deep learning framework for objective consciousness level measurement using multi-dimensional transcranial electrical stimulation (TES) with EEG. Combines TES-evoked brain responses with CNN classification for bedside-awareness assessment. Activation triggers: eeg tes, consciousness measurement, transcranial stimulation, brain state classification, awareness assessment, disorder of consciousness."
---

# EEG-TES Consciousness Measurement

> Deep learning framework that classifies EEG responses to multi-dimensional transcranial electrical stimulation (TES) patterns to provide objective measures of consciousness level at the bedside.

## Metadata
- **Source**: arXiv:2512.20319
- **Authors**: Alexis Pomares Pastor, Ines Ribeiro Violante, Gregory Scott
- **Published**: 2025-12-23
- **Subjects**: Neurons and Cognition (q-bio.NC); Artificial Intelligence (cs.AI)

## Core Methodology

### Key Innovation
Current clinical assessments of consciousness rely on command-following paradigms (fMRI, EEG) that fail when patients cannot understand commands or initiate motor responses. This paper introduces a **TES-evoked EEG response classification framework** that bypasses sensory inputs and directly measures brain state through stimulation-response patterns.

### Technical Framework

1. **Multi-dimensional TES Paradigm**: Transcranial direct current stimulation (tDCS) applied to posterior cortical areas targeting the angular gyrus, eliciting exceptionally reliable brain responses.

2. **EEG Data Collection**: Record EEG brain responses evoked by defined multi-dimensional TES patterns across participants.

3. **Deep Learning Classification**:
   - Convolutional Neural Network (CNN) architecture for EEG-TES response classification
   - Cross-subject generalization: trained on some participants, tested on held-out participants
   - Best model achieved 92% F1-score on holdout data
   - Significantly surpasses human-level performance (60-70%)

4. **Clinical Translation**: Framework designed for bedside use without requiring patient cooperation or motor responses.

## Implementation Guide

### Prerequisites
- EEG recording equipment
- TES/tDCS stimulation device
- Deep learning framework (PyTorch/TensorFlow)
- Open-sourced datasets available from authors

### Step-by-Step

1. **Data Acquisition**:
   - Apply multi-dimensional tDCS to posterior cortical areas (angular gyrus target)
   - Record EEG responses during and after stimulation
   - Collect data from sufficient participants for cross-subject generalization

2. **Preprocessing**:
   - Standard EEG preprocessing (filtering, artifact removal)
   - Time-lock EEG to TES events
   - Extract relevant temporal windows

3. **Model Training**:
   - Design CNN for spatio-temporal EEG pattern classification
   - Use cross-subject validation (train on subset, test on held-out subjects)
   - Target F1-score > 90% on holdout data

4. **Clinical Deployment**:
   - Deploy trained model for real-time consciousness assessment
   - Validate against clinical standards

### Code Example
```python
import torch
import torch.nn as nn

class EEGTESClassifier(nn.Module):
    """CNN for classifying EEG responses to TES stimulation."""
    def __init__(self, n_channels, n_timepoints, n_classes=2):
        super().__init__()
        self.conv1 = nn.Conv1d(n_channels, 32, kernel_size=5)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=3)
        self.pool = nn.AdaptiveAvgPool1d(1)
        self.fc = nn.Linear(64, n_classes)
    
    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = self.pool(x).squeeze(-1)
        return self.fc(x)
```

## Applications
- Objective consciousness measurement in disorders of consciousness (DoC)
- Bedside assessment for brain injury patients
- Monitoring during anesthesia and sedation
- Seizure-related consciousness impairment assessment
- Research into neural correlates of awareness

## Pitfalls
- TES parameters must be carefully calibrated for safety and efficacy
- EEG artifacts from stimulation must be properly handled
- Cross-subject generalization requires diverse training data
- Current approach validated on healthy participants; clinical validation needed
- Open-sourced datasets and code available for replication

## Related Skills
- brain-stimulation-dynamics-state
- eeg-foundation-model-adapters
- tms-eeg-biomarkers
