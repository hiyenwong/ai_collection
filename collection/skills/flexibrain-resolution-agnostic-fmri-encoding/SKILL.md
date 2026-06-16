# FlexiBrain: Resolution-Agnostic Voxel-Level Encoding for Native fMRI

## Overview
FlexiBrain - Resolution-agnostic voxel-level encoding framework for native fMRI based on Mamba-JEPA. Bypasses destructive spatial standardization, reduces preprocessing costs, and accelerates robust voxel-level fMRI foundation models.

**arXiv ID**: 2606.11500v1
**Authors**: Mo Wang, Wenhao Ye, Junfeng Xia, Minghao Xu, Hongkai Wen, Quanying Liu
**Updated**: 2026-06-09

## Problem
Native fMRI data from diverse sources exhibit severe heterogeneity:
- Spatial resolution variation across scanners
- Temporal resolution differences
- Preprocessing pipelines enforce uniformity
- Subject-specific anatomical information degraded
- Significant computational overhead (hours per subject)

## Solution
Resolution-agnostic framework that:
- Defines patch sizes in real-world physical units
- Uses dynamic patch resizing
- Bypasses destructive spatial standardization
- Enables direct native space ingestion

## Key Methods

### Resolution-Agnostic Design
```
Physical Units:
- Patch sizes in mm (not voxels)
- Dynamic patch resizing
- Native space processing

Architecture:
- Mamba-JEPA backbone
- 4D fMRI signal modeling
- Efficient latent representation
```

### Mamba-JEPA Backbone
- Joint Embedding Predictive Architecture
- Efficient 4D sequence modeling
- State-space model for temporal dynamics
- Low memory footprint

### Dynamic Patch Resizing
- Adapts to input resolution
- Maintains physical scale consistency
- Preserves anatomical information
- No fixed voxel dimensions

## Key Results

### Performance Gains
- Up to 12% improvement over SOTA
- No external data augmentation needed
- Consistent gains across 5 tasks

### Preprocessing Reduction
- Bypasses spatial standardization
- Dramatically reduced processing time
- Native space direct ingestion
- Plug-in module compatibility

## Applications
- Voxel-level fMRI encoding
- Multi-site fMRI analysis
- Native space foundation models
- Cross-resolution learning
- Subject-specific preservation

## Technical Implementation

### Input Requirements
- Native fMRI (any resolution)
- No preprocessing required
- Physical coordinate system

### Output
- Voxel-level embeddings
- Task-specific predictions
- Cross-resolution compatible

## Advantages
- Resolution-agnostic design
- Preprocessing cost reduction
- Subject-specific anatomy preserved
- Plug-in module architecture
- Foundation model accelerator

## Limitations
- Requires physical coordinate system
- Patch size affects granularity
- Temporal dynamics modeling depth

## Related Work
- fMRI foundation models
- Voxel-level encoding
- Mamba architecture
- JEPA frameworks

## Trigger Words
- resolution-agnostic, native fMRI, voxel-level encoding, mamba-jepa, physical patch sizes, dynamic resizing, preprocessing reduction, fMRI foundation model, cross-resolution learning, native space processing

## Activation
Use when:
- Processing heterogeneous multi-site fMRI data
- Building voxel-level fMRI foundation models
- Reducing preprocessing overhead
- Preserving subject-specific anatomy
- Handling variable spatial resolutions
- Encoding native space fMRI

## References
- arXiv:2606.11500v1
- Mamba state-space models
- JEPA architectures
- GitHub: https://github.com/OneMore1/FlexiBrain