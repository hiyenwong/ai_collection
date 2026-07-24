# Cluster-based Sequential Feature Selection (CSFS) Methodology

## Overview

Cluster-based Sequential Feature Selection (CSFS) is a novel wrapper-based feature selection method designed to improve efficiency in feature selection for renewable energy prediction tasks. The method addresses two key challenges:

1. **High computational cost** of traditional wrapper methods like Sequential Forward Selection (SFS) when dealing with many features
2. **Multicollinearity** among environmental variables in renewable energy datasets

## Algorithm Details

### Step 1: Feature Clustering
- **Input**: Feature matrix X (n_samples × n_features)
- **Process**: 
  - Compute similarity/distance between features (typically using 1 - |correlation|)
  - Apply clustering algorithm (hierarchical clustering is recommended)
  - Determine optimal number of clusters using validity indices or domain knowledge
- **Output**: K feature clusters {C₁, C₂, ..., Cₖ}

### Step 2: Within-Cluster Selection
- **For each cluster Cᵢ**:
  - Extract submatrix Xᵢ containing only features in cluster Cᵢ
  - Apply Sequential Forward Selection (SFS) on Xᵢ
  - Select features that maximize cross-validated performance
  - Output: Representative features Rᵢ from cluster Cᵢ

### Step 3: Feature Aggregation and Refinement
- **Combine representatives**: R = ∪ᵢ Rᵢ
- **Optional refinement**: Apply SFS on the combined representative features
- **Output**: Final feature subset S

## Mathematical Formulation

Let X = [x₁, x₂, ..., xₙ] be the feature matrix where xⱼ is the j-th feature vector.

**Clustering Objective**: Partition features into K clusters to minimize within-cluster dissimilarity:
```
min Σᵢ₌₁ᴷ Σₓⱼ,ₓₖ∈Cᵢ d(xⱼ, xₖ)
```
where d(xⱼ, xₖ) is the distance between features xⱼ and xₖ.

**Within-Cluster Selection**: For each cluster Cᵢ, find subset Sᵢ ⊆ Cᵢ that maximizes:
```
J(Sᵢ) = E[performance(model trained on Xₛᵢ)]
```
where Xₛᵢ is the submatrix containing only features in Sᵢ.

## Advantages Over Traditional Methods

### Compared to Standard SFS:
- **Computational Complexity**: 
  - Standard SFS: O(n² × m × c) where n=features, m=samples, c=cost of model evaluation
  - CSFS: O(Σᵢ₌₁ᴷ |Cᵢ|² × m × c) + O(K² × m × c) 
  - Since Σ|Cᵢ| = n and typically |Cᵢ| << n, significant reduction when features form tight clusters

- **Handling Multicollinearity**: 
  - SFS may select multiple highly correlated features
  - CSFS encourages diversity by selecting representatives from different clusters

### Compared to Filter Methods:
- **Model-Specificity**: Wrapper methods like CSFS consider the specific predictor model
- **Feature Interactions**: Captures feature interactions through model performance
- **Optimality Guarantee**: Generally finds better-performing subsets than filter methods

## Parameter Selection Guidelines

### Clustering Parameters:
- **Distance Metric**: 
  - Correlation-based distance (1 - |corr|) works well for linear relationships
  - Euclidean distance for standardized features
  - Mutual information for non-linear dependencies
- **Linkage Criterion**: 
  - Ward's method minimizes variance within clusters (recommended)
  - Complete/linkage for compact clusters
  - Average/linkage for balanced clusters
- **Number of Clusters**: 
  - Use silhouette score, gap statistic, or domain knowledge
  - Typical range: √n to n/3 for n features

### SFS Parameters:
- **Cross-validation folds**: 5-10 folds recommended
- **Scoring Metric**: 
  - Regression: Negative MSE, R², MAE
  - Classification: Accuracy, F1-score, AUC
- **Stopping Criteria**: 
  - Maximum features (optional)
  - Performance improvement threshold

## Implementation Notes

### Handling Edge Cases:
- **Single feature clusters**: Automatically selected (no SFS needed)
- **Highly correlated features**: May result in selecting just one representative per cluster
- **Constant features**: Should be removed during preprocessing
- **Missing values**: Impute before clustering (correlation-based methods sensitive to NaN)

### Computational Optimization:
- Precompute distance/similarity matrix
- Use efficient clustering algorithms (scipy linkage is O(n²) memory)
- Parallelize SFS across clusters if needed
- Cache model evaluations when possible

## Extensions and Variations

### Hybrid Approaches:
- **Filter-Wrapper Hybrid**: Use filter methods for initial dimensionality reduction, then CSFS
- **Embedded Methods**: Combine with embedded feature selection (e.g., L1 regularization) within clusters

### Alternative Clustering:
- **Spectral clustering**: For non-convex cluster shapes
- **DBSCAN**: For automatic cluster number detection and outlier handling
- **Gaussian Mixture Models**: For probabilistic cluster assignments

### Multi-objective Optimization:
- Balance between performance and number of features
- Consider computational cost as explicit objective

## Validation and Evaluation

### Performance Metrics:
- **Prediction Accuracy**: Primary metric (comparable to SFS baseline)
- **Computational Efficiency**: Measure reduction in feature evaluations or runtime
- **Stability**: Feature selection stability across bootstrap samples
- **Interpretability**: Number and interpretability of selected features

### Statistical Significance:
- Use paired t-tests or Wilcoxon signed-rank tests to compare CSFS vs. baselines
- Report effect sizes alongside p-values
- Consider multiple comparison corrections when comparing many methods

## Practical Tips for Renewable Energy Applications

### Feature Engineering for Wind/Solar:
- **Temporal Features**: Hour of day, day of year, lagged variables
- **Weather Features**: Temperature, humidity, pressure, wind speed/direction, cloud cover
- **Satellite/Digital Elevation**: Terrain roughness, elevation, aspect
- **Plant Characteristics**: Turbine height, panel orientation, capacity

### Preprocessing Steps:
1. Remove features with near-zero variance
2. Handle missing values (interpolation or model-based imputation)
3. Consider feature transformations (log, Box-Cox) for skewed distributions
4. Standardize/normalize if using distance-based clustering

### Model Selection for Wrapper:
- Choose model that matches your final prediction goal
- Common choices: Random Forest, Gradient Boosting, Neural Networks, SVR
- Ensure model is compatible with selected evaluation metric

## References

[1] Grillmeyer, D., Hadry, M., Stenger, M., Borst, V., Lesch, V., et al. (2026). 
    Improving Wind and Solar Power Prediction with Efficient Wrapper-based Feature Selection: 
    An Empirical Study. arXiv:2607.14024v1.

[2] Guyon, I., & Elisseeff, A. (2003). An introduction to variable and feature selection. 
    Journal of Machine Learning Research, 3, 1157-1182.

[3] Kohavi, R., & John, G. H. (1997). Wrappers for feature subset selection. 
    Artificial Intelligence, 97(1-2), 273-324.

[4] Jain, A. K., Murty, M. N., & Flynn, P. J. (1999). Data clustering: a review. 
    ACM Computing Surveys (CSUR), 31(3), 264-323.

---