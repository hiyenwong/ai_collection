---
name: brain-to-text-unified-decoding
description: "Unified brain-to-text decoding framework for both speech production and perception in Mandarin Chinese. Uses shared neural representations across modalities with dual-decoder architecture. Activation: brain-to-text decoding, speech BCI, neural speech decoding, unified speech decoding."
---

# Unified Brain-to-Text Decoding Across Speech Production and Perception

> A unified brain-to-sentence decoding framework for both speech production and perception in Mandarin Chinese, exhibiting strong cross-modal generalization capabilities.

## Metadata
- **Source**: arXiv:2603.12628v1
- **Authors**: Zhizhang Yuan, Yang Yang, Gaorui Zhang, et al.
- **Published**: 2026-03-13
- **Category**: Brain-Computer Interface, Speech Decoding, Neural Engineering

## Core Methodology

### Problem Addressed
Traditional brain-to-text decoding approaches:
- Focus on single modality (production OR perception)
- Limited to alphabetic languages
- Cannot leverage shared neural representations

### Key Innovation
This framework provides **unified decoding** across:
1. **Speech Production** (motor cortex → speech)
2. **Speech Perception** (auditory cortex → speech)

Using a shared latent space with modality-specific decoders.

### Architecture

```
Neural Activity (ECoG/iEEG)
    ↓
Shared Feature Encoder
    ↓
┌─────────────┴─────────────┐
↓                           ↓
Production Decoder    Perception Decoder
↓                           ↓
Mandarin Sentence Output
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch
- MNE-Python for ECoG/iEEG preprocessing
- Chinese NLP tools (jieba for tokenization)

### Step-by-Step Implementation

#### Step 1: Data Preprocessing
```python
import mne
import numpy as np
from scipy.signal import resample

# Load ECoG/iEEG data
raw = mne.io.read_raw_edf('neural_data.edf', preload=True)

# High-gamma band extraction (70-150 Hz for speech)
raw.filter(l_freq=70, h_freq=150)
raw.apply_hilbert(envelope=True)

# Epoch around speech events
events = mne.find_events(raw, stim_channel='STI')
epochs = mne.Epochs(raw, events, tmin=-0.5, tmax=2.0, baseline=None)

# Get data: (n_trials, n_channels, n_timepoints)
neural_data = epochs.get_data()

# Resample to common frequency
neural_data = resample(neural_data, num=200, axis=2)  # 200 timepoints
```

#### Step 2: Shared Feature Encoder
```python
import torch
import torch.nn as nn

class SharedFeatureEncoder(nn.Module):
    """Shared encoder for both production and perception"""
    def __init__(self, n_channels, n_timepoints, hidden_dim=512):
        super().__init__()
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(n_channels, 128, kernel_size=11, padding=5),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Conv1d(128, 256, kernel_size=7, padding=3),
            nn.ReLU(),
            nn.BatchNorm1d(256),
            nn.Conv1d(256, hidden_dim, kernel_size=5, padding=2),
            nn.ReLU()
        )
        
        # Temporal pooling
        self.temporal_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim, num_heads=8, batch_first=True
        )
        
    def forward(self, x):
        # x: (batch, n_channels, n_timepoints)
        features = self.temporal_conv(x)
        features = features.transpose(1, 2)  # (batch, time, hidden)
        
        # Self-attention for temporal aggregation
        attn_out, _ = self.temporal_attention(features, features, features)
        
        # Mean pooling
        encoded = attn_out.mean(dim=1)  # (batch, hidden_dim)
        return encoded
```

#### Step 3: Dual Decoder Architecture
```python
class ModalitySpecificDecoder(nn.Module):
    """Decoder for specific modality (production or perception)"""
    def __init__(self, hidden_dim=512, vocab_size=5000, max_length=50):
        super().__init__()
        self.vocab_size = vocab_size
        self.max_length = max_length
        
        self.decoder = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=2,
            batch_first=True
        )
        
        self.output_projection = nn.Linear(hidden_dim, vocab_size)
        
    def forward(self, encoded_features, target_tokens=None):
        batch_size = encoded_features.shape[0]
        
        # Initialize decoder input
        decoder_input = encoded_features.unsqueeze(1)  # (batch, 1, hidden)
        
        outputs = []
        hidden = None
        
        for t in range(self.max_length if target_tokens is None else target_tokens.shape[1]):
            out, hidden = self.decoder(decoder_input, hidden)
            logits = self.output_projection(out.squeeze(1))
            outputs.append(logits)
            
            if target_tokens is not None:
                # Teacher forcing
                next_input = target_tokens[:, t]
                decoder_input = self.embedding(next_input).unsqueeze(1)
            else:
                # Greedy decoding
                next_token = logits.argmax(dim=1)
                decoder_input = self.embedding(next_token).unsqueeze(1)
        
        return torch.stack(outputs, dim=1)  # (batch, seq_len, vocab_size)


class UnifiedBrainToText(nn.Module):
    """Complete unified decoding model"""
    def __init__(self, n_channels, n_timepoints, vocab_size=5000, hidden_dim=512):
        super().__init__()
        self.encoder = SharedFeatureEncoder(n_channels, n_timepoints, hidden_dim)
        self.production_decoder = ModalitySpecificDecoder(hidden_dim, vocab_size)
        self.perception_decoder = ModalitySpecificDecoder(hidden_dim, vocab_size)
        
    def forward(self, neural_data, modality='production', target_tokens=None):
        # Encode neural features
        shared_features = self.encoder(neural_data)
        
        # Route to appropriate decoder
        if modality == 'production':
            output = self.production_decoder(shared_features, target_tokens)
        else:
            output = self.perception_decoder(shared_features, target_tokens)
        
        return output
```

#### Step 4: Training with Cross-Modal Regularization
```python
def train_unified_model(model, train_loader, epochs=50, lr=1e-3):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss(ignore_index=0)  # Ignore padding
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for neural_data, modality_labels, text_tokens in train_loader:
            optimizer.zero_grad()
            
            # Split by modality
            prod_mask = modality_labels == 'production'
            perc_mask = modality_labels == 'perception'
            
            loss = 0
            
            # Production branch
            if prod_mask.any():
                prod_out = model(
                    neural_data[prod_mask], 
                    modality='production',
                    target_tokens=text_tokens[prod_mask]
                )
                loss += criterion(
                    prod_out.reshape(-1, prod_out.shape[-1]),
                    text_tokens[prod_mask].reshape(-1)
                )
            
            # Perception branch
            if perc_mask.any():
                perc_out = model(
                    neural_data[perc_mask],
                    modality='perception', 
                    target_tokens=text_tokens[perc_mask]
                )
                loss += criterion(
                    perc_out.reshape(-1, perc_out.shape[-1]),
                    text_tokens[perc_mask].reshape(-1)
                )
            
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss = {total_loss/len(train_loader):.4f}")
```

#### Step 5: Mandarin Chinese Tokenization
```python
import jieba

def tokenize_mandarin(text):
    """Tokenize Mandarin Chinese text"""
    tokens = list(jieba.cut(text))
    return tokens

# Build vocabulary
vocab = {'<PAD>': 0, '<UNK>': 1, '<START>': 2, '<END>': 3}
for sentence in training_sentences:
    for token in tokenize_mandarin(sentence):
        if token not in vocab:
            vocab[token] = len(vocab)
```

## Applications

1. **Communication BCIs**: Enable speech output for paralyzed patients
2. **Speech Rehabilitation**: Assist stroke recovery with neural feedback
3. **Cognitive Neuroscience**: Study speech production-perception interactions
4. **Multilingual BCIs**: Framework adaptable to other languages

## Pitfalls

- **Language Specificity**: Current implementation optimized for Mandarin; tonal languages may need pitch encoding
- **Electrode Coverage**: Requires specific coverage of motor and auditory cortices
- **Training Data**: Needs paired production-perception recordings for best results
- **Cross-Subject Generalization**: Performance varies across subjects; transfer learning recommended
- **Latency**: Real-time decoding requires optimization for low-latency applications

## Related Skills
- brain-to-speech-prosody-feature-engineering
- brain-to-speech-synthesis
- eeg-brain-connectivity-bci
- iphoneme-brain-to-text-als-conformerxl

## Citation
```bibtex
@article{yuan2026unified,
  title={Towards unified brain-to-text decoding across speech production and perception},
  author={Yuan, Zhizhang and Yang, Yang and Zhang, Gaorui and others},
  journal={arXiv preprint arXiv:2603.12628},
  year={2026}
}
```
