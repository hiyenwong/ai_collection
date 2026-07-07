---
name: quantum-brain-voxel-control
description: "Quantum-inspired neural network for vision-brain understanding using voxel controlling, phase shifting, and measurement-like projection in Hilbert space. Maps brain region connectivity via quantum-inspired modules for fMRI analysis. Use when: (1) analyzing fMRI voxel connectivity, (2) building vision-brain decoding models, (3) reconstructing images from brain signals, (4) designing quantum-inspired architectures for neuroimaging. Activation: quantum brain, vision-brain understanding, voxel controlling, phase shifting, measurement projection, fmri decoding, brain connectivity."
metadata:
  arxiv_id: "2411.13378"
  published: "2024-11-20"
  authors: "Hoang-Quan Nguyen, Xuan-Bac Nguyen, Hugh Churchill"
  tags: [quantum-inspired, fMRI, vision-brain, voxel-connectivity, neural-decoding]
---

# Quantum-Brain: Quantum-Inspired Voxel Control for Vision-Brain

## Core Concept

Uses quantum-inspired neural modules to model connectivity between brain regions (fMRI voxels) in Hilbert space, enabling effective vision-brain understanding tasks: image retrieval, brain signal retrieval, and fMRI-to-image reconstruction.

## Architecture Modules

### 1. Quantum-Inspired Voxel-Controlling (QIVC)

- Models influence of one brain voxel on others
- Operates in Hilbert space representation
- Captures non-local voxel dependencies (entanglement-like)
- Replaces traditional attention for brain connectivity

### 2. Phase-Shifting Module (PSM)

- Calibrates brain signal values
- Inspired by quantum phase operations
- Adjusts signal amplitude and phase relationships
- Stabilizes learning across subjects

### 3. Measurement-like Projection (MLP)

- Projects connectivity information from Hilbert space to feature space
- Mimics quantum measurement collapse
- Extracts task-relevant features from quantum-inspired representation

## Performance

- Natural Scene Dataset benchmarks:
  - Image retrieval: 95.1% Top-1 accuracy
  - Brain retrieval: 95.6% Top-1 accuracy
  - fMRI-to-image reconstruction: 95.3% Inception score

## Methodology

### Step 1: Encode fMRI to Hilbert Space
- Map voxel activations to quantum state representation
- Each voxel → amplitude in Hilbert space vector

### Step 2: Apply Voxel-Controlling
- Compute voxel influence matrix
- Apply quantum-inspired transformation
- Capture inter-regional connectivity

### Step 3: Phase Calibration
- Apply phase-shifting to stabilize representations
- Normalize across subjects and sessions

### Step 4: Measurement Projection
- Project to task-specific feature space
- Use for downstream tasks (classification, reconstruction)

## Implementation

- Can be implemented with standard deep learning frameworks
- Hilbert space = high-dimensional complex vector space
- Voxel-Controlling = parameterized unitary-like transformation
- Phase-Shifting = element-wise complex phase rotation
- Measurement = linear projection + nonlinearity

## Pitfalls

- **fMRI resolution**: Spatial resolution limits voxel-level analysis
- **Subject variability**: Requires per-subject calibration or alignment
- **Hilbert space dimensionality**: Balance between expressivity and computational cost
- **Training stability**: Quantum-inspired modules can be sensitive to initialization

## Related Work

- QEEGNet: Similar hybrid approach for EEG encoding (arXiv: 2407.19214)
- Quantum State Fidelity for functional networks (arXiv: 2508.16895)
- TRIBE v2: Multi-modal brain foundation model
