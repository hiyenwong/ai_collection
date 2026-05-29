---
name: subcortical-shape-cognition-aging
description: Subcortical shape variations and their associations with cognition across the 8th decade of life using longitudinal data from Lothian Birth Cohort 1936
---

# Subcortical Shape Variations and Their Associations with Cognition Across the 8th Decade of Life

**arXiv**: 2605.29703
**Categories**: q-bio.NC (Neurons and Cognition)
**Date**: May 2026

## Background

The study of brain morphology changes in normal individuals may capture aspects of functionally-relevant brain aging not fully indicated by gross volumetry. Despite the important role of subcortical brain structures in cognition, the associations between their morphological trajectories and cognitive changes in aging have not been documented.

This research uses neuroimaging, demographic, and cognitive data from a large longitudinal study of cognitive aging — the **Lothian Birth Cohort 1936** — to explore shape changes in subcortical structures and their cognitive correlates.

## Methodology

### Study Design

**Dataset**: Lothian Birth Cohort 1936 (LBC1936)
- Participants born in 1936, tested at ages ~70, ~73, ~76, ~79
- Longitudinal follow-up across 8th decade of life (70-79 years)
- Comprehensive cognitive testing + neuroimaging

### Shape Analysis Approach

1. **Subcortical Structure Segmentation**
   - Target structures: hippocampus, amygdala, thalamus, caudate, putamen, pallidum
   - High-resolution MRI-based segmentation
   - Shape modeling using surface meshes

2. **Shape Variation Quantification**
   - Point-wise surface displacement analysis
   - Statistical shape modeling (PCA-based)
   - Regional deformation patterns

3. **Cognitive Association Analysis**
   - Cognitive domains: memory, processing speed, executive function
   - Correlation of shape changes with cognitive trajectories
   - Mixed-effects models for longitudinal data

### Key Innovations

- **Shape vs. Volume**: Morphological changes capture subtle aging patterns lost in volumetry
- **Longitudinal Design**: 9-year trajectory analysis, not cross-sectional
- **Regional Specificity**: Identifies WHERE in each structure changes matter
- **Cognitive Linking**: Direct associations with specific cognitive domains

## Key Findings

### Morphological Trajectories

1. **Non-uniform shape changes**: Different subcortical regions age differently
2. **Anterior-posterior gradients**: Some structures show directional aging patterns
3. **Heterogeneity**: Inter-individual variation in shape trajectories

### Cognitive Associations

1. **Hippocampal head** changes linked to memory performance
2. **Thalamic regions** associated with processing speed
3. **Caudate shape** correlates with executive function
4. **Amygdalar morphology** linked to emotional regulation

### Clinical Implications

- Shape metrics may predict cognitive decline earlier than volume
- Regional specificity improves diagnostic precision
- Normative aging trajectories established

## Applications

### Use Cases

- **Brain aging assessment**: Shape-based biomarkers for cognitive health
- **Alzheimer's risk prediction**: Subcortical shape as early indicator
- **Longitudinal monitoring**: Tracking individual aging trajectories
- **Cognitive intervention targets**: Identifying vulnerable regions
- **Normative database**: Reference for aging studies

### Triggers

- Subcortical morphology, brain aging, cognitive decline
- Shape analysis, longitudinal neuroimaging
- Hippocampus, thalamus, caudate, amygdala
- Lothian Birth Cohort, aging trajectories

## Pitfalls

### Limitations

1. **Age range limited**: 8th decade only (70-79), younger/older needs study
2. **Cohort-specific**: LBC1936 may not generalize to other populations
3. **Shape analysis complexity**: Requires specialized expertise/tools
4. **MRI resolution limits**: Subvoxel precision unattained

### Methodological Considerations

- Shape registration accuracy critical
- Segmentation quality affects downstream analysis
- Longitudinal alignment must account for scanner drift
- Multiple comparison corrections needed for regional analyses

### Edge Cases

- Atypical aging trajectories → may deviate from normative patterns
- Structural abnormalities → shape analysis may misinterpret pathology
- High inter-individual variance → statistical power challenges

## References

- Paper: https://arxiv.org/abs/2605.29703
- Related: [[brain-morphology-aging]], [[subcortical-cognition]]
- Dataset: Lothian Birth Cohort 1936
- See also: [[alzheimer-pet-suvr-network-models]], [[brain-network-controllability]]