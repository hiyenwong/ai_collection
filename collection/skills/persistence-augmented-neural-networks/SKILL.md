---
name: persistence-augmented-neural-networks
description: Persistence-based data augmentation framework using topological data analysis (TDA) and Morse-Smale complexes. Encodes local gradient flow regions for improved deep learning.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [topological-data-analysis, persistence, neural-networks, data-augmentation, morse-smale, deep-learning]
    source_paper: "Persistence-Augmented Neural Networks (arXiv:2604.08469)"
    authors: "Elena Xinyi Wang, Arnur Nigmetov, Dmitriy Morozov"
    published: "2026-04-09"
---

# Persistence-Augmented Neural Networks

Persistence-based data augmentation framework using Topological Data Analysis (TDA) that encodes local gradient flow regions and their hierarchical evolution using Morse-Smale complexes.

## Overview

Topological Data Analysis (TDA) provides tools to describe the shape of data, but integrating topological features into deep learning pipelines remains challenging. This methodology proposes a **persistence-based data augmentation framework** that:

- Encodes local gradient flow regions
- Captures hierarchical evolution using Morse-Smale complexes
- Retains spatially localized topological information across multiple scales
- Achieves O(n log n) computational complexity

## Core Concepts

### Morse-Smale Complex

A partition of the domain based on gradient flow:
- **Ascending manifold**: Points flowing to a maximum
- **Descending manifold**: Points flowing from a minimum
- **Morse-Smale cells**: Intersection regions forming a complex

### Persistence Diagram

Tracks topological features across scales:
- **Birth**: Scale at which feature appears
- **Death**: Scale at which feature disappears
- **Persistence**: Lifetime (death - birth)

### Local vs Global TDA

| Approach | Method | Information |
|----------|--------|-------------|
| **Global** | Persistence images/landscapes | Summary statistics |
| **Local** | Morse-Smale augmentation | Spatial localization |

## Mathematical Framework

### Morse-Smale Complex Construction

```python
class MorseSmaleComplex:
    """
    Morse-Smale complex for gradient flow analysis
    """
    def __init__(self, data, function):
        self.data = data
        self.function = function  # Scalar field on data
        
    def compute_critical_points(self):
        """
        Identify critical points (minima, saddles, maxima)
        
        ∇f(x) = 0 and Hessian is non-degenerate
        """
        gradient = self.compute_gradient()
        critical = np.where(np.linalg.norm(gradient, axis=1) < epsilon)[0]
        
        # Classify by Hessian eigenvalues
        self.critical_points = {}
        for cp in critical:
            hessian = self.compute_hessian(cp)
            eigenvals = np.linalg.eigvals(hessian)
            n_negative = np.sum(eigenvals < 0)
            
            if n_negative == 0:
                self.critical_points['minima'].append(cp)
            elif n_negative == len(eigenvals):
                self.critical_points['maxima'].append(cp)
            else:
                self.critical_points['saddles'].append(cp)
        
        return self.critical_points
    
    def compute_ascending_manifolds(self):
        """
        Compute ascending manifolds (flow to maxima)
        
        For each point, follow gradient flow upward
        """
        manifolds = {}
        for max_idx in self.critical_points['maxima']:
            manifolds[max_idx] = self.gradient_flow(max_idx, direction='up')
        return manifolds
    
    def compute_descending_manifolds(self):
        """
        Compute descending manifolds (flow from minima)
        
        For each point, follow negative gradient flow
        """
        manifolds = {}
        for min_idx in self.critical_points['minima']:
            manifolds[min_idx] = self.gradient_flow(min_idx, direction='down')
        return manifolds
    
    def compute_ms_cells(self):
        """
        Compute Morse-Smale cells
        
        Intersection of ascending and descending manifolds
        """
        cells = []
        for min_idx in self.critical_points['minima']:
            for max_idx in self.critical_points['maxima']:
                cell = intersect_manifolds(
                    self.descending_manifolds[min_idx],
                    self.ascending_manifolds[max_idx]
                )
                if cell:
                    cells.append({
                        'min': min_idx,
                        'max': max_idx,
                        'points': cell
                    })
        return cells
```

### Persistence Computation

```python
class PersistenceComputation:
    """
    Compute persistent homology
    """
    def __init__(self, filtration):
        self.filtration = filtration  # Simplicial filtration
        
    def compute_persistence(self, max_dim=2):
        """
        Compute persistence pairs
        
        Returns: [(birth, death, dimension)]
        """
        # Union-find for connected components (0-dim)
        # Matrix reduction for higher dimensions
        
        persistence_pairs = []
        
        for dim in range(max_dim + 1):
            pairs = self.reduce_boundary_matrix(dim)
            persistence_pairs.extend(pairs)
        
        return persistence_pairs
    
    def persistence_diagram(self):
        """Convert pairs to diagram format"""
        pairs = self.compute_persistence()
        
        diagram = {}
        for birth, death, dim in pairs:
            if dim not in diagram:
                diagram[dim] = []
            diagram[dim].append((birth, death))
        
        return diagram
    
    def persistence_statistics(self):
        """Compute statistics from persistence diagram"""
        diagram = self.persistence_diagram()
        
        stats = {}
        for dim, points in diagram.items():
            persistences = [death - birth for birth, death in points if death != np.inf]
            stats[dim] = {
                'mean_persistence': np.mean(persistences),
                'max_persistence': np.max(persistences),
                'num_features': len(persistences)
            }
        
        return stats
```

### Augmentation Framework

```python
class PersistenceAugmentation:
    """
    Persistence-based data augmentation
    """
    def __init__(self, n_scales=5):
        self.n_scales = n_scales
        
    def augment(self, data):
        """
        Generate augmented samples using topological features
        
        Args:
            data: Input data (image, graph, etc.)
        
        Returns:
            Augmented data with topological features
        """
        # Step 1: Compute scalar field (e.g., intensity)
        scalar_field = self.compute_scalar_field(data)
        
        # Step 2: Build Morse-Smale complex
        ms_complex = MorseSmaleComplex(data, scalar_field)
        ms_complex.compute_critical_points()
        ms_complex.compute_ascending_manifolds()
        ms_complex.compute_descending_manifolds()
        cells = ms_complex.compute_ms_cells()
        
        # Step 3: Compute persistence
        filtration = self.build_filtration(data)
        persistence = PersistenceComputation(filtration)
        diagram = persistence.persistence_diagram()
        
        # Step 4: Encode features
        features = self.encode_topological_features(
            cells, diagram, data
        )
        
        # Step 5: Generate augmented sample
        augmented = self.combine_with_data(data, features)
        
        return augmented
    
    def encode_topological_features(self, cells, diagram, data):
        """
        Encode topological features in network-compatible format
        
        Compatible with:
        - Convolutional Neural Networks (spatial)
        - Graph Neural Networks (structural)
        """
        # Multi-scale encoding
        features = []
        
        for scale_idx in range(self.n_scales):
            scale_features = self.extract_at_scale(
                cells, diagram, data, scale_idx
            )
            features.append(scale_features)
        
        return np.stack(features, axis=0)
    
    def extract_at_scale(self, cells, diagram, data, scale):
        """Extract features at specific scale"""
        # Filter features by persistence threshold
        threshold = self.scale_to_threshold(scale)
        
        relevant_cells = [
            cell for cell in cells
            if self.cell_persistence(cell) > threshold
        ]
        
        # Encode cell geometry
        encoded = self.encode_cells(relevant_cells, data)
        
        return encoded
```

## Implementation

### For Image Data

```python
class ImagePersistenceAugmentation(PersistenceAugmentation):
    """
    Persistence augmentation for images
    """
    def compute_scalar_field(self, image):
        """Use image intensity or gradient magnitude"""
        if len(image.shape) == 3:
            # RGB - convert to grayscale
            gray = np.mean(image, axis=2)
        else:
            gray = image
        
        # Can also use gradient magnitude
        grad_x = np.gradient(gray, axis=0)
        grad_y = np.gradient(gray, axis=1)
        grad_mag = np.sqrt(grad_x**2 + grad_y**2)
        
        return grad_mag
    
    def encode_cells(self, cells, image):
        """Encode Morse-Smale cells as image channels"""
        # Create feature maps
        n_cells = len(cells)
        feature_map = np.zeros((image.shape[0], image.shape[1], n_cells))
        
        for i, cell in enumerate(cells):
            for point in cell['points']:
                feature_map[point[0], point[1], i] = 1
        
        return feature_map
```

### For Graph Data

```python
class GraphPersistenceAugmentation(PersistenceAugmentation):
    """
    Persistence augmentation for graph data
    """
    def compute_scalar_field(self, graph):
        """Use node features or graph properties"""
        # Could use degree, centrality, etc.
        return nx.degree_centrality(graph)
    
    def build_filtration(self, graph):
        """Build simplicial filtration from graph"""
        # Vietoris-Rips or witness complex
        points = self.graph_to_points(graph)
        return VietorisRipsFiltration(points)
    
    def encode_cells(self, cells, graph):
        """Encode as graph features"""
        # Add topological features as node attributes
        features = {}
        for node in graph.nodes():
            features[node] = self.compute_node_features(node, cells)
        
        nx.set_node_attributes(graph, features)
        return graph
```

## Complexity

- **Morse-Smale complex**: O(n log n) for 2D/3D data
- **Persistence computation**: O(n³) worst case, O(n log n) for filtrations
- **Augmentation**: Linear in number of scales

## Applications

- **Histopathology**: Cancer detection in tissue images
- **Material Science**: Porous material property prediction
- **Scientific Computing**: Analysis of simulation data
- **Computer Vision**: Feature enhancement

## Advantages

1. **Local Information**: Preserves spatial localization
2. **Multi-scale**: Captures features across scales
3. **Interpretable**: Clear topological meaning
4. **Efficient**: O(n log n) complexity
5. **Compatible**: Works with CNNs and GNNs

## References

- Wang, E. X., Nigmetov, A., & Morozov, D. (2026). Persistence-Augmented Neural Networks.

## Related

- [[topological-data-analysis]]
- [[persistent-homology]]
- [[morse-theory]]
- [[data-augmentation]]
- [[computational-topology]]
