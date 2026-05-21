---
name: mine-mechanistically-interpretable-neural-encoding
description: "Mechanistically Interpretable Neural Encoding (MINE) framework that applies mechanistic interpretability tools to neural encoding models, using language-aligned image representations to localize and causally validate features driving voxel-level activity in human visual cortex. Activation: MINE, mechanistic interpretability, neural encoding, visual cortex, voxel-level fMRI, language-aligned representations, counterfactual editing, functional selectivity."
---

# MINE: Mechanistically Interpretable Neural Encoding

**arXiv:** 2605.16468v1 [cs.CV] | **Published:** 2026-05-15
**Authors:** Idan Daniel Grosbard, Mor Geva, Galit Yovel (Tel Aviv University)

## Core Research Question

**What visual features drive neuron-level activity in the human visual cortex?**

MINE opens the black box of neural encoding models by applying mechanistic-interpretability tools to localize the features within natural images that drive millimeter-scale (voxel-level) activity.

## Core Innovation

MINE bridges two previously separate research paradigms:

| Traditional Neural Encoding | MINE Framework |
|---|---|
| Black-box encoder predicts fMRI responses | Opens the black box |
| Correlational: predicts which voxels respond | Causal: identifies what drives each voxel |
| Category-level selectivity (e.g., "faces") | Fine-grained feature-level profiles |
| No per-voxel interpretability | Per-voxel semantic descriptions |
| No causal validation | Counterfactual insertion/removal |

## Methodology

### 1. Language-Aligned Image Encoding
- Uses language-aligned image representations (e.g., CLIP-like) to predict each voxel's response
- Each voxel's response = f(image embedding)
- Allows tracing activation back to specific semantic features

### 2. Feature Attribution via Mechanistic Interpretability
- Applies attribution methods to identify which features in natural images drive each voxel
- Produces **semantically interpretable descriptions** of critical features
- Generalizes per-image features into **per-voxel functional profiles**

### 3. Causal Validation Pipeline

**Step 1: Description Validation**
- Generated descriptions are sufficient to create synthetic images
- Synthetic images elicit voxel responses matching original images
- Beats random/low-attribution controls

**Step 2: Counterfactual Editing**
- Insert predicted features → activation increases
- Remove predicted features → activation decreases
- Provides **causal evidence** for feature-voxel relationship

**Step 3: Profile-Guided Editing**
- Per-voxel activation profiles guide counterfactual editing
- Produces even stronger activation shifts
- Confirms profiles faithfully capture selectivity

## Key Findings

### 1. Recovery of Known Selectivity
MINE recovers known categorical preferences of well-studied category-selective brain regions (e.g., FFA for faces, PPA for places)

### 2. Fine-Grained Voxel Structure
Reveals unique voxel-level structure **within** each region — not all voxels in FFA respond to the same face features

### 3. Causal Validation
Counterfactual insertion/removal of predicted features causes expected activation shifts:
- Feature insertion → increased response ✓
- Feature removal → decreased response ✓
- Profile-guided editing → strongest effects

### 4. Per-Voxel Functional Profiles
Each voxel has a unique functional fingerprint — a profile of visual features that drive its activity

## Technical Framework

### Encoding Model
```
voxel_response = g(f(image))
```
Where:
- f: language-aligned image encoder (e.g., CLIP)
- g: linear/nonlinear mapping to voxel responses
- Feature attribution via gradient-based or perturbation-based methods

### Feature Attribution
- Identifies image regions/semantic concepts most predictive of voxel response
- Attribution maps localized to specific visual features

### Per-Voxel Profile Construction
- Aggregate attribution across many natural images
- Cluster features into functional dimensions
- Each voxel gets a weighted profile across dimensions

## Biological Significance

### 1. Beyond Category Selectivity
Category-selective regions (FFA, PPA, EBA, etc.) contain heterogeneous voxel populations with distinct feature preferences. MINE reveals this internal structure.

### 2. Fine-Grained Functional Architecture
The visual cortex exhibits finer-grained functional organization than previously measurable with standard fMRI analysis.

### 3. Mechanistic Understanding
MINE enables **mechanistic, causal** understanding of neural computation rather than correlational description.

## Implications

### For Neuroscience
- Opens the black box of neural encoding
- Provides causal rather than correlational understanding
- Enables discovery of novel functional selectivity at voxel resolution

### For AI
- Establishes mechanistic interpretability as a tool for scientific discovery
- Language-aligned representations are effective for brain encoding
- Framework applicable beyond vision to other sensory modalities

### For Brain-Model Alignment
- More diagnostic than prediction accuracy alone
- Reveals which features models share with brains and which they miss

## Activation Keywords

- MINE
- mechanistic interpretability
- neural encoding
- visual cortex
- voxel-level fMRI
- language-aligned representations
- counterfactual editing
- functional selectivity
- category-selective regions
- feature attribution brain
- per-voxel functional profile
- causal validation neuroscience
- human visual cortex
- fMRI encoding model

## Related Skills

- **naturality-violation-score**: Category-theory-based brain-DNN alignment
- **feature-visualization-brain-encoder**: Feature visualization for brain encoder models
- **predictive-subspace-recovery-profiles**: Target-space recovery profiles for model-brain alignment
- **neural-encoding-evaluation-ground-truth**: Evaluation framework for neural encoding models
- **brainscore-alignment-prediction**: Brain alignment evaluation beyond prediction accuracy
- **decoding-encoding-alignment-critique**: Critical analysis of brain-model alignment

## References

- arXiv: [2605.16468](https://arxiv.org/abs/2605.16468)
- PDF: [Download](https://arxiv.org/pdf/2605.16468)
