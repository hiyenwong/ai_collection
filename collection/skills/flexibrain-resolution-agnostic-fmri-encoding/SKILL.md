---
name: flexibrain-resolution-agnostic-fmri-encoding
description: "FlexiBrain: Resolution-Agnostic Voxel-Level Encoding for Native fMRI based on Mamba-JEPA. Defines patch sizes in real-world physical units, employs dynamic patch resizing to bypass destructive spatial standardization. Activation: resolution-agnostic, native fMRI, voxel-level encoding, Mamba-JEPA, fMRI foundation model, preprocessing-free."
category: neuroscience
---

## Context

arXiv:2606.11500 - Large-scale deep learning models in neuroscience are constrained by severe data heterogeneity. Native fMRI data exhibit substantial variation in spatial and temporal resolutions, requiring lengthy preprocessing pipelines that enforce uniformity. This introduces two critical limitations: (1) degradation of subject-specific anatomical information; (2) significant computational overhead. FlexiBrain proposes a resolution-agnostic voxel-level encoding framework based on Mamba-JEPA, bypassing destructive spatial standardization.

**Key Innovation**: First resolution-agnostic fMRI encoding framework that functions directly on native space data, reducing preprocessing from hours to minutes while improving downstream task performance by up to 12 percentage points.

**Methodology Score**: 10/10 (practical engineering + performance gains + foundation model architecture)

## Core Methodology

### 1. Resolution-Agnostic Patch Definition

**Physical Unit Patches**: Define patch sizes in real-world physical units (mm³) rather than voxel indices:
```python
# Conceptual implementation
class FlexiBrainEncoder:
    def __init__(self, patch_size_mm=(5, 5, 5)):
        self.patch_size_mm = patch_size_mm  # physical units
        self.mamba_jepa = MambaJEPA()  # backbone
    
    def dynamic_resize_patches(self, native_fMRI, voxel_dimensions):
        # Convert physical patch size to voxel count
        voxel_patch = physical_to_voxel(self.patch_size_mm, voxel_dimensions)
        # Dynamic resizing based on native resolution
        patches = extract_patches(native_fMRI, voxel_patch)
        return patches
```

**Key Principle**: Same physical patch size across datasets with different voxel resolutions → consistent semantic patches.

### 2. Dynamic Patch Resizing

**Resolution Adaptation**: Automatically adjust patch extraction based on native voxel dimensions:
- High-resolution data (1mm³ voxels) → smaller voxel patches
- Low-resolution data (3mm³ voxels) → larger voxel patches
- Both extract equivalent physical brain regions

**Bypasses Standardization**: No resampling to uniform resolution, preserving:
- Subject-specific anatomical detail
- Native spatial relationships
- Original signal characteristics

### 3. Mamba-JEPA Backbone

**Efficient 4D fMRI Modeling**: Mamba architecture with Joint Embedding Predictive Architecture (JEPA):
- Efficient sequence modeling for 4D fMRI (space × time)
- Self-supervised learning without reconstruction
- Scalable to high-dimensional brain signals

**Architecture Advantages**:
- Linear time complexity O(n) vs transformer O(n²)
- Memory-efficient for large fMRI datasets
- JEPA learns semantic representations without pixel-level reconstruction

### 4. Voxel-Level Encoding

**Native Space Processing**: Direct ingestion of fMRI data in native space:
```python
def encode_native_fMRI(native_fMRI, voxel_dimensions):
    # No preprocessing pipeline required
    encoder = FlexiBrainEncoder()
    
    # Dynamic patch extraction
    patches = encoder.dynamic_resize_patches(native_fMRI, voxel_dimensions)
    
    # Mamba-JEPA encoding
    embeddings = encoder.mamba_jepa(patches)
    
    return embeddings  # voxel-level representations
```

**Plug-in Module**: Functions as seamless module in existing pipelines:
- Minimal integration overhead
- No external data augmentation required
- Compatible with downstream task-specific models

## Implementation Steps

1. **Model Initialization**:
   - Configure FlexiBrainEncoder with physical patch size
   - Initialize Mamba-JEPA backbone for 4D signal modeling
   - Set up voxel dimension parser for native data

2. **Native Data Loading**:
   - Load fMRI in native space (no preprocessing)
   - Extract voxel dimensions from header metadata
   - Pass native resolution to encoder

3. **Dynamic Patch Extraction**:
   - Calculate voxel patch size from physical units
   - Extract patches based on native resolution
   - Feed patches to Mamba-JEPA backbone

4. **Downstream Task Integration**:
   - Use voxel-level embeddings for task-specific heads
   - Fine-tune on target neuroscience tasks
   - Evaluate against preprocessed baselines

5. **Performance Validation**:
   - Compare against SOTA methods across diverse tasks
   - Measure preprocessing time reduction
   - Verify anatomical information preservation

## Key Results

- **Downstream Task Performance**: Up to 12 percentage point gains without external augmentation
- **Preprocessing Cost Reduction**: Bypasses hours-long spatial standardization
- **Anatomical Preservation**: Subject-specific anatomical detail retained
- **Plug-in Compatibility**: Seamless integration with existing pipelines
- **Cross-Resolution Generalization**: Works across heterogeneous datasets

## Pitfalls

1. **Voxel Dimension Metadata**: Requires accurate voxel dimension metadata from native fMRI headers
2. **Physical Patch Size Selection**: Patch size choice affects semantic granularity
3. **Mamba Training Stability**: JEPA training requires careful hyperparameter tuning
4. **Native Data Variability**: Extreme resolution differences may challenge patch equivalence
5. **Downstream Task Specificity**: Embedding quality varies across task types

## Verification

1. **Resolution Consistency**: Verify same physical patches across different voxel resolutions
2. **Anatomical Preservation**: Compare anatomical detail against preprocessed baselines
3. **Preprocessing Time**: Measure time reduction from native vs standard pipeline
4. **Downstream Accuracy**: Evaluate task performance gains across diverse datasets

## Activation Keywords

resolution-agnostic, native fMRI, voxel-level encoding, Mamba-JEPA, fMRI foundation model, preprocessing-free, dynamic patch resizing, physical unit patches, heterogeneous data, spatial standardization bypass, whole-brain encoding, 4D signal modeling, plug-in module

## Applications

- fMRI foundation model development (bypass preprocessing)
- Multi-site fMRI studies with heterogeneous data
- Voxel-level decoding tasks
- Cross-subject generalization
- Rapid fMRI analysis pipeline development
- Large-scale fMRI aggregation without standardization

## References

- arXiv:2606.11500 - FlexiBrain: Resolution-Agnostic Voxel-Level Encoding for Native fMRI
- Wang et al. (2026) - Code available at GitHub
- Mamba architecture (Gu & Dao, 2023)
- JEPA self-supervised learning framework
- HCP multi-resolution fMRI datasets