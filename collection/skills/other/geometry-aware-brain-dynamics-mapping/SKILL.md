---
name: geometry-aware-brain-dynamics-mapping
description: "Geometry-Aware Framework for noninvasive whole human brain dynamics mapping. Incorporates individual cortical geometry into electrophysiology for accurate spatiotemporal reconstruction of brain activity. Activation: geometry-aware, brain dynamics mapping, cortical geometry, noninvasive electrophysiology."
---

# Geometry-Aware Framework for Noninvasive Whole Human Brain Dynamics Mapping

> A geometry-aware framework that incorporates individual cortical geometry into noninvasive electrophysiology to accurately reconstruct whole-brain spatiotemporal dynamics from EEG/MEG.

## Metadata
- **Source**: arXiv:2604.25592v1
- **Authors**: Youssuf Saleh, Camille Gontier, Jonathan Arreguit, Denis Rivière, Pamela Villagrán, Bertrand Thirion, Alain Destexhe
- **Published**: 2026-04-28
- **Categories**: q-bio.NC, cs.LG

## Core Methodology

### Problem Statement
Non-invasive electrophysiology (EEG/MEG) lacks methods that accurately reconstruct whole-brain spatiotemporal dynamics while incorporating individual cortical geometry. Current approaches suffer from:
- **Spatial Smearing**: Standard source localization blurs activity across regions
- **Geometry Neglect**: Flattening or ignoring individual cortical folding patterns
- **Temporal Limitations**: Poor temporal resolution in fMRI-based methods
- **Inverse Problem Ill-Posedness**: Non-unique solutions in EEG/MEG source localization

### Key Innovation
Geometry-Aware Framework integrates:
1. **Individual Cortical Geometry**: Uses subject-specific cortical surface meshes
2. **Geometric Deep Learning**: GNN/CNN architectures operating on cortical surfaces
3. **Physics-Informed Regularization**: Enforces biophysical constraints from electromagnetic theory
4. **Spatiotemporal Modeling**: Joint spatial and temporal dynamics reconstruction

### Technical Framework

#### 1. Cortical Geometry Representation

```
Cortical Surface Representation:
├── High-resolution triangular mesh (vertex ~1-2mm)
├── Sulcal-gyral pattern encoding
├── Local curvature features
├── Distance along cortical surface (geodesic)
└── Normal vectors for orientation

Individual Geometry Processing:
1. T1-weighted MRI → Freesurfer reconstruction
2. White matter surface extraction
3. Mesh decimation (100k-200k vertices)
4. Geodesic distance matrix computation
5. Curvature and thickness feature extraction
```

#### 2. Forward Physics Model

The EEG/MEG forward problem maps neural currents to sensor measurements:

```
Y = L · J + ε

Where:
- Y: Sensor measurements [n_sensors × n_timepoints]
- L: Leadfield matrix [n_sensors × n_sources] 
- J: Source currents [n_sources × n_timepoints]
- ε: Noise

Leadfield computation (boundary element method):
L_ij = ∫ G(r_sensor_i, r_source_j) · n_j dA

Where G is the Green's function for the head model
```

#### 3. Geometry-Aware Inverse Solver

```
J* = argmin_J ||Y - L·J||² + λ₁·R_geometry(J) + λ₂·R_temporal(J) + λ₃·R_spatial(J)

Geometry Regularization:
R_geometry(J) = Σᵢ Σⱼ wᵢⱼ · ||Jᵢ - Jⱼ||² · d_geodesic(i,j)⁻¹

Where wᵢⱼ encodes cortical connectivity strength
and d_geodesic is geodesic distance along cortex
```

#### 4. Graph Neural Network Architecture

```python
# Geometry-Aware GNN

Input: Source activity J on cortical mesh vertices

GNN Layers:
1. Spatial Graph Convolution:
   J' = σ( D⁻¹ᐟ² A D⁻¹ᐟ² J W )
   
   Where A is adjacency matrix based on geodesic distance
   D is degree matrix
   W is learnable weights
   σ is activation (e.g., ReLU)

2. Temporal Convolution:
   J'' = TemporalConv(J', kernel_size=K)

3. Geometry-Aware Pooling:
   - Pool across hierarchical cortical parcellations
   - Preserve sulcal-gyral boundaries

Output: Reconstructed spatiotemporal dynamics
```

## Implementation Guide

### Prerequisites
- Python >= 3.8
- PyTorch >= 1.10
- PyTorch Geometric (for GNNs)
- Freesurfer (for cortical reconstruction)
- MNE-Python (for EEG/MEG processing)
- NumPy, SciPy

### Step-by-Step Implementation

#### 1. Cortical Geometry Processing

```python
import nibabel as nib
import numpy as np
from scipy.sparse import csr_matrix
from scipy.spatial.distance import cdist

class CorticalGeometry:
    """
    Process individual cortical geometry for brain mapping
    """
    def __init__(self, surface_file, curvature_file=None):
        """
        Initialize with Freesurfer surface
        
        Args:
            surface_file: Path to .pial or .white surface file
            curvature_file: Optional curvature map
        """
        # Load surface mesh
        self.surf = nib.freesurfer.read_geometry(surface_file)
        self.vertices = self.surf[0]  # [n_vertices, 3]
        self.faces = self.surf[1]    # [n_faces, 3]
        self.n_vertices = len(self.vertices)
        
        # Compute geodesic distances
        self.geo_dist = self._compute_geodesic_distance()
        
        # Curvature features
        if curvature_file:
            self.curvature = nib.freesurfer.read_morph_data(curvature_file)
        else:
            self.curvature = self._estimate_curvature()
        
        # Surface normals
        self.normals = self._compute_normals()
        
    def _compute_geodesic_distance(self, max_dist=50):
        """
        Compute approximate geodesic distances on cortical surface
        """
        from scipy.sparse.csgraph import dijkstra
        
        # Build adjacency from faces
        adj = np.zeros((self.n_vertices, self.n_vertices))
        for face in self.faces:
            for i in range(3):
                for j in range(i+1, 3):
                    v1, v2 = face[i], face[j]
                    dist = np.linalg.norm(self.vertices[v1] - self.vertices[v2])
                    adj[v1, v2] = dist
                    adj[v2, v1] = dist
        
        # Compute geodesic distances (floyd-warshall or dijkstra)
        geo_dist = dijkstra(adj, directed=False, limit=max_dist)
        
        return geo_dist
    
    def _estimate_curvature(self):
        """
        Estimate mean curvature at each vertex
        """
        curvature = np.zeros(self.n_vertices)
        
        for i in range(self.n_vertices):
            # Get neighbors
            neighbors = np.unique(self.faces[
                np.any(self.faces == i, axis=1)
            ].flatten())
            neighbors = neighbors[neighbors != i]
            
            if len(neighbors) > 0:
                # Simple curvature estimate based on local variation
                local_pts = self.vertices[neighbors]
                centroid = np.mean(local_pts, axis=0)
                curvature[i] = np.linalg.norm(self.vertices[i] - centroid)
        
        return curvature
    
    def _compute_normals(self):
        """
        Compute vertex normals as average of face normals
        """
        normals = np.zeros((self.n_vertices, 3))
        
        for face in self.faces:
            v1, v2, v3 = self.vertices[face]
            fnormal = np.cross(v2 - v1, v3 - v1)
            fnormal = fnormal / (np.linalg.norm(fnormal) + 1e-10)
            
            for v in face:
                normals[v] += fnormal
        
        # Normalize
        normals = normals / (np.linalg.norm(normals, axis=1, keepdims=True) + 1e-10)
        
        return normals
    
    def get_geometry_features(self):
        """
        Return geometry features for each vertex
        """
        return {
            'vertices': self.vertices,
            'curvature': self.curvature,
            'normals': self.normals,
            'geodesic_distance': self.geo_dist,
            'sulcal_depth': self._estimate_sulcal_depth()
        }
    
    def _estimate_sulcal_depth(self):
        """
        Estimate sulcal depth as proxy for folding
        """
        # Simple proxy: distance from convex hull
        from scipy.spatial import ConvexHull
        hull = ConvexHull(self.vertices)
        
        # For each vertex, distance to nearest hull point
        hull_pts = self.vertices[hull.vertices]
        depths = np.min(cdist(self.vertices, hull_pts), axis=1)
        
        return depths
```

#### 2. Leadfield Computation

```python
import mne
import numpy as np

class ForwardModel:
    """
    Compute EEG/MEG forward model with geometry
    """
    def __init__(self, info, trans, bem, src):
        """
        Args:
            info: MNE info structure with sensor positions
            trans: MRI-to-head transformation
            bem: Boundary element model
            src: Source space (cortical surface)
        """
        self.info = info
        self.trans = trans
        self.bem = bem
        self.src = src
        
        # Compute leadfield
        self.leadfield = self._compute_leadfield()
        
    def _compute_leadfield(self):
        """
        Compute leadfield matrix using BEM
        """
        from mne.forward import make_forward_solution
        
        fwd = make_forward_solution(
            self.info, self.trans, self.src, self.bem,
            meg=True, eeg=True, mindist=5.0
        )
        
        # Extract leadfield as dense matrix
        leadfield = fwd['sol']['data']  # [n_sensors, n_sources*3]
        
        # For simplified orientation (normal to cortex)
        n_sources = len(self.src[0]['vertno'])
        leadfield_normal = np.zeros((leadfield.shape[0], n_sources))
        
        for i in range(n_sources):
            # Get orientation (normal to surface)
            nn = self.src[0]['nn'][i]
            # Extract normal component
            idx = slice(i*3, (i+1)*3)
            leadfield_normal[:, i] = leadfield[:, idx] @ nn
        
        return leadfield_normal
    
    def project_to_sensors(self, source_activity):
        """
        Project source activity to sensor space
        
        Args:
            source_activity: [n_sources, n_times]
        
        Returns:
            sensor_data: [n_sensors, n_times]
        """
        return self.leadfield @ source_activity
    
    def get_snr_weights(self, noise_cov):
        """
        Compute SNR-based sensor weighting
        """
        noise_var = np.diag(noise_cov)
        weights = 1.0 / (noise_var + 1e-10)
        return weights
```

#### 3. Geometry-Aware GNN

```python
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv, GATConv, global_mean_pool
from torch_geometric.data import Data

class GeometryAwareGNN(nn.Module):
    """
    Graph Neural Network operating on cortical surface
    """
    def __init__(self, in_channels=1, hidden_channels=64, num_layers=4):
        super().__init__()
        
        self.convs = nn.ModuleList()
        self.batch_norms = nn.ModuleList()
        
        # First layer
        self.convs.append(GATConv(in_channels, hidden_channels, heads=4, concat=False))
        self.batch_norms.append(nn.BatchNorm1d(hidden_channels))
        
        # Hidden layers
        for _ in range(num_layers - 1):
            self.convs.append(GATConv(hidden_channels, hidden_channels, heads=4, concat=False))
            self.batch_norms.append(nn.BatchNorm1d(hidden_channels))
        
        self.temporal_conv = nn.Conv1d(hidden_channels, hidden_channels, kernel_size=3, padding=1)
        
    def forward(self, x, edge_index, edge_attr=None, batch=None):
        """
        Args:
            x: Node features [n_nodes, in_channels, n_time]
            edge_index: Graph connectivity [2, n_edges]
            edge_attr: Edge weights (geodesic distance) [n_edges]
        """
        n_time = x.shape[2]
        outputs = []
        
        # Process each timepoint
        for t in range(n_time):
            x_t = x[:, :, t]  # [n_nodes, in_channels]
            
            # Graph convolutions
            for conv, bn in zip(self.convs, self.batch_norms):
                x_t = conv(x_t, edge_index, edge_attr)
                x_t = bn(x_t)
                x_t = torch.relu(x_t)
            
            outputs.append(x_t)
        
        # Stack temporal
        x = torch.stack(outputs, dim=2)  # [n_nodes, hidden_channels, n_time]
        
        # Temporal convolution
        x = self.temporal_conv(x)
        
        return x

class BrainDynamicsReconstructor(nn.Module):
    """
    End-to-end brain dynamics reconstruction
    """
    def __init__(self, n_sensors, n_sources, geometry_info):
        super().__init__()
        
        self.n_sensors = n_sensors
        self.n_sources = n_sources
        
        # Sensor to source mapping
        self.sensor_encoder = nn.Sequential(
            nn.Linear(n_sensors, 256),
            nn.ReLU(),
            nn.Linear(256, 128)
        )
        
        # Graph network on cortical surface
        self.gnn = GeometryAwareGNN(in_channels=128, hidden_channels=64)
        
        # Source decoder
        self.source_decoder = nn.Sequential(
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)  # Reconstructed source amplitude
        )
        
        # Learned leadfield refinement
        self.leadfield_correction = nn.Linear(n_sources, n_sources, bias=False)
        
        # Store geometry
        self.edge_index = geometry_info['edge_index']
        self.edge_attr = geometry_info.get('edge_attr')
        
    def forward(self, sensor_data):
        """
        Reconstruct source activity from sensor data
        
        Args:
            sensor_data: [batch, n_sensors, n_time]
        
        Returns:
            source_activity: [batch, n_sources, n_time]
        """
        batch_size, n_time = sensor_data.shape[0], sensor_data.shape[2]
        
        # Encode sensor data
        sensor_encoded = []
        for t in range(n_time):
            enc = self.sensor_encoder(sensor_data[:, :, t])
            sensor_encoded.append(enc)
        
        sensor_encoded = torch.stack(sensor_encoded, dim=2)  # [batch, 128, n_time]
        
        # Prepare batch for GNN
        all_sources = []
        for b in range(batch_size):
            # Repeat encoded features for each source
            x = sensor_encoded[b].unsqueeze(0).repeat(self.n_sources, 1, 1)  # [n_sources, 128, n_time]
            
            # GNN forward
            gnn_out = self.gnn(x, self.edge_index, self.edge_attr)  # [n_sources, 64, n_time]
            
            # Decode to source activity
            source_t = []
            for t in range(n_time):
                dec = self.source_decoder(gnn_out[:, :, t])
                source_t.append(dec)
            
            source_activity = torch.stack(source_t, dim=1)  # [n_sources, n_time]
            all_sources.append(source_activity)
        
        return torch.stack(all_sources, dim=0)  # [batch, n_sources, n_time]
```

#### 4. Training with Physics Constraints

```python
class GeometryAwareLoss(nn.Module):
    """
    Multi-component loss with geometry constraints
    """
    def __init__(self, leadfield, geo_dist, lambda_data=1.0, 
                 lambda_smooth=0.1, lambda_geodesic=0.05):
        super().__init__()
        self.leadfield = leadfield
        self.geo_dist = geo_dist
        self.lambda_data = lambda_data
        self.lambda_smooth = lambda_smooth
        self.lambda_geodesic = lambda_geodesic
        
    def forward(self, pred_sources, true_sources, sensor_data):
        """
        Compute geometry-aware loss
        
        Args:
            pred_sources: [batch, n_sources, n_time]
            true_sources: [batch, n_sources, n_time]
            sensor_data: [batch, n_sensors, n_time]
        """
        # Data fidelity: reconstructed sensors should match
        pred_sensors = torch.matmul(self.leadfield, pred_sources)
        loss_data = torch.mean((pred_sensors - sensor_data)**2)
        
        # Source prediction loss
        loss_source = torch.mean((pred_sources - true_sources)**2)
        
        # Spatial smoothness (geometry-aware)
        # Nearby sources on cortex should have similar activity
        loss_smooth = self._geometry_smoothness(pred_sources)
        
        # Geodesic distance regularization
        loss_geodesic = self._geodesic_regularization(pred_sources)
        
        total_loss = (self.lambda_data * loss_data + 
                     loss_source + 
                     self.lambda_smooth * loss_smooth +
                     self.lambda_geodesic * loss_geodesic)
        
        return {
            'total': total_loss,
            'data': loss_data,
            'source': loss_source,
            'smooth': loss_smooth,
            'geodesic': loss_geodesic
        }
    
    def _geometry_smoothness(self, sources):
        """
        Enforce smoothness along cortical surface
        """
        batch_size, n_sources, n_time = sources.shape
        
        # Compute pairwise differences
        diff = sources.unsqueeze(2) - sources.unsqueeze(1)  # [batch, n_sources, n_sources, n_time]
        
        # Weight by inverse geodesic distance
        weight = torch.exp(-self.geo_dist / torch.median(self.geo_dist))  # Closer = more similar
        weight = weight.unsqueeze(0).unsqueeze(-1)  # [1, n_sources, n_sources, 1]
        
        loss = torch.mean(weight * diff**2)
        
        return loss
    
    def _geodesic_regularization(self, sources):
        """
        Regularize based on geodesic distance along cortex
        """
        # Penalize high-frequency spatial patterns
        # (implementation depends on specific parcellation)
        return torch.tensor(0.0)  # Placeholder
```

## Applications

1. **Precision Neuromedicine**: Subject-specific brain activity mapping
2. **Real-time Neuroimaging**: Online dynamics reconstruction
3. **Brain-Computer Interfaces**: Accurate cortical state estimation
4. **Cognitive Neuroscience**: High-resolution spatiotemporal analysis
5. **Clinical Diagnostics**: Patient-specific brain dynamics for epilepsy, stroke

## Key Features

- **Individual Geometry**: Subject-specific cortical surface incorporation
- **End-to-end Learning**: Direct sensor-to-source mapping
- **Physics Constraints**: Biophysically plausible reconstructions
- **Geodesic Regularization**: Anatomically-informed smoothness
- **Multi-scale**: Operates at multiple spatial resolutions

## Pitfalls

1. **Mesh Quality**: Requires high-quality individual cortical surfaces
2. **Computational Cost**: Geodesic distance computation is expensive
3. **Registration**: MRI-to-head coordinate alignment critical
4. **Head Model**: BEM accuracy affects forward solution
5. **Training Data**: Needs paired source-sensor data (simulated or intra-cranial)

## Related Skills
- geometric-brain-dynamics-mapping
- eeg-visual-attention-decoding
- brain-dit-fmri-foundation-model

## References
```
Saleh, Y., et al. (2026). A geometry aware framework enhances noninvasive 
mapping of whole human brain dynamics. 
arXiv preprint arXiv:2604.25592v1.
```
