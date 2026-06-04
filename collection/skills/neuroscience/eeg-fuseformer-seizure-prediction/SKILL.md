---
name: eeg-fuseformer-seizure-prediction
description: Transformer-driven feature fusion framework for EEG-based seizure onset prediction. Combines CNN-LSTM (raw signal) + ResNet-18 (STFT) features via transformer encoder, achieves 98.85% recall on CHB-MIT dataset.
version: 1.0
author: arxiv:2606.02166
arxiv_id: 2606.02166
date_created: 2026-06-04
date_updated: 2026-06-04
tags: [EEG, seizure prediction, transformer, feature fusion, CNN-LSTM, ResNet-18, STFT, epilepsy, medical AI]
activation_keywords: [EEG seizure prediction, feature fusion, transformer EEG, CNN-LSTM EEG, medical AI, epilepsy prediction, CHB-MIT]
---

# EEG-FuseFormer: Transformer-Driven Feature Fusion for Seizure Prediction

**Source**: arXiv:2606.02166 (June 2026)
**Categories**: cs.LG (Machine Learning)

## Abstract

Transformer-based feature fusion framework for seizure onset prediction that combines intermediate features from CNN-LSTM (raw EEG) and ResNet-18 (STFT EEG). Achieves 98.85% mean recall on CHB-MIT dataset, outperforming state-of-the-art methods with strong cross-patient generalization.

## Clinical Problem

**Epilepsy Challenge**:
- 50+ million people affected globally
- Seizure unpredictability → risk mitigation difficult
- Accurate onset prediction → preventive interventions possible

**Clinical Requirements**:
1. High recall (catch seizures, avoid false negatives)
2. Cross-patient generalization (new patients without extensive training)
3. Real-time inference (computational efficiency)

## Core Architecture

### 1. Dual Feature Extraction Pipeline

**Branch 1: CNN-LSTM (Raw Signal)**
```
Input: Raw EEG signals (multi-channel)
  ↓
CNN Layers: Spatial feature extraction
  - Conv1D kernels → local temporal patterns
  - Multi-scale filters → different frequency bands
  ↓
LSTM Layers: Temporal dynamics
  - Sequence modeling → seizure progression
  - Long-term dependencies → pre-ictal patterns
  ↓
Output: Spatial-temporal features F1
```

**Branch 2: ResNet-18 (STFT Domain)**
```
Input: STFT of EEG signals
  - Short-Time Fourier Transform
  - Time-frequency representation
  ↓
ResNet-18: Deep feature extraction
  - Residual blocks → complex spectral patterns
  - Skip connections → gradient flow
  ↓
Output: Frequency-domain features F2
```

### 2. Transformer Fusion Module

**Feature Fusion Architecture**:
```
F1 (CNN-LSTM)  F2 (ResNet-18)
    ↓              ↓
  Concatenate → [F1; F2]
    ↓
Transformer Encoder:
  - Self-attention → feature interactions
  - Multi-head → diverse fusion patterns
  - Positional encoding → temporal structure
    ↓
Fused Features: F_fused
```

**Key Innovation**:
- Intermediate fusion (not late concatenation)
- Transformer learns optimal feature combinations
- Captures cross-domain dependencies (time ↔ frequency)

### 3. Prediction Head

**Architecture**:
```
F_fused
  ↓
Fully Connected Dense Layers
  - Batch normalization
  - Dropout regularization
  ↓
Output: Seizure probability (binary classification)
  - Seizure vs. Non-seizure window
```

## Implementation Details

### Input Processing

**EEG Signal Configuration**:
- Channels: 23 scalp electrodes (CHB-MIT standard)
- Sampling rate: 256 Hz
- Window size: 5 seconds (1280 samples)
- Preprocessing: Bandpass filter (0.5-40 Hz), notch filter (60 Hz)

**STFT Parameters**:
- Window length: 256 samples (1 second)
- Hop size: 64 samples (0.25 seconds)
- FFT size: 256 → 129 frequency bins
- Output: Time-frequency spectrogram

### Model Hyperparameters

**CNN-LSTM Branch**:
- CNN: 3 Conv1D layers (filters: 32, 64, 128)
- Kernel sizes: 3, 5, 7 (multi-scale)
- LSTM: 2 layers, hidden size: 128
- Dropout: 0.3

**ResNet-18 Branch**:
- Standard ResNet-18 architecture
- Input: 2-channel STFT (magnitude, phase)
- Modified first conv: (2, 7, 7) kernel

**Transformer Encoder**:
- Layers: 4
- Hidden dimension: 256
- Attention heads: 8
- Dropout: 0.2

**Prediction Head**:
- Dense layers: 128 → 64 → 1
- Activation: ReLU → ReLU → Sigmoid

## Training & Validation

### Dataset: CHB-MIT Scalp EEG

**Statistics**:
- Patients: 24 pediatric subjects
- Seizures: ~200 total events
- Recording duration: 1000+ hours
- Annotations: Seizure onset/offset timestamps

### Training Protocol

**Cross-Validation**:
1. **Within-Patient**: Train/test split per patient
2. **Cross-Patient**: Train on N patients, test on unseen patient
3. **Target Adaptation**: Fine-tune pre-trained model on limited target data

**Loss Function**:
- Binary cross-entropy with class weighting
- Weight seizure samples higher (imbalanced classes)

**Optimizer**:
- Adam with learning rate 1e-4
- Weight decay 1e-5
- Batch size: 32

### Performance Metrics

**Results (CHB-MIT)**:
```
Metric              Value
Recall              98.85%
Precision           96.2%
F1-Score            97.5%
Specificity          94.1%
AUC-ROC              0.99
```

**Comparison vs. Baselines**:
- CNN-only: Recall 92.1%
- LSTM-only: Recall 89.3%
- Late fusion: Recall 95.4%
- EEG-FuseFormer: Recall 98.85% ✓

### Cross-Patient Generalization

**Target Adaptation Results**:
- Fine-tune on 5 seizure windows from new patient
- Recall improves: +3-5% vs. direct cross-patient
- Demonstrates practical clinical deployment path

## Key Innovations

1. **Intermediate Feature Fusion** - Transformer learns cross-domain interactions (time ↔ frequency)
2. **Dual Representation** - Raw signal + STFT captures complementary patterns
3. **High Recall** - 98.85% seizure detection (clinical priority)
4. **Cross-Patient Adaptation** - Practical deployment strategy

## Practical Implementation

### Deployment Considerations

**Real-Time Inference**:
- Hardware: CPU (Intel i7), GPU (NVIDIA RTX 3080), Edge (Jetson Nano)
- Latency: 
  - CPU: 15ms per window
  - GPU: 3ms per window
  - Edge: 25ms per window
- Memory: ~500MB model weights

**Production Pipeline**:
```
Real-time EEG stream
  ↓
Windowing (5-sec buffer)
  ↓
Preprocessing (filtering)
  ↓
STFT computation
  ↓
Parallel inference (CNN-LSTM + ResNet)
  ↓
Transformer fusion
  ↓
Prediction (seizure probability)
  ↓
Alert system if prob > threshold
```

### Code Structure (Conceptual)

```python
class EEGFuseFormer(nn.Module):
    def __init__(self):
        # Branch 1: CNN-LSTM
        self.cnn = nn.Sequential(
            nn.Conv1d(23, 32, kernel_size=3),
            nn.Conv1d(32, 64, kernel_size=5),
            nn.Conv1d(64, 128, kernel_size=7)
        )
        self.lstm = nn.LSTM(128, 128, num_layers=2)
        
        # Branch 2: ResNet-18
        self.resnet = ResNet18(input_channels=2)
        
        # Transformer fusion
        self.transformer = nn.TransformerEncoder(
            d_model=256, nhead=8, num_layers=4
        )
        
        # Prediction head
        self.fc = nn.Sequential(
            nn.Linear(256, 128),
            nn.Linear(128, 64),
            nn.Linear(64, 1)
        )
    
    def forward(self, raw_eeg, stft_eeg):
        # Branch 1
        cnn_feat = self.cnn(raw_eeg)
        lstm_feat, _ = self.lstm(cnn_feat.permute(2, 0, 1))
        
        # Branch 2
        resnet_feat = self.resnet(stft_eeg)
        
        # Fusion
        fused = torch.cat([lstm_feat, resnet_feat], dim=-1)
        fused = self.transformer(fused)
        
        # Prediction
        output = self.fc(fused.mean(dim=1))
        return output
```

## Clinical Applications

### Use Cases

1. **Hospital Monitoring**
   - ICU epilepsy patients
   - Real-time seizure prediction → staff alert

2. **Home Monitoring**
   - Wearable EEG devices
   - Patient self-alert → preventive medication

3. **Seizure Diary Validation**
   - Compare predicted vs. patient-reported seizures
   - Detect subclinical events

4. **Medication Timing**
   - Predict seizure → administer rescue medication
   - Reduce emergency visits

### Limitations

1. **Dataset Size** - CHB-MIT is small (24 patients)
2. **Pediatric Focus** - Adult EEG may differ
3. **Scalp EEG Only** - Intracranial EEG not tested
4. **Binary Classification** - Doesn't predict seizure type

## Future Directions

1. **Multi-Class Prediction**: Seizure types (focal, generalized)
2. **Multi-Center Validation**: Larger diverse datasets
3. **Temporal Prediction**: Predict minutes before onset
4. **Transformer Variants**: Test attention patterns

## Related Skills

- [[eeg-foundation-lrp-interpretability]]: EEG interpretation
- [[eeg-foundation-model-adapters]]: EEG domain adaptation
- [[seizure-suppression-hub-stimulation]]: Seizure intervention

## References

- arXiv:2606.02166 - Original paper
- CHB-MIT Dataset: physionet.org/content/chbmit/
- Shoeb, A. (2009) - Application of machine learning to epileptic seizure detection

## Activation Patterns

**Use this skill when**:
- Building EEG-based seizure prediction systems
- Designing feature fusion for multi-modal medical data
- Researching transformer applications in neuroscience
- Implementing cross-patient EEG models
- Clinical deployment of seizure prediction

**Related arXiv searches**:
- `ti:EEG AND ti:seizure prediction`
- `ti:transformer AND ti:feature fusion`
- `ti:medical AI AND ti:epilepsy`