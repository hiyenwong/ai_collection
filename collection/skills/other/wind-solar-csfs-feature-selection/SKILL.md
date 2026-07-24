---
name: wind-solar-csfs-feature-selection
description: "Skill for applying Cluster-based Sequential Feature Selection (CSFS) to improve feature selection in wind and solar power prediction tasks. Use when working with renewable energy prediction datasets that have many environmental variables and need efficient, model-agnostic feature selection."
license: Complete terms in LICENSE.txt
---

# Wind and Solar Power Prediction with CSFS Feature Selection

This skill provides guidance for implementing Cluster-based Sequential Feature Selection (CSFS), a novel wrapper-based feature selection method that clusters similar features to reduce redundancy and improve efficiency in renewable energy forecasting.

## Overview

Cluster-based Sequential Feature Selection (CSFS) addresses the challenge of feature selection in wind and solar power prediction by grouping correlated environmental variables (e.g., temperature, humidity, wind speed) into clusters and performing sequential forward selection within each cluster. This reduces computational cost while maintaining predictive performance comparable to standard Sequential Forward Selection (SFS).

## Methodology

### Cluster-based Sequential Feature Selection (CSFS)

1. **Clustering Phase**: 
   - Apply a clustering algorithm (e.g., hierarchical clustering, k-means) to group input features based on similarity (e.g., correlation distance).
   - Determine optimal number of clusters using validity indices (e.g., silhouette score) or domain knowledge.

2. **Within-Cluster Selection**:
   - For each cluster, apply Sequential Forward Selection (SFS) to select the most representative feature(s).
   - SFS iteratively adds features that improve model performance the most, using a cross-validated score.

3. **Feature Aggregation**:
   - Combine selected features from all clusters to form the final feature subset.
   - Optionally, apply a final SFS step across cluster representatives to refine the selection.

### Advantages
- Reduces computational complexity by searching within smaller clusters.
- Mitigates multicollinearity by selecting diverse representatives.
- Model-agnostic: works with any regression/classification model.

## Usage Steps

1. **Prepare Dataset**:
   - Collect historical weather/power data with features like temperature, humidity, wind speed, solar irradiance, etc.
   - Ensure data is cleaned and normalized if required by your model.

2. **Apply Clustering**:
   - Use the provided script or your preferred clustering method to group similar features.
   - Example: hierarchical clustering with Ward linkage on correlation distance.

3. **Perform Within-Cluster Selection**:
   - For each cluster, run SFS using your target model (e.g., Random Forest, Neural Network).
   - Evaluate performance using cross-validated metric (e.g., RMSE for regression).

4. **Combine and Refine**:
   - Merge selected features from each cluster.
   - Optionally run a final SFS on the cluster representatives to refine the selection.

## When to Use This Skill

Use this skill when:
- Working with renewable energy datasets (wind/solar power prediction)
- Dataset contains many correlated environmental features
- Need efficient feature selection that reduces computational cost
- Want to maintain or improve prediction performance compared to exhaustive search methods
- Prefer model-agnostic feature selection approaches

## References

See `references/methodology.md` for detailed methodological explanation and `references/api_reference.md` for API documentation of the provided scripts.