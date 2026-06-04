---
name: hpc-mec-world-model
description: >
  Hippocampal-Entorhinal (HPC-MEC) inspired hierarchical world model for structure
  abstraction and generalization from video sequences. Based on arXiv:2605.15733 (May 2026).
  Use when: designing brain-inspired world models, HPC-MEC cognitive architecture,
  structure abstraction from video, latent transition learning, hippocampal-entorhinal
  coupling models, continuous attractor neural networks for AI, path integration in
  abstract spaces, self-supervised world model learning, zero-shot structural transfer.
  Activation: hpc-mec world model, hippocampal entorhinal model, structure abstraction,
  cognitive map AI, grid cell model, latent transition reuse, brain-inspired world model,
  continuous attractor neural network, CANN, episodic synthesis, structural generalization.
---

# HPC-MEC Inspired Hierarchical World Model

arXiv:2605.15733 | Tianqiu Zhang, Muyang Lyu, Xiao Liu, Si Wu | May 2026 | ICML

## Neuroscience Foundation

### HPC-MEC Circuit Functional Division

- **MEC (Medial Entorhinal Cortex)**: Encodes abstract relational structures via grid cells
  organized as Continuous Attractor Neural Networks (CANNs). Performs path integration
  driven by velocity inputs.
- **HPC (Hippocampus)**: Binds content-specific episodic information. Integrates
  sensory observations into unified scene representations.
- **Synergy**: MEC maintains structure; HPC binds context. This separation enables
  structural generalization — reuse of abstract transitions across novel entities.

### Biological World Model

The HPC-MEC circuit serves as a biological world model:
- Path integration in MEC → predict future states from current state + transition
- Grid cells encode abstract spaces (spatial, conceptual, olfactory)
- Mental simulation and planning emerge from attractor dynamics

## Model Architecture

### Three-Component System

1. **HPC-MEC Coupling Model** (Fig. 1A,B) — Hierarchical encoder-decoder
   - **Visual Inference Flow**: s → p → g (observation → HPC → MEC)
   - **Generation Flow**: g → p → s (MEC path integration → HPC → observation)
   - **Visual Feedback**: Corrects accumulated path integration errors
   - HPC and MEC use spatial-temporal Transformers with per-patch processing

2. **Inverse Model** (Fig. 1C) — Learns latent transitions
   - Takes consecutive MEC embeddings: g_t, g_{t+1}
   - Outputs latent transition z_t representing abstract dynamics
   - Enables action-free learning from observation-only videos

3. **Pretrained VQ-VAE** — Visual encoding/decoding
   - Multi-scale VQ-VAE (VAR model, depth=16) extracts observation embeddings
   - Fixed during training; simulates pre-processed sensory input to HPC-MEC

### HPC-MEC Coupling Details

- **HPC**: Spatial Transformer (depth 4) + Temporal Transformer (depth 4), hidden size 8192
- **MEC**: Spatial Transformer (depth 4) + Temporal Transformer (depth 4), hidden size 4096
  - Implements CANN dynamics for path integration
  - Per-patch hidden dimension: 256
- **Inverse Model**: Transition dimension 2048, per-patch transition 128
- **Visual feedback mechanism**: Periodically corrects accumulated PI errors

## Key Capabilities

### Structure Abstraction

- MEC embeddings encode shared structures across objects (e.g., rotation dynamics)
- HPC embeddings retain object-specific identity features
- UMAP analysis shows: periodic objects form distinctive low-dimensional trajectories
  in MEC space; HPC space separates individual objects

### Structural Generalization (Zero-Shot Transfer)

- Extract latent transition z from one video sequence
- Apply z to entirely different object/scene
- Generate analogous dynamics for novel entities
- Demonstrated on: SSv2 → OmniObject3D, Franka Kitchen, Block Pushing, Push-T, LIBERO

### Episodic Synthesis

- **One-step prediction**: Extract z from input video, generate matching next frame
- **Autoregressive prediction**: Apply sequence of z's to initial frame, generate full sequence
- Quality degrades over time due to PI error accumulation (matches biological systems)
- Visual feedback at intermediate steps corrects compounding errors

## Training Protocol

### Three-Phase Training

1. **Phase 1** (10 epochs, batch 32, seq len 8): Reconstruction + alignment losses
2. **Phase 2** (10 epochs, batch 16, seq len 10): Transition dynamics
3. **Phase 3** (10 epochs, batch 16, seq len 10): Visual feedback

- **Optimizer**: AdamW, lr=1e-4, weight decay 1e-4, gradient clipping 0.1
- **Compute**: 6-8 hours on 3× A100 GPUs (SSv2: 220K videos)
- **Inference**: 84 FPS (batch 16, seq 8 on A100) — minimal overhead

### Loss Functions

- Reconstruction losses: p_inf → s_rec, g_inf → s_rec, g_gen → s_gen
- Alignment losses: VICReg on HPC embeddings
- Transition loss: Forward model consistency
- Visual feedback loss: Corrected generation accuracy

## Datasets

- **Training**: Something-Something V2 (220,847 human action videos)
- **Evaluation**: COIL-100, MIRO, OmniObject3D (3D rotation)
- **Simulated benchmarks**: Franka Kitchen, Block Pushing, Push-T, LIBERO Goal

## Comparison to Baselines

| Model | FPS | Batch Time | Approach |
|-------|-----|-----------|----------|
| LAPA | 205.33 | 0.623s | Pixel-level optimization |
| Moto | 55.22 | 2.318s | Latent dynamics |
| AdaWorld(LAM) | 35.60 | 3.595s | Adaptive world model |
| **Ours** | **84.00** | **1.523s** | **HPC-MEC latent space** |

- HPC-MEC module adds almost no computational overhead (operates in latent space)
- Better global structure preservation vs. pixel-level methods

## Limitations

1. Autoregressive compounding errors (mitigated by visual feedback)
2. Performance degrades with distributional drift from training data
3. Coordinating multiple independent entities remains challenging
4. Future work: hierarchical HPC-MEC, object-centric representations

## Related Work

- TEM (Tolman-Eichenbaum Machine): Cognitive maps, discrete domains
- CSCG (Clone-structured cognitive graphs): Graph-based Markovian representations
- Vector-HaSH: Velocity inputs from hippocampal states
- World models (Ha & Schmidhuber, LeCun): Generative prediction frameworks
