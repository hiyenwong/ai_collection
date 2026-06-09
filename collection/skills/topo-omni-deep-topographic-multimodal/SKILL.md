---
name: topo-omni-deep-topographic-multimodal
description: "Topo-Omni deep topographic multimodal model methodology for discovering functionally selective brain regions. Single contiguous in-silico sheet for visual, auditory, and language/cognitive processing. Activation: topographic, multimodal, brain regions, cortical organization, spatial smoothness, foundation model, neuroimaging, functional selectivity, sensory cognitive systems"
metadata:
  arxiv_id: "2606.09770"
  submitted: "2026-06-08"
  authors: "Badr AlKhamissi, Johannes Mehrer, Lara Marinov, Ahmed Abdelaal, Abdulkadir Gokce, Martin Schrimpf"
  tags: [neuroscience, brain-network, multimodal, topographic, foundation-model, neuroimaging, cortical-organization]
license: Complete terms in LICENSE.txt
---

# Topo-Omni: Deep Topographic Multimodal Model

## Context

Nearby neurons in cortex share similar response profiles, producing systematic spatial organization across sensory and cognitive systems. Recent topographic models reproduce aspects of this structure but remain unimodal and spatially constrain each layer separately, yielding fragmented maps that capture neither the contiguity of cortical processing streams nor their integration across modalities.

## Core Methodology

### Architecture Design

1. **Single Contiguous In-Silico Sheet**: Unlike previous unimodal topographic models, Topo-Omni uses a single spatial sheet shared across visual, auditory, and language/cognitive modalities
2. **Foundation Model Fine-Tuning**: Built by fine-tuning a pretrained foundation model with spatial smoothness objective
3. **Multimodal Integration**: Visual, auditory, and language/cognitive processing streams share the same spatial topology

### Spatial Organization Principles

1. **Spatial Smoothness Objective**: Ensure nearby neurons share similar response profiles
2. **Cross-Modal Contiguity**: Capture contiguity of cortical processing streams across modalities
3. **Cluster Consistency**: Develop clusters consistent with human neuroimaging data from sensory to cognitive systems

### Discovery Process

1. **Cluster Formation**: Model automatically develops clusters across modalities
2. **Validation**: Clusters validated against human neuroimaging data
3. **Intervention Testing**: Driving/suppressing clusters to test selective bias/perception impairment (paralleling human intervention studies)
4. **Novel Cluster Screening**: Use model to screen for new natural landscape and animal networks
5. **Human Data Validation**: Validate discovered clusters in actual human neuroimaging data

## Implementation Steps

### Model Construction

1. Initialize with pretrained foundation model (e.g., CLIP, LLaVA, or similar multimodal backbone)
2. Add spatial smoothness regularization term to loss function:
   ```
   L_smooth = λ * Σ_i Σ_j w_ij ||f_i - f_j||²
   ```
   where w_ij represents spatial proximity weights
3. Organize neurons/units in 2D sheet topology with spatial coordinates
4. Train with multimodal inputs (visual, auditory, language)

### Analysis Workflow

1. **Cluster Detection**: Use clustering algorithms (k-means, hierarchical, spectral) on learned spatial representations
2. **Functional Selectivity Mapping**: Map clusters to functional brain regions (visual cortex, auditory cortex, language areas, cognitive systems)
3. **Cross-Modal Analysis**: Compare cluster organization across different modalities
4. **Novel Hypothesis Generation**: Screen for uncharacterized spatial clusters
5. **Validation Pipeline**: 
   - Compare with fMRI/MEG activation maps
   - Test intervention effects via activation manipulation
   - Validate novel discoveries in independent human datasets

### Neuroimaging Comparison

1. Extract human neuroimaging data (fMRI, MEG, PET) for sensory/cognitive tasks
2. Compute spatial similarity between model clusters and brain activation patterns
3. Use metrics: spatial correlation, overlap coefficient, Dice score
4. Validate topographic correspondence across processing stages

## Key Results

- Clusters across modalities consistent with human neuroimaging (sensory → cognitive)
- Driving/suppressing clusters selectively biases/impairs perception (paralleling human studies)
- Discovered novel natural landscape and animal networks validated in human data
- Single spatial principle organizes representations across modalities and processing stages

## Applications

1. **Hypothesis Generation**: Testable predictions about cortical organization
2. **Brain Mapping**: Automated discovery of functionally selective regions
3. **Cross-Modal Integration**: Understanding how different sensory streams integrate spatially
4. **Clinical Translation**: Potential for identifying anomalous topographic patterns in neurological disorders

## Pitfalls

- **Spatial Resolution Mismatch**: Human neuroimaging resolution (mm) vs model resolution may differ significantly — normalize spatial coordinates before comparison
- **Modality Dominance**: Foundation model may be biased toward visual modality — balance training data across modalities
- **Over-Smoothing**: Excessive smoothness regularization can blur functional boundaries — tune λ parameter carefully
- **Cluster Validation**: Not all model clusters correspond to real brain regions — require independent human data validation before accepting as discoveries
- **Intervention Artifacts**: Driving/suppressing clusters may produce artifacts beyond real neural effects — validate with multiple intervention methods

## Verification

1. **Spatial Organization**: Verify clusters are spatially contiguous, not fragmented
2. **Cross-Modal Consistency**: Check that same spatial region processes multiple modalities consistently
3. **Neuroimaging Correlation**: Compute correlation with human fMRI/MEG activation maps (target r > 0.5)
4. **Intervention Parallels**: Confirm cluster manipulation parallels human intervention study effects
5. **Novel Discovery Validation**: Independent human dataset validation for screened clusters

## Activation Keywords

- topographic multimodal model
- brain region discovery
- cortical organization
- spatial smoothness
- functional selectivity
- multimodal foundation model
- neuroimaging validation
- sensory cognitive systems
- brain mapping
- cross-modal integration