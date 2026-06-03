---
name: quantum-circuit-synthesis-gst
description: >
  Generative quantum circuit synthesis from Gate Set Tomography (GST) data using
  diffusion models and set-vision transformers. Bypasses traditional two-step
  pipeline (GST characterization + unitary decomposition) by directly learning
  generative concept spaces from raw GST data. Use when synthesizing hardware-native
  quantum circuits, learning from gate characterization data, or building
  context-aware quantum compilation pipelines.
  Activation: quantum circuit synthesis, GST circuit generation, hardware-native
  compilation, quantum diffusion model, QMLC framework.
---

# Quantum Circuit Synthesis from GST Data (QMLC Framework)

## Overview

The QMLC (Quantum Machine Learning Control) framework learns a generative concept
space directly from Gate Set Tomography (GST) data, enabling conditional synthesis
of quantum circuits that account for real device noise (crosstalk, drift) without
explicit characterization steps.

## Core Architecture

### Step 1: GST Germ Circuit Tokenization

Tokenize GST germ circuits into structured sequences:
- Each germ circuit → token sequence representing gate operations
- Curriculum learning: start with short circuits, progressively add longer ones
- Embed sequences into latent space

### Step 2: Set-Vision Transformer with Permutation-Invariant Pooling

Process embedded circuit sequences:
```
Circuit tokens → Set-ViT → Permutation-invariant pooling → k-seed vectors
```

Key properties:
- **Permutation invariance**: Order of circuits doesn't affect representation
- **Context awareness**: Aggregates across multiple circuits
- **Noise environment capture**: Shared physical noise (crosstalk, drift)
  is encoded in latent representation

### Step 3: Latent Concept Space

The k-seed vectors represent the learned concept space of the quantum device:
- Each seed vector encodes a "concept" about the device's behavior
- Captures correlations between gates that isolated metrics miss
- Enables conditional generation based on target distributions

### Step 4: Diffusion Model for Circuit Generation

**Unconditional sampling**: Sample from the concept space
**Conditional generation**:
1. User provides target measurement distribution
2. Diffusion model generates circuit producing that distribution
3. Output denoised via diffusion on conditional covariance matrix

## Workflow

```
Raw GST Data → Tokenization → Curriculum Learning → Set-ViT Encoding
    → Concept Space (k seeds) → Diffusion Model → Circuit Synthesis
```

## Advantages Over Traditional Pipeline

| Aspect | Traditional | QMLC |
|--------|-------------|------|
| Steps | 2 (GST + decomposition) | 1 (end-to-end) |
| Noise awareness | Single-gate metrics | Context-aware |
| Crosstalk modeling | Separate calibration | Built into latent space |
| Drift adaptation | Recalibrate | Latent space adapts |

## Implementation Patterns

### Pattern 1: Curriculum Learning Strategy

```python
# Phase 1: Short circuits (1-2 gates)
# Phase 2: Medium circuits (3-5 gates)
# Phase 3: Long circuits (6+ gates) with diverse statistics
```

### Pattern 2: Conditional Covariance Denoising

```python
# During inference:
# 1. Sample from diffusion model given target distribution
# 2. Denoise output using diffusion on conditional covariance
# 3. Result: circuit robust to device noise
```

### Pattern 3: Set-Vision Transformer Architecture

```python
# Input: Set of embedded circuit sequences (order doesn't matter)
# Architecture: Transformer with self-attention over set elements
# Pooling: Permutation-invariant (e.g., mean/max pooling)
# Output: Fixed-dimensional concept vectors
```

## Target Applications

- **NISQ devices**: Near-term quantum devices with complex calibration
- **Hardware-native compilation**: Generate circuits respecting device topology
- **Automated calibration**: Reduce manual calibration overhead
- **Noise-aware synthesis**: Account for crosstalk and drift automatically

## Key Insights

1. **Context matters**: Isolated gate metrics miss correlated noise
2. **GST data is rich**: Contains full device characterization information
3. **Generative approach**: Learn distribution over circuits, not single optimum
4. **Diffusion for denoising**: Ensure generated circuits are physically realizable

## References

- QMLC paper: arxiv:2605.01367 (Yu, Sarkar, Hua, Rimbach-Russ, Ishihara, 2026)
- Gate Set Tomography: Blume-Kohout et al.
- Set Transformers: Lee et al. (2019)
- Diffusion Models: Ho et al. (2020)
