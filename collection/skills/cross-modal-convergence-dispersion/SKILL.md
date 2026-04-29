---
name: cross-modal-convergence-dispersion
description: "Measuring cross-modal neural network convergence using single-stimulus intra-modal dispersion. Generalized Procrustes Algorithm for quantifying how stimuli with low intra-modal dispersion elicit higher cross-modal alignment. Activation triggers: cross-modal convergence, neural network alignment, vision-language alignment, representational similarity."
---

# Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion

> A methodology based on the Generalized Procrustes Algorithm to measure how intra-modal representational convergence at the single-stimulus level modulates cross-modal alignment between vision and language models.

## Metadata
- **Source**: arXiv:2604.21836v1
- **Authors**: Eghbal A. Hosseini, Brian Cheung, Evelina Fedorenko, Alex H. Williams
- **Published**: 2026-04-23
- **Category**: Representation Learning, Multi-Modal AI, Neural Network Analysis

## Core Methodology

### Problem Statement
Neural networks exhibit remarkable representational convergence:
- Across diverse architectures
- Across training objectives
- Even across data modalities

This convergence predicts alignment with brain representations. However, it's unclear how **individual stimuli** elicit convergent representations across networks.

**Key Question**: An image can be perceived in multiple ways and expressed differently using words. What determines when different networks converge on similar representations?

### Key Finding
**Intra-modal dispersion strongly modulates cross-modal convergence.**

Stimuli with **low intra-modal dispersion** (high agreement among vision models) elicit significantly higher cross-modal alignment than stimuli with high dispersion.

### Hypothesis
Representational convergence arises from learning the underlying structure of the environment in similar ways. When vision models agree on how to represent a stimulus (low dispersion), that stimulus is more likely to align with language model representations.

## Methodology: Generalized Procrustes Analysis

### Intra-Modal Dispersion

**Concept**: Measure how much vision models disagree about a single stimulus.

```
Vision Model A → Representation r_A(stimulus_i)
Vision Model B → Representation r_B(stimulus_i)
Vision Model C → Representation r_C(stimulus_i)

Intra-Modal Dispersion = variance([r_A, r_B, r_C]) after alignment
```

**Low dispersion**: All vision models represent the stimulus similarly
**High dispersion**: Vision models have different representations

### Cross-Modal Convergence

**Concept**: Measure alignment between vision and language models for the same stimulus.

```
Vision Model → Representation r_V(stimulus_i)
Language Model → Representation r_L(text_description_i)

Cross-Modal Alignment = similarity(r_V, r_L)
```

### The Relationship

```
Low Intra-Modal Dispersion ──────→ High Cross-Modal Alignment
        ↓                                    ↓
Vision models agree              Vision-language models align
        ↓                                    ↓
Clear, unambiguous               Consistent representation
visual structure                 across modalities

High Intra-Modal Dispersion ──────→ Low Cross-Modal Alignment
        ↓                                    ↓
Vision models disagree           Vision-language models misalign
        ↓                                    ↓
Ambiguous or complex             Inconsistent representation
visual content                   across modalities
```

### Generalized Procrustes Algorithm

**Purpose**: Align representations from different models for fair comparison.

```python
# Standard Procrustes Problem
Given: Two matrices X, Y (representations from two models)
Find: Orthogonal Q, translation b, scale s minimizing:
      ||s * X * Q + b - Y||²

# Generalized Procrustes (for multiple models)
Given: Matrices X₁, X₂, ..., Xₙ (representations from n models)
Find: Transformations for each minimizing:
      Σᵢ ||transform(Xᵢ) - consensus||²
```

## Implementation Guide

### Prerequisites
```python
# Core dependencies
numpy
scipy
scikit-learn
torch

# For model access
timm          # Vision models
transformers  # Language models
```

### Step 1: Extract Representations

```python
import torch
import numpy as np
from transformers import CLIPModel, CLIPProcessor
import timm

class RepresentationExtractor:
    """
    Extract representations from vision and language models.
    """
    def __init__(self, device='cuda'):
        self.device = device
        
        # Load multiple vision models
        self.vision_models = {
            'resnet50': timm.create_model('resnet50', pretrained=True, num_classes=0).to(device),
            'vit': timm.create_model('vit_base_patch16_224', pretrained=True, num_classes=0).to(device),
            'dino': timm.create_model('vit_base_patch16_224_dino', pretrained=True, num_classes=0).to(device),
            'deit': timm.create_model('deit_base_patch16_224', pretrained=True, num_classes=0).to(device),
        }
        
        # Load language model (CLIP for vision-language alignment)
        self.clip = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
        self.clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        
        for model in self.vision_models.values():
            model.eval()
        self.clip.eval()
    
    def extract_vision_representations(self, image):
        """
        Extract representations from multiple vision models.
        
        Args:
            image: Preprocessed image tensor [1, 3, 224, 224]
        
        Returns:
            representations: Dict of {model_name: feature_vector}
        """
        representations = {}
        
        with torch.no_grad():
            for name, model in self.vision_models.items():
                features = model(image.to(self.device))
                representations[name] = features.cpu().numpy()
        
        return representations
    
    def extract_language_representation(self, text):
        """
        Extract text representation from CLIP.
        
        Args:
            text: String description
        
        Returns:
            representation: Text feature vector
        """
        inputs = self.clip_processor(text=[text], return_tensors="pt", padding=True)
        
        with torch.no_grad():
            text_features = self.clip.get_text_features(**inputs)
        
        return text_features.cpu().numpy()
    
    def extract_clip_vision(self, image):
        """Extract vision representation from CLIP."""
        inputs = self.clip_processor(images=image, return_tensors="pt")
        
        with torch.no_grad():
            vision_features = self.clip.get_image_features(**inputs)
        
        return vision_features.cpu().numpy()
```

### Step 2: Generalized Procrustes Analysis

```python
from scipy.linalg import orthogonal_procrustes
from scipy.spatial.distance import cosine

def procrustes_alignment(X, Y):
    """
    Align Y to X using orthogonal Procrustes.
    
    Args:
        X: Reference representation [n_samples, n_features]
        Y: Target representation [n_samples, n_features]
    
    Returns:
        Y_aligned: Aligned Y
        R: Orthogonal rotation matrix
    """
    R, _ = orthogonal_procrustes(Y, X)
    Y_aligned = Y @ R
    return Y_aligned, R


def generalized_procrustes(representations_dict, max_iter=100, tol=1e-6):
    """
    Align multiple representations using Generalized Procrustes Analysis.
    
    Args:
        representations_dict: Dict of {model_name: representation_matrix}
        max_iter: Maximum iterations
        tol: Convergence tolerance
    
    Returns:
        aligned_reps: Dict of aligned representations
        consensus: Consensus (mean) representation
    """
    model_names = list(representations_dict.keys())
    n_models = len(model_names)
    n_samples = representations_dict[model_names[0]].shape[0]
    
    # Normalize each representation
    normalized = {}
    for name, rep in representations_dict.items():
        # Center and scale
        rep_centered = rep - rep.mean(axis=0)
        rep_scaled = rep_centered / np.linalg.norm(rep_centered, axis=1, keepdims=True)
        normalized[name] = rep_scaled
    
    # Initialize consensus as mean
    consensus = np.mean(list(normalized.values()), axis=0)
    
    # Iterative alignment
    for iteration in range(max_iter):
        aligned = {}
        
        for name, rep in normalized.items():
            # Align to consensus
            aligned_rep, _ = procrustes_alignment(consensus, rep)
            aligned[name] = aligned_rep
        
        # Update consensus
        new_consensus = np.mean(list(aligned.values()), axis=0)
        
        # Check convergence
        diff = np.linalg.norm(new_consensus - consensus)
        if diff < tol:
            break
        
        consensus = new_consensus
    
    return aligned, consensus


def compute_intra_modal_dispersion(aligned_representations):
    """
    Compute intra-modal dispersion for each stimulus.
    
    Args:
        aligned_representations: Dict of aligned rep matrices [n_stimuli, n_features]
    
    Returns:
        dispersion: [n_stimuli] vector of dispersion values
    """
    # Stack representations: [n_models, n_stimuli, n_features]
    reps_stack = np.stack(list(aligned_representations.values()), axis=0)
    
    # Compute variance across models for each stimulus
    dispersion = np.var(reps_stack, axis=0).mean(axis=1)
    
    return dispersion
```

### Step 3: Measure Cross-Modal Alignment

```python
def compute_cross_modal_alignment(vision_reps, language_reps, metric='cosine'):
    """
    Compute cross-modal alignment for each stimulus.
    
    Args:
        vision_reps: Vision representations [n_stimuli, n_features]
        language_reps: Language representations [n_stimuli, n_features]
        metric: Similarity metric ('cosine' or 'euclidean')
    
    Returns:
        alignment: [n_stimuli] vector of alignment scores
    """
    if metric == 'cosine':
        # Cosine similarity
        vision_norm = vision_reps / (np.linalg.norm(vision_reps, axis=1, keepdims=True) + 1e-8)
        language_norm = language_reps / (np.linalg.norm(language_reps, axis=1, keepdims=True) + 1e-8)
        
        # Element-wise cosine similarity for corresponding stimuli
        alignment = np.sum(vision_norm * language_norm, axis=1)
    else:
        # Negative Euclidean distance (higher = more aligned)
        diff = vision_reps - language_reps
        alignment = -np.linalg.norm(diff, axis=1)
    
    return alignment
```

### Step 4: Analyze Relationship

```python
import matplotlib.pyplot as plt
from scipy import stats

def analyze_dispersion_alignment_relationship(intra_modal_dispersion,
                                               cross_modal_alignment,
                                               bins=5):
    """
    Analyze how intra-modal dispersion modulates cross-modal alignment.
    
    Args:
        intra_modal_dispersion: [n_stimuli] dispersion values
        cross_modal_alignment: [n_stimuli] alignment values
        bins: Number of dispersion bins
    
    Returns:
        analysis_results: Dict with statistics and binned results
    """
    # Compute correlation
    correlation, p_value = stats.pearsonr(intra_modal_dispersion, cross_modal_alignment)
    
    # Bin by dispersion
    percentiles = np.percentile(intra_modal_dispersion, 
                                 np.linspace(0, 100, bins + 1))
    
    binned_results = []
    for i in range(bins):
        lower = percentiles[i]
        upper = percentiles[i + 1]
        
        mask = (intra_modal_dispersion >= lower) & (intra_modal_dispersion < upper)
        mean_alignment = np.mean(cross_modal_alignment[mask])
        std_alignment = np.std(cross_modal_alignment[mask])
        
        binned_results.append({
            'dispersion_range': (lower, upper),
            'mean_alignment': mean_alignment,
            'std_alignment': std_alignment,
            'n_stimuli': mask.sum()
        })
    
    return {
        'correlation': correlation,
        'p_value': p_value,
        'binned_results': binned_results
    }


def visualize_relationship(intra_modal_dispersion, cross_modal_alignment,
                          model_names=None):
    """
    Create visualization of the dispersion-alignment relationship.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Scatter plot
    ax1 = axes[0]
    ax1.scatter(intra_modal_dispersion, cross_modal_alignment, alpha=0.5)
    ax1.set_xlabel('Intra-Modal Dispersion')
    ax1.set_ylabel('Cross-Modal Alignment')
    ax1.set_title('Dispersion vs Alignment')
    
    # Add trend line
    z = np.polyfit(intra_modal_dispersion, cross_modal_alignment, 1)
    p = np.poly1d(z)
    ax1.plot(np.sort(intra_modal_dispersion), 
             p(np.sort(intra_modal_dispersion)), 
             "r--", alpha=0.8)
    
    # Binned bar plot
    ax2 = axes[1]
    analysis = analyze_dispersion_alignment_relationship(
        intra_modal_dispersion, cross_modal_alignment
    )
    
    means = [b['mean_alignment'] for b in analysis['binned_results']]
    stds = [b['std_alignment'] for b in analysis['binned_results']]
    labels = [f"{b['dispersion_range'][0]:.3f}-{b['dispersion_range'][1]:.3f}" 
              for b in analysis['binned_results']]
    
    ax2.bar(range(len(means)), means, yerr=stds)
    ax2.set_xticks(range(len(means)))
    ax2.set_xticklabels(labels, rotation=45)
    ax2.set_xlabel('Intra-Modal Dispersion Range')
    ax2.set_ylabel('Mean Cross-Modal Alignment')
    ax2.set_title('Alignment by Dispersion Quartile')
    
    plt.tight_layout()
    return fig, analysis
```

### Step 5: Complete Analysis Pipeline

```python
def analyze_cross_modal_convergence(stimuli, text_descriptions, images):
    """
    Complete pipeline for analyzing cross-modal convergence.
    
    Args:
        stimuli: List of stimulus identifiers
        text_descriptions: List of text descriptions (parallel to stimuli)
        images: List of image tensors (parallel to stimuli)
    
    Returns:
        results: Dict with all analysis results
    """
    # Initialize extractor
    extractor = RepresentationExtractor()
    
    # Extract vision representations from multiple models
    print("Extracting vision representations...")
    vision_reps = {name: [] for name in extractor.vision_models.keys()}
    
    for img in images:
        reps = extractor.extract_vision_representations(img)
        for name, rep in reps.items():
            vision_reps[name].append(rep[0])  # [0] to remove batch dim
    
    # Convert to matrices
    vision_matrices = {name: np.stack(reps) for name, reps in vision_reps.items()}
    
    # Extract language representations
    print("Extracting language representations...")
    language_reps = []
    for text in text_descriptions:
        rep = extractor.extract_language_representation(text)
        language_reps.append(rep[0])
    language_matrix = np.stack(language_reps)
    
    # Generalized Procrustes for vision models
    print("Aligning vision representations...")
    aligned_vision, vision_consensus = generalized_procrustes(vision_matrices)
    
    # Compute intra-modal dispersion
    print("Computing intra-modal dispersion...")
    intra_modal_dispersion = compute_intra_modal_dispersion(aligned_vision)
    
    # Compute cross-modal alignment
    print("Computing cross-modal alignment...")
    # Use one vision model (e.g., DINOv2) for cross-modal comparison
    cross_modal_alignment = compute_cross_modal_alignment(
        aligned_vision['dino'], 
        language_matrix
    )
    
    # Analyze relationship
    print("Analyzing dispersion-alignment relationship...")
    analysis = analyze_dispersion_alignment_relationship(
        intra_modal_dispersion, 
        cross_modal_alignment
    )
    
    # Visualize
    fig, detailed_analysis = visualize_relationship(
        intra_modal_dispersion, 
        cross_modal_alignment,
        list(extractor.vision_models.keys())
    )
    
    return {
        'intra_modal_dispersion': intra_modal_dispersion,
        'cross_modal_alignment': cross_modal_alignment,
        'correlation': analysis['correlation'],
        'p_value': analysis['p_value'],
        'binned_analysis': analysis['binned_results'],
        'figure': fig
    }
```

## Applications

1. **Model Selection** - Choose stimuli that maximize cross-modal alignment
2. **Dataset Curation** - Filter ambiguous stimuli that reduce alignment
3. **Brain Alignment** - Predict which stimuli will align with neural recordings
4. **Multi-Modal Training** - Design better vision-language pretraining datasets
5. **Interpretability** - Understand what makes stimuli "alignable" across modalities

## Key Findings

- **Up to 2x improvement**: Low dispersion stimuli show 2x higher cross-modal alignment
- **Robust effect**: Generalizes across different vision-language model pairings
- **Interpretable**: High dispersion = ambiguous/complex content; Low dispersion = clear structure

## Pitfalls

1. **Model Selection** - Results depend on which vision models are compared
2. **Procrustes Limitations** - Orthogonal transformations may not capture all alignment types
3. **Stimulus Selection Bias** - Care needed to avoid circular reasoning
4. **Computational Cost** - Multiple forward passes required
5. **Dimensionality** - High-dimensional representations may need dimensionality reduction

## Related Skills

- vlm-visual-cortex-alignment - Vision-language model brain alignment
- brain-llm-key-neurons-grammar - Brain-LLM analogy
- meta-learning-in-context-brain-decoding - Cross-subject brain decoding

## References

```bibtex
@article{hosseini2026crossmodal,
  title={Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion},
  author={Hosseini, Eghbal A. and Cheung, Brian and Fedorenko, Evelina and Williams, Alex H.},
  journal={arXiv preprint arXiv:2604.21836},
  year={2026}
}
```
