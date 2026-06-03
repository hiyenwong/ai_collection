---
skill_id: whisper-ecog-alignment
category: neuroscience
date_created: 2026-06-02
paper_source: arXiv:2606.02305v1
authors: Matteo Ciferri, Tommaso Boccato, Michal Olak, Matteo Ferrante, Nicola Toschi
tags: [speech-foundation-model, ecog, brain-alignment, whisper, neural-encoding, temporal-modeling]
status: active
---

# Whisper-ECoG Alignment: Mapping Speech Foundation Models to Human Cortical Activity

## Overview

This methodology investigates how Whisper speech foundation model representations predict intracranial ECoG (electrocorticography) responses during naturalistic speech perception. It introduces a time-resolved neural encoder with recurrent temporal modeling and soft attention to examine layer-wise brain alignment.

**Core Innovation**: Intermediate Whisper layers provide strongest correspondence with neural activity, supporting hierarchical match between model representations and cortical speech processing.

## Key Concepts

### 1. Speech Foundation Models to Brain Mapping
- **Whisper**: OpenAI's speech foundation model for transcription
- **ECoG**: High-resolution intracranial brain recordings
- **Challenge**: Understanding how model representations relate to cortical activity

### 2. Time-Resolved Neural Encoder Architecture
```
Encoder Architecture:
  speech_embeddings → recurrent_temporal_model → soft_attention → neural_prediction
  
Components:
  - Speech embeddings: Whisper layer outputs
  - Recurrent temporal model: Captures temporal dynamics
  - Soft attention: Temporally local alignment
  - Neural prediction: ECoG signal reconstruction
```

### 3. Layer-wise Brain Alignment
- **Finding**: Intermediate Whisper layers → strongest ECoG correspondence
- **Implication**: Hierarchical match between model and cortical processing
- **Validation**: Layer-wise encoding performance analysis

## Implementation Methodology

### Step 1: Extract Whisper Representations

```python
import whisper

# Load Whisper model
model = whisper.load_model("base")

# Extract layer-wise representations
def extract_whisper_embeddings(audio_path, layer_indices):
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)
    
    # Get mel spectrogram
    mel = whisper.log_mel_spectrogram(audio)
    
    # Extract embeddings from specified layers
    embeddings = {}
    for layer_idx in layer_indices:
        # Hook into intermediate layers
        embeddings[layer_idx] = model.encoder(mel, layer_idx)
    
    return embeddings
```

### Step 2: Time-Resolved Neural Encoder

```python
import torch
import torch.nn as nn

class TimeResolvedEncoder(nn.Module):
    """Combines speech embeddings with temporal modeling"""
    def __init__(self, embedding_dim, hidden_dim=128):
        super().__init__()
        self.rnn = nn.GRU(embedding_dim, hidden_dim, batch_first=True)
        self.attention = nn.MultiheadAttention(hidden_dim, num_heads=4)
        self.decoder = nn.Linear(hidden_dim, ecog_channels)
    
    def forward(self, embeddings):
        # Recurrent temporal modeling
        temporal_features, _ = self.rnn(embeddings)
        
        # Soft attention mechanism
        attended, _ = self.attention(
            temporal_features, temporal_features, temporal_features
        )
        
        # Neural prediction
        ecog_prediction = self.decoder(attended)
        return ecog_prediction
```

### Step 3: Phonemic Interpretability Analysis
- **Goal**: Identify phoneme-category organization in electrodes
- **Method**: Anatomically coherent clustering
- **Output**: Electrode-electrode phoneme category mapping

### Step 4: Training and Evaluation
```python
# Training loop
def train_encoder(encoder, speech_data, ecog_data):
    optimizer = torch.optim.Adam(encoder.parameters())
    
    for epoch in range(num_epochs):
        for audio, ecog in zip(speech_data, ecog_data):
            # Extract Whisper embeddings
            embeddings = extract_whisper_embeddings(audio)
            
            # Predict ECoG
            prediction = encoder(embeddings)
            
            # Loss: MSE between prediction and actual ECoG
            loss = F.mse_loss(prediction, ecog)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

## Key Findings

### 1. Layer-wise Performance
- **Intermediate layers**: Best encoding performance
- **Deep layers**: May diverge from brain representations
- **Shallow layers**: Less correspondence

### 2. Temporal Structured Modeling Benefit
- **High-resolution ECoG**: Benefits from temporal modeling
- **Linear mappings**: Limited performance
- **Temporal models**: Significant improvement

### 3. Attention Pattern Insights
- **Temporally local alignment**: Speech embeddings ↔ neural responses
- **Attention maps**: Reveals temporal correspondence
- **Interpretability**: Phoneme-category electrode organization

## When to Use

**Activation Keywords**: whisper ecog, speech brain alignment, foundation model neural encoding, temporal neural encoder, speech perception modeling

**Use Cases**:
1. **Brain-computer interfaces**: Speech decoding from neural signals
2. **Neuroscience research**: Speech processing in cortex
3. **Model-brain comparison**: Foundation model representational analysis
4. **Speech perception studies**: Naturalistic stimuli neural responses

## Pitfalls & Considerations

1. **ECoG data requirements**: High-quality intracranial recordings needed
2. **Temporal alignment**: Precise audio-neural synchronization
3. **Model layer selection**: Need to identify optimal intermediate layers
4. **Generalization**: May not transfer to all speech models

## Research Questions

1. Does alignment hold across different speech foundation models?
2. How does task-specific fine-tuning affect brain alignment?
3. Can encoder predict ECoG for unseen speakers?
4. Cross-subject generalization capabilities?

## Related Skills

- [[brain-llm-alignment]]
- [[vlm-visual-cortex-alignment-robustness]]
- [[whisper]]
- [[neural-encoding-evaluation-ground-truth]]

## References

- arXiv:2606.02305v1 - Mapping Whisper Representations to Human ECoG Responses (2026-06-01)
- Whisper: OpenAI speech recognition model
- ECoG neural encoding literature

## Quick Start Example

```python
# Minimal Whisper-ECoG alignment pipeline
import whisper
import torch.nn as nn

class WhisperECoGAligner(nn.Module):
    def __init__(self, whisper_model="base", hidden_dim=128):
        super().__init__()
        self.whisper = whisper.load_model(whisper_model)
        self.encoder = nn.GRU(512, hidden_dim)  # Whisper embedding dim
        self.decoder = nn.Linear(hidden_dim, num_ecog_channels)
    
    def encode_speech(self, audio):
        # Get Whisper intermediate embeddings
        mel = whisper.log_mel_spectrogram(audio)
        embeddings = self.whisper.encoder(mel)
        return embeddings
    
    def forward(self, audio):
        embeddings = self.encode_speech(audio)
        temporal, _ = self.encoder(embeddings)
        ecog_pred = self.decoder(temporal)
        return ecog_pred

# Usage
aligner = WhisperECoGAligner()
ecog_prediction = aligner.forward(audio_data)
```

## Anatomical Insights

**Phoneme-Category Organization**:
- Encoding-informative electrodes cluster anatomically
- Phoneme categories show spatial coherence
- Implications for speech processing hierarchy

---

**Summary**: Whisper speech foundation models align hierarchically with human cortical ECoG responses — intermediate layers best predict neural activity via time-resolved encoding with temporal modeling and attention mechanisms.