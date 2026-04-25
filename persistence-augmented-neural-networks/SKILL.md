---
name: persistence-augmented-neural-networks
description: "Persistence-based data augmentation framework using Morse-Smale complex for neural networks. Encodes local gradient flow regions and hierarchical evolution for improved classification. Compatible with CNNs and GNNs. Activation: persistence augmentation, Morse-Smale complex, topological data augmentation, TDA neural networks, 持续同调增强, 拓扑数据增强."
---

# Persistence-Augmented Neural Networks

## Description

Topological Data Analysis (TDA) provides powerful tools to describe the shape of data, but integrating topological features into deep learning pipelines remains challenging, especially when preserving local geometric structure rather than summarizing it globally. This skill implements a persistence-based data augmentation framework that encodes local gradient flow regions and their hierarchical evolution using the Morse-Smale complex. This representation is compatible with both convolutional and graph neural networks, retaining spatially localized topological information across multiple scales.

## Paper Reference

- **Title**: Persistence-Augmented Neural Networks
- **Authors**: Elena Xinyi Wang, Arnur Nigmetov, Dmitriy Morozov
- **arXiv ID**: 2604.08469v1
- **Published**: 2026-04-09
- **PDF**: https://arxiv.org/pdf/2604.08469v1

## Key Contributions

1. **Persistence-Based Augmentation**: Novel data augmentation using topological persistence
2. **Morse-Smale Complex**: Encodes local gradient flow regions and hierarchical evolution
3. **Multi-Scale Representation**: Retains spatially localized topological information
4. **Network Agnostic**: Compatible with both CNNs and Graph Neural Networks
5. **Efficient Computation**: O(n log n) complexity makes it practical for large datasets
6. **Local Structure Preservation**: Preserves local geometric structure rather than global summary

## Core Concepts

### Topological Data Analysis (TDA)
TDA provides tools to describe the shape of data:
- **Persistent Homology**: Tracks topological features across scales
- **Morse Theory**: Studies gradient flows and critical points
- **Morse-Smale Complex**: Decomposes space based on gradient flows

### Morse-Smale Complex
```
Input: Scalar function f on manifold M
↓
Find critical points (minima, saddles, maxima)
↓
Compute gradient flow trajectories
↓
Decompose M into regions (ascending/descending manifolds)
↓
Extract hierarchical structure (persistence)
```

### Persistence Augmentation Pipeline
```
Input Image/Data
↓
Compute gradient magnitude
↓
Build Morse-Smale complex
↓
Extract persistence diagram
↓
Encode as augmentation features
↓
Concatenate with original features
↓
Neural Network (CNN/GNN)
```

## Latest Paper

- **Title**: Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **arXiv**: 2604.14096v1
- **Published**: 2026-04-15
- **Authors**: Laurent U Perrinet
- **PDF**: https://arxiv.org/abs/2604.14096v1

## Activation Keywords

- persistence augmentation
- Morse-Smale complex
- topological data augmentation
- TDA neural networks
- 持续同调增强
- 拓扑数据增强
- persistence diagram
- gradient flow encoding
- topological features
- Morse theory deep learning

## Tools Used

- **python**: Implementation of augmentation framework
- **torch**: PyTorch for neural network integration
- **numpy**: Numerical computations
- **scipy**: Scientific computing utilities
- **gudhi**: Topological data analysis library
- **scikit-tda**: scikit-tda for persistent homology

## Implementation

### Core Algorithm

```python
import numpy as np
import torch
import torch.nn as nn
from typing import Tuple, List
import gudhi as gd

class PersistenceAugmentor:
    """
    Persistence-based data augmentation using Morse-Smale complex
    """
    def __init__(self, 
                 max_dimension: int = 2,
                 persistence_threshold: float = 0.1,
                 num_persistence_points: int = 100):
        self.max_dimension = max_dimension
        self.persistence_threshold = persistence_threshold
        self.num_persistence_points = num_persistence_points
    
    def compute_morse_smale_complex(self, image: np.ndarray) -> Tuple[np.ndarray, dict]:
        """
        Compute Morse-Smale complex from image
        
        Args:
            image: Input image (H, W) or (H, W, C)
        
        Returns:
            morse_complex: Morse-Smale decomposition
            persistence_info: Persistence diagram and hierarchy
        """
        # Convert to grayscale if needed
        if image.ndim == 3:
            scalar_field = np.mean(image, axis=2)
        else:
            scalar_field = image
        
        # Compute gradient magnitude
        gy, gx = np.gradient(scalar_field)
        gradient_magnitude = np.sqrt(gx**2 + gy**2)
        
        # Build cubical complex for persistence computation
        cc = gd.CubicalComplex(
            dimensions=scalar_field.shape,
            top_dimensional_cells=scalar_field.flatten()
        )
        
        # Compute persistence diagram
        persistence = cc.persistence()
        persistence_diagram = cc.persistence_intervals_in_dimension(0)
        
        # Extract Morse-Smale complex structure
        # (simplified - full implementation uses gradient flow tracing)
        morse_complex = self._extract_morse_smale(gradient_magnitude, scalar_field)
        
        persistence_info = {
            'diagram': persistence_diagram,
            'betti_numbers': cc.betti_numbers(),
            'gradient_magnitude': gradient_magnitude
        }
        
        return morse_complex, persistence_info
    
    def _extract_morse_smale(self, 
                            gradient_magnitude: np.ndarray,
                            scalar_field: np.ndarray) -> np.ndarray:
        """
        Extract Morse-Smale complex regions
        """
        # Find critical points (simplified)
        from scipy.ndimage import maximum_filter, minimum_filter
        
        local_max = maximum_filter(scalar_field, size=3) == scalar_field
        local_min = minimum_filter(scalar_field, size=3) == scalar_field
        
        # Mark regions based on gradient flow
        regions = np.zeros_like(scalar_field, dtype=int)
        regions[local_max] = 2  # Maxima
        regions[local_min] = 1  # Minima
        
        return regions
    
    def encode_persistence_features(self, 
                                   persistence_info: dict,
                                   target_shape: Tuple[int, ...]) -> np.ndarray:
        """
        Encode persistence diagram as feature augmentation
        
        Args:
            persistence_info: Dictionary with persistence data
            target_shape: Target shape for output features
        
        Returns:
            encoded_features: Persistence-based features
        """
        diagram = persistence_info['diagram']
        
        # Vectorize persistence diagram
        # Use persistence image or other vectorization
        num_points = min(len(diagram), self.num_persistence_points)
        
        features = np.zeros((num_points, 2))
        if len(diagram) > 0:
            # Birth-death pairs
            valid_pairs = [(b, d) for b, d in diagram if d - b > self.persistence_threshold]
            for i, (birth, death) in enumerate(valid_pairs[:num_points]):
                features[i] = [birth, death - birth]  # birth, persistence
        
        # Reshape to target shape
        if len(target_shape) == 2:
            # Flatten and pad/truncate
            flat_features = features.flatten()
            target_size = target_shape[0] * target_shape[1]
            if len(flat_features) < target_size:
                flat_features = np.pad(flat_features, 
                                      (0, target_size - len(flat_features)))
            else:
                flat_features = flat_features[:target_size]
            return flat_features.reshape(target_shape)
        
        return features
    
    def augment(self, image: np.ndarray) -> np.ndarray:
        """
        Apply persistence-based augmentation
        
        Args:
            image: Input image
        
        Returns:
            augmented: Image with persistence features concatenated
        """
        morse_complex, persistence_info = self.compute_morse_smale_complex(image)
        
        # Encode persistence features
        if image.ndim == 2:
            target_shape = image.shape
        else:
            target_shape = image.shape[:2]
        
        persistence_features = self.encode_persistence_features(
            persistence_info, target_shape
        )
        
        # Concatenate as additional channel
        if image.ndim == 2:
            augmented = np.stack([image, persistence_features], axis=-1)
        else:
            augmented = np.concatenate([image, 
                                       persistence_features[..., np.newaxis]], 
                                      axis=-1)
        
        return augmented


class PersistenceAugmentedCNN(nn.Module):
    """
    CNN with persistence-based augmentation
    """
    def __init__(self, 
                 num_classes: int = 10,
                 in_channels: int = 4,  # RGB + persistence
                 persistence_augmentor: PersistenceAugmentor = None):
        super().__init__()
        
        self.persistence_augmentor = persistence_augmentor or PersistenceAugmentor()
        
        # Standard CNN backbone
        self.features = nn.Sequential(
            nn.Conv2d(in_channels, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(128, 256, 3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1))
        )
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, num_classes)
        )
    
    def forward(self, x: torch.Tensor, 
                apply_augmentation: bool = True) -> torch.Tensor:
        """
        Forward pass with optional persistence augmentation
        """
        if apply_augmentation and self.training:
            # Apply persistence augmentation to each image in batch
            augmented = []
            for img in x:
                img_np = img.cpu().numpy()
                aug = self.persistence_augmentor.augment(img_np)
                augmented.append(torch.from_numpy(aug).to(x.device))
            x = torch.stack(augmented)
        
        x = self.features(x)
        x = self.classifier(x)
        return x
```

### Usage Example

```python
import torch
import numpy as np
from persistence_augmented_nn import PersistenceAugmentor, PersistenceAugmentedCNN

# Initialize augmentor
augmentor = PersistenceAugmentor(
    max_dimension=2,
    persistence_threshold=0.1,
    num_persistence_points=100
)

# Create model
model = PersistenceAugmentedCNN(
    num_classes=10,
    in_channels=4,  # 3 RGB + 1 persistence
    persistence_augmentor=augmentor
)

# Training loop
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = torch.nn.CrossEntropyLoss()

for batch in dataloader:
    images, labels = batch
    
    # Forward pass (automatically applies augmentation during training)
    outputs = model(images, apply_augmentation=True)
    loss = criterion(outputs, labels)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

## Applications

### Histopathology Image Classification
- **Challenge**: Complex tissue structures with multi-scale patterns
- **Solution**: Persistence augmentation captures topological tissue features
- **Benefit**: Improved classification of cancer subtypes

### 3D Porous Media Analysis
- **Challenge**: Characterizing pore connectivity and flow paths
- **Solution**: Morse-Smale complex captures flow topology
- **Benefit**: Better prediction of material properties

### Medical Imaging
- **Challenge**: Detecting subtle structural abnormalities
- **Solution**: Topological features highlight shape anomalies
- **Benefit**: Enhanced diagnostic accuracy

### Scientific Computing
- **Challenge**: Analyzing complex physical simulations
- **Solution**: Persistence tracks feature evolution
- **Benefit**: Better understanding of dynamic processes

## Advantages

1. **Preserves Local Structure**: Unlike global summaries, keeps local geometric info
2. **Multi-Scale**: Captures features at different scales via persistence
3. **Efficient**: O(n log n) computation suitable for large datasets
4. **Flexible**: Works with both CNNs and GNNs
5. **Interpretable**: Topological features have geometric meaning
6. **Robust**: Persistence is stable under perturbations

## Limitations

1. **Computational Cost**: More expensive than standard augmentations
2. **Hyperparameter Sensitivity**: Requires tuning persistence threshold
3. **Dimensionality**: Best suited for 2D/3D data
4. **Library Dependencies**: Requires TDA libraries (GUDHI, etc.)

## Related Work

- **Persistent Homology**: Edelsbrunner et al.
- **Morse Theory**: Milnor, Forman
- **Topological Deep Learning**: Hofer et al.
- **Persistence Images**: Adams et al.
- **Graph Neural Networks**: Kipf & Welling

## References

```bibtex
@article{wang2026persistence,
  title={Persistence-Augmented Neural Networks},
  author={Wang, Elena Xinyi and Nigmetov, Arnur and Morozov, Dmitriy},
  journal={arXiv preprint arXiv:2604.08469},
  year={2026}
}
```

## Instructions for Agents

1. **Understand the Data**: Identify if topological features would be beneficial
2. **Install Dependencies**: Ensure GUDHI or similar TDA library is available
3. **Configure Augmentor**: Set persistence threshold based on data characteristics
4. **Integrate with Model**: Add persistence channel to input
5. **Evaluate**: Compare with and without augmentation
6. **Tune**: Adjust hyperparameters for optimal performance

## Examples

### Example 1: Image Classification with Persistence

**User**: "I want to classify histopathology images using topological features"

**Agent**: 
1. Set up PersistenceAugmentor with appropriate threshold
2. Create PersistenceAugmentedCNN model
3. Train on histopathology dataset
4. Evaluate classification accuracy

### Example 2: Graph Neural Network with Persistence

**User**: "How can I incorporate topological features into my GNN for molecular property prediction?"

**Agent**:
1. Compute persistence diagrams for molecular graphs
2. Encode as node/edge features
3. Integrate into GNN message passing
4. Train and evaluate
