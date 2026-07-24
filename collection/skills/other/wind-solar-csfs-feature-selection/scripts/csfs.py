"""
Cluster-based Sequential Feature Selection (CSFS) implementation
for renewable energy feature selection.
"""

import numpy as np
from sklearn.base import clone
from sklearn.model_selection import cross_val_score
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
import warnings
warnings.filterwarnings('ignore')


def cluster_features(X, method='hierarchical', linkage='ward', metric='correlation', t=0.5):
    """
    Cluster features based on similarity.
    
    Parameters:
    X: Feature matrix (n_samples, n_features)
    method: Clustering method ('hierarchical')
    linkage: Linkage criterion for hierarchical clustering
    metric: Distance metric ('correlation', 'euclidean', etc.)
    t: Threshold for forming flat clusters (for hierarchical)
    
    Returns:
    clusters: List of lists, where each sublist contains indices of features in that cluster
    """
    n_features = X.shape[1]
    
    if method == 'hierarchical':
        # Compute distance matrix
        if metric == 'correlation':
            # Compute correlation matrix and convert to distance
            corr_matrix = np.corrcoef(X.T)
            # Handle potential NaN values
            corr_matrix = np.nan_to_num(corr_matrix, nan=0.0)
            # Convert correlation to distance: d = 1 - |corr|
            distance_matrix = 1 - np.abs(corr_matrix)
            # Ensure diagonal is zero
            np.fill_diagonal(distance_matrix, 0)
        else:
            from sklearn.metrics import pairwise_distances
            distance_matrix = pairwise_distances(X.T, metric=metric)
        
        # Convert to condensed distance vector for linkage
        # Skip if distance matrix is all zeros (identical features)
        if np.allclose(distance_matrix, 0):
            # Each feature is its own cluster
            return [[i] for i in range(n_features)]
            
        # Check for invalid values in distance matrix
        if not np.all(np.isfinite(distance_matrix)):
            # Replace inf/nan with large value
            distance_matrix = np.nan_to_num(distance_matrix, nan=1e10, posinf=1e10, neginf=0)
            
        condensed_distance = squareform(distance_matrix, checks=False)
        
        # Perform hierarchical clustering
        try:
            Z = linkage(condensed_distance, method=linkage)
            # Form flat clusters
            cluster_labels = fcluster(Z, t=t, criterion='distance')
        except:
            # Fallback: each feature in its own cluster
            return [[i] for i in range(n_features)]
        
        # Group features by cluster label
        clusters = {}
        for i, label in enumerate(cluster_labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(i)
        
        return list(clusters.values())
    
    else:
        raise ValueError(f"Unsupported clustering method: {method}")


def sequential_forward_selection(X, y, estimator, cv=5, scoring='neg_mean_squared_error',
                                max_features=None):
    """
    Perform Sequential Forward Selection (SFS).
    
    Parameters:
    X: Feature matrix
    y: Target vector
    estimator: Sklearn-compatible estimator
    cv: Number of cross-validation folds
    scoring: Scoring metric
    max_features: Maximum number of features to select (None for all)
    
    Returns:
    selected_features: List of selected feature indices
    """
    n_features = X.shape[1]
    if max_features is None:
        max_features = n_features
    
    selected_features = []
    remaining_features = list(range(n_features))
    
    for _ in range(min(max_features, n_features)):
        best_score = -np.inf
        best_feature = None
        
        for feature in remaining_features:
            # Try adding this feature
            trial_features = selected_features + [feature]
            if len(trial_features) == 0:
                continue
                
            X_subset = X[:, trial_features]
            
            # Evaluate using cross-validation
            try:
                scores = cross_val_score(estimator, X_subset, y, cv=cv, scoring=scoring)
                mean_score = np.mean(scores)
            except:
                # If CV fails, use a simple train/test split on first 80%
                split_idx = int(0.8 * len(X))
                X_train, X_val = X_split[:split_idx], X_split[split_idx:]
                y_train, y_val = y[:split_idx], y[split_idx:]
                try:
                    estimator.fit(X_train, y_train)
                    score = estimator.score(X_val, y_val)
                    # For consistency with sklearn scoring, convert to negative MSE-like
                    if scoring == 'neg_mean_squared_error':
                        mean_score = -((y_val - estimator.predict(X_val)) ** 2).mean()
                    else:
                        mean_score = score
                except:
                    mean_score = -np.inf
            
            if mean_score > best_score:
                best_score = mean_score
                best_feature = feature
        
        if best_feature is None:
            break
            
        selected_features.append(best_feature)
        remaining_features.remove(best_feature)
    
    return selected_features


def cluster_based_sfs(X, y, estimator, clustering_method='hierarchical',
                     linkage='ward', metric='correlation', t=0.5,
                     cv=5, scoring='neg_mean_squared_error',
                     final_sfs=True):
    """
    Cluster-based Sequential Feature Selection (CSFS).
    
    Parameters:
    X: Feature matrix (n_samples, n_features)
    y: Target vector
    estimator: Sklearn-compatible estimator
    clustering_method: Method for clustering features
    linkage: Linkage criterion for hierarchical clustering
    metric: Distance metric for clustering
    t: Threshold for forming flat clusters
    cv: Number of cross-validation folds for SFS
    scoring: Scoring metric
    final_sfs: Whether to apply final SFS on cluster representatives
    
    Returns:
    selected_features: List of selected feature indices
    selected_X: Feature matrix with selected columns
    """
    # Step 1: Cluster features
    clusters = cluster_features(X, method=clustering_method, 
                               linkage=linkage, metric=metric, t=t)
    
    # Step 2: Within-cluster selection
    cluster_representatives = []
    for cluster in clusters:
        if len(cluster) == 0:
            continue
        elif len(cluster) == 1:
            # Single feature cluster - automatically select
            cluster_representatives.extend(cluster)
        else:
            # Multiple features - apply SFS within cluster
            X_cluster = X[:, cluster]
            selected_in_cluster = sequential_forward_selection(
                X_cluster, y, estimator, cv=cv, scoring=scoring
            )
            # Map back to original feature indices
            cluster_representatives.extend([cluster[i] for i in selected_in_cluster])
    
    # Step 3: Optional final SFS on representatives
    if final_sfs and len(cluster_representatives) > 1:
        X_representatives = X[:, cluster_representatives]
        final_selected = sequential_forward_selection(
            X_representatives, y, estimator, cv=cv, scoring=scoring
        )
        # Map back to original feature indices
        selected_features = [cluster_representatives[i] for i in final_selected]
    else:
        selected_features = cluster_representatives
    
    selected_features = sorted(selected_features)  # For consistent ordering
    selected_X = X[:, selected_features] if len(selected_features) > 0 else np.empty((X.shape[0], 0))
    
    return selected_features, selected_X


# Example usage function
def example_usage():
    """Example of how to use the CSFS function."""
    # This is just a template - replace with actual data loading
    print("CSFS module loaded. Use cluster_based_sfs() function with your data.")
    print("Example:")
    print("  selected_features, selected_X = cluster_based_sfs(X, y, estimator)")
    

if __name__ == "__main__":
    example_usage()