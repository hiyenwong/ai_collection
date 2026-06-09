---
name: topo-omni-deep-topographic-multimodal
description: Topo-Omni - Deep Topographic Multimodal Model for discovering functionally selective brain regions. Single contiguous in-silico cortical sheet spanning visual, auditory, and language/cognitive processing stages.
category: neuroscience
version: 1.0.0
author: arxiv-research-cron
created: 2026-06-09
arxiv_id: 2606.09770v1
paper_title: "Discovering Functionally Selective Brain Regions with a Deep Topographic Multimodal Model"
paper_authors: "Badr AlKhamissi*, Johannes Mehrer*, Lara Marinov, Ahmed Abdelaal, Abdulkadir Gokce, Martin Schrimpf"
paper_date: 2026-06-08
paper_url: https://arxiv.org/abs/2606.09770v1
code_url: https://github.com/epflneuroailab/topo-omni
model_url: https://huggingface.co/epfl-neuroai/topo-omni
institution: EPFL NeuroAI Lab
tags:
  - topographic-model
  - multimodal
  - brain-alignment
  - cortical-organization
  - functional-selectivity
  - visual-cortex
  - auditory-cortex
  - language-network
  - category-selective
  - in-silico-cortex
  - causal-intervention
  - model-guided-discovery
activation_keywords:
  - topo-omni
  - topographic multimodal
  - cortical organization
  - functional selectivity
  - category-selective regions
  - in-silico cortical sheet
  - brain-like clustering
  - spatial smoothness
  - model-guided discovery
  - causal intervention neuroscience
---

# Topo-Omni: Deep Topographic Multimodal Model

## Overview

Topo-Omni is a topographic multimodal model that discovers functionally selective brain regions by embedding visual, auditory, and language/cognitive processing in a **single contiguous in-silico cortical sheet**. The model develops clusters consistent with human neuroimaging across sensory to cognitive systems, and enables causal interventions and model-guided discovery of novel brain regions.

**Key Innovation**: Unlike existing unimodal topographic models with fragmented maps, Topo-Omni uses a unified sheet across all processing stages and modalities, capturing the contiguity of cortical processing streams.

## Core Principles

### 1. Contiguous In-Silico Cortical Sheet

**Problem with existing models**:
- Unimodal focus (vision, audition, or language only)
- Each layer embedded on separate 2D maps
- Spatially disconnected sheets
- Cannot represent spatio-functional patterns across hierarchical levels

**Topo-Omni solution**:
- Single contiguous sheet spanning vision encoder, audio encoder, and language/cognitive module
- Spatial constraints act across levels of processing complexity
- Integration across modalities enabled by unified architecture

### 2. Spatial Smoothness Objective

**Mechanism**:
- Apply spatial smoothness loss on local cortical neighborhoods
- Task optimization + spatial regularizer → emergent category-selective patches
- **No brain data or category labels supplied during training**

**Mathematical formulation**:
```
Spatial Loss: Smoothness over local neighborhoods in the in-silico sheet
Training: Fine-tuning pretrained multimodal foundation model with spatial objective
Target: Self-distillation from unmodified baseline outputs
```

### 3. Pretrained Foundation Model Backbone

**Base architecture**: Qwen2.5-Omni-3B multimodal model
**Training corpus**: ~4,500 videos (modest scale)
**Paradigm**: Self-distillation - baseline outputs as targets
**Advantage**: Preserves capability while imposing spatial organization

## Emergent Functional Organization

### Visual Cortex Organization

**Category-selective regions recovered**:
- **Face-selective**: Parallel to human OFA/FFA
- **Scene-selective**: Parallel to human place-selective areas
- **Body-selective**: Body patches in visual cortex
- **Tool-selective**: Tool category specialization

**Validation**:
- EMFL localizer stimuli (Marvi et al., 2025)
- Response profiles match human fMRI across category-selective regions
- Pearson correlation with human visual cortex responses

**Spatial property**: Selectivity confined to vision encoder portion of sheet

### Auditory Cortex Organization

**Speech-selective regions**:
- Localizer: Non-words vs. Quilted Speech
- Parallels human superior temporal gyrus (STG)
- Pearson r = 0.69, p = 0.025
- Sensitivity to speech structure, not just acoustic energy

**Voice-selective regions**:
- Localizer: Human Voices vs. Non-voices (Pernet et al., 2015)
- Parallel to temporal voice area along superior temporal sulcus
- Responds preferentially to human speech stimuli
- Distinct from speech-selective regions

**Tonotopic organization**:
- Spatially organized map of preferred frequency
- Mirrors human auditory cortex tonotopy
- Neighboring units share similar best frequencies

**Modality specificity**: Auditory selectivity confined to audio encoder, no vision encoder activation

### Higher Cognitive Networks

**Language network**:
- Localizer: Sentences vs. Non-words (Fedorenko et al., 2010)
- Language-selectivity d′ = 1.39, p < 0.001
- Parallel to fronto-temporal language network

**Multiple demand network**:
- Localizer: Math questions vs. narrative questions (Fedorenko et al., 2013)
- Selectivity d′ = 0.54, p < 0.001
- Parallel to frontoparietal multiple demand network
- Activates during cognitively demanding tasks

**Theory of mind network**:
- Localizer: False Belief vs. False Photograph (Dufour et al., 2013)
- Selectivity d′ = 0.15, p < 0.001 (weaker than language/MD)
- Parallel to temporo-parietal junction and medial prefrontal cortex

**Processing**: Input as text tokens directly to language/cognitive module

## Model-Guided Cluster Discovery

### Novel Region Discovery

**Methodology**:
1. Cluster naturalistic video segments using Topo-Omni selectivity
2. Generate contrast predictions for human fMRI
3. Test predictions in human neuroimaging data (Spacetop dataset)

**Discovered clusters**:
- **Animal-selective cluster**: Predominantly in prefrontal cortex
- **Natural landscape-selective cluster**: Prefrontal localization

**Significance**: These have not previously been described as functionally selective regions comparable to classical face-, place-, word-, voice-selective areas.

**Closed-loop science**:
- Model proposes hypotheses → human validation → independent confirmation needed
- Shift from post-hoc explanation to hypothesis generation

## Causal Intervention Capability

### Spatially Targeted Perturbations

**Face-selective region demonstration**:
- **Suppression**: Abolishes face identification, other categories intact
- **Driving**: Biases model toward face responses regardless of actual input

**Analogue of neuroscience interventions**:
- TMS (transcranial magnetic stimulation)
- Intracranial stimulation
- Lesion studies

**Advantages over human experiments**:
- Scalable interventions
- Cost-effective screening
- Spatially interpretable results
- Causal validation before in-vivo experiments

### Intervention Protocol

```
1. Define localizer-specific ROI units
2. Suppress: Zero out activations in cluster
3. Drive: Amplify activations beyond normal range
4. Measure: Task performance changes, selectivity shifts
5. Validate: Compare to human intervention studies
```

## Performance Validation

### Brain Alignment Benchmarks

**NSD (Natural Scenes Dataset) ROIs**:
- Twelve regions tested
- Topo-Omni matches or exceeds non-topographic baseline
- No degradation from imposing spatial organization

**OmniBench accuracy**:
- Downstream task performance maintained
- Spatial structure need not trade off against computational performance

**Brain-Score benchmarks**:
- Competitive with non-topographic multimodal models
- Spatial organization incorporated at no measurable cost

## Architecture Details

### Multimodal Cortical Architecture

**Components**:
- Vision encoder → mapped to sheet region
- Audio encoder → mapped to contiguous region
- Language/cognitive module → mapped to higher-order region
- **Contiguous layout**: Single sheet spanning all components

### Projection Scheme

**Mapping to in-silico sheet**:
- Units assigned positions on 2D surface
- Spatial smoothness loss applied across neighboring positions
- Emergent clustering without explicit anatomical priors

**Key**: Any multimodal foundation model can be fitted with contiguous topographic sheet using this projection scheme

## Interpretation & Limitations

### In-Silico Sheet Interpretation

**Captures organizational principles, not anatomy**:
- Coarse spatio-functional patterns
- Category-selective regions
- Modality-appropriate organization

**Does NOT model**:
- Hemispheres
- Cortical folding
- White-matter connectivity
- Cytoarchitecture
- Precise relative positions of human regions
- Anatomical subregions (e.g., OFA vs. FFA)

**Future directions**: Stronger anatomical correspondences require stronger architectural priors

### Limitations

1. **Anatomical abstraction**: Coarse principles, not detailed anatomy
2. **Limited validation dataset**: EMFL subset, n=6 participants
3. **Training scale**: ~4,500 videos (modest)
4. **Self-distillation coupling**: Spatial loss tied to specific functional anchor
5. **Novel-cluster validation**: Single dataset (Spacetop), needs independent validation and causal tests

## Research Applications

### 1. Model-Guided Localizer Design

- Clusters propose contrasts for human/animal experiments
- Complement conventional pipeline (model accounts for known regions)
- Predict previously uncharacterized organization

### 2. In-Silico Screening Platform

- Pre-TMS screening for target regions
- Intracranial stimulation prediction
- Lesion study analogues
- Generate necessity/sufficiency hypotheses

### 3. Cross-Modal Organization Study

- Component boundary behavior
- Semantic relatedness across vision, audio, language
- Spatial loss pulls together semantically related units

### 4. Architectural Generalization

- Template applicable to any multimodal foundation model
- Potential extension to touch, olfactory, motor processing
- Topographic variants for additional modalities

## Implementation Guidelines

### Using Topo-Omni

**Code repository**: https://github.com/epflneuroailab/topo-omni

**Model weights**: https://huggingface.co/epfl-neuroai/topo-omni

**Basic usage**:
```python
from topo_omni import TopoOmniModel

# Load pretrained model
model = TopoOmniModel.from_pretrained("epfl-neuroai/topo-omni")

# Process multimodal input
inputs = {
    "video": video_tensor,
    "audio": audio_tensor,
    "text": text_tokens
}

# Get activations on in-silico sheet
activations = model(inputs, return_sheet_activations=True)

# Extract cluster activations
face_cluster = model.get_cluster_activations("face-selective")
speech_cluster = model.get_cluster_activations("speech-selective")
language_cluster = model.get_cluster_activations("language")
```

### Causal Intervention

```python
# Suppress face-selective region
model.suppress_cluster("face-selective")
output = model(inputs)

# Drive face-selective region
model.drive_cluster("face-selective", amplification=2.0)
output = model(inputs)

# Measure selectivity shift
face_selectivity = model.measure_selectivity("face", output)
```

### Cluster Discovery

```python
# Cluster naturalistic stimuli
clusters = model.discover_clusters(
    stimuli=naturalistic_videos,
    method="selectivity_clustering",
    n_clusters=10
)

# Generate contrast predictions
contrasts = model.generate_contrasts(clusters)

# Validate in human data
validation_results = validate_in_fmri(contrasts, human_data)
```

## Key Takeaways

1. **Unified sheet sufficient**: Single spatial smoothness principle induces brain-like organization across modalities
2. **No trade-off**: Spatial organization preserved in high-performing systems
3. **Hypothesis generation**: Models predict new cortical organization, not just explain known regions
4. **Causal testing**: In-silico interventions enable scalable neuroscience screening
5. **Platform for NeuroAI**: Spatially grounded models for hypothesis-driven brain research

## Future Directions

1. **Anatomical precision**: Incorporate hemispheric organization, cortical folding, connectivity
2. **Larger training scale**: Test spatial loss under bigger corpora
3. **Training from scratch**: Explore organization emergence under alternative objectives
4. **Additional modalities**: Extend to touch, olfactory, motor processing
5. **Causal validation**: Independent TMS/intracranial studies for novel clusters

## Related Skills

- `brain-graph-neural` - Graph neural networks for brain connectivity
- `brain-dit-fmri-foundation-model` - Brain-DiT fMRI foundation model
- `neural-population-dynamics` - Neural population dynamics analysis
- `brain-inspired-snn-pattern-analysis` - Brain-inspired SNN patterns
- `topological-ml-eeg-classification` - Topological ML for EEG classification

## References

- arXiv:2606.09770v1 - Original paper
- Marvi et al. (2025) - EMFL localizer dataset
- Fedorenko et al. (2010, 2013) - Language/MD localizers
- Pernet et al. (2015) - Voice localizer
- Dufour et al. (2013) - Theory of mind localizer
- Mehrer et al. (2026) - TMS screening framework
- Lee et al. (2020), Margalit et al. (2024) - Prior topographic models

---

**Note**: This skill represents a paradigm shift in NeuroAI - from post-hoc explanation to hypothesis generation, enabling models to propose novel cortical organization that can be tested in human neuroscience experiments.