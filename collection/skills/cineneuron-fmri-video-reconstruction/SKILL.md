---
name: cineneuron-fmri-video-reconstruction
description: "CineNeuron — hierarchical framework for semantically enhanced fMRI-to-video reconstruction inspired by dual-pathway brain processing. Bottom-up semantic enrichment + top-down Mixture-of-Memories integration for dynamic visual experience reconstruction from brain signals. Activation: fMRI video reconstruction, CineNeuron, fMRI-to-video, brain-to-video, neural video decoding, semantic fMRI, Mixture-of-Memories."
---

# CineNeuron: Bridging Brain and Semantics for fMRI-to-Video Reconstruction

Hierarchical framework for semantically enhanced video reconstruction from fMRI signals, inspired by dual-pathway processing in the human brain.

## Paper

- **arXiv**: 2605.14569
- **Title**: Bridging Brain and Semantics: A Hierarchical Framework for Semantically Enhanced fMRI-to-Video Reconstruction
- **Published**: 2026-05-14
- **Categories**: cs.CV

## Problem

Reconstructing dynamic visual experiences from fMRI faces a critical **semantic gap**:
1. fMRI signals are noisy, low-resolution, and temporally sluggish
2. Current methods rely on incomplete semantic embeddings
3. Embeddings don't capture video-specific cues (actions, motion)
4. Lack of prior knowledge integration

## Solution: CineNeuron Framework

Inspired by the **dual-pathway processing** in human visual cortex:

### Stage 1: Bottom-Up Semantic Enrichment

Maps fMRI signals to a rich, multi-dimensional embedding space:
- **Textual semantics**: Language model embeddings
- **Image contents**: Visual features from pretrained vision models
- **Action concepts**: Motion and activity representations
- **Object categories**: Semantic class labels

```
fMRI → Semantic Encoder → Rich Embedding Space
  ↓                          ↓
Neural Activity    [Text + Image + Action + Objects]
```

### Stage 2: Top-Down Memory Integration (Mixture-of-Memories)

Dynamically selects and fuses relevant memories:
- **Memory Bank**: Previously seen data with rich annotations
- **Dynamic Selection**: Attends to most relevant memories for current fMRI signal
- **Fusion**: Combines memory with fMRI embedding to refine reconstruction
- **Output**: Enhanced video generation signal

```
fMRI Embedding + Memory Bank → Mixture-of-Memories → Refined Video Reconstruction
```

### Architecture Flow

```
fMRI Signal
    ↓
[Stage 1: Bottom-Up]
Semantic Enrichment → Multi-modal embedding (text + image + action + object)
    ↓
[Stage 2: Top-Down]
Mixture-of-Memories → Dynamic memory selection + fusion
    ↓
Video Decoder → Reconstructed dynamic visual sequence
```

## Key Innovations

### 1. Dual-Pathway Inspiration
- **Bottom-up**: Data-driven feature extraction from brain signals
- **Top-down**: Memory-guided refinement with prior knowledge
- Mirrors how human visual cortex processes information

### 2. Mixture-of-Memories
- Not just retrieval — weighted combination of multiple relevant memories
- Each memory contributes different aspects (action, objects, context)
- Dynamically adjusts weights based on current fMRI signal

### 3. Multi-Modal Semantic Enrichment
- Goes beyond CLIP embeddings to include action and temporal semantics
- Captures video-specific features that static image models miss
- Enables reconstruction of dynamic content, not just static scenes

## Results

- Surpasses state-of-the-art on fMRI-to-video benchmarks
- Better semantic alignment in reconstructed videos
- Improved temporal coherence in dynamic sequences

## Applications

- Neural decoding for brain-computer interfaces
- Understanding visual processing in the brain
- Communication aids for locked-in patients
- Cognitive neuroscience research tools
- Dream/imagery reconstruction research

## Technical Patterns

### Pattern 1: Bottom-Up + Top-Down Processing for Neural Decoding
```
Bottom-up: Extract features from neural data
Top-down: Use prior knowledge/memory to refine
Combine: Weighted fusion of both streams
```

### Pattern 2: Mixture-of-Memories for Neural Signal Enhancement
```
Memory Bank → Attention → Weighted Combination → Enhanced Signal
Similar to how brain uses past experiences to interpret current input
```

### Pattern 3: Multi-Modal Semantic Space for Neural Representation
```
Neural signals → Project to shared semantic space
  ↓
Align with: text, images, actions, objects
  ↓
Generate output conditioned on aligned representation
```

## Implementation Considerations

- **fMRI Preprocessing**: Motion correction, spatial smoothing, temporal filtering
- **ROI Selection**: Visual cortex regions (V1-V4, LOC, etc.)
- **Memory Bank**: Curated dataset with multi-modal annotations
- **Video Decoder**: Pretrained video generation model (e.g., diffusion-based)
- **Evaluation**: Semantic similarity, temporal coherence, perceptual quality

## Related Skills

- visual-imagery-decoding-fmri
- eeg-fmri-spatiotemporal-neural-frames
- monkey-perceptogram-visual-reconstruction
- brain-dit-fmri-foundation-model
