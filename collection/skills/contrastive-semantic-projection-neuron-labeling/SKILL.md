---
name: contrastive-semantic-projection-neuron-labeling
description: "Contrastive Semantic Projection (CSP) for faithful neuron labeling in deep networks using contrastive examples. Two-stage pipeline with VLM-based candidate generation and CLIP-based label assignment. Improves interpretability and explanation faithfulness. Activation: neuron labeling, contrastive examples, neural network interpretability, feature visualization, semantic projection."
---

# Contrastive Semantic Projection for Neuron Labeling

> Two-stage neuron labeling framework using contrastive examples to improve faithfulness and semantic granularity: VLM-based candidate generation followed by CLIP-based label assignment.

## Metadata
- **Source**: arXiv:2604.22477v1
- **Authors**: Neural Network Interpretability Research Team
- **Published**: 2026-04-24
- **Category**: Neural Network Interpretability, Feature Visualization, Explainable AI

## Core Methodology

### Key Innovation
Addresses limitations of existing neuron labeling approaches that rely solely on highly activating examples by incorporating **contrastive examples** - inputs semantically similar to activating examples but eliciting low activations - to sharpen explanations and improve label specificity.

### Two-Stage Pipeline

#### Stage 1: Candidate Label Generation with VLMs
**Problem**: Existing approaches yield broad or misleading labels by focusing on dominant but incidental visual factors.

**Solution**: Use Vision-Language Models (VLMs) with contrastive image sets

**Process**:
```
Input: Activating examples + Contrastive examples
↓
VLM processes both sets
↓
Output: More specific, faithful candidate labels
```

**Why it works**:
- Contrastive examples highlight what the neuron does NOT respond to
- VLMs generate more discriminating descriptions
- Reduces focus on incidental visual factors

#### Stage 2: Label Assignment with CLIP-like Encoders
**Method**: Contrastive Semantic Projection (CSP)

**Extension of SemanticLens**:
- Incorporates contrastive examples directly into scoring pipeline
- Uses CLIP-based similarity scoring
- Improved selection criteria

**Algorithm**:
```
For each candidate label:
1. Compute CLIP similarity to activating examples
2. Compute CLIP similarity to contrastive examples
3. Calculate contrastive score: sim(activate) - sim(contrast)
4. Select label with highest contrastive score
```

## Technical Framework

### Contrastive Example Generation
**Definition**: Inputs that are:
- Semantically similar to activating examples
- But elicit low activations from the neuron

**Generation Methods**:
- FALCON-style approach: Find near neighbors with low activation
- Perturbation-based: Apply targeted modifications
- Synthetic generation: Create semantic variants

### CLIP-Based Scoring
**Components**:
- Image encoder: Projects images to embedding space
- Text encoder: Projects candidate labels to same space
- Similarity metric: Cosine similarity between embeddings

**Contrastive Scoring Function**:
```python
def contrastive_score(label, activate_imgs, contrast_imgs, clip_model):
    label_emb = clip_model.encode_text(label)
    
    # Similarity to activating examples
    activate_embs = clip_model.encode_images(activate_imgs)
    activate_sim = mean(cosine_similarity(label_emb, activate_embs))
    
    # Similarity to contrastive examples
    contrast_embs = clip_model.encode_images(contrast_imgs)
    contrast_sim = mean(cosine_similarity(label_emb, contrast_embs))
    
    # Contrastive score
    return activate_sim - contrast_sim
```

## Implementation Guide

### Prerequisites
- Vision-Language Model (e.g., CLIP, BLIP)
- Pre-trained neural network for analysis
- Dataset of images for activation analysis
- Access to neuron activation values

### Step-by-Step

#### 1. Collect Activating Examples
```python
def collect_activating_examples(model, dataset, neuron_id, top_k=10):
    """
    Find images with highest activation for given neuron
    """
    activations = []
    for img in dataset:
        act = model.get_activation(img, neuron_id)
        activations.append((img, act))
    
    # Sort by activation
    activations.sort(key=lambda x: x[1], reverse=True)
    return [img for img, _ in activations[:top_k]]
```

#### 2. Generate Contrastive Examples
```python
def generate_contrastive_examples(model, activating_imgs, neuron_id, n=10):
    """
    Generate contrastive examples (semantic similar, low activation)
    """
    contrastive = []
    # Implementation depends on FALCON or similar approach
    # Find semantically similar images with low activation
    return contrastive
```

#### 3. Generate Candidate Labels with VLM
```python
def generate_labels_with_vlm(vlm_model, activating_imgs, contrastive_imgs):
    """
    Use VLM to generate candidate labels given both image sets
    """
    prompt = """
    These images HIGHLY activate the neuron: [activating images]
    These similar images DO NOT activate the neuron: [contrastive images]
    What concept does this neuron detect?
    """
    candidates = vlm_model.generate(prompt)
    return candidates
```

#### 4. Apply Contrastive Semantic Projection
```python
def csp_label_selection(candidate_labels, activating_imgs, 
                        contrastive_imgs, clip_model):
    """
    Select best label using contrastive semantic projection
    """
    best_label = None
    best_score = -inf
    
    for label in candidate_labels:
        score = contrastive_score(label, activating_imgs, 
                                   contrastive_imgs, clip_model)
        if score > best_score:
            best_score = score
            best_label = label
    
    return best_label, best_score
```

## Applications

### Neural Network Interpretability
- Automated neuron labeling for deep networks
- Feature visualization with semantic descriptions
- Network architecture understanding

### Model Debugging
- Identifying spurious correlations
- Detecting unintended behaviors
- Validating model learning

### Scientific Discovery
- Understanding visual representations
- Comparing across model architectures
- Tracking concept evolution during training

## Case Study: Melanoma Detection
**Application**: Analyzing neurons in skin lesion classification

**Findings**:
- CSP labels more faithful to actual neuron function
- Improved semantic granularity over baselines
- Better identification of clinically relevant features

## Pitfalls

### Limitations
- Requires access to model internals (activations)
- Computationally expensive for large networks
- VLM bias may affect candidate generation
- Contrastive example quality critical

### Common Issues
1. **Poor contrastive examples**: May not effectively discriminate
2. **VLM hallucination**: Generated labels may not match visual content
3. **CLIP bias**: Text-image alignment limitations
4. **Activation noise**: Unstable neuron responses

## Evaluation Metrics

### Faithfulness
- Alignment with human annotations
- Consistency across similar neurons
- Robustness to input perturbations

### Semantic Granularity
- Specificity of labels
- Discriminative power
- Hierarchy capture

## Related Skills
- llm-concept-neurons-control
- representation-steering
- brain-inspired-capture-evidence-driven

## References
- arXiv:2604.22477v1 - Contrastive Semantic Projection: Faithful Neuron Labeling with Contrastive Examples
- FALCON (prior work on contrastive examples)
- SemanticLens (baseline method)
