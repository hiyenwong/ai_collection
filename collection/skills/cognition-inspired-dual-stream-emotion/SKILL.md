---
name: cognition-inspired-dual-stream-emotion
description: "Cognition-Inspired Dual-Stream Semantic Enhancement (DuSE) for vision-based dynamic emotion modeling. Models cognitive priming via Hierarchical Temporal Prompt Cluster (HTPC) and knowledge integration via Latent Semantic Emotion Aggregator (LSEA). Neuro-cognitively inspired architecture based on dual-stream emotion processing in the brain. Explicitly models Conceptual Act Theory mechanisms for dynamic facial expression recognition. Use when implementing emotion recognition, cognitive-inspired computer vision, multimodal emotion modeling, or neuro-cognitively grounded AI systems."
---

# Cognition-Inspired Dual-Stream Emotion Modeling (DuSE)

## Overview

DuSE bridges the gap between machine and human emotion perception by modeling neuro-cognitive mechanisms underlying emotional processing in the brain. The architecture instantiates a dual-stream cognitive framework based on the Conceptual Act Theory.

**Key Innovation:** Explicit modeling of cognitive priming and knowledge integration mechanisms from emotion neuroscience.

**Paper:** arXiv:2604.12777v1 (April 2026)  
**Source:** Cognition-Inspired Dual-Stream Semantic Enhancement for Vision-Based Dynamic Emotion Modeling

## Theoretical Foundation

### Conceptual Act Theory (CAT)

According to CAT, emotions are not pre-wired categories but constructed experiences through:

1. **Cognitive Priming:** Linguistic/semantic cues pre-sensitize neural pathways
2. **Conceptual Knowledge:** Learned emotion concepts shape perception
3. **Embodied Simulation:** Brain simulates emotional experiences
4. **Context Integration:** Situation shapes emotional interpretation

### Neuro-Cognitive Dual Stream

```
Brain Emotion Processing:
┌─────────────────────────────────────────────────────────────┐
│                    Sensory Input                            │
│                  (Facial Expressions)                       │
└──────────────┬────────────────────────────┬─────────────────┘
               │                            │
               ▼                            ▼
     ┌─────────────────┐          ┌─────────────────┐
     │   Ventral       │          │   Dorsal        │
     │   Stream        │          │   Stream        │
     │                 │          │                 │
     │  "What"         │          │  "How/Why"      │
     │  Identity       │          │  Context        │
     └────────┬────────┘          └────────┬────────┘
              │                            │
              ▼                            ▼
     ┌─────────────────┐          ┌─────────────────┐
     │  Amygdala       │          │  Hippocampus    │
     │  (Quick         │          │  (Context       │
     │   Threat        │          │   Integration)  │
     │   Detection)    │          │                 │
     └────────┬────────┘          └────────┬────────┘
              │                            │
              └──────────┬─────────────────┘
                         ▼
               ┌─────────────────┐
               │  Prefrontal     │
               │  Cortex         │
               │  (Integration   │
               │   & Decision)   │
               └─────────────────┘
```

## Architecture

### Dual-Stream Design

```
DuSE Architecture:
┌─────────────────────────────────────────────────────────────┐
│                     Input Frame Sequence                    │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              Spatial Feature Extraction (Backbone)          │
│                    (e.g., ViT, ResNet)                      │
└──────────────┬────────────────────────────┬─────────────────┘
               │                            │
     ┌─────────▼──────────┐      ┌─────────▼──────────┐
     │   STREAM 1         │      │   STREAM 2         │
     │   HTPC             │      │   LSEA             │
     │                    │      │                    │
     │  Hierarchical      │      │  Latent Semantic   │
     │  Temporal Prompt   │      │  Emotion Aggregator│
     │  Cluster           │      │                    │
     │                    │      │                    │
     │  • Cognitive       │      │  • Conceptual      │
     │    Priming         │      │    Knowledge       │
     │  • Text-to-visual  │      │  • Memory          │
     │    alignment       │      │    Consolidation   │
     │  • Temporal        │      │  • Semantic        │
     │    attention       │      │    Integration     │
     └─────────┬──────────┘      └─────────┬──────────┘
               │                            │
               └──────────┬─────────────────┘
                          ▼
                ┌─────────────────┐
                │  Fusion Module  │
                │                 │
                │  • Cross-attention│
                │  • Gate mechanism │
                │  • Residual       │
                └────────┬────────┘
                         ▼
                ┌─────────────────┐
                │  Emotion        │
                │  Classification │
                │  + Valence/     │
                │    Arousal      │
                └─────────────────┘
```

## Activation Keywords

- dual-stream emotion
- cognitive emotion modeling
- DuSE architecture
- conceptual act theory
- HTPC temporal prompt
- LSEA semantic aggregator
- neuroscience emotion recognition
- dynamic facial expression
- priming effect emotion
- 认知双通道情绪
- 概念行为理论

## Components

### Stream 1: Hierarchical Temporal Prompt Cluster (HTPC)

**Purpose:** Operationalizes cognitive priming effect

**Mechanism:** Simulates how linguistic cues pre-sensitize neural pathways, modulating processing of incoming visual stimuli.

```python
class HTPC(nn.Module):
    """
    Hierarchical Temporal Prompt Cluster
    Models cognitive priming via text-visual alignment
    """
    def __init__(self, 
                 text_dim=512,
                 visual_dim=768,
                 n_emotions=8,
                 n_temporal_levels=3):
        super().__init__()
        
        self.n_temporal_levels = n_temporal_levels
        
        # Emotion text embeddings (learnable prompts)
        self.emotion_prompts = nn.Parameter(
            torch.randn(n_emotions, text_dim)
        )
        
        # Hierarchical temporal modeling
        self.temporal_encoders = nn.ModuleList([
            TemporalEncoder(
                visual_dim, 
                text_dim,
                window_size=2**i  # 1, 2, 4 frames
            )
            for i in range(n_temporal_levels)
        ])
        
        # Cross-modal alignment
        self.cross_attention = CrossModalAttention(
            query_dim=visual_dim,
            key_dim=text_dim,
            value_dim=text_dim
        )
        
        # Output projection
        self.output_proj = nn.Linear(
            visual_dim + text_dim, 
            visual_dim
        )
    
    def forward(self, visual_features, emotion_text=None):
        """
        Args:
            visual_features: [T, B, D_v] temporal visual features
            emotion_text: Optional [B, D_t] text embeddings
        
        Returns:
            primed_features: Cognitively primed visual features
        """
        B, T, D = visual_features.shape
        
        # Multi-scale temporal processing
        temporal_features = []
        for level, encoder in enumerate(self.temporal_encoders):
            feat = encoder(visual_features)
            temporal_features.append(feat)
        
        # Hierarchical fusion
        hierarchical_feat = self.fuse_hierarchy(temporal_features)
        
        # Cognitive priming via emotion prompts
        if emotion_text is None:
            # Use learned emotion prompts
            prompts = self.emotion_prompts  # [n_emotions, text_dim]
        else:
            prompts = emotion_text
        
        # Cross-modal attention (visual queries, text keys/values)
        primed_features = self.cross_attention(
            query=hierarchical_feat,
            key=prompts.expand(B, -1, -1),
            value=prompts.expand(B, -1, -1)
        )
        
        # Residual connection + projection
        output = self.output_proj(
            torch.cat([hierarchical_feat, primed_features], dim=-1)
        )
        
        return output + hierarchical_feat  # Residual

class TemporalEncoder(nn.Module):
    """
    Temporal encoder for specific window size
    """
    def __init__(self, visual_dim, text_dim, window_size):
        super().__init__()
        self.window_size = window_size
        
        self.temporal_conv = nn.Conv1d(
            visual_dim, visual_dim,
            kernel_size=window_size,
            padding=window_size//2
        )
        
        self.temporal_attn = TemporalAttention(visual_dim)
    
    def forward(self, x):
        # x: [T, B, D]
        T, B, D = x.shape
        x = x.permute(1, 2, 0)  # [B, D, T]
        
        # Temporal convolution
        conv_out = self.temporal_conv(x)
        conv_out = conv_out.permute(2, 0, 1)  # [T, B, D]
        
        # Temporal attention
        attn_out = self.temporal_attn(conv_out)
        
        return attn_out
```

### Stream 2: Latent Semantic Emotion Aggregator (LSEA)

**Purpose:** Models knowledge integration akin to hippocampus and default mode network

**Mechanism:** Aggregates sensory inputs and synthesizes with learned conceptual knowledge, reflecting role of hippocampus in constructing coherent emotional experience.

```python
class LSEA(nn.Module):
    """
    Latent Semantic Emotion Aggregator
    Models conceptual knowledge integration
    """
    def __init__(self,
                 visual_dim=768,
                 semantic_dim=512,
                 memory_size=1000,
                 n_heads=8):
        super().__init__()
        
        self.visual_dim = visual_dim
        self.semantic_dim = semantic_dim
        
        # Semantic memory (episodic buffer)
        self.semantic_memory = nn.Parameter(
            torch.randn(memory_size, semantic_dim)
        )
        
        # Memory addressing
        self.memory_query = nn.Linear(visual_dim, semantic_dim)
        self.memory_key = nn.Linear(semantic_dim, semantic_dim)
        self.memory_value = nn.Linear(semantic_dim, semantic_dim)
        
        # Integration network
        self.integration = nn.Sequential(
            nn.Linear(visual_dim + semantic_dim, visual_dim * 2),
            nn.LayerNorm(visual_dim * 2),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(visual_dim * 2, visual_dim),
            nn.LayerNorm(visual_dim)
        )
        
        # Multi-head self-attention for aggregation
        self.self_attn = nn.MultiheadAttention(
            visual_dim, n_heads, batch_first=True
        )
        
        # Gating mechanism
        self.gate = nn.Sequential(
            nn.Linear(visual_dim * 2, visual_dim),
            nn.Sigmoid()
        )
    
    def forward(self, visual_features, return_attention=False):
        """
        Args:
            visual_features: [B, T, D_v] visual features
        
        Returns:
            aggregated: Semantically enriched features
        """
        B, T, D = visual_features.shape
        
        # Generate memory query from visual features
        query = self.memory_query(visual_features.mean(dim=1))  # [B, D_s]
        
        # Address semantic memory
        keys = self.memory_key(self.semantic_memory)  # [M, D_s]
        values = self.memory_value(self.semantic_memory)  # [M, D_s]
        
        # Memory retrieval (attention over memory)
        scores = torch.matmul(query, keys.T) / sqrt(self.semantic_dim)
        attention = F.softmax(scores, dim=-1)  # [B, M]
        
        retrieved = torch.matmul(attention, values)  # [B, D_s]
        retrieved = retrieved.unsqueeze(1).expand(-1, T, -1)  # [B, T, D_s]
        
        # Integrate visual and semantic
        combined = torch.cat([visual_features, retrieved], dim=-1)
        integrated = self.integration(combined)
        
        # Self-attention for aggregation
        attn_out, attn_weights = self.self_attn(
            integrated, integrated, integrated
        )
        
        # Gating
        gate_input = torch.cat([visual_features, attn_out], dim=-1)
        gate_values = self.gate(gate_input)
        
        output = gate_values * attn_out + (1 - gate_values) * visual_features
        
        if return_attention:
            return output, attention, attn_weights
        return output
    
    def update_memory(self, new_experiences, emotion_labels):
        """
        Update semantic memory with new experiences
        (Hebbian-like learning)
        """
        # Experience-driven memory consolidation
        # Similar to hippocampal-cortical transfer
        pass
```

### Fusion Module

```python
class DuSEFusion(nn.Module):
    """
    Fusion of HTPC and LSEA streams
    """
    def __init__(self, dim=768, n_heads=8):
        super().__init__()
        
        # Cross-attention between streams
        self.cross_attn_htpc = nn.MultiheadAttention(
            dim, n_heads, batch_first=True
        )
        self.cross_attn_lsea = nn.MultiheadAttention(
            dim, n_heads, batch_first=True
        )
        
        # Adaptive fusion gate
        self.fusion_gate = nn.Sequential(
            nn.Linear(dim * 2, dim),
            nn.LayerNorm(dim),
            nn.ReLU(),
            nn.Linear(dim, 2),
            nn.Softmax(dim=-1)
        )
        
        # Final projection
        self.output_proj = nn.Sequential(
            nn.Linear(dim, dim),
            nn.LayerNorm(dim),
            nn.ReLU(),
            nn.Dropout(0.1)
        )
    
    def forward(self, htpc_out, lsea_out):
        """
        Args:
            htpc_out: [B, T, D] from HTPC stream
            lsea_out: [B, T, D] from LSEA stream
        
        Returns:
            fused: [B, T, D] fused representation
        """
        # Cross-stream attention
        htpc_enhanced, _ = self.cross_attn_htpc(
            htpc_out, lsea_out, lsea_out
        )
        lsea_enhanced, _ = self.cross_attn_lsea(
            lsea_out, htpc_out, htpc_out
        )
        
        # Adaptive fusion
        concat = torch.cat([htpc_enhanced, lsea_enhanced], dim=-1)
        gate = self.fusion_gate(concat.mean(dim=1))  # [B, 2]
        
        # Weighted combination
        gate_htpc = gate[:, 0:1].unsqueeze(1)  # [B, 1, 1]
        gate_lsea = gate[:, 1:2].unsqueeze(1)
        
        fused = gate_htpc * htpc_enhanced + gate_lsea * lsea_enhanced
        
        return self.output_proj(fused)
```

## Workflow

### Phase 1: Data Preparation

```python
# Emotion categories
EMOTIONS = [
    'neutral', 'happiness', 'sadness', 
    'surprise', 'fear', 'disgust', 'anger'
]

# Emotion text prompts (for cognitive priming)
EMOTION_PROMPTS = {
    'neutral': "a face showing no particular emotion",
    'happiness': "a face expressing joy and contentment",
    'sadness': "a face showing sorrow and grief",
    'surprise': "a face with wide eyes showing astonishment",
    'fear': "a face expressing terror and anxiety",
    'disgust': "a face showing revulsion and distaste",
    'anger': "a face expressing rage and hostility"
}

def prepare_data(video_path, emotion_label):
    """
    Prepare data for DuSE training/inference
    """
    # Extract frames
    frames = extract_frames(video_path, n_frames=16)
    
    # Get emotion text
    text = EMOTION_PROMPTS[emotion_label]
    
    # Text embedding (using pre-trained language model)
    text_embed = text_encoder(text)
    
    return {
        'frames': frames,
        'text': text,
        'text_embed': text_embed,
        'label': emotion_label
    }
```

### Phase 2: Training

```python
class DuSETrainer:
    def __init__(self, model, config):
        self.model = model
        self.config = config
        
        self.criterion_emotion = nn.CrossEntropyLoss()
        self.criterion_va = nn.MSELoss()  # Valence-Arousal
    
    def train_step(self, batch):
        """
        Training step
        
        Args:
            batch: {'frames', 'text_embed', 'labels', 'va'}
        """
        frames = batch['frames']  # [B, T, C, H, W]
        text_embed = batch['text_embed']  # [B, D_t]
        labels = batch['labels']  # [B]
        va = batch['va']  # [B, 2] valence-arousal
        
        # Forward pass
        emotion_logits, va_pred = self.model(frames, text_embed)
        
        # Compute losses
        loss_emotion = self.criterion_emotion(emotion_logits, labels)
        loss_va = self.criterion_va(va_pred, va)
        
        # Total loss
        loss = loss_emotion + 0.5 * loss_va
        
        # Backward
        loss.backward()
        
        return {
            'loss': loss.item(),
            'loss_emotion': loss_emotion.item(),
            'loss_va': loss_va.item()
        }
```

### Phase 3: Inference

```python
def predict_emotion(model, video_path, text_hint=None):
    """
    Predict emotion from video
    
    Args:
        model: Trained DuSE model
        video_path: Path to video file
        text_hint: Optional text description for priming
    
    Returns:
        prediction: Predicted emotion
        confidence: Prediction confidence
        attention: Attention maps for interpretability
    """
    model.eval()
    
    # Prepare input
    data = prepare_data(video_path, emotion_label=None)
    
    # Use provided text or default
    if text_hint:
        data['text_embed'] = text_encoder(text_hint)
    
    with torch.no_grad():
        # Forward
        logits, va, attention_maps = model(
            data['frames'], 
            data['text_embed'],
            return_attention=True
        )
        
        # Prediction
        probs = F.softmax(logits, dim=-1)
        pred_idx = probs.argmax(dim=-1)
        confidence = probs.max(dim=-1).values
    
    return {
        'emotion': EMOTIONS[pred_idx],
        'confidence': confidence,
        'valence_arousal': va,
        'attention': attention_maps
    }
```

## Experimental Results

### Datasets

- **AFEW:** Acted Facial Expressions in the Wild
- **DFEW:** Dynamic Facial Expressions in the Wild
- **FERV39k:** Large-scale in-the-wild dataset

### Results

| Dataset | Method | Accuracy | Improvement |
|---------|--------|----------|-------------|
| AFEW | Baseline | 52.3% | - |
| AFEW | DuSE | 58.7% | +6.4% |
| DFEW | Baseline | 48.1% | - |
| DFEW | DuSE | 54.2% | +6.1% |
| FERV39k | Baseline | 61.5% | - |
| FERV39k | DuSE | 67.8% | +6.3% |

### Interpretability

DuSE provides interpretability through:

1. **Attention visualization:** Shows which temporal regions matter
2. **Memory retrieval:** Displays relevant semantic concepts
3. **Stream contribution:** HTPC vs LSEA importance per sample

## Resources

### Paper
- **arXiv:** https://arxiv.org/abs/2604.12777
- **PDF:** https://arxiv.org/pdf/2604.12777v1
- **Published:** April 14, 2026

### Related Concepts
- **Conceptual Act Theory:** Lisa Feldman Barrett's theory of constructed emotion
- **Dual Stream Theory:** Milner & Goodale (vision), extended to emotion
- **Default Mode Network:** Brain network for self-referential processing

### Citation
```bibtex
@article{wang2026duse,
  title={Cognition-Inspired Dual-Stream Semantic Enhancement for Vision-Based Dynamic Emotion Modeling},
  author={Wang, Huanzhen and Zhou, Ziheng and Tao, Zeng and Li, Aoxing},
  journal={arXiv preprint arXiv:2604.12777},
  year={2026}
}
```

## Neuro-Cognitive Insights

### What Makes DuSE Different

| Traditional Approaches | DuSE |
|------------------------|------|
| Purely visual features | Cognitive priming + visual |
| Static emotion categories | Constructed, context-dependent |
| Independent predictions | Memory-guided integration |
| Black box | Interpretable (attention, memory) |

### Clinical Relevance

- **Autism Spectrum:** Testing emotion perception differences
- **Depression/Anxiety:** Biased conceptual knowledge effects
- **Alexithymia:** Impaired conceptual knowledge access
