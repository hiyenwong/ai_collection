---
name: sc-taupath-alzheimer-tau-propagation
description: SC-TauPath framework for mapping tau propagation pathways in Alzheimer's disease using structural connectivity attribution. Combines Network Diffusion Model (NDM) with multilayer perceptron and gradient × input attribution to score SC edge contributions to tau prediction, generating multi-scale pathway maps validated against Braak staging anatomy.
version: 1.0.0
author: arxiv-2606.04066
arxiv_id: 2606.04066
date_created: 2026-06-06
source: arXiv q-bio.NC
category: neuroscience
keywords: Alzheimer's, tau propagation, structural connectivity, attribution, network diffusion model, Braak staging, gradient attribution, brain network
activation_keywords: Alzheimer's, tau propagation, structural connectivity, attribution framework, Braak staging, network diffusion, SC-TauPath
related_skills:
  - brain-network-analysis
  - alzheimer-prediction-fmri
  - neurodegenerative-disease
  - structural-functional-brain-gnn
---

# SC-TauPath: Structural Connectivity Attribution for Tau Propagation in Alzheimer's Disease

**arXiv: 2606.04066** | **Authors**: Jing Zhang, Norman Scheel, Minheng Chen, Tong Chen, Yanjun Lyu, David C. Zhu, Rong Zhang, Dajiang Zhu | **Date**: 2026-06-02

## Abstract

Understanding how structural connections are associated with tau propagation in Alzheimer's disease (AD) remains a central open question. Existing computational models either rely heavily on biophysical assumptions or lack neurobiologically interpretable pathway maps.

**SC-TauPath**: A structural connectivity (SC) attribution framework that maps tau propagation pathways from in vivo neuroimaging data. Combines Network Diffusion Model (NDM)-augmented multilayer perceptron with gradient × input attribution to score each SC edge's contribution to tau prediction, translating attribution scores into multi-scale pathway maps (backbone edges, high-traffic routes, and hub ROIs).

**Validation**: Applied to 234 ADNI participants with paired DTI SC and 18F-Flortaucipir PET, SC-TauPath achieves strong cross-validated tau prediction and yields attribution-based pathway maps consistent with established Braak staging anatomy, demonstrating that SC encodes spatially specific information about regional tau distribution in AD.

## Core Methodology

### 1. Network Diffusion Model (NDM) Integration

**Background**: Network diffusion models simulate tau protein spread through brain structural connections, modeling trans-synaptic propagation.

**NDM-Augmented MLP Architecture**:
- Input: Structural connectivity matrix from DTI
- Hidden layers: NDM-inspired diffusion dynamics
- Output: Regional tau distribution predictions

**Mathematical Framework**:
```
Tau propagation: dτ/dt = -ατ + βSC τ
where:
  τ = tau concentration vector
  SC = structural connectivity matrix
  α, β = diffusion parameters
```

### 2. Gradient × Input Attribution

**Attribution Mechanism**: Explainable AI approach to identify critical structural connectivity edges contributing to tau predictions.

**Implementation**:
```python
# Gradient × Input attribution
def gradient_input_attribution(model, SC_matrix, tau_target):
    # Forward pass
    tau_pred = model(SC_matrix)
    
    # Compute gradient w.r.t. SC matrix
    gradient = torch.autograd.grad(tau_pred, SC_matrix)
    
    # Attribution score: gradient × input
    attribution = gradient * SC_matrix
    
    # Edge-level contribution scores
    edge_scores = attribution.sum(dim=tuple(range(1, attribution.dim())))
    
    return edge_scores
```

**Key Innovation**: Translates gradient-based attribution into biologically interpretable pathway maps.

### 3. Multi-Scale Pathway Map Generation

**Three-Level Representation**:

1. **Backbone Edges**: Highest attribution SC connections
   - Critical pathways for tau spread
   - Identified as top-k edge scores

2. **High-Traffic Routes**: Aggregated pathway sequences
   - Multi-hop propagation paths
   - Summed edge attributions along routes

3. **Hub ROIs**: Regions with highest incoming/outgoing attribution
   - Key propagation nodes
   - Network hub identification

**Generation Process**:
```
SC Matrix → NDM-MLP → Tau Prediction → Gradient × Input Attribution → 
Edge Scores → Backbone Edges → High-Traffic Routes → Hub ROIs
```

## Key Findings

### Validation Against Braak Staging

**Braak Stages**: Established pathological progression pattern in AD:
- Stage I-II: Transentorhinal/entorhinal regions
- Stage III-IV: Limbic system (hippocampus, amygdala)
- Stage V-VI: Neocortical regions

**SC-TauPath Results**:
| Braak Stage | SC-TauPath Identified Regions | Match Rate |
|-------------|------------------------------|------------|
| I-II | Entorhinal, transentorhinal | **High** |
| III-IV | Hippocampus, amygdala, limbic | **High** |
| V-VI | Neocortex, temporal, frontal | **High** |

**Conclusion**: Attribution-based pathway maps validate against established Braak staging anatomy.

### Performance Metrics

**Dataset**: 234 ADNI participants
- DTI-derived structural connectivity (SC)
- 18F-Flortaucipir PET tau imaging

**Results**:
- Strong cross-validated tau prediction accuracy
- Biologically interpretable pathway maps
- Spatially specific SC-tau relationship identification

## Application Domains

### 1. Alzheimer's Disease Research

**Research Applications**:
- Tau propagation mechanism elucidation
- Structural connectivity role in AD progression
- Early-stage pathway identification
- Therapeutic target discovery

**Clinical Utility**:
- Disease staging support
- Progression prediction
- Treatment planning
- Biomarker identification

### 2. Neuroimaging Analysis

**Pipeline Integration**:
```yaml
sc_taupath_pipeline:
  input:
    - DTI structural connectivity
    - Tau PET imaging (optional)
  processing:
    - NDM-MLP prediction
    - Gradient attribution
    - Pathway map generation
  output:
    - Regional tau predictions
    - Backbone edges
    - High-traffic routes
    - Hub ROIs
  validation:
    - Braak staging comparison
    - Cross-validation
```

### 3. Network Neuroscience

**Brain Network Analysis**:
- Structural-functional connectivity integration
- Disease-specific network alterations
- Propagation dynamics modeling
- Hub identification in pathology

## Implementation Guidelines

### Step 1: Structural Connectivity Processing

**DTI Pipeline**:
```python
# SC matrix extraction
def extract_structural_connectivity(DTI_data):
    # Tractography generation
    tracts = tractography(DTI_data)
    
    # Region parcellation (e.g., AAL, Desikan-Killiany)
    regions = parcellate(tracts, atlas)
    
    # Connectivity matrix
    SC_matrix = count_connections(tracts, regions)
    
    # Normalization
    SC_normalized = normalize(SC_matrix, method='log')
    
    return SC_normalized
```

### Step 2: NDM-Augmented MLP Training

**Model Architecture**:
```python
class NDM_MLP(nn.Module):
    def __init__(self, n_regions, hidden_dims):
        super().__init__()
        # NDM-inspired diffusion layer
        self.diffusion = DiffusionLayer(n_regions)
        
        # MLP layers
        self.fc1 = nn.Linear(n_regions, hidden_dims[0])
        self.fc2 = nn.Linear(hidden_dims[0], hidden_dims[1])
        self.fc3 = nn.Linear(hidden_dims[1], n_regions)
        
    def forward(self, SC_matrix):
        # Diffusion dynamics
        x = self.diffusion(SC_matrix)
        
        # MLP prediction
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        tau_pred = self.fc3(x)
        
        return tau_pred
```

### Step 3: Attribution Score Extraction

**Gradient × Input Method**:
```python
def compute_attribution(model, SC_matrix, tau_target):
    # Ensure SC_matrix is a leaf tensor
    SC_tensor = torch.tensor(SC_matrix, requires_grad=True)
    
    # Forward pass
    tau_pred = model(SC_tensor)
    
    # Compute loss
    loss = F.mse_loss(tau_pred, tau_target)
    
    # Backward pass
    loss.backward()
    
    # Gradient × Input attribution
    attribution = SC_tensor.grad * SC_tensor
    
    # Edge-level scores
    edge_scores = attribution.abs()
    
    return edge_scores
```

### Step 4: Pathway Map Generation

**Multi-Scale Analysis**:
```python
def generate_pathway_maps(edge_scores, SC_matrix, threshold_percentile=95):
    # Backbone edges: top-percentile connections
    threshold = np.percentile(edge_scores, threshold_percentile)
    backbone_edges = np.where(edge_scores >= threshold)
    
    # High-traffic routes: multi-hop path aggregation
    routes = identify_propagation_paths(SC_matrix, backbone_edges)
    route_scores = aggregate_edge_scores(routes, edge_scores)
    
    # Hub ROIs: regions with highest attribution
    incoming_scores = edge_scores.sum(axis=0)
    outgoing_scores = edge_scores.sum(axis=1)
    hub_regions = identify_hubs(incoming_scores, outgoing_scores)
    
    return {
        'backbone_edges': backbone_edges,
        'high_traffic_routes': routes,
        'hub_rois': hub_regions
    }
```

## Integration with Existing Frameworks

### Neuroimaging Software

**Compatible Platforms**:
- FSL (DTI processing)
- FreeSurfer (brain parcellation)
- ANTs (image registration)
- SPM (PET analysis)
- Connectome Workbench (visualization)

### Deep Learning Frameworks

**Implementation**:
- PyTorch (model training, gradient computation)
- TensorFlow/Keras (alternative backend)
- NumPy/SciPy (connectivity analysis)
- NetworkX (graph pathway analysis)

### Brain Atlas Integration

**Supported Atlases**:
- AAL (Automated Anatomical Labeling)
- Desikan-Killiany-Tourville
- Harvard-Oxford
- Brainnetome
- HCP-MMP1 (Glasser et al.)

## Experimental Validation

### Dataset Description

**ADNI Cohort**:
- N = 234 participants
- Paired DTI and 18F-Flortaucipir PET
- Cross-sectional analysis
- Cross-validation methodology

**Imaging Protocols**:
- DTI: Diffusion-weighted MRI
- Tau PET: 18F-Flortaucipir tracer
- Standardized preprocessing pipelines

### Validation Strategy

**Braak Staging Comparison**:
- Pathology-established staging regions
- SC-TauPath pathway map comparison
- Qualitative match assessment
- Quantitative accuracy metrics

**Cross-Validation**:
- K-fold validation (k=5 or k=10)
- Tau prediction accuracy
- Attribution stability across folds
- Robustness to data splits

## Related Work

### Comparison with Existing Methods

| Method | Approach | Biophysical Assumptions | Pathway Interpretability |
|--------|----------|------------------------|--------------------------|
| Diffusion models | Physics-based | **High** (tau kinetics) | Moderate |
| Graph neural networks | Learning-based | Low | Moderate |
| **SC-TauPath** | **Attribution-based** | **Low** | **High (multi-scale)** |

### Extension Opportunities

1. **Temporal modeling**: Incorporate longitudinal tau progression data
2. **Multi-modal fusion**: Combine SC with functional connectivity (FC)
3. **Individualized predictions**: Subject-specific pathway maps
4. **Early-stage detection**: Predict tau spread before PET evidence

## Key Takeaways

### Core Insights

1. **Attribution-based interpretability**: Gradient × Input provides biologically meaningful pathway maps
2. **Braak validation**: Pathways match established pathological staging anatomy
3. **Low biophysical assumptions**: Learning-based approach reduces reliance on tau kinetics models
4. **Multi-scale representation**: Backbone edges, high-traffic routes, and hub ROIs

### Clinical Implications

1. **Tau propagation mechanisms**: Structural connectivity encodes tau spread information
2. **Disease staging support**: SC-TauPath pathway maps align with Braak stages
3. **Therapeutic targeting**: Identified backbone edges/routes as potential intervention points
4. **Early diagnosis**: Potential for predicting tau spread patterns

## Future Directions

### Research Extensions

1. **Longitudinal validation**: Track tau progression over time
2. **Multi-modal integration**: Combine with functional connectivity, amyloid PET
3. **Cognitive correlation**: Link pathway maps to cognitive decline patterns
4. **Treatment response**: Monitor pathway changes after therapeutic intervention

### Clinical Applications

1. **Diagnostic support**: Aid clinical staging decisions
2. **Prognosis prediction**: Forecast disease progression trajectories
3. **Personalized medicine**: Subject-specific pathway maps
4. **Drug development**: Identify propagation bottlenecks for intervention

## References

- arXiv:2606.04066 - Full paper
- Braak staging (Braak & Braak, 1991)
- Network diffusion models (Raj et al., 2012)
- Gradient attribution methods (Sundararajan et al., 2017)
- ADNI dataset (Mueller et al., 2005)

## Citation

```bibtex
@article{zhang2026sctaupath,
  title={SC-TauPath: A Structural Connectivity Attribution Framework for Mapping Tau Propagation Pathways in Alzheimer's Disease},
  author={Zhang, Jing and Scheel, Norman and Chen, Minheng and Chen, Tong and Lyu, Yanjun and Zhu, David C. and Zhang, Rong and Zhu, Dajiang},
  journal={arXiv preprint arXiv:2606.04066},
  year={2026}
}
```

---

**Skill Status**: Created from arXiv paper 2606.04066
**Next Update**: Integrate with longitudinal ADNI data
**Integration**: Combine with functional connectivity analysis frameworks