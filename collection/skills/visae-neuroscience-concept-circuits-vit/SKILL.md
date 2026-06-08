---
name: visae-neuroscience-concept-circuits-vit
description: "ViSAE - Neuroscience-Motivated Concept Circuits for Interpreting and Steering Vision Transformers. Use when: (1) Mechanistic interpretability of Vision Transformers (ViT), (2) Sparse Autoencoder-based model understanding, (3) Concept circuit discovery and tracing, (4) Top-down concept reading and Bottom-up circuit tracing, (5) Auditing and steering ViT behavior, (6) Spurious cue detection and concept editing. Triggers: ViSAE, concept circuit, ViT interpretability, sparse autoencoder, mechanistic interpretability, concept editing, model steering, visual concept discovery."
license: Complete terms in LICENSE.txt
---

# ViSAE: Neuroscience-Motivated Concept Circuits for ViT Interpretability

arXiv:2606.06664 - ICML 2026 (acceptance rate 26.6%)

## Core Innovation

**ViSAE** is a mechanistic interpretability toolbox for understanding Vision Transformer inner workings through concept circuits, inspired by neuroscience principles.

### Three Components

1. **Probing Suite**: 64K images + 16K visually grounded concept vocabulary
2. **Circuit Algorithms**: Top-down concept reading + Bottom-up circuit tracing
3. **Applications**: Auditing and steering ViT behavior

## Implementation Guide

### 1. Concept Vocabulary Construction

```python
import torch
import numpy as np
from PIL import Image

class ConceptVocabulary:
    """
    16K visually grounded concept vocabulary for ViT interpretation.
    20x concept coverage efficiency over ImageNet.
    """
    
    def __init__(self, vocab_size=16000):
        self.vocab_size = vocab_size
        self.concepts = self._load_concept_set()
        
    def _load_concept_set(self):
        """
        Load comprehensive visual concept vocabulary.
        Categories: colors, textures, shapes, objects, scenes, attributes
        """
        concepts = {
            'colors': ['red', 'blue', 'green', 'yellow', 'orange', 'purple', ...],
            'textures': ['smooth', 'rough', 'striped', 'dotted', 'gradient', ...],
            'shapes': ['circular', 'rectangular', 'triangular', 'oval', ...],
            'objects': ['car', 'person', 'building', 'tree', 'animal', ...],
            'scenes': ['indoor', 'outdoor', 'urban', 'natural', 'water', ...],
            'attributes': ['bright', 'dark', 'large', 'small', 'centered', ...]
        }
        
        # Flatten to unified vocabulary
        all_concepts = []
        for category, items in concepts.items():
            all_concepts.extend(items)
        
        return all_concepts[:self.vocab_size]
    
    def probe_concept_activation(self, image, vit_model, concept):
        """
        Probe specific concept activation in ViT representations.
        
        Args:
            image: Input image
            vit_model: Pre-trained ViT
            concept: Target concept from vocabulary
        
        Returns:
            activation: Concept activation score
        """
        # Extract ViT features
        features = vit_model.extract_features(image)
        
        # Compute concept alignment
        concept_embedding = self._get_concept_embedding(concept)
        activation = torch.cosine_similarity(features, concept_embedding)
        
        return activation.item()
```

### 2. Sparse Autoencoder Architecture

```python
import torch.nn as nn

class SparseAutoencoder(nn.Module):
    """
    Sparse Autoencoder for decomposing ViT representations into interpretable concepts.
    """
    
    def __init__(self, input_dim, hidden_dim, sparsity_target=0.05):
        super().__init__()
        
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(hidden_dim, input_dim),
            nn.Identity(),
        )
        
        self.sparsity_target = sparsity_target
        
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        
        return encoded, decoded
    
    def sparsity_loss(self, encoded):
        """
        KL divergence sparsity penalty for concept isolation.
        """
        avg_activation = torch.mean(encoded, dim=0)
        kl_div = self.sparsity_target * torch.log(
            self.sparsity_target / (avg_activation + 1e-8)
        ) + (1 - self.sparsity_target) * torch.log(
            (1 - self.sparsity_target) / (1 - avg_activation + 1e-8)
        )
        
        return torch.sum(kl_div)
```

### 3. Top-Down Concept Reading

```python
def top_down_concept_reading(vit_features, sae_decoder, target_concept):
    """
    Recover ViT inner workings via top-down concept reading.
    
    Process:
    1. Identify concept neurons in SAE hidden layer
    2. Trace activations back through decoder
    3. Map to ViT attention heads and layers
    """
    # Find concept neurons with high activation
    concept_neurons = find_concept_neurons(sae_decoder, target_concept)
    
    # Trace backward through decoder weights
    decoder_weights = sae_decoder.weight
    
    # Map to ViT attention patterns
    attention_mapping = {}
    for neuron_idx in concept_neurons:
        weights = decoder_weights[neuron_idx]
        
        # Identify influential ViT layers
        layer_importance = compute_layer_importance(weights)
        attention_mapping[neuron_idx] = layer_importance
    
    return attention_mapping

def find_concept_neurons(sae_decoder, concept):
    """
    Identify neurons encoding specific concept.
    """
    concept_embedding = get_concept_embedding(concept)
    
    # Compute neuron-concept alignment
    decoder_weights = sae_decoder.weight
    alignments = torch.cosine_similarity(
        decoder_weights, 
        concept_embedding.unsqueeze(0)
    )
    
    # Select top neurons
    top_neurons = torch.topk(alignments, k=10).indices
    
    return top_neurons.tolist()
```

### 4. Bottom-Up Circuit Tracing

```python
def bottom_up_circuit_tracing(vit_model, sae_encoder, input_image):
    """
    Automatically recover ViT circuit via bottom-up tracing.
    
    Process:
    1. Extract ViT features from input
    2. Encode to SAE concept space
    3. Identify active concepts
    4. Trace circuit pathways
    """
    # Extract ViT intermediate features
    layer_features = extract_intermediate_features(vit_model, input_image)
    
    # Encode each layer to concept space
    concept_activations = {}
    for layer_name, features in layer_features.items():
        encoded = sae_encoder(features)
        active_concepts = identify_active_concepts(encoded, threshold=0.3)
        concept_activations[layer_name] = active_concepts
    
    # Build circuit graph
    circuit_graph = build_circuit_graph(concept_activations)
    
    return circuit_graph

def identify_active_concepts(encoded, threshold=0.3):
    """
    Identify concepts with significant activation.
    """
    active_mask = encoded > threshold
    active_indices = torch.where(active_mask)[0].tolist()
    
    # Map indices to concept names
    active_concepts = [concept_vocabulary[idx] for idx in active_indices]
    
    return active_concepts

def build_circuit_graph(concept_activations):
    """
    Construct circuit graph from concept flow.
    """
    import networkx as nx
    
    G = nx.DiGraph()
    
    # Add nodes for each layer-concept
    for layer, concepts in concept_activations.items():
        for concept in concepts:
            G.add_node(f"{layer}:{concept}")
    
    # Add edges for concept flow
    layers = sorted(concept_activations.keys())
    for i in range(len(layers) - 1):
        source_layer = layers[i]
        target_layer = layers[i + 1]
        
        for src_concept in concept_activations[source_layer]:
            for tgt_concept in concept_activations[target_layer]:
                # Compute concept transition probability
                prob = compute_transition_prob(src_concept, tgt_concept)
                if prob > 0.1:
                    G.add_edge(
                        f"{source_layer}:{src_concept}",
                        f"{target_layer}:{tgt_concept}",
                        weight=prob
                    )
    
    return G
```

### 5. Concept Editing for Behavior Steering

```python
def concept_editing(vit_model, sae, input_image, target_concept, edit_value):
    """
    Edit ViT behavior by modifying concept activations.
    
    Args:
        edit_value: Modification to concept activation (+/-)
    
    Returns:
        edited_output: ViT output after concept intervention
    """
    # Extract original features
    original_features = vit_model.extract_features(input_image)
    
    # Encode to concept space
    encoded = sae.encoder(original_features)
    
    # Find target concept neuron
    concept_idx = find_concept_index(target_concept)
    
    # Apply intervention
    edited_encoded = encoded.clone()
    edited_encoded[concept_idx] += edit_value
    
    # Decode back to feature space
    edited_features = sae.decoder(edited_encoded)
    
    # Compute edited ViT output
    edited_output = vit_model.classify_from_features(edited_features)
    
    return edited_output

def worst_group_accuracy_improvement(dataset, target_concepts):
    """
    Improve worst-group accuracy via concept editing.
    WaterBirds: 48.2% improvement, outperforming existing methods by 23.8%
    """
    worst_group = identify_worst_group(dataset)
    
    improvements = []
    for sample in worst_group:
        # Identify problematic concepts
        problematic_concepts = diagnose_prediction(sample)
        
        # Apply targeted edits
        edited_output = concept_editing(
            vit_model, sae, sample.image,
            problematic_concepts[0],
            edit_value=-0.5
        )
        
        improvements.append(edited_output)
    
    return compute_accuracy(improvements)
```

## Experimental Results

| Metric | Performance |
|--------|-------------|
| Concept coverage efficiency | 20x over ImageNet |
| Interpretation accuracy | 28.7% improvement |
| WaterBirds worst-group accuracy | 48.2% improvement |
| vs. existing methods | +23.8% |

## Key Advantages

1. **Large Concept Vocabulary**: 16K concepts, comprehensive coverage
2. **Automated Circuit Discovery**: Top-down + Bottom-up tracing
3. **Behavior Steering**: Concept editing for targeted interventions
4. **Spurious Cue Detection**: Identify and remove biases

## Applications

- ViT mechanistic interpretability
- Model debugging and auditing
- Bias detection and mitigation
- Concept-based model editing
- Explainable AI for vision
- Transfer learning analysis

## Code & Data

https://github.com/deep-real/ViSAE

## Activation Keywords

- ViSAE
- concept circuit
- ViT interpretability
- sparse autoencoder
- mechanistic interpretability
- concept editing
- model steering
- visual concept discovery
- Top-down concept reading
- Bottom-up circuit tracing