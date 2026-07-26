---
name: alzheimer-pet-suvr-network-models
description: "High-fidelity spatio-temporal mathematical models of Alzheimer's disease progression using 3D brain geometries and network-based connectome models, validated against PET-SUVR imaging data. Activation triggers: Alzheimer's disease, brain network modeling, protein propagation, tau pathology, amyloid-beta, PET-SUVR, computational neurodegeneration."
---

# High-fidelity and Network-based Spatio-temporal Mathematical Models of Alzheimer's Disease Progression

> A novel framework comparing 3D patient-specific brain geometries with reduced network-based connectome models for predicting amyloid-beta and tau protein propagation in Alzheimer's disease.

## Metadata
- **Source**: arXiv:2604.18470v1
- **Authors**: Beatrice Caon, Mattia Corti, Francesca Bonizzoni, Paola F. Antonietti
- **Published**: 2026-04-20
- **Category**: Computational Neuroscience, Neurodegeneration

## Core Methodology

### Problem Statement
Alzheimer's disease (AD) progression involves the misfolding and accumulation of two toxic proteins:
- **Amyloid-beta (Aβ)** plaques
- **Tau** neurofibrillary tangles

Mathematical models provide quantitative tools for monitoring disease progression and understanding the spatio-temporal dynamics of protein propagation.

### Dual-Approach Framework

#### Approach 1: High-Fidelity 3D Biophysical Model
- **Geometry**: Patient-specific 3D brain geometries reconstructed from MRI
- **Governing Equations**: Reaction-diffusion PDEs on complex geometries
- **Advantages**: Most accurate and biologically consistent description
- **Limitations**: Computationally demanding

#### Approach 2: Reduced Network-Based Model
- **Graph Structure**: Brain connectome as a graph (nodes = regions, edges = white matter tracts)
- **Formulation**: Graph Laplacian-based dynamics
- **Advantages**: Cheaper computational cost
- **Limitations**: Not always able to achieve reliable results across all brain regions

### Mathematical Formulation

#### 3D Model
```
∂u/∂t = D∇²u + R(u)  (Reaction-diffusion equation)
```
Where:
- u = protein concentration (Aβ or tau)
- D = diffusion coefficient
- R(u) = reaction term (protein production/clearance)

#### Network Model
```
du/dt = -L_G · u + R(u)  (Graph Laplacian dynamics)
```
Where:
- L_G = graph Laplacian of the brain connectome
- u = protein concentration at each node
- R(u) = reaction term

### Validation Strategy
- **PET Tracers**: 18F-AZD4694 (amyloid), 18F-MK6240 (tau)
- **Data Type**: PET Standardized Uptake Value Ratios (SUVR)
- **Comparison**: Model predictions vs. clinical PET-SUVR data
- **Sensitivity Analysis**: Quantify parameter influence on concentration patterns

## Implementation Guide

### Prerequisites
- **MRI Processing**: FreeSurfer or similar for brain geometry reconstruction
- **Numerical PDE Solvers**: FEniCS, COMSOL, or custom finite element code
- **Connectome Data**: Diffusion MRI tractography (e.g., from HCP, ADNI)
- **PET Analysis**: SUVR calculation pipelines

### Step-by-Step

#### Step 1: Data Preparation
1. Acquire structural MRI (T1-weighted)
2. Segment brain into regions of interest
3. Reconstruct 3D surface/volume meshes
4. Process diffusion MRI for tractography (connectome)
5. Acquire PET images and calculate SUVR maps

#### Step 2: Model Setup (3D)
```python
# Pseudo-code for 3D model setup
import fenics as fn

# Load brain geometry
mesh = fn.Mesh('brain_geometry.xml')
V = fn.FunctionSpace(mesh, 'P', 1)

# Define reaction-diffusion problem
u = fn.Function(V)
v = fn.TestFunction(V)

# Diffusion term
D = 0.1  # diffusion coefficient
diffusion = D * fn.dot(fn.grad(u), fn.grad(v)) * fn.dx

# Reaction term (example: logistic growth + clearance)
alpha = 0.5  # production rate
beta = 0.3   # clearance rate
reaction = (alpha * u * (1 - u) - beta * u) * v * fn.dx

# Time stepping
F = (u - u_n)/dt * v * fn.dx + diffusion - reaction
```

#### Step 3: Model Setup (Network)
```python
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply

# Load connectome
connectome = np.load('brain_connectome.npy')  # N x N connectivity matrix
G = nx.from_numpy_array(connectome)
L = nx.laplacian_matrix(G)  # Graph Laplacian

# Network reaction-diffusion
N = len(connectome)
u = np.zeros(N)  # Initial protein concentration

# Simulation loop
for t in range(n_steps):
    # Graph Laplacian diffusion + reaction
    dudt = -L.dot(u) + reaction_term(u)
    u = u + dt * dudt
```

#### Step 4: Parameter Estimation
- Use sensitivity analysis to identify influential parameters
- Calibrate against PET-SUVR data
- Compare regional SUVR predictions

#### Step 5: Model Validation
- Calculate prediction error vs. clinical data
- Compare 3D vs. network model performance
- Assess biological plausibility

### Code Example: Sensitivity Analysis
```python
def sensitivity_analysis(model_func, params, param_ranges):
    """
    Perform sensitivity analysis for model parameters.
    
    Args:
        model_func: Function that runs the model
        params: Dictionary of parameter values
        param_ranges: Dict of {param_name: (min, max)}
    
    Returns:
        sensitivity_scores: Dict of parameter importance
    """
    from SALib.sample import saltelli
    from SALib.analyze import sobol
    
    problem = {
        'num_vars': len(param_ranges),
        'names': list(param_ranges.keys()),
        'bounds': list(param_ranges.values())
    }
    
    param_values = saltelli.sample(problem, 1024)
    outputs = []
    
    for params_sample in param_values:
        params_dict = dict(zip(param_ranges.keys(), params_sample))
        output = model_func(**params_dict)
        outputs.append(output)
    
    Si = sobol.analyze(problem, np.array(outputs))
    return Si

# Example usage
param_ranges = {
    'D': [0.01, 1.0],        # Diffusion coefficient
    'alpha': [0.1, 1.0],     # Production rate
    'beta': [0.01, 0.5],     # Clearance rate
    'u0': [0.0, 0.5]         # Initial concentration
}
```

## Applications

### Clinical Applications
- **Disease Progression Prediction**: Forecast tau/Aβ spread across brain regions
- **Treatment Planning**: Identify optimal intervention targets
- **Clinical Trial Design**: Stratify patients by predicted progression rate
- **Biomarker Development**: Identify early detection signatures

### Research Applications
- **Pathology Understanding**: Mechanistic insights into protein propagation
- **Model Comparison**: Evaluate trade-offs between accuracy and computational cost
- **Connectomics**: Study role of network topology in disease spread
- **Cross-Disease Analysis**: Apply to other proteinopathies (Parkinson's, CTE)

## Pitfalls

### Model Limitations
- **3D Model**: Computationally expensive for large-scale studies
- **Network Model**: May miss local heterogeneity within regions
- **Parameter Identifiability**: Multiple parameter combinations may fit data equally well
- **Patient Variability**: Single model may not capture all patient trajectories

### Validation Challenges
- **PET Noise**: SUVR measurements have inherent uncertainty
- **Regional Variability**: Different brain regions may require different parameters
- **Longitudinal Data**: Limited availability of multi-timepoint data

### Implementation Notes
- **Mesh Quality**: Poor mesh quality can destabilize 3D simulations
- **Graph Construction**: Connectome quality strongly affects network model results
- **Boundary Conditions**: Careful handling of brain boundaries required

## Related Skills
- brain-connectivity-analysis
- graph-laplacian-denoising
- brain-network-controllability
- brain-dit-fmri-foundation-model
- computational-lesions-multilingual-language-models

## References
- Caon et al. (2026). High-fidelity and Network-based Spatio-temporal Mathematical Models of Alzheimer's Disease Progression. arXiv:2604.18470v1
- ADNI (Alzheimer's Disease Neuroimaging Initiative): adni.loni.usc.edu
- Raj et al. (2012). Network diffusion model of disease progression. Neuron.
- Fornari et al. (2019). Practicalities of graph-based models for Alzheimer's disease.
