---
name: cognition-inspired-dual-stream-emotion
description: "Cognition-Inspired Dual-Stream Semantic Enhancement (DuSE) for Vision-Based Dynamic Emotion Modeling. Implements hierarchical temporal prompt clusters (HTPC) for cognitive priming and latent semantic emotion aggregators (LSEA) for knowledge integration. Models neuro-cognitive mechanisms from Conceptual Act Theory for dynamic facial expression recognition. Use for: emotion recognition, cognitive-inspired computer vision, neuro-cognitive modeling, dynamic facial expression analysis."
version: v1.0.0
last_updated: 2026-04-15
paper: "https://arxiv.org/abs/2604.12777v1"
---

# Cognition-Inspired Dual-Stream Emotion Modeling (DuSE)

**Source Paper:** Cognition-Inspired Dual-Stream Semantic Enhancement for Vision-Based Dynamic Emotion Modeling  
**Authors:** Huanzhen Wang, Ziheng Zhou, Zeng Tao, Aoxing Li, Yingkai Zhao  
**Published:** 2026-04-14

## Overview

Models human brain emotion perception through dynamic, hierarchical integration of sensory input with semantic and contextual knowledge. Implements neuro-cognitive mechanisms from Conceptual Act Theory for dynamic facial expression recognition.

## Biological Inspiration

The human brain constructs emotional percepts by:
1. **Cognitive Priming:** Linguistic cues pre-sensitize neural pathways (HTPC stream)
2. **Knowledge Integration:** Sensory inputs synthesized with learned concepts (LSEA stream)
3. **Hierarchical Processing:** Reflecting hippocampus and default mode network roles

## Dual-Stream Architecture

### Stream 1: Hierarchical Temporal Prompt Cluster (HTPC)

**Purpose:** Operationalize cognitive priming effect

```
Text Semantics ──► Fine-grained Temporal Features ──► Modulated Visual Processing
```

**Mechanism:**
- Linguistic cues pre-sensitize neural pathways
- Modulate processing of incoming visual stimuli
- Align textual semantics with temporal facial dynamics

### Stream 2: Latent Semantic Emotion Aggregator (LSEA)

**Purpose:** Model knowledge integration (Conceptual Act Theory)

```
Sensory Inputs ──► Learned Conceptual Knowledge ──► Coherent Emotional Experience
```

**Mechanism:**
- Aggregates sensory inputs across modalities
- Synthesizes with learned conceptual knowledge
- Reflects hippocampus and default mode network function

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    Dual-Stream DuSE Model                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────┐                    ┌─────────────────┐   │
│   │   HTPC Stream   │                    │   LSEA Stream   │   │
│   │  (Cognitive     │                    │  (Knowledge     │   │
│   │   Priming)      │                    │   Integration)  │   │
│   │                 │                    │                 │   │
│   │ Text Semantics  │                    │ Sensory Inputs  │   │
│   │      │          │                    │       │         │   │
│   │      ▼          │                    │       ▼         │   │
│   │ Fine-grained    │                    │ Learned         │   │
│   │ Temporal Feats  │                    │ Conceptual      │   │
│   │      │          │                    │ Knowledge       │   │
│   │      ▼          │                    │       │         │   │
│   │ Modulate Visual │                    │       ▼         │   │
│   │ Processing      │                    │  Coherent       │   │
│   └────────┬────────┘                    │  Emotion Exp.   │   │
│            │                             └────────┬────────┘   │
│            │                                      │            │
│            └───────────────┬──────────────────────┘            │
│                            │                                   │
│                            ▼                                   │
│                    ┌───────────────┐                           │
│                    │  Fusion &     │                           │
│                    │  Decision     │                           │
│                    └───────────────┘                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Key Features

### 1. Neuro-Cognitive Plausibility

Explicitly models:
- **Prefrontal-limbic interactions** in emotion processing
- **Hierarchical temporal dynamics** across brain regions
- **Conceptual Act Theory** mechanisms

### 2. Semantic Context Integration

Unlike traditional approaches that process facial expressions in isolation:
- Integrates temporal dynamics with semantic knowledge
- Context-aware emotion modeling
- Cross-modal (text + vision) alignment

### 3. Improved Interpretability

Neuro-cognitive grounding provides:
- Clear mapping to known brain mechanisms
- Interpretable attention weights
- Modularity aligned with brain function

## Workflow

### Phase 1: HTPC Processing

```python
class HTPC(nn.Module):
    """
    Hierarchical Temporal Prompt Cluster
    Models cognitive priming effect
    """
    def __init__(self):
        self.semantic_encoder = TextEncoder()
        self.temporal_aligner = TemporalAlignmentModule()
        
    def forward(self, text_input, temporal_features):
        # Encode text semantics
        semantic_repr = self.semantic_encoder(text_input)
        
        # Align with temporal features
        modulated_features = self.temporal_aligner(
            semantic_repr, temporal_features
        )
        
        return modulated_features
```

### Phase 2: LSEA Processing

```python
class LSEA(nn.Module):
    """
    Latent Semantic Emotion Aggregator
    Models knowledge integration
    """
    def __init__(self):
        self.sensory_encoder = VisualEncoder()
        self.conceptual_knowledge = ConceptMemory()
        
    def forward(self, visual_input):
        # Process sensory input
        sensory_repr = self.sensory_encoder(visual_input)
        
        # Integrate with conceptual knowledge
        conceptual_repr = self.conceptual_knowledge(sensory_repr)
        
        # Aggregate into coherent experience
        emotional_experience = self.aggregate(
            sensory_repr, conceptual_repr
        )
        
        return emotional_experience
```

### Phase 3: Dual-Stream Fusion

```python
class DuSE(nn.Module):
    """
    Dual-Stream Semantic Enhancement
    """
    def __init__(self):
        self.htpc = HTPC()
        self.lsea = LSEA()
        self.fusion = AttentionFusion()
        
    def forward(self, visual_input, text_input):
        # HTPC stream: cognitive priming
        htpc_output = self.htpc(text_input, visual_input)
        
        # LSEA stream: knowledge integration
        lsea_output = self.lsea(visual_input)
        
        # Fuse both streams
        output = self.fusion(htpc_output, lsea_output)
        
        return output
```

## Results

- **Benchmarks:** State-of-the-art on challenging in-the-wild datasets
- **Performance:** Superior to vision-only approaches
- **Interpretability:** Enhanced through neuro-cognitive alignment

## Activation Keywords

- dual stream emotion recognition
- cognition inspired vision model
- conceptual act theory implementation
- hierarchical temporal prompt cluster
- latent semantic emotion aggregator
- neuro cognitive emotion modeling
- dynamic facial expression recognition

## References

- Paper: https://arxiv.org/abs/2604.12777v1
- PDF: https://arxiv.org/pdf/2604.12777v1
- arXiv ID: 2604.12777v1
