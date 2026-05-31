---
name: subcortical-shape-cognition-aging
description: "Subcortical shape variations and their associations with cognition across the 8th decade of life. Longitudinal study using neuroimaging and cognitive data from Lothian Birth Cohort 1936. Analyzes heterogeneous morphological trajectories in hippocampus, thalami, globus pallidi, and ventral DC. Uses ANCOVA and mixed linear model analyses to investigate vertex displacement patterns associated with cognitive aging. Use when studying brain morphology changes, subcortical shape analysis, cognitive aging, longitudinal neuroimaging, or vertex-based morphometry."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.29703"
  published: "2026-05-28"
  authors: "Maria del C. Valdes-Hernandez, Wonjung Park, Joanna Moodie, Susana Muñoz Maniega, Janie Corley, Fraser N. Sneden, Mark E. Bastin, Joanna M. Wardlaw, Simon R. Cox, Jinah Park"
  tags: [subcortical, morphology, shape-analysis, cognitive-aging, longitudinal, vertex-displacement, hippocampus, thalamus, neuroimaging]
---

# Subcortical Shape Variations and Cognition Across Aging

Methodology from **"Subcortical Shape Variations and Their Associations with Cognition Across the 8th Decade of Life. A Study in the Lothian Birth Cohort 1936"** (arXiv:2605.29703).

## Overview

This methodology provides **longitudinal shape analysis** of subcortical brain structures across aging, revealing:

1. **Heterogeneous atrophy patterns**: Different subcortical structures show distinct morphological deformation trajectories
2. **Left-right asymmetry**: Hippocampus and ventral DC show hemisphere-specific patterns
3. **Cognition-morphology association**: Vertex displacements correlate with cognitive changes

**Key insight**: Shape changes capture functionally-relevant brain aging beyond gross volumetry.

## Study Design

### Lothian Birth Cohort 1936

**Unique longitudinal dataset**:
- Community-dwelling individuals (age ~70-80 across study)
- Multiple neuroimaging timepoints
- Detailed cognitive assessments
- Demographic and lifestyle data

**Advantages**:
- Same birth year → Controls for developmental cohort effects
- High retention rate → Longitudinal tracking feasible
- Rich phenotyping → Multivariate analysis possible

### Analysis Approach

**Two-stage methodology**:

1. **Shape quantification**: Vertex-based morphometry of subcortical structures
2. **Association testing**: ANCOVA and mixed linear models linking shape changes to cognition

## Core Methodology

### Vertex-Based Morphometry

**Shape representation**:
- Surface meshes for each subcortical structure
- Vertex coordinates define shape
- **Vertex displacement**: Movement of surface points from baseline

**Key structures analyzed**:
- Hippocampus (memory encoding)
- Thalamus (sensory relay, consciousness)
- Globus pallidus (motor control)
- Ventral DC (dorsal striatum, motor/cognitive)

### Measurement Pipeline

**Workflow**:

```python
# Conceptual framework for shape analysis

def longitudinal_shape_analysis(scan_baseline, scan_followup, structure_name):
    """
    Analyze shape changes in subcortical structure across timepoints
    """
    # 1. Segmentation
    structure_baseline = segment_subcortical(scan_baseline, structure_name)
    structure_followup = segment_subcortical(scan_followup, structure_name)
    
    # 2. Surface extraction
    mesh_baseline = extract_surface(structure_baseline)
    mesh_followup = extract_surface(structure_followup)
    
    # 3. Vertex correspondence
    # Match vertices across timepoints (same anatomical location)
    matched_vertices = establish_correspondence(mesh_baseline, mesh_followup)
    
    # 4. Displacement calculation
    # Vector from baseline to followup position
    displacements = calculate_vertex_displacement(matched_vertices)
    
    # 5. Shape statistics
    # Magnitude, direction, regional patterns
    displacement_stats = analyze_displacement_patterns(displacements)
    
    return displacements, displacement_stats
```

### Statistical Analysis

**ANCOVA framework**:

```
Shape_change ~ Cognitive_score + Age + Sex + Education + covariates
```

**Mixed linear models**:

```
Vertex_displacement ~ Time + Cognitive_trajectory + Random(Subject)
```

**Key comparisons**:
- Between-subject: Individual differences in shape trajectories
- Within-subject: Time-dependent shape changes
- Structure-specific: Different patterns for hippocampus vs thalamus vs globus pallidus

## Key Findings

### Heterogeneous Atrophy Patterns

**Structure-specific deformations**:

1. **Hippocampus and ventral DC**:
   - Varied morphological deformations
   - **Left-right asymmetry**: Different patterns in each hemisphere
   - Region-specific inward/outward movements

2. **Thalami and globus pallidi**:
   - More uniform volume contraction
   - **Symmetrical**: Nearly identical patterns in left and right
   - Global shrinkage rather than focal deformation

**Implication**: Not all subcortical structures age uniformly—shape analysis reveals hidden heterogeneity.

### Cognitive Associations

**Vertex-cognition links**:

- **General cognition**: Associated with inward/outward vertex displacements between timepoints
- **Direction matters**: Expansion vs contraction linked to different cognitive domains
- **Regional specificity**: Certain vertex clusters show stronger cognitive correlations

**Interpretation**:
- Shape changes capture functionally-relevant aging
- Morphological trajectories may predict cognitive decline
- Targeted analysis of deformation patterns improves understanding beyond volume alone

## Implementation Guide

### Step 1: Image Processing

**Required tools**:
- Segmentation: FSL FIRST, FreeSurfer, or manual delineation
- Surface extraction: Mesh generation from binary masks
- Correspondence: Point-set registration algorithms

**Quality control**:
- Visual inspection of segmentation accuracy
- Consistency check across timepoints (same structure labeled)
- Outlier detection for extreme displacements

### Step 2: Shape Quantification

**Vertex displacement calculation**:

```python
import numpy as np

def calculate_displacement(mesh_baseline, mesh_followup):
    """
    Calculate vertex displacement vectors
    """
    n_vertices = len(mesh_baseline.vertices)
    
    # Initialize displacement array
    displacements = np.zeros((n_vertices, 3))  # x, y, z components
    
    for i in range(n_vertices):
        # Baseline position
        p_baseline = mesh_baseline.vertices[i]
        
        # Followup position (same anatomical location)
        p_followup = mesh_followup.vertices[i]  # Assumes correspondence
        
        # Displacement vector
        displacements[i] = p_followup - p_baseline
    
    return displacements

def displacement_statistics(displacements):
    """
    Calculate shape change metrics
    """
    magnitudes = np.linalg.norm(displacements, axis=1)
    
    # Global metrics
    mean_displacement = np.mean(magnitudes)
    std_displacement = np.std(magnitudes)
    
    # Regional clustering (group nearby vertices)
    # Apply k-means or anatomical parcellation
    
    return mean_displacement, std_displacement
```

### Step 3: Association Testing

**Cognitive correlation**:

```python
from statsmodels.formula.api import mixedlm

def shape_cognition_association(displacements, cognitive_scores, covariates):
    """
    Test association between vertex displacement and cognition
    """
    # Magnitude of displacement
    displacement_magnitude = np.linalg.norm(displacements, axis=1)
    
    # Mixed linear model
    # Random intercept for subject (repeated measures)
    model = mixedlm(
        "displacement_magnitude ~ cognitive_score + age + sex",
        data=dataframe,
        groups=dataframe['subject_id']
    )
    
    result = model.fit()
    
    return result
```

### Step 4: Visualization

**Shape deformation maps**:

```python
def visualize_shape_changes(mesh, displacements):
    """
    Plot displacement vectors on surface mesh
    """
    # Color vertices by displacement magnitude
    magnitudes = np.linalg.norm(displacements, axis=1)
    
    # Plot surface with displacement arrows
    plot_mesh_with_vectors(mesh, displacements, color_by=magnitudes)
    
    # Show inwards (contraction) vs outwards (expansion)
    inward_mask = magnitudes < threshold
    outward_mask = magnitudes > threshold
    
    return visualization
```

## Applications

### Aging Research

**Longitudinal tracking**:
- Monitor subcortical shape trajectories across decades
- Detect early morphological changes before clinical symptoms
- Identify individuals at risk for cognitive decline

**Clinical translation**:
- Shape markers as early biomarkers for Alzheimer's, Parkinson's
- Target regions for intervention (e.g., hippocampal preservation)

### Neuroimaging Methodology

**Beyond volumetry**:
- Gross volume measures miss regional heterogeneity
- Shape analysis captures nuanced morphological changes
- Vertex-based approach enables high-resolution spatial mapping

**Other applications**:
- Developmental studies (brain shape maturation)
- Disease progression tracking
- Treatment response monitoring

## Pitfalls

### Methodological Challenges

1. **Vertex correspondence**: Establishing consistent vertex matching across timepoints is critical
   - Solution: Use surface registration algorithms (SPHARM-PDM, spherical harmonics)
   - Alternative: Statistical shape models (SSM) with built-in correspondence

2. **Segmentation accuracy**: Errors propagate to shape analysis
   - Solution: Visual QC, multi-atlas segmentation, manual correction where needed

3. **Multiple comparisons**: Thousands of vertices → multiple testing burden
   - Solution: Cluster-based correction, ROI-focused analysis, permutation testing

4. **Confounding factors**: Age, sex, education, vascular health affect shape
   - Solution: Include as covariates in statistical models

### Interpretation Issues

1. **Direction meaning**: Inward displacement ≠ atrophy necessarily (could be displacement from surrounding tissue)
   - Solution: Consider global volume change alongside local displacement

2. **Asymmetry significance**: Left-right differences may reflect functional specialization or noise
   - Solution: Test statistical significance of asymmetry metrics

3. **Causality**: Shape changes and cognition association is correlational
   - Solution: Longitudinal design helps infer temporal precedence

## Statistical Power

**Sample size considerations**:
- Lothian Birth Cohort: N ~ 100s with multiple timepoints
- Vertex-level analysis: Requires sufficient power for thousands of tests
- Cluster-based approach: Reduces multiple testing penalty

**Effect sizes**:
- Subcortical shape changes are subtle (mm-level displacements)
- Cognitive associations moderate (partial correlations ~0.2-0.4)
- Longitudinal tracking reveals cumulative effects

## Cross-References

- **brain-mri-foundation-clinical**: Clinical deployment of brain MRI foundation models
- **geosae-brain-mri-sae**: Interpretable brain MRI foundation models
- **brain-segmentation-active-learning**: Active learning for brain segmentation

## References

- Valdes-Hernandez, M. C., Park, W., Moodie, J., et al. (2026). Subcortical Shape Variations and Their Associations with Cognition Across the 8th Decade of Life. arXiv:2605.29703
- FSL FIRST: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST
- FreeSurfer Subcortical Segmentation: https://surfer.nmr.mgh.harvard.edu/

## Activation Keywords

- subcortical shape
- vertex morphometry
- longitudinal neuroimaging
- cognitive aging
- hippocampus morphology
- thalamus shape
- brain aging
- vertex displacement
- shape trajectory